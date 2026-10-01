---
tur: plan
alan: branding
guncelleme: 2026-10-01
ozet: "Better Payment görsel kimlik, web, motion, çok dil ve lansman yenilemesinin faz bazlı ana planı."
durum: aktif
---
# Better Payment Branding Ana Planı

Kanonik karar: [[Kararlar/ADR-003 - Branding Önce Light First ve Tek PR]].

## Hedef

Better Payment'ı “bir başka geliştirici landing page'i” görünümünden çıkarıp güvenilir, teknik olarak net, Türkiye ödeme ekosistemine özgü ve lansmana hazır bir marka deneyimine dönüştürmek.

## Değişmez yön

- Light mode önce.
- Beyaz/açık yüzeyler ve güven veren mavi tonları.
- Güçlü tipografi, daha az dekoratif UI kalıbı.
- Merkezi Better Payment markası ile provider'lar arasında anlamlı bağlantı sistemi.
- Çok dil mimarisi branding ile birlikte.
- İnce, amaçlı scroll/motion; reduced-motion desteği.
- AI slop yok: her görsel kararın ürün gerçeğine dayanması gerekir.

## Faz 0 — Kurulum ve koruma sınırı

**Durum:** tamamlandı.

- Higgsfield CLI `1.1.26` kuruldu ve hesap/workspace doğrulandı.
- Sekiz companion skill kuruldu.
- Aktif üretim araçları `higgsfield-brandkit` ve gerektiğinde `higgsfield-generate` olarak sınırlandı.
- Brandkit onay state'i yerel `brandkit/state.json` altında oluşturuldu.
- Skill dosyaları, lock dosyası ve Brandkit state'i ürün PR'larından yerel ignore ile ayrıldı.
- Başlangıç görsel eksenleri kaydedildi: dengeli/hafif expressive, geometrik ağırlıklı, kontrollü experimental.

**Çıkış kriteri:** CLI authenticated, local state hazır, ürün branch'i temiz.

## Faz 1 — Brand Lock ve temel kimlik

### 1A. Mevcut logonun kaderi

Mevcut `apps/web/public/logo.svg` baseline olarak ölçülecek. Üç seçenekten biri açıkça seçilecek:

1. koru ve yalnız kullanım sistemini güçlendir,
2. aynı merkezi fikri sadeleştirerek refine et,
3. yeni bir sembol sistemi oluştur.

Bu seçim yapılmadan logo authoritative olarak kilitlenmez.

### 1B. Palet

- Üç anlamlı light-first palet panosu hazırlanacak.
- Her pano exact hex, semantic rol, kontrast davranışı ve destekleyebileceği logo mekanizmalarını içerecek.
- Mavi tercih sabit yönlendirmedir fakat exact palet değildir.
- Kullanıcı seçimi Brandkit state'e kaydedilmeden logo aşamasına geçilmez.

### 1C. Logo

- Koruma/refine kararı seçilirse mevcut geometri deterministik biçimde ele alınır.
- Yeni logo kararı seçilirse Recraft V4.1 vector ile tam üç farklı SVG mekanizma üretilir.
- Referans görseller logo modeline kopyalama hedefi olarak verilmez.
- Seçim, küçük boyut testi ve geometri fingerprint'inden sonra kilitlenir.

### 1D. Tipografi

- Seçilmiş palet ve logo ile iki veya üç gerçek font çifti gösterilir.
- Türkçe ve planlanan dillerin karakter kapsamı doğrulanır.
- Display ve body rolleri en fazla iki aileyle çözülür.
- Tipografi kullanıcı onayıyla state'e kaydedilir.

**Çıkış kriteri:** palette + logo + typography onaylı; Brand Lock v1 hazır.

## Faz 2 — Light design system

- Semantic color token'ları: canvas, surface, ink, muted, border, primary, accent, success, warning, danger.
- Tipografi rolleri: display, heading, body, code, label; gereksiz uppercase/eyebrow kalıbı yok.
- Grid, spacing, radius, border ve shadow kuralları.
- Button, link, navigation, code block, provider node, stat/proof ve CTA bileşenleri.
- Light moda kilitli HTML ve CSS; tema toggle kaldırılır.
- WCAG kontrast kontrolü.

**Çıkış kriteri:** token'lar ve temel component specimen'ı onaylı.

## Faz 3 — Hero sistemi

