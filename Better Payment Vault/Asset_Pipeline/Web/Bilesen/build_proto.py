import base64
import pathlib


def b(p, m="image/jpeg"):
    return f"data:{m};base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode()


logo = b("../../family/lockup/better-payment-horizontal-color.svg", "image/svg+xml")
A2, A3 = b("web-hero-A2.jpg"), b("web-hero-A3.jpg")
chev = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
gh = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>'


def btn(cls, label, icon, lead=False):
    inner = (icon + f"<span>{label}</span>") if lead else (f"<span>{label}</span>" + icon)
    return (
        f'<button class="btn {cls}"><span class="clip"><span class="row">{inner}</span>'
        f'<span class="row ghost" aria-hidden="true">{inner}</span></span></button>'
    )


PRI = btn("pri", "Dokümantasyonu aç", chev)
SEC = btn("sec", "GitHub'da incele", gh, lead=True)

CSS = """
:root{--canvas:#F8F8FC;--ink:#13132B;--muted:#5A5A78;--line:#E4E3F0;--indigo:#4338F2;--indigo-hover:#3A2FE0;--tint:#ECEAFF;--spring:cubic-bezier(.34,1.56,.64,1)}
*{box-sizing:border-box}body{margin:0;background:#EEEEF4;color:var(--ink);font-family:Inter,system-ui,sans-serif}
.page{max-width:1240px;margin:0 auto;padding:28px 16px 48px}
.bar{display:flex;flex-wrap:wrap;gap:18px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:14px;padding:12px 16px;margin-bottom:14px;font-size:13.5px}
.bar b{font-weight:600}.seg{display:inline-flex;background:var(--canvas);border:1px solid var(--line);border-radius:10px;padding:3px}
.seg button{font:inherit;border:0;background:none;padding:6px 12px;border-radius:7px;cursor:pointer;color:var(--muted)}.seg button[aria-pressed=true]{background:#fff;color:var(--ink);box-shadow:0 1px 2px #0001}
.frame{position:relative;aspect-ratio:16/9;background-size:cover;background-position:center;border-radius:18px;overflow:hidden;border:1px solid var(--line)}
nav{position:absolute;left:5%;right:5%;top:5.5%;display:flex;justify-content:space-between;align-items:center}nav img{height:clamp(16px,2.1vw,28px)}
nav ul{display:flex;gap:2.2vw;list-style:none;margin:0;padding:0;font-size:clamp(10px,1.05vw,14.5px);color:var(--muted)}
.copy{position:absolute;left:5%;top:20%;max-width:48%}
.copy h1{font-family:Manrope;font-weight:800;letter-spacing:-.035em;line-height:1.03;font-size:clamp(22px,4vw,56px);margin:0 0 1.3vw}.copy h1 span{color:var(--muted)}
.copy p{font-size:clamp(11px,1.25vw,17px);line-height:1.55;color:var(--muted);margin:0 0 2vw;max-width:520px}
.btns{display:flex;gap:12px;flex-wrap:wrap}
.install{margin-top:16px;display:inline-flex;gap:10px;font:clamp(10px,1vw,14px) "JetBrains Mono",monospace;background:#ffffffcc;border:1px solid var(--line);border-radius:10px;padding:9px 13px}.install b{color:var(--muted);font-weight:400}
.btn{--h:46px;position:relative;height:var(--h);padding:0 20px;border-radius:12px;font:500 15px/1 Inter,sans-serif;cursor:pointer;border:1px solid transparent;display:inline-flex;align-items:center;transition:background .2s,border-color .2s}
.btn .clip{position:relative;display:block;height:20px;overflow:hidden}
.btn .row{display:flex;align-items:center;gap:8px;height:20px;white-space:nowrap}
.btn .ghost{position:absolute;left:0;top:0;transform:translateY(130%)}
.btn .ic{width:16px;height:16px;flex:none}
.btn.pri{background:var(--indigo);color:#fff;box-shadow:0 1px 0 #ffffff33 inset,0 6px 16px -6px #4338F2aa}.btn.pri:hover{background:var(--indigo-hover)}
.btn.sec{background:#fff;color:var(--ink);border-color:var(--line)}.btn.sec:hover{border-color:#CFCDE6}
.btn:focus-visible{outline:2px solid var(--indigo);outline-offset:3px}.btn:active{transform:translateY(1px)}
.btn.sm{--h:36px;padding:0 14px;font-size:13.5px;border-radius:10px}.btn.lg{--h:54px;padding:0 26px;font-size:16.5px;border-radius:14px}
/* hop: up and out, falls back from above with a small bounce */
[data-m=hop] .btn:hover .row:not(.ghost),[data-m=hop] .btn:focus-visible .row:not(.ghost){animation:hop .62s both}
@keyframes hop{0%{transform:translateY(0);animation-timing-function:cubic-bezier(.4,0,1,1)}30%{transform:translateY(-130%)}30.01%{transform:translateY(-130%);animation-timing-function:cubic-bezier(.2,.8,.3,1)}62%{transform:translateY(12%)}80%{transform:translateY(-5%)}100%{transform:translateY(0)}}
/* roll: content slides up, its copy enters from below with a spring */
[data-m=roll] .btn .row{transition:transform .45s var(--spring)}
[data-m=roll] .btn:hover .row:not(.ghost){transform:translateY(-130%)}[data-m=roll] .btn:hover .ghost{transform:translateY(0)}
/* nudge: only the icon moves */
[data-m=nudge] .btn .ic{transition:transform .35s var(--spring)}
[data-m=nudge] .btn.pri:hover .row:not(.ghost) .ic{transform:translateX(4px)}
[data-m=nudge] .btn.sec:hover .row:not(.ghost) .ic{transform:rotate(-8deg) scale(1.08)}
/* shine family: a diagonal light sheen sweeps across once per hover */
.btn{overflow:hidden;isolation:isolate}
.btn::after{content:"";position:absolute;inset:-1px;border-radius:inherit;pointer-events:none;z-index:-0;
  background:linear-gradient(105deg,transparent 30%,var(--sheen) 47%,var(--sheen-soft) 53%,transparent 68%);
  transform:translateX(-130%);opacity:0}
.btn.pri{--sheen:rgba(255,255,255,.55);--sheen-soft:rgba(255,255,255,.18)}
.btn.sec{--sheen:rgba(67,56,242,.14);--sheen-soft:rgba(67,56,242,.05)}
.dark .btn.sec{--sheen:rgba(255,255,255,.22);--sheen-soft:rgba(255,255,255,.06)}
:is([data-m=shine],[data-m=shine-chev],[data-m=shine-idle]) .btn:is(:hover,:focus-visible)::after{opacity:1;transform:translateX(130%);transition:transform .75s cubic-bezier(.2,.7,.2,1),opacity .1s}
[data-m=shine-chev] .btn .ic{transition:transform .35s var(--spring)}
[data-m=shine-chev] .btn.pri:hover .row:not(.ghost) .ic,[data-m=shine-chev] .btn.sec:hover .row:not(.ghost) .ic:last-child{transform:translateX(3px)}
[data-m=shine-idle] .btn.pri:not(:hover)::after{opacity:1;animation:idle-sheen 4.5s cubic-bezier(.2,.7,.2,1) infinite 1s}
@keyframes idle-sheen{0%{transform:translateX(-130%)}22%{transform:translateX(130%)}100%{transform:translateX(130%)}}
:is([data-m=shine],[data-m=shine-chev],[data-m=shine-idle]) .btn.pri:hover{box-shadow:0 1px 0 #ffffff40 inset,0 10px 24px -8px #4338F2cc}
@media (prefers-reduced-motion:reduce){.btn::after{display:none}}
@media (prefers-reduced-motion:reduce){.btn .row{animation:none!important;transition:none!important;transform:none!important}.btn .ghost{display:none}}
.lab{background:#fff;border:1px solid var(--line);border-radius:18px;padding:22px;margin-top:14px}
.lab h2{font-family:Manrope;font-size:18px;margin:0 0 4px}.lab p{color:var(--muted);margin:0 0 16px;font-size:14px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.cell{background:var(--canvas);border:1px solid var(--line);border-radius:14px;padding:22px;display:grid;gap:12px;justify-items:start}
.cell small{color:var(--muted);font-size:12px}.cell.dark{background:var(--ink)}.cell.dark small{color:#A8A8C0}
.dark .btn.sec{background:transparent;color:#fff;border-color:#ffffff33}.dark .btn.pri{box-shadow:none}
.note{margin-top:12px;font-size:13px;color:var(--muted);line-height:1.5}
@media(max-width:860px){.copy{max-width:80%;top:16%}.grid{grid-template-columns:1fr}nav ul{display:none}}
"""

