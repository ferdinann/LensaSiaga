# ❓ Frequently Asked Questions (FAQ)

Jawaban untuk pertanyaan yang sering diajukan tentang LensaSiaga.

---

## 📱 Umum

### Q: Apa itu LensaSiaga?
**A:** LensaSiaga adalah aplikasi deteksi bencana berbasis AI yang menggunakan Deep Learning untuk mengidentifikasi situasi darurat melalui analisis gambar. Aplikasi ini dapat mendeteksi bangunan runtuh, kebakaran, banjir, kecelakaan lalu lintas, dan kondisi normal.

### Q: Siapa yang bisa menggunakan LensaSiaga?
**A:** Siapa saja! LensaSiaga dirancang untuk:
- Tim SAR dan penanggulangan bencana
- Petugas keamanan dan keselamatan
- Jurnalis dan media
- Masyarakat umum
- Peneliti dan akademisi
- Pemerintah dan NGO

### Q: Apakah LensaSiaga gratis?
**A:** Ya, LensaSiaga adalah open-source dan gratis untuk digunakan di bawah lisensi MIT.

### Q: Apakah LensaSiaga tersedia dalam bahasa Indonesia?
**A:** Saat ini antarmuka sebagian besar dalam bahasa Indonesia dengan beberapa istilah teknis dalam bahasa Inggris. Multi-language support penuh akan ditambahkan di versi mendatang.

---

## 🔧 Instalasi & Setup

### Q: Apa saja yang dibutuhkan untuk menjalankan LensaSiaga?
**A:** Anda membutuhkan:
- Python 3.8 atau lebih tinggi
- File model (`mobilenet_final_model.h5`)
- File class names (`class_names.json`)
- Dependencies dari `requirements.txt`
- Koneksi internet (untuk download dependencies)

### Q: Bagaimana cara menginstall LensaSiaga?
**A:** Ikuti langkah berikut:
```bash
# 1. Clone/download repository
# 2. Install dependencies
pip install -r requirements.txt
# 3. Jalankan aplikasi
streamlit run app.py
```
Lihat **INSTALLATION.md** untuk panduan lengkap.

### Q: Mengapa muncul error saat install TensorFlow?
**A:** TensorFlow memiliki requirements spesifik:
- **Windows**: Pastikan menggunakan Python 64-bit
- **macOS M1/M2**: Gunakan `tensorflow-macos` dan `tensorflow-metal`
- **Linux**: Install dependencies sistem seperti `libhdf5`

Solusi:
```bash
# Reinstall dengan no-cache
pip install tensorflow==2.15.0 --no-cache-dir
```

### Q: Port 8501 sudah digunakan, bagaimana?
**A:** Gunakan port lain:
```bash
streamlit run app.py --server.port 8502
```

### Q: Aplikasi tidak terbuka di browser?
**A:** Buka manual di browser:
```
http://localhost:8501
```
Atau tambahkan flag:
```bash
streamlit run app.py --server.headless false
```

---

## 🤖 Model & Prediksi

### Q: Seberapa akurat model LensaSiaga?
**A:** Akurasi model bergantung pada:
- Kualitas gambar input
- Kondisi pencahayaan
- Angle pengambilan foto
- Similarity dengan training data

Model telah dilatih dengan dataset yang beragam, namun tidak 100% akurat. Selalu verifikasi dengan observasi langsung untuk keputusan kritis.

### Q: Kelas apa saja yang bisa dideteksi?
**A:** LensaSiaga dapat mendeteksi 5 kelas:
1. 🏚️ **Collapsed Building** - Bangunan runtuh
2. 🔥 **Fire** - Kebakaran
3. 🌊 **Flooded Areas** - Area banjir
4. 🚗 **Traffic Incident** - Kecelakaan lalu lintas
5. ✅ **Normal** - Kondisi normal

### Q: Berapa lama waktu prediksi?
**A:** Waktu prediksi berkisar:
- **Dengan GPU**: 1-2 detik
- **Tanpa GPU (CPU)**: 3-5 detik

First run akan lebih lama karena loading model.

### Q: Apa itu Confidence Score?
**A:** Confidence score adalah tingkat kepercayaan model terhadap prediksi, dalam bentuk persentase (0-100%). Semakin tinggi, semakin yakin model dengan prediksinya.

### Q: Minimum confidence berapa yang dianggap akurat?
**A:** Secara umum:
- **>80%**: Sangat yakin
- **60-80%**: Cukup yakin
- **40-60%**: Kurang yakin
- **<40%**: Tidak yakin

Namun, interpretasi tergantung pada use case spesifik.

### Q: Bisakah model salah prediksi?
**A:** Ya, seperti semua AI model, LensaSiaga bisa salah. Faktor yang mempengaruhi:
- Gambar blur atau gelap
- Objek terlalu jauh atau terlalu dekat
- Kondisi tidak umum
- Similarity visual antar kelas

