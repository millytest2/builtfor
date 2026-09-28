# Top 10 from docs/niche_twenty.py, rescored with the goal made explicit: getting the OWNER on the line.
# owner = odds of a live conversation with the decision-maker within three touches (1-5, judgment).
# Run from repo root: python3 docs/niche_owner_access.py
import random, collections
C=['money','pain','reach','supply','fit','compet','interest','story','owner']; W=[2,2,1,1.5,2,1,2,1,3]
R={
 'Recovery and wellness studios':          [4,4,4,3,4,3,5,4,3],
 'Physical therapy and sports rehab':      [5,4,3,4,4,2,4,5,2],
 'Therapy and counseling group practices': [4,4,3,5,3,3,5,5,2],
 'Youth sports performance training':      [4,4,3,3,4,4,5,4,4],
 'Party and event rental':                 [4,4,4,4,3,4,4,3,4],
 'Mobile bartending companies':            [2,4,4,3,4,4,5,3,5],
 'Custom tailors and menswear':            [4,3,5,2,3,4,4,3,4],
 'Event venues and event spaces':          [5,4,3,3,3,2,4,3,2],
 'Tutoring and test prep centers':         [4,3,3,4,4,3,3,4,3],
 'Massage therapy studios':                [3,3,3,5,4,3,4,3,3],
}
sc=lambda v,w=W: round(sum(a*b for a,b in zip(v,w))/sum(w)/5*100)
for i,k in enumerate(sorted(R,key=lambda k:-sc(R[k])),1): print(f"{i:2d} {k:40s} owner {R[k][-1]}  score {sc(R[k])}")
random.seed(33); N=20000; t1=collections.Counter(); t3=collections.Counter()
for _ in range(N):
    w=[random.uniform(.5,3) for _ in C]; w[-1]=random.uniform(2,4)   # owner access always weighs heavily
    r=sorted(R,key=lambda k:-sc(R[k],w)); t1[r[0]]+=1
    for k in r[:3]: t3[k]+=1
print(f'\n{N} weightings, owner access always heavy:')
for k,c in t3.most_common(6): print(f"   {k:40s} #1 {t1[k]/N:5.0%}  top3 {c/N:5.0%}")
