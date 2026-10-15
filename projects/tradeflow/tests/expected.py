"""Independent pricing for the Quote Lab tests, written separately from the page's JavaScript.

Uses Decimal in pounds and metres with ROUND_HALF_UP, so it checks the page's integer-pence
maths from a different direction. Writes cases.json for test_pricing.mjs.
Sample rates only: these are not real prices.
"""
import json, math
from decimal import Decimal as D, ROUND_HALF_UP
from pathlib import Path

RATES = dict(wall=D("3.20"), ceil=D("3.80"), skirt=D("4.50"), door=D("65.00"), window=D("45.00"),
             furniture=D("25.00"), sundries=D("15.00"), fair=15, poor=35, emulsion=D("24.00"), wood=D("18.00"))
q = lambda x: x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def price(job, vat=False, rates=None):
    R = dict(RATES, **(rates or {}))
    total = D(0); wall_area_coats = D(0); ceil_area_coats = D(0); wood_ml = 0
    for r in job["rooms"]:
        L, W, H = (q(D(r[k])) for k in ("length", "width", "height"))
        doors, windows = int(r["doors"]), int(r["windows"])
        labour = D(0); room = D(0)
        if r.get("walls"):
            area = max(D(0), q(2 * (L + W) * H) - doors * D("1.90") - windows * D("1.50"))
            coats = 3 if r.get("darkChange") else 2
            labour += q(area * coats * R["wall"]); wall_area_coats += area * coats
        if r.get("ceiling"):
            area = q(L * W)
            labour += q(area * 2 * R["ceil"]); ceil_area_coats += area * 2
        if r.get("woodwork"):
            skirt = max(D(0), 2 * (L + W) - doors * D("0.90"))
            labour += q(skirt * R["skirt"]) + doors * R["door"] + windows * R["window"]
            wood_ml += doors * 350 + windows * 200 + int(q(skirt * 30).to_integral_value(rounding=ROUND_HALF_UP))
        pct = {"fair": R["fair"], "poor": R["poor"]}.get(r["condition"], 0)
        room = labour + q(labour * pct / 100)
        if job["furniture"] == "us":
            room += R["furniture"]
        room += R["sundries"]
        total += room
    if job["paint"] == "us":
        total += math.ceil(wall_area_coats / 30) * R["emulsion"]
        total += math.ceil(ceil_area_coats / 30) * R["emulsion"]
        total += math.ceil(D(wood_ml) / 1000) * R["wood"]
    v = q(total * D("0.20")) if vat else D(0)
    return {"subtotal": int(total * 100), "vat": int(v * 100), "total": int((total + v) * 100)}


def room(**kw):
    base = dict(name="Room", length="4", width="3", height="2.4", walls=True, ceiling=False, woodwork=False,
                doors="1", windows="1", condition="good", darkChange=False)
    base.update(kw); return base


def job(rooms, furniture="customer", paint="customer", **kw):
    j = dict(customer="Test", access="Drive", furniture=furniture, paint=paint, rooms=rooms); j.update(kw); return j


cases = []
def priced(name, j, vat=False, rates=None):
    cases.append({"name": name, "job": j, "vat": vat, "rates": rates or {}, "expect": price(j, vat, rates)})

priced("sample job after reply", job([
    room(name="Living room", length="5", width="4", height="2.4", ceiling=True, woodwork=True, doors="2", windows="1", condition="fair", darkChange=True),
    room(name="Main bedroom", length="3.5", width="3.2", height="2.4", woodwork=True, doors="1", windows="1", condition="good")], paint="us"))
priced("walls only, labour only", job([room()]))
priced("walls only with VAT", job([room()]), vat=True)
priced("ceiling only", job([room(walls=False, ceiling=True)]))
priced("woodwork only, no doors", job([room(walls=False, woodwork=True, doors="0", windows="0")]))
priced("poor condition prep", job([room(condition="poor", ceiling=True, woodwork=True)]))
priced("fair condition prep", job([room(condition="fair")]))
priced("we move furniture, 3 rooms", job([room(), room(name="B"), room(name="C")], furniture="us"))
priced("odd decimals 3.333 x 2.789 x 2.455", job([room(length="3.333", width="2.789", height="2.455", ceiling=True, woodwork=True)]))
priced("half-up dims 2.005", job([room(length="2.005", width="2.005", height="2.005", ceiling=True)]))
priced("tiny cupboard, deductions exceed wall", job([room(length="0.5", width="0.4", height="1", doors="3", windows="2")]))
priced("big room, paint supplied", job([room(length="12.5", width="9.75", height="3.1", ceiling=True, woodwork=True, doors="4", windows="6", darkChange=True)], paint="us"))
priced("paint supplied, VAT", job([room(ceiling=True, woodwork=True)], paint="us"), vat=True)
priced("many windows no woodwork", job([room(windows="5", doors="0")]))
priced("dark change only", job([room(darkChange=True)]))
priced("changed rates", job([room(ceiling=True, woodwork=True, condition="fair")]), rates={"wall": D("4.10"), "door": D("80.00"), "fair": 20})
priced("VAT rounding 0.5p", job([room(length="1.01", width="1.01", height="1.01", doors="0", windows="0")]), vat=True)
priced("five rooms mixed", job([room(name=str(i), length=f"{3+i*0.37:.2f}", width=f"{2+i*0.21:.2f}", ceiling=i % 2 == 0, woodwork=i % 3 == 0,
                                     condition=["good", "fair", "poor"][i % 3], darkChange=i == 4) for i in range(5)], furniture="us", paint="us"), vat=True)
priced("zero doors and windows", job([room(doors="0", windows="0", woodwork=True)]))
priced("2.4 vs 2.40 same", job([room(height="2.40")]))

checks = [
    {"name": "missing height blocks price", "job": job([room(height="")]), "valid": False},
    {"name": "missing condition blocks price", "job": job([room(condition="")]), "valid": False},
    {"name": "missing paint answer blocks price", "job": job([room()], paint=""), "valid": False},
    {"name": "missing access blocks price", "job": job([room()], access=""), "valid": False},
    {"name": "no rooms blocks price", "job": job([]), "valid": False},
    {"name": "nothing to paint blocks price", "job": job([room(walls=False)]), "valid": False},
    {"name": "comma decimal rejected", "job": job([room(length="3,5")]), "valid": False, "bad": True},
    {"name": "negative rejected", "job": job([room(width="-2")]), "valid": False, "bad": True},
    {"name": "zero length rejected", "job": job([room(length="0")]), "valid": False, "bad": True},
    {"name": "text rejected", "job": job([room(height="tall")]), "valid": False, "bad": True},
    {"name": "half a door rejected", "job": job([room(doors="1.5")]), "valid": False, "bad": True},
    {"name": "complete job is valid", "job": job([room()]), "valid": True},
]

out = Path(__file__).with_name("cases.json")
json.dump({"priced": [{**c, "rates": {k: (str(v) if isinstance(v, D) else v) for k, v in c["rates"].items()}} for c in cases],
           "validation": checks}, out.open("w"), indent=1)
print(f"{len(cases)} priced cases, {len(checks)} validation cases -> {out.name}")
