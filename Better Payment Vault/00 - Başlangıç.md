---
tur: baslangic
alan: sistem
guncelleme: 2026-10-01
ozet: "Vault'un amacı, kullanım sırası ve hızlı komutları."
durum: aktif
---
# Başlangıç

Bu vault, `better-payment` için kişisel katkı sistemi ve uzun vadeli maintainer hafızasıdır.

## İlk okuma sırası

1. [[01 - Misyon ve Vizyon]]
2. [[02 - Mevcut Durum ve Riskler]]
3. [[Planlama/Issue Portföyü]]
4. [[Planlama/90 Günlük Maintainer Yol Haritası]]
5. [[Rehberler/Rehber - Katkı Döngüsü]]

## Yerel komutlar

```powershell
node .local-tools/vault.mjs check
node .local-tools/vault.mjs lint
node .local-tools/vault.mjs pr-safety
node .local-tools/vault.mjs new-adr "Karar başlığı"
```

Hook kurulumu ve yeni klonda tekrar kurulum için [[Rehberler/Rehber - Vault Bakımı]] okunur.

## Sistem sınırı

Vault ve araçları yereldir. GitHub'a, fork'a veya upstream PR'a gönderilmez. Bu kararın gerekçesi [[Kararlar/ADR-001 - Vault Yerel ve PR Dışı]] içindedir.

