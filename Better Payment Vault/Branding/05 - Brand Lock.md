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

## Palet (K2)

Durum: üç aday kullanıcı seçiminde. Panolar: `Asset_Pipeline/Logo/Konsept/palette-A.png`, `palette-B.png`, `palette-C.png`, interaktif karşılaştırma `palette-karsilastirma.html`.

| Rol | A · Açık Hava | B · İndigo Sinyal | C · Teknik Defter |
|---|---|---|---|
| Canvas | `#F6F9FD` | `#F8F8FC` | `#FAFAF7` |
| Surface | `#FFFFFF` | `#FFFFFF` | `#FFFFFF` |
| Ink | `#0B1526` (17.3:1) | `#13132B` (17.2:1) | `#101114` (18.1:1) |
| Muted | `#55627A` (5.8:1) | `#5A5A78` (6.3:1) | `#5C5F66` (6.1:1) |
| Line | `#DFE6F0` | `#E4E3F0` | `#E6E5DF` |
| Primary | `#1A56F0` Route Blue (beyaz 5.8:1) | `#4338F2` Signal Indigo (beyaz 6.8:1) | `#0F5EFF` Signal Blue (beyaz 5.2:1) |
| Tint | `#E3ECFF` | `#ECEAFF` | `#EAF1FF` |
| Accent (yalnız dekor) | `#7FB2FF` Air | `#A9A3FF` Lilac | `#14B88A` Verified Mint |

Ortak semantik renkler (beyaz üzerinde ≥ 4.5:1): success `#087A55`, warning `#A86207`, danger `#C8322B`.

## Tipografi (K3)

Durum: palet seçiminden sonra 2–3 çift sunulacak.

## Logo (K4–K6)

Durum: tipografiden sonra. Brief: [[Asset_Pipeline/Logo/Brief - Better Payment Logo v1]].

İlgili: [[Branding/00 - Branding Ana Planı]] · [[Branding/03 - Higgsfield Kurulum ve Üretim Protokolü]]
