# 📥 Panduan Instalasi LensaSiaga

Panduan lengkap untuk instalasi dan menjalankan aplikasi LensaSiaga di berbagai platform.

## 📋 Prasyarat Sistem

### Minimum Requirements
- **OS**: Windows 10/11, macOS 10.14+, atau Linux (Ubuntu 18.04+)
- **Python**: 3.8, 3.9, 3.10, atau 3.11
- **RAM**: Minimal 4GB (Rekomendasi 8GB)
- **Storage**: Minimal 2GB free space
- **Internet**: Diperlukan untuk download dependencies

### Software yang Dibutuhkan
- Python 3.8+ dengan pip
- Git (opsional, untuk clone repository)
- Text editor atau IDE (VSCode, PyCharm, dll)

---

## 🪟 Instalasi di Windows

### 1. Install Python

Download Python dari [python.org](https://www.python.org/downloads/)

**Penting**: Centang "Add Python to PATH" saat instalasi!

Verifikasi instalasi:
```cmd
python --version
pip --version
```

### 2. Download Project

**Opsi A: Menggunakan Git**
```cmd
git clone <repository-url>
cd lensasiaga
```

**Opsi B: Download ZIP**
- Download ZIP dari GitHub
- Extract ke folder pilihan Anda
- Buka Command Prompt di folder tersebut

### 3. Install Dependencies

```cmd
pip install -r requirements.txt
```

### 4. Siapkan Model Files

Copy file berikut ke folder project:
- `mobilenet_final_model.h5`
- `class_names.json`

### 5. Jalankan Aplikasi

```cmd
streamlit run app.py
```

Atau gunakan script otomatis:
```cmd
run.bat
```

### 6. Akses Aplikasi

Buka browser dan kunjungi: `http://localhost:8501`

---

## 🍎 Instalasi di macOS

### 1. Install Python

**Menggunakan Homebrew (Recommended)**
```bash
# Install Homebrew jika belum ada
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11
```

**Atau download dari** [python.org](https://www.python.org/downloads/macos/)

Verifikasi:
```bash
python3 --version
pip3 --version
```

### 2. Download Project

```bash
git clone <repository-url>
cd lensasiaga
```

### 3. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Siapkan Model Files

Copy file model ke folder project:
```bash
cp /path/to/mobilenet_final_model.h5 .
cp /path/to/class_names.json .
```

### 5. Jalankan Aplikasi

```bash
chmod +x run.sh
./run.sh
```

Atau langsung:
```bash
streamlit run app.py
```

---

## 🐧 Instalasi di Linux (Ubuntu/Debian)

### 1. Update System

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install Python dan pip

```bash
sudo apt install python3 python3-pip python3-venv -y
```

Verifikasi:
```bash
python3 --version
pip3 --version
```

### 3. Install Git (jika belum ada)

```bash
sudo apt install git -y
```

### 4. Clone Project

```bash
git clone <repository-url>
cd lensasiaga
```

### 5. (Opsional) Buat Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 6. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 7. Siapkan Model Files

```bash
cp /path/to/mobilenet_final_model.h5 .
cp /path/to/class_names.json .
```

### 8. Jalankan Aplikasi

```bash
chmod +x run.sh
./run.sh
```

---

## 🐳 Instalasi dengan Docker (Advanced)

### 1. Buat Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

### 2. Build Image

```bash
docker build -t lensasiaga .
```

### 3. Run Container

```bash
docker run -p 8501:8501 lensasiaga
```

---

## 🔧 Troubleshooting

### Problem: "pip is not recognized"

**Windows:**
```cmd
python -m pip install -r requirements.txt
```

**macOS/Linux:**
```bash
python3 -m pip install -r requirements.txt
```

### Problem: TensorFlow Installation Error

Jika terjadi error saat install TensorFlow:

**Windows:**
```cmd
pip install tensorflow==2.15.0 --no-cache-dir
```

**macOS (Apple Silicon):**
```bash
pip install tensorflow-macos==2.15.0
pip install tensorflow-metal==1.1.0
```

**Linux:**
```bash
pip3 install tensorflow==2.15.0
```

### Problem: Port 8501 Already in Use

Gunakan port lain:
```bash
streamlit run app.py --server.port 8502
```

### Problem: Model File Not Found

Pastikan file berada di direktori yang benar:
```bash
ls -la | grep -E "mobilenet|class_names"
```

### Problem: Module Not Found Error

Reinstall dependencies:
```bash
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

### Problem: Streamlit Not Opening in Browser

Buka manual di browser:
```
http://localhost:8501
```

Atau coba:
```bash
streamlit run app.py --server.headless true
```

---

## 🔐 Security Best Practices

1. **Jangan commit model files ke Git** (tambahkan ke .gitignore)
2. **Gunakan virtual environment** untuk isolasi dependencies
3. **Update dependencies secara berkala** untuk security patches
4. **Jangan expose aplikasi ke public tanpa authentication**

---

## 📊 Verifikasi Instalasi

Setelah instalasi, jalankan test berikut:

### 1. Check Python
```bash
python --version  # atau python3 --version
```
Expected: Python 3.8.x atau lebih tinggi

### 2. Check Dependencies
```bash
pip list
```
Pastikan semua package dari requirements.txt terinstall

### 3. Check Model Files
```bash
ls -lh mobilenet_final_model.h5 class_names.json
```
Pastikan kedua file ada dan ukurannya normal

### 4. Test Run
```bash
streamlit run app.py
```
Aplikasi seharusnya terbuka di browser

---

## 🚀 Quick Start Commands

### Windows
```cmd
# One-liner installation
python -m pip install -r requirements.txt && streamlit run app.py
```

### macOS/Linux
```bash
# One-liner installation
pip3 install -r requirements.txt && streamlit run app.py
```

---

## 📞 Bantuan Lebih Lanjut

Jika mengalami masalah:

1. **Cek Dokumentasi**: Baca README.md dengan teliti
2. **Search Error Message**: Google error message yang muncul
3. **GitHub Issues**: Buat issue di repository
4. **Email Support**: support@lensasiaga.id
5. **Community Forum**: Bergabung dengan komunitas user

---

## 📝 Catatan Penting

- **GPU Support**: TensorFlow akan otomatis menggunakan GPU jika tersedia
- **RAM Usage**: Aplikasi membutuhkan ~500MB - 2GB RAM
- **First Run**: First run akan lebih lama karena loading model
- **Updates**: Selalu pull update terbaru dari repository

---

## ✅ Checklist Instalasi

- [ ] Python 3.8+ terinstall
- [ ] pip terinstall dan ter-update
- [ ] Dependencies terinstall
- [ ] Model files tersedia
- [ ] Aplikasi berjalan tanpa error
- [ ] Browser dapat akses localhost:8501
- [ ] Upload gambar berfungsi
- [ ] Prediksi berjalan normal

---

**Selamat! LensaSiaga siap digunakan! 🎉**

Untuk panduan penggunaan, lihat README.md

---

*Last Updated: 2026-01-28*
