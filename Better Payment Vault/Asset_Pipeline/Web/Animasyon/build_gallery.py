import base64, json, pathlib
W = pathlib.Path("web")
items = [("unified-api","Tek API"),("callback","Callback doğrulama"),("threeds","3D Secure"),("refund","İade"),("cancel","İptal"),("installments","Taksit"),("status","Durum sorgu"),("events","Event / listener"),("plugin","Plugin"),("edge","Edge runtime"),("sandbox","Sandbox / test"),("languages","Çok dil"),("handler","Güvenli handler"),("idempotency","Idempotency"),("docs","Dokümantasyon")]
rep = json.loads((W / "report.json").read_text())
V = {k: "data:video/mp4;base64," + base64.b64encode((W / f"icon-{k}.mp4").read_bytes()).decode() for k, _ in items}
cells = "".join(f'<figure><video data-k="{k}" autoplay muted loop playsinline></video><figcaption><b>{t}</b><span>{rep[k]["kb"]} KB · dikiş {rep[k]["seam_rmse"]*100:.1f}%</span></figcaption></figure>' for k, t in items)
html = f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Better Payment · Animasyonlu İkonlar</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@700;800&display=swap">
<style>body{{margin:0;background:#EEEEF4;color:#13132B;font-family:Inter,system-ui,sans-serif}}.page{{max-width:1180px;margin:0 auto;padding:28px 16px 48px}}
h1{{font:800 30px Manrope;letter-spacing:-.03em;margin:0 0 6px}}p.l{{color:#5A5A78;margin:0 0 20px;line-height:1.5;max-width:780px}}
.bar{{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap}}.bar button{{font:500 13px Inter;border:1px solid #E4E3F0;background:#fff;border-radius:9px;padding:7px 12px;cursor:pointer}}.bar button[aria-pressed=true]{{background:#13132B;color:#fff;border-color:#13132B}}
.grid{{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;padding:18px;border-radius:18px;background:var(--bg,#fff);border:1px solid #E4E3F0;transition:background .3s}}
figure{{margin:0;text-align:center}}video{{width:100%;aspect-ratio:1;mix-blend-mode:multiply;display:block}}figcaption{{display:grid;gap:2px;font-size:13px;margin-top:4px}}figcaption span{{color:#5A5A78;font-size:11.5px}}
@media(max-width:860px){{.grid{{grid-template-columns:repeat(3,1fr)}}}}@media(prefers-reduced-motion:reduce){{video{{animation:none}}}}</style></head><body><div class="page">
<h1>Animasyonlu ikon seti</h1><p class="l">15 ikon, Higgsfield Kling 3.0 ile 5 saniyelik dikişsiz döngü. Videolar beyaz zeminli kodlanır, sayfada <code>mix-blend-mode: multiply</code> ile zeminle kaynaşır. Zemin düğmeleriyle açık yüzeylerde dene.</p>
<div class="bar" id="bg"><button aria-pressed="true" data-v="#FFFFFF">Beyaz</button><button aria-pressed="false" data-v="#F8F8FC">Canvas</button><button aria-pressed="false" data-v="#ECEAFF">Lilac Tint</button></div>
<div class="grid" id="g">{cells}</div></div>
<script>const V={json.dumps(V)};document.querySelectorAll("video[data-k]").forEach(v=>v.src=V[v.dataset.k]);
const bs=document.querySelectorAll('#bg button');bs.forEach(b=>b.onclick=()=>{{bs.forEach(x=>x.setAttribute('aria-pressed',x===b));document.getElementById('g').style.setProperty('--bg',b.dataset.v)}});
if(matchMedia('(prefers-reduced-motion: reduce)').matches)document.querySelectorAll('video').forEach(v=>{{v.removeAttribute('autoplay');v.pause()}});</script></body></html>'''
pathlib.Path("animasyonlu-ikonlar.html").write_text(html, encoding="utf-8")
print(len(html)//1024, "KB")
