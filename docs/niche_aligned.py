# Ten niches that match Miles's own life (body, mind, events, presence, career), scored on the
# offer's gates plus interest and content fit. Auto repair included only as the baseline.
# Judgment scores 1-5. Run from repo root: python3 docs/niche_aligned.py
import random, collections
C=['money','reach','supply','sell','fit','unpitched','interest','content']; W=[2,2,1,2,2,1,2,1]
R={
 'recovery and wellness studios (sauna, cold plunge, massage, stretch)':[4,4,3,4,4,3,5,4],
 'physical therapy and sports rehab practices':                         [5,3,4,4,4,2,4,4],
 'therapy and counseling group practices':                              [4,3,5,4,3,3,5,4],
 'independent boxing, MMA and martial arts gyms':                       [3,4,3,3,3,3,5,5],
 'personal training and strength studios':                              [3,3,4,3,3,2,5,5],
 'event venues and event spaces':                                       [5,3,3,4,3,2,4,3],
 'mobile bartending and event bar companies':                           [2,4,3,4,4,4,5,3],
 "men's grooming lounges and custom tailors":                           [3,5,2,3,3,4,4,4],
 'tutoring and test prep centers':                                      [4,3,4,3,4,3,3,2],
 'pilates and yoga studios':                                            [3,4,4,3,2,2,4,3],
 '(baseline) independent auto repair':                                  [5,5,5,4,5,3,1,1],
}
sc=lambda v,w=W: round(sum(a*b for a,b in zip(v,w))/sum(w)/5*100)
print(f"{'':70s}"+''.join(f'{c[:5]:>6s}' for c in C)+'  score')
for k in sorted(R,key=lambda k:-sc(R[k])): print(f"{k:70s}"+''.join(f'{x:6d}' for x in R[k])+f"  {sc(R[k]):5d}")
random.seed(12); N=20000; t1=collections.Counter(); t3=collections.Counter()
for _ in range(N):
    w=[random.uniform(.5,3) for _ in C]; r=sorted(R,key=lambda k:-sc(R[k],w)); t1[r[0]]+=1
    for k in r[:3]: t3[k]+=1
print(f'\n{N} random weightings:')
for k,c in t3.most_common(6): print(f"   {k:70s} #1 {t1[k]/N:5.0%}  top3 {c/N:5.0%}")
