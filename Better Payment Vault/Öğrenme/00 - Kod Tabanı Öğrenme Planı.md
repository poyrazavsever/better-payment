---
tur: plan
alan: ogrenme
guncelleme: 2026-10-03
ozet: "better-payment kod tabanını (SDK paketi, testler, web uygulaması) faz faz öğrenme ve review edebilir hale gelme planı."
durum: aktif
---
# Kod Tabanı Öğrenme Planı

## Amaç

Yazılan kodu kendim anlayabilmek ve PR'ları kendim, gerekçesiyle review edebilmek. Bu plan bitmeden yeni implementasyona başlanmaz. Sıradaki iş, plan bitince [#95 SvelteKit](https://github.com/czaydev/better-payment/issues/95) ve ardından [#93 NestJS](https://github.com/czaydev/better-payment/issues/93) olacak; durumları [[Planlama/Issue Portföyü]] içinde tutulur.

Referans nokta: `upstream/main` @ `a215089` (2026-10-03). Satır sayıları bu commit'e göredir.

## Çalışma şekli

- **Okuma sırası:** Her faz "önce akışı anla, sonra dosyayı oku" mantığıyla ilerler. Dosyalar yukarıdan aşağı değil, bir isteğin izlediği yoldan okunur.
- **Fazın parçaları:** Her fazda **okunacaklar**, **cevaplanacak sorular**, bir **alıştırma** ve bir **bitti kriteri** var. Sorulara kendi cümlelerimle cevap yazmadan faz bitmiş sayılmaz.
- **Notlar:** Cevaplar ve "aha" anları `Öğrenme/Notlar/Faz N - <konu>.md` dosyasına yazılır. Kod kopyalanmaz; dosya ve satır referansı verilir.
- **Claude ile oturumlar:** Oturum, faz numarasıyla başlar ("Faz 3'e devam"). Claude önce akışı anlatır, sonra soruları bana sorar; cevabı ben veririm, o düzeltir.
- **Alıştırma kodu:** Alıştırmalar ayrı bir lokal branch'te (`learn/faz-N`) yapılır, push edilmez. Upstream'e hiçbir şey gitmez.

## Genel harita

```
packages/better-payment (SDK, sıfır runtime bağımlılığı)
  src/index.ts ............ public API: betterPayment(), provider factory'leri, tipler
  src/core/ ............... PaymentCore, handler, plugin, event, hata, http, kripto
  src/providers/ .......... iyzico, paytr, parampos, akbank (her biri index + utils + types)
  src/adapters/ ........... fetch, next, express, fastify, hono, elysia (handler'ı framework'e bağlar)
  src/client/ ............. tarayıcı tarafı (better-payment/client)
  src/testing/ ............ MockProvider, test kartları (better-payment/testing)
  src/plugins/ ............ localized-errors (better-payment/plugins)
  tests/ .................. unit, integration, sandbox, fixtures, helpers
apps/web (Next.js 16 + Fumadocs, site ve dokümantasyon)
  app/[lang]/ ............. ana sayfa ve docs, TR/EN
  app/api/pay/[...path] ... SDK'nın kendisini kullanan demo endpoint (dogfooding)
  content/docs/ ........... 52 MDX sayfası (EN + .tr.mdx)
```

---

## Faz 0: Kurulum ve işleyiş haritası

**Hedef:** Repo'yu çalıştırmak, CI'ın her adımının ne kontrol ettiğini bilmek.

**Okunacaklar**
- Kök: `package.json` (`pnpm@10.33.0`), `pnpm-workspace.yaml`, `CONTRIBUTING.md`
- `.github/workflows/ci.yml`: Node 20, 22 ve 24 matrisi; lint, format, typecheck, typecheck:examples, coverage, edge, build, size, smoke, edge-smoke, runtime bağımlılığı yok kontrolü, paket içeriği
- `.github/workflows/sandbox.yml`, `.github/workflows/publish.yml` (yalnızca genel bakış)
- `packages/better-payment/package.json`: `scripts` ve `exports`

**Sorular**
1. `pnpm test`, `test:edge`, `test:sandbox` ve `test:edge-smoke` arasındaki fark ne?
2. CI "runtime dependency yok" kuralını nasıl uyguluyor, neden önemli?
3. Bir PR'ın CI'ı neden ilk seferde çalışmaz (fork ve ilk katkı onayı)?

**Alıştırma:** CI'daki adımları lokalde tek tek çalıştır ve her birinin neyi yakaladığını bir cümleyle yaz.