BODY = f"""<div class="page" data-m="shine" id="root">
<div class="bar"><b>Hero:</b><span class="seg" id="hero"><button aria-pressed="true" data-v="A2">A2 · sağ alt</button><button aria-pressed="false" data-v="A3">A3 · alt bant</button></span>
<b>Buton hover:</b><span class="seg" id="motion"><button aria-pressed="true" data-v="shine">Parıltı</button><button aria-pressed="false" data-v="shine-chev">Parıltı + chevron</button><button aria-pressed="false" data-v="shine-idle">Sürekli ışıltı</button><button aria-pressed="false" data-v="hop">Zıpla ve düş</button><button aria-pressed="false" data-v="roll">Yuvarla</button></span></div>
<div class="frame" id="frame">
<nav><img src="{logo}" alt="Better Payment"><ul><li>Dokümantasyon</li><li>Sağlayıcılar</li><li>Örnekler</li><li>GitHub</li></ul></nav>
<div class="copy"><h1>Türkiye'nin ödeme sağlayıcıları.<br><span>Tek TypeScript API'si.</span></h1>
<p>iyzico, PayTR, Parampos ve Akbank için aynı istek ve sonuç tipleri. Her callback senin anahtarlarınla doğrulanır.</p>
<div class="btns">{PRI}{SEC}</div><div class="install"><b>$</b>npm install better-payment</div></div></div>
<section class="lab"><h2>Buton laboratuvarı</h2><p>Üzerine gel ve hareketi dene. Klavyede Tab ile odak halkasını gör. Sistemde "hareketi azalt" açıksa animasyon kapanır.</p>
<div class="grid">
<div class="cell"><small>Primary · sm / md / lg</small>{btn("pri sm", "Başla", chev)}{PRI}{btn("pri lg", "Dokümantasyonu aç", chev)}</div>
<div class="cell"><small>Secondary</small>{btn("sec sm", "GitHub", gh, True)}{SEC}{btn("sec", "npm'de gör", chev)}</div>
<div class="cell dark"><small>Koyu zemin</small>{PRI}{SEC}</div>
</div><p class="note">Zıpla ve düş: yazı ve ikon birlikte yukarı çıkar, yukarıdan hızla düşüp hafif sekmeyle oturur (0.62 sn). Yuvarla: içerik yukarı kayar, aynısı aşağıdan yaylı gelir (0.45 sn). Parıltı: çapraz ışık şeridi hover başına bir kez süzülür (0.75 sn), ana butonda gölge hafifçe derinleşir. Sürekli ışıltı: ana buton 4.5 sn arayla kendiliğinden parlar. Ok yerine chevron kullanıldı.</p></section>
</div>"""

JS = """const H={A2:"%s",A3:"%s"};
const frame=document.getElementById('frame');frame.style.backgroundImage='url('+H.A2+')';
function seg(id,fn){const bs=document.querySelectorAll('#'+id+' button');bs.forEach(b=>b.addEventListener('click',()=>{bs.forEach(x=>x.setAttribute('aria-pressed',x===b));fn(b.dataset.v)}))}
seg('hero',v=>frame.style.backgroundImage='url('+H[v]+')');
seg('motion',v=>document.getElementById('root').dataset.m=v);""" % (A2, A3)

html = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    "<title>Better Payment · Hero ve Buton Prototipi</title>"
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&family=JetBrains+Mono&display=swap">'
    f"<style>{CSS}</style></head><body>{BODY}<script>{JS}</script></body></html>"
)
pathlib.Path("hero-buton-prototip.html").write_text(html, encoding="utf-8")
print(len(html) // 1024, "KB")
