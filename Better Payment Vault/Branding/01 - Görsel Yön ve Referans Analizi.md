---
tur: inceleme
alan: branding
guncelleme: 2026-10-01
ozet: "Kullanıcı tarafından sağlanan üç ilham görselinin Better Payment görsel yönüne çevrilen güvenli sinyalleri."
durum: aktif
---
# Görsel Yön ve Referans Analizi

Bu görseller yalnız style reference'tır; resmî Better Payment asset'i değildir. Logo, özgün layout, illüstrasyon ve ayırt edici kompozisyonları kopyalanmaz.

## Asset envanteri

| Kaynak | Format / ölçü | Rol | Otorite |
|---|---|---|---|
| `codex-clipboard-69e60c63-...png` | PNG, 400×300 | style-reference | ilham, resmî değil |
| `codex-clipboard-c6d86f29-...png` | PNG, 1800×1350 | style-reference | ilham, resmî değil |
| `codex-clipboard-309ed16c-...png` | PNG, 473×628 | style-reference | ilham, resmî değil |
| `apps/web/public/logo.svg` | SVG, 1000×897 viewBox | mevcut logo baseline | repo içindeki mevcut resmî kullanım; geleceği henüz kilitli değil |

## Referans 1 — Restrained kinetic object

**Kullanılabilir sinyaller:**

- Bol beyaz alan ve düşük gürültü.
- Siyah tipografi ile tek kontrollü mavi ifade alanı.
- Hareket hissini çizgi sıklığı ve blur yerine yönlü form dönüşümüyle verme.
- Büyük medya yüzeyi ile kısa ürün anlatısını dengeleme.

**Kopyalanmayacaklar:** exact küre/silindir formu, aynı split layout ve aynı gradient şeridi.

## Referans 2 — Editorial technology split

**Kullanılabilir sinyaller:**

- Editorial ölçekte tipografi.
- Beyaz bilgi alanı ile doygun mavi teknik alan arasında yüksek kontrast.
- Teknik sistemi dekor değil, anlatının ikinci yarısı olarak kullanma.
- Kontrollü serif/sans gerilimi ihtimali.

**Kopyalanmayacaklar:** cloud observability başlığı, ASCII laptop görseli, aynı 50/50 kabuk ve karanlık dış çerçeve.

## Referans 3 — Immersive blue field

**Kullanılabilir sinyaller:**

- Hero içinde kapsayıcı bir mavi atmosfer.
- Ürünün farklı parçalarını merkez kompozisyon etrafında gösterme.
- Büyük, temiz tipografi ve sınırlı canlı accent kullanımı.
- Alt bölümlerde açık yüzeyler ve veri/proof blokları.

**Kopyalanmayacaklar:** bulut görseli, anlamsız floating-card dizisi, lime rengin otomatik vurgu olarak kullanılması ve template CTA düzeni.

## Sentezlenen görsel yön

**Ürün gerçeği:** Better Payment, farklı Türk ödeme sağlayıcılarını tek ve tip güvenli bir API altında birleştirir; callback doğrulaması ve güvenli handler davranışı sunar.

**Merkezi mekanizma:** kontrollü ödeme yönlendirme ağı. Better Payment merkez düğümdür; provider'lar bağımsız endpoint'lerdir. Gidiş/dönüş akışı, birleşik request/result sözleşmesini ve doğrulanmış callback'i anlatır.

**Duygu:** finansal güven + teknik netlik + çağdaş açık kaynak enerjisi.

**Başlangıç eksenleri:**

- restrained ↔ expressive: `55/100`, dengeli fakat hero'da kontrollü ifade.
- geometric ↔ organic: `35/100`, geometrik ağırlıklı; motion yumuşak olabilir.
- familiar ↔ experimental: `60/100`, kategori güvenini koruyan ölçülü yenilik.

## Renk davranışı

- Light canvas ana yüzey.
- Derin ink metin; saf siyah yerine maviye çok hafif yaklaşabilen nötr.
- Güven veren ana mavi; exact ton palette review'da seçilecek.
- Gerekirse tek sınırlı accent; lime veya mor otomatik varsayım değildir.
- Gradient yalnız akış/derinlik anlatıyorsa ve düz renk alternatifi yetersizse kullanılır.

## Tipografi davranışı

- Büyük başlıklar gerçek mesajı doğrudan taşır; üstlerinde açıklayıcı eyebrow bulunmaz.
- Body ve docs metni yüksek okunabilirlikte kalır.
- Serif, yalnız editorial vurgu gerçekten sistemi güçlendirirse display rolünde değerlendirilir.
- Kod alanı ürünün teknik gerçekliğini gösterir; dekoratif pseudo-code kullanılmaz.
- Türkçe karakter ve ilerideki locale kapsamı seçim kriteridir.

## Mevcut logo baseline bulguları

- SVG iki ana path, gri ve mavi gradient'ler ile çoklu siyah/beyaz stroke katmanları içeriyor.
- Kaynak renkleri mavi tarafta `#5A7CAB`, `#34579A`, `#23427F`; gri tarafta `#ECECEC`, `#D4D4D4`, `#A9A9A9`.
- Yaklaşık kare/dikey oran navbar, favicon ve provider-network merkez düğümünde kullanılabilir; ancak çoklu outline/gradient küçük boyutta ağırlık ve bulanıklık riski taşıyor.
- Karar kapısı: geometri korunacak mı, sadeleştirilecek mi, yoksa yeni bir sembol mü üretilecek? Kullanıcı seçmeden mevcut logo Brandkit state'te authoritative kilitlenmez.

## Yasak kalıplar

- Üst başlık/eyebrow etiketiyle başlayan her bölüm.
- Her şeyi yuvarlatılmış kart içine alma.
- Shield, sparkle, globe, anlamsız orbit ve rastgele network çizgileri.
- Aşırı glassmorphism, bloom, plastic sheen ve gradient blob.
- Sahte sosyal kanıt, lorem dashboard ve hayali metrikler.
- Referanslardaki ayırt edici görselleri yeniden üretme.
- AI ile üretilmiş metni veya yaklaşık logoyu final UI'a gömme.

## Hero için güvenli yorum

Provider bağlantıları rastgele dekor değil, durum taşıyan bir sistem olacaktır:

- request akışı merkezden seçili provider'a gider,
- callback/result provider'dan merkeze döner,
- aktif node açıklaması gerçek destek kapsamını gösterir,
- reduced-motion görünümünde aynı bilgi statik bağlarla korunur.

Bu yaklaşım referansların dinamik merkez kompozisyon hissini taşır fakat özgün ürün davranışına dayanır.
