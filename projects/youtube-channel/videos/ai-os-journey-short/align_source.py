"""Final caption clock uses independent Whisper words on the cut narration."""
import json,pathlib,re
r=pathlib.Path(__file__).resolve().parent
source=json.loads((r/'timed-source.json').read_text())
asr=json.loads((r/'speech-check.json').read_text())
assert asr['similarity']>=.90
authored=[w for s in source['scenes'] for w in s['line'].split()]
assert len(authored)==len(asr['words'])==149
norm=lambda s:re.sub('[^a-z0-9]','',s.lower()).replace('organize','organise')
for expected,heard in zip(authored,asr['words']):
    assert norm(expected)==norm(heard['text']), (expected,heard)
flat=[]; index=0
for s in source['scenes']:
    out=[]
    for _ in s['line'].split():
        w=asr['words'][index]; text=authored[index]; index+=1
        # Clamp to the frame-snapped scene; Whisper can place a boundary 30ms past a cut.
        out.append({'text':text,'start':max(s['start'],w['start']),'end':min(s['end'],w['end'])})
    s['words']=out; flat+=out
source['words']=flat; source['caption_clock']='faster-whisper small on final cut narration'; source['caption_word_count']=len(flat)
(r/'aligned-source.json').write_text(json.dumps(source,indent=2))
print('149/149 authored words aligned to independently recognised speech')
