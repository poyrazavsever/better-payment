---
tur: inceleme
alan: lansman
guncelleme: 2026-10-01
ozet: "Better Payment için web sitesi yenilemesi ve duyuru odaklı ilk çalışma hattı; mevcut issue eşlemesi ve eksik issue önerileri."
durum: aktif
---
# Lansman ve Web Sitesi Önceliği

## Öncelik kararı

İlk ürün odağı, yeni büyük özellik eklemekten önce Better Payment'ın dışarıdan görünen yüzünü lansmana hazır hâle getirmektir. Sıra şöyledir:

1. Mevcut web sitesinin anlatısını, görsel kimliğini ve dönüşüm akışını yenile.
2. Çalışan örnek ve güven kanıtlarıyla ürün iddialarını görünür biçimde doğrula.
3. Türkçe ve İngilizce duyuru materyallerini hazırla.
4. Ölçülebilir bir soft launch yap, geri bildirimi site ve roadmap'e işle.

Bu karar, teknik güvenilirlikten vazgeçmek anlamına gelmez. Açık [PR #121](https://github.com/czaydev/better-payment/pull/121) ve [PR #122](https://github.com/czaydev/better-payment/pull/122) takip edilir; fakat yeni iş seçerken lansman yüzeyi önce gelir.

## 2026-10-01 mevcut durum incelemesi

Canlı site: [better-payment.czaylabs.com](https://better-payment.czaylabs.com)

### Güçlü taraflar

- Canlı site güncel `0.5.2` sürümünü gösteriyor; eski v2/v3 anlatısı kaldırılmış.
- Türkçe ve İngilizce homepage ile dokümantasyon mevcut.
- Hero, problem/çözüm karşılaştırması, özellikler, provider/banka alanı, quick start ve CTA sıralaması anlaşılır.
- Ana CTA dokümantasyona, ikincil CTA GitHub'a yönlendiriyor.
- Mobil menü, koyu tema, locale routing, sitemap, robots ve hreflang altyapısı bulunuyor.
- Üretim build'i başarıyla tamamlandı: 62 statik sayfa üretildi.
- Ürün iddiaları büyük ölçüde güncel README ve API ile uyumlu.

### Lansman boşlukları

- Görsel sistem bilinçli olarak tamamen nötr; güçlü ve ayırt edilebilir bir Better Payment marka dili henüz oluşmuyor.
- Framework isimlerinden oluşan trust bar var, fakat kullanıcı logosu, gerçek kullanım örneği, katkıcı kanıtı, yıldız/download eğilimi veya vaka çalışması yok.
- Ziyaretçinin ödeme akışını deneyebileceği çalışan bir demo yok. Kod örneği var, ürün kanıtı sınırlı.
- Özel Open Graph/Twitter launch görseli, Twitter metadata'sı ve `SoftwareApplication`/`WebSite` structured data görünmüyor.
- Analytics veya privacy-friendly dönüşüm ölçümü görünmüyor; docs tıklaması, npm çıkışı, GitHub çıkışı ve demo tamamlama oranı ölçülemiyor.
- Duyuruya özel landing bölümü, press/brand kit, paylaşılabilir ekran görüntüleri ve kısa ürün demosu yok.
- Ana anlatı özellikleri listeliyor fakat kimin için, hangi göç senaryosunda ve neden bugün kullanılmalı sorularını sosyal kanıtla kapatmıyor.
- Website redesign, launch readiness ve announcement campaign işlerini tek hedef altında yöneten açık bir issue yok.

## Mevcut issue eşlemesi

| Issue | Durum | Lansman ilişkisi | Karar |
|---|---|---|---|
| [#48 Website homepage still advertises v3 and outdated claims](https://github.com/czaydev/better-payment/issues/48) | kapalı | Eski ve yanlış homepage anlatısını düzeltti | Tamamlanmış temel; redesign kapsamı değil |
| [#59 Website and docs in Turkish and English](https://github.com/czaydev/better-payment/issues/59) | kapalı | TR/EN lansman tabanını sağladı | Lansman için yeterli başlangıç dili |
| [#98 Example app: end-to-end shop with Next.js and Prisma](https://github.com/czaydev/better-payment/issues/98) | açık, atanmamış | En güçlü ürün kanıtı ve demo kaynağı | Lansman hattında yüksek önceliğe alınmalı; kapsamı büyükse önce küçük public demo dilimine ayrılmalı |
| [#111 Website i18n: support more than two languages](https://github.com/czaydev/better-payment/issues/111) | açık, atanmamış | Uluslararası büyüme altyapısı | İlk TR/EN lansmanını bloklamaz; redesign locale mimarisini bozmamalı |
| [#112 German](https://github.com/czaydev/better-payment/issues/112), [#113 Russian](https://github.com/czaydev/better-payment/issues/113), [#114 Arabic](https://github.com/czaydev/better-payment/issues/114), [#115 tracker](https://github.com/czaydev/better-payment/issues/115) | açık | Lansman sonrası erişim genişlemesi | #111 sonrası paralel topluluk işi |
| [#106 Added in x.y](https://github.com/czaydev/better-payment/issues/106) | açık, PR #121 hazır | Doküman güveni ve sürüm şeffaflığı | Merge takibi yapılmalı; redesign'i bloklamaz |
| [#44 Roadmap](https://github.com/czaydev/better-payment/issues/44) | açık | Tüm geliştirme planı | Lansman/web yenileme fazı bugün görünmüyor; roadmap'e eklenmesi önerilmeli |
| [#70 Versioned documentation](https://github.com/czaydev/better-payment/issues/70) | açık, 1.0 sonrası | Uzun vadeli docs güveni | Bu lansmanın kapsamı dışında |
| [#53 Embeddable UI components](https://github.com/czaydev/better-payment/issues/53) | açık, 1.0 sonrası | Ürün UI'sı; pazarlama sitesi değil | Homepage redesign ile karıştırılmamalı |

## Sonuç

Mevcut issue'lar web altyapısı, çeviri ve örnek uygulamanın parçalarını kapsıyor; fakat kullanıcının belirlediği önceliği doğrudan karşılayan bir redesign/lansman çalışma paketi yok. Bu nedenle mevcut issue'lardan yalnız #98 doğrudan lansman kaldıraçıdır. #111 ve çeviri zinciri büyümeyi destekler ama ilk lansman için kritik yol değildir.

## Açılması önerilen issue'lar

### 1. Tracking: Website launch readiness and visual refresh

Amaç: lansmanın tek kanonik epic'i. Başarı ölçütleri:

- Onaylanmış hedef kitle ve tek cümle değer önerisi.
- Homepage bilgi mimarisi, görsel yön ve içerik envanteri.
- Mobil, erişilebilirlik ve performans bütçesi.
- TR/EN içerik eşliği.
- Alt issue'lar, sorumlular, soft launch tarihi ve ölçümler.

### 2. Homepage redesign: product story, proof and conversion

- Hero ve CTA hiyerarşisi.
- “Neden Better Payment?” anlatısı ve göç senaryoları.
- Provider kapsamı ve güvenlik iddiaları için kanıt katmanı.
- Gerçek contributor/kullanım sinyalleri; doğrulanamayan logo veya sayı kullanılmaz.
- #98 demo veya küçük MockProvider playground'una görünür giriş.
- Launch öncesi desktop/mobile, dark/light ve TR/EN ekran görüntüleri.

### 3. Launch metadata, measurement and share assets

- Özel OG/Twitter görselleri ve metadata.
- `SoftwareApplication` ve `WebSite` structured data.
- Privacy-friendly analytics; docs, GitHub, npm ve demo dönüşümleri.
- Paylaşım kartları, logo paketi, kısa demo GIF/video ve ekran görüntüleri.
- Ölçüm olayları ve başlangıç metriği.

### 4. Announcement campaign: Turkish and English soft launch

- Ana duyuru metni, teknik deep-dive ve kısa sosyal gönderiler.
- Hedef kanallar ve yayın sırası.
- Provider sandbox/katkıcı çağrıları için ayrı CTA.
- İlk 24 saat, 7 gün ve 30 gün geri bildirim/ölçüm ritmi.
- Gelen soruların docs, issue ve roadmap'e dönüştürülmesi.

## Önerilen çalışma sırası

1. Furkan ile lansman hedefi, hedef kitle ve görsel yön üzerinde kısa mutabakat.
2. Tracking issue ve üç alt issue'yu aç; #98'i epic'e bağla.
3. İçerik ve tasarım brief'i; mevcut claim'leri kanıt kaynaklarıyla eşle.
4. Homepage redesign uygulaması ve görsel QA.
5. OG/SEO/analytics ile demo girişini tamamla.
6. Önce sınırlı soft launch, sonra TR/EN genel duyuru.

## Lansman ölçümleri

- Homepage → docs tıklama oranı.
- Homepage → GitHub ve npm çıkış oranı.
- Demo başlatma/tamamlama oranı.
- GitHub star, issue, contributor ve sandbox yardım dönüşümü.
- Duyuru sonrası 7/30 günlük npm indirme eğilimi.
- Gelen sorulardan dokümana dönüştürülen konu sayısı.

## Sınırlar

- Doğrulanmamış müşteri logosu, download sayısı veya performans iddiası kullanılmaz.
- Görsel yenileme, güvenlik ve provider kapsamı hakkında aşırı vaat üretmez.
- TR/EN eşliği korunur; #111 gelmeden yeni locale mimarisi yeniden yazılmaz.
- Duyuru, çalışan site/build ve güncel dokümantasyon doğrulanmadan yayınlanmaz.
