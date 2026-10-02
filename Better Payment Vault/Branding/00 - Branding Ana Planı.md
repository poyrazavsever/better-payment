---
tur: plan
alan: branding
guncelleme: 2026-10-01
ozet: "Better Payment branding yenilemesinin faz bazlı ana planı: önce palet ve tipografi, sonra logo, sonra web/docs ve lansman."
durum: aktif
---
# Better Payment Branding Ana Planı

Kanonik kararlar: [[Kararlar/ADR-003 - Branding Önce Light First ve Tek PR]] · [[Kararlar/ADR-005 - Sahip Olunan Görsel Evren]].

## Hedef

Better Payment'ı “bir başka geliştirici landing page'i” görünümünden çıkarıp sade, şık, fresh ve güvenilir; teknik olarak net, Türkiye ödeme ekosistemine özgü ve lansmana hazır bir marka deneyimine dönüştürmek. Web sitesi, dokümantasyon, ikonlar ve lansman görselleri aynı markaya ait görünmeli.

## Değişmez yön

- Light mode önce; dark mode ayrı bir takip işi.
- Beyaz/açık yüzeyler ve güven veren mavi tonları.
- Güçlü tipografi, daha az dekoratif UI kalıbı; eyebrow yok.
- Merkezi Better Payment markası ile provider'lar arasında anlamlı bağlantı sistemi.
- Hero artwork + ikon/obje seti + gerçek durum kartları ile bütüncül görsel evren (ADR-005); maskot yok.
- Aynı dil docs'a da uygulanır.
- İnce, amaçlı motion; reduced-motion desteği.
- AI slop yok: her görsel kararın ürün gerçeğine dayanması gerekir.

## Sıra kararı (2026-10-01)

Kullanıcı kararı: **önce palet ve tipografi, sonra logo.**

- Brandkit'te tipografi bağımsız bir slottur; logo ise onaylı palet revizyonuna bağlıdır. Bu yüzden `palet → tipografi → logo` sırası güvenlidir.
- Tipografi önceden kilitlendiği için logo seçilir seçilmez wordmark ve lockup aynı fazda tamamlanır.
- Palet değişirse üretilen logo geçersiz olur; tipografi değişirse sembol etkilenmez, yalnız lockup yeniden yapılır.

## Faz özeti