Selalu gunakan penilaian manusia untuk keputusan final.

---

## 📸 Penggunaan

### Q: Format gambar apa yang didukung?
**A:** Format yang didukung:
- PNG (.png)
- JPEG (.jpg, .jpeg)
- Max size: 200MB

### Q: Resolusi gambar berpengaruh?
**A:** Ya, namun model akan auto-resize ke 224x224 pixels. Untuk hasil terbaik:
- Minimal 224x224 pixels
- Rekomendasi: 640x640 atau lebih
- Hindari gambar terlalu kecil (<100x100)

### Q: Apakah gambar saya disimpan?
**A:** Tidak permanen. Gambar hanya disimpan dalam session dan akan hilang saat:
- Anda menutup browser
- Session expired
- Anda clear history

LensaSiaga tidak mengirim gambar ke server eksternal atau cloud.

### Q: Bagaimana cara input koordinat GPS?
**A:** 
1. Masukkan Latitude (contoh: 3.5952)
2. Masukkan Longitude (contoh: 98.6722)
3. Atau gunakan GPS smartphone Anda
4. Click "Lihat di Maps" untuk verifikasi lokasi

### Q: GPS wajib diisi?
**A:** Tidak wajib. GPS bersifat opsional untuk tracking lokasi kejadian. Default location adalah Medan, North Sumatra.

---

## 📜 History & Data

### Q: Berapa lama history disimpan?
**A:** History disimpan selama session aktif. Akan hilang saat:
- Browser ditutup
- Tab ditutup
- Session timeout
- Manual clear history

### Q: Berapa maksimal history yang tersimpan?
**A:** Maksimal 50 entries. Jika melebihi, entry terlama akan otomatis terhapus.

### Q: Bagaimana cara export history?
**A:** Saat ini export history belum tersedia. Fitur ini akan ditambahkan di versi mendatang. Untuk sementara, Anda bisa screenshot atau copy-paste informasi.

### Q: Apakah history bisa di-restore setelah dihapus?
**A:** Tidak. Setelah Anda click "Hapus Semua History", data akan hilang permanen. Lakukan dengan hati-hati.

---

## 🔒 Keamanan & Privacy

### Q: Apakah data saya aman?
**A:** Ya. LensaSiaga:
- ✅ Tidak mengirim data ke server eksternal
- ✅ Semua processing dilakukan lokal
- ✅ Tidak menyimpan gambar permanen
- ✅ Tidak melakukan tracking user
- ✅ Open-source (kode bisa diaudit)

### Q: Apakah LensaSiaga menggunakan internet?
**A:** Internet hanya dibutuhkan untuk:
- Download dependencies (saat instalasi)
- Load Lottie animations
- Link ke Google Maps
- Fetch update (opsional)

Setelah terinstall, model berjalan offline (kecuali untuk fitur yang disebutkan).

### Q: Apakah LensaSiaga GDPR compliant?
**A:** Ya. LensaSiaga tidak mengumpulkan, menyimpan, atau membagikan data personal pengguna.

---

## 🛠️ Troubleshooting

### Q: Model file tidak ditemukan?
**A:** Pastikan:
1. File `mobilenet_final_model.h5` ada di folder yang sama dengan `app.py`
2. File tidak corrupt (download ulang jika perlu)
3. Permissions file sudah benar

### Q: Memory Error saat load model?
**A:** Model butuh minimal 2GB RAM. Solusi:
- Close aplikasi lain
- Restart komputer
- Upgrade RAM jika mungkin

### Q: Prediksi sangat lambat?
**A:** Penyebab umum:
- CPU lemah (tidak ada GPU)
- Background processes berat
- First run (load model)

Solusi:
- Gunakan GPU jika tersedia
- Close aplikasi lain
- Tunggu first run selesai

### Q: Upload gambar gagal?
**A:** Check:
- File size < 200MB
- Format: PNG, JPG, atau JPEG
- File tidak corrupt
- Browser support (update browser)

### Q: UI tidak tampil dengan baik?
**A:** Solusi:
- Clear browser cache
- Update browser ke versi terbaru
- Coba browser lain
- Disable browser extensions

---

## 🚀 Features & Roadmap

### Q: Bisakah deteksi dari video?
**A:** Belum. Fitur video detection planned untuk versi 1.1.0. Saat ini hanya support image.

### Q: Apakah ada mobile app?
**A:** Belum. Mobile app (React Native) dalam roadmap untuk versi 1.2.0.

### Q: Bisakah batch upload multiple images?
**A:** Belum. Fitur batch upload planned untuk versi 1.1.0.

### Q: Apakah bisa export report ke PDF?
**A:** Belum. Fitur export report planned untuk versi 1.1.0.

