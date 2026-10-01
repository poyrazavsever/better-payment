---
tur: durum
alan: teknik
guncelleme: 2026-10-01
ozet: "Projenin güncel güçlü yönleri, riskleri ve güvenilirlik kapıları."
durum: aktif
---
# Mevcut Durum ve Riskler

Kanonik araştırma kaydı: [[Araştırma/İnceleme - 2026-10-01 Teknik ve Topluluk Durumu]].

## Güçlü yönler

- Callback doğrulama ve sabit zamanlı karşılaştırma.
- Mutating ödeme işlemlerinde otomatik retry yapılmaması.
- Ağ belirsizliğinin `pending + NETWORK_ERROR` olarak modellenmesi.
- Güvenli varsayılan HTTP handler ve idempotency.
- Sıfır runtime dependency, ESM/CJS ve edge runtime desteği.
- Plugin, event, testing ve framework adapter yüzeyleri.
- İngilizce/Türkçe dokümantasyon ve güçlü katkı rehberi.

## Kritik riskler

- Bus factor 1: CODEOWNERS ve npm collaborator tek kişi.
- PayTR, Parampos ve Akbank gerçek sandbox doğrulaması bekliyor.
- Contract fixture issue'su açık.
- Çok hızlı release temposu insan review ihtiyacını artırıyor.
- Son beş nightly sandbox koşusu test isim gölgelemesi nedeniyle kırık.
- Web uygulaması için standart CI build/lint job'u görünür değil.
- Repo description/topics boş; `apps/web/README.md` şablon halinde.
- Yerel pnpm `onlyBuiltDependencies` yapılandırmasını yok sayıyor.

## Güvenilirlik kapısı

Duyuru veya büyük provider iddiasından önce:

1. Nightly sandbox yeşil.
2. Provider matrisi `unit-tested`, `real sandbox verified`, `verification wanted` ayrımını gösteriyor.
3. Security-sensitive PR insan review'ı alıyor.
4. Contract fixture kapsamı artıyor.