**Bitti:** CI yeşilken neyin garanti edildiğini, neyin edilmediğini (örneğin `exports` eksikliği, #128) açıklayabiliyorum.

---

## Faz 1: Ödeme alanı (domain) temelleri

**Hedef:** Kodu okumadan önce iş kavramlarını oturtmak.

**Okunacaklar**
- Docs: `concepts/` (configuration, handler, events, plugins, testing), `payments/` (pre-authorization, stored-cards)
- `src/types/index.ts` (521): `PaymentRequest`, `ThreeDSPaymentRequest`, `PaymentResponse`, `PaymentStatus`
- `src/types/common.ts`, `src/core/error-codes.ts` (92)

**Sorular**
1. 3D Secure akışı adım adım nasıl ilerler: init → banka sayfası → callback → complete? Hangi adım kimin sunucusunda gerçekleşir?
2. `createPayment`, `authorize` + `capture` ve `cancel` / `refund` / `voidAuthorization` farkları neler?
3. Callback neden form-urlencoded gelir ve neden imzası doğrulanmadan güvenilmez?
4. Idempotency ne işe yarar? "Çift çekim" (double charge) nasıl oluşur?

**Alıştırma:** 3DS akışını kendi çizdiğim bir diyagramla nota koy (tarayıcı, mağaza sunucusu, better-payment, banka).

**Bitti:** 3DS akışını ve her `PaymentStatus` değerini kendi cümlelerimle anlatabiliyorum.

---

## Faz 2: Çekirdek (core)

**Hedef:** `betterPayment({...})` çağrısından bir provider metoduna kadar giden yolu izlemek.

**Okuma sırası**
1. `src/index.ts` (152): neyin public olduğu
2. `src/core/BetterPayment.ts` (528): `PaymentCore`. `constructor`, `proxy()`, `run()`, `resolve()`, `emit()`, `use()`, `betterPayment()` factory'si ve plugin tip birleştirmesi (`PluginMethods`)
3. `src/core/BetterPaymentConfig.ts` (139), `validation.ts` (234)
4. `errors.ts` (59), `failure.ts` (91), `error-codes.ts`
5. `events.ts` (149), `plugin.ts` (227), `idempotency.ts` (74), `retry.ts`, `logger.ts`
6. `http.ts` (223): HTTP client, timeout, `HttpError`; `crypto.ts` (94): HMAC ve hash yardımcıları, WebCrypto
7. `utils.ts` (66)

**Sorular**
1. `payment.createPayment(req)` çağrıldığında hangi sırayla ne olur: doğrulama, plugin hook'ları, provider, event?
2. `proxy()` neden var? `use(id)` ile `rawProvider(id)` arasındaki fark ne?
3. Bir hata `BetterPaymentError` mı fırlatılır, yoksa `status: 'failure'` sonucu mu döner? Kural ne?
4. Plugin'ler hangi noktalara bağlanabilir, `PluginMethods` tipi bunu nasıl yansıtır?
5. Neden Node `crypto` değil de WebCrypto kullanılıyor (edge uyumu)?

**Alıştırma:** Debugger ya da `console.log` ile `tests/unit/core/better-payment.test.ts` içinden bir testi adım adım izle; çağrı sırasını nota yaz.

**Bitti:** `PaymentCore.run()` akışını dosya ve satır referanslarıyla anlatabiliyorum.

---

## Faz 3: Provider katmanı

**Hedef:** Bir provider'ın iskeletini ve dört provider'ın farklılıklarını kavramak.

**Okuma sırası**
1. `src/core/PaymentProvider.ts` (246): abstract metotlar (`createPayment`, `initThreeDSPayment`, `completeThreeDSPayment`, `refund`, `cancel`, `getPayment`), opsiyonel olanlar (`authorize`, `capture`, `saveCard` ve diğerleri, `notSupported`), `createHttpClient`, `errorCodeTable`
2. **PayTR** (ilk örnek, en anlaşılır hash yapısı): `paytr/utils.ts` (288) → `paytr/index.ts` (911) → `types.ts`, `error-codes.ts`
3. **iyzico:** `iyzico/utils.ts` (IYZWSv2 imzası) → `iyzico/index.ts` (1279)
4. **Parampos:** SOAP/XML, SHA1, ISO-8859-9 karakter seti. `parampos/utils.ts` (395) → `index.ts` (826)
5. **Akbank:** banka sanal POS'u, HMAC-SHA512. `akbank/utils.ts` (145) → `index.ts` (552)
6. `examples/custom-provider.ts` ve `tests/unit/examples/custom-provider.test.ts`

**Sorular**
1. Dört provider'ın kimlik doğrulama ve imza yöntemleri nasıl farklılaşıyor (tablo yap)?
2. `completeThreeDSPayment(callbackData)` her provider'da imzayı nerede ve nasıl doğruluyor?
3. Provider'a özgü hata kodları ortak `PaymentErrorCode`'a nasıl eşleniyor?
4. Bir provider bir özelliği desteklemiyorsa ne olur?

**Alıştırma:** `tests/unit/providers/paytr/utils.test.ts` içindeki bir hash'i elle (Node REPL'de `crypto` ile) yeniden hesapla. Ardından custom-provider örneğini kopyalayıp `learn/faz-3` branch'inde mini bir provider yaz.

