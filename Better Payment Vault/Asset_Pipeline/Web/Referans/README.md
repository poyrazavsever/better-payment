---
tur: kaynak-envanteri
alan: web-branding
guncelleme: 2026-10-01
ozet: "Kullanıcının paylaştığı beş landing page referansından web, docs ve görsel evren sinyalleri."
durum: aktif
---
# Web Referans Envanteri

2026-10-01'de kullanıcı tarafından paylaşıldı. Görseller yalnız `style-reference` rolündedir; layout, illüstrasyon, metin ve marka öğeleri kopyalanmaz, Higgsfield'a input olarak yüklenmez. Saklama kuralı [[Asset_Pipeline/Logo/Referans/README]] ile aynıdır.

## Kullanıcının tarif ettiği his

- sade, şık, yenilikçi ve fresh
- light-first; dark mode ancak sonraki fazlarda
- güvenilir hissettiren bütünlük: hero görseli, ikonlar, küçük görsel öğeler ve web aynı markaya ait görünmeli
- maskot değil; Higgsfield ile üretilecek, Better Payment'a ait bir görsel ve ikon evreni
- aynı dil landing page ile sınırlı kalmamalı; dokümantasyona da taşınmalı

## Dosyalar

| Dosya | Kullanılabilir sinyal | Kopyalanmayacak / kaçınılacak |
|---|---|---|
| `web-01-chronotask-hero.png` | açık kırık-beyaz canvas, çok hafif nokta ızgarası; ortada iki tonlu büyük başlık (ikinci satır gri); tek mavi CTA; başlığı çerçeveleyen yumuşak, dokunsal 3D objeler ve gerçek ürün parçaları | yapışkan not, uygulama ikonları ve kart dizilimi; aynı merkez kompozisyon |
| `web-02-nourish-landing.png` | açık mavi paneller, büyük radius; başlık içine yerleştirilmiş küçük görsel çipler; tek bir marka glyph'inin sistemli tekrarı; mavi ana vurgu | sparkle glyph (yasak kalıp), doğrulanmamış stat kutuları, doğa fotoğrafı |
| `web-03-podcastly-hero.webp` | yuvarlatılmış çerçeve içinde tek, art-direction'lı hero dünyası; ikon setinin aynı malzeme ve ışıkla üretilmesi; kartların aynı aileden görünmesi | “Top #1” eyebrow, uydurma logo şeridi, tekrar eden kartlar, ağır glass efekti, sıcak/pembe palet |
| `web-04-platform-restaurant-hero.png` | beyaz hero, net başlık, ürün arayüzü merkezde; etrafında durum bildiren küçük çipler ve onları bağlayan el çizimi oklar; çok hafif mavi-mor hale | sahte dashboard metrikleri, insan avatarları, Watch video kalıbı |
| `web-05-startive-finance-landing.png` | finans güveni veren hava gibi açık mavi-beyaz ışık; merkez başlık ve kelimede yumuşak ton geçişi; sakin bölüm ritmi | “New” eyebrow pill, “Trusted by 120+ brands”, her bölümde aynı kart grid'i, lorem dashboard |

## Better Payment'a çevrilen sentez

1. **Canvas:** beyaz/kırık-beyaz yüzey, en fazla bir hafif doku (nokta ızgarası veya çok hafif mavi ışık). Hava ferah, yoğunluk düşük.
2. **Merkez:** hero'da büyük ve doğrudan başlık; altında tek birincil CTA. Eyebrow yok.
3. **Sahip olunan görsel evren:** Higgsfield ile Brand Lock sonrası üretilen tek bir hero artwork ve aynı malzeme, ışık ve açıyla üretilmiş ikon/obje seti. Objeler seçilen logo geometrisinden türetilir (modüler blok, geçit, ray); para, kart, kalkan veya sparkle klişesi değil.
4. **Başlık içi çipler:** Nourish'teki gibi başlıkların içine küçük marka ikonları veya provider logoları yerleştirilebilir; yalnız anlam taşıyorsa ve metin olmadan da cümle okunuyorsa.
5. **Durum kartları:** Platform/ChronoTask'taki yüzen kart hissi, yalnız gerçek SDK durumlarını gösteren kartlarla verilir: `status: "pending"` 3DS, doğrulanan callback, `payment.succeeded` event'i, `INVALID_HASH` ile reddedilen sahte callback. Uydurma metrik yok.
6. **Docs:** aynı token'lar, ikon seti ve light tema Fumadocs'a taşınır; docs ana sayfası ve kategori sayfaları aynı ikonlarla işaretlenir.

## Açık gerilimler

- [[Kararlar/ADR-003 - Branding Önce Light First ve Tek PR]] “işlevi olmayan yüzen kartlar ve sahte dashboard” yasaklar. Referanslardaki kart hissi yalnız gerçek ürün durumu taşıyan kartlarla uyumlu kabul edilir. Karar: [[Kararlar/ADR-005 - Sahip Olunan Görsel Evren]].
- Hero artwork LCP bütçesini bozmamalı: optimize AVIF/WebP still, metin ve CTA görselden bağımsız ilk boyamada görünür.
- Hero merkezindeki provider network kod tabanlı (SVG/React) kalır; artwork onun zemini veya çerçevesidir, yerine geçmez.
