"""Checks actual encoded video, not the animation plan; prepares visual evidence."""
import hashlib,json,pathlib,re,subprocess,sys,os
from PIL import Image,ImageDraw
r=pathlib.Path(__file__).resolve().parent
video=r/'charlie-ai-os-journey-short-final.mp4'
out=r/'evidence';out.mkdir(exist_ok=True)
def run(*args):return subprocess.run(args,capture_output=True,text=True)
probe=run('ffprobe','-v','error','-show_streams','-show_format','-of','json',str(video));assert probe.returncode==0
info=json.loads(probe.stdout);v=next(s for s in info['streams'] if s['codec_type']=='video');a=next(s for s in info['streams'] if s['codec_type']=='audio')
assert (v['width'],v['height'])==(1080,1920) and v['codec_name']=='h264' and a['codec_name']=='aac'
assert abs(float(v['duration'])-float(a['duration']))<.2
decoded=run('ffmpeg','-v','error','-i',str(video),'-f','null','-');assert decoded.returncode==0 and not decoded.stderr.strip()
audio=run('ffmpeg','-hide_banner','-i',str(video),'-af','silencedetect=noise=-42dB:d=0.8,ebur128=peak=true','-f','null','-');assert audio.returncode==0
(out/'audio-analysis.txt').write_text(audio.stderr)
revision=int(os.environ.get('JOURNEY_REVISION','5'))
caps=json.loads((r/f'captions-r{revision}.json').read_text()); source=json.loads((r/'aligned-source.json').read_text())
assert sum(len(c['text'].split()) for c in caps)==149
assert max(len(c['text'].split()) for c in caps)<=5 and max(len(c['text']) for c in caps)<=32
assert all(x['end']<=y['start']+.000001 for x,y in zip(caps,caps[1:]))
clean=' '.join(s['line'] for s in source['scenes']); cc=' '.join(c['text'] for c in caps)
assert re.sub(r'\s+',' ',clean)==re.sub(r'\s+',' ',cc)
times=[i*.5 for i in range(int(float(info['format']['duration'])*2)+1)]
times=sorted(set(times+[max(0,s['start']-.05) for s in source['scenes'][1:]]+[s['start']+.05 for s in source['scenes']]+[57.65]))
thumbs=[]
for i,t in enumerate(times):
    frame=out/f'sampled-{i:03}.jpg'
    f=run('ffmpeg','-v','error','-y','-ss',str(t),'-i',str(video),'-frames:v','1','-vf','scale=240:426',str(frame));assert f.returncode==0 and frame.exists()
    thumbs.append((t,frame))
for page in range((len(thumbs)+15)//16):
    sheet=Image.new('RGB',(960,1824),'#05070d');d=ImageDraw.Draw(sheet)
    for j,(t,frame) in enumerate(thumbs[page*16:(page+1)*16]):
        sheet.paste(Image.open(frame),(j%4*240,j//4*456));d.text((j%4*240+8,j//4*456+431),f'{t:.3f}s',fill='white')
    sheet.save(out/f'final-sequence-{page+1:02}.jpg',quality=88)
for i,s in enumerate(source['scenes']):
    t=s['start']+s['duration']*.90
    f=run('ffmpeg','-v','error','-y','-ss',str(t),'-i',str(video),'-frames:v','1','-vf','scale=390:694',str(out/f'final-phone-{i+1:02}.jpg'));assert f.returncode==0
report={'video_sha256':hashlib.sha256(video.read_bytes()).hexdigest(),'probe':info,'full_decode':{'exit_code':decoded.returncode,'stderr':decoded.stderr},'caption_words':149,'caption_count':len(caps),'caption_max_words':max(len(c['text'].split()) for c in caps),'caption_max_chars':max(len(c['text']) for c in caps),'caption_overlap_count':0,'all_authored_words_preserved':True,'inspection_times':times,'inspection_frames':len(times),'loudness_summary':audio.stderr[audio.stderr.rfind('Summary:'):],'silence_events':[line.strip() for line in audio.stderr.splitlines() if 'silence_' in line]}
(out/'measurements.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['probe','inspection_times']}))
