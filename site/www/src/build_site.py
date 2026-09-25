import io

# ---------- the street, drawn once, cropped and lit per use ----------
def street(cls, viewbox, fifth_lit, label_size, fifth_label):
    L = 'rgba(242,236,224,.36)'
    fifth = ('<rect class="lit lit5" x="794" y="100" width="86" height="56" fill="#f0b429" stroke="none"/>'
             if fifth_lit else '')
    dash = '' if fifth_lit else ' stroke-dasharray="6 7"'
    op = '1' if fifth_lit else '.5'
    aw5 = ('<path d="M774 90 h176" stroke-dasharray="14 14" stroke="#c0392f" stroke-width="5"/>' if fifth_lit
           else '<path d="M774 90 h176" stroke-dasharray="10 10" stroke="rgba(242,236,224,.3)" stroke-width="5"/>')
    t = lambda x, s, dim=False: (f'<text x="{x}" y="178" text-anchor="middle" font-family="IBM Plex Mono,monospace" '
        f'font-size="{label_size}" letter-spacing="1" fill="{"rgba(242,236,224,.34)" if dim else "rgba(242,236,224,.62)"}" stroke="none">{s}</text>')
    return f'''<svg class="{cls}" viewBox="{viewbox}" role="img" aria-label="A row of shops on a main street. {'All five are lit, including yours.' if fifth_lit else 'Four are lit. The fifth, yours, is dark.'}">
  <g fill="none" stroke="{L}" stroke-width="1.6" stroke-linecap="square">
    <line x1="0" y1="190" x2="1000" y2="190" stroke="rgba(242,236,224,.26)"/>
    <rect x="14" y="56" width="176" height="134"/><path d="M14 56 L102 26 L190 56"/>
    <rect class="lit" x="34" y="90" width="86" height="62" fill="#f0b429" stroke="none"/>
    <rect x="34" y="90" width="86" height="62"/><line x1="77" y1="90" x2="77" y2="152"/>
    <rect x="140" y="104" width="34" height="86"/>
    <path d="M14 80 h176" stroke-dasharray="14 14" stroke="#c0392f" stroke-width="5"/>
    <rect x="204" y="68" width="176" height="122"/>
    <rect class="lit" x="224" y="98" width="62" height="56" fill="#f0b429" stroke="none"/>
    <rect x="224" y="98" width="62" height="56"/><line x1="255" y1="98" x2="255" y2="154"/>
    <rect x="306" y="110" width="34" height="80"/>
    <path d="M204 90 h176" stroke-dasharray="14 14" stroke="#c0392f" stroke-width="5"/>
    <path d="M360 190 v-38 M360 164 l-16 -18 M360 172 l16 -16"/><circle cx="360" cy="138" r="20"/>
    <rect x="394" y="50" width="176" height="140"/><path d="M394 50 h176 v18 h-176 z"/>
    <rect class="lit" x="414" y="94" width="98" height="62" fill="#f0b429" stroke="none"/>
    <rect x="414" y="94" width="98" height="62"/>
    <line x1="414" y1="110" x2="512" y2="110"/><line x1="414" y1="126" x2="512" y2="126"/>
    <line x1="414" y1="142" x2="512" y2="142"/><rect x="530" y="108" width="26" height="82"/>
    <path d="M394 82 h176" stroke-dasharray="14 14" stroke="#c0392f" stroke-width="5"/>
    <rect x="584" y="62" width="176" height="128"/><line x1="584" y1="82" x2="760" y2="82"/>
    <line x1="628" y1="62" x2="628" y2="82"/><line x1="672" y1="62" x2="672" y2="82"/>
    <line x1="716" y1="62" x2="716" y2="82"/>
    <rect class="lit" x="604" y="102" width="84" height="54" fill="#f0b429" stroke="none"/>
    <rect x="604" y="102" width="84" height="54"/><rect x="708" y="108" width="34" height="82"/>
    <path d="M584 94 h176" stroke-dasharray="14 14" stroke="#c0392f" stroke-width="5"/>
    <g opacity="{op}">
      {fifth}
      <rect x="774" y="68" width="176" height="122"{dash}/>
      <rect x="794" y="100" width="86" height="56"{dash}/>
      <line x1="837" y1="100" x2="837" y2="156"{dash}/>
      <rect x="900" y="110" width="34" height="80"{dash}/>
      {aw5}
    </g>
  </g>
  {t(102,'UPHOLSTERY')}{t(262,'TREE SERVICE')}{t(482,'WELDING')}{t(672,'MASONRY')}{t(862,fifth_label, dim=not fifth_lit)}
</svg>'''

