# Final combined niche model: 33 business types.
# Fundamentals (afford, reach, supply, pitch pressure, offer fit, retention, gap) + Miles's three
# (easy to sell, obvious need, will he understand it). Judgment scores 1-5. Run from repo root.
import random, collections
BW=[3,2,3,2,2,2,2,2]
def base(v): return round(sum(a*b for a,b in zip(v,BW))/sum(BW)/5*100)
#                              sell afford reach supply unpitched fit retain gap | sell need know
R = {
 'auto repair':               ([5,5,5,5,3,5,5,3], (4,5,4)),
 'party / equipment rental':  ([5,4,5,3,4,5,4,3], (4,4,5)),
 'transmission shop':         ([5,5,5,2,4,5,4,3], (4,4,3)),
 'auto body / collision':     ([4,5,4,4,3,5,4,3], (3,4,3)),
 'window, door and glass':    ([5,5,4,3,4,5,3,3], (4,4,2)),
 'flooring store':            ([5,5,5,3,3,5,3,3], (4,4,2)),
 'countertop showroom':       ([5,5,4,2,4,5,3,3], (4,4,2)),
 'tire shop':                 ([3,4,5,4,3,4,4,3], (3,3,4)),
 'gym / martial arts':        ([4,3,4,2,4,3,5,3], (3,3,5)),
 'bars / restaurants':        ([3,4,5,5,2,2,2,2], (3,4,5)),
 'septic':                    ([5,5,3,2,5,5,4,4], (4,4,1)),
 'cabinet shop':              ([4,5,3,3,4,5,3,4], (3,4,2)),
 'RV / boat repair':          ([4,5,5,2,5,4,4,4], (3,3,2)),
 'auto glass':                ([3,3,5,3,3,4,3,3], (3,3,3)),
 'monument / headstone':      ([5,5,5,1,5,5,3,4], (3,3,1)),
 'concrete / masonry':        ([5,5,1,3,4,5,3,4], (3,4,2)),
 'tree service':              ([5,4,1,4,3,5,3,4], (3,4,2)),
 'sign shop':                 ([3,4,5,3,5,4,4,3], (3,2,3)),
 'HVAC / plumbing':           ([5,5,4,5,1,5,5,1], (2,3,2)),
 'pest control':              ([4,4,4,3,2,4,5,2], (3,3,2)),
 # route and cleaning services
 'pool service':              ([3,4,2,3,3,4,5,4], (3,3,3)),
 'window cleaning':           ([3,2,2,4,3,3,3,3], (3,2,4)),
 'pressure washing':          ([3,2,2,5,1,3,3,2], (2,2,4)),
 'carpet / upholstery cleaning':([3,3,3,4,2,4,3,2],(3,3,3)),
 'gutter cleaning':           ([3,2,2,3,3,3,2,3], (3,2,3)),
 'junk removal':              ([4,3,3,4,1,4,3,2], (3,4,4)),
 'mobile auto detailing':     ([3,2,2,5,2,3,2,3], (2,3,4)),
 'mobile mechanic':           ([4,3,2,3,4,4,3,4], (4,4,4)),
 'chimney sweep':             ([4,3,2,2,4,4,3,4], (3,3,2)),
 'dryer vent cleaning':       ([3,2,2,2,4,3,3,3], (3,2,3)),
 'solar panel cleaning':      ([3,2,2,2,4,3,3,3], (3,2,3)),
 'house cleaning':            ([3,1,3,5,3,3,3,3], (2,3,4)),
 'lawn care / landscaping':   ([3,3,1,5,3,4,3,4], (3,3,3)),
}
three=lambda t: round(sum(t)/15*100)
over=lambda k,a=.5: round(a*three(R[k][1])+(1-a)*base(R[k][0]))
print(f"{'business':30s} base  your3  overall")
for i,k in enumerate(sorted(R,key=lambda k:-over(k)),1): print(f"{i:2d} {k:30s} {base(R[k][0]):4d}  {three(R[k][1]):5d}  {over(k):6d}")
random.seed(4); N=20000; t1=collections.Counter(); t5=collections.Counter()
for _ in range(N):
    bw=[random.uniform(.5,3) for _ in range(8)]; mw=[random.uniform(.5,3) for _ in range(3)]; a=random.uniform(.3,.7)
    f=lambda k: a*sum(x*w for x,w in zip(R[k][1],mw))/sum(mw)/5*100+(1-a)*sum(x*w for x,w in zip(R[k][0],bw))/sum(bw)/5*100
    r=sorted(R,key=lambda k:-f(k)); t1[r[0]]+=1
    for k in r[:5]: t5[k]+=1
print(f'\n{N} random weightings of all 11 criteria:')
for k,c in t5.most_common(8): print(f"   {k:30s} #1 {t1[k]/N:5.0%}  top5 {c/N:5.0%}")
route=['pool service','window cleaning','pressure washing','carpet / upholstery cleaning','gutter cleaning','junk removal','mobile auto detailing','mobile mechanic','chimney sweep','dryer vent cleaning','solar panel cleaning','house cleaning','lawn care / landscaping']
print('\nbest route/cleaning service:', max(route,key=over), over(max(route,key=over)), '| auto repair', over('auto repair'))
