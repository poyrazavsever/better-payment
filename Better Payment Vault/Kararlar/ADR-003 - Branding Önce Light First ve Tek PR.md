---
tur: adr
alan: branding
guncelleme: 2026-10-01
ozet: "Better Payment branding yenilemesinin light-first, çok dilli, onay kapılı ve tek toplu PR olarak yürütülmesi kararı."
durum: kabul
---
# ADR-003: Branding Önce, Light-first ve Tek PR

## Bağlam

Proje sahibinden branding çalışması için onay alındı. Lansman ve duyuru öncesinde logo sistemi, görsel kimlik, web sitesi, çok dilli yapı ve motion davranışının birlikte ele alınması gerekiyor. Mevcut site işlevsel ve güncel olsa da marka ayrışması ve ürün kanıtı sınırlı.

## Karar

- Çalışma `branding` şemsiyesi altında tek bir upstream PR olarak hazırlanacak.
- PR tek parça görünse de commit'ler ve review kapıları fazlara ayrılacak; palet, logo ve tipografi kullanıcı tarafından ayrı ayrı onaylanmadan sonraki bağımlı faza geçilmeyecek.
- İlk sürüm yalnız light mode olacak. Dark mode tasarlanmayacak; mevcut tema anahtarı ilk branding kapsamından çıkarılacak veya light moda kilitlenecek.
- Türkçe ve İngilizce korunacak; çok dilli yapının ikiden fazla dili destekleyecek şekilde genelleştirilmesi branding programına dahil edilecek.
- Hero'nun merkezinde Better Payment markası, çevresinde iyzico, PayTR, Parampos ve Akbank düğümleri olacak. Bağlantılar gerçek ürün fikrini, yani tek tip API üzerinden ödeme yönlendirmeyi anlatacak.
- Hero animasyonu SVG/CSS/React tabanlı ve erişilebilir olacak. Önceden render edilmiş AI videosu veya anlamsız orbit efekti ana ürün arayüzü olarak kullanılmayacak.
- Higgsfield Brandkit; palet, logo sistemi, tipografi değerlendirmesi ve launch asset'leri için kullanılacak. Higgsfield Generate yalnız onaylanmış Brand Lock sonrasında sosyal görsel/video üretiminde kullanılacak.
- Final arayüz; kesin renk token'ları, gerçek fontlar, seçilmiş SVG logo ve kod tabanlı motion ile uygulanacak.
- Homepage üzerindeki eyebrow/üst başlık kalıbı kaldırılacak. Her bölümün küçük uppercase etikete sahip olması yasak tasarım kalıbı sayılacak.

## Anti-slop sınırları

- Rastgele gradient blob, parlak küre, sparkle, shield, anlamsız network/orbit ve cam efekti kullanılmaz.
- İşlevi olmayan yüzen kartlar ve sahte dashboard ekranları kullanılmaz.
- Doğrulanmamış müşteri logosu, download/star sayısı veya “trusted by” alanı oluşturulmaz.
- Her bölüm aynı kart, pill, eyebrow ve ikon kalıbıyla kurulmaz.
- AI tarafından üretilmiş yaklaşık logo veya pseudo-text final ürüne girmez.
- Motion içerikten rol çalmaz, scroll hijacking yapılmaz ve `prefers-reduced-motion` desteklenir.

## PR stratejisi

- Branch, açık PR'lar sonuçlandıktan ve `upstream/main` güncellendikten sonra `codex/branding-refresh` adıyla açılacak.
- Önerilen PR başlığı: `feat(web): refresh Better Payment branding and launch experience`.
- PR içinde foundation, design tokens, hero, homepage, i18n, motion, launch assets ve QA için ayrı commit'ler bulunacak.
- Onaylanmamış Brandkit taslakları, Higgsfield skill dosyaları ve yerel state PR'a eklenmeyecek.

## Sonuçlar

- Tek PR bütünsel bir deneyim sunar fakat review riski büyür; bu risk faz bazlı commit ve ekran görüntüsü kapılarıyla yönetilir.
- Light-only karar scope'u küçültür ve ilk lansmanda tutarlılığı artırır; dark mode ayrı bir takip işi olur.
- Palet değişirse üretilmiş logo ve palete bağlı çıktılar yeniden değerlendirilir. Tipografi değişikliği sembolü değil, lockup ve web tipografisini etkiler.
- Branding tamamlanmadan duyuru görselleri final sayılmaz.
