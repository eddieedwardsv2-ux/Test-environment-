"""Independently recognise the final clean audio; do not fake ASR from script."""
import difflib,json,pathlib,re,time,sys
from faster_whisper import WhisperModel
root=pathlib.Path(__file__).resolve().parent
start=time.monotonic()
model=WhisperModel('small',device='cpu',compute_type='int8')
audio=root/(sys.argv[1] if len(sys.argv)>1 else 'narration.wav')
report_file=root/(sys.argv[2] if len(sys.argv)>2 else 'speech-check.json')
segments,info=model.transcribe(str(audio),language='en',word_timestamps=True,vad_filter=True,condition_on_previous_text=False)
rows=[]; words=[]
for s in segments:
    rows.append({'start':s.start,'end':s.end,'text':s.text})
    words.extend({'start':w.start,'end':w.end,'text':w.word.strip(),'probability':w.probability} for w in s.words)
source=json.loads((root/'timed-source.json').read_text())
norm=lambda s:re.sub('[^a-z0-9]','',s.lower())
expected=[norm(w['text']) for w in source['words']]
actual=[norm(w['text']) for w in words]
matching=difflib.SequenceMatcher(None,expected,actual,autojunk=False)
report={'model':'faster-whisper small / cpu int8','elapsed_seconds':time.monotonic()-start,'segments':rows,'words':words,'expected_words':len(expected),'asr_words':len(actual),'similarity':matching.ratio(),'differences':[{'kind':tag,'expected':expected[a:b],'heard':actual[c:d]} for tag,a,b,c,d in matching.get_opcodes() if tag!='equal']}
report['audio_file']=audio.name
report_file.write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k not in ['segments','words']}))
