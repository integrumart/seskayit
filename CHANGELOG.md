# Değişiklik Günlüğü (Changelog)

Ses Kayıt Edici projesinin tüm önemli değişiklikleri bu dosyada belgelenecektir.

Format [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) standardına dayanmaktadır,
ve bu proje [Semantic Versioning](https://semver.org/spec/v2.0.0.html) kullanmaktadır.

## [1.0.0] - 2024-01-02

### Eklenenler
- İlk versiyon yayınlandı
- Temel ses kayıt fonksiyonu
- Tkinter tabanlı grafik kullanıcı arayüzü
- Başlat/Durdur butonları
- Kayıt süresi göstergesi (SS:DD:SS formatında)
- Durum göstergeleri (Hazır, Kayıt yapılıyor, vb.)
- WAV formatında yüksek kaliteli ses kaydı (44100 Hz, Stereo, 16-bit)
- Dosya kaydetme dialog penceresi
- Otomatik dosya adı önerisi (timestamp ile)
- Kapanış onay dialog'u (kayıt devam ederken)
- cx_Freeze ile Windows executable desteği
- MSI installer oluşturma desteği
- Otomatik build script (build.bat)
- Kolay çalıştırma script'i (run.bat)
- Türkçe kullanıcı arayüzü
- Türkçe dokümantasyon

### Dokümantasyon
- README.md - Genel bilgi ve hızlı başlangıç
- KURULUM_REHBERI.md - Detaylı kurulum ve build talimatları
- KULLANIM_KILAVUZU.md - Kapsamlı kullanım kılavuzu
- ICON_INFO.md - Icon ekleme rehberi
- LICENSE - GPL-3.0 lisans dosyası

### Teknik Detaylar
- Python 3.6+ desteği
- PyAudio kütüphanesi ile ses kaydı
- Threading ile arkaplan kayıt işlemi
- Wave modülü ile WAV dosyası oluşturma
- Tkinter ile platform-bağımsız GUI (Windows odaklı)

## [Gelecek] - Planlanıyor

### Planlanan Özellikler
- [ ] MP3 format desteği
- [ ] OGG/Vorbis format desteği
- [ ] Ses seviyesi göstergesi (VU meter)
- [ ] Kayıt duraklatma özelliği
- [ ] Ses kalitesi ayarları (sample rate seçimi)
- [ ] Mikrofon seçim menüsü
- [ ] Klavye kısayolları
- [ ] Otomatik kayıt başlatma
- [ ] Zamanlayıcı ile kayıt
- [ ] Ses efektleri (normalize, gürültü azaltma)
- [ ] Karanlık tema desteği
- [ ] Çoklu dil desteği (İngilizce, vb.)
- [ ] Sistem tray icon'u
- [ ] Ses görselleştirme (waveform)
- [ ] Otomatik güncelleme kontrolü

### Geliştirmeler
- [ ] Daha iyi hata yönetimi
- [ ] Performans optimizasyonları
- [ ] Bellek kullanımı iyileştirmeleri
- [ ] Daha detaylı log kayıtları
- [ ] Birim testleri
- [ ] Entegrasyon testleri

### Hata Düzeltmeleri
- Henüz bilinen bir hata bulunmamaktadır

---

## Versiyon Notasyonu

Proje [Semantic Versioning](https://semver.org/) kullanır:
- **MAJOR**: Geriye uyumsuz API değişiklikleri
- **MINOR**: Geriye uyumlu yeni özellikler
- **PATCH**: Geriye uyumlu hata düzeltmeleri

## Kategori Açıklamaları

- **Eklenenler**: Yeni özellikler
- **Değiştirilenler**: Mevcut fonksiyonlarda değişiklikler
- **Kullanımdan Kaldırılanlar**: Yakında kaldırılacak özellikler
- **Kaldırılanlar**: Kaldırılan özellikler
- **Düzeltilenler**: Hata düzeltmeleri
- **Güvenlik**: Güvenlik açıkları için düzeltmeler
