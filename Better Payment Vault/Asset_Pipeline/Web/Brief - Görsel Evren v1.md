---
tur: brief
alan: web-branding
guncelleme: 2026-10-01
ozet: "Better Payment hero artwork ve ikon/obje seti için brief ve stil testi kaydı (ADR-005)."
durum: aktif
---
# Brief — Görsel Evren v1

Karar: [[Kararlar/ADR-005 - Sahip Olunan Görsel Evren]] · Brand Lock: [[Branding/05 - Brand Lock]] · Referanslar: [[Asset_Pipeline/Web/Referans/README]].

## Amaç

Landing page, docs ve lansman görsellerinde aynı markaya ait hissettiren tek bir görsel dil: bir hero artwork ve 12–16 parçalık ikon/obje seti.

## Brand Lock bloğu (her prompt'a aynen girer)

- Palet: Signal Indigo `#4338F2` ana obje rengi, Lilac `#A9A3FF` ikinci ton, Lilac Tint `#ECEAFF` ve Canvas `#F8F8FC` açık yüzey, Ink `#13132B` yalnız çok küçük vurgu.
- Form dili: logodaki iki şeridin birleşmesinden türeyen yuvarlak uçlu, kalın, akıcı şeritler; geometrik, az parçalı.
- Yasak: kredi kartı, madeni para, para birimi simgesi, kalkan, kilit, sparkle, onay işareti, küre/orbit, rastgele network çizgisi, maskot, yazı, logo kopyası, sahte arayüz.

## Aşamalar

1. **Stil testi:** aynı konu (“tek API'de birleşen yollar” objesi) üç malzeme diliyle. Kullanıcı birini seçer.
2. **İkon seti:** seçilen dille önce 3 ikon, onaydan sonra kalan set tek turda aynı stil referansıyla.
3. **Hero artwork:** ikon seti diliyle 2–3 aday; yazı ve logo görsele gömülmez, kodla eklenir.

## İkon seti adayı listesi

Tek API · callback doğrulama · 3D Secure · iade · iptal · taksit · durum sorgu · event/listener · plugin · edge runtime · test/sandbox · çok dil · güvenli handler · idempotency · sağlayıcı ekleme · dokümantasyon.

## Stil testi kaydı

| Yön | Model | Sonuç |
|---|---|---|
| A · Yumuşak mat | GPT Image 2 | elendi |
| B · Buzlu cam | GPT Image 2 | **seçildi** (2026-10-01): premium, şık, modern; 3D derinlik korunur |
| C · Düz geometrik | GPT Image 2 | elendi |

Teknik bulgu: `--background transparent` istenmesine rağmen GPT Image 2 alfa kanalı üretmedi, arka plana sahte dama deseni çizdi. Final üretim düz Canvas `#F8F8FC` zeminde yapılır, arka plan ayrı bir adımda temizlenir. Üç model de objeyi logonun 3D yorumu olarak çizdi; ikon setinde konu başına ayrı form tarif edilmeli. Maliyet: 3 × 6.5 = 19.5 kredi.

## İkon seti v1 — ilk üç ikon

Stil referansı: `Konsept/icon-style-test-B.jpg`. Üretim düz `#F8F8FC` zeminde, ardından `image_background_remover` ile gerçek alfa. Şeffaf masterlar `Ikon/Seffaf/`, job kayıtları `Ikon/Kaynak/jobs.md`, inceleme `QA/ikon-seti-v1.html`.

| İkon | Form | Not |
|---|---|---|
| callback doğrulama | kapalı döngü, indigo mühür parçası | ilk deneme anahtar deliği ürettiği için (kilit klişesi) yeniden üretildi; zincir halkasını andırabilir |
| iade | kendi üzerine dönen yol, indigo kare | geri al oku dili; en okunur |
| taksit | dört kapsül, ilki dolu | ilk deneme düz ve küçük kaldı, yeniden üretildi; sinyal çubuğunu andırabilir |

Bulgular: beyaz zeminde cam gövde soluk kalır, indigo çekirdek okunurluğu taşır; 40 px altında detay kaybolur. Docs'ta en az 40 px veya Lilac Tint kutucuk içinde kullanılması önerilir.

Durum: kullanıcı onayı bekliyor. Maliyet: stil testi 19.5 + ikonlar 5 × 6.5 + temizleme 3 = 55 kredi.
