---
tur: uretim
alan: web-branding
guncelleme: 2026-10-01
ozet: "15 ikonluk animasyonlu set: Higgsfield video döngüleri, web kodlaması ve şeffaflık yöntemi."
durum: aktif
---
# Animasyonlu ikonlar

Kullanıcı kararı (2026-10-01): tüm ikonlar animasyonlu olacak; özellikle homepage'deki altı özellik kartı.

## Üretim

- Model: Kling 3.0, 1:1, 5 sn, ses kapalı. Başlangıç ve bitiş karesi aynı statik ikon → dikişsiz döngü.
- Her ikon için konuya özel tek hareket: `prompt/icon-*.txt`.
- İlk turda tek API, callback, 3D Secure ve taksit bozuldu (şerit sayısı değişti, döngü ezildi, kemer kopyalandı, çekirdek kapsülden taştı). Bu dördü "obje katı, şekil değişmez, yalnız X hareket eder" talimatıyla **pro** modda yeniden üretildi. Diğer on bir ikon std mod.
- Bilinen küçük kusur: taksitte bir iki karede hafif turkuaz parıltı.

## Web kodlaması (`process_anim.py`)

1. Zemin rengi ilk karenin köşesinden ölçülür.
2. Yedi örnek karede nesnenin sınırları bulunur; birleşik alan %22 payla kare kırpılır.
3. `colorlevels` ile zemin tam beyaza çekilir (ölçülen değer × 0.985).
4. 480 × 480 H.264 (`.mp4`) ve VP9 (`.webm`), poster karesi.

Sayfada `<video autoplay muted loop playsinline poster>` + `mix-blend-mode: multiply`. Yalnız açık yüzeylerde (beyaz, Canvas, Lilac Tint); koyu zeminde statik şeffaf PNG. `prefers-reduced-motion` altında poster.

`video_background_remover` alfa kanalı vermediği (nesneyi siyah zemine koydu) için kullanılmaz.

## Kayıt

| İkon | Job | Döngü dikişi (RMSE) | MP4 |
|---|---|---|---|
| unified-api | `1302b1a1-0b83-4f53-8317-a2c7d0cfef24` | 0.4% | 55 KB |
| callback | `9a003a4a-5303-4131-8ab0-1dd698f28931` | 0.5% | 69 KB |
| threeds | `3fda8039-db0f-49f1-a8a4-d48a80f859e2` | 0.4% | 38 KB |
| refund | `139efa84-4330-4407-a2a5-9544ded1446d` | 1.1% | 58 KB |
| cancel | `39406b32-125e-453b-81ba-125e4dde4ba9` | 0.8% | 40 KB |
| installments | `7d4a4464-2f20-4ecc-8160-b9bb31d729c0` | 0.4% | 50 KB |
| status | `9fd0aaaf-21c9-4556-b5c3-00cb9f07acdd` | 0.9% | 31 KB |
| events | `f690cdc6-5a25-48b7-84ba-ced4dc1f78b5` | 0.9% | 93 KB |
| plugin | `2b947d8a-3255-45b7-8ca9-6b2abb6ff50b` | 1.0% | 49 KB |
| edge | `842cae18-212b-4896-bad7-0c66905ad7e5` | 0.9% | 66 KB |
| sandbox | `787dceb0-4bb6-4ee5-bfa4-206aebdee3ec` | 0.8% | 68 KB |
| languages | `3decdd54-7aaa-4202-9b4f-640d435b0d9a` | 0.9% | 40 KB |
| handler | `26cba4d3-a6a8-44cd-bd84-3eff4b2a6eaf` | 0.8% | 48 KB |
| idempotency | `f9c1bcf0-1afc-4512-ab26-ac0c329e2e94` | 0.8% | 35 KB |
| docs | `34fdd0d8-e7f7-46af-8422-ce5daa7baa70` | 0.9% | 92 KB |

İnceleme: `animasyonlu-ikonlar.html` (zemin değiştirilebilir galeri).
