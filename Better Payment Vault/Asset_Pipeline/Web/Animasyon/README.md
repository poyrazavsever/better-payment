---
tur: uretim
alan: web-branding
guncelleme: 2026-10-01
ozet: "Animasyonlu ikon denemesi: Higgsfield video döngüsü, web kodlaması ve şeffaflık yöntemi."
durum: aktif
---
# Animasyonlu ikonlar

## Deneme: event/listener

- Model: Kling 3.0, 1:1, 5 sn, std, ses kapalı; başlangıç ve bitiş karesi aynı statik ikon (`Ikon/Kaynak/icon-events-source.jpg` kaynağı) → dikişsiz döngü. Job `f690cdc6-5a25-48b7-84ba-ced4dc1f78b5`, 10 kredi.
- İlk ve son kare farkı RMSE %0.9; döngü fark edilmiyor.
- Hareket: halkalar sırayla hafif dalgalanır, indigo çekirdek parlayıp söner, obje çok az süzülür.

## Şeffaflık yöntemi

`video_background_remover` (job `6b75e614-6024-4a8b-bda0-6fdd83fe24c8`, 1 kredi) alfa kanalı vermedi; nesneyi siyah zemine yerleştirilmiş H.264 olarak döndürdü. Kullanılmadı.

Seçilen yöntem: orijinal videonun zemini (250, 249, 252) `colorlevels` ile tam beyaza çekilir, video sayfada `mix-blend-mode: multiply` ile oynatılır. Beyaz, altındaki açık yüzeyde kaybolur.

```
colorlevels=rimax=0.9804:gimax=0.9765:bimax=0.9882,crop=640:640:(iw-640)/2:(ih-640)/2+10,scale=480:480
```

- Çıktı: `icon-events.mp4` (H.264, 136 KB), `icon-events.webm` (VP9), `icon-events-poster.png`.
- Sınır: yalnız açık yüzeylerde (beyaz, Canvas, Lilac Tint) çalışır; koyu zeminde statik şeffaf PNG kullanılır.
- Web: `<video autoplay muted loop playsinline poster>`; `prefers-reduced-motion` altında poster gösterilir.

## Maliyet tahmini

Tüm 15 ikon için yaklaşık 15 × 10 = 150 kredi.
