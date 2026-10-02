"""Build the K7c motion prototype: hero load sequence, provider network flow, scroll reveal."""

import base64
import pathlib

HERE = pathlib.Path(__file__).parent
BK = HERE.parent.parent
WEB = BK.parent / "apps" / "web" / "public"


def data(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()


A = {
    "logo": data(BK / "family/lockup/better-payment-horizontal-color.svg", "image/svg+xml"),
    "symbolWhite": data(BK / "family/symbol/better-payment-symbol-white.svg", "image/svg+xml"),
    "hero": data(BK / "visual/hero/web-hero-A3.jpg", "image/jpeg"),
    "iyzico": data(WEB / "iyzico.svg", "image/svg+xml"),
    "paytr": data(WEB / "paytr.svg", "image/svg+xml"),
    "param": data(WEB / "param.svg", "image/svg+xml"),
    "akbank": data(WEB / "akbank.svg", "image/svg+xml"),
}
for n in ("unified-api", "callback", "events"):
    A["v_" + n] = data(BK / f"visual/anim/web/icon-{n}.mp4", "video/mp4")
    A["p_" + n] = data(BK / f"visual/anim/web/icon-{n}-poster.png", "image/png")

CHEV = '<svg class="ic chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
GH = '<svg class="ic brand" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>'

CSS = r"""
:root{--canvas:#F8F8FC;--surface:#FFF;--ink:#13132B;--muted:#5A5A78;--line:#E4E3F0;--line-strong:#CFCDE6;--indigo:#4338F2;--indigo-hover:#3A2FE0;--tint:#ECEAFF;
--success:#087A55;--success-bg:#E6F5EF;--warning:#A86207;--warning-bg:#FDF3E3;
--display:"Manrope",sans-serif;--body:"Inter",sans-serif;--mono:"JetBrains Mono",monospace;
/* motion tokens */
--d-xs:140ms;--d-sm:240ms;--d-md:450ms;--d-lg:700ms;--d-xl:900ms;--d-art:1600ms;
--e-std:cubic-bezier(.16,1,.3,1);--e-spring:cubic-bezier(.34,1.56,.64,1);--e-exit:cubic-bezier(.4,0,1,1);--rise:18px}
*{box-sizing:border-box}html,body{margin:0}body{background:var(--canvas);color:var(--ink);font-family:var(--body);-webkit-font-smoothing:antialiased;overflow-x:hidden}
.ic{width:16px;height:16px;flex:none}
/* buttons (K7a) */
.btn{position:relative;display:inline-flex;align-items:center;gap:8px;height:46px;padding:0 20px;border-radius:12px;font:500 15px/1 var(--body);text-decoration:none;white-space:nowrap;overflow:hidden;isolation:isolate;border:1px solid transparent;transition:background .2s,border-color .2s,box-shadow .25s}
.btn.sm{height:36px;padding:0 14px;font-size:13.5px;border-radius:10px}
.btn::after{content:"";position:absolute;inset:-1px;border-radius:inherit;pointer-events:none;background:linear-gradient(105deg,transparent 30%,var(--sheen) 47%,var(--sheen-soft) 53%,transparent 68%);transform:translateX(-130%)}
.btn .ic{transition:transform .35s var(--e-spring)}
.btn:is(:hover,:focus-visible)::after{transform:translateX(130%);transition:transform var(--d-xl) var(--e-std)}
.btn:is(:hover,:focus-visible) .chev{transform:translateX(4px)}.btn:is(:hover,:focus-visible) .brand{transform:rotate(-8deg) scale(1.08)}
.btn:focus-visible{outline:2px solid var(--indigo);outline-offset:3px}
.btn.pri{background:var(--indigo);color:#fff;--sheen:rgba(255,255,255,.55);--sheen-soft:rgba(255,255,255,.18);box-shadow:0 1px 0 #ffffff33 inset,0 6px 16px -6px #4338F2aa}
.btn.pri:not(:hover):not(:focus-visible)::after{animation:idle-sheen 4.5s var(--e-std) infinite 1.8s}
.btn.pri:hover{background:var(--indigo-hover)}
@keyframes idle-sheen{0%{transform:translateX(-130%)}22%,100%{transform:translateX(130%)}}
.btn.sec{background:#ffffffd9;color:var(--ink);border-color:var(--line);--sheen:rgba(67,56,242,.14);--sheen-soft:rgba(67,56,242,.05)}

/* control bar */
.ctrl{position:fixed;z-index:50;right:16px;bottom:16px;display:flex;gap:8px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:8px;box-shadow:0 10px 30px -12px #13132B33;font:500 13px var(--body)}
.ctrl button{font:inherit;border:1px solid var(--line);background:var(--canvas);border-radius:9px;padding:7px 11px;cursor:pointer}.ctrl button[aria-pressed=true]{background:var(--ink);color:#fff;border-color:var(--ink)}

/* nav */
.nav{position:sticky;top:0;z-index:20;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:14px max(20px,calc((100vw - 1180px)/2));background:rgba(248,248,252,.72);backdrop-filter:blur(14px) saturate(1.4);border-bottom:1px solid transparent;transition:border-color var(--d-md)}
.nav.scrolled{border-color:rgba(228,227,240,.9)}
.nav img{height:24px;display:block}.nav ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-size:14.5px}.nav ul a{color:var(--muted);text-decoration:none}
.nav .act{display:flex;gap:8px;align-items:center}

/* hero */
.hero{position:relative;min-height:calc(100vh - 64px);max-height:900px;overflow:hidden}
.hero .art{position:absolute;inset:0;background:var(--canvas) center bottom/cover no-repeat;}
.hero .in{position:relative;max-width:1180px;margin:0 auto;padding:72px 20px 0;display:grid;grid-template-columns:1.05fr .95fr;gap:40px;align-items:center}
.hero h1{font:800 clamp(38px,5vw,62px)/1.03 var(--display);letter-spacing:-.035em;margin:0 0 18px}
.hero h1 .l{display:block}.hero h1 .l2{color:var(--muted)}
.hero p.lead{font-size:18px;line-height:1.6;color:var(--muted);margin:0 0 28px;max-width:520px}
.btns{display:flex;gap:12px;flex-wrap:wrap}
.install{margin-top:18px;display:inline-flex;gap:10px;font:14px var(--mono);background:#ffffffcc;border:1px solid var(--line);border-radius:10px;padding:10px 14px}.install b{color:var(--muted);font-weight:400}

/* load sequence */
.seq{opacity:0;transform:translateY(var(--rise))}
.play .seq{animation:enter var(--d-lg) var(--e-std) forwards;animation-delay:var(--at,0ms)}
.play .art{animation:art var(--d-art) var(--e-std) both}
@keyframes enter{to{opacity:1;transform:none}}
@keyframes art{from{opacity:0;transform:translateY(24px) scale(1.02)}to{opacity:1;transform:none}}

/* network */
.net{position:relative;width:100%;max-width:470px;aspect-ratio:47/40;justify-self:end}
.net svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.net .wire{fill:none;stroke:#D9D6F2;stroke-width:1.6;stroke-dasharray:4 6}
.net .wire.on{stroke:var(--indigo);stroke-dasharray:none;stroke-width:2;transition:stroke var(--d-sm)}
.net .dot{fill:var(--indigo)}.net .dot.back{fill:var(--success)}
.net .halo{fill:var(--indigo);opacity:.18}.net .halo.back{fill:var(--success)}
.hub{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:10px;background:var(--indigo);color:#fff;border-radius:16px;padding:13px 16px;font:600 14px var(--mono);box-shadow:0 14px 30px -12px #4338F2;z-index:2}
.hub img{width:22px;height:22px}
.chip{position:absolute;left:50%;top:calc(50% + 38px);transform:translate(-50%,6px);opacity:0;display:inline-flex;align-items:center;gap:6px;font:600 12px var(--body);padding:6px 10px;border-radius:999px;white-space:nowrap;transition:opacity var(--d-md) var(--e-std),transform var(--d-md) var(--e-spring);z-index:2}
.chip.show{opacity:1;transform:translate(-50%,0)}
.chip.req{background:#fff;color:var(--muted);border:1px solid var(--line)}.chip.ok{background:var(--success-bg);color:var(--success)}
.chip i{width:6px;height:6px;border-radius:50%;background:currentColor}
.pnode{position:absolute;transform:translate(-50%,-50%);display:flex;align-items:center;gap:10px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:8px 12px 8px 8px;cursor:pointer;font:inherit;color:inherit;z-index:2;transition:border-color var(--d-sm),box-shadow var(--d-md) var(--e-std),transform var(--d-md) var(--e-spring)}
.pnode .lg{width:38px;height:38px;border-radius:9px;background:var(--canvas);border:1px solid var(--line);display:grid;place-items:center}.pnode .lg img{width:32px;height:18px;object-fit:contain}
.pnode b{font:700 13.5px var(--display)}
.pnode.on{border-color:var(--indigo);box-shadow:0 0 0 5px var(--tint);transform:translate(-50%,-50%) scale(1.04)}
.pnode.ok{border-color:var(--success);box-shadow:0 0 0 5px var(--success-bg)}
.pnode:focus-visible{outline:2px solid var(--indigo);outline-offset:3px}
.tip{position:absolute;z-index:5;max-width:220px;background:var(--ink);color:#fff;font:12.5px/1.45 var(--body);padding:8px 10px;border-radius:9px;pointer-events:none;opacity:0;transform:translateY(4px);transition:opacity var(--d-sm),transform var(--d-sm)}
.tip.show{opacity:1;transform:none}

/* sections */
section.s{max-width:1180px;margin:0 auto;padding:96px 20px}
.sh h2{font:800 clamp(28px,3.4vw,40px)/1.08 var(--display);letter-spacing:-.03em;margin:0 0 12px;max-width:640px}.sh p{color:var(--muted);margin:0 0 36px;max-width:560px;line-height:1.6;font-size:17px}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.feat{background:#fff;border:1px solid var(--line);border-radius:16px;padding:22px;transition:transform .35s var(--e-spring),box-shadow .3s var(--e-std)}
.feat:hover{transform:translateY(-3px);box-shadow:0 10px 30px -14px rgba(19,19,43,.22)}
.feat video{width:96px;height:96px;mix-blend-mode:multiply;margin:-6px 0 10px -8px;display:block}
.feat h3{font:700 17px var(--display);margin:0 0 6px}.feat p{margin:0;color:var(--muted);line-height:1.55;font-size:14.5px}
/* scroll reveal */
.rv{opacity:0;transform:translateY(22px);transition:opacity var(--d-lg) var(--e-std),transform var(--d-lg) var(--e-std);transition-delay:var(--at,0ms)}
.rv.in{opacity:1;transform:none}
.flow{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.step{background:#fff;border:1px solid var(--line);border-radius:14px;padding:16px}.step small{font:600 12px var(--mono);color:var(--indigo)}.step h4{font:700 15px var(--display);margin:6px 0 4px}.step p{margin:0;color:var(--muted);font-size:13.5px;line-height:1.5}
.spec{max-width:1180px;margin:0 auto 120px;padding:0 20px}.spec table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;font-size:14px}
.spec th,.spec td{text-align:left;padding:10px 14px;border-bottom:1px solid var(--line)}.spec th{font:600 12.5px var(--body);color:var(--muted);background:var(--canvas)}.spec code{font:12.5px var(--mono)}

/* reduced motion: real preference or the prototype toggle */
@media (prefers-reduced-motion:reduce){:root{--rm:1}}
.rm .seq,.rm .rv{opacity:1!important;transform:none!important;animation:none!important;transition:none!important}
.rm .art{animation:none!important}.rm .btn::after{display:none}.rm .net .dot,.rm .net .halo{display:none}.rm .chip{opacity:1;transform:translate(-50%,0)}
.rm .net .wire{stroke:var(--line-strong);stroke-dasharray:none}

@media(max-width:900px){.nav ul{display:none}.nav .act .sec{display:none}.hero{max-height:none;min-height:0}.hero .in{grid-template-columns:1fr;padding-top:40px}.net{justify-self:center;max-width:420px}.cards,.flow{grid-template-columns:1fr}section.s{padding:64px 20px}.hero .art{background-size:250% auto;background-position:42% 100%}.hero .in{padding-bottom:210px;gap:28px}.net{aspect-ratio:47/50}.pnode{padding:6px 10px 6px 6px;gap:8px}.pnode .lg{width:30px;height:30px}.pnode .lg img{width:26px;height:15px}.pnode b{font-size:12.5px}.hub{padding:10px 12px;font-size:12.5px;gap:8px}.hub img{width:18px;height:18px}.chip{top:calc(50% + 32px);font-size:11.5px}}
"""

PNODES = [("iyzico", "iyzico", 16, 18, "3DS · Non-3D · İade · İptal · BIN · Taksit"),
          ("paytr", "PayTR", 84, 18, "3DS iFrame · Non-3D · İade · BIN · Taksit"),
          ("param", "Parampos", 16, 82, "TP_WMD_UCD · Non-3D (TRY) · İade · İptal · BIN"),
          ("akbank", "Akbank", 84, 82, "3D_PAY · Non-3D · İade · İptal")]
nodes = "".join(
    f'<button class="pnode" data-i="{i}" data-caps="{caps}" style="left:{x}%;top:{y}%" aria-label="{name}: {caps}"><span class="lg"><img src="{A[k]}" alt=""></span><b>{name}</b></button>'
    for i, (k, name, x, y, caps) in enumerate(PNODES)
)

BODY = f"""
<div class="ctrl" role="group" aria-label="Prototip kontrolleri"><button id="replay">Açılışı tekrar oynat</button><button id="rm" aria-pressed="false">Hareketi azalt</button></div>
<nav class="nav" id="nav"><img src="{A['logo']}" alt="Better Payment"><ul><li><a href="#">Dokümantasyon</a></li><li><a href="#">Sağlayıcılar</a></li><li><a href="#">Örnekler</a></li><li><a href="#">Blog</a></li></ul>
<div class="act"><a class="btn sec sm" href="#">{GH}<span>GitHub</span></a><a class="btn pri sm" href="#"><span>Başla</span>{CHEV}</a></div></nav>
<header class="hero" id="hero"><div class="art" style="background-image:url({A['hero']})"></div>
<div class="in"><div>
<h1><span class="l seq" style="--at:300ms">Türkiye'nin ödeme sağlayıcıları.</span><span class="l l2 seq" style="--at:440ms">Tek TypeScript API'si.</span></h1>
<p class="lead seq" style="--at:600ms">iyzico, PayTR, Parampos ve Akbank için aynı istek ve sonuç tipleri. Her callback senin anahtarlarınla doğrulanır.</p>
<div class="btns seq" style="--at:760ms"><a class="btn pri" href="#"><span>Dokümantasyonu aç</span>{CHEV}</a><a class="btn sec" href="#">{GH}<span>GitHub'da incele</span></a></div>
<div class="install seq" style="--at:900ms"><b>$</b>npm install better-payment</div></div>
<div class="net seq" id="net" style="--at:1000ms"><svg viewBox="0 0 470 400" aria-hidden="true"><g id="wires"></g><g id="dots"></g></svg>
<div class="hub"><img src="{A['symbolWhite']}" alt="">betterPayment()</div><div class="chip" id="chip"></div>{nodes}<div class="tip" id="tip"></div></div>
</div></header>

<section class="s"><div class="sh rv"><h2>Callback'e güvenme, doğrula.</h2><p>Her bildirim senin anahtarlarınla kontrol edilir; eşleşmeyen hiçbir şey başarılı sayılmaz.</p></div>
<div class="cards">
<article class="feat rv" style="--at:0ms"><video src="{A['v_unified-api']}" poster="{A['p_unified-api']}" autoplay muted loop playsinline aria-hidden="true"></video><h3>Tek API, dört sağlayıcı</h3><p>Aynı istek ve sonuç tipleri, her sağlayıcıda.</p></article>
<article class="feat rv" style="--at:110ms"><video src="{A['v_callback']}" poster="{A['p_callback']}" autoplay muted loop playsinline aria-hidden="true"></video><h3>Callback'ler doğrulanır</h3><p>İmza senin kimlik bilgilerinle kontrol edilir.</p></article>
<article class="feat rv" style="--at:220ms"><video src="{A['v_events']}" poster="{A['p_events']}" autoplay muted loop playsinline aria-hidden="true"></video><h3>Tek event akışı</h3><p>Doğrulanmış sonuçlar tek listener'a düşer.</p></article>
</div></section>

<section class="s" style="padding-top:0"><div class="sh rv"><h2>Bir ödemenin yolculuğu.</h2><p>Hero'daki akışın adım adım hali; her adım kaydırdıkça sırayla belirir.</p></div>
<div class="flow">
<div class="step rv" style="--at:0ms"><small>01 · istek</small><h4>initThreeDSPayment()</h4><p>Aynı tiple sağlayıcıya gider.</p></div>
<div class="step rv" style="--at:110ms"><small>02 · pending</small><h4>3D Secure</h4><p>Müşteri bankada doğrular.</p></div>
<div class="step rv" style="--at:220ms"><small>03 · callback</small><h4>İmza kontrolü</h4><p>Senin anahtarlarınla doğrulanır.</p></div>
<div class="step rv" style="--at:330ms"><small>04 · success</small><h4>payment.succeeded</h4><p>Tek listener'a düşer.</p></div>
</div></section>

<div class="spec rv"><table><thead><tr><th>Hareket</th><th>Süre / easing</th><th>Not</th></tr></thead><tbody>
<tr><td>Hero açılışı</td><td><code>art 1600ms · metin 700ms, 130–160ms aralık · ease-out-expo</code></td><td>artwork yükselerek, metin 18 px aşağıdan</td></tr>
<tr><td>Sağlayıcı akışı</td><td><code>istek 1300ms · bekleme 600ms · dönüş 1300ms · ara 2200ms · döngü ~5.4s</code></td><td>sırayla dört sağlayıcı; hover/focus o sağlayıcıyı hemen oynatır</td></tr>
<tr><td>Durum çipi</td><td><code>450ms + spring</code></td><td>istek: gri · dönüş: yeşil "doğrulandı"</td></tr>
<tr><td>Bölüm reveal</td><td><code>700ms, 110ms kademe</code></td><td>görünür olunca bir kez; 22 px</td></tr>
<tr><td>Navbar</td><td><code>320ms</code></td><td>kaydırınca alt çizgi belirir</td></tr>
<tr><td>Hareketi azalt</td><td>—</td><td>her şey son halinde, akış noktaları gizli, çip statik</td></tr>
</tbody></table></div>
"""

JS = r"""
const root=document.documentElement, hero=document.getElementById('hero');
const sysRM=matchMedia('(prefers-reduced-motion: reduce)').matches; if(sysRM){root.classList.add('rm');document.getElementById('rm').setAttribute('aria-pressed','true')}
function play(){hero.classList.remove('play');void hero.offsetWidth;hero.classList.add('play')}
requestAnimationFrame(play);
document.getElementById('replay').onclick=()=>{play();restartFlow()};
document.getElementById('rm').onclick=e=>{const on=root.classList.toggle('rm');e.currentTarget.setAttribute('aria-pressed',on);restartFlow()};
document.querySelectorAll('a[href="#"]').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));
const nav=document.getElementById('nav');addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>8),{passive:true});
// scroll reveal
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting||e.boundingClientRect.top<0){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.15});
addEventListener('scroll',()=>document.querySelectorAll('.rv:not(.in)').forEach(el=>{if(el.getBoundingClientRect().top<innerHeight*.85){el.classList.add('in');io.unobserve(el)}}),{passive:true});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
// network
const NS='http://www.w3.org/2000/svg', net=document.getElementById('net'), svg=net.querySelector('svg');
const W=470,H=400,HUB={x:W/2,y:H/2};
const nodes=[...net.querySelectorAll('.pnode')], wiresG=svg.querySelector('#wires'), dotsG=svg.querySelector('#dots'), chip=document.getElementById('chip'), tip=document.getElementById('tip');
const wires=nodes.map(n=>{const x=parseFloat(n.style.left)/100*W,y=parseFloat(n.style.top)/100*H;const mx=(x+HUB.x)/2;
 const p=document.createElementNS(NS,'path');p.setAttribute('d',`M${HUB.x},${HUB.y} C${mx},${HUB.y} ${mx},${y} ${x},${y}`);p.setAttribute('class','wire');wiresG.appendChild(p);return p});
const names=['iyzico','PayTR','Parampos','Akbank'];
let timer=null, idx=0, gen=0;
function dot(cls){const g=document.createElementNS(NS,'g');const h=document.createElementNS(NS,'circle');h.setAttribute('r',11);h.setAttribute('class','halo '+cls);const c=document.createElementNS(NS,'circle');c.setAttribute('r',5);c.setAttribute('class','dot '+cls);g.append(h,c);dotsG.appendChild(g);return g}
function travel(path,reverse,cls,ms,my){return new Promise(res=>{const g=dot(cls),L=path.getTotalLength(),t0=performance.now();
 function step(t){if(my!==gen){g.remove();return res(false)}let k=Math.min(1,(t-t0)/ms);const e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;const pt=path.getPointAtLength((reverse?1-e:e)*L);g.setAttribute('transform',`translate(${pt.x},${pt.y})`);
  if(k<1)requestAnimationFrame(step);else{g.remove();res(true)}}requestAnimationFrame(step)})}
function setChip(kind,text){chip.className='chip '+kind+' show';chip.innerHTML='<i></i>'+text}
async function run(i,my){
 const rm=root.classList.contains('rm');nodes.forEach(n=>n.classList.remove('on','ok'));wires.forEach(w=>w.classList.remove('on'));
 if(rm){setChip('ok','tek API · 4 sağlayıcı');return}
 const w=wires[i],n=nodes[i];w.classList.add('on');setChip('req','istek → '+names[i]);
 if(!await travel(w,false,'',1300,my))return;n.classList.add('on');await new Promise(r=>setTimeout(r,600));if(my!==gen)return;
 n.classList.remove('on');n.classList.add('ok');if(!await travel(w,true,'back',1300,my))return;
 setChip('ok','✓ doğrulandı · success · '+names[i]);w.classList.remove('on');
}
async function loop(my){await run(idx,my);if(my!==gen)return;idx=(idx+1)%4;timer=setTimeout(()=>loop(my),2200)}
function startAt(i,delay){gen++;const my=gen;clearTimeout(timer);dotsG.innerHTML='';idx=i;timer=setTimeout(()=>loop(my),delay)}
function restartFlow(){startAt(0,root.classList.contains('rm')?0:1900)}
restartFlow();
nodes.forEach((n,i)=>{const show=()=>{const r=n.getBoundingClientRect(),q=net.getBoundingClientRect();tip.textContent=n.dataset.caps;tip.style.left=(r.left-q.left)+'px';tip.style.top=(r.bottom-q.top+8)+'px';tip.classList.add('show')};
 const hide=()=>tip.classList.remove('show');
 n.addEventListener('mouseenter',show);n.addEventListener('focus',show);n.addEventListener('mouseleave',hide);n.addEventListener('blur',hide);
 n.addEventListener('click',()=>startAt(i,0))});
"""

html = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    "<title>Better Payment · Motion Prototipi</title>"
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&family=JetBrains+Mono:wght@400;500;600&display=swap">'
    f"<style>{CSS}</style></head><body>{BODY}<script>{JS}</script></body></html>"
)
out = HERE / "motion-prototip-v1.html"
out.write_text(html, encoding="utf-8")
print(out.name, len(html) // 1024, "KB")