**Bitti:** Yeni bir provider eklemek için hangi dosyaların ve hangi testlerin gerektiğini sayabiliyorum.

---

## Faz 4: HTTP handler ve adapter'lar (#95 ve #93'ün temeli)

**Hedef:** Bir HTTP isteğinin framework'ten provider'a nasıl ulaştığını ve cevabın nasıl döndüğünü anlamak.

**Okuma sırası**
1. `src/core/BetterPaymentHandler.ts` (963)
   - Action listeleri: `ALL_HANDLER_ACTIONS`, `DEFAULT_HANDLER_ACTIONS`, `PRIVILEGED_HANDLER_ACTIONS`, `CALLBACK_HANDLER_ACTIONS`
   - `BetterPaymentHandlerOptions`: `basePath`, `allowedActions`, `authorize`, `callbackRedirect`, idempotency
   - `handle()` → `route()` → `parseRoute()` → body parse → core
2. `src/adapters/fetch.ts` (81): `toFetchHandler`, `resolveHandler`, `serializeResponse`. **Diğer bütün adapter'lar buna dayanır.**
3. Web `Request`/`Response` kullananlar: `next.ts` (25), `hono.ts` (25), `elysia.ts` (30)
4. Node stream kullananlar: `express.ts` (96; raw body okuma, body parser çalıştıysa `readableEnded`), `fastify.ts` (94; plugin içinde form parser)
5. `apps/web/app/api/pay/[...path]/route.ts` ve `apps/web/lib/payment.ts`: SDK'nın sitede gerçek kullanımı

**Sorular**
1. `HandlerSource` neden bir fonksiyon da olabiliyor (lazy init, build sırasında env yokken)?
2. Callback action'ları neden ayrı tutuluyor; `authorize` onlara uygulanıyor mu?
3. Raw body neden kritik? Express'te bir body parser önce çalışırsa ne olur? Elysia'da hook body'yi okursa ne olur (#128)?
4. 303 redirect ve PayTR'nin düz metin `OK` cevabı nerede üretiliyor?
5. Yeni bir adapter eklemek için dokunulması gereken 9 yer neler? (Bkz. Faz 7 kontrol listesi.)

**Alıştırma**
- `complete-3ds` form callback'inin isteğini Express adapter'ından provider'a kadar satır satır izle.
- #95 hazırlığı: SvelteKit `+server.ts` imzasını (`{ request }` → `Response`) ve `csrf.checkOrigin` davranışını resmi dokümandan oku, nota özetle.
- #93 hazırlığı: NestJS'in Express ve Fastify platformlarında body parser'ın varsayılan davranışını oku.

**Bitti:** Bir isteğin yaşam döngüsünü (adapter → handler → core → provider → event → response) beyaz tahtada anlatabiliyorum.

---

## Faz 5: Client, testing ve plugin paketleri

**Okunacaklar**
- `src/client/index.ts` (399): tarayıcı güvenli API, neden ayrı subpath ve neden "browser-safe" kontrolü var
- `src/testing/index.ts` (885): `MockProvider`, `MOCK_CARDS`; kullanıcıların kendi testlerinde kullandığı araçlar
- `src/plugins/localized-errors/` (index 179 + tr/en/de/ru): örnek bir plugin

**Sorular**
1. `better-payment/testing`'in ana entry ile aynı class'ları paylaşması neden şart (`instanceof`, CI smoke testi)?
2. Bir plugin hangi tiplerle yeni metot ve hata kodu ekliyor?

**Alıştırma:** `localized-errors` plugin'ini örnek alıp `learn/faz-5` branch'inde yeni bir dil ekle ve testini yaz.

