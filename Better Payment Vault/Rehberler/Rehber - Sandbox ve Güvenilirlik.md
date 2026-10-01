---
tur: rehber
alan: güvenilirlik
guncelleme: 2026-10-01
ozet: "Provider sandbox testlerini kararlı, güvenli ve teşhis edilebilir tutma yaklaşımı."
durum: aktif
---
# Sandbox ve Güvenilirlik Rehberi

## Amaç

Sandbox testleri provider entegrasyonunun canlı sözleşmeye en yakın erken uyarı katmanıdır. Bir başarısızlık; ürün regresyonu, provider değişikliği, credential sorunu veya test altyapısı hatası olarak sınıflandırılmalıdır.

## Teşhis sırası

1. Workflow ve test daha provider çağrısından önce mi kırılıyor?
2. Hata deterministik mi; son başarılı run ve ilk başarısız run hangileri?
3. Kod, environment variable isimleri veya SDK başlangıç sırası değişti mi?
4. Provider endpoint'i, sertifika veya response şeması değişmiş olabilir mi?
5. Retry yalnız geçici ağ hatalarında mı uygulanıyor?

## Güvenlik sınırları

- Secret değerlerini terminale veya test çıktısına basma.
- Fixture'larda gerçek kart, müşteri veya merchant verisi kullanma.
- PR'dan gelen güvenilmeyen kodu repository secret'larıyla çalıştırma.
- Hata mesajlarını paylaşmadan önce sanitize et.

## Kararlılık ilkeleri

- Factory/import isimleri ile local değişkenleri çakıştırma.
- Testleri bağımsız ve tekrar çalıştırılabilir tut.
- Zaman, network ve provider kaynaklı flaky davranışı açıkça etiketle.
- Nightly başarısızlığı için issue, run linki, hata sınıfı ve sonraki aksiyon kaydı oluştur.

İlk hedef, [[Araştırma/İnceleme - 2026-10-01 Teknik ve Topluluk Durumu]] içinde belgelenen Iyzico sandbox başlangıç hatasını küçük bir düzeltmeyle kapatmaktır.

