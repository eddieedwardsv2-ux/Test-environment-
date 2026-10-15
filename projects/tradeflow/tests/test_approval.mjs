// Checks the approval rules using the page's own statusOf and hashOf:
// a complete job starts as a draft, approving makes it approved, any priced change
// voids that approval (old version kept), and a re-approval becomes the next version.
import {readFileSync} from "node:fs";
import {dirname, join} from "node:path";
import {fileURLToPath} from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, "../quote-lab/quote-lab.html"), "utf8");
const pricing = html.split("// ==PRICING START==")[1].split("// ==PRICING END==")[0];
const grab = re => { const m = html.match(re); if (!m) throw new Error("not found: " + re); return m[0]; };
const hashSrc = grab(/const hashOf = [^\n]+\n/);
const statusSrc = grab(/function statusOf\(v\)\{[\s\S]*?\n\}\n/);
const T = new Function("S0", pricing + hashSrc + "let S = S0;" + statusSrc +
  "return {S, DEFAULT_RATES, validate, priceJob, statusOf, hashOf, approve(){ const q = priceJob(S.job, S.rates); S.versions.push({n: S.versions.length + 1, hash: hashOf(S), total: q.total}); }};");

let pass = 0, fail = 0;
const ok = (c, n) => { c ? pass++ : fail++; console.log(c ? "ok  " : "FAIL", n); };
const room = {name: "Lounge", length: "4", width: "3", height: "2.4", walls: true, ceiling: false, woodwork: false, doors: "1", windows: "1", condition: "good", darkChange: false};
const t = T({job: {enquiry: "x", customer: "A", access: "Drive", furniture: "customer", paint: "customer", rooms: [{...room}]}, rates: {vatRegistered: false}, versions: []});
t.S.rates = {...t.DEFAULT_RATES};
const st = () => t.statusOf(t.validate(t.S.job)).k;

ok(st() === "draft", "complete job starts as an unapproved draft");
t.approve();
ok(st() === "approved", "approving marks it approved v1");
t.S.job.enquiry = "customer added a note";
ok(st() === "approved", "editing only the enquiry text keeps the approval");
t.S.job.rooms[0].length = "4.5";
ok(st() === "changed", "changing a measurement voids the approval");
ok(t.S.versions.length === 1, "v1 is kept after the change");
t.approve();
ok(st() === "approved" && t.S.versions.length === 2 && t.S.versions[1].n === 2, "re-approving creates v2");
ok(t.S.versions[0].total !== t.S.versions[1].total, "v1 and v2 keep their own totals");
t.S.rates.wallPerM2Coat = 400;
ok(st() === "changed", "changing a rate voids the approval");
t.S.rates.wallPerM2Coat = 320;
ok(st() === "approved", "putting the rate back matches v2 again");
t.S.job.rooms[0].height = "";
ok(st() === "needs", "a missing measurement blocks approval again");
console.log(`${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
