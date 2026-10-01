"""Build the self-contained Better Payment component specimen (Faz 4.5 · K7b)."""

import base64
import json
import pathlib
import subprocess

HERE = pathlib.Path(__file__).parent
BK = HERE.parent.parent
WEB = BK.parent / "apps" / "web" / "public"
MAGICK = r"C:\msys64\ucrt64\bin\magick.exe"


def data(path, mime):
    return f"data:{mime};base64," + base64.b64encode(pathlib.Path(path).read_bytes()).decode()


def icon(name, size=160):
    out = HERE / f"_i-{name}.png"
    subprocess.run(
        [MAGICK, str(BK / "visual" / "icons" / f"icon-{name}-cut.png"), "-trim", "+repage",
         "-resize", f"{size}x{size}", "-gravity", "center", "-background", "none",
         "-extent", f"{size}x{size}", str(out)],
        check=True,
    )
    uri = data(out, "image/png")
    out.unlink()
    return uri


ASSETS = {
    "logo": data(BK / "family/lockup/better-payment-horizontal-color.svg", "image/svg+xml"),
    "logoWhite": data(BK / "family/lockup/better-payment-horizontal-white.svg", "image/svg+xml"),
    "symbol": data(BK / "family/symbol/better-payment-symbol-color.svg", "image/svg+xml"),
    "hero": data(BK / "visual/hero/web-hero-A3.jpg", "image/jpeg"),
    "iyzico": data(WEB / "iyzico.svg", "image/svg+xml"),
    "paytr": data(WEB / "paytr.svg", "image/svg+xml"),
    "param": data(WEB / "param.svg", "image/svg+xml"),
    "akbank": data(WEB / "akbank.svg", "image/svg+xml"),
}
for _n in ("unified-api", "callback", "events", "plugin", "edge", "sandbox"):
    ASSETS["v_" + _n] = data(BK / f"visual/anim/web/icon-{_n}.mp4", "video/mp4")
    ASSETS["p_" + _n] = data(BK / f"visual/anim/web/icon-{_n}-poster.png", "image/png")
for n in ("unified-api", "callback", "refund", "installments", "sandbox", "docs", "events", "plugin", "edge"):
    ASSETS["i_" + n] = icon(n)

CHEV = '<svg class="ic chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m9 6 6 6-6 6"/></svg>'
GH = '<svg class="ic brand" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/></svg>'
COPY = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>'
DONE = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
MENU = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'
CLOSE = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
INFO = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/></svg>'
WARN = '<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4 2.8 19.5h18.4L12 4Z"/><path d="M12 10v4M12 17h.01"/></svg>'


def btn(kind, label, ic=CHEV, size="", lead=False):
    inner = (ic + f"<span>{label}</span>") if lead else (f"<span>{label}</span>" + ic)
    return f'<a class="btn {kind} {size}" href="#">{inner}</a>'


