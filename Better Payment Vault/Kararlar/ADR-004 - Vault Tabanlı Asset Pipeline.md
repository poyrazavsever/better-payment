---
tur: adr
alan: asset
guncelleme: 2026-10-01
ozet: "Branding varlıklarının kaynak, onay, QA ve ürün kopyası ayrımı."
durum: kabul
---
# ADR-004: Vault Tabanlı Asset Pipeline

## Bağlam

Better Payment logosu, favicon ailesi, wordmark, web görselleri ve lansman varlıkları farklı makinelerde üretilecek. Taslakların doğrudan ürün koduna girmesi; kaynağın, prompt'un ve seçilme gerekçesinin kaybolması engellenmelidir.

## Karar

Branding varlıklarının kanonik üretim kaynağı `Better Payment Vault/Asset_Pipeline/` olur. Her varlık brief, provenance/prompt, aday, onaylı master ve QA kanıtı ile ilerler.

Bir varlık en fazla iki yerde bulunur:

1. vault içinde üretim kaynağı ve onaylı master
2. gerekli olduğunda ürün koduna kopyalanmış final export

`brandkit/state.json`, Higgsfield geçici işler ve review cache yerel kalır; upstream PR'a ve vault branch'ine girmez. Yalnız açıkça onaylanan logo masterları vault pipeline'a taşınır.

## Durum modeli

`0 · Envanterde` → `1 · Brief kilitli` → `2 · Aday üretildi` → `3 · Seçim onaylandı` → `4 · Master temiz` → `5 · Aile doğrulandı` → `6 · Koda bağlı` → `7 · Hedefte doğrulandı`.

## Sonuçlar

- Üretim tekrarlanabilir ve denetlenebilir olur.
- Reddedilen adaylar karar geçmişi olarak arşivlenir, aktif master sayılmaz.
- Favicon, monochrome ve wordmark yalnız seçilen sembol geometrisinden deterministik türetilir.
- Branding PR'ına sadece onaylı ürün exportları girer; vault ve yerel üretim araçları girmez.

## Doğrulama

- `node .local-tools/vault.mjs assets`
- `node .local-tools/vault.mjs check`
- PR öncesi `node .local-tools/vault.mjs pr-safety`
