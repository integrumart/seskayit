# 🚀 Hızlı Başlangıç (Quick Start)

Bu dosya, Ses Kayıt Edici programını hızlıca başlatmanız için en temel adımları içerir.

## Windows Kullanıcıları İçin (Önerilen)

### Kurulumdan Sonra:

1. **Programı Başlatın**
   - Başlat menüsünden "Ses Kayıt Edici" veya "SesKayitEdici" uygulamasını bulun
   - Masaüstü kısayoluna tıklayın (varsa)

2. **Kayıt Yapın**
   ```
   ⏺ Kaydı Başlat → Konuşun → ⏹ Kaydı Durdur → Dosyayı Kaydedin
   ```

3. **Kaydınızı Bulun**
   - Seçtiğiniz klasörde `.wav` dosyası olarak kaydedilmiştir
   - Windows Media Player ile açabilirsiniz

## Geliştiriciler İçin

### Hızlı Kurulum:

```bash
# 1. Repoyu klonlayın
git clone https://github.com/integrumart/seskayit.git
cd seskayit

# 2. PyAudio'yu yükleyin (Windows)
pip install pipwin
pipwin install pyaudio

# 3. Programı çalıştırın
python seskayit.py
```

veya Windows'ta:
```bash
run.bat
```

### Executable Oluşturma:

```bash
# 1. cx_Freeze'i yükleyin
pip install cx_Freeze

# 2. Build edin
python setup.py build

# veya otomatik:
build.bat
```

## Sorun mu Yaşıyorsunuz?

### Mikrofon Çalışmıyor
1. Windows Ayarları → Gizlilik → Mikrofon
2. Mikrofon erişimini açın
3. Programı yeniden başlatın

### PyAudio Kurulamıyor
```bash
pip install pipwin
pipwin install pyaudio
```

### Program Açılmıyor
- Python 3.6+ yüklü olduğundan emin olun
- Bağımlılıkları yeniden yükleyin: `pip install -r requirements.txt`

## Daha Fazla Bilgi

- **Detaylı Kurulum**: [KURULUM_REHBERI.md](KURULUM_REHBERI.md)
- **Kullanım Kılavuzu**: [KULLANIM_KILAVUZU.md](KULLANIM_KILAVUZU.md)
- **Katkıda Bulunma**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Genel Bilgi**: [README.md](README.md)

## İletişim

Sorunlar için: https://github.com/integrumart/seskayit/issues

---

**Not:** Bu program sadece Windows işletim sisteminde çalışır. Linux/Mac desteği henüz bulunmamaktadır.
