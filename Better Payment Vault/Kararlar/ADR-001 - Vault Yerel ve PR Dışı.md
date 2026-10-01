---
tur: adr
alan: kararlar
guncelleme: 2026-10-01
ozet: "Vault'un ayrı bir kişisel branch'te senkronlanıp upstream PR'larından kesin olarak ayrılması kararı."
durum: kabul
---
# ADR-001: Vault Yerel ve PR Dışı

## Bağlam

Vault kişisel planlar, maintainer hazırlığı, mesaj taslakları ve çalışma kayıtları içerir. Bunlar upstream ürün kaynağı değildir ve fork üzerinden açılacak PR'lara gitmemelidir.

## Karar

- `Better Payment Vault/`, `.local-tools/`, `.local-githooks/` ve `.better-payment-local-ignore` yalnızca fork'taki yetim `personal/vault` branch'inde versionlanır.
- `personal/vault`, `main` ile ortak geçmiş taşımaz; hiçbir zaman `main`e merge edilmez ve PR kaynağı yapılmaz.
- Diğer bilgisayarlarda vault, ürün checkout'undan ayrı bir klasöre `--branch personal/vault --single-branch` ile clone edilir.
- Repo `.gitignore` dosyası değiştirilmez.
- Yerel `core.excludesFile`, kendisini de yok sayan `.better-payment-local-ignore` dosyasını kullanır.
- Yerel `core.hooksPath`, `.local-githooks` dizisini kullanır.
- Pre-commit hook'u kişisel dosyaların normal branch'lerde tracked veya staged olmasını engeller.
- Pre-push hook'u vault içeren bir commit'in `refs/heads/personal/vault` dışında herhangi bir remote branch'e gönderilmesini reddeder.
- `personal/vault` branch'i yalnız vault, yerel araçlar ve branch uyarı dosyalarını kabul eder; ürün kaynaklarını reddeder.

## Sonuçlar

- Normal `git add .` vault'u görmez.
- `git add -f` ile yanlışlıkla ekleme hook tarafından yakalanır.
- Yeni bilgisayarda vault ayrı clone edilir; ürün repository'sine karışmadan güncellenebilir.
- Fork herkese açıksa `personal/vault` branch'i de herkese açıktır; secret, credential, kart verisi ve özel müşteri bilgisi kesinlikle yazılmaz.
- Git hook'ları kazaları önleyen bir savunma katmanıdır, mutlak güvenlik sınırı değildir; `--no-verify` ile aşılabilir. Bu nedenle değiştirilemez sınır ayrı orphan branch ve ayrı clone kullanımıdır. Her upstream PR öncesinde `git diff --name-only upstream/main...HEAD` çıktısında vault yollarının sıfır olduğu ayrıca doğrulanır; bu koşulu sağlamayan PR açılmaz.
- Vault yedeklemesi ve geçmişi GitHub PR sürecinden tamamen ayrı kalır.

## Doğrulama

```powershell
git check-ignore -v "Better Payment Vault/Harita.md"
git config --get core.hooksPath
node .local-tools/vault.mjs check
git status --short --untracked-files=all
git branch --show-current
git diff --name-only upstream/main...HEAD
```
