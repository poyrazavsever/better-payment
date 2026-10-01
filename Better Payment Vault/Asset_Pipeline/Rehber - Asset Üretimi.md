---
tur: rehber
alan: asset
guncelleme: 2026-10-01
ozet: "Brief'ten aday, master, varyant, QA ve ürün bağlantısına ilerleyen asset hattı."
durum: aktif
---
# Rehber - Asset Üretimi

## Aşamalar

| # | `asset_asama` | Çıkış kanıtı |
|---:|---|---|
| 0 | `0 · Envanterde` | benzersiz key, owner, hedef ve tarih |
| 1 | `1 · Brief kilitli` | amaç, geometri, renk, yasaklar ve kabul ölçütleri |
| 2 | `2 · Aday üretildi` | editable source, araç/model, prompt ve job kimliği |
| 3 | `3 · Seçim onaylandı` | kullanıcının açık seçimi ve Brandkit state kaydı |
| 4 | `4 · Master temiz` | SVG geometry fingerprint, alpha, renk ve isim QA |
| 5 | `5 · Aile doğrulandı` | renkli/siyah/beyaz, lockup ve 16–128 px contact sheet |
| 6 | `6 · Koda bağlı` | yalnız onaylı final kopya ve kullanım referansı |
| 7 | `7 · Hedefte doğrulandı` | responsive web, favicon ve sosyal crop kanıtı |
| X | `X · Emekli` | kullanım sıfır, ürün kopyası kaldırılmış, kayıt korunmuş |

## Üretim turu

1. [[Asset_Pipeline/Şablon/Asset Brief]] ile brief'i kilitle.
2. Referansları `official` ve `inspiration` olarak ayır; inspiration görsellerini üretim inputu yapma.
3. Palet seçimini ayrı bir kapıda tamamla.
4. Higgsfield Recraft V4.1 vector mode ile aynı parametrelerde tam üç symbol-only aday üret.
5. Kullanıcı seçmeden adaylardan hiçbirini master veya favicon ilan etme.
6. Seçilen SVG'yi fingerprint ile kilitle; siyah/beyaz/renkli varyantları aynı geometri üzerinden türet.
7. 16/20/24/32/48/64/128 px testleri, light yüzey matrisi ve alpha QA yap.
8. Tipografi seçildikten sonra wordmark, yatay ve gerekirse stacked lockup üret.
9. Yalnız onaylanan final exportları ürün koduna bağla.

## Genel QA

- [ ] tek bakışta ayırt edilebilir birleşik silhouette
- [ ] 16 ve 32 px favicon boyutunda okunabilirlik
- [ ] gerçek alpha; gömülü kart zemini, fringe veya halo yok
- [ ] color, pure black ve reverse white aynı geometriyi koruyor
- [ ] başka bir ödeme/teknoloji markasının işaretini taklit etmiyor
- [ ] kredi kartı, para simgesi, check, shield, sparkle ve generic orbit klişelerine dayanmıyor
- [ ] editlenebilir SVG kaynak ve provenance mevcut
- [ ] wordmark metni görsele gömülü üretim modeliyle yazılmıyor
- [ ] ürün kodunda yalnız onaylı final kopya var

## Dosya adlandırma

- aday: `better-payment-symbol-candidate-01.svg`
- master: `better-payment-symbol-color.svg`
- monochrome: `better-payment-symbol-black.svg`, `better-payment-symbol-white.svg`
- favicon: `favicon-16.png`, `favicon-32.png`, `favicon.svg`, `favicon.ico`
- lockup: `better-payment-horizontal-color.svg`, `better-payment-wordmark-black.svg`

Kanonik karar: [[Kararlar/ADR-004 - Vault Tabanlı Asset Pipeline]].
