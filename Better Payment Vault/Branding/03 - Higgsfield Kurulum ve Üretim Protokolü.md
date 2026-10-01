---
tur: rehber
alan: branding-tools
guncelleme: 2026-10-01
ozet: "Better Payment branding çalışmasında Higgsfield CLI, skill ve onay state'inin güvenli kullanım protokolü."
durum: aktif
---
# Higgsfield Kurulum ve Üretim Protokolü

## Kurulum durumu

- Higgsfield CLI kuruldu: `1.1.26`.
- Authentication tamamlandı.
- Workspace seçili ve hesap erişimi doğrulandı.
- `higgsfield-ai/skills` kaynağından sekiz skill kuruldu.

Kurulan skill'ler:

- `higgsfield-brandkit`
- `higgsfield-generate`
- `higgsfield-marketplace-cards`
- `higgsfield-product-photoshoot`
- `higgsfield-soul-id`
- `higgsfield-video-explainer`
- `higgsfield-websites`
- `higgsfield-youtube-thumbnail`

## Makine bazlı durum

| Makine | CLI | Auth / workspace | Skill'ler | `brandkit/state.json` | Export araçları |
|---|---|---|---|---|---|
| İlk kurulum makinesi | `1.1.26` | doğrulandı | proje içi `.agents/skills/` | var (yerel) | eksik |
| Windows `D:\Yazılım` (2026-10-01) | `1.1.26` | doğrulandı, `Private` workspace | global `~/.agents/skills/` (sekiz skill) | yok; Brandkit ilk turunda yeniden oluşturulacak | `rsvg-convert` ve ImageMagick eksik |

Notlar:

- Bu makinede Python `python3` değil `python` komutuyla çalışır; Brandkit script'leri `python` ile çağrılır.
- Brandkit state yerel olduğu için makineler arasında taşınmaz. Onaylanan her slot (palet, logo, tipografi) bu vault'a da yazılır; böylece başka makinede state aynı kararlarla yeniden kurulabilir.
- Windows'ta ürün checkout'u `D:\Yazılım\better-payment`, vault clone'u `D:\Yazılım\better-payment-vault`. Ürün checkout'unda `brandkit/`, `.agents/skills/` ve `skills-lock.json` `.git/info/exclude` ile PR dışında tutulur.

## Bu proje için aktif kapsam

- **Brandkit:** palet, logo, tipografi, Brand Lock ve launch görsel sistemi.
- **Generate:** onaylanmış marka ile sosyal görsel ve kısa launch video üretimi.
- Web sitesi implementasyonu mevcut Next.js repo içinde yapılır; Higgsfield Websites ile ayrı site üretilmez.
- Marketplace, Soul ID, product photoshoot, explainer ve YouTube thumbnail skill'leri talep gelmeden kullanılmaz.

## Yerel ve PR dışı dosyalar

- `.agents/skills/`
- `skills-lock.json`
- `brandkit/state.json`
- Brandkit taslakları ve ham job çıktıları

Bu dosyalar `.better-payment-local-ignore` ile ürün PR'larından ayrılır. Yalnız açıkça onaylanmış final SVG/PNG/video ve uygulama kodu branding PR'a alınabilir.

## Onay state'i

Brandkit state elle düzenlenmez. Şu slotlar bağımsızdır:

- palette
- logo
- typography
- downstream launch asset'leri

Palet, logo veya tipografi başarılı üretimle kendiliğinden onaylanmış sayılmaz. Her slot için açık kullanıcı seçimi gerekir.

## Üretim sırası

1. Her Brandkit turunda state status oku.
2. Resmî asset ve ilham referanslarını ayır.
3. Brand Lock oluştur.
4. Üç palette board göster ve bekle.
5. Logo yolu redesign ise üç Recraft SVG göster ve bekle.
6. İki/üç typography board göster ve bekle.
7. Essential Kit kilitlendikten sonra web ve launch uygulamalarına geç.
8. Her final asset'i exact logo, renk ve copy ile QA et.

## Model sınırları

- Yeni vector logo yalnız Recraft V4.1 vector.
- Genel launch görseli için varsayılan yüksek kaliteli image modeli, canlı model contract'ı doğrulandıktan sonra seçilir.
- Video için Seedance 2.5 ancak logo/palet/type kilitlendikten ve storyboard onaylandıktan sonra kullanılır.
- Exact metin ve logo image modeline bırakılmaz; SVG/HTML ile deterministik uygulanır.

## Güvenlik ve maliyet

- Token, credential ve hesap bilgisi vault'a yazılmaz.
- Ücretli generation öncesi live model contract kontrol edilir.
- Spekülatif ekstra asset üretilmez; her generation'ın belirli bir downstream amacı olur.
- Aynı başarısız üretim en fazla bir kez düzeltilerek tekrarlanır.
- Hiçbir çıktı otomatik olarak siteye, GitHub'a veya sosyal kanala yayınlanmaz.

## Eksik yerel araçlar

SVG export/Brandbook aşamasında `rsvg-convert` ve ImageMagick gerekebilir. Mevcut planlama/state aşaması bunlara ihtiyaç duymuyor. Bu araçlar yalnız ilgili export fazına gelindiğinde kullanıcı izniyle kurulacak.
