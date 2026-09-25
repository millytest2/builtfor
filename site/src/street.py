# The main street drawing, drawn once and cropped or lit per use.
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
  {t(88,'UPHOLSTERY')}{t(262,'TREE SERVICE')}{t(482,'WELDING')}{t(672,'MASONRY')}{t(862,fifth_label, dim=not fifth_lit)}
</svg>'''

