---
tur: rehber
alan: review
guncelleme: 2026-10-01
ozet: "Better Payment pull request'leri için risk odaklı inceleme kontrol listesi."
durum: aktif
---
# PR Review Rehberi

## İnceleme sırası

1. PR'ın vaadi ile diff aynı kapsamda mı?
2. Public API, type ve hata sözleşmesi geriye uyumlu mu?
3. Para tutarı, para birimi, taksit, refund ve idempotency davranışı doğru mu?
4. Provider'a özgü ayrıntı ortak abstraction'a sızıyor mu?
5. Credential, kart verisi, imza veya kişisel veri loglanıyor mu?
6. Başarılı akış kadar hata, timeout ve eksik veri yolları test edilmiş mi?
7. Dokümantasyon ve örnekler gerçek API ile uyumlu mu?

## Kanıt standardı

- Yorum; dosya/satır, yeniden üretim yolu ve kullanıcı etkisini açıklar.
- Bloklayan yorum yalnız correctness, security, compatibility veya açık proje standardına dayanır.
- Tercih niteliğindeki öneriler `non-blocking` olarak belirtilir.
- Review sonucu: `approve`, `comment` veya `request changes`; gerekçe kısa ve eyleme dönüktür.

## Göndermeden önce

- CI kontrollerinin tamamını ve son commit'i kontrol et.
- Benzer provider implementasyonlarını karşılaştır.
- Değişiklik release note gerektiriyor mu değerlendir.
- Takip işi gerekiyorsa mevcut PR'ı büyütmek yerine ayrı issue öner.

