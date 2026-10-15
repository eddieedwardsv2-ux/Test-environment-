// Runs the page's own pricing code (between the PRICING markers) against cases.json,
// which expected.py builds with a separate Decimal implementation.
// Usage: python3 expected.py && node test_pricing.mjs
import {readFileSync} from "node:fs";
import {dirname, join} from "node:path";
import {fileURLToPath} from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const html = readFileSync(join(here, "../quote-lab/quote-lab.html"), "utf8");
const src = html.split("// ==PRICING START==")[1].split("// ==PRICING END==")[0];
const P = new Function(src + "; return {DEFAULT_RATES, validate, priceJob, parseMetres, money};")();
const {priced, validation} = JSON.parse(readFileSync(join(here, "cases.json"), "utf8"));

const rateKey = {wall: "wallPerM2Coat", ceil: "ceilingPerM2Coat", skirt: "skirtingPerM", door: "doorEach", window: "windowEach",
  furniture: "furniturePerRoom", sundries: "sundriesPerRoom", emulsion: "emulsionTin", wood: "woodworkTin", fair: "prepFairPct", poor: "prepPoorPct"};
let pass = 0, fail = 0;
const ok = (cond, name, detail = "") => { cond ? pass++ : fail++; if (!cond) console.log("FAIL", name, detail); };

for (const c of priced){
  const rates = {vatRegistered: c.vat};
  for (const [k, v] of Object.entries(c.rates)) rates[rateKey[k]] = k === "fair" || k === "poor" ? v : Math.round(parseFloat(v) * 100);
  const v = P.validate(c.job);
  ok(v.ok, c.name + " (valid)", JSON.stringify(v.missing.concat(v.bad)));
  const got = P.priceJob(c.job, rates);
  ok(got.subtotal === c.expect.subtotal && got.vat === c.expect.vat && got.total === c.expect.total,
     c.name, `page ${got.subtotal}/${got.vat}/${got.total} vs expected ${c.expect.subtotal}/${c.expect.vat}/${c.expect.total}`);
  const sumLines = got.rooms.reduce((a, r) => a + r.lines.reduce((b, l) => b + l.pence, 0), 0) + got.materials.reduce((a, l) => a + l.pence, 0);
  ok(sumLines === got.subtotal, c.name + " (lines add up)");
}
for (const c of validation){
  const v = P.validate(c.job);
  ok(v.ok === c.valid, c.name, JSON.stringify(v));
  if (c.bad) ok(v.bad.length > 0, c.name + " (flagged as a bad number)");
}
ok(P.money(123456789) === "£1,234,567.89" && P.money(5) === "£0.05", "money formatting");
ok(P.parseMetres("2.345").cm === 235 && P.parseMetres("2.344").cm === 234, "metres round half up");

const sample = priced[0];
console.log(`sample job total: ${P.money(sample.expect.total)}`);
console.log(`${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
