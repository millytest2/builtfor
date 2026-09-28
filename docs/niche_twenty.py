# Twenty niches matched to Miles, scored on the coach's criteria (money, pain) and Miles's
# (reach by phone, supply, offer fit, competition, interest, story/career value).
# Judgment scores 1-5. Auto repair is a reference line only. Run from repo root.
import random, collections
C=['money','pain','reach','supply','fit','compet','interest','story']; W=[2,2,2,1.5,2,1,2,1]
R={
 'Recovery and wellness studios':           [4,4,4,3,4,3,5,4],
 'Physical therapy and sports rehab':       [5,4,3,4,4,2,4,5],
 'Therapy and counseling group practices':  [4,4,3,5,3,3,5,5],
 'Youth sports performance training':       [4,4,3,3,4,4,5,4],
 'Party and event rental':                  [4,4,4,4,3,4,4,3],
 'Mobile bartending companies':             [2,4,4,3,4,4,5,3],
 'Event venues and event spaces':           [5,4,3,3,3,2,4,3],
 'Tutoring and test prep centers':          [4,3,3,4,4,3,3,4],
 'Custom tailors and menswear':             [4,3,5,2,3,4,4,3],
 'Acupuncture and holistic health':         [3,3,3,3,4,4,4,3],
 'Massage therapy studios':                 [3,3,3,5,4,3,4,3],
 'Boxing, MMA and martial arts gyms':       [3,3,4,3,3,3,5,3],
 'Caterers':                                [4,3,2,4,4,4,4,3],
 'Podcast and content studios':             [3,3,4,2,3,4,5,3],
 'Meal prep and healthy meal delivery':     [3,3,4,3,3,3,5,3],
 'Chiropractors':                           [4,3,3,5,4,1,3,3],
 'Personal training and strength studios':  [3,3,3,4,3,2,5,3],
 'Pilates and yoga studios':                [3,3,4,4,2,2,4,3],
 'Wedding and event photo / video':         [2,3,4,5,2,2,4,2],
 "Men's grooming lounges and barbers":      [2,2,5,4,2,4,4,2],
 '(reference) independent auto repair':     [5,3,4,5,5,2,1,2],
}
sc=lambda v,w=W: round(sum(a*b for a,b in zip(v,w))/sum(w)/5*100)
for i,k in enumerate(sorted(R,key=lambda k:-sc(R[k])),1):
    print(f"{i:2d} {k:42s}"+''.join(f'{x:3d}' for x in R[k])+f"  {sc(R[k]):3d}")
random.seed(21); N=20000; t1=collections.Counter(); t5=collections.Counter()
for _ in range(N):
    w=[random.uniform(.5,3) for _ in C]; r=sorted(R,key=lambda k:-sc(R[k],w)); t1[r[0]]+=1
    for k in r[:5]: t5[k]+=1
print(f'\n{N} random weightings:')
for k,c in t5.most_common(8): print(f"   {k:42s} #1 {t1[k]/N:5.0%}  top5 {c/N:5.0%}")
print('\ncoach only (money, pain):', sorted(R,key=lambda k:-sc(R[k],[1,1,0,0,0,0,0,0]))[:5])
print('call-ability only (reach, supply, fit):', sorted(R,key=lambda k:-sc(R[k],[0,0,1,1,1,0,0,0]))[:5])
