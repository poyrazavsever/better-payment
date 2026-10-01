---
tur: arastirma
alan: teknik
guncelleme: 2026-10-01
ozet: "Repo, issue, PR, Actions, npm ve topluluk durumunun başlangıç fotoğrafı."
durum: tamamlandi
---
# İnceleme: 2026-10-01 Teknik ve Topluluk Durumu

## Anlık tablo

| Alan | Değer |
|---|---:|
| Sürüm | 0.5.2 |
| GitHub star | 196 |
| Fork | 18 |
| Watcher | 7 |
| npm haftalık indirme | 1.530 |
| Açık issue | 44 |
| Açık PR | 1 |
| Runtime dependency | 0 |
| Son CI test sayısı | 438 |
| Line coverage | %92,75 |
| Ana bundle | 26,4 kB gzip |

## Mimari

- `packages/better-payment`: yayınlanan TypeScript paketi.
- `apps/web`: Next.js ve Fumadocs tabanlı site/dokümantasyon.
- Core: provider abstraction, handler, validation, idempotency, events, plugins.
- Entry point'ler: root, client, testing, plugins, next, express, hono, fastify.

## Topluluk

- CODEOWNERS yalnız `@czaydev`.
- İncelenen 51 merged PR'ın 36'sı owner, 12'si bot, 3'ü tek dış contributor tarafından açılmış.
- npm collaborator listesinde yalnız proje sahibi görünüyor.
- Maintainer desteği için gerçek alan var; önce sürdürülebilir katkı ve review güveni gerekli.

## CI ve sandbox

- Ana CI Node 20/22 üzerinde yeşil.
- Son beş scheduled sandbox run kırmızı.
- Kök neden: `iyzico.sandbox.test.ts` içinde import edilen factory ile yerel `const iyzico` isim çakışması.
- PayTR, Parampos ve Akbank secret'ları scheduled run'da yok; ilgili testler skip ediliyor.

## Repo hijyeni

- GitHub description ve topics boş.
- `apps/web/README.md` create-next-app şablonu.
- Web için ayrı build/lint CI job'u görünür değil.
- pnpm 10.33, kök `pnpm.onlyBuiltDependencies` alanını yok sayıyor.

## Kanıt bağlantıları

- Repo: https://github.com/czaydev/better-payment
- Roadmap: https://github.com/czaydev/better-payment/issues/44
- Database RFC: https://github.com/czaydev/better-payment/issues/116
- Açık PR: https://github.com/czaydev/better-payment/pull/120
- Son kırık sandbox: https://github.com/czaydev/better-payment/actions/runs/36698219783
- npm: https://www.npmjs.com/package/better-payment