CSS = r"""
:root{--canvas:#F8F8FC;--surface:#FFFFFF;--ink:#13132B;--muted:#5A5A78;--line:#E4E3F0;--line-strong:#CFCDE6;
--indigo:#4338F2;--indigo-hover:#3A2FE0;--tint:#ECEAFF;--lilac:#A9A3FF;
--success:#087A55;--success-bg:#E6F5EF;--warning:#A86207;--warning-bg:#FDF3E3;--danger:#C8322B;--danger-bg:#FDECEB;
--display:"Manrope",sans-serif;--body:"Inter",sans-serif;--mono:"JetBrains Mono",monospace;
--r-sm:10px;--r-md:12px;--r-lg:16px;--r-xl:20px;
--spring:cubic-bezier(.34,1.56,.64,1);--ease:cubic-bezier(.2,.7,.2,1);
--shadow-sm:0 1px 2px rgba(19,19,43,.05);--shadow-md:0 10px 30px -14px rgba(19,19,43,.22)}
*{box-sizing:border-box}html,body{margin:0}
body{overflow-x:hidden;background:#EEEEF4;color:var(--ink);font-family:var(--body);-webkit-font-smoothing:antialiased}
.page{max-width:1200px;margin:0 auto;padding:28px 16px 64px}
.intro h1{font:800 30px/1.1 var(--display);letter-spacing:-.03em;margin:0 0 6px}
.intro p{color:var(--muted);margin:0 0 22px;max-width:780px;line-height:1.55}
.spec{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-xl);padding:26px;margin-bottom:16px}
.spec>h2{font:700 19px/1.2 var(--display);letter-spacing:-.015em;margin:0 0 4px}
.spec>p.d{color:var(--muted);font-size:14px;margin:0 0 18px;line-height:1.5}
.stage{background:var(--canvas);border:1px solid var(--line);border-radius:var(--r-lg);padding:24px}
.grid{display:grid;gap:14px}.grid>*,.docs>*{min-width:0}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}.g4{grid-template-columns:repeat(4,1fr)}
.ic{width:16px;height:16px;flex:none}
code,.mono{font-family:var(--mono)}

/* ---------- buttons (K7a, locked) ---------- */
.btn{position:relative;display:inline-flex;align-items:center;gap:8px;height:46px;padding:0 20px;border-radius:var(--r-md);font:500 15px/1 var(--body);text-decoration:none;white-space:nowrap;overflow:hidden;isolation:isolate;border:1px solid transparent;transition:background .2s,border-color .2s,box-shadow .25s,color .2s}
.btn.sm{height:36px;padding:0 14px;font-size:13.5px;border-radius:var(--r-sm)}.btn.lg{height:54px;padding:0 26px;font-size:16.5px;border-radius:14px}
.btn::after{content:"";position:absolute;inset:-1px;border-radius:inherit;pointer-events:none;background:linear-gradient(105deg,transparent 30%,var(--sheen) 47%,var(--sheen-soft) 53%,transparent 68%);transform:translateX(-130%)}
.btn .ic{transition:transform .35s var(--spring)}
.btn:is(:hover,:focus-visible)::after{transform:translateX(130%);transition:transform .75s var(--ease)}
.btn:is(:hover,:focus-visible) .chev{transform:translateX(4px)}
.btn:is(:hover,:focus-visible) .brand{transform:rotate(-8deg) scale(1.08)}
.btn:focus-visible{outline:2px solid var(--indigo);outline-offset:3px}
.btn:active{transform:translateY(1px)}
.btn.pri{background:var(--indigo);color:#fff;--sheen:rgba(255,255,255,.55);--sheen-soft:rgba(255,255,255,.18);box-shadow:0 1px 0 #ffffff33 inset,0 6px 16px -6px #4338F2aa}
.btn.pri:not(:hover):not(:focus-visible)::after{animation:idle-sheen 4.5s var(--ease) infinite 1s}
.btn.pri:hover{background:var(--indigo-hover);box-shadow:0 1px 0 #ffffff40 inset,0 10px 24px -8px #4338F2cc}
@keyframes idle-sheen{0%{transform:translateX(-130%)}22%,100%{transform:translateX(130%)}}
.btn.sec{background:var(--surface);color:var(--ink);border-color:var(--line);--sheen:rgba(67,56,242,.14);--sheen-soft:rgba(67,56,242,.05)}.btn.sec:hover{border-color:var(--line-strong)}
.btn.ghost{background:transparent;color:var(--ink);--sheen:rgba(67,56,242,.12);--sheen-soft:rgba(67,56,242,.04)}.btn.ghost:hover{background:var(--tint)}
.btn.inv{background:#fff;color:var(--indigo);--sheen:rgba(67,56,242,.16);--sheen-soft:rgba(67,56,242,.05)}
.btn.inv:not(:hover):not(:focus-visible)::after{animation:idle-sheen 4.5s var(--ease) infinite 1.6s}
.on-dark .btn.sec{background:transparent;color:#fff;border-color:#ffffff40;--sheen:rgba(255,255,255,.22);--sheen-soft:rgba(255,255,255,.06)}
.iconbtn{display:inline-grid;place-items:center;width:36px;height:36px;border-radius:var(--r-sm);border:1px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer;transition:background .2s,border-color .2s}
.iconbtn:hover{background:var(--tint);border-color:var(--line-strong)}.iconbtn:focus-visible{outline:2px solid var(--indigo);outline-offset:2px}

/* ---------- links ---------- */
.link{color:var(--indigo);text-decoration:none;background:linear-gradient(currentColor,currentColor) 0 100%/0 1.5px no-repeat;transition:background-size .3s var(--ease);padding-bottom:1px}
.link:hover,.link:focus-visible{background-size:100% 1.5px;outline:none}
.link.quiet{color:var(--ink)}
.link.more{display:inline-flex;align-items:center;gap:4px;font-weight:500;background:none}.link.more .ic{transition:transform .35s var(--spring)}.link.more:hover .ic{transform:translateX(3px)}

/* ---------- navbar ---------- */
.navstage{position:relative;border-radius:var(--r-lg);overflow:hidden;border:1px solid var(--line);background:var(--canvas) center bottom/cover no-repeat}
.nav{position:sticky;top:0;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:14px 22px;background:rgba(248,248,252,.72);backdrop-filter:blur(14px) saturate(1.4);border-bottom:1px solid rgba(228,227,240,.8)}
.nav .brandlink img{height:24px;display:block}
.nav ul{display:flex;gap:26px;list-style:none;margin:0;padding:0;font-size:14.5px}
.nav ul a{color:var(--muted);text-decoration:none;transition:color .2s}.nav ul a:hover,.nav ul a[aria-current]{color:var(--ink)}
.nav .act{display:flex;gap:8px;align-items:center}
.ver{font:500 12px/1 var(--mono);color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:6px 9px;background:var(--surface)}
.herobox{height:330px;padding:56px 32px 0}
.herobox h3{font:800 44px/1.04 var(--display);letter-spacing:-.035em;margin:0 0 12px;max-width:620px}.herobox h3 span{color:var(--muted)}
.phone{width:360px;border:1px solid var(--line);border-radius:28px;overflow:hidden;background:var(--canvas);position:relative;height:520px;box-shadow:var(--shadow-md)}
.phone .nav{padding:12px 16px}.phone .nav ul,.phone .nav .act .btn{display:none}
.sheet{position:absolute;inset:57px 0 0 0;background:var(--canvas);padding:18px 16px;display:grid;align-content:start;gap:4px;transform:translateY(-8px);opacity:0;pointer-events:none;transition:opacity .25s var(--ease),transform .3s var(--ease)}
.sheet.open{opacity:1;transform:none;pointer-events:auto}
.sheet a.item{display:flex;justify-content:space-between;align-items:center;padding:14px 12px;border-radius:12px;color:var(--ink);text-decoration:none;font:600 17px var(--display)}
.sheet a.item:hover{background:var(--tint)}.sheet .btns{display:grid;gap:10px;margin-top:14px}.sheet .btn{justify-content:center}

/* ---------- code ---------- */
.code{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-md);overflow:hidden}
.code .bar{display:flex;align-items:center;justify-content:space-between;padding:8px 8px 8px 14px;border-bottom:1px solid var(--line);background:var(--canvas)}
.code .file{font:500 12.5px var(--mono);color:var(--muted)}
.code pre{margin:0;padding:16px 18px;font:13.5px/1.7 var(--mono);overflow:auto;color:var(--ink)}
.k{color:var(--indigo)}.s{color:var(--success)}.c{color:var(--muted);font-style:italic}.f{color:#6A3FD8}.n{color:#A86207}
.copy{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 10px;border-radius:8px;border:1px solid transparent;background:none;color:var(--muted);font:500 12.5px var(--body);cursor:pointer;transition:background .2s,color .2s}
.copy:hover{background:var(--tint);color:var(--indigo)}.copy.done{color:var(--success)}
.copy .ok{display:none}.copy.done .ok{display:inline}.copy.done .cp{display:none}
.tabs{position:relative;display:inline-flex;gap:2px;padding:3px;border-radius:10px;background:var(--canvas);border:1px solid var(--line)}
.tabs button{position:relative;z-index:1;border:0;background:none;font:500 13px var(--mono);color:var(--muted);padding:6px 12px;border-radius:7px;cursor:pointer;transition:color .2s}
.tabs button[aria-selected=true]{color:var(--ink)}
.tabs .tabind{position:absolute;z-index:0;top:3px;bottom:3px;border-radius:7px;background:var(--surface);box-shadow:var(--shadow-sm);transition:left .35s var(--spring),width .35s var(--spring)}
.install{display:flex;align-items:center;justify-content:space-between;gap:12px;font:14px var(--mono);padding:12px 8px 12px 16px}
.install b{color:var(--muted);font-weight:400;margin-right:10px}

/* ---------- cards ---------- */
.feat{position:relative;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:22px;transition:transform .35s var(--spring),box-shadow .3s var(--ease),border-color .2s}
.feat:hover{transform:translateY(-3px);box-shadow:var(--shadow-md);border-color:var(--line-strong)}
.feat .tile{width:96px;height:96px;display:grid;place-items:center;margin:-6px 0 10px -8px}
.feat .tile>*{width:96px;height:96px;object-fit:contain;mix-blend-mode:multiply;transition:transform .45s var(--spring)}
.feat:hover .tile>*{transform:translateY(-4px) rotate(-5deg) scale(1.08)}
.feat h4{font:700 17px/1.25 var(--display);letter-spacing:-.01em;margin:0 0 6px}
.feat p{margin:0 0 14px;color:var(--muted);font-size:14.5px;line-height:1.55}
.status{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:18px}
.status .top{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}
.pill{display:inline-flex;align-items:center;gap:6px;font:600 12px/1 var(--body);padding:5px 9px;border-radius:999px}
.pill::before{content:"";width:6px;height:6px;border-radius:50%;background:currentColor}
.pill.pending{color:var(--warning);background:var(--warning-bg)}.pill.pending::before{animation:pulse 1.6s ease-in-out infinite}
.pill.success{color:var(--success);background:var(--success-bg)}.pill.failure{color:var(--danger);background:var(--danger-bg)}
.pill.cancelled{color:var(--muted);background:#EFEFF5}
@keyframes pulse{50%{opacity:.35}}
.status h5{font:700 15.5px var(--display);margin:0 0 4px}.status p{margin:0 0 12px;color:var(--muted);font-size:13.5px;line-height:1.5}
.status pre{margin:0;font:12.5px/1.6 var(--mono);background:var(--canvas);border:1px solid var(--line);border-radius:10px;padding:10px 12px;overflow:auto}
.prov{font:500 12px var(--mono);color:var(--muted)}
.badge{display:inline-flex;align-items:center;gap:6px;font:500 12px/1 var(--body);padding:6px 10px;border-radius:999px;border:1px solid var(--line);background:var(--surface);color:var(--ink)}
.badge.brand{background:var(--tint);border-color:transparent;color:var(--indigo)}.badge.mono{font-family:var(--mono)}
.badge .dot{width:6px;height:6px;border-radius:50%;background:var(--indigo)}

/* ---------- provider node ---------- */
.node{display:flex;align-items:center;gap:12px;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:10px 14px 10px 10px;cursor:pointer;transition:border-color .2s,box-shadow .3s var(--ease),transform .35s var(--spring);text-align:left;font:inherit;color:inherit}
.node .lg{width:44px;height:44px;border-radius:10px;background:var(--canvas);display:grid;place-items:center;border:1px solid var(--line)}
.node .lg img{width:38px;height:22px;object-fit:contain}
.node b{display:block;font:700 14.5px var(--display)}.node small{color:var(--muted);font-size:12px}
.node:hover{transform:translateY(-2px);border-color:var(--line-strong)}
.node[aria-pressed=true]{border-color:var(--indigo);box-shadow:0 0 0 4px var(--tint)}
.hub{display:inline-flex;align-items:center;gap:10px;background:var(--indigo);color:#fff;border-radius:14px;padding:12px 16px;font:600 14px var(--mono);box-shadow:0 10px 24px -10px #4338F2}
.hub img{width:22px;height:22px;filter:brightness(0) invert(1)}
.caps{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}

/* ---------- callout ---------- */
.callout{display:flex;gap:12px;border-radius:12px;padding:14px 16px;font-size:14.5px;line-height:1.55;border:1px solid}
.callout .ic{width:18px;height:18px;margin-top:2px}
.callout.info{background:var(--tint);border-color:#DCD8FF;color:#2B2496}.callout.warn{background:var(--warning-bg);border-color:#F4DFB8;color:#7A4605}
.callout.danger{background:var(--danger-bg);border-color:#F6CFCC;color:#8F211C}.callout.ok{background:var(--success-bg);border-color:#C4E7D8;color:#065C40}
.callout code{font-size:.9em;background:rgba(255,255,255,.6);padding:1px 5px;border-radius:5px}

/* ---------- docs ---------- */
.docs{display:grid;grid-template-columns:230px 1fr;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);overflow:hidden}
.side{border-right:1px solid var(--line);padding:18px 12px;background:var(--canvas)}
.side .grp{font:600 12px var(--body);color:var(--muted);margin:14px 10px 6px}
.side a{display:flex;align-items:center;gap:10px;padding:7px 10px;border-radius:8px;color:var(--ink);text-decoration:none;font-size:14px;transition:background .2s,color .2s}
.side a img{width:20px;height:20px}
.side a:hover{background:#F0EFFA}.side a[aria-current]{background:var(--tint);color:var(--indigo);font-weight:600}
.art{padding:28px 32px}.art h3{font:800 28px/1.15 var(--display);letter-spacing:-.025em;margin:0 0 10px}
.art h4{font:700 19px var(--display);margin:26px 0 8px}.art p{line-height:1.7;margin:0 0 14px;font-size:15.5px}
.art :not(pre)>code{font-size:.88em;background:var(--tint);color:var(--indigo);padding:2px 6px;border-radius:6px}
.added{display:inline-flex;margin-left:8px;vertical-align:middle}
table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;font:600 12.5px var(--body);color:var(--muted);padding:10px 12px;border-bottom:1px solid var(--line);background:var(--canvas)}
td{padding:11px 12px;border-bottom:1px solid var(--line)}tr:last-child td{border-bottom:0}
td.y{color:var(--success);font-weight:600}td.n{color:var(--muted)}
.tablewrap{border:1px solid var(--line);border-radius:12px;overflow:hidden}

/* ---------- CTA + footer ---------- */
.cta{position:relative;overflow:hidden;border-radius:var(--r-xl);background:var(--indigo);color:#fff;padding:44px 40px;display:grid;gap:24px;justify-items:start}
.cta h3{font:800 32px/1.1 var(--display);letter-spacing:-.03em;margin:0 0 8px}.cta p{margin:0;color:#DCD9FF;max-width:460px;line-height:1.55}
.cta .deco{position:absolute;right:4%;top:50%;width:230px;transform:translateY(-50%) rotate(-12deg);pointer-events:none}
.cta .btns{position:relative;z-index:1;display:flex;gap:10px;flex-wrap:wrap}
.foot{display:grid;grid-template-columns:1.4fr repeat(3,1fr);gap:24px;padding:30px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg)}
.foot img{height:24px}.foot p{color:var(--muted);font-size:13.5px;line-height:1.55;margin:12px 0 0;max-width:280px}
.foot h6{font:600 13px var(--body);margin:0 0 10px}.foot a{display:block;color:var(--muted);text-decoration:none;font-size:14px;padding:4px 0}.foot a:hover{color:var(--ink)}
.legal{grid-column:1/-1;display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:16px;color:var(--muted);font-size:12.5px}

.sectionhead h3{font:800 34px/1.08 var(--display);letter-spacing:-.03em;margin:0 0 10px;max-width:620px}
.sectionhead p{color:var(--muted);margin:0;max-width:560px;line-height:1.6}
.note{font-size:13px;color:var(--muted);margin-top:12px;line-height:1.5}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}.btn::after{display:none}}
@media(max-width:900px){.cta{padding:32px 22px}.cta .deco{opacity:.18;width:160px;right:-40px;top:auto;bottom:-36px;transform:rotate(-12deg)}.spec{padding:18px}.stage{padding:16px}.phone{width:100%;max-width:360px}.art{padding:20px}.tablewrap{overflow-x:auto}.tablewrap table{min-width:520px}.g2,.g3,.g4,.docs,.foot{grid-template-columns:1fr}.navstage .nav .act .ver,.navstage .nav .act .btn.sec{display:none}.navstage .nav{padding:12px 14px}.navstage .nav .brandlink img{height:20px}.navstage .herobox{padding:36px 18px 0;height:260px}.sectionhead h3{font-size:28px}.nav ul{display:none}.side{border-right:0;border-bottom:1px solid var(--line)}.cta{flex-direction:column;align-items:flex-start}.herobox h3{font-size:32px}}
"""

