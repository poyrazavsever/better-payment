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
| 3 | Light design system (kod) | yok | Faz 4.5 + PR #121/#122 | K7 token ve bileşenlerin koda birebir aktarımı |
| 5 | Hero ve homepage | yok | Faz 3–4 | K10 hero prototipi, K11 tam homepage |
| 6 | Docs teması | yok | Faz 3–4 | K12 docs ekranları |
| 7 | Çok dilli mimari (#111) | yok | Faz 5–6 | K13 locale davranışı |
| 8 | Motion polish | yok | Faz 5–7 | K14 motion davranışı |
| 9 | Lansman görselleri ve metadata | var | Faz 2, 4 | K15 launch kit |
| 10 | QA, tek branding PR, temizlik | yok | hepsi | PR review |

Sıra değişikliği (2026-10-01, kullanıcı kararı): koda geçmeden önce bileşenler ve animasyonlar tasarlanır. Faz 4.5, Faz 3'ten önce gelir; Faz 3 yalnız onaylı spesifikasyonu koda aktarır.

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
