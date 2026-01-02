# Örnek Konfigürasyon (Example Configuration)

Bu dosya, `seskayit.py` dosyasında yapılabilecek özelleştirmeleri gösterir.

## Ses Kalitesi Ayarları

`seskayit.py` dosyasında, `__init__` metodunda aşağıdaki değerleri değiştirebilirsiniz:

### Düşük Kalite (Daha Az Disk Alanı)
```python
self.CHUNK = 1024
self.FORMAT = pyaudio.paInt16
self.CHANNELS = 1          # Mono
self.RATE = 22050          # 22.05 kHz
```

Disk kullanımı: ~5 MB/dakika

### Orta Kalite (Varsayılan)
```python
self.CHUNK = 1024
self.FORMAT = pyaudio.paInt16
self.CHANNELS = 2          # Stereo
self.RATE = 44100          # 44.1 kHz (CD kalitesi)
```

Disk kullanımı: ~10 MB/dakika

### Yüksek Kalite (Stüdyo Kalitesi)
```python
self.CHUNK = 1024
self.FORMAT = pyaudio.paInt24  # 24-bit
self.CHANNELS = 2              # Stereo
self.RATE = 96000              # 96 kHz
```

Disk kullanımı: ~34 MB/dakika

## Pencere Boyutu

```python
self.root.geometry("400x300")  # Genişlik x Yükseklik
```

Örnek boyutlar:
- Küçük: "350x250"
- Orta (varsayılan): "400x300"
- Büyük: "500x400"

## Pencere Ayarları

```python
# Pencereyi yeniden boyutlandırma
self.root.resizable(True, True)  # Genişlik, Yükseklik

# Her zaman üstte
self.root.attributes('-topmost', True)

# Tam ekran başlangıç
self.root.state('zoomed')
```

## Renk Temaları

### Koyu Tema
```python
# Arka plan
self.root.configure(bg='#2c3e50')

# Başlık
title_label = tk.Label(
    self.root,
    text="🎤 Ses Kayıt Edici",
    font=("Arial", 18, "bold"),
    fg="#ecf0f1",  # Açık renk
    bg="#2c3e50"   # Koyu arka plan
)

# Durum etiketi
self.status_label = tk.Label(
    self.root,
    text="Hazır",
    font=("Arial", 12),
    fg="#2ecc71",  # Yeşil
    bg="#2c3e50"
)
```

### Açık Tema (Varsayılan)
Mevcut kod açık tema kullanmaktadır.

## Buton Stilleri

### Daha Büyük Butonlar
```python
self.start_button = tk.Button(
    button_frame,
    text="⏺ Kaydı Başlat",
    command=self.start_recording,
    bg="#27ae60",
    fg="white",
    font=("Arial", 14, "bold"),  # Daha büyük font
    width=18,                     # Daha geniş
    height=3,                     # Daha yüksek
    cursor="hand2"
)
```

## Varsayılan Kayıt Konumu

```python
import os

def save_recording(self):
    # Belgeler klasörüne kaydet
    default_dir = os.path.join(os.path.expanduser("~"), "Documents", "Kayıtlar")
    
    # Klasör yoksa oluştur
    if not os.path.exists(default_dir):
        os.makedirs(default_dir)
    
    # Varsayılan dosya adı
    default_filename = f"kayit_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
    default_path = os.path.join(default_dir, default_filename)
    
    # Dosya kaydetme dialogu
    filename = filedialog.asksaveasfilename(
        initialdir=default_dir,  # Başlangıç klasörü
        initialfile=default_filename,
        defaultextension=".wav",
        filetypes=[("WAV dosyası", "*.wav"), ("Tüm dosyalar", "*.*")]
    )
```

## Maksimum Kayıt Süresi

```python
import time

def start_recording(self):
    self.recording = True
    self.frames = []
    self.start_time = datetime.datetime.now()
    self.max_duration = 3600  # 1 saat (saniye cinsinden)
    
    # ... diğer kod ...
    
def record_audio(self):
    self.p = pyaudio.PyAudio()
    
    try:
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        
        while self.recording:
            # Maksimum süre kontrolü
            elapsed = (datetime.datetime.now() - self.start_time).total_seconds()
            if elapsed >= self.max_duration:
                self.recording = False
                self.root.after(0, lambda: messagebox.showinfo(
                    "Bilgi",
                    "Maksimum kayıt süresine ulaşıldı."
                ))
                break
            
            data = self.stream.read(self.CHUNK)
            self.frames.append(data)
```

## Otomatik Kayıt Başlatma

```python
def __init__(self, root):
    # ... diğer kod ...
    
    # Arayüzü oluştur
    self.setup_ui()
    
    # Otomatik olarak kaydı başlat
    # self.root.after(1000, self.start_recording)  # 1 saniye sonra
```

## Keyboard Shortcuts (Klavye Kısayolları)

```python
def setup_ui(self):
    # ... diğer kod ...
    
    # Klavye bağlantıları
    self.root.bind('<Control-r>', lambda e: self.start_recording())
    self.root.bind('<Control-s>', lambda e: self.stop_recording())
    self.root.bind('<Escape>', lambda e: self.on_closing())
```

Kısayollar:
- `Ctrl+R`: Kaydı başlat
- `Ctrl+S`: Kaydı durdur
- `Esc`: Programı kapat

## Ses Seviyesi Kontrolü

```python
import audioop

def record_audio(self):
    # ... diğer kod ...
    
    while self.recording:
        data = self.stream.read(self.CHUNK)
        self.frames.append(data)
        
        # Ses seviyesini hesapla
        rms = audioop.rms(data, 2)  # 2 = 16-bit
        db = 20 * math.log10(rms) if rms > 0 else 0
        
        # Ses seviyesini göster (main thread'de)
        self.root.after(0, lambda: self.update_volume_meter(db))
```

## Notlar

- Bu değişiklikler için `seskayit.py` dosyasını düzenlemeniz gerekir
- Değişiklik yaptıktan sonra programı yeniden çalıştırın
- Build ettiyseniz, yeniden build etmeniz gerekir
- Büyük değişiklikler yapmadan önce yedek alın

## Gelişmiş Kullanım

Daha gelişmiş özelleştirmeler için Python ve Tkinter dokümantasyonuna bakın:
- Python Tkinter: https://docs.python.org/3/library/tkinter.html
- PyAudio: https://people.csail.mit.edu/hubert/pyaudio/docs/
