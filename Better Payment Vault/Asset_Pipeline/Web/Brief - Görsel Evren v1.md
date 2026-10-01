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
| A · Yumuşak mat | GPT Image 2 | kullanıcı değerlendirmesinde |
| B · Buzlu cam | GPT Image 2 | kullanıcı değerlendirmesinde |
| C · Düz geometrik | GPT Image 2 | kullanıcı değerlendirmesinde |

Teknik bulgu: `--background transparent` istenmesine rağmen GPT Image 2 alfa kanalı üretmedi, arka plana sahte dama deseni çizdi. Final üretim düz Canvas `#F8F8FC` zeminde yapılır, arka plan ayrı bir adımda temizlenir. Üç model de objeyi logonun 3D yorumu olarak çizdi; ikon setinde konu başına ayrı form tarif edilmeli. Maliyet: 3 × 6.5 = 19.5 kredi.
