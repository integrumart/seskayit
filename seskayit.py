"""
Ses Kayıt Edici (Audio Recorder)
Basit bir Windows ses kayıt edici programı
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pyaudio
import wave
import threading
import datetime
import os

class SesKayitEdici:
    def __init__(self, root):
        self.root = root
        self.root.title("Ses Kayıt Edici")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        
        # Kayıt ayarları
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        
        # Durum değişkenleri
        self.recording = False
        self.frames = []
        self.p = None
        self.stream = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Kullanıcı arayüzünü oluştur"""
        # Başlık
        title_label = tk.Label(
            self.root, 
            text="🎤 Ses Kayıt Edici", 
            font=("Arial", 18, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=20)
        
        # Durum etiketi
        self.status_label = tk.Label(
            self.root, 
            text="Hazır", 
            font=("Arial", 12),
            fg="#27ae60"
        )
        self.status_label.pack(pady=10)
        
        # Süre etiketi
        self.time_label = tk.Label(
            self.root,
            text="00:00:00",
            font=("Arial", 16, "bold"),
            fg="#3498db"
        )
        self.time_label.pack(pady=10)
        
        # Butonlar frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # Kayıt başlat butonu
        self.start_button = tk.Button(
            button_frame,
            text="⏺ Kaydı Başlat",
            command=self.start_recording,
            bg="#27ae60",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2,
            cursor="hand2"
        )
        self.start_button.grid(row=0, column=0, padx=5)
        
        # Kayıt durdur butonu
        self.stop_button = tk.Button(
            button_frame,
            text="⏹ Kaydı Durdur",
            command=self.stop_recording,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 12, "bold"),
            width=15,
            height=2,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.stop_button.grid(row=0, column=1, padx=5)
        
        # Bilgi etiketi
        info_label = tk.Label(
            self.root,
            text="Kayıt formatı: WAV (44100 Hz, Stereo)",
            font=("Arial", 8),
            fg="#7f8c8d"
        )
        info_label.pack(side=tk.BOTTOM, pady=10)
        
    def start_recording(self):
        """Ses kaydını başlat"""
        self.recording = True
        self.frames = []
        self.start_time = datetime.datetime.now()
        
        # Buton durumlarını güncelle
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Kayıt yapılıyor...", fg="#e74c3c")
        
        # Kayıt thread'ini başlat
        self.record_thread = threading.Thread(target=self.record_audio)
        self.record_thread.start()
        
        # Süreyi güncelle
        self.update_time()
        
    def record_audio(self):
        """Ses kaydetme işlemi"""
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
                data = self.stream.read(self.CHUNK)
                self.frames.append(data)
                
        except Exception as e:
            self.recording = False
            self.root.after(0, lambda: messagebox.showerror(
                "Hata", 
                f"Kayıt hatası: {str(e)}\n\nMikrofon bağlı olduğundan emin olun."
            ))
        
    def update_time(self):
        """Kayıt süresini güncelle"""
        if self.recording:
            elapsed = datetime.datetime.now() - self.start_time
            hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)
            self.root.after(1000, self.update_time)
        
    def stop_recording(self):
        """Ses kaydını durdur ve kaydet"""
        self.recording = False
        
        # Stream'i kapat
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if self.p:
            self.p.terminate()
        
        # Buton durumlarını güncelle
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Kayıt tamamlandı", fg="#27ae60")
        
        # Dosyayı kaydet
        self.save_recording()
        
        # Süreyi sıfırla
        self.time_label.config(text="00:00:00")
        
    def save_recording(self):
        """Kaydedilen sesi dosyaya kaydet"""
        if not self.frames:
            messagebox.showwarning("Uyarı", "Kaydedilecek ses bulunamadı!")
            return
        
        # Varsayılan dosya adı
        default_filename = f"kayit_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        
        # Dosya kaydetme dialogu
        filename = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("WAV dosyası", "*.wav"), ("Tüm dosyalar", "*.*")],
            initialfile=default_filename
        )
        
        if filename:
            try:
                # WAV dosyası oluştur
                wf = wave.open(filename, 'wb')
                wf.setnchannels(self.CHANNELS)
                wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
                wf.setframerate(self.RATE)
                wf.writeframes(b''.join(self.frames))
                wf.close()
                
                messagebox.showinfo(
                    "Başarılı", 
                    f"Kayıt başarıyla kaydedildi:\n{filename}"
                )
                self.status_label.config(text="Hazır", fg="#27ae60")
            except Exception as e:
                messagebox.showerror(
                    "Hata", 
                    f"Dosya kaydedilemedi: {str(e)}"
                )
        else:
            self.status_label.config(text="Kayıt iptal edildi", fg="#e67e22")
            
    def on_closing(self):
        """Pencere kapatılırken"""
        if self.recording:
            if messagebox.askokcancel("Çıkış", "Kayıt devam ediyor. Çıkmak istediğinizden emin misiniz?"):
                self.recording = False
                if self.stream:
                    self.stream.stop_stream()
                    self.stream.close()
                if self.p:
                    self.p.terminate()
                self.root.destroy()
        else:
            self.root.destroy()

def main():
    """Ana program"""
    root = tk.Tk()
    app = SesKayitEdici(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
