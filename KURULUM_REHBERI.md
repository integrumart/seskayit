# Kurulum Rehberi (Installation Guide)

Bu dosya, Ses Kayıt Edici programının Windows için kurulum paketinin nasıl oluşturulacağını detaylı olarak açıklar.

## Önkoşullar

1. **Python 3.6 veya üzeri** yüklü olmalı
2. **pip** paket yöneticisi kurulu olmalı
3. **Windows işletim sistemi** (Windows 7, 8, 10 veya 11)

## Adım 1: Gerekli Paketleri Yükleme

### PyAudio Kurulumu

PyAudio, Windows'ta doğrudan pip ile kurulamayabilir. Aşağıdaki yöntemlerden birini kullanın:

#### Yöntem 1: pipwin ile (Önerilen)
```bash
pip install pipwin
pipwin install pyaudio
```

#### Yöntem 2: Önceden derlenmiş wheel dosyası ile
1. https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio adresinden sisteminize uygun .whl dosyasını indirin
2. İndirdiğiniz dosyayı yükleyin:
```bash
pip install PyAudio-0.2.11-cp39-cp39-win_amd64.whl
```
(Dosya adı Python versiyonunuza göre değişecektir)

### cx_Freeze Kurulumu

```bash
pip install cx_Freeze
```

## Adım 2: Executable Oluşturma

### Otomatik Build (Kolay Yol)

Windows'ta `build.bat` dosyasını çift tıklayarak çalıştırın:
```bash
build.bat
```

Bu script:
1. Gerekli bağımlılıkları yükler
2. Executable dosyasını oluşturur
3. MSI installer'ı oluşturur

### Manuel Build

#### Sadece Executable Oluşturma
```bash
python setup.py build
```

Oluşturulan dosyalar `build/` klasöründe olacaktır.

#### MSI Installer Oluşturma
```bash
python setup.py bdist_msi
```

Oluşturulan .msi dosyası `dist/` klasöründe olacaktır.

## Adım 3: Oluşturulan Dosyaları Test Etme

### Executable'ı Test Etme

1. `build/exe.win-amd64-3.x/` klasörüne gidin (x Python sürümünüze göre değişir)
2. `SesKayitEdici.exe` dosyasını çalıştırın
3. Programın düzgün açıldığını ve çalıştığını doğrulayın

### MSI Installer'ı Test Etme

1. `dist/` klasöründeki .msi dosyasını bulun
2. .msi dosyasını çift tıklayarak çalıştırın
3. Kurulum sihirbazını takip edin
4. Kurulum tamamlandıktan sonra programı başlatın

## Adım 4: Dağıtım

### Portable Executable Dağıtımı

`build/exe.win-amd64-3.x/` klasörünün tamamını:
1. Bir ZIP dosyasına sıkıştırın
2. Kullanıcılara dağıtın
3. Kullanıcılar ZIP'i açıp `SesKayitEdici.exe`'yi çalıştırabilirler

### Installer ile Dağıtım

`dist/` klasöründeki .msi dosyasını:
1. Kullanıcılara gönderin
2. Kullanıcılar .msi dosyasını çalıştırarak programı bilgisayarlarına kurabilirler

## Sorun Giderme

### PyAudio Kurulum Hatası

Eğer PyAudio kurulumu başarısız olursa:

1. Microsoft Visual C++ 14.0 veya üzeri gerekebilir
   - https://visualstudio.microsoft.com/downloads/ adresinden "Build Tools for Visual Studio" indirin

2. Alternatif olarak, önceden derlenmiş wheel dosyası kullanın (yukarıda belirtildiği gibi)

### cx_Freeze Build Hatası

Eğer build sırasında hata alırsanız:

1. Python versiyonunuzun güncel olduğundan emin olun
2. cx_Freeze'in en son versiyonunu yükleyin:
   ```bash
   pip install --upgrade cx_Freeze
   ```

### Missing DLL Hatası

Eğer executable çalıştırıldığında DLL hatası alınırsa:

1. `setup.py` dosyasında `include_files` listesine gerekli DLL'leri ekleyin
2. Build işlemini tekrarlayın

## Icon Ekleme

Programa icon eklemek için:

1. 256x256 boyutunda bir .ico dosyası oluşturun
2. Dosyayı `icon.ico` olarak proje klasörüne kaydedin
3. `setup.py` dosyasında şu satırı güncelleyin:
   ```python
   icon=None  # Bunu değiştirin
   ```
   şu şekilde:
   ```python
   icon="icon.ico"
   ```
4. Build işlemini tekrarlayın

## Dijital İmza Ekleme (İsteğe Bağlı)

Profesyonel dağıtım için dijital imza ekleyebilirsiniz:

1. Bir kod imzalama sertifikası edinin
2. `signtool.exe` kullanarak executable'ı imzalayın:
   ```bash
   signtool sign /f sertifika.pfx /p şifre /t http://timestamp.digicert.com SesKayitEdici.exe
   ```

## Lisans ve Dağıtım

Program GPL-3.0 lisansı altındadır. Dağıtırken:
- LICENSE dosyasını ekleyin
- Kaynak kodu sağlayın veya erişilebilir yapın
- Değişiklikleri belgelendirin

## Ek Kaynaklar

- cx_Freeze Dokümantasyonu: https://cx-freeze.readthedocs.io/
- PyAudio Dokümantasyonu: https://people.csail.mit.edu/hubert/pyaudio/
- Python Packaging: https://packaging.python.org/
