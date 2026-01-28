# 🚨 LensaSiaga - Sistem Deteksi Bencana Berbasis AI

![LensaSiaga Banner](https://img.shields.io/badge/LensaSiaga-AI%20Disaster%20Detection-red?style=for-the-badge&logo=tensorflow)

## 📋 Deskripsi

**LensaSiaga** adalah aplikasi deteksi bencana berbasis kecerdasan buatan (AI) yang menggunakan model Deep Learning MobileNet untuk mengidentifikasi situasi darurat secara otomatis melalui analisis gambar. Aplikasi ini dirancang untuk meningkatkan kesiapsiagaan dan respons cepat terhadap bencana.

### ✨ Fitur Utama

- 🤖 **Deteksi AI Real-time** - Menggunakan MobileNet untuk klasifikasi gambar
- 📍 **GPS Tracking** - Mencatat lokasi koordinat setiap deteksi
- 📜 **History Management** - Menyimpan riwayat scan dengan kemampuan hapus
- 💡 **Penjelasan Hasil** - Memberikan penjelasan detail untuk setiap hasil deteksi
- 🎯 **Saran Tindakan** - Rekomendasi langkah-langkah yang harus diambil
- 🎨 **Modern UI/UX** - Interface yang modern dengan dark mode support
- 📊 **Visualisasi Data** - Grafik dan progress bar yang informatif
- 🎭 **Lottie Animations** - Animasi menarik untuk meningkatkan user experience

## 🎯 Kelas Deteksi

Aplikasi ini dapat mendeteksi 5 kategori situasi:

1. 🏚️ **Collapsed Building** (Bangunan Runtuh) - KRITIS
2. 🔥 **Fire** (Kebakaran) - DARURAT
3. 🌊 **Flooded Areas** (Area Banjir) - TINGGI
4. 🚗 **Traffic Incident** (Kecelakaan Lalu Lintas) - SEDANG
5. ✅ **Normal** (Kondisi Normal) - AMAN

## 🚀 Instalasi

### Prasyarat

- Python 3.8 - 3.11
- pip (Python package manager)
- Model file: `mobilenet_final_model.h5`
- Class names file: `class_names.json`

### Langkah Instalasi

1. **Clone atau Download Repository**
```bash
git clone <repository-url>
cd lensasiaga
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Pastikan File Model Ada**

Letakkan file berikut di direktori yang sama dengan `app.py`:
- `mobilenet_final_model.h5`
- `class_names.json`

4. **Jalankan Aplikasi**
```bash
streamlit run app.py
```

5. **Akses Aplikasi**

Buka browser dan akses: `http://localhost:8501`

## 📖 Cara Penggunaan

### 1. Upload Gambar
- Klik area upload atau drag & drop gambar
- Format yang didukung: PNG, JPG, JPEG

### 2. Input Koordinat GPS (Opsional)
- Masukkan Latitude dan Longitude lokasi
- Default: Medan, North Sumatra (3.5952, 98.6722)

### 3. Analisis Gambar
- Klik tombol "🔬 Analisis Gambar"
- Tunggu proses analisis selesai

### 4. Lihat Hasil
- Hasil deteksi akan ditampilkan dengan:
  - Kelas yang terdeteksi
  - Tingkat kepercayaan (confidence score)
  - Tingkat keparahan (severity level)
  - Lokasi GPS dengan link Google Maps
  - Penjelasan detail hasil deteksi
  - Saran tindakan yang harus diambil
  - Distribusi probabilitas semua kelas

### 5. Cek History
- Pindah ke tab "📜 History Scan"
- Lihat semua riwayat scan sebelumnya
- Hapus history jika diperlukan

## 🎨 Fitur Desain

### Visual Highlights

- **Dark Theme** - Gradient background dengan glassmorphism effect
- **Custom Fonts** - Poppins dan Bebas Neue untuk tampilan modern
- **Animations** - Smooth transitions dan hover effects
- **Lottie Integration** - Animated icons untuk sidebar
- **Responsive Layout** - Adaptif untuk berbagai ukuran layar
- **Color-Coded Alerts** - Warna berbeda sesuai tingkat keparahan

### Severity Color Scheme

| Severity | Color | Hex Code |
|----------|-------|----------|
| KRITIS | Red | #dc3545 |
| DARURAT | Orange | #fd7e14 |
| TINGGI | Yellow | #ffc107 |
| SEDANG | Blue | #0096ff |
| AMAN | Green | #28a745 |

## 🛠️ Struktur File

```
lensasiaga/
│
├── app.py                      # File utama aplikasi
├── requirements.txt            # Dependencies
├── README.md                   # Dokumentasi
├── mobilenet_final_model.h5    # Model TensorFlow (tidak termasuk)
└── class_names.json            # Konfigurasi kelas (tidak termasuk)
```

## 📊 Teknologi yang Digunakan

- **Streamlit** - Framework untuk web application
- **TensorFlow/Keras** - Deep Learning framework
- **MobileNet** - Pre-trained CNN model
- **Pillow (PIL)** - Image processing
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Streamlit-Lottie** - Animated icons
- **Requests** - HTTP library

## 🔧 Konfigurasi

### Model Configuration

File `class_names.json` harus berisi:
```json
{
  "class_names": [
    "collapsed_building",
    "fire",
    "flooded_areas",
    "normal",
    "traffic_incident"
  ],
  "num_classes": 5,
  "image_size": [224, 224]
}
```

### Preprocessing

- Input size: 224x224 pixels
- Normalization: 1/255.0
- Color space: RGB

## 🎯 Contoh Penggunaan

### Deteksi Kebakaran
1. Upload foto yang menunjukkan api atau asap
2. Input koordinat lokasi kebakaran
3. Sistem akan mendeteksi "Fire" dengan confidence score
4. Saran tindakan akan ditampilkan (hubungi pemadam kebakaran, evakuasi, dll)

### Deteksi Banjir
1. Upload foto area yang tergenang
2. Masukkan koordinat lokasi banjir
3. Sistem mendeteksi "Flooded Areas"
4. Rekomendasi tindakan evakuasi akan muncul

## ⚠️ Peringatan

- Model AI memiliki batasan dan tidak 100% akurat
- Selalu verifikasi dengan observasi langsung
- Gunakan sebagai alat bantu, bukan pengganti penilaian manusia
- Untuk situasi darurat nyata, hubungi layanan darurat resmi:
  - 🚒 Pemadam Kebakaran: 113
  - 🚑 Ambulans: 118/119
  - 🚓 Polisi: 110
  - 🆘 BNPB: 117

## 🤝 Kontribusi

Kami menerima kontribusi dari komunitas! Berikut cara berkontribusi:

1. Fork repository ini
2. Buat branch baru (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail.

## 👥 Tim Pengembang

**LensaSiaga Development Team**

Dikembangkan dengan ❤️ untuk meningkatkan kesiapsiagaan bencana di Indonesia.

## 📧 Kontak

- Email: support@lensasiaga.id
- Website: https://lensasiaga.id
- GitHub: https://github.com/lensasiaga

## 🙏 Acknowledgments

- TensorFlow Team untuk framework machine learning
- Streamlit Team untuk web framework yang luar biasa
- LottieFiles untuk animasi gratis
- Komunitas open source yang telah berkontribusi

## 📈 Roadmap

- [ ] Integrasi dengan API cuaca
- [ ] Notifikasi real-time via Telegram/WhatsApp
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Integration dengan sistem peringatan dini nasional
- [ ] Live video stream analysis
- [ ] Crowdsourcing data untuk training model

## 🐛 Bug Reports

Jika menemukan bug, silakan buat issue di GitHub dengan informasi:
- Deskripsi bug
- Langkah-langkah untuk reproduce
- Screenshot (jika memungkinkan)
- Environment details (OS, Python version, dll)

---

**Dibuat dengan ❤️ untuk Indonesia yang lebih siap menghadapi bencana**

*"Deteksi Cepat, Respons Tepat"*

🚨 **LensaSiaga** - Your AI-Powered Disaster Detection System
