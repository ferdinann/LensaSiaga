# ⚡ Quick Start Guide - LensaSiaga

Panduan singkat untuk langsung menggunakan LensaSiaga dalam 5 menit!

---

## 🚀 3 Langkah Cepat

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Jalankan Aplikasi
```bash
streamlit run app.py
```

### 3️⃣ Buka Browser
```
http://localhost:8501
```

**Selesai! 🎉**

---

## 📸 Cara Menggunakan

### Upload & Deteksi
1. Klik area upload atau drag & drop gambar
2. (Opsional) Masukkan koordinat GPS
3. Klik tombol **"🔬 Analisis Gambar"**
4. Lihat hasil deteksi

### Lihat History
1. Klik tab **"📜 History Scan"**
2. Expand entry untuk detail
3. Klik **"🗑️ Hapus Semua History"** untuk clear

---

## 🎯 Format Gambar yang Didukung
- ✅ PNG (.png)
- ✅ JPEG (.jpg, .jpeg)
- ✅ Max size: 200MB

---

## 📊 5 Kelas Deteksi

| Icon | Kelas | Severity |
|------|-------|----------|
| 🏚️ | Collapsed Building | KRITIS |
| 🔥 | Fire | DARURAT |
| 🌊 | Flooded Areas | TINGGI |
| 🚗 | Traffic Incident | SEDANG |
| ✅ | Normal | AMAN |

---

## 🆘 Nomor Darurat

- 🚒 **Pemadam Kebakaran**: 113
- 🚑 **Ambulans**: 118 / 119
- 🚓 **Polisi**: 110
- 🆘 **BNPB**: 117

---

## 💡 Tips

✨ **Tip 1**: Gunakan gambar yang jelas dan fokus
✨ **Tip 2**: Pastikan pencahayaan cukup
✨ **Tip 3**: Hindari gambar blur atau terlalu gelap
✨ **Tip 4**: Foto dari angle yang menunjukkan situasi
✨ **Tip 5**: Input GPS untuk tracking lokasi

---

## ⚠️ Troubleshooting Cepat

### Aplikasi Tidak Jalan?
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Port 8501 Sudah Dipakai?
```bash
# Gunakan port lain
streamlit run app.py --server.port 8502
```

### Model File Not Found?
Pastikan file ada:
- `mobilenet_final_model.h5`
- `class_names.json`

### Error TensorFlow?
```bash
# Install ulang TensorFlow
pip install tensorflow==2.15.0 --no-cache-dir
```

---

## 📚 Dokumentasi Lengkap

Untuk informasi detail, baca:
- 📖 **README.md** - Overview & features
- 🔧 **INSTALLATION.md** - Panduan instalasi lengkap
- 🌟 **FEATURES.md** - Detail semua fitur

---

## 🤝 Butuh Bantuan?

- 📧 Email: support@lensasiaga.id
- 🐛 GitHub Issues: Report bugs
- 💬 Community: Join our Discord

---

## 🎉 Selamat Menggunakan!

**LensaSiaga siap membantu deteksi bencana Anda!**

🚨 *Deteksi Cepat, Respons Tepat* 🚨

---

**Pro Tip**: Bookmark localhost:8501 untuk akses cepat! 🔖
