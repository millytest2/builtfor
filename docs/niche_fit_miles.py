# 20 business types scored on Miles's three questions, then combined with the earlier fundamentals.
# sell = easy to sell this offer, need = how obvious the problem is to the owner,
# know = how likely Miles understands the industry (bartending, events, tech sales, fitness, driver/customer).
# base = score from docs/niche_scorecard.py (afford, reach, supply, pitch pressure, fit, retention, gap).
# Run from repo root: python3 docs/niche_fit_miles.py
import random, collections
R = {#                       sell need know base  why he knows it (or not)
 'auto repair':             (4, 5, 4, 91, 'Every driver has been the customer. The fear of getting ripped off is universal'),
 'transmission shop':       (4, 4, 3, 84, 'Same customer, more technical, bigger bills'),
 'auto body / collision':   (3, 4, 3, 80, 'Easy to picture, but insurance claims add a layer to learn'),
 'auto glass':              (3, 3, 3, 72, 'Simple job, but Safelite owns the category'),
 'tire shop':               (3, 3, 4, 76, 'Everyone has bought tires'),
 'window, door and glass':  (4, 4, 2, 81, 'Homeowner purchase, you have mostly rented'),
 'flooring store':          (4, 4, 2, 82, 'Homeowner purchase, dealer networks to learn'),
 'countertop showroom':     (4, 4, 2, 79, 'Remodel purchase, far from your life'),
 'cabinet shop':            (3, 4, 2, 77, 'Remodel purchase, contractor-driven'),
 'party / equipment rental':(4, 4, 5, 84, 'You have staffed the events they rent for'),
 'monument / headstone':    (3, 3, 1, 84, 'Grief purchase, no exposure'),
 'septic':                  (4, 4, 1, 82, 'Rural, technical, no exposure'),
 'RV / boat repair':        (3, 3, 2, 83, 'Hobby market you are not in'),
 'concrete / masonry':      (3, 4, 2, 73, 'Homeowner project, owner in the field'),
 'tree service':            (3, 4, 2, 71, 'Homeowner emergency, no exposure'),
 'HVAC / plumbing':         (2, 3, 2, 79, 'Know it as a renter calling the landlord'),
 'sign shop':               (3, 2, 3, 78, 'You think in marketing, they sell to businesses'),
 'pest control':            (3, 3, 2, 71, 'Mostly franchise-run'),
 'gym / martial arts':      (3, 3, 5, 71, 'You lift, you know the member side cold'),
 'bars / restaurants':      (3, 4, 5, 64, 'You bartend. Deepest insider knowledge you have'),
}
three=lambda r: round((r[0]+r[1]+r[2])/15*100)
overall=lambda r,a=.5: round(a*three(r)+(1-a)*r[3])
print(f"{'business':26s} sell need know  your3  base  overall")
for k in sorted(R,key=lambda k:-overall(R[k])):
    r=R[k]; print(f"{k:26s}  {r[0]}    {r[1]}    {r[2]}    {three(r):4d}  {r[3]:4d}  {overall(r):5d}")
random.seed(9); N=10000; t1=collections.Counter(); t3=collections.Counter()
for _ in range(N):
    ws=[random.uniform(.5,3) for _ in range(3)]; a=random.uniform(.3,.7)
    f=lambda k: a*(sum(x*w for x,w in zip(R[k][:3],ws))/sum(ws)/5*100)+(1-a)*R[k][3]
    r=sorted(R,key=lambda k:-f(k)); t1[r[0]]+=1
    for k in r[:3]: t3[k]+=1
print('\nrandom weights on your three, and 30-70% weight on them vs the fundamentals:')
for k,c in t3.most_common(6): print(f"{k:26s} #1 {t1[k]/N:5.0%}  top3 {c/N:5.0%}")
print('\nyour three alone:', sorted(R,key=lambda k:-three(R[k]))[:6])
