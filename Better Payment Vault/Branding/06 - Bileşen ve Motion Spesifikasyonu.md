---
tur: marka-sistemi
alan: web-branding
guncelleme: 2026-10-01
ozet: "Faz 3 kodunun tek kaynağı: onaylı bileşenler, durumlar, hareketler ve token'lar."
durum: aktif
---
# Bileşen ve Motion Spesifikasyonu

Plan: [[Branding/00 - Branding Ana Planı]] (Faz 4.5) · Brand Lock: [[Branding/05 - Brand Lock]] · Logo: [[Branding/04 - Logo Sistemi Taslağı]].

Prototipler `Asset_Pipeline/Web/Bilesen/` altında; ürün repo'suna girmez. Faz 3 bu nottaki kararları birebir koda aktarır.

## Hero (K8) — fixed

- Artwork: **A3 · Alt bant** (kullanıcı kararı 2026-10-01). Kaynak `Asset_Pipeline/Web/Hero/hero-A3-master.jpg`, prompt `hero-A3.prompt.txt`.
- Üst üçte iki tamamen içerik alanı: başlık, açıklama, butonlar, kurulum komutu. Şeritler alt bantta.
- Yazı, butonlar ve sağlayıcı ağı kodla çizilir; artwork yalnız zemin. Web için AVIF/WebP, LCP metne bağlı kalır.

## Butonlar (K7a) — fixed

Kullanıcı kararı 2026-10-01.

| Tür | Durağan | Hover / focus |
|---|---|---|
| Primary ve primary CTA | **Sürekli ışıltı**: çapraz ışık şeridi 4.5 sn arayla kendiliğinden geçer | parıltı hemen geçer + ikon hareketi + gölge derinleşir |
| Diğer tüm butonlar (secondary, ghost, koyu zemin) | sabit | **parıltı** (bir kez, 0.75 sn) + **ikon hareketi** |

- İkon: ok yerine **chevron**. Chevron hover'da 3–4 px sağa kayar. Marka/servis ikonları (GitHub vb.) hafifçe döner ve büyür (−8°, 1.08).
- İkon hareketi yaylı easing ile (`cubic-bezier(.34,1.56,.64,1)`, 0.35 sn).
- Parıltı: `linear-gradient(105deg, …)` şeridi; primary'de beyaz %55, secondary'de indigo %14, koyu zeminde beyaz %22.
- Boyutlar: sm 36 px, md 46 px, lg 54 px; radius 10 / 12 / 14 px.
- Focus: 2 px indigo halka, 3 px offset; parıltı klavye odağında da çalışır.
- `prefers-reduced-motion: reduce`: parıltı ve ikon hareketi kapanır, renk değişimi kalır.
- Elenen yorumlar: *Zıpla ve düş*, *Yuvarla* ("fena değil ama içime sinmedi").
- Prototip: `Bilesen/hero-buton-prototip-v2.html`.

## Bileşen seti (K7b)

