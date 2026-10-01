---
tur: sistem
alan: vault
guncelleme: 2026-10-01
ozet: "Better Payment Vault çalışma ve doğruluk sözleşmesi."
durum: aktif
---
# Vault Çalışma Sözleşmesi

Bu vault, Poyraz'ın `better-payment` katkı, araştırma, karar ve maintainer hazırlık sistemidir. Projenin upstream dokümantasyonunun yerine geçmez; kişisel çalışma doğruluğunu ve sürekliliğini korur.

## Zorunlu kurallar

1. Yeni çalışma önce [[Harita]] üzerinden kanonik bir nota bağlanır.
2. Kesin mimari ve süreç kararları `Kararlar/ADR-*` içinde tutulur.
3. Issue durumları yalnız [[Planlama/Issue Portföyü]] içinde kanonik olarak izlenir.
4. Aktif hedefler [[Planlama/90 Günlük Maintainer Yol Haritası]] ile uyumlu olmalıdır.
5. Aynı bilgi iki ayrı notta kanonik tutulmaz; diğer notlar wiki link verir.
6. Her not `tur`, `alan`, `guncelleme` ve `ozet` frontmatter alanlarını taşır.
7. Tarihler `YYYY-MM-DD` biçimindedir.
8. Not 25 KB'a yaklaşınca bölünür.
9. Vault'a gerçek provider credential'ı, kart verisi, token, kişisel veri veya gizli müşteri bilgisi yazılmaz.
10. Bir iddia kanıt gerektiriyorsa issue, PR, commit, Actions run veya resmi doküman bağlantısı eklenir.
11. Karar durumu `onerilen`, `kabul`, `superseded` veya `iptal`; çalışma durumu `bekliyor`, `hazir`, `aktif`, `bloklu` veya `tamamlandi` olur.
12. Vault, `.local-tools` ve `.local-githooks` yalnızca yetim `personal/vault` branch'inde versionlanır; `main`, feature branch'leri ve upstream PR'larına hiçbir koşulda girmez. [[Kararlar/ADR-001 - Vault Yerel ve PR Dışı]] değiştirilemez güvenlik sınırıdır.

## Dil

Planlar ve değerlendirmeler Türkçe; kod, API, event, branch ve tablo adları İngilizce yazılır. Dışarı gönderilecek mesajlar hedef kitlenin dilinde hazırlanır.

## Çalışma ritmi

- Çalışmaya başlarken: [[Harita]] → ilgili plan → issue/PR kaydı.
- Karar verirken: ADR aç, seçenekleri ve sonuçları yaz.
- PR öncesi: [[Rehberler/Rehber - Katkı Döngüsü]] ve [[Rehberler/Rehber - PR Review]].
- Haftalık kapanışta: yol haritası, riskler, Actions ve topluluk ölçümleri güncellenir.
