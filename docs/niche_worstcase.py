# Worst-case pass on the niche scorecard. Each business gets its pessimistic scores and the scenario behind them.
# Run from the repo root: python3 docs/niche_worstcase.py
import random, collections, importlib.util
spec=importlib.util.spec_from_file_location('n','docs/niche_scorecard.py')
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()): n=importlib.util.module_from_spec(spec); spec.loader.exec_module(n)
base=dict(n.rows)
# worst case: sell, afford, reach, supply, unpitched, fit, retain, gap  |  the scenario
W = {
'auto repair':            ([3,4,3,5,2,4,4,1], 'Most already have a decent site from their shop software, auto-marketing firms call weekly, the service writer screens you'),
'transmission shop':      ([3,4,4,1,3,4,3,2], 'Two per town, and most work is referred by general shops, not searched'),
'auto body / collision':  ([2,4,3,3,2,4,4,2], 'Insurance direct-repair programs steer the work, so search matters less'),
'equipment / party rental':([3,3,4,2,3,3,3,2],'Party side books through Yelp and Instagram, seasonal, few true independents'),
'RV / boat repair':       ([2,4,4,1,4,3,3,3], 'Few per region and booked months out, so they do not want more work'),
'monument / headstone':   ([2,4,4,1,4,4,3,3], 'Funeral homes send the work, and there are one or two per region'),
'septic':                 ([4,4,2,1,4,4,3,3], 'Rural and few, owner is on the truck, work comes from realtors and inspectors'),
'flooring store':         ([4,4,4,3,2,4,3,1], 'Most are buying-group dealers with a corporate site already'),
'window, door and glass': ([4,4,3,2,3,4,3,2], 'Window companies are heavily marketed, fewer independents than expected'),
'countertop showroom':    ([4,4,3,1,3,4,2,2], 'One or two per town, lumpy demand tied to remodels'),
'cabinet shop':           ([3,4,2,2,4,4,3,3], 'Owner on the shop floor, most work from contractors'),
'tire shop':              ([2,3,4,3,2,3,3,2], 'Price shoppers, chains dominate, thin margins'),
'sign shop':              ([2,3,4,2,4,3,3,2], 'Work comes from repeat business clients, not search'),
'motorcycle / small engine':([2,2,4,2,4,3,3,3],'Small jobs, seasonal, owner is the only mechanic'),
'dumpster / portable toilet':([4,3,4,2,1,3,2,2],'Brokers own the search results and undercut'),
'pest control':           ([3,4,3,2,1,4,4,1], 'Franchises and agencies already own the space'),
'appliance repair':       ([3,2,3,2,1,3,2,2], 'Lead-gen sites own the demand, small tickets'),
'HVAC':                   ([2,5,3,5,1,4,4,1], 'You are the 11th agency this week, and they already have a site, so it is a redo'),
'plumbing':               ([2,5,3,5,1,4,4,1], 'You are the 11th agency this week, and they already have a site, so it is a redo'),
'concrete / masonry':     ([4,4,1,3,3,5,2,3], 'Owner unreachable in the field, seasonal outside the Sun Belt'),
'tree service':           ([4,3,1,3,2,5,2,3], 'Owner in a tree all day, lead-gen platforms own emergencies'),
'fencing / decks':        ([4,4,1,3,2,5,2,3], 'Owner on site, seasonal'),
'restaurant':             ([2,3,4,5,1,1,1,1], 'Want Instagram you do not sell, most have a site, closures'),
'martial arts studio':    ([3,2,4,2,3,3,4,2], 'Run on referrals and booking software, tight budgets'),
}
w=[3,2,3,2,2,2,2,2]
sc=lambda s,w=w: round(sum(a*b for a,b in zip(s,w))/sum(w)/5*100)
rows=sorted(W, key=lambda k:-sc(W[k][0]))
print(f"{'business':27s} best  worst  drop")
for k in rows: print(f"{k:27s} {sc(base[k]):4d}  {sc(W[k][0]):5d}  {sc(base[k])-sc(W[k][0]):4d}")
random.seed(11); N=10000; t1=collections.Counter(); t3=collections.Counter()
for _ in range(N):
    ww=[random.uniform(.5,3) for _ in range(8)]
    r=sorted(W,key=lambda k:-sc(W[k][0],ww))
    t1[r[0]]+=1
    for k in r[:3]: t3[k]+=1
print('\nworst case, random weights: #1 share, top-3 share')
for k,c in t3.most_common(10): print(f"{k:27s} #1 {t1[k]/N:5.0%}  top3 {c/N:5.0%}")
print('\nyour three only, worst case:', sorted(W,key=lambda k:-sc(W[k][0],[1,1,1,0,0,0,0,0]))[:8])
