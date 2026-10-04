---
tur: portfoy
alan: planlama
guncelleme: 2026-10-04
ozet: "Açık issue'ların bağımlılık, risk ve katkı sırasına göre kanonik sınıflandırması."
durum: aktif
---
# Issue Portföyü

## Sıradaki işler

Önce [[Öğrenme/00 - Kod Tabanı Öğrenme Planı]]; ardından daha basit, "good first issue" seviyesinde işler seçilecek. #95 ve #93'ten 2026-10-04'te vazgeçildi.

## Öncelik 0: güvenilirlik

| İş | Durum | Sonraki adım |
|---|---|---|
| Nightly iyzico isim gölgeleme hatası | hazir | Küçük PR, sandbox rerun |
| [#108 Actions Node 20 uyarısı](https://github.com/czaydev/better-payment/issues/108) | [PR #122](https://github.com/czaydev/better-payment/pull/122) açıldı | Code owner review, fork workflow onayı ve publish dry-run doğrulaması bekleniyor |

## Başlangıç katkıları

| Issue | Neden |
|---|---|
| [#106](https://github.com/czaydev/better-payment/issues/106) | [PR #121](https://github.com/czaydev/better-payment/pull/121) açıldı; code owner review ve fork workflow onayı bekleniyor |
| #103 | Core yardımcı, kuruş hassasiyeti, property-style test |
| #111 | #112–#115'i açan yüksek etkili web altyapısı |
| #82 | Parampos hata deneyimi; resmi kaynak şart |

## Tasarım bekleyen zincir

- #116 önce tasarım tartışması.
- #90 ve #91 storage adapter kararı bekliyor.
- #104 pending resolver store tasarımını bekliyor.
- #105 fraud counters aynı KV katmanını bekliyor.
- #41 reconciliation ledger üzerine kurulacak.
- #53 dashboard/audit daha sonra ledger kullanacak.

## Credential veya dış doküman kapısı

- #22 contract recordings.
- #60 PayTR pre-authorization.
- #62 PayTR, #63 Parampos, #64 Akbank sandbox.
- #30 Parampos foreign currency.
- #36–#40 yeni bankalar ve kurumlar.
- #65 Parampos/Akbank stored cards.

## Web ve DX

- **Yeni bir tracking issue gerekli:** website launch readiness + visual refresh. Mevcut issue'lar doğrudan redesign ve duyuru sahipliği sunmuyor.
- #48 eski homepage iddialarını düzeltti ve kapandı; görsel yenileme kapsamı değildi.
- #59 TR/EN altyapısını tamamladı ve kapandı; ilk lansman için dil tabanı hazır.
- #98 Next.js + Prisma uçtan uca örnek uygulama, lansman için en güçlü açık demo/proof issue'su; yüksek öncelik adayı.
- #111 ve #112–#115 uluslararası erişimi genişletir fakat ilk TR/EN lansmanını bloklamaz.
- #93 NestJS, #94 Nuxt, #95 SvelteKit, #96 React Router. #93 ve #95'i üstlenmiştim, 2026-10-04'te bıraktım (daha basit işlerle ilerleme kararı).
- #97 Elysia: [PR #128](https://github.com/czaydev/better-payment/pull/128) ile merge edildi; `exports` ve `parse: 'none'` düzeltmelerini biz push ettik (e97de06).
- #107 release PR otomasyonu.
- #84 Arapça localized errors.

Ayrıntılı değerlendirme: [[Araştırma/İnceleme - 2026-10-01 Lansman ve Web Sitesi Önceliği]].

## Büyük ürün bahisleri

- #88 marketplace payments.
- #89 unified hosted checkout.
- #92 CLI.
- #42 telemetry.
- #43 1.0 readiness.
- #51 commission router.
- #70 versioned docs, 1.0 sonrası.

## WIP kuralı

Aynı anda yalnız bir issue aktif implementasyonda tutulur. Sonraki issue için sıra niyeti belirtilebilir ama ilk iş kapanmadan kodlamaya başlanmaz. Atanmış issue'ya maintainer açıkça istemeden girilmez.
