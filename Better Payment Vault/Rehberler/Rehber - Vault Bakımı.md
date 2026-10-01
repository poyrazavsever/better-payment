---
tur: rehber
alan: vault
guncelleme: 2026-10-01
ozet: "Yerel vault'un oluşturulması, doğrulanması ve sade tutulması için işletim rehberi."
durum: aktif
---
# Vault Bakımı

## Günlük kullanım

- Giriş noktası: [[Harita]].
- Yeni iş: ilgili plan veya issue notuna eklenir.
- Kalıcı karar: yeni ADR olarak yazılır.
- Gün sonu: yapılanlar, kanıtlar, engeller ve sonraki adım günlük kaydına işlenir.

## Komutlar

```powershell
node .local-tools/vault.mjs check
node .local-tools/vault.mjs lint
node .local-tools/vault.mjs pr-safety
node .local-tools/vault.mjs new-adr "Karar başlığı"
```

`check`; haritayı, frontmatter alanlarını, wiki linklerini, not boyutlarını ve PR güvenliğini birlikte doğrular.

## Not yaşam döngüsü

1. Notu uygun klasörde oluştur.
2. `tur`, `alan`, `guncelleme`, `ozet` alanlarını ekle.
3. Kanonik notu [[Harita]] veya ilgili üst nota bağla.
4. Tamamlanan geçici bilgiyi kanonik nota taşı; kopyaları sil veya linke dönüştür.
5. Haftada bir kırık link, eski tarih ve sahipsiz plan taraması yap.

## Git güvenliği

Yerel ignore ve hook kurulumu çalışma kopyası başına bir kez çalıştırılır:

```powershell
powershell -ExecutionPolicy Bypass -File .local-tools/setup-vault.ps1
```

Koruma katmanları [[Kararlar/ADR-001 - Vault Yerel ve PR Dışı]] içinde açıklanır. Fork yeniden clone edilirse yerel dosyalar Git'ten gelmeyeceği için vault ayrıca güvenli bir kişisel yedeğe alınmalıdır.

Bilgisayarlar arası kurulum ve senkronizasyon için [[Rehberler/Rehber - Vault Senkronizasyonu]] izlenir. `personal/vault` hiçbir zaman ürün branch'i veya PR kaynağı olarak kullanılmaz.
