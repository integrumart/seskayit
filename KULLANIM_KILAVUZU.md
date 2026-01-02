# Kullanım Kılavuzu (User Guide)

## Program Arayüzü

Ses Kayıt Edici programı açıldığında şu öğeleri göreceksiniz:

```
┌─────────────────────────────────────┐
│      🎤 Ses Kayıt Edici            │
│                                     │
│         Hazır                       │
│                                     │
│         00:00:00                    │
│                                     │
│  ┌──────────┐    ┌──────────┐     │
│  │⏺ Kaydı   │    │⏹ Kaydı   │     │
│  │  Başlat  │    │  Durdur  │     │
│  └──────────┘    └──────────┘     │
│                                     │
│ Kayıt formatı: WAV (44100 Hz, Stereo)│
└─────────────────────────────────────┘
```

### Arayüz Öğeleri

1. **Başlık**: Program adı
2. **Durum Etiketi**: Mevcut durum (Hazır, Kayıt yapılıyor, vb.)
3. **Süre Göstergesi**: Kayıt süresi (SS:DD:SS formatında)
4. **Kaydı Başlat Butonu**: Ses kaydını başlatır (Yeşil)
5. **Kaydı Durdur Butonu**: Ses kaydını durdurur (Kırmızı)
6. **Bilgi Etiketi**: Teknik bilgiler

## Temel Kullanım

### 1. Ses Kaydı Başlatma

1. **"⏺ Kaydı Başlat"** butonuna tıklayın
2. Durum "Kayıt yapılıyor..." olarak değişecek
3. Süre sayacı başlayacak (00:00:01, 00:00:02, ...)
4. Mikrofona konuşmaya başlayabilirsiniz

**Not:** Kayıt başladığında:
- "Kaydı Başlat" butonu devre dışı kalır
- "Kaydı Durdur" butonu aktif hale gelir
- Durum etiketi kırmızı renk olur

### 2. Ses Kaydını Durdurma

1. **"⏹ Kaydı Durdur"** butonuna tıklayın
2. Kayıt durur ve dosya kaydetme penceresi açılır
3. Kaydetmek istediğiniz konumu seçin
4. Dosya adı girin (varsayılan: kayit_YYYYMMDD_HHMMSS.wav)
5. **"Kaydet"** butonuna tıklayın

**Not:** Kayıt durdurulduğunda:
- Süre sayacı sıfırlanır
- Butonlar ilk durumlarına döner
- Durum "Hazır" olur

### 3. Dosya Kaydetme

Kayıt durdurulduğunda açılan pencerede:

- **Konum**: Kaydın kaydedileceği klasörü seçin
- **Dosya Adı**: İstediğiniz adı verin
- **Format**: .wav (otomatik eklenir)

Örnek dosya adları:
- `gorusme_2024.wav`
- `toplanti_notlari.wav`
- `muzik_kaydi.wav`

## İleri Seviye Özellikler

### Varsayılan Dosya Adı

Program otomatik olarak şu formatta dosya adı önerir:
```
kayit_YYYYMMDD_HHMMSS.wav
```

Örnek:
- `kayit_20240115_143052.wav` (15 Ocak 2024, 14:30:52)

### Kayıt Kalitesi

Program yüksek kaliteli ses kaydı yapar:
- **Sample Rate**: 44100 Hz (CD kalitesi)
- **Channels**: 2 (Stereo)
- **Bit Depth**: 16-bit
- **Format**: WAV (kayıpsız)

Bu ayarlar çoğu kullanım için idealdir ve değiştirilemez.

### Uzun Süreli Kayıtlar

Program teorik olarak sınırsız süre kayıt yapabilir, ancak:
- Disk alanı yeterli olmalıdır
- WAV dosyaları büyük olabilir (yaklaşık 10 MB/dakika)
- 2 GB'dan büyük dosyalar için 64-bit sistem önerilir

## Klavye Kısayolları

Program şu anda klavye kısayollarını desteklememektedir, ancak:
- `Tab` tuşu ile butonlar arasında geçiş yapabilirsiniz
- `Space` veya `Enter` ile seçili butona tıklayabilirsiniz

## Program Kapatma

### Normal Kapatma

Program çalışmıyorken:
- Pencereyi kapatma (X) butonuna tıklayın

### Kayıt Sırasında Kapatma

Kayıt devam ederken pencereyi kapatmaya çalışırsanız:
1. Bir uyarı mesajı görürsünüz
2. "Tamam" diyerek çıkabilirsiniz (kayıt kaybolur)
3. "İptal" diyerek programa geri dönebilirsiniz

