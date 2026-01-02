# Katkıda Bulunma Rehberi (Contributing Guide)

Ses Kayıt Edici projesine katkıda bulunmak istediğiniz için teşekkür ederiz! Bu rehber, projeye nasıl katkıda bulunabileceğinizi açıklar.

## 📋 İçindekiler

- [Davranış Kuralları](#davranış-kuralları)
- [Nasıl Katkıda Bulunabilirim?](#nasıl-katkıda-bulunabilirim)
- [Geliştirme Ortamı Kurulumu](#geliştirme-ortamı-kurulumu)
- [Pull Request Süreci](#pull-request-süreci)
- [Kod Standartları](#kod-standartları)
- [Commit Mesaj Kuralları](#commit-mesaj-kuralları)

## Davranış Kuralları

Bu projede herkes için saygılı ve yapıcı bir ortam sağlamayı hedefliyoruz. Lütfen:

- Saygılı ve profesyonel olun
- Yapıcı eleştiri yapın
- Farklı bakış açılarına açık olun
- Topluluk odaklı düşünün

## Nasıl Katkıda Bulunabilirim?

### 🐛 Hata Bildirimi

Bir hata buldunuz mu? Lütfen:

1. Önce [Issues](https://github.com/integrumart/seskayit/issues) bölümünde benzer bir hata bildirilmiş mi kontrol edin
2. Bulamadıysanız yeni bir issue açın
3. Hatayı detaylı açıklayın:
   - Ne yaptınız?
   - Ne bekliyordunuz?
   - Ne oldu?
   - Hata mesajları (varsa)
   - Sistem bilgileri (Windows versiyonu, Python versiyonu)

### 💡 Özellik Önerisi

Yeni bir özellik önermek ister misiniz?

1. [Issues](https://github.com/integrumart/seskayit/issues) bölümünde benzer bir öneri var mı kontrol edin
2. Yeni bir issue açın ve `enhancement` etiketi ekleyin
3. Özelliği detaylı açıklayın:
   - Ne yapmak istiyorsunuz?
   - Neden bu özellik yararlı olacak?
   - Nasıl çalışmalı?

### 📝 Dokümantasyon

Dokümantasyonu iyileştirmek için:

1. README, rehberler veya kod yorumlarında hata/eksik bulduysanız düzeltin
2. Yeni özellikler için dokümantasyon ekleyin
3. Örnekler ve açıklamalar ekleyin

### 💻 Kod Katkısı

Kod katkısı yapmak için aşağıdaki adımları izleyin.

## Geliştirme Ortamı Kurulumu

### 1. Repository'yi Fork Edin

GitHub'da projeyi fork edin ve yerel bilgisayarınıza klonlayın:

```bash
git clone https://github.com/KULLANICI_ADINIZ/seskayit.git
cd seskayit
```

### 2. Upstream Repository Ekleyin

```bash
git remote add upstream https://github.com/integrumart/seskayit.git
```

### 3. Geliştirme Ortamını Hazırlayın

```bash
# Virtual environment oluşturun (önerilen)
python -m venv venv
venv\Scripts\activate  # Windows

# Bağımlılıkları yükleyin
pip install -r requirements.txt
pip install cx_Freeze  # Build için gerekli
```

### 4. Geliştirme Branch'i Oluşturun

```bash
git checkout -b feature/yeni-ozellik
```

Branch isimlendirme:
- `feature/` - Yeni özellikler için
- `fix/` - Hata düzeltmeleri için
- `docs/` - Dokümantasyon için
- `refactor/` - Kod iyileştirmeleri için

## Pull Request Süreci

### 1. Değişikliklerinizi Yapın

- Küçük, odaklanmış değişiklikler yapın
- Her commit tek bir mantıksal değişiklik içermeli
- Kod standartlarına uyun

### 2. Test Edin

```bash
# Programı çalıştırın ve test edin
python seskayit.py

# Syntax kontrolü yapın
python -m py_compile seskayit.py

# Build test edin (opsiyonel)
python setup.py build
```

### 3. Commit Yapın

```bash
git add .
git commit -m "feat: yeni özellik eklendi"
```

### 4. Push Edin

```bash
git push origin feature/yeni-ozellik
```

### 5. Pull Request Oluşturun

1. GitHub'da fork'unuza gidin
2. "Pull Request" butonuna tıklayın
3. Değişikliklerinizi açıklayın:
   - Ne değiştirdiniz?
   - Neden değiştirdiniz?
   - Nasıl test ettiniz?
4. "Create Pull Request" butonuna tıklayın

### 6. İnceleme Süreci

- Maintainer'lar PR'ınızı inceleyecek
- Gerekirse değişiklik isteyebilirler
- Onaylandıktan sonra merge edilecek

## Kod Standartları

### Python Stil Kuralları

- [PEP 8](https://pep8.org/) stil rehberine uyun
- Fonksiyon ve değişken isimleri Türkçe olabilir (kullanıcı arayüzü için)
- Kod yorumları Türkçe veya İngilizce olabilir

### Kod Formatı

```python
# İyi örnek
def kayit_baslat(self):
    """Ses kaydını başlatır."""
    self.recording = True
    self.start_time = datetime.datetime.now()
    
# Kötü örnek
def kayit_baslat(self):
    self.recording=True
    self.start_time=datetime.datetime.now()
```

### İsimlendirme

- **Sınıflar**: PascalCase (ör. `SesKayitEdici`)
- **Fonksiyonlar**: snake_case (ör. `start_recording`)
- **Değişkenler**: snake_case (ör. `recording_status`)
- **Sabitler**: UPPER_CASE (ör. `MAX_DURATION`)

### Yorumlar

```python
# İyi - Açıklayıcı yorum
# Kayıt thread'ini başlat ve ses verilerini topla
self.record_thread = threading.Thread(target=self.record_audio)

# Kötü - Gereksiz yorum
# Thread başlat
self.record_thread = threading.Thread(target=self.record_audio)
```

## Commit Mesaj Kuralları

### Format

```
tip: kısa açıklama

Detaylı açıklama (opsiyonel)
```

### Commit Tipleri

- `feat`: Yeni özellik
- `fix`: Hata düzeltme
- `docs`: Dokümantasyon değişikliği
- `style`: Kod formatı (logic değişikliği yok)
- `refactor`: Kod iyileştirme
- `test`: Test ekleme/düzeltme
- `chore`: Build, konfigürasyon vb.

### Örnekler

```bash
# İyi örnekler
git commit -m "feat: MP3 format desteği eklendi"
git commit -m "fix: mikrofon bulunamama hatası düzeltildi"
git commit -m "docs: KURULUM_REHBERI.md güncellendi"

# Kötü örnekler
git commit -m "değişiklikler"
git commit -m "bug fix"
git commit -m "update"
```

## Özel Durumlar

### Büyük Değişiklikler

Büyük değişiklikler için:

1. Önce bir issue açın ve tartışın
2. Maintainer'lardan onay alın
3. Değişikliği küçük PR'lara bölün (mümkünse)

### Breaking Changes

Geriye uyumsuz değişiklikler için:

1. Issue'da ve PR'da açıkça belirtin
2. Migration rehberi ekleyin
3. CHANGELOG.md'de MAJOR version bump gerektiğini belirtin

### Güvenlik Açıkları

Güvenlik açığı buldunuz mu?

1. **Public issue açmayın**
2. Doğrudan maintainer'lara ulaşın
3. Detaylı açıklama gönderin

## Test Etme

### Manuel Test

- Programı başlatın ve tüm özellikleri test edin
- Farklı senaryoları deneyin
- Hata mesajlarını kontrol edin

### Syntax Test

```bash
python -m py_compile seskayit.py
```

### Build Test

```bash
python setup.py build
# Oluşturulan .exe'yi test edin
```

## Sorularınız mı Var?

- Issue açın ve `question` etiketi ekleyin
- Maintainer'lara ulaşın
- Dokümantasyonu okuyun

## Teşekkürler!

Katkılarınız için teşekkür ederiz! Her katkı, büyük veya küçük, projeyi daha iyi hale getirir.
