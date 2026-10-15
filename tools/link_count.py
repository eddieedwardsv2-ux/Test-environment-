"""Count note links, backlinks and orphans in a folder of Markdown notes.
Use: python3 tools/link_count.py <folder>. Counts [md](links), `path.md` mentions and [[wiki links]].
Made 15 Oct 2026 for the second-brain-os test (projects/second-brain-test/)."""
import re,os,sys
root=sys.argv[1] if len(sys.argv)>1 else '.'
os.chdir(root)
files=[os.path.join(d,f)[2:] for d,_,fs in os.walk('.') if '.git' not in d for f in fs if f.endswith('.md')]
S=set(files);out={};inn={}
for f in files:
    t=open(f,errors='ignore').read()
    for m in re.findall(r'\]\(([^)#\s]+\.md)|`([\w./-]+\.md)`|\[\[([^\]|#]+)',t):
        tgt=next(x for x in m if x)
        for c in [os.path.normpath(os.path.join(os.path.dirname(f),tgt)),os.path.normpath(tgt),os.path.normpath(tgt+'.md')]:
            if c in S and c!=f: out.setdefault(f,set()).add(c);inn.setdefault(c,set()).add(f);break
links=sum(len(v) for v in out.values())
orph=[f for f in files if f not in inn and f not in out]
print(f"notes {len(files)} | links {links} | per note {links/len(files):.1f} | notes with a backlink {len(inn)} ({100*len(inn)//len(files)}%) | orphans {len(orph)} ({100*len(orph)//len(files)}%)")
