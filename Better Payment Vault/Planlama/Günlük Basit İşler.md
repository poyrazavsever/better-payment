---
tur: plan
alan: planlama
guncelleme: 2026-10-04
ozet: "İki günde bir kapatılacak, küçük ve hata riski düşük işlerin tarihli sırası."
durum: aktif
---
# Basit İşler Takvimi

**Ritim:** İki günde bir iş, bir PR. Bir iş birden fazla güne bölünmez.

**Seçim ölçütü:** Küçük diff, mevcut bir kalıbı izliyor, para hesabı ya da imza mantığına dokunmuyor, resmi dış kaynak gerektirmiyor. Upstream `main` @ `3758bef` (2026-10-04) üzerinden değerlendirildi.

**Her işten önce:**
- Issue varsa altına "claim" yorumu yaz.
- Issue yoksa önce kısa bir issue aç; CONTRIBUTING her PR için bir issue istiyor.

## Takvim

| # | Tarih | İş | Kapsam | Risk | Durum |
|---|---|---|---|---|---|
| 1 | 10-04 → 10-05 | [#84 localizedErrors: Arapça (ar)](https://github.com/czaydev/better-payment/issues/84) | `ar.ts` (15 mesaj), `index.ts`'e bir satır, testteki `locales` listesi, patch changeset; gerekirse `dist/plugins` boyut bütçesi | Çok düşük | aktif |
| 2 | 10-06 → 10-07 | `tests/README.md` güncelleme | Klasör ağacı gerçeğe uydurulur (`e2e/` ve PayTR integration testi yok; sandbox, helpers ve fixtures güncel); ölü `test:e2e` script'i kaldırılır | Çok düşük | hazir (önce issue) |
| 3 | 10-08 → 10-09 | CI: adapter subpath smoke testi | Build sonrası `next`, `express`, `hono`, `fastify` ve `elysia` için `require` ve `import` denemesi; "Check package contents"e adapter dosyaları. #128'deki `exports` hatasını CI yakalar | Düşük | hazir (önce issue) |
| 4 | 10-10 → 10-11 | Doküman: ürün adı | Prose'da "better-payment" → "Better Payment" (186 yer, EN ve TR, tek PR). Kod, import ve paket adı değişmez; çeviri kontrolü kod bloklarını korur | Düşük | hazir (önce issue, #123 devamı) |
| 5 | 10-12 → 10-13 | Web: marka 404 sayfası | `app/[lang]/not-found.tsx`, EN ve TR metinleri `dictionary.ts`'te, ana sayfa ve docs'a dönüş butonları | Düşük | hazir (önce issue) |
| 6 | 10-14 → 10-15 | Web: README ve kullanılmayan bağımlılıklar | `apps/web/README.md` create-next-app varsayılanından projeye özel kurulum notuna; kullanılmayan `next-themes` ve `zod` kaldırılır (import yok, doğrulandı) | Çok düşük | hazir (önce issue) |
| 7 | 10-16 → 10-17 | Web: sosyal paylaşım görseli | Higgsfield ile marka OG görseli (1200×630, EN ve TR); `openGraph.images` ve Twitter card metadata. Branding Faz 9'un devamı | Düşük | hazir (önce issue) |
| 8 | 10-18 → 10-19 | [#96 React Router adapter](https://github.com/czaydev/better-payment/issues/96) | `next.ts` gibi web `Request`/`Response` adapter'ı; subpath adımları (exports, tsup, alias, size, ortak testler, örnek, doküman, changeset) | Düşük-orta | bekliyor |
| 9 | 10-20 → 10-21 | [#94 Nuxt / h3 adapter](https://github.com/czaydev/better-payment/issues/94) | #96 ile aynı kalıp; h3 v1 ve v2 `Request` erişimi farkı | Düşük-orta | bekliyor |

## Yeni subpath kontrol listesi (8. ve 9. işler için)

1. `src/adapters/<ad>.ts` (yapısal tipler)
2. `tsup.config.ts` entry
3. `package.json` `exports`
4. `vitest.config.ts` alias
5. `tsconfig.examples.json` path
6. `scripts/check-size.mjs` bütçesi
7. `tests/unit/adapters/adapters.test.ts`
8. `examples/frameworks.ts`
9. `integrations/frameworks(.tr).mdx`, `concepts/handler(.tr).mdx` tablosu, iki README
10. Changeset
11. `npm pack` ve boş bir projede `require`/`import` denemesi

## Bilerek listeye alınmayanlar

| Issue | Neden |
|---|---|
| #82 Parampos hata kodları | Param'ın resmi kod listesi gerekiyor |
| #103 Basket builder | Kuruş hassasiyetinde para dağıtımı; hata riski yüksek |
| #112, #113, #114 site çevirileri | #111 bitmeden başlanamaz |
| #93 NestJS, #95 SvelteKit | 2026-10-04'te bırakıldı |
| #90, #91, #104, #105, #116 | Tasarım veya RFC bekliyor |
| #60, #62–#65, #30, #36–#40, #133, #134 | Credential, sandbox ya da banka dokümanı gerekiyor |

## Kapanan işler

| Tarih | İş | PR |
|---|---|---|
