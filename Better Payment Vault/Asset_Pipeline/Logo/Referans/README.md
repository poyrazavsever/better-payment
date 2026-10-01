---
tur: kaynak-envanteri
alan: logo
guncelleme: 2026-10-01
ozet: "Kullanıcının paylaştığı logo referanslarından güvenli biçim sinyalleri ve anti-copy sınırları."
durum: aktif
---
# Logo Referans Envanteri

Paylaşılan altı görsel yalnız `style-reference` rolündedir. Dosyaların kendisi üretim modeline verilmez ve üçüncü taraf marka işaretleri vault branch'ine kopyalanmaz.

| Referans | Kullanılabilir sinyal | Kopyalanmayacak öğe |
|---|---|---|
| Stripe lockup | cesur sans, sembol–wordmark optik dengesi, tek-renk güç | bölünmüş S benzeri özgün sembol ve Stripe wordmark |
| Clerk horizontal | iki tonlu kompakt sembol, küçük ölçekte merkez odağı | C biçimli halka ve kullanıcı silueti |
| Clerk app icon | kare içinde merkezlenmiş yüksek-kontrast mark | aynı halka/baş/gövde mekanizması |
| Purple gate icon | çok az parçalı negatif alan, favicon netliği | eğik beyaz panelin birebir oranı |
| Supabase mark | yön ve momentum, iki parçalı güçlü silhouette | karşılıklı lightning formu ve yeşil gradient |
| Better Auth lockup | siyah-beyaz teknik tavır, compact monogram + wordmark | piksel H formu ve spesifik lockup |

## Ortak taste signal

- minimal, basic ve modern
- ikon önce; wordmark'tan bağımsız kullanılabilir
- flat ve vektörel
- az parça, kalın kütle, temiz negatif alan
- favicon/app-icon ölçeğinde güçlü
- light arayüzde mavi/indigo ana vurgu

## Anti-copy kuralı

Referansların hiçbiri Higgsfield logo generation inputu olmaz. Promptlarda marka adları kullanılmaz; yalnız geometrik sadelik, dolu silhouette, kompakt oran ve küçük boyut okunabilirliği gibi genel nitelikler tarif edilir.
