import csv
from collections import defaultdict

def load_csv(path):
    with open(path, 'r', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

sales = load_csv('Data/FactSales.csv')
prods = {r['ProductKey']: r for r in load_csv('Data/DimProduct.txt')}
regions = {r['RegionKey']: r for r in load_csv('Data/DimRegion.txt')}
custs = {r['CustomerKey']: r for r in load_csv('Data/DimCustomer.txt')}

total_rev = sum(float(r['Revenue']) for r in sales)
total_cost = sum(float(r['Cost']) for r in sales)
total_profit = total_rev - total_cost
total_units = sum(int(r['UnitsSold']) for r in sales)

print(f"Total Revenue: {total_rev:,.2f}")
print(f"Total Cost: {total_cost:,.2f}")
print(f"Total Profit: {total_profit:,.2f}")
print(f"Profit Margin: {total_profit/total_rev:.1%}")
print(f"Total Units: {total_units:,}")
print(f"Transactions: {len(sales)}")

by_month = defaultdict(lambda: {'rev': 0.0, 'cost': 0.0, 'units': 0, 'tx': 0})
for r in sales:
    m = r['Date'][:7]
    by_month[m]['rev'] += float(r['Revenue'])
    by_month[m]['cost'] += float(r['Cost'])
    by_month[m]['units'] += int(r['UnitsSold'])
    by_month[m]['tx'] += 1

print("\n--- BY MONTH ---")
for m, v in sorted(by_month.items()):
    p = v['rev'] - v['cost']
    mg = p / v['rev']
    print(f"{m}: Rev={v['rev']:,.0f}, Cost={v['cost']:,.0f}, Profit={p:,.0f} ({mg:.1%}), Units={v['units']}, Tx={v['tx']}")

by_prod = defaultdict(lambda: {'rev': 0.0, 'cost': 0.0, 'units': 0, 'cat': ''})
for r in sales:
    pname = prods.get(r['ProductKey'], {}).get('ProductName', 'Unknown')
    by_prod[pname]['rev'] += float(r['Revenue'])
    by_prod[pname]['cost'] += float(r['Cost'])
    by_prod[pname]['units'] += int(r['UnitsSold'])
    by_prod[pname]['cat'] = prods.get(r['ProductKey'], {}).get('Category', '')

print("\n--- BY PRODUCT ---")
for p, v in sorted(by_prod.items(), key=lambda x: x[1]['rev'], reverse=True):
    prof = v['rev'] - v['cost']
    mg = (prof / v['rev']) if v['rev'] else 0.0
    print(f"{p} ({v['cat']}): Rev={v['rev']:,.0f}, Cost={v['cost']:,.0f}, Profit={prof:,.0f} ({mg:.1%}), Units={v['units']}")

by_reg = defaultdict(lambda: {'rev': 0.0, 'cost': 0.0, 'units': 0, 'mgr': ''})
for r in sales:
    rname = regions.get(r['RegionKey'], {}).get('RegionName', 'Unknown')
    by_reg[rname]['rev'] += float(r['Revenue'])
    by_reg[rname]['cost'] += float(r['Cost'])
    by_reg[rname]['units'] += int(r['UnitsSold'])
    by_reg[rname]['mgr'] = regions.get(r['RegionKey'], {}).get('SalesManager', '')

print("\n--- BY REGION ---")
for reg_name, v in sorted(by_reg.items(), key=lambda x: x[1]['rev'], reverse=True):
    prof = v['rev'] - v['cost']
    print(f"{reg_name} (Mgr: {v['mgr']}): Rev={v['rev']:,.0f}, Cost={v['cost']:,.0f}, Profit={prof:,.0f} ({prof/v['rev']:.1%}), Units={v['units']}")

by_seg = defaultdict(lambda: {'rev': 0.0, 'cost': 0.0, 'units': 0})
for r in sales:
    sname = custs.get(r['CustomerKey'], {}).get('Segment', 'Unknown')
    by_seg[sname]['rev'] += float(r['Revenue'])
    by_seg[sname]['cost'] += float(r['Cost'])
    by_seg[sname]['units'] += int(r['UnitsSold'])

print("\n--- BY SEGMENT ---")
for sname, v in sorted(by_seg.items(), key=lambda x: x[1]['rev'], reverse=True):
    prof = v['rev'] - v['cost']
    print(f"{sname}: Rev={v['rev']:,.0f}, Cost={v['cost']:,.0f}, Profit={prof:,.0f} ({prof/v['rev']:.1%}), Units={v['units']}")

print("\n--- UNPROFITABLE TRANSACTIONS ---")
for r in sales:
    rev = float(r['Revenue'])
    cost = float(r['Cost'])
    if cost > rev:
        pname = prods.get(r['ProductKey'], {}).get('ProductName', 'Unknown')
        rname = regions.get(r['RegionKey'], {}).get('RegionName', 'Unknown')
        print(f"SalesKey {r['SalesKey']} ({r['Date']}) | {pname} | {rname} | Rev={rev:,.0f}, Cost={cost:,.0f}, Loss={rev-cost:,.2f}")
