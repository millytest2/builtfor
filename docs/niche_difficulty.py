# Difficulty and money per 100 dials for the top 5 from docs/niche_sellability.py.
# Every rate is an assumption until calls replace it. Worst case halves all three rates.
# Run from repo root: python3 docs/niche_difficulty.py
N = {#                          reach  book  close  months kept
 'party / event rental':        (.40, .15, .20,  8),
 'mobile bartending':           (.50, .20, .15,  6),
 'transmission shops':          (.35, .10, .25, 18),
 'auto repair (phone)':         (.35, .10, .20, 18),
 'auto repair (walk-in, LA)':   (.70, .10, .20, 18),
 'caterers':                    (.25, .15, .20, 10),
}
print(f"{'':28s} dials/client  worst  value/client  $ per 100 dials  worst")
for k,(r,b,c,m) in N.items():
    p=r*b*c; v=1000+199*m
    print(f"{k:28s} {1/p:10.0f}  {8/p:6.0f}  {v:10,d}  {100*p*v:14,.0f}  {100*p*v/8:6,.0f}")
