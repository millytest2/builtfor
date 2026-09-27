# Service scorecard: 22 things Built for Main Street could sell, gated by the hard rules in CLAUDE.md,
# then a service-by-niche fit pass. Scores are judgment (1-5). Run from repo root.
import random, collections
# want = owner asks for it / gets it fast, proof = we can show a number, effort = 5 means few hours,
# recurring = justifies the monthly, different = agencies do not lead with it, risk = 5 means low risk
C=['want','proof','effort','recurring','different','risk']; W=[3,2,2,2,2,2]
S = {
 'Google listing claimed and cleaned up':      ([5,5,5,2,3,5], None),
 'AI visibility check + monthly AI report':    ([4,5,4,5,5,5], None),
 'Review requests at the counter (QR + email)':([5,5,4,5,3,4], None),
 'Monthly found-and-reachable report':         ([4,5,4,5,4,5], None),
 'Website: page per service and per town':     ([5,4,3,2,2,5], None),
 'Directory cleanup (Apple, Bing, Yelp, BBB)': ([3,4,3,3,4,5], None),
 'Review reply drafts, owner approves':        ([4,3,5,5,3,5], None),
 'Quote form with photo upload, tested':       ([4,4,5,2,3,5], None),
 'Listing upkeep: hours, holidays, photos':    ([4,3,5,5,2,5], None),
 'Make and model pages (auto only)':           ([4,4,3,3,4,5], None),
 'Missed-call log (count, no texts)':          ([4,5,3,4,4,3], None),
 'Spanish-language pages':                     ([4,3,3,2,5,5], None),
 'Booking link hooked to their shop software': ([3,4,5,2,2,5], None),
 'Business email on their own domain':         ([3,3,5,2,2,5], None),
 'Service reminder emails to past customers':  ([4,4,2,5,4,3], None),
 'Real photo shoot of shop and crew':          ([4,3,2,1,4,5], None),
 'AI receptionist or chatbot':                 (None, 'Hard rule: nothing that replaces labour'),
 'Missed-call text-back':                      (None, 'Hard rule: no SMS before client #10'),
 'Social media management':                    (None, 'Hard rule: no social'),
 'Google Ads / Local Services Ads':            (None, 'Hard rule: no ads'),
 'SEO retainer / blog posts':                  (None, 'Hard rule: no SEO retainer'),
 'Logo and rebrand':                           (None, 'Out of scope in OFFER.md'),
}
sc=lambda s,w=W: round(sum(a*b for a,b in zip(s,w))/sum(w)/5*100)
ok={k:v[0] for k,v in S.items() if v[0]}
print('SERVICES (allowed)'); 
random.seed(2); top=collections.Counter(); N=10000
for _ in range(N):
    ww=[random.uniform(.5,3) for _ in C]
    for k in sorted(ok,key=lambda k:-sc(ok[k],ww))[:6]: top[k]+=1
for i,k in enumerate(sorted(ok,key=lambda k:-sc(ok[k])),1): print(f"{i:2d} {k:45s} {sc(ok[k]):3d}  top6 {top[k]/N:4.0%}")
print('\nBLOCKED'); [print('   ',k,'->',v[1]) for k,v in S.items() if not v[0]]

# how much each niche needs each of the top services (1-5)
TOP=['Google listing claimed and cleaned up','AI visibility check + monthly AI report','Review requests at the counter (QR + email)',
     'Monthly found-and-reachable report','Website: page per service and per town','Directory cleanup (Apple, Bing, Yelp, BBB)',
     'Review reply drafts, owner approves','Quote form with photo upload, tested','Make and model pages (auto only)','Spanish-language pages']
N_ = {#                 gbp ai rev rep web dir rply quote make spa
 'auto repair':         [5, 5, 5, 5, 4, 5, 5, 3, 5, 4],
 'auto body':           [5, 4, 5, 4, 4, 5, 4, 5, 5, 4],
 'window, door, glass': [4, 4, 4, 4, 4, 4, 3, 5, 3, 3],
 'concrete / masonry':  [4, 4, 4, 3, 5, 3, 3, 5, 1, 4],
 'flooring':            [4, 3, 3, 3, 4, 4, 3, 4, 1, 3],
 'septic':              [4, 3, 4, 4, 3, 3, 3, 3, 1, 2],
 'cabinet shop':        [3, 3, 3, 3, 5, 3, 2, 5, 1, 3],
 'monument':            [4, 3, 3, 3, 5, 3, 2, 4, 1, 3],
 'HVAC / plumbing':     [3, 3, 4, 4, 2, 3, 3, 3, 1, 3],
}
wt=[sc(ok[s]) for s in TOP]
pull=lambda v: round(sum(a*b for a,b in zip(v,wt))/sum(wt)/5*100)
rec=[1 if ok[s][3]>=4 else 0 for s in TOP]
monthly=lambda v: round(sum(a for a,r in zip(v,rec) if r)/ (5*sum(rec))*100)
print('\nNICHE PULL from the top 10 services   (monthly = how much they need the recurring ones)')
for k in sorted(N_,key=lambda k:-pull(N_[k])): print(f"   {k:22s} pull {pull(N_[k]):3d}   monthly {monthly(N_[k]):3d}")
