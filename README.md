# 🎤 Ses Kayıt Edici (Audio Recorder)

Basit bir Windows ses kayıt edici programı. Python ve Tkinter kullanılarak geliştirilmiştir.

## 📋 Özellikler

- 🎙️ Yüksek kaliteli ses kaydı (44100 Hz, Stereo)
- 🖥️ Kullanıcı dostu grafik arayüz
- ⏱️ Kayıt süresi göstergesi
- 💾 WAV formatında kayıt
- 🚀 Windows executable (setup.exe) ile kolay kurulum

## 🔧 Kurulum

### Metod 1: Windows Executable (Önerilen)

1. `dist` klasöründen `setup.exe` dosyasını çalıştırın
2. Kurulum sihirbazını takip edin
3. Program otomatik olarak bilgisayarınıza kurulacaktır

### Metod 2: Python ile Çalıştırma

#### Gereksinimler
- Python 3.6 veya üzeri
- PyAudio kütüphanesi

#### Adımlar

1. Repoyu klonlayın:
```bash
git clone https://github.com/integrumart/seskayit.git
cd seskayit
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

**Not:** PyAudio kurulumu için Windows'ta `pipwin` kullanabilirsiniz:
```bash
pip install pipwin
pipwin install pyaudio
```

3. Programı çalıştırın:
```bash
python seskayit.py
```

## 📦 Windows Executable Oluşturma

Windows için .exe dosyası oluşturmak için:

1. cx_Freeze'i yükleyin:
```bash
pip install cx_Freeze
```

2. Setup script'i çalıştırın:
```bash
python setup.py build
```

3. Oluşturulan executable `build` klasöründe bulunacaktır.

### MSI Installer Oluşturma

Windows installer (.msi) oluşturmak için:

```bash
python setup.py bdist_msi
```

Oluşturulan .msi dosyası `dist` klasöründe bulunacaktır.

## 🎯 Kullanım

1. Programı başlatın
2. **"⏺ Kaydı Başlat"** butonuna tıklayarak kayda başlayın
3. Mikrofona konuşun veya ses kaydı yapın
4. **"⏹ Kaydı Durdur"** butonuna tıklayarak kaydı durdurun
5. Açılan pencereden kaydetmek istediğiniz konumu ve dosya adını seçin
6. Kayıt .wav formatında kaydedilecektir

## 🛠️ Teknik Detaylar

- **Format:** WAV (Waveform Audio File Format)
- **Sample Rate:** 44100 Hz
- **Channels:** 2 (Stereo)
- **Bit Depth:** 16-bit
- **GUI Framework:** Tkinter
- **Audio Library:** PyAudio

## 📝 Notlar

- Programın çalışması için bilgisayarınızda mikrofon bulunması gerekmektedir
- Mikrofon izinlerinin aktif olduğundan emin olun
- WAV dosyaları sıkıştırılmamış format olduğu için büyük boyutlu olabilir

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje GPL-3.0 lisansı altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

## 👤 Yazar

**integrumart**

## 🐛 Sorun Bildirme

Bir hata veya öneri için lütfen [Issues](https://github.com/integrumart/seskayit/issues) bölümünden bildirebilirsiniz.
