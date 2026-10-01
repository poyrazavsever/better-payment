---
tur: yol-haritasi
alan: planlama
guncelleme: 2026-10-01
ozet: "İlk katkıdan maintainer sorumluluğuna kadar 90 günlük uygulama planı."
durum: aktif
---
# 90 Günlük Maintainer Yol Haritası

## Gün 1–14: güvenilir katkıcı

- [ ] Nightly sandbox isim gölgeleme hatasını düzelt.
- [ ] Sandbox workflow'u yeniden çalıştır ve kanıtı PR'a ekle.
- [x] #108 veya #106 issue'sunu claim et.
- [ ] #120 PR'ını ayrıntılı incele.
- [x] Fork'a `upstream` remote ekle ve katkı branch düzenini kur.
- [ ] İlk iki PR'da test, doküman, changeset ve güvenlik kurallarını eksiksiz uygula.

## Gün 15–35: alan sahipliği

- [ ] #111 veya #103 arasından bir orta ölçekli issue seç.
- [ ] Haftalık Actions/PR/issue taramasına başla.
- [ ] Bir dış contributor PR'ına review ver.
- [ ] Açık issue'ları hazır/bloklu/credential/assigned olarak triage et.
- [ ] İlk teknik duyuru veya build-in-public notunu hazırla.

## Gün 36–60: tasarım ve release

- [ ] #116 RFC için yazılı tasarım değerlendirmesi üret.
- [ ] Adapter conformance test kit'i önerisini somutlaştır.
- [ ] Bir release PR'ına ve dry-run publish sürecine eşlik et.
- [ ] Web/docs veya güvenilirlik alanında düzenli sorumluluk al.
- [ ] Maintainer ile Triage rolünü konuş.

## Gün 61–90: bakım sorumluluğu

- [ ] En az 3–5 merged PR ve iki alan kanıtı.
- [ ] İki nitelikli PR review.
- [ ] En az bir core/test güvenilirlik katkısı.
- [ ] Düzenli issue triage ve Actions takibi.
- [ ] Triage sonrası Write/Maintain rolü için sorumluluk sınırını konuş.
- [ ] CODEOWNERS'ın önce `apps/web` gibi düşük riskli alanlarda bölünmesini öner.

## Haftalık kanıt

Her hafta [[Şablonlar/Şablon - Günlük Kayıt]] üzerinden kısa kapanış kaydı açılır; PR, issue ve Actions bağlantıları eklenir.
