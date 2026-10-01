---
tur: adr
alan: branding
guncelleme: 2026-10-01
ozet: "Hero artwork, ikon/obje seti ve gerçek durum kartlarından oluşan, web ve docs'a yayılan Better Payment görsel evreni kararı."
durum: onerilen
---
# ADR-005: Sahip Olunan Görsel Evren

## Bağlam

2026-10-01'de kullanıcı beş landing page referansı paylaştı ([[Asset_Pipeline/Web/Referans/README]]). Beklenti: sade, şık, fresh ve güvenilir; hero'da güçlü bir görsel; maskot olmadan Better Payment'a ait görseller, ikonlar ve küçük görsel öğelerle bütünlük. Bu bütünlük hem landing page'de hem dokümantasyonda hissedilmeli.

[[Kararlar/ADR-003 - Branding Önce Light First ve Tek PR]] yalnız kod tabanlı hero network'ünü tanımlıyor ve yüzen kartları yasaklıyor; görsel evreni ve docs kapsamını açıkça kapsamıyor.

## Karar

- Better Payment'ın üç katmanlı bir görsel evreni olur:
  1. **Hero artwork:** Brand Lock sonrası Higgsfield Generate ile üretilen tek bir art-direction'lı, light ve seçilen paletle uyumlu görsel. Kod tabanlı provider network'ün zemini veya çerçevesidir; onun yerine geçmez.
  2. **İkon/obje seti:** aynı malzeme, ışık, açı ve paletle üretilmiş 12–16 parçalık set. Formlar seçilen logo geometrisinden türetilir. Özellik bölümleri, başlık içi çipler, docs kategori sayfaları ve sosyal görseller aynı seti kullanır.
  3. **Durum kartları:** yüzen kart hissi yalnız gerçek SDK durumlarıyla verilir (`pending` 3DS, doğrulanan callback, `payment.succeeded`, reddedilen `INVALID_HASH`). Kart içeriği kodla render edilir, görsele gömülmez.
- Maskot yok.
- Branding kapsamı docs'u da içerir: aynı token'lar, light tema ve ikon seti Fumadocs'a uygulanır.
- ADR-003'teki “işlevi olmayan yüzen kart” yasağı korunur; gerçek ürün durumu taşıyan kartlar bu yasağın dışında sayılır.

## Seçenekler

- **Yalnız kod tabanlı minimal site:** en hızlı ve en güvenli seçenek, fakat kullanıcının istediği bütüncül marka hissini vermez.
- **Maskot tabanlı evren:** güçlü akılda kalıcılık, fakat ödeme altyapısında güven tonuyla çatışır ve kullanıcı istemedi.
- **Seçilen:** logo geometrisinden türeyen hero artwork + ikon seti + gerçek durum kartları.

## Sonuçlar

- Asset Pipeline'a `Web` hattında hero artwork ve ikon seti işleri eklenir; ikisi de Brand Lock (palet + logo + tipografi) onayına bağlıdır.
- İkon seti tek turda tutarlı üretilir; sonradan eklenen ikonlar aynı stil referansını kullanır.
- Hero görseli optimize still olur; LCP, metin ve CTA görselden bağımsızdır.
- AI üretimi metin, logo veya provider logosu görsele gömülmez; bunlar SVG/HTML katmanında kalır.
- Docs teması branding PR'ının kapsamına girer; PR büyür, bu nedenle docs için ayrı commit ve ekran görüntüsü kapısı eklenir.

## Doğrulama

- Kullanıcı bu ADR'yi `kabul` durumuna çekene kadar görsel evren üretimi başlamaz.
- Hero artwork ve ikon seti için ayrı brief: `Asset_Pipeline/Web/`.
- QA: ikon setinin 24/48/96 px'de okunurluğu, aynı ışık yönü, palet dışı renk yok, desktop/mobile hero LCP ölçümü.
