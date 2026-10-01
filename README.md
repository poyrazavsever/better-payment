# Better Payment Personal Vault

> **Bu branch ürün kodu değildir.** Kişisel çalışma sistemini bilgisayarlar arasında senkronlamak için ayrılmış, bağımsız geçmişe sahip bir orphan branch'tir.

## Değiştirilemez sınır

- `personal/vault`, `main` veya herhangi bir feature branch ile merge edilmez.
- Bu branch upstream PR kaynağı olarak kullanılmaz.
- Ürün kaynak kodu bu branch'e eklenmez.
- Fork herkese açıksa buradaki içerik de herkese açıktır; secret, credential, kart verisi ve özel müşteri bilgisi tutulmaz.

## Kullanım

Vault'u kod checkout'undan ayrı bir klasöre clone et:

```powershell
git clone --branch personal/vault --single-branch https://github.com/poyrazavsever/better-payment.git better-payment-vault
```

Ardından doğrulama ve yerel hook kurulumu için:

```powershell
powershell -ExecutionPolicy Bypass -File .local-tools/setup-vault.ps1
node .local-tools/vault.mjs check
```

Ayrıntılar için `Better Payment Vault/Rehberler/Rehber - Vault Senkronizasyonu.md` dosyasına bak.