top_desk = street('st-desk', '0 0 1000 196', False, 11.5, 'YOURS?')
top_mob  = street('st-mob',  '578 14 384 182', False, 13, 'YOURS?')
end_desk = street('st-desk', '0 0 1000 196', True, 11.5, 'YOURS')
end_mob  = street('st-mob',  '578 14 384 182', True, 13, 'YOURS')

CSS = open('site/www/src/style.css').read()

BODY = f'''
<nav class="nav" id="nav">
  <div class="nav-in">
    <a class="mark" href="#top">BUILT FOR MAIN <span class="st">STREET</span></a>
    <div class="nav-links" id="navlinks">
      <a href="#problem">The problem</a>
      <a href="#check">Check yours</a>
      <a href="#fix">What you get</a>
      <a href="#pricing">Pricing</a>
    </div>
    <a class="nav-cta" href="#start">Free check</a>
    <button class="menu" id="menu" type="button" aria-expanded="false" aria-controls="navlinks" aria-label="Sections"><span></span><span></span><span></span></button>
  </div>
</nav>


<main id="top">

<section class="wrap hero">
  <div class="duo">
    <div class="words">
      <h1>Your next customer is asking a machine who to <em>call</em>.</h1>
      <p class="dek">It names two or three shops, and that's the list. We fix what keeps yours
      off it, and make sure the people who find you can reach you in one tap.</p>
      <div class="cta-row">
        <a class="btn" href="#start">Get a free check</a>
        <a class="btn ghost" href="#check">Check it yourself</a>
      </div>
    </div>
    <figure class="chat" aria-label="An example of an AI assistant answering a customer's question">
      <div class="chat-top"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="chat-t">AI assistant</span></div>
      <div class="bubble ask">Who's the best upholstery shop in Fort Wayne?</div>
      <div class="bubble ans">
        <p>Here are three well-reviewed options:</p>
        <ol>
          <li><b>Ridgeline Upholstery</b><span>4.8</span></li>
          <li><b>Carver &amp; Daughters</b><span>4.7</span></li>
          <li><b>Northside Furniture Repair</b><span>4.6</span></li>
        </ol>
      </div>
      <div class="missing"><span>Not in the answer</span>The shop with thirty years and the best reviews in town.</div>
      <figcaption>An example. The shop names are made up.</figcaption>
    </figure>
  </div>
</section>

<section class="band" id="problem">
  <div class="wrap">
    <h2>Four of these shops come up. <span class="l2">One doesn&rsquo;t.</span></h2>
    {top_desk}
    {top_mob}
    <div class="why">
      <div><h3>They never find you</h3>
        <p>Google and the AI tools can&rsquo;t tell what you do or where you work, so they skip you.</p></div>
      <div><h3>They find you and give up</h3>
        <p>The number won&rsquo;t tap to call, the form doesn&rsquo;t reach anyone, or the hours are wrong, so they call the next shop.</p></div>
    </div>
    <p class="cap">The dark one has the best reviews on the street.</p>
  </div>
</section>

<section class="wrap" id="check">
  <div class="duo">
    <div class="words">
      <h2>Ask it about your own shop.</h2>
      <p class="lead">Paste these into ChatGPT or Google&rsquo;s AI answer and see what comes back.
      Nothing you type here leaves this page.</p>
      <div class="verdict">If your shop isn&rsquo;t in the answer, or it says it doesn&rsquo;t have any
      information about you, <b>that&rsquo;s the thing we fix.</b> It&rsquo;s the same fix either way.</div>
    </div>
    <div class="tool">
      <div class="fields">
        <div><label for="trade">Your trade</label>
          <select id="trade">
            <option value="reupholstery">Upholstery</option>
            <option value="tree removal">Tree service</option>
            <option value="welding and ornamental iron">Welding and iron</option>
            <option value="masonry and concrete">Masonry and concrete</option>
            <option value="custom cabinetry">Cabinetry</option>
            <option value="landscaping">Landscaping</option>
          </select></div>
        <div><label for="town">Your town</label>
          <input type="text" id="town" placeholder="Fort Wayne" autocomplete="address-level2"></div>
        <div class="span2"><label for="biz">Your shop&rsquo;s name</label>
          <input type="text" id="biz" placeholder="Hoffman &amp; Sons" autocomplete="organization"></div>
      </div>
      <div class="qlab">Ask this first</div>
      <div class="qrow"><div class="qtxt" id="q1"></div><button class="copy" type="button" data-for="q1">Copy</button></div>
      <div class="qlab">Then this</div>
      <div class="qrow"><div class="qtxt" id="q2"></div><button class="copy" type="button" data-for="q2">Copy</button></div>
    </div>
  </div>
</section>

<section class="wrap" id="fix">
  <div class="duo">
    <div class="words">
      <h2>One job, written up like any other.</h2>
      <p class="lead">Everything we do for you fits on one ticket. It&rsquo;s done two weeks
      after your photos come in.</p>
      <p class="no">What&rsquo;s not on it: social media, ads, logos, or a chatbot talking to
      your customers. We don&rsquo;t do those.</p>
    </div>
    <div class="ticket-wrap">
      <article class="ticket" aria-label="Work order">
        <header class="t-head">
          <div><div class="t-title">Work order</div><div class="t-sub">Built for Main Street &middot; Los Angeles</div></div>
          <div class="t-no">No. 0001</div>
        </header>
        <div class="t-meta"><span>Customer: <b>your shop</b></span><span>Due: <b>2 weeks</b></span></div>
        <div class="t-group">Get found</div>
        <ul class="t-items">
          <li><i></i>A page for every service you offer</li>
          <li><i></i>A page for every town you drive to</li>
          <li><i></i>Written so AI assistants can read you</li>
          <li><i></i>Google listing claimed in your name</li>
        </ul>
        <div class="t-group">Get reached</div>
        <ul class="t-items">
          <li><i></i>Tap to call on every page</li>
          <li><i></i>Quote form, tested before launch</li>
          <li><i></i>Hours right on the site and on Google</li>
        </ul>
        <div class="t-tot" id="pricing">
          <div class="ln"><span>Build</span><span class="f"></span><b>$1,000</b></div>
          <div class="ln"><span>Upkeep</span><span class="f"></span><b>$199/mo</b></div>
          <div class="ln"><span>Terms</span><span class="f"></span><b>30 days&rsquo; notice</b></div>
        </div>
        <p class="t-fine">$1,000 covers up to 8 services and 6 towns. Smaller shops are $600
        with the first year of upkeep paid up front ($1,990). Bigger shops, we quote. We
        settle it on the first call and it doesn&rsquo;t change.</p>
        <p class="t-fine">Upkeep covers hosting, edits, and a monthly report on what the AI
        assistants say about you. We build and host the site; the domain is registered in
        your name. After a year you can buy the site outright for $2,000.</p>
        <div class="stamp">No account<br>managers</div>
      </article>
    </div>
  </div>
</section>

<section class="band end" id="start">
  <div class="wrap">
    <h2>Find out where you stand.</h2>
    {end_desk}
    {end_mob}
    <div class="duo close">
      <div class="words">
        <p class="lead">Tell us your shop and your town. We look you up, run the check, and
        send you what we find. If everything&rsquo;s already working, we&rsquo;ll say so.</p>
        <p class="alt">Rather email? <a href="mailto:hello@builtformainstreet.com">hello@builtformainstreet.com</a></p>
      </div>
      <form id="askform" name="free-check" method="POST" target="lead-sink" action="https://script.google.com/macros/s/PASTE_YOUR_SCRIPT_ID/exec">
        <input type="hidden" name="subject" id="f-subject" data-remove-prefix value="New free check request">
        <p class="hp" aria-hidden="true"><label for="hp">Leave this empty</label><input id="hp" name="company-url" tabindex="-1" autocomplete="off"></p>
        <div><label for="f-name">Your name</label><input type="text" id="f-name" name="name" required placeholder="Jim Hoffman"></div>
        <div><label for="f-biz">Shop</label><input type="text" id="f-biz" name="business" required placeholder="Hoffman &amp; Sons"></div>
        <div><label for="f-town">Town</label><input type="text" id="f-town" name="town" placeholder="Fort Wayne, IN"></div>
        <div><label for="f-phone">Best number</label><input type="tel" id="f-phone" name="phone" required placeholder="(260) 555-0100"></div>
        <div class="full"><label for="f-email">Email (optional)</label><input type="email" id="f-email" name="email" placeholder="jim@hoffmanandsons.com" autocomplete="email"></div>
        <div class="full"><button class="btn" type="submit" id="send">Send it over</button></div>
        <p class="fnote" id="fnote" aria-live="polite">We&rsquo;ll run the check and get back to you. We won&rsquo;t put you on a mailing list.</p>
      </form>
      <iframe name="lead-sink" id="lead-sink" title="Form receiver" hidden></iframe>
    </div>
  </div>
</section>

</main>

<footer class="wrap">
  <div class="fgrid">
    <div>
      <a class="mark" href="#top">BUILT FOR MAIN <span class="st">STREET</span></a>
      <p>Websites and Google listings for local trade shops, so the people looking for your
      work find it and can reach you.</p>
    </div>
    <div class="fcontact">
      <a href="mailto:hello@builtformainstreet.com">hello@builtformainstreet.com</a>
      <span>Based in Los Angeles. We work with shops anywhere in the US.</span>
    </div>
  </div>
  <div class="fbot">&copy; 2026 Built for Main Street &middot; Los Angeles, California</div>
</footer>

<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"ProfessionalService","name":"Built for Main Street",
"description":"Websites and Google Business Profile work for local trade shops, so search engines and AI assistants can find them and customers can reach them.",
"url":"https://builtformainstreet.com","email":"hello@builtformainstreet.com",
"priceRange":"$600-$1500","areaServed":{{"@type":"Country","name":"United States"}},
"address":{{"@type":"PostalAddress","addressLocality":"Los Angeles","addressRegion":"CA","addressCountry":"US"}},
"hasOfferCatalog":{{"@type":"OfferCatalog","name":"Services","itemListElement":[
{{"@type":"Offer","name":"Visibility Check","price":"0","priceCurrency":"USD","itemOffered":{{"@type":"Service","name":"Visibility Check"}}}},
{{"@type":"Offer","name":"Build and fix","price":"600","priceCurrency":"USD","itemOffered":{{"@type":"Service","name":"Website build and Google Business Profile setup"}}}},
{{"@type":"Offer","name":"Keep it found","price":"199","priceCurrency":"USD","itemOffered":{{"@type":"Service","name":"Hosting, edits and monthly visibility report"}}}}]}}}}
</script>
<script>
{open('site/www/src/app.js').read()}
</script>
'''

HEAD_NOTE = '''<!--
  Built for Main Street. One file, no build step.

  GO LIVE
  1. Leads to your inbox. Open site/www/lead-to-email.gs and follow the five
     steps at the top. It ends with a URL. Paste it over
     https://script.google.com/macros/s/PASTE_YOUR_SCRIPT_ID/exec below.
     Every lead is emailed to hello@builtformainstreet.com from your own Google
     account and added as a row to a Google Sheet you own.
  2. Drag the site/www folder onto app.netlify.com/drop.
  3. Netlify > Domain management > Add a domain > www.builtformainstreet.com.
     At Namecheap > Advanced DNS: A record, host @, value 75.2.60.5;
     CNAME record, host www, value <your-site>.netlify.app. Leave MX records alone.
  4. Fill in the form on the live site once. Confirm the email and the Sheet row.
-->
'''
art = CSS + BODY
full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + HEAD_NOTE + CSS + '</head>\n<body>\n' + BODY + '\n</body>\n</html>\n')
d='output/'
io.open(d+'mainstreet.html','w',encoding='utf-8').write(art)
io.open('/home/user/builtfor/site/www/index.html','w',encoding='utf-8').write(full)
print('built', len(full))
