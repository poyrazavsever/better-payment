---
tur: gunluk
alan: kayıtlar
guncelleme: 2026-10-01
ozet: "Better Payment kişisel katkı sisteminin ilk kurulum kaydı."
durum: tamamlandi
---
# 2026-10-01 — Vault Başlangıcı

## Bugünün hedefi

Better Payment için plan, araştırma, ADR, review ve topluluk çalışmalarını tek bir yerel sistemde toplamak.

## Yapılanlar

- [[Harita]] ve çalışma sözleşmesi oluşturuldu.
- Misyon, vizyon, mevcut durum ve 90 günlük maintainer yolu kanonik notlara ayrıldı.
- Issue portföyü ve temel rehberler eklendi.
- Yerel ignore, pre-commit/pre-push güvenliği ve vault doğrulama aracı hazırlandı.
- Bilgisayarlar arası senkronizasyon için yalnız vault dosyalarını taşıyan bağımsız `personal/vault` branch politikası ve sert push korumaları hazırlandı.
- Vault, fork'taki bağımsız [`personal/vault`](https://github.com/poyrazavsever/better-payment/tree/personal/vault) branch'ine gönderildi; doğru hedef ve yanlışlıkla `main`e push senaryoları hook testleriyle doğrulandı.
- [#108](https://github.com/czaydev/better-payment/issues/108) için yaklaşımı açıklayan sahiplenme yorumu gönderildi.
- [#108](https://github.com/czaydev/better-payment/issues/108) için `upstream/main` tabanlı `codex/issue-108-node24-actions` branch'i açıldı; action release note'ları doğrulanıp üç workflow güncellendi.
- [#108](https://github.com/czaydev/better-payment/issues/108) için [PR #122](https://github.com/czaydev/better-payment/pull/122) açıldı; merge edildiğinde issue otomatik kapanacak.
- [#106](https://github.com/czaydev/better-payment/issues/106) için #108 sonrasına sıra niyeti belirtildi.
- [#106](https://github.com/czaydev/better-payment/issues/106) uygulaması tamamlandı ve [PR #121](https://github.com/czaydev/better-payment/pull/121) açıldı. PR, merge edildiğinde issue'yu otomatik kapatacak.

## Kararlar ve öğrenilenler

- Vault ve yardımcı araçlar yalnız fork'taki bağımsız `personal/vault` branch'inde tutulacak; `main`e, feature branch'lere ve upstream PR'lara hiçbir koşulda dahil edilmeyecek.
- İlk teknik katkı, nightly sandbox güvenilirliğindeki deterministik hatayı hedefleyecek.
- Maintainer yolu yetki talebiyle değil, ölçülebilir sahiplik ve düzenli review geçmişiyle kurulacak.

## Sonraki net adım

[PR #121](https://github.com/czaydev/better-payment/pull/121) ve [PR #122](https://github.com/czaydev/better-payment/pull/122) için code owner review ile fork workflow onaylarını takip etmek; #122 için maintainer publish dry-run sonucunu kaydetmek.
