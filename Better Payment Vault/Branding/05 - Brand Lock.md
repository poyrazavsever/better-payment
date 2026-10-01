---
tur: marka-sistemi
alan: branding
guncelleme: 2026-10-01
ozet: "Better Payment Brand Lock: kilitlenen ve önerilen marka kararlarının kanonik kaydı; Brandkit state'inin makineler arası yedeği."
durum: aktif
---
# Brand Lock

Brandkit onay state'i (`brandkit/state.json`) yerel kalır ve makineler arasında taşınmaz. Bu not her onaylanan slotun kanonik yedeğidir; başka makinede state buradaki değerlerle yeniden kurulur.

Durumlar: `fixed` (onaylı) · `proposed` (aday) · `unknown`.

## Kimlik

| Alan | Değer | Durum |
|---|---|---|
| Marka adı ve wordmark yazımı | `Better Payment` | fixed · K1, 2026-10-01 |
| Paket/kod adı | `better-payment`; yalnız kod, npm ve kurulum komutlarında | fixed · K1 |
| Ton | sade, şık, fresh, güvenilir, teknik | fixed · K1 |
| Görsel eksenler | restrained↔expressive `55` · geometric↔organic `35` · familiar↔experimental `60` | fixed · state'e yazıldı |

## Palet (K2) — fixed

Kullanıcı 2026-10-01'de **B · İndigo Sinyal** paletini seçti. Brandkit state: `approve_palette`, palette revision `1`.

| Rol | İsim | Hex | Not |
|---|---|---|---|
| background | Canvas | `#F8F8FC` | sayfa zemini |
| surface | Surface | `#FFFFFF` | kart, kod, panel |
| text | Ink | `#13132B` | 17.2:1 |
| secondary text | Muted | `#5A5A78` | 6.3:1 |
| border | Line | `#E4E3F0` | çizgi |
| primary | Signal Indigo | `#4338F2` | beyaz yazı 6.8:1 |
| tint surface | Lilac Tint | `#ECEAFF` | vurgu zemini |
| accent | Lilac | `#A9A3FF` | yalnız dekor ve logo ikinci tonu; metin değil |
| semantic | Success | `#087A55` | beyaz üzerinde 5.4:1 |
| semantic | Warning | `#A86207` | 4.8:1 |
| semantic | Danger | `#C8322B` | 5.3:1 |

Elenen adaylar: A · Açık Hava (`#1A56F0`), C · Teknik Defter (`#0F5EFF`). Panolar `Asset_Pipeline/Logo/Konsept/palette-*.png`.

Not: Signal Indigo Stripe moruna komşu; logo aşamasında yedi referansla karışma kontrolü zorunlu.

## Tipografi (K3) — fixed

Kullanıcı 2026-10-01'de **T1 · Güvenli Geometri** çiftini seçti. Brandkit state: `approve_typography`, typography revision `1`.

| Rol | Font | Ağırlık | Kaynak |
|---|---|---|---|
| display / heading / wordmark | Manrope | 800 display, 700 heading | [Google Fonts](https://fonts.google.com/specimen/Manrope) |
| body / UI | Inter | 400, 500, 600 | [Google Fonts](https://fonts.google.com/specimen/Inter) |
| code | JetBrains Mono | 400, 500 | [Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono) |

- Üçü de `latin-ext` ve `cyrillic` kapsar; Türkçe ve Kiril render testi geçti.
- Web'de `next/font/google` ile self-host edilir; Geist ve Geist Mono branding PR'ında kaldırılır.
- Brandkit state şeması yalnız display/body tutar; mono kararı bu notta kanoniktir.
- Arapça (#114) için ayrı fallback font, ilgili locale işinde seçilir.

Elenen adaylar: T2 Onest + Geist + Geist Mono, T3 Unbounded + Inter + IBM Plex Mono. Panolar `Asset_Pipeline/Logo/Konsept/type-T*.png`.

## Logo (K4–K6)

Durum: sıradaki kapı K4 (logo yolu). Palet ve tipografi kilitli. Brief: [[Asset_Pipeline/Logo/Brief - Better Payment Logo v1]].

İlgili: [[Branding/00 - Branding Ana Planı]] · [[Branding/03 - Higgsfield Kurulum ve Üretim Protokolü]]
