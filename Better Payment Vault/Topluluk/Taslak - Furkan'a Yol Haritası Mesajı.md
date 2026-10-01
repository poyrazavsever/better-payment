---
tur: taslak
alan: topluluk
guncelleme: 2026-10-01
ozet: "Proje sahibiyle katkı ve maintainer yol haritasını paylaşmak için mesaj taslağı."
durum: hazir
---
# Furkan'a Yol Haritası Mesajı

Furkan abi selam,

Projeyi konuştuğumuzdan beri README'den provider implementasyonlarına, testlere, CI/sandbox akışlarına, dokümantasyon sitesine ve açık issue'lara kadar detaylıca inceledim.

Vizyonu iki katmanda okuyorum: kısa vadede Türkiye'deki ödeme sağlayıcıları için güvenli, type-safe ve tek bir entegrasyon yüzeyi oluşturmak; orta vadede ise plugin/adapter yapısıyla orkestrasyon, gözlemlenebilirlik ve daha geniş provider kapsamına ilerlemek. Bence projenin en güçlü tarafı, yalnızca bir SDK koleksiyonu değil, geliştiricinin provider değiştirme ve bakım maliyetini azaltan açık kaynak bir altyapı olma potansiyeli.

Bu proje özelinde kendime şöyle bir yol haritası çıkardım:

1. İlk aşamada nightly sandbox akışındaki Iyzico başlangıç hatasını düzeltip güvenilirlik tarafında hızlı ve ölçülebilir bir katkı yapmak.
2. Ardından warning/CI temizliği ile küçük ve iyi tanımlı issue'lardan birkaçını kapatmak; özellikle test ve dokümantasyon kalitesini yükseltmek.
3. Açık PR'larda düzenli review desteği vermek, issue'ları bağımlılık ve önceliğe göre düzenlemek ve contributor deneyimini iyileştirmek.
4. Plugin API gibi mimari başlıklarda önce ADR/tasarım önerisi hazırlayıp uygulamaya mutabakatla geçmek.
5. Teknik ilerlemeyi haftalık kısa duyurular, release notları ve katkıcı çağrılarıyla görünür kılmak.

Hedefim yalnızca birkaç PR göndermek değil; triage, review, güvenilirlik ve dokümantasyon sorumluluğunu düzenli biçimde üstlenerek zamanla maintainer rolünü hak eden bir katkı geçmişi oluşturmak. İlk 60–90 günde 3–5 nitelikli merge, sürdürülebilir review katkısı ve en az bir çekirdek güvenilirlik iyileştirmesi hedefliyorum. Bu ritim faydalı olursa önce Triage, ardından Write/Maintain yetkisini birlikte değerlendirebiliriz.

Uygunsa ilk işi nightly sandbox hatası olarak alıp küçük bir PR ile başlayayım; sonrasında issue sıralamasını ve duyuru planını birlikte netleştirelim.