**Bitti:** Kendi plugin'imi yazıp tipleri doğru çıkacak şekilde bağlayabiliyorum.

---

## Faz 6: Test stratejisi (unit, integration, adapter, edge, sandbox)

**Hedef:** Hangi değişikliğin hangi test türüyle korunacağına karar verebilmek ve test yazabilmek.

**Okunacaklar**
- `tests/README.md`: test türleri. Not: içindeki klasör ağacı biraz eski (`e2e/` yok, `fixtures` daha fazla); gerçek yapı aşağıda.
- `vitest.config.ts` (coverage eşikleri, alias'lar), `vitest.edge.config.ts`, `vitest.sandbox.config.ts`

**Test türleri ve örnek dosyalar**

| Tür | Ne korur | Örnek | Teknik |
|---|---|---|---|
| Unit: util | Saf fonksiyon, hash ve imza | `unit/providers/paytr/utils.test.ts` | Sabit girdi ve beklenen çıktı |
| Unit: provider | Provider'ın giden isteği ve gelen cevabı yorumlaması | `unit/providers/paytr/index.test.ts` | `client.post = vi.fn()`, gönderilen form ve URL üzerinde assertion |
| Unit: core | Doğrulama, event, plugin, idempotency, retry | `unit/core/*.test.ts` | `tests/helpers/fake-payment.ts` |
| Unit: güvenlik | Sahte imza ve forged callback reddi | `unit/providers/iyzico/security.test.ts` | Negatif senaryolar |
| Adapter | Her framework'te aynı davranış | `unit/adapters/adapters.test.ts` | `describe.each` ile ortak senaryolar: JSON 3DS init, form callback ve 303, PayTR `OK`, invalid JSON, health |
| Integration | Gerçek istek formatı (header, body, imza) | `integration/providers/iyzico.test.ts`, `integration/core/multi-provider.test.ts` | İstek yakalama (intercept), `helpers/request-validator.ts` |
| Edge | WebCrypto ve fetch ile edge runtime uyumu | Bütün suite, `pnpm test:edge` | `environment: 'edge-runtime'` |
| Edge smoke | Build edilmiş bundle'ın Vercel Edge VM'de çalışması | `scripts/edge-smoke.mjs` | Build sonrası |
| Sandbox | Gerçek provider test ortamı | `tests/sandbox/*.sandbox.test.ts` | Credential yoksa atlanır; nightly workflow |
| Örnekler | Dokümandaki kodun derlenmesi | `examples/*.ts` | `pnpm typecheck:examples` |

**Sorular**
1. Provider testinde neden `fetch` değil de `client.post` mock'lanıyor?
2. Integration testi unit testten ne fazlasını yakalıyor?
3. #128'deki `exports` hatası hangi test türüyle yakalanabilirdi (paket kurulum smoke testi)?
4. Sandbox testleri neden PR CI'ında değil de nightly çalışıyor, credential'lar nasıl korunuyor?

**Alıştırmalar** (`learn/faz-6`)
1. **Unit:** `core/utils.ts` içinden bir fonksiyon seç; sınır değerleri dahil üç test yaz.
2. **Provider unit:** PayTR'de `refund` için forged ve geçersiz senaryolarla yeni bir test yaz.
3. **Adapter:** `adapters.test.ts` içindeki `adapters` tablosunu oku; Express'teki "body parser önce çalıştı" varyantının neden var olduğunu açıkla ve lokalde bir varyant ekle.
4. **Coverage:** `pnpm test:coverage` raporunda en düşük kapsamlı dosyayı bul; neyin test edilmediğini nota yaz.

**Bitti:** Bir PR'a baktığımda "bu değişiklik şu testlerle korunmalı" diyebiliyorum ve eksik testi kendim yazabiliyorum.

---

## Faz 7: Build, paketleme ve yayın

**Okunacaklar:** `tsup.config.ts` (entry'ler, cjs ve esm, dts), `package.json` `exports`, `scripts/check-size.mjs`, `.changeset/`, `publish.yml`, `CHANGELOG.md`

**Yeni subpath kontrol listesi** (#128'den çıkan ders; #95 ve #93'te bunu kullanacağım)
1. `src/adapters/<ad>.ts` (yapısal tipler, framework bağımlılığı yok)
2. `tsup.config.ts` entry
3. `package.json` `exports` (types, import, require)
4. `vitest.config.ts` alias
5. `tsconfig.examples.json` path
6. `scripts/check-size.mjs` bütçesi
7. `tests/unit/adapters/adapters.test.ts` ortak senaryoları, gerekiyorsa varyant
8. `examples/frameworks.ts`
9. Doküman: `integrations/frameworks(.tr).mdx`, `concepts/handler(.tr).mdx` tablosu, iki README
10. `.changeset/*.md` (minor)
11. Doğrulama: `npm pack` sonrasında boş bir projede `require` ve `import` denenir

**Sorular:** Changeset'in sürüm numarasını nasıl belirlediği; cjs ve esm ikili çıktının neden gerektiği.

**Bitti:** Kontrol listesini ezberden değil, nedenleriyle anlatabiliyorum.

---

## Faz 8: Web uygulaması (apps/web)

**Hedef:** Siteyi ve dokümanı değiştirebilecek ve review edebilecek seviyeye gelmek.

**Okuma sırası**
1. `apps/web/AGENTS.md` (Next 16 uyarısı), `README.md`, `TRANSLATIONS.md`
2. i18n: `proxy.ts` (dil yönlendirmesi ve `bp_locale` cookie), `lib/i18n/config.ts`, `dictionary.ts`, `ui.ts`
3. Sayfalar: `app/[lang]/layout.tsx` (fontlar, `RootProvider`), `app/[lang]/page.tsx` (bölüm sırası)
4. Docs: `source.config.ts` (rehype checkmark, Shiki teması), `lib/source.ts` (ikon plugin'i), `app/[lang]/docs/[[...slug]]/page.tsx`, `lib/mdx-components.tsx`, `content/docs/**/meta.json`
5. Bileşenler: `Hero`, `ProviderNetwork` (zamanlayıcıyla çalışan akış), `Integrations` ve `CompareSlider`, `RevealOnScroll`, `lib/button-variants.ts`, `globals.css` (token'lar ve motion)
6. `scripts/check-translations.mjs`, `next.config.ts` (redirect'ler, `images.qualities`), `app/sitemap.ts`, `app/robots.ts`
7. Marka kararları: [[Branding/05 - Brand Lock]], [[Branding/06 - Bileşen ve Motion Spesifikasyonu]]

**Sorular**
1. Bir docs sayfası EN ve TR olarak nasıl eşleşiyor, çeviri kontrolü neyi kontrol ediyor?
2. Server ve client component sınırı nerede, neden (`DocsCodeBlock` örneği)?
3. Yeni bir doküman sayfası eklemek için hangi dosyalara dokunulur?

**Alıştırma:** `learn/faz-8` branch'inde sahte bir docs sayfası ekle (EN ve TR, `meta.json`), çeviri kontrolünü çalıştır, sonra sil.

**Bitti:** Bir web PR'ını görsel, i18n ve build açısından review edebiliyorum.

---

## Faz 9: Review pratiği ve issue'lara geçiş

1. [[Rehberler/Rehber - PR Review]] ve [[Şablonlar/Şablon - PR Review]] üzerinden kendi review kontrol listemi güncelle (Faz 6 ve Faz 7 dersleriyle).
2. **Pratik:** #128'in (Elysia) ilk halini Claude'un bulgularına bakmadan kendim review et; sonra karşılaştır.
3. **#95 SvelteKit:** Daha basit bir iş; web `Request`/`Response` ile çalışır. Kontrol listesine ek olarak CSRF (`csrf.checkOrigin`) notu gerekiyor.
4. **#93 NestJS:** Tasarım sorusu var (module mü, controller helper mı). Önce issue'da yaklaşım yazılır, sonra kod. Express ve Fastify platformlarının ikisi de test edilir.

**Bitti:** #95 için PR'ı kendim yazıp kendim review ederek açabiliyorum.

---

## İlerleme

| Faz | Konu | Durum | Not dosyası |
|---|---|---|---|
| 0 | Kurulum ve CI | bekliyor | |
| 1 | Ödeme alanı | bekliyor | |
| 2 | Core | bekliyor | |
| 3 | Provider'lar | bekliyor | |
| 4 | Handler ve adapter'lar | bekliyor | |
| 5 | Client, testing, plugin | bekliyor | |
| 6 | Test stratejisi | bekliyor | |
| 7 | Build ve yayın | bekliyor | |
| 8 | Web uygulaması | bekliyor | |
| 9 | Review pratiği → #95, #93 | bekliyor | |

Tahmini süre: günde 1–2 saatle Faz 0–4 bir hafta, Faz 5–9 bir hafta. #95 için Faz 0, 4, 6 ve 7'nin bitmiş olması yeterli; geri kalanlar paralel ilerleyebilir.
