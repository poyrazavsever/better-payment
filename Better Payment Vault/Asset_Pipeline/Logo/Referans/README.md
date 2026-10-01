---
tur: kaynak-envanteri
alan: logo
guncelleme: 2026-10-01
ozet: "Kullanıcının paylaştığı yedi logo referansı, güvenli biçim sinyalleri ve anti-copy sınırları."
durum: aktif
---
# Logo Referans Envanteri

Bu klasördeki görseller yalnız `style-reference` rolündedir. Hiçbiri Better Payment'a ait değildir ve hiçbiri üretim modeline input olarak verilmez.

## Saklama kararı

2026-10-01'de kullanıcı, referansların bilgisayarlar arasında kaybolmaması için dosyaların vault'ta tutulmasını istedi. Önceki “üçüncü taraf marka işaretleri vault branch'ine kopyalanmaz” kuralı bu kararla güncellendi:

- Dosyalar yalnız kişisel moodboard kaydıdır; ürün koduna, upstream PR'a, Higgsfield upload'una veya yayınlanan bir asset'e girmez.
- `personal/vault` fork herkese açıksa bu dosyalar da herkese açık görünür. Yeni referans eklerken bu bilinçle, düşük çözünürlüklü ve yalnız gerekli görseller eklenir.

## Dosyalar

| Dosya | Referans | Kullanılabilir sinyal | Kopyalanmayacak öğe |
|---|---|---|---|
| `ref-01-gate-app-icon.png` | mor zemin üzerinde eğik beyaz panel | çok az parçalı negatif alan, favicon netliği, tek renk zemin + tek beyaz form | eğik panelin birebir oranı ve açısı |
| `ref-02-stripe-lockup.png` | Stripe lockup | cesur sans, sembol–wordmark optik dengesi, tek-renk güç | bölünmüş S benzeri sembol ve Stripe wordmark |
| `ref-03-clerk-app-icon.png` | Clerk app icon | daire içinde merkezlenmiş yüksek kontrast, iki ton mor | aynı halka/baş/gövde mekanizması |
| `ref-04-clerk-horizontal.png` | Clerk horizontal | iki tonlu kompakt sembol, küçük ölçekte merkez odağı | C biçimli halka ve kullanıcı silueti |
| `ref-05-better-auth-lockup.png` | Better Auth lockup | siyah-beyaz teknik tavır, compact monogram + geniş harf aralıklı wordmark | piksel H formu, uppercase wordmark ve sondaki nokta |
| `ref-06-better-auth-icon.png` | Better Auth icon | modüler blok geometrisi, piksel ızgarası, sıfır dekor | iki blok arasındaki spesifik kesişme |
| `ref-07-supabase-mark.png` | Supabase mark | yön ve momentum, iki parçalı güçlü silhouette | karşılıklı lightning formu ve yeşil gradient |

## Ortak taste signal

- minimal, basic ve modern
- ikon önce; wordmark'tan bağımsız kullanılabilir
- flat ve vektörel; en fazla iki ton
- az parça, kalın kütle, temiz negatif alan
- favicon/app-icon ölçeğinde güçlü
- light arayüzde mavi/indigo ana vurgu; gate, Stripe ve Clerk örneklerindeki doygun mavi-mor aile en güçlü sinyal

## Anti-copy kuralı

Referansların hiçbiri Higgsfield logo generation inputu olmaz. Promptlarda marka adları kullanılmaz; yalnız geometrik sadelik, dolu silhouette, kompakt oran ve küçük boyut okunabilirliği gibi genel nitelikler tarif edilir. Aday seçiminde her aday bu yedi referansla yan yana konur ve karışma riski kontrol edilir.

İlgili: [[Asset_Pipeline/Logo/Brief - Better Payment Logo v1]] · [[Asset_Pipeline/Web/Referans/README]]
