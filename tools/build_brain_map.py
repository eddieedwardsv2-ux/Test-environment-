"""Builds research/nate-herk/brain/map/brain-map.html from concepts.md and rules.md.
Run after the brain changes: python3 tools/build_brain_map.py
Review marks live in the published page's "flags" database, not in this file."""
import re, json, html, sys
B = "/home/user/test-environment-/research/nate-herk/brain/"
GH = "https://github.com/eddieedwardsv2-ux/test-environment-/blob/main/research/nate-herk/"
REFS = {"os": "../steal-my-exact-ai-os-setup-5-simple-tips--Ek1NBfnnTH0-transcript.md",
        "kb": "../i-built-another-andrej-karpathy-using-claude--bvGptCLDhyo-transcript.md"}
def url(u):
    if u.startswith("http"): return u
    if u.startswith("../"): return GH + u[3:]
    return GH + "brain/" + u
def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\[([^\]]+)\]\[(\w+)\]', lambda m: f'[{m.group(1)}]({REFS.get(m.group(2),"")})', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: f'<a href="{url(m.group(2))}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', s)
    return s
def blocks(lines):
    out=[]
    for l in lines:
        l=l.rstrip()
        if not l or l=="---": continue
        if l.startswith(">"): out.append({"t":"q","h":inline(l.lstrip("> ").strip())})
        elif l.startswith("**Agent check:**"): out.append({"t":"check","h":inline(l[len("**Agent check:**"):].strip())})
        elif l.startswith("**Used by:**"): continue
        else: out.append({"t":"p","h":inline(l)})
    return out
# concepts
cl = open(B+"concepts.md").read().split("\n")
concepts=[]; section=None; cur=None
for l in cl:
    if l.startswith("## Limits"): break
    m=re.match(r'^## ([A-H])\. (.*)',l)
    if m: section={"id":m.group(1),"title":m.group(2)}; continue
    m=re.match(r'^\*\*(\d+)\. (.*)\*\*$',l)
    if m:
        cur={"n":int(m.group(1)),"title":m.group(2),"sec":section["id"],"secTitle":section["title"],"lines":[],"rules":[]}
        concepts.append(cur); continue
    if cur is not None:
        if l.startswith("**Used by:**"):
            cur["rules"]=[int(x) for x in re.findall(r'Rule (\d+)',l)]
            if not cur["rules"]: cur["note"]=inline(l[len("**Used by:**"):].strip())
        cur["lines"].append(l)
for c in concepts: c["body"]=blocks(c.pop("lines"))
# rules
rl = open(B+"rules.md").read().split("\n")
rules=[]; cur=None
for l in rl:
    if l.startswith("## Inferring"): break
    m=re.match(r'^\*\*Rule (\d+): (.*?)\*\*\s*(\((.*)\))?\s*$',l)
    if m:
        cur={"n":int(m.group(1)),"title":m.group(2),"conf":m.group(4) or "","lines":[],"concepts":[]}
        rules.append(cur); continue
    if cur is not None:
        for g in re.findall(r'\(Concepts? ([\d, and]+)\)',l):
            cur["concepts"]+= [int(x) for x in re.findall(r'\d+',g)]
        cur["lines"].append(l)
for r in rules:
    r["body"]=blocks(r.pop("lines"))
# union links
for c in concepts:
    for rn in c["rules"]:
        r=next((x for x in rules if x["n"]==rn),None)
        if r and c["n"] not in r["concepts"]: r["concepts"].append(c["n"])
for r in rules:
    for cn in r["concepts"]:
        c=next((x for x in concepts if x["n"]==cn),None)
        if c and r["n"] not in c["rules"]: c["rules"].append(r["n"])
    r["concepts"].sort()
for c in concepts: c["rules"].sort()
print(len(concepts),len(rules),file=sys.stderr)
print("orphan rules",[r["n"] for r in rules if not r["concepts"]],file=sys.stderr)
print("orphan concepts",[c["n"] for c in concepts if not c["rules"]],file=sys.stderr)
T=B+"map/template.html"; out=B+"map/brain-map.html"
open(out,"w").write(open(T).read().replace("__DATA__", json.dumps({"concepts":concepts,"rules":rules},ensure_ascii=False).replace("</","<\\/")))
print("wrote",out,file=sys.stderr)
