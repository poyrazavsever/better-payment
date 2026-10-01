---
tur: adr
alan: kararlar
guncelleme: 2026-10-01
ozet: "Craftgate north star'ına SDK güvenilirliği üzerinden aşamalı ilerleme kararı."
durum: onerilen
---
# ADR-002: SDK Önce Aşamalı Ürün Vizyonu

## Bağlam

Proje sahibi açık kaynak Craftgate alternatifi, Better Auth benzeri ekosistem ve global provider/MoR desteği hedefliyor. Mevcut ürün ise güçlü fakat henüz sınırlı gerçek sandbox kapsamı olan birleşik SDK'dır.

## Karar

Ürün vizyonu üç bağımsız olgunluk aşamasında ele alınır:

1. Güvenilir Türkiye ödeme SDK'sı.
2. Opsiyonel state ve plugin'ler üzerinde ödeme orkestrasyonu.
3. PSP ve MoR için capability tabanlı global billing katmanı.

Polar benzeri MoR entegrasyonları ürün, sipariş, abonelik ve vergi semantiği taşıdığı için mevcut `PaymentProvider` arayüzüne zorlanmaz.

## Sonuçlar

- Kısa vadeli pazarlama dürüst ve kanıt temelli olur.
- Provider doğruluğu orkestrasyon özelliklerinden önce gelir.
- #116 ledger RFC'si, ilerideki operasyon katmanının temeli olur.
- Global billing, çekirdek payment API'sini karmaşıklaştırmadan ayrı capability yüzeyi kazanır.

## Açık doğrulama

- Maintainer ile vizyon sıralamasının onaylanması.
- #116 tasarımında adapter ve schema sınırının netleşmesi.
- 1.0 stabilite politikasına capability/experimental işaretlerinin eklenmesi.

