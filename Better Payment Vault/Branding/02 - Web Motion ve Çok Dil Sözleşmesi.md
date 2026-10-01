---
tur: plan
alan: web-branding
guncelleme: 2026-10-01
ozet: "Branding PR'ında uygulanacak light web, motion ve çok dil mimarisinin sözleşmesi."
durum: taslak
---
# Web, Motion ve Çok Dil Sözleşmesi

## Web yüzeyi

- Next.js/Fumadocs yapısı korunur; ayrı bir site builder'a taşınmaz.
- Design token'ları `globals.css` ve ortak component primitive'leri üzerinden yönetilir.
- Light mode tek kanonik görünüm olur.
- Mevcut içeriğin doğru claim'leri korunur, bilgi mimarisi ve sunumu yenilenir.
- Provider logoları resmî kaynaklardan deterministik yerleştirilir; model tarafından yeniden çizilmez.

## Hero davranışı

- Better Payment markası merkezde.
- Dört provider için eşit ve erişilebilir node.
- SVG bağlantıları semantik gruplara ayrılır: request, provider action, verified result.
- Hover tek bilgi yolu değildir; keyboard focus ve dokunmatik davranış bulunur.
- Otomatik animasyon kısa ve sakin; devamlı dikkat isteyen loop kullanılmaz.

## Scroll ve motion ilkeleri

- Layout kilitlenmeden motion eklenmez.
- Reveal, flow ve state transition dışında dekoratif hareket kullanılmaz.
- Scroll pozisyonu içerik sırasını açıklamak için kullanılabilir fakat kullanıcı kontrolünü ele geçirmez.
- Motion token'ları süre, easing ve mesafe olarak merkezileştirilir.
- `prefers-reduced-motion: reduce` altında transform/loop kaldırılır, içerik ve bağlantılar görünür kalır.
- Mobilde GPU ve batarya maliyeti düşük tutulur.

## Çok dil sözleşmesi

- English varsayılan unprefixed rota, Türkçe `/tr`; mevcut URL sözleşmesi korunur.
- Locale listesi config'ten türetilir; ikili toggle yerine dil menüsü kullanılır.
- Yeni diller partial fallback ile English içeriği ve görünür fallback notunu kullanabilir.
- Türkçe her English içerik değişikliğinde eş zamanlı güncellenir.
- Layout uzun Alman/Rusça metinlere ve RTL yönüne hazırlanır.
- Kod blokları LTR kalır.
- Heading id'leri çeviriden bağımsız stabil tutulur.

## İçerik sözleşmesi

- Doğrudan değer önerisi; eyebrow ile tekrar yok.
- Teknik iddialar README capability tablosu veya testlerle doğrulanır.
- Provider'a özel özellikler birleşikmiş gibi sunulmaz.
- CTA'lar ölçülebilir ve az sayıda: docs, GitHub, npm, demo.
- Sosyal kanıt yalnız gerçek ve doğrulanabilir veriyle eklenir.

## Performans bütçesi

- Hero ana içeriği video indirmeden görünür.
- Kritik logo ve provider asset'leri SVG.
- Motion library eklenirse tree-shake ve client boundary incelenir.
- LCP görseli optimize edilir; font yükleme layout shift üretmez.
- Animasyon nedeniyle CLS/TBT regresyonu kabul edilmez.

## QA matrisi

| Alan | Zorunlu durumlar |
|---|---|
| viewport | desktop, tablet, mobile |
| locale | en, tr, partial fallback locale |
| motion | normal, reduced |
| input | mouse, keyboard, touch |
| content | kısa/uzun heading, code overflow, dört provider |
| metadata | title, description, OG, Twitter, canonical, hreflang |
| build | lint, typecheck, production build, translation check |

## Kapsam dışı

- Dark mode.
- Dashboard veya payment UI component ürünü (#53).
- Native mobile UI.
- 1.0 versioned docs (#70).
- AI videoyu homepage background'u yapmak.
