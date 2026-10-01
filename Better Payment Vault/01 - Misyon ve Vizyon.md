---
tur: strateji
alan: urun
guncelleme: 2026-10-01
ozet: "better-payment misyonu, north star vizyonu ve aşamalı ürün sınırı."
durum: aktif
---
# Misyon ve Vizyon

## Bugünkü misyon

Türkiye'deki ödeme kuruluşları ve banka sanal POS'larını güvenli, tip güvenli ve framework bağımsız tek bir TypeScript API altında toplamak.

## North star

Craftgate benzeri açık kaynak bir ödeme orkestrasyonu katmanı; Better Auth benzeri plugin, adapter ve topluluk ekosistemi; daha sonra global PSP ve Merchant of Record entegrasyonları.

## Aşamalı vizyon

1. **Güvenilir SDK:** provider doğruluğu, gerçek sandbox kanıtı, contract fixture'ları, güvenli callback'ler.
2. **Ödeme orkestrasyonu:** ledger, routing, reconciliation, marketplace, fraud ve operasyon araçları.
3. **Global billing:** Stripe benzeri PSP'ler ve Polar benzeri MoR çözümleri için capability tabanlı ayrı yüzeyler.

Ürün konumlandırma kararı için [[Kararlar/ADR-002 - SDK Önce Aşamalı Ürün Vizyonu]].

## Bugün kullanılacak ifade

> Türkiye'deki ödeme sağlayıcılarını güvenli ve tip güvenli tek bir TypeScript API altında toplayan açık kaynak ödeme SDK'sı; uzun vadede açık kaynak ödeme orkestrasyonuna doğru ilerliyor.

## Kaçınılacak ifade

Gerçek sandbox kapsamı ve operasyon katmanı tamamlanmadan “production-ready Craftgate alternatifi” denmez.