- Merkezde Better Payment sembol/lockup.
- Çevrede iyzico, PayTR, Parampos ve Akbank sağlayıcı düğümleri.
- Bağlantılar dekoratif orbit değil; tek API'ye giriş, provider yönlendirme ve doğrulanmış callback dönüşünü anlatan akışlar.
- İlk yüklemede kontrollü reveal; pointer/focus ile provider detayları; scroll ile hafif derinlik.
- Mobilde düğümler okunur ve tek kolon/horizontal akışa dönüşür.
- `prefers-reduced-motion` durumunda statik ama eksiksiz kompozisyon.
- Hero copy'sinde eyebrow badge kullanılmaz.

**Çıkış kriteri:** desktop/mobile ve reduced-motion prototipi onaylı.

## Faz 4 — Homepage yeniden yapılandırma

Önerilen anlatı sırası:

1. Net değer önerisi + provider network hero.
2. Türkiye'de ödeme entegrasyonunun gerçek parçalanmışlığı.
3. Better Payment'ın tek API ve güvenlik modeli.
4. Provider kapsamı; gerçek yetenek matrisi.
5. Kod ile çalışan akışın yan yana kanıtı.
6. #98 veya daha küçük MockProvider demo girişi.
7. Dokümantasyon, GitHub ve npm CTA'ları.
8. Katkı ve sandbox doğrulama çağrısı.

Mevcut “her bölümde eyebrow + başlık + kart grid” ritmi kırılacak. Bölümler aynı görsel şablonun tekrarları olmayacak.

**Çıkış kriteri:** tüm homepage light modda, güncel claim'lerle ve iki dilde tamam.

## Faz 5 — Çok dilli mimari ve içerik

- #111 kapsamındaki locale config, language menu, `Accept-Language`, fallback ve RTL hazırlığı branding bileşenleriyle birlikte ele alınır.
- Türkçe ve İngilizce zorunlu, eksiksiz ve aynı bilgi mimarisine sahip olur.
- Yeni diller partial fallback ile eklenebilir.
- Motion ve layout dil uzunluğundan bozulmaz.
- Final copy, translation anahtarları ve metadata aynı PR'da güncellenir.

**Çıkış kriteri:** TR/EN tam; üçüncü locale ekleme yalnız config + dictionary + içerik gerektiriyor.

## Faz 6 — Motion ve scroll polish

- Motion ancak layout ve içerik kilitlendikten sonra eklenir.
- Scroll reveal, provider bağlantı akışı, code/result geçişleri ve CTA mikro etkileşimleri.
- Scroll hijacking, sürekli hareket ve decorative parallax yok.
- Motion token'ları tek yerden yönetilir.
- Core Web Vitals ve ana thread bütçesi korunur.

**Çıkış kriteri:** motion anlam taşıyor, reduced-motion eşdeğeri var, performans regresyonu yok.

## Faz 7 — Lansman görselleri ve video

Brand Lock onaylandıktan sonra Higgsfield ile:

- Open Graph ve sosyal paylaşım görselleri,
- launch announcement görsel serisi,
- kısa ürün tanıtım videosu veya motion storyboard,
- GitHub/NPM duyuru kartları

üretilir. Exact logo ve metin gerektiğinde deterministik SVG/HTML katmanıyla uygulanır. Üretilen hiçbir asset otomatik yayınlanmaz.

**Çıkış kriteri:** TR/EN launch kit, doğrulanmış copy ve platform ölçüleri hazır.

## Faz 8 — QA ve tek branding PR

- Web build, lint ve typecheck.
- Desktop/mobile; Chrome/Safari/Firefox makul kapsama.
- Light theme, TR/EN ve fallback kontrolleri.
- Klavye, focus, screen reader semantiği ve reduced-motion.
- Lighthouse/Core Web Vitals bütçesi.
- Sosyal preview ve metadata doğrulaması.
- Önce/sonra ekran görüntüleri ve faz bazlı commit listesi.

**Çıkış kriteri:** tek branding PR review'a hazır; onaylanmamış taslak veya yerel Higgsfield state'i diff'te yok.

## Önerilen commit sırası

1. `brand: add approved identity assets and tokens`
2. `refactor(web): establish light design system`
3. `feat(web): build provider network hero`
4. `feat(web): redesign homepage narrative`
5. `feat(web): generalize locale architecture`
6. `feat(web): add accessible motion system`
7. `brand: add launch metadata and social assets`
8. `test(web): add branding visual and accessibility checks`

## Onay kapıları

1. Logo yolu: preserve / refine / redesign.
2. Palet seçimi.
3. Logo seçimi veya mevcut logo varyant sistemi.
4. Tipografi seçimi.
5. Hero prototype.
6. Full homepage.
7. Motion davranışı.
8. Launch asset seti.

Bir kapı açıkken ona bağlı sonraki çıktı final kabul edilmez.