A = ASSETS
BODY = f"""
<div class="page">
<header class="intro"><h1>Better Payment · Bileşen Seti</h1>
<p>Faz 4.5 · K7b. Onaylı palet, tipografi, logo, ikon seti ve buton hareketleriyle kurulmuş bileşenler. Her şey etkileşimli: üzerine gel, tıkla, Tab ile gez. Hero zemini A3 · Alt bant.</p></header>

<section class="spec"><h2>1 · Navbar</h2><p class="d">Yarı saydam, bulanık zemin; kaydırınca içerik altından geçer. Sağda sürüm rozeti, GitHub ve primary "Başla". Mobilde menü tam ekran açılır.</p>
<div class="grid" style="gap:18px">
<div class="navstage" style="background-image:url({A['hero']})">
<nav class="nav"><a class="brandlink" href="#"><img src="{A['logo']}" alt="Better Payment"></a>
<ul><li><a href="#" aria-current="page">Dokümantasyon</a></li><li><a href="#">Sağlayıcılar</a></li><li><a href="#">Örnekler</a></li><li><a href="#">Blog</a></li></ul>
<div class="act"><span class="ver">v0.5.2</span>{btn('sec','GitHub',GH,'sm',True)}{btn('pri','Başla',CHEV,'sm')}</div></nav>
<div class="herobox"><h3>Türkiye'nin ödeme sağlayıcıları. <span>Tek TypeScript API'si.</span></h3></div></div>
<div style="display:flex;gap:24px;align-items:flex-start;flex-wrap:wrap"><div class="phone"><nav class="nav"><a class="brandlink" href="#"><img src="{A['logo']}" alt="Better Payment" style="height:20px"></a><div class="act"><button class="iconbtn" id="menuBtn" aria-expanded="false" aria-label="Menüyü aç">{MENU}</button></div></nav>
<div class="sheet" id="sheet"><a class="item" href="#">Dokümantasyon {CHEV}</a><a class="item" href="#">Sağlayıcılar {CHEV}</a><a class="item" href="#">Örnekler {CHEV}</a><a class="item" href="#">Blog {CHEV}</a>
<div class="btns">{btn('pri','Dokümantasyonu aç',CHEV)}{btn('sec',"GitHub'da incele",GH,'',True)}</div></div>
<div style="padding:28px 18px"><div class="sectionhead"><h3 style="font-size:28px">Türkiye'nin ödeme sağlayıcıları.</h3><p>Menü ikonuna dokun.</p></div></div></div><p class="note" style="max-width:420px">Mobil: menü ikonu sağ üstte; açılan sayfa büyük dokunma alanlı bağlantılar ve iki ana aksiyon içerir. Masaüstünde navbar yapışkan kalır ve arka planı bulanıklaştırır.</p></div>
</div></section>

<section class="spec"><h2>2 · Butonlar ve linkler</h2><p class="d">K7a kilitli: primary sürekli ışıltı; diğerleri hover'da parıltı + ikon hareketi. Linklerde alt çizgi soldan çizilir.</p>
<div class="grid g3">
<div class="stage" style="display:grid;gap:12px;justify-items:start">{btn('pri','Başla',CHEV,'sm')}{btn('pri','Dokümantasyonu aç')}{btn('pri','Dokümantasyonu aç',CHEV,'lg')}</div>
<div class="stage" style="display:grid;gap:12px;justify-items:start">{btn('sec',"GitHub'da incele",GH,'',True)}{btn('sec',"npm'de gör")}{btn('ghost','Tüm sağlayıcılar')}<div style="display:flex;gap:8px"><button class="iconbtn" aria-label="Kopyala">{COPY}</button><button class="iconbtn" aria-label="Menü">{MENU}</button></div></div>
<div class="stage" style="display:grid;gap:14px;align-content:start;font-size:15.5px;line-height:1.7"><p style="margin:0">Satır içi link: ayrıntılar için <a class="link" href="#">hata kodları</a> sayfasına bak.</p><p style="margin:0">Sessiz link: <a class="link quiet" href="#">Değişiklik günlüğü</a></p><a class="link more" href="#">Daha fazla bilgi {CHEV}</a></div>
</div></section>

<section class="spec"><h2>3 · Kod ve kurulum</h2><p class="d">Dosya adı başlıklı kod bloğu, kopyala butonu (tıklayınca onay), paket yöneticisi sekmeleri yaylı kayan seçim göstergesiyle.</p>
<div class="grid g2">
<div class="code"><div class="bar"><span class="file">lib/payment.ts</span><button class="copy" data-copy>{f'<span class="cp" style="display:inline-flex;gap:6px;align-items:center">{COPY}Kopyala</span><span class="ok" style="gap:6px;align-items:center">{DONE}Kopyalandı</span>'}</button></div>
<pre><span class="k">import</span> {{ betterPayment, iyzico, paytr }} <span class="k">from</span> <span class="s">"better-payment"</span>;

<span class="k">const</span> payment = <span class="f">betterPayment</span>({{
  providers: {{ iyzico: <span class="f">iyzico</span>({{ ... }}), paytr: <span class="f">paytr</span>({{ ... }}) }},
}});

<span class="c">// her sağlayıcıda aynı istek ve sonuç tipleri</span>
<span class="k">const</span> result = <span class="k">await</span> payment.iyzico.<span class="f">initThreeDSPayment</span>(order);</pre></div>
<div style="display:grid;gap:14px;align-content:start">
<div class="code"><div class="bar"><div class="tabs" role="tablist" id="pm"><span class="tabind"></span><button role="tab" aria-selected="true" data-cmd="npm install better-payment">npm</button><button role="tab" aria-selected="false" data-cmd="pnpm add better-payment">pnpm</button><button role="tab" aria-selected="false" data-cmd="yarn add better-payment">yarn</button><button role="tab" aria-selected="false" data-cmd="bun add better-payment">bun</button></div><button class="copy" data-copy>{f'<span class="cp" style="display:inline-flex;gap:6px;align-items:center">{COPY}Kopyala</span><span class="ok" style="gap:6px;align-items:center">{DONE}Kopyalandı</span>'}</button></div>
<div class="install"><span><b>$</b><span id="cmd">npm install better-payment</span></span></div></div>
<div class="callout info">{INFO}<div>Sıfır runtime bağımlılığı. Node.js 20+ ve edge runtime'larda çalışır.</div></div>
</div></div></section>

<section class="spec"><h2>4 · Özellik kartları</h2><p class="d">Zeminsiz, animasyonlu cam ikonlar (Higgsfield Kling 3.0, 5 sn dikişsiz döngü, 35–100 KB). Video beyaz zeminli kodlanır ve <code>mix-blend-mode: multiply</code> ile kartla kaynaşır. Hover&#39;da kart yükselir, ikon döner. Hareketi azalt açıkken poster karesi görünür.</p>
<div class="grid g3">
<article class="feat"><div class="tile"><video src="{A['v_unified-api']}" poster="{A['p_unified-api']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Tek API, dört sağlayıcı</h4><p>iyzico, PayTR, Parampos ve Akbank için aynı istek ve sonuç tipleri.</p><a class="link more" href="#">Sağlayıcılar {CHEV}</a></article>
<article class="feat"><div class="tile"><video src="{A['v_callback']}" poster="{A['p_callback']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Callback'ler doğrulanır</h4><p>Her 3D Secure callback'i senin anahtarlarınla kontrol edilir, sonra güvenilir.</p><a class="link more" href="#">Güvenlik modeli {CHEV}</a></article>
<article class="feat"><div class="tile"><video src="{A['v_events']}" poster="{A['p_events']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Tek event akışı</h4><p>Bütün sağlayıcılar için doğrulanmış sonuçlar tek listener'a düşer.</p><a class="link more" href="#">Events {CHEV}</a></article>
<article class="feat"><div class="tile"><video src="{A['v_plugin']}" poster="{A['p_plugin']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Plugin sistemi</h4><p>İşlem öncesi ve sonrası hook'lar, kendi endpoint'lerin.</p><a class="link more" href="#">Plugin yaz {CHEV}</a></article>
<article class="feat"><div class="tile"><video src="{A['v_edge']}" poster="{A['p_edge']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Edge'de çalışır</h4><p>Yalnız fetch ve WebCrypto. Vercel Edge, Workers, Deno, Bun.</p><a class="link more" href="#">Edge rehberi {CHEV}</a></article>
<article class="feat"><div class="tile"><video src="{A['v_sandbox']}" poster="{A['p_sandbox']}" autoplay muted loop playsinline aria-hidden="true"></video></div><h4>Test araçları</h4><p>MockProvider ile gerçek kart girmeden uçtan uca test.</p><a class="link more" href="#">Testing {CHEV}</a></article>
</div></section>

<section class="spec"><h2>5 · Durum kartları ve rozetler</h2><p class="d">SDK'nın gerçek dört durumu. <code>pending</code> noktası yavaşça nabız atar; diğerleri sabit.</p>
<div class="grid g4">
<article class="status"><div class="top"><span class="pill pending">pending</span><span class="prov">iyzico</span></div><h5>3D Secure bekleniyor</h5><p>Müşteri bankanın doğrulama sayfasında.</p><pre>{{ status: "pending" }}</pre></article>
<article class="status"><div class="top"><span class="pill success">success</span><span class="prov">parampos</span></div><h5>Callback doğrulandı</h5><p>İmza kontrol edildi, ödeme tamamlandı.</p><pre>{{ status: "success" }}</pre></article>
<article class="status"><div class="top"><span class="pill failure">failure</span><span class="prov">paytr</span></div><h5>Sahte callback reddedildi</h5><p>Hash eşleşmedi, hiçbir şey başarılı sayılmadı.</p><pre>{{ code: "INVALID_HASH" }}</pre></article>
<article class="status"><div class="top"><span class="pill cancelled">cancelled</span><span class="prov">akbank</span></div><h5>Ödeme iptal edildi</h5><p>Tam iade veya void sonrası durum sorgusu.</p><pre>{{ status: "cancelled" }}</pre></article>
</div>
<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:16px"><span class="badge brand"><span class="dot"></span>Yeni</span><span class="badge mono">v0.5.2</span><span class="badge">Added in 0.4</span><span class="badge">Edge uyumlu</span><span class="badge">Deneysel</span></div>
</section>

<section class="spec"><h2>6 · Sağlayıcı düğümü</h2><p class="d">Hero ağındaki ve sağlayıcı sayfasındaki kart. Tıklayınca seçili hale gelir; yetenekler rozetlerle gösterilir. Logolar repo'daki mevcut SVG'ler.</p>
<div class="stage"><div style="display:flex;justify-content:center;margin-bottom:22px"><span class="hub"><img src="{A['symbol']}" alt="">betterPayment()</span></div>
<div class="grid g4" id="nodes">
<button class="node" aria-pressed="true" data-caps="3DS,Non-3D,İade,İptal,BIN,Taksit"><span class="lg"><img src="{A['iyzico']}" alt=""></span><span><b>iyzico</b><small>Sandbox doğrulandı</small></span></button>
<button class="node" aria-pressed="false" data-caps="3DS iFrame,Non-3D,İade,BIN,Taksit"><span class="lg"><img src="{A['paytr']}" alt=""></span><span><b>PayTR</b><small>Doğrulama bekliyor</small></span></button>
<button class="node" aria-pressed="false" data-caps="TP_WMD_UCD,Non-3D (TRY),İade,İptal,BIN"><span class="lg"><img src="{A['param']}" alt=""></span><span><b>Parampos</b><small>Doğrulama bekliyor</small></span></button>
<button class="node" aria-pressed="false" data-caps="3D_PAY,Non-3D,İade,İptal"><span class="lg"><img src="{A['akbank']}" alt=""></span><span><b>Akbank</b><small>Doğrulama bekliyor</small></span></button>
</div><div class="caps" id="caps"></div></div></section>

<section class="spec"><h2>7 · Callout</h2><p class="d">Docs içi uyarılar. Renk anlamla sınırlı: bilgi indigo, uyarı amber, tehlike kırmızı, başarı yeşil.</p>
<div class="grid g2">
<div class="callout info">{INFO}<div>Bağlantı koparsa sonuç <code>pending</code> ve <code>NETWORK_ERROR</code> olur.</div></div>
<div class="callout warn">{WARN}<div>Ödeme, iade ve iptal istekleri otomatik olarak tekrar denenmez.</div></div>
<div class="callout danger">{WARN}<div>Callback gövdesine doğrulamadan güvenme.</div></div>
<div class="callout ok">{INFO}<div>Sandbox'ta tüm testler geçti.</div></div>
</div></section>

<section class="spec"><h2>8 · Dokümantasyon sayfası</h2><p class="d">Kenar menüde kategori ikonları (küçük cam ikonlar), aktif sayfa lila. Başlık, gövde, satır içi kod, tablo ve "Added in" rozeti.</p>
<div class="docs"><nav class="side" aria-label="Docs"><div class="grp">Başlangıç</div><a href="#"><img src="{A['i_docs']}" alt="">Kurulum</a><a href="#"><img src="{A['i_unified-api']}" alt="">Hızlı başlangıç</a>
<div class="grp">Ödemeler</div><a href="#" aria-current="page"><img src="{A['i_callback']}" alt="">Sonuçlar ve durumlar</a><a href="#"><img src="{A['i_refund']}" alt="">İade ve iptal</a><a href="#"><img src="{A['i_installments']}" alt="">Taksit</a>
<div class="grp">Geliştirme</div><a href="#"><img src="{A['i_events']}" alt="">Events</a><a href="#"><img src="{A['i_plugin']}" alt="">Plugin'ler</a><a href="#"><img src="{A['i_sandbox']}" alt="">Testing</a></nav>
<article class="art"><h3>Sonuçlar ve durumlar</h3><p>Her işlem <code>status</code> taşıyan bir sonuçla döner. Sağlayıcının ham kodu <code>errorCode</code> alanında kalır; sağlayıcıdan bağımsız kod <code>code</code> alanındadır. Ayrıntılar için <a class="link" href="#">hata kodları</a>.</p>
<h4>Durumlar <span class="badge added">Added in 0.1</span></h4>
<div class="tablewrap"><table><thead><tr><th>status</th><th>anlamı</th><th>sonraki adım</th></tr></thead><tbody>
<tr><td><span class="pill success">success</span></td><td>Sağlayıcı onayladı</td><td>Siparişi tamamla</td></tr>
<tr><td><span class="pill failure">failure</span></td><td>Sağlayıcı reddetti</td><td><code>code</code> alanına göre mesaj göster</td></tr>
<tr><td><span class="pill pending">pending</span></td><td>3DS bekleniyor veya sonuç bilinmiyor</td><td><code>getPayment()</code> ile kontrol et</td></tr>
<tr><td><span class="pill cancelled">cancelled</span></td><td>İptal veya tam iade</td><td>—</td></tr></tbody></table></div></article></div></section>

<section class="spec"><h2>9 · Bölüm başlığı, CTA bandı ve footer</h2><p class="d">Bölüm başlıklarında eyebrow yok; başlık doğrudan mesajı taşır. CTA bandında ters (beyaz) primary buton da sürekli ışıltılı.</p>
<div class="sectionhead" style="margin-bottom:22px"><h3>Callback'e güvenme, doğrula.</h3><p>Better Payment her bildirimi senin anahtarlarınla kontrol eder; eşleşmeyen hiçbir şey başarılı sayılmaz.</p></div>
<div class="cta"><img class="deco" src="{A['i_unified-api']}" alt=""><div style="position:relative"><h3>Beş dakikada ilk ödemeni al.</h3><p>Sandbox modunda kart girmeden dene, sonra tek satırla canlıya geç.</p></div><div class="btns on-dark">{btn('inv','Dokümantasyonu aç')}{btn('sec',"GitHub'da incele",GH,'',True)}</div></div>
<div style="height:16px"></div>
<footer class="foot"><div><img src="{A['logo']}" alt="Better Payment"><p>Türkiye'nin ödeme sağlayıcıları için açık kaynak, tip güvenli TypeScript SDK'sı.</p></div>
<div><h6>Ürün</h6><a href="#">Dokümantasyon</a><a href="#">Sağlayıcılar</a><a href="#">Değişiklikler</a></div>
<div><h6>Topluluk</h6><a href="#">GitHub</a><a href="#">Katkı rehberi</a><a href="#">Issue'lar</a></div>
<div><h6>Kaynaklar</h6><a href="#">npm</a><a href="#">Güvenlik</a><a href="#">Lisans (MIT)</a></div>
<div class="legal"><span>© 2026 Better Payment</span><span>TR · EN</span></div></footer>
</section>
</div>
"""