| Faz | Kapsam | Higgsfield kredisi | Bağımlılık | Onay kapısı |
|---|---|---|---|---|
| 0 | Kurulum, referanslar, vault | yok | — | tamamlandı |
| 1 | Brand Lock taslağı + palet + tipografi | yok (yerel HTML önizleme) | Faz 0 | tamamlandı: K1 Better Payment, K2 İndigo Sinyal, K3 Manrope + Inter + JetBrains Mono |
| 2 | Logo: sembol, favicon ailesi, wordmark, lockup | var (Recraft ×3) | K2, K3 | tamamlandı: K4 yeniden tasarım, K5 Birleşen yollar, K6 Manrope lockup |
| 4 | Görsel evren: hero artwork + ikon seti | var | Faz 1–2 | K8 hero A3 · Alt bant onaylı, K9 15 ikon + animasyonlar onaylı |
| **4.5** | **Bileşen ve motion tasarımı (koddan önce)** | yok | Faz 1, 2, 4 | tamamlandı: K7a, K7b, K7c onaylı (2026-10-02) |
| 3 | Light design system (kod) | yok | Faz 4.5 | tamamlandı (2026-10-02): `codex/branding-refresh` üzerinde `c7afbe2`, `025e601` |
| 5 | Hero ve homepage | yok | Faz 3–4 | uygulandı (2026-10-02): `7a23a49`, `fcd1dc8`; revize 1: `4b62992`, `e14a73b`; K11 kullanıcı incelemesi bekliyor |
| 6 | Docs teması | yok | Faz 3–4 | uygulandı (2026-10-02): `6064942`; K12 kullanıcıyla birlikte incelenecek |
| 7 | Çok dilli mimari (#111) | yok | Faz 5–6 | K13 locale davranışı |
| 8 | Motion polish | yok | Faz 5–7 | K14 motion davranışı |
| 9 | Lansman görselleri ve metadata | var | Faz 2, 4 | K15 launch kit |
| 10 | QA, tek branding PR, temizlik | yok | hepsi | PR review |

Sıra değişikliği (2026-10-01, kullanıcı kararı): koda geçmeden önce bileşenler ve animasyonlar tasarlanır. Faz 4.5, Faz 3'ten önce gelir; Faz 3 yalnız onaylı spesifikasyonu koda aktarır.

## Faz 3 — Uygulama kaydı (2026-10-02)

Kullanıcı kararıyla PR #121/#122 beklenmeden `upstream/main` (`e5af998`) üzerinden `codex/branding-refresh` açıldı; PR'lar merge edildikçe rebase edilecek. #121 docs içerikleri, `Since.tsx` ve `mdx-components.tsx`'e dokunuyor; çakışma riski düşük.

1. `c7afbe2 brand: add Better Payment logo, favicon and app icons`: `public/brand/` (lockup ve sembol, renkli ve beyaz; 192/512 PNG), `app/icon.svg`, `favicon.ico`, `apple-icon.png`; navbar, footer ve docs başlığında lockup; eski `public/logo.svg` silindi.
2. `025e601 refactor(web): light-only brand design system`: `globals.css` İndigo Sinyal token'ları (light only, `.dark` kaldırıldı), Fumadocs aynı değişkenleri kullanır; Manrope / Inter / JetBrains Mono (`next/font`, latin + latin-ext); `RootProvider` light'a kilitli, navbar tema düğmesi ve docs tema anahtarı kaldırıldı, kullanılmayan `ThemeProvider` silindi; motion token'ları; `.btn-fx` (hover parıltısı) ve `.btn-fx-idle` (primary sürekli ışıltı), `data-icon="chevron|brand"` ikon hareketi; oklar chevron; callout'lar marka semantik renkleri.

Doğrulama: `tsc` temiz; değişen dosyalarda lint temiz (yalnız önceden var olan `CodeBlock.tsx` uyarısı); production build 62/62 sayfa; dev sunucusunda fontlar, renkler, light kilidi, primary sürekli ışıltı ve ikon etiketleri ölçüldü; konsol hatası yok.

Notlar:
- Önceden var olan sorun: build sonrası `pnpm lint`, üretilen `.source/` dosyalarında 6 hata veriyor (eslint ignore listesinde değil). Branding kapsamı dışında; ayrı küçük PR adayı.
- Kiril (`cyrillic`) font alt kümesi #111/#113 ile eklenecek.
- Hero butonları şimdilik 44 px (hero'nun kendi sınıfı); Faz 5'te 46 px'e çekilir.

## Faz 5 — Uygulama kaydı (2026-10-02)

1. `7a23a49 feat(web): new hero with provider network and animated feature icons`: A3 artwork (`public/brand/hero/hero-a3.jpg`, 83 KB); `ProviderNetwork` (istek → doğrulanmış dönüş, yetenek balonu, tıklayınca o sağlayıcı, reduced-motion, ekran dışında duraklama); akış zamanlayıcıyla ilerler, animasyon kareleri yalnız noktayı çizer (kare atlanırsa sıra bozulmaz); açılış CSS ile (`.bp-enter`, `.bp-art`); kaydırma reveal'ı scroll-driven CSS (`.bp-reveal`, desteklenmeyen tarayıcıda içerik direkt görünür); özellik kartlarında `AnimatedIcon` (8 ikon, WebM/MP4 + WebP poster, multiply); navbar GitHub + Başlayın, masaüstü menü 1024 px'ten itibaren; hero rozet ve istatistikleri kaldırıldı.
2. `fcd1dc8 feat(web): restyle homepage sections to the brand system`: ortak `SectionHeading`; tüm eyebrow ve uppercase mikro etiketler kaldırıldı; kod blokları marka sözdizimi renkleri + iki dilli Kopyala/Kopyalandı; CTA indigo bant, beyaz sürekli ışıltılı buton, cam dekor (< 1024 px'de %20 opaklık, köşede); düz metin ve metadata'da "Better Payment".

Doğrulama: tsc ve lint temiz (yalnız önceden var olan uyarı); production build 62/62; tarayıcıda akış zamanlaması ölçüldü (1.9 sn'de istek, 3.2 sn sonra doğrulandı, 2.2 sn ara); 8 ikon videosu oynuyor ve multiply uygulanıyor; 375 px mobil hero ve ağ kontrol edildi; `#features` bağlantısı doğru konumda.

Bilinen: dev sunucusu açıkken `next build` çalıştırmak aynı `.next` klasörünü kullandığı için dev HMR'ını bozar; derlemeden önce dev durdurulur.

Kalan (Faz 5): tam ekran mobil menü (spesifikasyon), sağlayıcı sekme logolarının büyütülmesi, docs teması (Faz 6).

## Faz 5 — Revize 1 (2026-10-02, kullanıcı geri bildirimi)

- Hero akışı toplu: istekler dört sağlayıcıya aynı anda, dönüşler aynı anda ("tek tek çok yavaş, takip edilemiyor"). Çip mobilde düğümlerin arkasında kalıyordu; z-index ve konum düzeltildi.
- "Node.js ve edge ortamlarında çalışır" şeridi kaldırıldı.
- "API'si bambaşka" ve sağlayıcı sekmeleri tek bölüm (`Integrations` + `CompareSlider`): dört sağlayıcı sekmesi, yetenek kartı, tek kod kutusunda sürüklenebilir ayırıcı (sol: sağlayıcının ham API'si, sağ: Better Payment; iki taraf da satır başından okunur; klavye ve dokunma destekli).
- Özellik kartları 8 → 5 ("çok fazla box"): TypeScript, iyzico ekstraları ve "birden çok sağlayıcı" çıkarıldı.
- Banka bölümü: Akbank kartı + eşit yükseklikte 4 özellik; yol haritası kesikli dalga üzerinde Garanti BBVA, Yapı Kredi, İş Bankası, Ziraat (logolar %80 gri, hover'da renk; mobilde dikey). Logo kaynakları `apps/web/public/brand/banks/SOURCES.md`; Yapı Kredi SVG'si Wikipedia'da non-free (fair use), diğerleri public domain.
- Navbar bağlantıları `#` olmadan kaydırır (başka sayfadan gelince `sessionStorage` ile).
- Konsol hatası ("Encountered a script tag"): `next-themes` inline script'i, tr/en geçişinde `[lang]` layout'u istemcide yeniden render edilince React uyarıyordu. Site light-only olduğu için `RootProvider theme={{ enabled: false }}`; doğrulandı (tr → en → tr, 0 hata).
- Navbar sürüm rozeti 1280 px altında gizli (bağlantılarla çakışıyordu).

## Faz 6 — Docs teması: kullanıcı notları (2026-10-02)

- Kenar menü grupları (Get Started, Concepts, Payments, Providers...) açılıp kapanabilir, varsayılan olarak açık.
- Grup ikonları kendi cam ikon dilimizde tasarlanacak (şu anki lucide ikonları uymuyor).
- Alt sayfalara (Introduction, Installation, Quick Start...) küçük, kendi tasarımımız chevron-right ikonu.
- Onay işaretleri (ör. Introduction > Supported providers tablosu) paletimizden özel SVG.
- Uyarı kutuları (info, warning...) yeniden tasarlanacak: soldaki yarım çizgi, kesik ikon, sıkışık satırlar sorunlu.
- Kod kutuları homepage'deki gibi olacak: düzgün "Kopyalandı" durumu, marka sözdizimi renkleri.

## Faz 6 — Uygulama kaydı (2026-10-02)

`6064942 feat(docs): brand theme for the documentation` (branch fork'a push edildi):

- Kenar menü: separator yerine klasör grupları, `defaultOpen: true`, açılıp kapanır. Giriş sayfaları `content/docs/(get-started)/` klasör grubuna taşındı; Fumadocs parantezli klasörü slug'a katmadığı için URL'ler aynı (doğrulandı: /docs, /docs/installation, /docs/whats-new 200).
- Grup ikonları: `lib/source.ts` içinde `brandIconsPlugin` (Fumadocs iç `iconPlugin` ile aynı mantık), `public/brand/docs-icons/*.webp`. Eşleme: get-started→tek API, concepts→event, payments→taksit, providers→3D Secure, banks→handler, integrations→edge, plugins→plugin, guides→docs, reference→çok dil. İkon öğesine `key` verildi (React liste uyarısı).
- Alt sayfalar: CSS mask ile marka chevron'u; aktif sayfada Fumadocs'un ince çizgisi kaldırıldı.
- ✅ → `.bp-check` (source.config.ts rehype eklentisi, içerik dosyalarına dokunulmadı; giriş sayfasında 26 adet).
- Callout: `DocsCallout` (tam kenarlık, dolu ikon, rahat satır), Fumadocs `type` değerleriyle uyumlu (info, warn, warning, error, success, idea).
- Kod: marka Shiki teması (anahtar kelime indigo, string yeşil, fonksiyon mor, sayı amber, yorum soluk italik); `DocsCodeBlock` istemci sarmalayıcı + `DocsCopyButton` (Kopyala/Kopyalandı, iki dil); npm sekmeleri çalışıyor.
- Inline code: Lilac Tint zemin, indigo metin.
- Kullanılmayan `components/docs/Callout.tsx` ve `CodeBlock.tsx` silindi; lint uyarısı sıfır.

Bilinen: `scripts/check-translations.mjs` Windows'ta `URL.pathname` yüzünden çalışmıyor (önceden var olan; CI Linux'ta sorunsuz). Geçici yolla çalıştırıldı, tüm sayfalar iki dilde eşleşiyor. Docs içerik metinlerinde ürün adı hâlâ `better-payment`; içerik değişikliği #121 ile çakışma riski taşıdığı için ayrı karar.

## Faz 10 — PR hazırlığı (2026-10-02)

- `dac3edb fix(docs): tidy the sidebar footer and mobile drawer links`: dil butonu ortalı ve esnek, GitHub kare 36 px.
- Kontroller: lint, typecheck, test (438), translation check, production build (62/62) geçti. Diff yalnızca `apps/web` (104 dosya), kişisel dosya yok.
- Ekran görüntüleri (önce/sonra, ana sayfa, docs, mobil) ürün checkout'unda `brandkit/pr-screenshots/`, PR taslağı `brandkit/pr-draft.md` (ikisi de yerel, git exclude).
- Açık karar: CONTRIBUTING büyük değişiklik için önceden issue istiyor; takip issue'su ("Website launch readiness and visual refresh") açılıp PR `Closes #` ile bağlanacak. PR kullanıcı onayıyla açılacak.

## Faz 10 — PR ve merge (2026-10-02)

- Issue czaydev/better-payment#123 açıldı, PR czaydev/better-payment#124 açıldı ve czaydev tarafından merge edildi (07:38 UTC); canlı site yeni markayla yayında.
- PR sonrası iki commit merge'e girdi: `c6aa2c8` (hero 4K Topaz upscale + WebP q90, CSS scroll-timeline parallax, navbar ayırıcı ortalandı, butonlardan `bg-clip-padding` kaldırılarak primary butonlardaki açık halka giderildi) ve `b49c251` (bölümler ekrana girince hero hızında fade/rise, IntersectionObserver ile tek seferlik; reduced motion ve JS yokken içerik görünür).
- README için önce/sonra görselleri: ürün checkout'unda `brandkit/pr-screenshots/final/`.
- Sonraki: vault'taki üçüncü taraf referans görsellerini kaldırmak, `backup/before-trailer-cleanup` dalını silmek.

## Faz 4.5 — Bileşen ve motion tasarımı

Amaç: kod yazılmadan önce her bileşenin görünümü, durumları ve hareketi tıklanabilir HTML prototiplerle onaylanır. Prototipler vault'ta `Asset_Pipeline/Web/Bilesen/` altında tutulur, ürün repo'suna girmez.

### K7a — Buton ve hover (aktif)

- Ok yerine chevron ikonu (kullanıcı geri bildirimi).
- Hover: yazı ve ikon birlikte hareket eder. Prototipte üç yorum: *Zıpla ve düş* (yukarı çık, yukarıdan hızla düşüp hafif sekme, 0.62 sn), *Yuvarla* (yukarı kay, kopya aşağıdan yaylı gelir, 0.45 sn), *Sade* (yalnız ikon).
- Varyantlar: primary, secondary, koyu zemin; sm/md/lg; focus halkası; `prefers-reduced-motion`.
- Prototip: `Bilesen/hero-buton-prototip-v1.html`.
- v1 geri bildirimi (2026-10-01): hareket yorumları "fena değil ama içime sinmedi"; parıltı (shiny) efekti istendi.
- v2: `Bilesen/hero-buton-prototip-v2.html` — *Parıltı* (çapraz ışık şeridi hover başına bir kez, 0.75 sn, gölge derinleşir), *Parıltı + chevron*, *Sürekli ışıltı* (ana buton 4.5 sn arayla); v1 hareketleri karşılaştırma için duruyor.

### K7b — Bileşen specimen

Navbar (masaüstü + mobil menü), link, kod bloğu ve kopyala butonu, paket yöneticisi sekmeleri (npm/pnpm/yarn), özellik kartı (ikonlu), durum kartı, sağlayıcı düğümü, callout, docs kenar menüsü, tablo, rozet/pill, CTA bandı, footer.

### K7c — Motion spesifikasyonu

- Motion token'ları: süreler, easing (standart, çıkış, yaylı), mesafeler.
- Hero: ilk yükleme reveal'ı ve sağlayıcı ağında istek → doğrulanmış dönüş akışı; artwork ile katmanlama.
- Bölüm reveal, kart hover, link alt çizgisi, kopyala geri bildirimi.
- Her hareket için reduced-motion eşdeğeri.

**Çıkış kriteri:** K7a, K7b, K7c onaylı; tek bir 'Bileşen ve Motion Spesifikasyonu' notu Faz 3'ün kaynağıdır.

## Faz 0 — Kurulum ve referanslar

**Durum:** tamamlandı.

- Higgsfield CLI `1.1.26`, auth ve workspace iki makinede doğrulandı; sekiz skill kurulu.
- Yedi logo ve beş web referansı vault'ta: [[Asset_Pipeline/Logo/Referans/README]] · [[Asset_Pipeline/Web/Referans/README]].
- ADR-005 kabul edildi.

## Faz 1 — Brand Lock temeli: palet ve tipografi

**Çıktı:** onaylı palet + onaylı tipografi; Brandkit state ve vault'a yazılmış Brand Lock v0.

### 1A. Brand Lock taslağı (K1)

- Brandkit state bu makinede sıfırdan kurulur; vault'taki eksenler ve yasaklar kaydedilir.
- **İsim yazımı kararı:** site şu an `better-payment` (npm paket adı) kullanıyor; vault `Better Payment` diyor. Marka adı, wordmark yazımı ve paket adının nerede kullanılacağı kilitlenir.
- Ton: sade, şık, fresh, güvenilir, teknik.
- Yasaklar: [[Branding/01 - Görsel Yön ve Referans Analizi]] yasak kalıpları.

### 1B. Palet (K2)

- Üç light-first palet panosu; deterministik HTML, kredi harcamaz.
- Her pano: canvas, surface, ink, muted, border, primary mavi, sınırlı accent, success, warning, danger, info.
- Her pano aynı mini homepage hero'su, bir docs sayfası kesiti, kod bloğu ve durum kartları (`pending`, `success`, `failure`) üzerinde gösterilir.
- WCAG kontrast değerleri panoda yazılır.
- Mavi sabit yön; exact ton seçimle belirlenir. Mor/indigo komşuluğu (gate, Stripe, Clerk sinyali) bir seçenek olarak temsil edilir.

### 1C. Tipografi (K3)

- Seçilen palet üzerinde 2–3 gerçek font çifti: display, body ve kod için mono.
- Google Fonts veya açık lisanslı font; Next.js `next/font` ile self-host edilebilir olmalı.
- Zorunlu kapsam: Türkçe (`ğ ş ı İ ç ö ü`) ve latin-ext. #113 Rusça için Kiril kapsamı kontrol edilir; Arapça (#114) ayrı fallback font gerektirir, seçimi bloklamaz.
- Önizleme gerçek içerikle: hero başlığı TR/EN, docs paragrafı, tablo, kod bloğu.
- Mevcut Geist/Geist Mono baseline olarak bir seçenekte tutulabilir.

**Çıkış kriteri:** K1, K2 ve K3 onaylı; Brand Lock v0 vault'a yazıldı.

## Faz 2 — Logo sistemi

**Çıktı:** sembol, favicon ailesi, renk modları, wordmark ve yatay lockup.

1. **K4 logo yolu:** koru / sadeleştir / yeniden tasarla. Öneri: yeniden tasarla; mevcut çok katmanlı gradient logo referansların sinyaliyle (az parça, flat, favicon'da güçlü) uyuşmuyor.
2. Brief: [[Asset_Pipeline/Logo/Brief - Better Payment Logo v1]]; onaylı palet renkleriyle Recraft V4.1 vector, aynı parametrelerle tam üç aday.
3. **K5 sembol seçimi:** yedi referansla yan yana karışma kontrolü, 16/32 px testi.
4. Geometry fingerprint; color/black/reverse-white; favicon SVG/ICO/16/32/48; PWA 192/512.
5. **K6 lockup:** onaylı tipografiyle wordmark ve yatay lockup; clear space ve minimum boyut.

Bu fazın export adımı için `rsvg-convert` ve ImageMagick kullanıcı izniyle kurulur.

**Çıkış kriteri:** Brand Lock v1 (palet + tipografi + logo) tamam.

## Faz 3 — Light design system

Branch açılış koşulu: [PR #121](https://github.com/czaydev/better-payment/pull/121) ve [PR #122](https://github.com/czaydev/better-payment/pull/122) sonuçlanmış, `upstream/main` güncel. Branch: `codex/branding-refresh`.

- `globals.css` semantic token'ları; aynı token'lar Fumadocs değişkenlerine bağlanır.
- Tipografi rolleri: display, heading, body, code, label.
- Grid, spacing, radius, border, shadow kuralları.
- Button, link, navigation, code block, provider node, durum kartı, CTA.
- Tema toggle kaldırılır; HTML light'a kilitlenir.
- Onaylı logo ve favicon'lar `apps/web/public/brand/` ve `app/` altına bağlanır.
- **K7:** token ve component specimen sayfası.

## Faz 4 — Görsel evren (ADR-005)

- Hero artwork brief'i `Asset_Pipeline/Web/` altında; Brand Lock değerleri prompt'a birebir kopyalanır.
- Hero artwork: 2–3 aday, **K8**.
- İkon/obje seti: önce 3 parçalık stil testi, onaydan sonra 12–16 parçalık set tek turda, **K9**.
- Optimize AVIF/WebP export; 24/48/96 px okunurluk testi.

## Faz 5 — Hero ve homepage

- Kod tabanlı provider network hero; artwork zemin/çerçeve; gerçek SDK durum kartları. **K10**.
- Anlatı sırası:
  1. Net değer önerisi + provider network hero.
  2. Türkiye'de ödeme entegrasyonunun parçalanmışlığı.
  3. Tek API ve güvenlik modeli.
  4. Gerçek provider yetenek matrisi.
  5. Kod ile çalışan akışın yan yana kanıtı.
  6. #98 veya MockProvider demo girişi.
  7. Docs, GitHub ve npm CTA'ları.
  8. Katkı ve sandbox doğrulama çağrısı.
- TR/EN eksiksiz. **K11**.

## Faz 6 — Docs teması

- Fumadocs sayfaları aynı token, tipografi ve ikon setiyle.
- Docs ana sayfası ve kategori girişlerinde ikonlar; kod blokları ve callout'lar yeni sistemde.
- **K12:** docs ana sayfası, bir provider sayfası ve bir referans sayfası ekran görüntüleri.

## Faz 7 — Çok dilli mimari

- [#111](https://github.com/czaydev/better-payment/issues/111) kapsamı: locale config, dil menüsü, `Accept-Language`, fallback, RTL hazırlığı.
- Bu işe başlamadan #111 issue'su sahiplenilir; atanmamış durumda.
- TR/EN aynı bilgi mimarisinde; üçüncü locale yalnız config + dictionary + içerik ile eklenebilir. **K13**.

## Faz 8 — Motion polish

- Layout ve içerik kilitlendikten sonra: reveal, provider akışı, kod/sonuç geçişleri, CTA mikro etkileşimleri.
- Scroll hijacking yok; `prefers-reduced-motion` eşdeğeri; Core Web Vitals regresyonu yok. **K14**.

## Faz 9 — Lansman görselleri ve metadata

- OG/Twitter görselleri TR/EN, sosyal avatar ve cover, duyuru kartları, isteğe bağlı kısa video storyboard'u.
- Metin ve logo deterministik SVG/HTML katmanında.
- `SoftwareApplication`/`WebSite` structured data, Twitter metadata. **K15**.

## Faz 10 — QA, PR ve temizlik

- Web build, lint, typecheck; desktop/tablet/mobile; TR/EN/fallback; klavye, focus, reduced-motion; Lighthouse.
- Önce/sonra ekran görüntüleri ve faz bazlı commit listesi.
- PR: `feat(web): refresh Better Payment branding and launch experience`.
- Diff'te vault, `brandkit/`, skill dosyaları veya onaylanmamış taslak yok.
- **Temizlik:** branding PR merge edildikten sonra üçüncü taraf referans görselleri vault'tan kaldırılır (kullanıcı kararı, 2026-10-01); analiz notları korunur.

## Önerilen commit sırası

1. `brand: add approved identity assets and tokens`
2. `refactor(web): establish light design system`
3. `feat(web): add brand illustration and icon set`
4. `feat(web): build provider network hero`
5. `feat(web): redesign homepage narrative`
6. `feat(docs): apply brand system to documentation`
7. `feat(web): generalize locale architecture`
8. `feat(web): add accessible motion system`
9. `brand: add launch metadata and social assets`
10. `test(web): add branding visual and accessibility checks`

## Tahmini takvim

Takvim onay hızına bağlıdır; her kapı bir oturumda kapanırsa:

| Dönem | Fazlar |
|---|---|
| 1. hafta | Faz 1 (palet, tipografi) ve Faz 2 (logo ailesi) |
| 2. hafta | Faz 3 (design system) ve Faz 4 (görsel evren), paralel |
| 3. hafta | Faz 5 (hero, homepage) ve Faz 6 (docs) |
| 4. hafta | Faz 7–9 ve Faz 10 PR |

Bir kapı açıkken ona bağlı sonraki çıktı final kabul edilmez.
