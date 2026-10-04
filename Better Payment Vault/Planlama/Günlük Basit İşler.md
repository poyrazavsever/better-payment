---
tur: plan
alan: planlama
guncelleme: 2026-10-04
ozet: "Günde bir tane kapatılabilecek, küçük ve hata riski düşük işlerin sıralı listesi."
durum: aktif
---
# Günlük Basit İşler

**Kural:** Günde bir iş, bir PR. Seçim ölçütü: küçük diff, mevcut bir kalıbı izliyor, para hesabı ya da imza mantığına dokunmuyor, resmi dış kaynak gerektirmiyor. Upstream `main` @ `3758bef` (2026-10-04) üzerinden değerlendirildi.

**Her işten önce:**
- Issue varsa altına "claim" yorumu yaz.
- Issue yoksa önce kısa bir issue aç; CONTRIBUTING her PR için bir issue istiyor.

## Sıra

| Gün | İş | Kapsam | Risk | Durum |
|---|---|---|---|---|
| 1 | [#84 localizedErrors: Arapça (ar)](https://github.com/czaydev/better-payment/issues/84) | `src/plugins/localized-errors/ar.ts` (15 mesaj, `en.ts` kopyası), `index.ts`'e bir satır, patch changeset. Ayrıca `tests/unit/plugins/localized-errors.test.ts:81`'deki `locales` listesine `'ar'` eklenir; `pnpm size`'da `dist/plugins` 5 kB bütçesi aşılırsa bütçe yükseltilir (script yorumu bunu öngörüyor) | Çok düşük. Yalnızca çeviri; bütün mesaj anahtarlarının varlığını test zaten kontrol ediyor | hazir |
| 2 | `tests/README.md` güncelleme | Klasör ağacı gerçeğe uydurulur: `e2e/` yok, `integration/providers/paytr.test.ts` yok, sandbox, helpers ve fixtures güncel. Ölü `test:e2e` script'i `package.json`'dan kaldırılır | Çok düşük. Yalnızca doküman ve bir script satırı | hazir (önce issue) |
| 3 | CI: adapter subpath smoke testi | `ci.yml` "Smoke test" adımına `next`, `express`, `hono`, `fastify` ve `elysia` için `require` ve `import` denemesi; "Check package contents"e adapter dosyaları. #128'deki `exports` hatasını gelecekte CI yakalar | Düşük. Yalnızca CI; davranış değişmiyor | hazir (önce issue) |
| 4 | Doküman: ürün adı, 1. parça | `get-started` ve `concepts` (en ve tr) prose'unda "better-payment" → "Better Payment". Kod, import ve paket adı (`better-payment`) **değişmez** | Düşük. Çeviri kontrolü kod bloklarını korur | hazir (önce issue, #123 devamı) |
| 5 | Doküman: ürün adı, 2. parça | `payments`, `providers`, `banks` | Düşük | bekliyor |
| 6 | Doküman: ürün adı, 3. parça | `integrations`, `plugins`, `guides`, `reference` | Düşük | bekliyor |
| 7 (isteğe bağlı) | [#96 React Router adapter](https://github.com/czaydev/better-payment/issues/96) | `next.ts` gibi ~25 satırlık bir web `Request`/`Response` adapter'ı ve yeni subpath adımları (exports, tsup, alias, size, test, örnek, doküman, changeset) | Düşük-orta. Kalıp hazır ama dokunulan dosya sayısı fazla | bekliyor |

**Gün 4–6 notu:** Ürün adı değişikliği 186 yerde geçiyor. Üç parçaya bölündü ki her PR'ın review'u kolay olsun.

## Bilerek listeye alınmayanlar

| Issue | Neden |
|---|---|
| #82 Parampos hata kodları | Param'ın resmi kod listesi gerekiyor; yanlış eşleme müşteriye yanlış mesaj gösterir |
| #103 Basket builder | Kuruş hassasiyetinde para dağıtımı; hata riski yüksek |
| #112, #113, #114 site çevirileri | #111 (ikiden fazla dil altyapısı) bitmeden başlanamaz |
| #94 Nuxt, #95 SvelteKit, #93 NestJS | Adapter işleri; #93 tasarım gerektiriyor. #95 ve #93 2026-10-04'te bırakıldı |
| #90, #91, #104, #105, #116 | Tasarım veya RFC bekliyor |
| #60, #62–#65, #30, #36–#40, #133, #134 | Credential, sandbox ya da banka dokümanı gerektiriyor |

## Kapanan işler

| Tarih | İş | PR |
|---|---|---|