JS = r"""
document.querySelectorAll('a[href="#"]').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));
const mb=document.getElementById('menuBtn'),sh=document.getElementById('sheet');
const MENU=mb.innerHTML,CLOSE=%s;
mb.addEventListener('click',()=>{const o=sh.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.innerHTML=o?CLOSE:MENU;});
document.querySelectorAll('[data-copy]').forEach(b=>b.addEventListener('click',()=>{b.classList.add('done');setTimeout(()=>b.classList.remove('done'),1600)}));
const pm=document.getElementById('pm'),pill=pm.querySelector('.tabind'),cmd=document.getElementById('cmd');
function place(b){pill.style.left=b.offsetLeft+'px';pill.style.width=b.offsetWidth+'px'}
pm.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{pm.querySelectorAll('button').forEach(x=>x.setAttribute('aria-selected',x===b));place(b);cmd.textContent=b.dataset.cmd}));
requestAnimationFrame(()=>place(pm.querySelector('[aria-selected=true]')));
const caps=document.getElementById('caps');
function showCaps(n){caps.innerHTML=n.dataset.caps.split(',').map(c=>'<span class="badge">'+c+'</span>').join('')}
document.querySelectorAll('#nodes .node').forEach(n=>n.addEventListener('click',()=>{document.querySelectorAll('#nodes .node').forEach(x=>x.setAttribute('aria-pressed',x===n));showCaps(n)}));
showCaps(document.querySelector('#nodes [aria-pressed=true]'));
""" % json.dumps(CLOSE)

html = (
    '<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
    "<title>Better Payment · Bileşen Seti</title>"
    '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&family=JetBrains+Mono:wght@400;500&display=swap">'
    f"<style>{CSS}</style></head><body>{BODY}<script>{JS}</script></body></html>"
)
out = HERE / "bilesen-seti-v1.html"
out.write_text(html, encoding="utf-8")
print(out.name, len(html) // 1024, "KB")
