---
tur: rehber
alan: vault
guncelleme: 2026-10-01
ozet: "Vault'u bilgisayarlar arasında personal/vault branch'iyle güvenli biçimde senkronlama rehberi."
durum: aktif
---
# Vault Senkronizasyonu

## Değiştirilemez sınır

`personal/vault` kişisel senkronizasyon branch'idir. `main`e merge edilmez, feature branch'lere taban olmaz ve upstream PR kaynağı olarak kullanılmaz. Fork herkese açıksa bu branch de herkese açıktır; secret, credential, kart verisi ve özel müşteri bilgisi yazılmaz.

## Başka bilgisayarda ilk kurulum

Ürün repository'si ile vault'u ayrı klasörlere clone et:

```powershell
git clone https://github.com/poyrazavsever/better-payment.git better-payment
git clone --branch personal/vault --single-branch https://github.com/poyrazavsever/better-payment.git better-payment-vault
```

Kod ve PR çalışmaları yalnız `better-payment` klasöründe, kişisel notlar yalnız `better-payment-vault` klasöründe yapılır.

## Günlük senkronizasyon

Vault klasöründe:

```powershell
git pull --ff-only
node .local-tools/vault.mjs check
git add -- "Better Payment Vault" .local-tools .local-githooks .better-payment-local-ignore README.md .gitignore .gitattributes
git commit -m "vault: sync personal workspace"
git push origin personal/vault
```

Pre-push hook'u vault içeren commit'lerin başka bir remote branch'e gönderilmesini reddeder. `personal/vault` üzerinde ürün kaynağı görülürse commit ve push doğrulamaları başarısız olur.

## PR öncesi kontrol

Ürün checkout'unda branch'in `personal/vault` olmadığını ve diff'te kişisel yol bulunmadığını doğrula:

```powershell
git branch --show-current
git diff --name-only upstream/main...HEAD
```

`Better Payment Vault/`, `.local-tools/`, `.local-githooks/` veya `.better-payment-local-ignore` görünürse PR açılmaz.