### Q: Kapan support bahasa lain?
**A:** Multi-language support (English, Indonesian) planned untuk versi 1.1.0.

---

## 👥 Kontribusi & Support

### Q: Bagaimana cara kontribusi?
**A:** Lihat **CONTRIBUTING.md** untuk panduan lengkap. Secara singkat:
1. Fork repository
2. Buat feature branch
3. Commit changes
4. Push ke fork
5. Create pull request

### Q: Menemukan bug, kemana report?
**A:** 
1. **GitHub Issues**: Create new issue
2. **Email**: support@lensasiaga.id
3. Include: screenshot, error message, steps to reproduce

### Q: Punya ide fitur baru?
**A:** Kami sangat welcome! Submit:
1. **GitHub Discussions**: Diskusi ide
2. **Feature Request**: Via GitHub Issues
3. **Email**: dev@lensasiaga.id

### Q: Bagaimana cara join development team?
**A:** 
1. Mulai dengan contribution (pull requests)
2. Active di community discussions
3. Consistent quality contributions
4. Core team akan invite aktif contributors

---

## 📞 Emergency

### Q: Ini emergency nyata, apa yang harus dilakukan?
**A:** **SEGERA HUBUNGI LAYANAN DARURAT:**
- 🚒 **Pemadam Kebakaran**: 113
- 🚑 **Ambulans**: 118 / 119
- 🚓 **Polisi**: 110
- 🆘 **BNPB**: 117

LensaSiaga adalah tool bantu, BUKAN pengganti layanan darurat profesional!

### Q: Model mendeteksi kebakaran tapi saya tidak lihat api?
**A:** 
1. **Double-check** kondisi aktual
2. Model bisa salah deteksi
3. Jika ragu, hubungi autoritas
4. Jangan abaikan tanda bahaya lain (asap, bau, dll)

### Q: Tingkat keparahan "KRITIS" berarti apa?
**A:** Keparahan levels:
- **KRITIS**: Bahaya immediate, perlu aksi SEGERA
- **DARURAT**: Situasi serius, perlu respons cepat
- **TINGGI**: Situasi berbahaya, perlu perhatian
- **SEDANG**: Perlu monitoring dan tindakan
- **AMAN**: Tidak ada bahaya terdeteksi

---

## 💡 Tips & Best Practices

### Q: Tips untuk hasil deteksi terbaik?
**A:**
1. ✅ Gunakan gambar jelas dan fokus
2. ✅ Pencahayaan cukup (tidak terlalu gelap/terang)
3. ✅ Angle yang menunjukkan situasi dengan jelas
4. ✅ Resolusi minimal 640x640
5. ✅ Hindari gambar blur atau motion blur
6. ✅ Zoom in pada area yang ingin dideteksi

### Q: Kapan sebaiknya menggunakan LensaSiaga?
**A:**
- ✅ Pra-assessment situasi darurat
- ✅ Dokumentasi kejadian
- ✅ Training dan simulasi
- ✅ Research dan analysis
- ✅ Quick screening area luas

Jangan gunakan sebagai satu-satunya basis untuk keputusan kritis!

---

## 📚 Resources

### Q: Dimana saya bisa belajar lebih lanjut?
**A:** Resources:
- 📖 **README.md**: Overview & getting started
- 🔧 **INSTALLATION.md**: Panduan instalasi detail
- 🌟 **FEATURES.md**: Dokumentasi fitur lengkap
- ⚡ **QUICKSTART.md**: Quick start guide
- 🤝 **CONTRIBUTING.md**: Panduan kontribusi
- 📝 **CHANGELOG.md**: Version history

### Q: Ada tutorial video?
**A:** Tutorial video planned untuk masa depan. Saat ini dokumentasi tertulis sudah comprehensive.

### Q: Bisa konsultasi untuk use case spesifik?
**A:** Ya! Kontak:
- 📧 Email: support@lensasiaga.id
- 💬 Discord: Join server kami
- 🐛 GitHub: Open discussion

---

## 🔄 Updates

### Q: Bagaimana cara update LensaSiaga?
**A:**
```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install -r requirements.txt --upgrade

# Restart application
streamlit run app.py
```

### Q: Seberapa sering ada update?
**A:** 
- **Major releases**: 2-3 bulan
- **Minor updates**: Monthly
- **Bug fixes**: As needed

Subscribe ke GitHub repository untuk notifications.

---

## 📞 Masih Punya Pertanyaan?

Hubungi kami:
- 📧 **Email**: support@lensasiaga.id
- 💬 **Discord**: [Join our server]
- 🐛 **GitHub**: [Open an issue]
- 🌐 **Website**: https://lensasiaga.id

**We're here to help! 🚨**

---

*Last Updated: 2026-01-28*

*FAQ akan di-update secara berkala berdasarkan pertanyaan yang masuk.*
