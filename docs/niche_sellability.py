# Which niche can Miles actually sell to first? Adds "your edge" (rapport, credibility, prior selling)
# to money, pain, offer fit, reach and pitch pressure. Judgment scores 1-5. Run from repo root.
import random, collections
C=['money','pain','fit','reach','edge','unpitched']; W=[2,2,2,2,3,1]
R={#                                money pain fit reach edge unp   edge reason
 'party / event rental':            ([4,4,5,4,4,4],'you have worked the events they rent for'),
 'mobile bartending companies':     ([3,4,4,4,5,4],'you are one: you know their gigs, prices and clients'),
 'caterers':                        ([4,3,4,3,4,4],'same events, same planners'),
 'event venues':                    ([5,4,3,3,4,2],'you have worked their rooms'),
 'DJs / photo booths':              ([2,3,3,4,4,3],'event crew you already know'),
 'bars / restaurants':              ([3,3,2,5,5,2],'you bartend, and you sold to them at Social Hog'),
 'gyms / martial arts':             ([3,3,3,4,4,2],'you lift'),
 'barbers':                         ([2,2,2,5,3,3],'you are a customer'),
 'independent auto repair':         ([5,3,5,5,2,3],'customer only, no insider credibility'),
 'collision / auto body':           ([5,4,4,4,2,3],'customer only'),
 'transmission shops':              ([5,4,5,5,2,4],'customer only'),
 'flooring stores':                 ([5,3,5,5,1,3],'no exposure'),
 'window, door and glass':          ([5,3,5,4,1,3],'no exposure'),
 'junk removal':                    ([3,4,4,3,3,2],'simple business, easy to learn'),
 'food trucks':                     ([2,3,2,3,4,3],'event circuit you know'),
}
sc=lambda v,w=W: round(sum(a*b for a,b in zip(v,w))/sum(w)/5*100)
print(f"{'business':30s} " + ' '.join(f'{c[:6]:>6s}' for c in C) + '  score')
for k in sorted(R,key=lambda k:-sc(R[k][0])): print(f"{k:30s} " + ' '.join(f'{x:6d}' for x in R[k][0]) + f"  {sc(R[k][0]):5d}")
random.seed(8); N=20000; t1=collections.Counter(); t5=collections.Counter()
for _ in range(N):
    w=[random.uniform(.5,3) for _ in C]; r=sorted(R,key=lambda k:-sc(R[k][0],w)); t1[r[0]]+=1
    for k in r[:5]: t5[k]+=1
print(f'\n{N} random weightings:')
for k,c in t5.most_common(8): print(f"   {k:30s} #1 {t1[k]/N:5.0%}  top5 {c/N:5.0%}")
print('\nwith edge weighted like everything else:', sorted(R,key=lambda k:-sc(R[k][0],[1,1,1,1,1,1]))[:5])
print('with edge ignored:                       ', sorted(R,key=lambda k:-sc(R[k][0],[2,2,2,2,0,1]))[:5])
