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

## Tipografi (K3)

Durum: üç aday kullanıcı seçiminde. Panolar `Asset_Pipeline/Logo/Konsept/type-T*.png` ve `tipografi-karsilastirma.html`.

| Aday | Display | Body | Mono |
|---|---|---|---|
| T1 · Güvenli Geometri | Manrope 800 | Inter 400 | JetBrains Mono |
| T2 · Keskin Altyapı | Onest 700 | Geist 400 | Geist Mono |
| T3 · Geniş İfade | Unbounded 600 | Inter 400 | IBM Plex Mono |

Seçim kriteri: Google Fonts, `latin-ext` ve `cyrillic` kapsamı. Plus Jakarta Sans, Bricolage Grotesque, Instrument Sans, Space Grotesk Kiril eksikliği nedeniyle aday dışı. Golos Text render testinde Türkçe `ğ` harfini doğru çizmediği için T3'ten çıkarıldı.

## Logo (K4–K6)

Durum: tipografiden sonra. Brief: [[Asset_Pipeline/Logo/Brief - Better Payment Logo v1]].

İlgili: [[Branding/00 - Branding Ana Planı]] · [[Branding/03 - Higgsfield Kurulum ve Üretim Protokolü]]
