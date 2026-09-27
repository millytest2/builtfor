# Worst case after fixes, for the top 10 from docs/niche_worstcase.py.
# Only scores a fix can honestly move are raised; structural limits stay put.
# Run from the repo root: python3 docs/niche_overcome.py
import random, collections
#                            sell afford reach supply unpitched fit retain gap
WORST = {
 'auto repair (+transmission)':[3,4,3,5,2,4,4,1],
 'flooring store':             [4,4,4,3,2,4,3,1],
 'window, door and glass':     [4,4,3,2,3,4,3,2],
 'monument / headstone':       [2,4,4,1,4,4,3,3],
 'septic':                     [4,4,2,1,4,4,3,3],
 'cabinet shop':               [3,4,2,2,4,4,3,3],
 'HVAC / plumbing':            [2,5,3,5,1,4,4,1],
 'concrete / masonry':         [4,4,1,3,3,5,2,3],
 'RV / boat repair':           [2,4,4,1,4,3,3,3],
 'auto body / collision':      [2,4,3,3,2,4,4,2],
}
FIXED = {
 'auto repair (+transmission)':[4,4,4,4,3,4,4,3],
 'flooring store':             [4,4,4,2,3,4,3,2],
 'window, door and glass':     [4,4,4,3,3,4,3,2],
 'monument / headstone':       [3,4,4,2,4,4,3,3],
 'septic':                     [4,4,3,2,4,4,3,3],
 'cabinet shop':               [4,4,3,2,4,4,3,3],
 'HVAC / plumbing':            [3,5,3,4,1,4,4,2],
 'concrete / masonry':         [4,4,2,3,3,5,3,3],
 'RV / boat repair':           [3,4,4,1,4,3,3,3],
 'auto body / collision':      [3,4,4,3,2,4,4,2],
}
w=[3,2,3,2,2,2,2,2]
sc=lambda s,w=w: round(sum(a*b for a,b in zip(s,w))/sum(w)/5*100)
print(f"{'business':30s} worst  fixed  gain")
for k in sorted(FIXED,key=lambda k:-sc(FIXED[k])): print(f"{k:30s} {sc(WORST[k]):5d}  {sc(FIXED[k]):5d}  {sc(FIXED[k])-sc(WORST[k]):+4d}")
random.seed(5); N=10000; t1=collections.Counter(); t3=collections.Counter()
for _ in range(N):
    ww=[random.uniform(.5,3) for _ in range(8)]
    r=sorted(FIXED,key=lambda k:-sc(FIXED[k],ww)); t1[r[0]]+=1
    for k in r[:3]: t3[k]+=1
print('\nafter fixes, random weights:')
for k,c in t3.most_common(6): print(f"{k:30s} #1 {t1[k]/N:5.0%}  top3 {c/N:5.0%}")
print('\nyour three only:', sorted(FIXED,key=lambda k:-sc(FIXED[k],[1,1,1,0,0,0,0,0]))[:5])
