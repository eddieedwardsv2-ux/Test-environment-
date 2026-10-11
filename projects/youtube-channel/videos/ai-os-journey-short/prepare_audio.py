"""Stage 1/2: synthesise locked narration; measure and cut provider padding.
Run in a scratch environment with edge-tts, ffmpeg and ffprobe. No keys or paid API.
"""
import asyncio, json, math, pathlib, re, subprocess, time
import edge_tts

ROOT=pathlib.Path(__file__).resolve().parent
LINES=[
"I started with a phone and a lot of questions. Could I build my own AI operating system without coding?",
"First, I learned the parts: a model to think, tools to act, skills to guide it, and saved context.",
"Then I built a Router. New information goes to the right specialist. I call these specialists my Elders.",
"The Router points the way. It loads the useful context, instead of dumping every note into every answer.",
"I stay the Chief. Small, reversible jobs can move ahead. Real choices come to my Desk, where I decide.",
"The Quartermaster helps pick the tools. The Architect helps organise the system. Their work becomes something I can use.",
"But a confident answer isn't proof. We plant faults and check the result. I'm still proving the foundations work.",
"Next, help a friend build their own system, and document it. One useful step at a time."]
def run(*args): return subprocess.run(args,check=True,capture_output=True,text=True)
async def main():
    started=time.monotonic(); (ROOT/'audio').mkdir(exist_ok=True)
    ledger=[]; cursor=0.0; all_words=[]
    for i,line in enumerate(LINES):
        raw=ROOT/f'audio/take-{i+1:02}.mp3'; wav=ROOT/f'audio/scene-{i+1:02}.wav'
        events=[]
        # Word boundary mode grounds caption timing in TTS metadata, not estimates.
        communicate=edge_tts.Communicate(line,'en-GB-RyanNeural',boundary='WordBoundary')
        with raw.open('wb') as f:
            async for e in communicate.stream():
                if e['type']=='audio': f.write(e['data'])
                elif e['type']=='WordBoundary': events.append(e)
        duration=float(json.loads(run('ffprobe','-v','error','-show_entries','format=duration','-of','json',str(raw)).stdout)['format']['duration'])
        log=run('ffmpeg','-hide_banner','-i',str(raw),'-af','silencedetect=noise=-42dB:d=0.08','-f','null','-').stderr
        starts=[float(x) for x in re.findall(r'silence_start: ([0-9.]+)',log)]
        ends=[float(x) for x in re.findall(r'silence_end: ([0-9.]+)',log)]
        # Only remove outer silence, keeping 60ms head and 120ms tail for consonants.
        trim_start=max(0,ends[0]-0.06) if starts and starts[0]<0.03 and ends else 0
        trim_end=min(duration,starts[-1]+0.12) if starts and ends and ends[-1]>duration-0.05 else duration
        cut_duration=trim_end-trim_start
        # Snap each scene to a full video frame, intentional <=33ms tail pad.
        scene_duration=math.ceil((cut_duration+0.12)*30)/30
        run('ffmpeg','-hide_banner','-loglevel','error','-y','-i',str(raw),'-af',f'atrim=start={trim_start}:end={trim_end},asetpts=PTS-STARTPTS,afade=t=in:d=0.008,afade=t=out:st={max(0,cut_duration-.018)}:d=0.018,apad,atrim=duration={scene_duration}', '-ar','48000','-ac','1',str(wav))
        words=[{'text':e['text'],'start':max(cursor,cursor+e['offset']/1e7-trim_start),'end':min(cursor+scene_duration,cursor+(e['offset']+e['duration'])/1e7-trim_start)} for e in events]
        all_words+=words
        ledger.append({'scene':i+1,'line':line,'start':round(cursor,6),'duration':scene_duration,'end':round(cursor+scene_duration,6),'raw_duration':duration,'trim_start':trim_start,'trim_end':trim_end,'removed_seconds':duration-cut_duration,'words':words,'silence_log':log})
        cursor+=scene_duration
    (ROOT/'audio/concat.txt').write_text(''.join(f"file 'scene-{i+1:02}.wav'\n" for i in range(len(LINES))))
    run('ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(ROOT/'audio/concat.txt'),'-af','loudnorm=I=-16:TP=-1.5:LRA=7','-ar','48000',str(ROOT/'narration.wav'))
    result={'voice':'en-GB-RyanNeural','synthetic':True,'stage_order':['transcribe/timing','cut'],'elapsed_seconds':round(time.monotonic()-started,3),'duration':cursor,'words':all_words,'scenes':ledger}
    (ROOT/'timed-source.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'duration':cursor,'seconds_removed':sum(s['removed_seconds'] for s in ledger),'elapsed_seconds':result['elapsed_seconds'],'words':len(all_words)}))
asyncio.run(main())
