---
tur: ders-notu
alan: ogrenme
guncelleme: 2026-10-04
ozet: "Faz 0: monorepo yapısı, paket script'leri, build ve CI adımlarının her birinin neyi garanti ettiği."
durum: aktif
---
# Faz 0: Kurulum ve CI

Plan: [[Öğrenme/00 - Kod Tabanı Öğrenme Planı]]. Referans: `upstream/main` @ `3758bef`, paket sürümü `0.6.0`.

## 1. Monorepo: iki proje, tek repo

- `pnpm-workspace.yaml` iki klasörü workspace sayar: `packages/*` (SDK) ve `apps/*` (web).
- `apps/web/package.json` SDK'ya `"better-payment": "workspace:*"` ile bağlanır. Site, npm'deki sürümü değil repodaki kodu kullanır (dogfooding).
- Kök `package.json` yalnızca yönlendirir: `pnpm test` → `pnpm --filter better-payment test`. Asıl script'ler paketin kendi `package.json`'ındadır.
- `packageManager: pnpm@10.33.0`: herkes aynı pnpm'i kullanır, lockfile kaymaz.
- `pnpm.onlyBuiltDependencies`: yalnızca `esbuild`, `sharp` ve `unrs-resolver`'ın install script'i çalışır. Bu bir supply-chain güvenlik önlemidir; #128'i incelerken "install script yok mu" diye bakmamızın nedeni bu.

## 2. Paketin script'leri (packages/better-payment/package.json)

| Script | Ne yapar |
|---|---|
| `build` | `tsup`: `src/`'den `dist/`'e CJS (`.js`), ESM (`.mjs`) ve tip (`.d.ts`) çıktısı |
| `test` | `vitest run`: `tests/**/*.test.ts` (sandbox, fixtures ve helpers hariç) |
| `test:coverage` | Aynı testler ve kapsam eşikleri (lines 87, functions 92, branches 73, statements 87) |
| `test:edge` | Aynı testler, edge-runtime global'leriyle (Buffer ve process yok) |
| `test:edge-smoke` | **Build edilmiş** `dist/index.mjs`'i gerçek Vercel Edge VM'de çalıştırır |
| `test:sandbox` | Gerçek provider test ortamları; secret yoksa atlanır |
| `typecheck` / `typecheck:examples` | `tsc --noEmit`; `examples/*.ts` ayrı tsconfig ile derlenir |
| `lint` / `format:check` | ESLint ve Prettier, yalnızca `src/**/*.ts` |
| `size` | `dist` dosyalarının gzip bütçesi ve client'ın sunucu modülü import etmemesi |

## 3. Build: tsup ve exports

- `tsup.config.ts` `entry`: her giriş noktası bir `dist/<ad>/index` üretir (index, client, testing, plugins, next, express, hono, fastify, elysia).
- `external: ['better-payment']`: `testing` ve `plugins` ana paketi **import eder**, içine gömmez. Böylece `MockProvider instanceof PaymentProvider` doğru çalışır (tek class kopyası).
- `minify: true` ve `keepNames: true`: küçük bundle, ama class ve fonksiyon isimleri korunur (hata adları, `instanceof`, `constructor.name`).
- `package.json` `exports`: dış dünyanın hangi yolları import edebileceğini belirler. tsup dosyayı üretse bile `exports`'ta yoksa `ERR_PACKAGE_PATH_NOT_EXPORTED` hatası alınır (#128).
- `vitest.config.ts` alias'ları `better-payment/*`'ı doğrudan `src/`'ye yönlendirir. Bu yüzden testler `exports` hatasını **göremez**.

## 4. CI (.github/workflows/ci.yml)

İki job var:

**`docs-translations`** (Node 22): `apps/web/scripts/check-translations.mjs`. Her `x.mdx` için bir `x.tr.mdx` olmalı, kod blokları birebir aynı olmalı, başlık seviyeleri eşleşmeli ve TR başlıklar EN id'sini (`[#id]`) korumalı.

**`package`** (Node 20, 22, 24 matrisi), sırayla:

| # | Adım | Yakaladığı hata türü |
|---|---|---|
| 1 | `pnpm install --frozen-lockfile` | `package.json` ile lockfile uyumsuzluğu |
| 2 | Lint | Kod kalitesi kuralları |
| 3 | Format check | Prettier uyumu (#128'de düşecekti) |
| 4 | Typecheck | Tip hataları |
| 5 | Typecheck examples | Dokümandaki örnek kodun derlenmemesi |
| 6 | Test (coverage) | Davranış hataları, kapsamın eşiğin altına düşmesi |
| 7 | Test (edge) | Node'a özgü API kullanımı (Buffer, node:crypto) |
| 8 | Build | Paketlenememe |
| 9 | Bundle size | Şişme; client'ın sunucu modülü çekmesi |
| 10 | Smoke (dist) | Build çıktısının CJS ve ESM olarak gerçekten yüklenmesi, class paylaşımı |
| 11 | Edge smoke | Minify edilmiş bundle'ın edge VM'de imza ve doğrulama yapabilmesi |
| 12 | No runtime deps | `dependencies` alanına bir şey eklenmesi |
| 13 | Package contents | `dist`'te beklenen dosyalar, `npm pack --dry-run` |

**CI'ın garanti etmedikleri** (review'da elle bakılmalı):
- Yeni subpath'in `exports`'ta olması. Smoke testi yalnızca `.`, `client`, `testing` ve `plugins`'i dener (#128).
- Gerçek provider davranışı. Sandbox ayrı workflow'da, nightly (`cron: '17 3 * * *'`) çalışır ve yalnızca `czaydev/better-payment` reposunda.
- Web uygulamasının build'i. Vercel yapıyor; fork PR'larında "Authorization required" uyarısı normal.

**Fork PR'ları:** İlk katkıda workflow `action_required` durumunda bekler; bir maintainer "Approve and run" der.

## Sorular (cevaplar bende)

1. `pnpm test`, `test:edge`, `test:sandbox` ve `test:edge-smoke` arasındaki fark ne?
2. CI "runtime dependency yok" kuralını nasıl uyguluyor, neden önemli?
3. Bir PR'ın CI'ı neden ilk seferde çalışmaz?
4. (Ek) Testler geçtiği halde #128'deki `exports` hatası neden yakalanmadı?
5. (Ek) `external: ['better-payment']` kaldırılsaydı hangi CI adımı düşerdi?

## Cevaplarım

_(doldurulacak)_

## Alıştırma

CI adımlarını lokalde sırayla çalıştır (bkz. derste verilen komutlar) ve her birinin çıktısını bir cümleyle not et.
