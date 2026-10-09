---
tur: plan
alan: planlama
guncelleme: 2026-10-09
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
| 1 | 10-04 → 10-05 | [#84 localizedErrors: Arapça (ar)](https://github.com/czaydev/better-payment/issues/84) → [PR #136](https://github.com/czaydev/better-payment/pull/136) | `ar.ts` (15 mesaj), `index.ts`'e bir satır, testteki `locales` listesi, patch changeset; gerekirse `dist/plugins` boyut bütçesi | Çok düşük | [[Planlama/Issue Portföyü#Güncel küçük iş durumu]] |
| 2 | 10-06 → 10-07 | [#139 test rehberi](https://github.com/czaydev/better-payment/issues/139) → [PR #140](https://github.com/czaydev/better-payment/pull/140) | Klasör ağacı gerçeğe uydurulur (`e2e/` ve PayTR integration testi yok; sandbox, helpers ve fixtures güncel); ölü `test:e2e` script'i kaldırılır | Çok düşük | [[Planlama/Issue Portföyü#Güncel küçük iş durumu]] |
| 3 | 10-08 → 10-09 | [#148 CI: adapter subpath smoke testi](https://github.com/czaydev/better-payment/issues/148) → [PR #149](https://github.com/czaydev/better-payment/pull/149) | Build sonrası `next`, `express`, `hono`, `fastify` ve `elysia` için `require` ve `import` denemesi; "Check package contents"e adapter dosyaları. #128'deki `exports` hatasını CI yakalar | Düşük | tamamlandi |
| 4 | 10-10 → 10-11 | [#158 Doküman: ürün adı](https://github.com/czaydev/better-payment/issues/158) → [PR #159](https://github.com/czaydev/better-payment/pull/159) | Prose'da "better-payment" → "Better Payment". 2026-10-09 sayımı: kod, import, link ve backtick dışında yaklaşık 30 yer (sayfa açıklamaları, giriş sayfası, birkaç cümle), EN ve TR, tek PR. `reference/changelog` hariç (artık changeset'ten üretiliyor). Başlık id'leri değişmez (`why-better-payment`, `add-a-language-to-better-payment` slug'ları aynı kalır). TR ekleri mevcut kullanım gibi ('i, 'e, 'in) | Düşük | review bekliyor |
| 5 | 10-12 → 10-13 | Web: marka 404 sayfası | `app/[lang]/not-found.tsx`, EN ve TR metinleri `dictionary.ts`'te, ana sayfa ve docs'a dönüş butonları | Düşük | hazir (önce issue) |
| 6 | 10-14 → 10-15 | Web: README ve kullanılmayan bağımlılıklar | `apps/web/README.md` create-next-app varsayılanından projeye özel kurulum notuna; kullanılmayan `next-themes` ve `zod` kaldırılır (import yok, doğrulandı) | Çok düşük | hazir (önce issue) |
| 7 | 10-16 → 10-17 | Web: sosyal paylaşım görseli | Higgsfield ile marka OG görseli (1200×630, EN ve TR); `openGraph.images` ve Twitter card metadata. Branding Faz 9'un devamı | Düşük | hazir (önce issue) |
| 8 | ~~10-18 → 10-19~~ | ~~[#96 React Router adapter](https://github.com/czaydev/better-payment/issues/96)~~ maintainer yaptı ([PR #142](https://github.com/czaydev/better-payment/pull/142)) | `next.ts` gibi web `Request`/`Response` adapter'ı; subpath adımları (exports, tsup, alias, size, ortak testler, örnek, doküman, changeset) | — | düştü |
| 9 | 10-20 → 10-21 | [#94 Nuxt / h3 adapter](https://github.com/czaydev/better-payment/issues/94) | #96 ile aynı kalıp; h3 v1 ve v2 `Request` erişimi farkı | Düşük-orta | bekliyor |

### İkinci dalga (eklendi 2026-10-04, henüz başlanmadı)

Kapsam ölçümü 2026-10-04'te yapıldı (`vitest --coverage`; toplam satır kapsamı %92,8, branch kapsamı %79,4).

| # | Tarih | İş | Kapsam | Risk | Durum |
|---|---|---|---|---|---|
| 10 | 10-22 → 10-23 | Test: `iyzico/utils.ts` | Kapsamı en düşük dosya (satır %71, branch %50). Eksik dallar için unit test; davranış değişmez | Çok düşük (yalnızca test) | hazir (önce issue) |
| 11 | 10-24 → 10-25 | Test: `core/crypto.ts` | Satır %81, fonksiyon %80. Kullanılmayan yardımcılar ve hata yolları için test; Node ve edge'de aynı sonuç | Çok düşük (yalnızca test) | hazir (önce issue) |
| 12 | 10-26 → 10-27 | Test: Express ve Fastify adapter dalları | Branch kapsamı %64 ve %60. `next(error)` yolu, `next` yokken 500, GET/HEAD gövdesiz istek, string chunk okuma. Testler bitince `vitest.config.ts` eşikleri yeni değerlerin hemen altına çekilir | Düşük (yalnızca test ve eşik) | hazir (önce issue) |
| 13 | 10-28 → 10-29 | Paket metadata ve README rozetleri | `keywords`'e eksikler (`hono`, `express`, `fastify`, `elysia`, `virtual-pos`, `sanal-pos`); kök ve paket README'sine CI ve Docs rozetleri | Çok düşük | hazir (önce issue) |
| 14 | 10-30 → 10-31 | Doküman issue şablonu | `.github/ISSUE_TEMPLATE/docs.yml`: sayfa linki, sorun, dil (EN/TR). Mevcut şablonlarla aynı yapı | Çok düşük | hazir (önce issue) |
| 15 | 11-01 → 11-02 | localizedErrors: Fransızca (fr) | #84'ün aynısı: `fr.ts`, kayıt, test, doküman, README, changeset. (`es` testte özel dil örneği olarak kullanıldığından seçilmedi) | Çok düşük | hazir (önce issue) |
| 16 | 11-03 → 11-04 | Örnek: iade ve iptal | `examples/refund-and-cancel.ts`: `refund`, `cancel`, `getPayment` kullanımı; `typecheck:examples` ile CI'da derlenir | Çok düşük | hazir (önce issue) |
| 17 | 11-05 → 11-06 | Web: erişilebilirlik küçük düzeltmeleri | "İçeriğe atla" (skip link) bağlantısı, `main` landmark kontrolü, odak halkaları; EN ve TR metin `dictionary.ts`'te | Düşük | hazir (önce issue) |
| 18 | 11-07 → 11-08 | Doküman: SSS ve sorun giderme sayfası | `guides/troubleshooting(.tr).mdx`: iyzico sepet toplamı uyuşmazlığı, callback URL ve CSRF, `NETWORK_ERROR` ile "tekrar ödeme" ve test kartları. Mevcut sayfalara link verir | Düşük | hazir (önce issue) |

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

Kapanış durumları ve kanıtları [[Planlama/Issue Portföyü#Güncel küçük iş durumu]] içinde tutulur.
