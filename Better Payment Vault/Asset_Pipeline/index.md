---
tur: uretim
alan: asset
guncelleme: 2026-10-01
ozet: "Better Payment branding varlıkları için üretim hattının giriş noktası."
durum: aktif
---
# Asset Pipeline — Giriş

Bu klasör Better Payment logo sistemi, favicon, web görselleri, motion kaynakları ve lansman kreatifleri için kanonik üretim kaynağıdır.

## Hatlar

| Hat | Kapsam | Vault kökü | Ürün hedefi |
|---|---|---|---|
| Logo | sembol, wordmark, lockup, monochrome | `Asset_Pipeline/Logo/` | `apps/web/public/brand/` |
| Sistem | favicon, PWA ve sosyal preview | `Asset_Pipeline/Sistem/` | `apps/web/public/` |
| Web | hero ve section grafikleri | `Asset_Pipeline/Web/` | `apps/web/public/brand/` |
| Motion | logo/route animasyon tarifleri | `Asset_Pipeline/Motion/` | code-native component veya optimize export |
| Sosyal | lansman avatar, cover ve duyuru görselleri | `Asset_Pipeline/Sosyal/` | platform exportu |

## Kaynak sınırı

- Higgsfield job çıktısı veya editable source önce pipeline'a girer.
- Seçilmemiş taslak ürün koduna kopyalanmaz.
- Onaylı master yeniden çizilmez; varyantlar aynı geometriden deterministik üretilir.
- Kullanıcı referansları taste signal'dır; başka markanın geometrisi, wordmark'ı veya trade dress'i kopyalanmaz.
- Vault ve yerel üretim durumu upstream PR'a girmez.

## Aktif kuyruk

| Öncelik | Set | Durum | Sonraki kapı |
|---:|---|---|---|
| P0 | Better Payment sembol v1 | `1 · Brief kilitli` | palet seçimi ve üç SVG aday |
| P0 | Favicon/small mark ailesi | `0 · Envanterde` | sembol seçimi |
| P0 | Wordmark ve yatay lockup | `0 · Envanterde` | sembol + tipografi seçimi |
| P1 | Siyah, beyaz ve renkli exportlar | `0 · Envanterde` | master geometrisi onayı |
| P1 | Hero payment-provider network grafiği | `0 · Envanterde` | logo ve web token kilidi |
| P1 | Hero artwork (Higgsfield) | `0 · Envanterde` | ADR-005 kabulü ve Brand Lock |
| P1 | İkon/obje seti (12–16 parça, web + docs) | `0 · Envanterde` | ADR-005 kabulü ve Brand Lock |

## Referanslar

- [[Asset_Pipeline/Logo/Referans/README]]: yedi logo referansı
- [[Asset_Pipeline/Web/Referans/README]]: beş landing page referansı

## İlgili

[[Asset_Pipeline/Rehber - Asset Üretimi]] · [[Asset_Pipeline/roadmap]] · [[Asset_Pipeline/Logo/index]] · [[Branding/04 - Logo Sistemi Taslağı]] · [[Kararlar/ADR-004 - Vault Tabanlı Asset Pipeline]]
