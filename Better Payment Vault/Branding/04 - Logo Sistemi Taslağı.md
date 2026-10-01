---
tur: marka-sistemi
alan: branding
guncelleme: 2026-10-01
ozet: "Better Payment logo ailesi: sembol, uygulama ikonu, favicon, wordmark ve lockup'ların dosyaları ve kullanım kuralları."
durum: aktif
---
# Logo Sistemi

Seçilen sembol: **Birleşen yollar** · kayıt [[Branding/05 - Brand Lock]].

## Aile

| Kod | Dosya kökü (`Asset_Pipeline/Logo/Varyantlar/`) | Kullanım |
|---|---|---|
| symbol | `symbol/better-payment-symbol-{color,ink,black,white}.svg` + 16–1024 px PNG | avatar, provider-network merkezi, ikon |
| app icon | `app-icon/better-payment-app-icon.svg` (indigo yuvarlak kare, beyaz sembol) + 16–1024 px | uygulama ikonu, PWA, sosyal avatar |
| avatar | `app-icon/better-payment-avatar-square.svg` + 400/1024 px | GitHub, npm, X; platform daire kırpar |
| favicon | `favicon/favicon.svg`, `favicon.ico` (16/32/48), `apple-touch-icon.png`, `icon-192/512.png` | `apps/web/app/` |
| wordmark | `wordmark/better-payment-wordmark-{color,black,white}.svg` | yalnız metin imzası |
| horizontal | `lockup/better-payment-horizontal-{color,black,white,on-indigo}.svg` | navbar, docs, README, sosyal kapak |
| stacked | `lockup/better-payment-stacked-{color,black,white}.svg` | kare alanlar, sunum kapağı |

Üretim: `Varyantlar/build_family.py` onaylı Brandkit exportundaki path'leri değiştirmeden yerleştirir; wordmark Manrope 800 (OFL) HarfBuzz ile dizilip outline'a çevrilir.

## Renk modları

- color: sembol `#4338F2`, yazı Ink `#13132B` — açık zeminlerin varsayılanı
- white: koyu ve indigo zemin
- black: tek renk baskı
- ink: sembol tek başına koyu tonda gerektiğinde

## Clear space ve minimum boyut

- `x` = sembol yüksekliğinin %25'i. Lockup'ın her yanında en az `x` boşluk.
- Yatay lockup dijitalde en az 120 px genişlik; altında yalnız sembol veya app icon.
- Sembol tek başına en az 24 px. 16 px'de iki şerit arasındaki boşluk kapanıyor; favicon için optik küçük boyut versiyonu kullanıcı onayı bekliyor.

## Yasaklar

- sembolü yeniden çizmek, oranını veya şerit boşluğunu değiştirmek
- gradient, gölge, outline veya lila ile iki tonlu yeniden boyamak (onaysız)
- wordmark'ı başka fontla veya canlı metinle yeniden yazmak
- sembolü döndürmek veya yönünü çevirmek

Üretim kaydı: [[Asset_Pipeline/Logo/index]] · QA: `Asset_Pipeline/Logo/QA/logo-family-contact-sheet.png`.
