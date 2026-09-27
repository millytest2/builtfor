# Niche scorecard: 60 local business types x 8 criteria, plus robustness checks.
# Scores are judgment (1-5). Replace them with measured numbers as calls come in.
# Run: python3 docs/niche_scorecard.py
import random, collections
# sell, afford, reach, supply, unpitched, fit, retain, gap   (1-5, judgment)
D = """auto repair|5,5,5,5,3,5,5,3
transmission shop|5,5,5,2,4,5,4,3
auto body / collision|4,5,4,4,3,5,4,3
auto glass|3,3,5,3,3,4,3,3
tire shop|3,4,5,4,3,4,4,3
RV / boat repair|4,5,5,2,5,4,4,4
motorcycle / small engine|3,3,5,3,5,4,4,4
auto upholstery|3,3,5,2,5,4,3,4
auto detailing|3,2,3,4,3,3,3,4
phone / computer repair|4,3,5,3,3,4,3,3
countertop showroom|5,5,4,2,4,5,3,3
flooring store|5,5,5,3,3,5,3,3
window, door and glass|5,5,4,3,4,5,3,3
cabinet shop|4,5,3,3,4,5,3,4
furniture upholstery|3,2,5,3,5,4,3,4
sign shop|3,4,5,3,5,4,4,3
print shop|3,3,5,2,4,4,4,3
machine shop|1,5,4,3,5,2,4,4
monument / headstone|5,5,5,1,5,5,3,4
funeral home|3,5,4,2,3,3,5,1
florist|3,3,5,3,3,3,3,2
jeweler / jewelry repair|3,4,5,3,4,3,4,2
bike shop|3,3,5,2,5,3,3,2
piano / instrument repair|3,3,5,1,5,4,3,4
tailor / alterations|3,1,5,3,5,3,4,4
dry cleaner|2,2,5,3,5,2,4,3
equipment / party rental|5,4,5,3,4,5,4,3
dumpster / portable toilet|5,4,5,3,2,4,3,3
towing|3,4,5,3,4,3,3,3
appliance repair|4,3,4,3,2,4,3,3
pest control|4,4,4,3,2,4,5,2
garage doors|4,4,4,3,1,4,3,2
locksmith|4,3,4,3,1,4,3,3
movers|4,4,4,3,1,4,2,2
pool service|3,4,2,3,3,4,5,4
concrete / masonry|5,5,1,3,4,5,3,4
tree service|5,4,1,4,3,5,3,4
fencing / decks|5,5,2,3,3,5,3,4
septic|5,5,3,2,5,5,4,4
welding / fabrication|3,5,1,3,5,4,3,4
landscaping|3,3,1,5,3,4,3,4
house cleaning|3,1,3,5,3,3,3,3
HVAC|5,5,4,5,1,5,5,1
plumbing|5,5,4,5,1,5,5,1
roofing|5,5,3,4,1,5,3,1
electrician|4,5,3,5,2,5,4,2
dentist|4,5,2,4,1,4,5,1
chiropractor|4,4,2,3,1,4,4,1
med spa|4,5,2,3,1,3,3,1
small law firm|4,5,3,4,1,3,5,1
accountant / tax prep|3,4,4,4,3,3,4,2
vet|3,5,2,3,2,3,5,1
restaurant|3,4,5,5,2,2,2,2
barber / salon|3,2,5,5,3,2,3,3
gym|3,3,4,3,1,3,3,2
martial arts studio|4,3,4,2,4,3,5,3
pet grooming / boarding|3,3,4,3,4,2,4,3
daycare|3,3,3,3,4,3,5,2
tutoring / music lessons|3,3,4,3,4,3,4,3
tattoo shop|3,3,4,3,4,2,3,2"""
rows=[(l.split('|')[0],[int(x) for x in l.split('|')[1].split(',')]) for l in D.splitlines()]
C=['sell','afford','reach','supply','unpitched','fit','retain','gap']
def rank(w): return sorted(rows,key=lambda r:-sum(a*b for a,b in zip(r[1],w)))
base=[3,2,3,2,2,2,2,2]
print('categories',len(rows))
B=rank(base)
for i,(n,s) in enumerate(B[:20]): print(i+1,n,round(sum(a*b for a,b in zip(s,base))/sum(base)/5*100))
random.seed(7); top5=collections.Counter(); top10=collections.Counter(); N=10000
for _ in range(N):
    w=[random.uniform(.5,3) for _ in C]
    r=rank(w); 
    for n,_ in r[:5]: top5[n]+=1
    for n,_ in r[:10]: top10[n]+=1
print('\nrobustness (share of 10k random weightings)')
for n,c in top10.most_common(16): print(f'{n:28s} top5 {top5[n]/N:5.0%}  top10 {c/N:5.0%}')
# jitter the scores themselves: +-1 on every score
random.seed(3); t5=collections.Counter()
for _ in range(N):
    jr=[(n,[min(5,max(1,x+random.choice([-1,0,0,1]))) for x in s]) for n,s in rows]
    r=sorted(jr,key=lambda r:-sum(a*b for a,b in zip(r[1],base)))
    for n,_ in r[:5]: t5[n]+=1
print('\nif my scores are off by one point anywhere:')
for n,c in t5.most_common(10): print(f'{n:28s} top5 {c/N:5.0%}')
# user's three only
print('\nyour three criteria only:',[n for n,_ in rank([1,1,1,0,0,0,0,0])[:12]])