Durum: **onaylandı** (2026-10-01). Kullanıcı: "bileşen setini detaylı inceledim, gayet hoşuma gitti"; animasyonlu ikonlar onaylı. Son düzeltme: kopyala butonunda "Kopyala" ve "Kopyalandı" birlikte görünüyordu (satır içi stil CSS'i eziyordu), giderildi. Prototip `Asset_Pipeline/Web/Bilesen/bilesen-seti-v1.html`, üretici `build_specimen.py`.

| Bileşen | Önerilen karar |
|---|---|
| Navbar | yapışkan, `rgba(248,248,252,.72)` + 14 px blur; logo lockup, 4 link, sürüm rozeti, GitHub (secondary sm) + Başla (primary sm) |
| Mobil menü | sağ üst ikon butonu; tam ekran sayfa, büyük dokunma alanlı linkler + iki ana aksiyon; açılış 0.3 sn fade + 8 px kayma |
| Link | indigo, alt çizgi hover'da soldan 0.3 sn çizilir; "daha fazla" linkinde chevron 3 px kayar |
| İkon butonu | 36 px kare, kenarlıklı, hover lila zemin |
| Kod bloğu | dosya adı başlığı, kopyala butonu (onayda yeşil "Kopyalandı", 1.6 sn); sözdizimi: anahtar kelime indigo, string yeşil, fonksiyon mor `#6A3FD8`, yorum soluk italik |
| Paket yöneticisi sekmeleri | npm / pnpm / yarn / bun; seçim göstergesi yaylı kayar |
| Özellik kartı | **zeminsiz** cam ikon 96 px (kullanıcı geri bildirimi: ikon arkasında renk olmasın); **animasyonlu ikon** (tüm set, kullanıcı kararı): Higgsfield video döngüsü + `mix-blend-mode: multiply` ([[Asset_Pipeline/Web/Animasyon/README]]); hover'da kart 3 px yükselir, ikon döner ve büyür |
| Durum kartı | dört gerçek durum; `pending` noktası nabız atar |
| Rozetler | Yeni (marka), sürüm (mono), Added in, Edge uyumlu, Deneysel |
| Sağlayıcı düğümü | repo'daki resmi logolar; seçili düğüm indigo kenar + lila halka; yetenek rozetleri; doğrulama durumu metinle |
| Callout | bilgi indigo, uyarı amber, tehlike kırmızı, başarı yeşil |
| Docs | kenar menüde küçük cam kategori ikonları, aktif sayfa lila; satır içi kod lila zemin; tablo + durum rozetleri |
| Bölüm başlığı | eyebrow yok; Manrope 800, 34 px |
| CTA bandı | indigo zemin, ters (beyaz) primary sürekli ışıltılı, cam obje dekoru sağda; mobilde (≤ 900 px) dekor %18 opaklık ve köşeye kayar, yazı ve butonlarla çakışmaz (kullanıcı geri bildirimi) |
| Footer | lockup + açıklama, üç sütun, alt satırda telif ve dil |

Radius: 10 / 12 / 16 / 20 px. Gölge: kartlarda yalnız hover'da yumuşak derin gölge.

## Motion (K7c)

Durum: **onaylandı** (2026-10-02). Kullanıcı: "mükemmel olmuş"; tek istek tempoyu daha ağır ve yumuşak yapmaktı ("ne kadar ağır olursa o kadar profesyonel"), aşağıdaki değerler bu ayarlamadan sonraki son hal. `Asset_Pipeline/Web/Motion/motion-prototip-v1.html`, üretici `build_motion.py`.

### Token'lar

| Token | Değer | Kullanım |
|---|---|---|
| `--d-xs` / `--d-sm` | 140 / 240 ms | renk, kenarlık, tooltip |
| `--d-md` | 450 ms | çip, navbar çizgisi, düğüm vurgusu |
| `--d-lg` | 700 ms | metin girişi, bölüm reveal |
| `--d-xl` | 900 ms | buton parıltısı |
| `--d-art` | 1600 ms | hero artwork girişi |
| `--e-std` | `cubic-bezier(.16,1,.3,1)` (ease-out-expo) | varsayılan |
| `--e-spring` | `cubic-bezier(.34,1.56,.64,1)` | ikon, kart, çip |
| `--e-exit` | `cubic-bezier(.4,0,1,1)` | çıkışlar |
| `--rise` | 18 px | giriş mesafesi |

### Hero açılışı

Artwork 1.6 sn içinde 24 px aşağıdan ve hafif ölçekten gelir. Başlığın iki satırı 300 / 440 ms, açıklama 600, butonlar 760, kurulum komutu 900, ağ 1000 ms gecikmeyle 18 px aşağıdan, 700 ms'de belirir. Prototipte "Açılışı tekrar oynat".

Uygulama notu: açılış CSS ile başlar, JavaScript'e bağlanmaz. Prototipte sınıf `requestAnimationFrame` ile ekleniyordu; arka planda açılan sekmede kare çizilmediği için içerik görünmez kalabiliyor. Kodda içerik varsayılan olarak görünür, animasyon yalnız ilerletici iyileştirmedir.

### Sağlayıcı ağı

- Kodla çizilir (SVG + HTML). Merkezde indigo `betterPayment()` düğümü (beyaz sembol), köşelerde dört sağlayıcı; bağlantılar kesikli lila.
- Döngü: istek noktası (indigo) merkezden sağlayıcıya 1.3 sn; düğüm 0.6 sn vurgulanır; doğrulanmış dönüş noktası (yeşil) 1.3 sn'de geri gelir; çip "istek → X" → "✓ doğrulandı · success · X"; sonraki sağlayıcıya 2.2 sn ara. Sıra iyzico → PayTR → Parampos → Akbank, sağlayıcı başına yaklaşık 5.4 sn. İlk akış açılıştan 1.9 sn sonra başlar.
- Etkileşim: üzerine gelme / odak → yetenek balonu; tıklama → o sağlayıcının akışı hemen başlar.
- Mobil: hero içeriğin altında ağ, altında 210 px şerit bandı; düğümler küçülür.

### Diğer

- Bölüm reveal: görünür olunca bir kez, 22 px, 700 ms, kademe 110 ms.
- Navbar: kaydırınca alt çizgi belirir (450 ms).
- `prefers-reduced-motion: reduce`: giriş ve reveal kapalı, her şey son halinde; akış noktaları gizli, çip statik "tek API · 4 sağlayıcı"; buton parıltısı kapalı; ikon videoları poster karesinde.

### Doğrulama

Gerçek tarayıcıda ölçüldü: akış sırası ve zamanlaması, art arda tıklamada tek akış, hareketi azalt modunda nokta kalmaması, mod kapanınca devam, 10/10 bölüm reveal, konsol hatası yok, 375 px'de taşma yok.