## Sorun Giderme

### "Kayıt hatası: Mikrofon bulunamadı"

**Çözüm:**
1. Mikrofonun bilgisayara takılı olduğunu kontrol edin
2. Windows Ses Ayarları'ndan mikrofonu varsayılan cihaz olarak ayarlayın
3. Mikrofon izinlerini kontrol edin (Ayarlar > Gizlilik > Mikrofon)

### "Dosya kaydedilemedi"

**Çözüm:**
1. Yeterli disk alanı olduğundan emin olun
2. Klasör izinlerinizi kontrol edin
3. Dosya adında geçersiz karakterler kullanmadığınızdan emin olun
4. Başka bir konuma kaydetmeyi deneyin

### Program Yanıt Vermiyor

**Çözüm:**
1. Birkaç saniye bekleyin (uzun kayıtlar kaydederken donabilir)
2. Görev Yöneticisi'nden (Task Manager) programı kapatın
3. Programı yeniden başlatın

### Ses Kaydedilmiyor

**Çözüm:**
1. Mikrofonun ses seviyesini kontrol edin
2. Windows Ses Karıştırıcı'dan (Volume Mixer) mikrofon düzeyini artırın
3. Başka bir mikrofon deneyin
4. Ses sürücülerini güncelleyin

## İpuçları ve Püf Noktaları

### 1. Kaliteli Kayıt İçin
- Sessiz bir ortamda kayıt yapın
- Mikrofonu ağzınıza 15-30 cm uzaklıkta tutun
- Rüzgar ve klimadan uzak durun
- Kaliteli bir mikrofon kullanın

### 2. Dosya Yönetimi
- Kayıtları düzenli klasörlerde saklayın
- Anlamlı dosya adları kullanın
- Eski kayıtları arşivleyin veya silin
- Yedek almayı unutmayın

### 3. Performans
- Gereksiz programları kapatın
- Disk alanını düzenli kontrol edin
- Kayıt sırasında yoğun işlemlerden kaçının

### 4. Güvenlik
- Kayıtları şifrelenmiş disklerde saklayın
- Hassas kayıtları paylaşırken dikkatli olun
- Gereksiz kayıtları güvenli şekilde silin

## Teknik Bilgiler

### Sistem Gereksinimleri
- **İşletim Sistemi**: Windows 7/8/10/11
- **RAM**: Minimum 2 GB
- **Disk Alanı**: Kayıt süresine bağlı (10 MB/dakika)
- **Ses Kartı**: Mikrofon girişi olan herhangi bir ses kartı

### Dosya Formatı
- **Format**: WAV (Waveform Audio File Format)
- **Sıkıştırma**: Yok (kayıpsız)
- **Codec**: PCM (Pulse-Code Modulation)
- **Byte Order**: Little-endian

### Uyumluluk
Kaydedilen WAV dosyaları şu programlarla uyumludur:
- Windows Media Player
- VLC Media Player
- Audacity
- Adobe Audition
- Ve WAV destekleyen tüm programlar

## Sık Sorulan Sorular (SSS)

**S: Kayıtları MP3 formatında kaydedebilir miyim?**
C: Şu anda sadece WAV formatı desteklenmektedir. WAV dosyalarını sonradan Audacity gibi programlarla MP3'e çevirebilirsiniz.

**S: Maksimum kayıt süresi nedir?**
C: Teorik olarak sınır yoktur, ancak disk alanı ve sistem kaynakları sınırlayıcı faktörlerdir.

**S: Program arka planda çalışabilir mi?**
C: Hayır, program penceresi açık olmalıdır. Minimize edilebilir ama kapatılamaz.

**S: Birden fazla mikrofon kullanabilir miyim?**
C: Program Windows'ta varsayılan mikrofonu kullanır. Farklı mikrofon kullanmak için Windows ses ayarlarından varsayılan cihazı değiştirin.

**S: Program ne kadar disk alanı kullanır?**
C: Yaklaşık olarak dakika başına 10 MB (Stereo, 44100 Hz, 16-bit).

## Destek

Daha fazla yardım için:
- GitHub Issues: https://github.com/integrumart/seskayit/issues
- README dosyasını okuyun
- KURULUM_REHBERI.md dosyasına bakın

## Güncellemeler

Program güncellemeleri için:
- GitHub reposunu düzenli kontrol edin
- Yeni versiyonları indirip kurun
- Değişiklik notlarını okuyun
