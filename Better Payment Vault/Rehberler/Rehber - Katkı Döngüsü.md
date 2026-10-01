---
tur: rehber
alan: katkı
guncelleme: 2026-10-01
ozet: "Bir fikri küçük, doğrulanabilir ve review edilebilir bir katkıya dönüştürme akışı."
durum: aktif
---
# Katkı Döngüsü

## 1. Seç

- Tek bir sorun ve ölçülebilir bir sonuç seç.
- [[Planlama/Issue Portföyü]] içindeki öncelik, bağımlılık ve sahiplik bilgisini kontrol et.
- Büyük özelliklerde önce issue üzerinde kapsam ve API tasarımı konusunda mutabakat ara.

## 2. Kanıtla

- Hatanın mevcut davranışını test, log veya minimal reproduction ile kaydet.
- Başarı koşullarını yaz: hangi test geçecek, hangi çıktı değişecek, ne değişmeyecek?
- Güvenlik veya provider davranışı söz konusuysa varsayımı resmi dokümanla doğrula.

## 3. Daralt

- Bir PR; bir ana amaç, az sayıda dosya ve okunabilir commit geçmişi taşımalı.
- Refactor ile davranış değişikliğini mümkünse ayır.
- Public API değişiyorsa types, docs, tests ve changelog etkisini birlikte değerlendir.

## 4. Uygula ve doğrula

- Önce hedef testi, ardından ilgili paket testlerini çalıştır.
- Lint, typecheck, build ve sandbox etkisini kontrol et.
- Provider credential'ı veya gerçek kart verisini hiçbir dosyaya/loga yazma.

## 5. Review'e hazırla

- [[Rehberler/Rehber - PR Review]] kontrol listesini uygula.
- PR açıklamasında problem, çözüm, kapsam dışı maddeler ve doğrulama komutları bulunsun.
- İlgili issue'yu bağla; ekran görüntüsü veya log gerekiyorsa yalnız güvenli/sanitize edilmiş çıktı kullan.

## 6. Öğrenmeyi kapat

- Sonucu ilgili issue kaydına ve gerekiyorsa ADR'a işle.
- Bir sonraki katkıyı, review geri bildiriminden çıkan en yüksek kaldıraçlı iş olarak seç.

