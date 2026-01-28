import os

os.environ["TF_USE_LEGACY_KERAS"] = "1"

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import json
import time
from datetime import datetime
import base64
from pathlib import Path
import pandas as pd
from streamlit_lottie import st_lottie
import requests

# ==================== KONFIGURASI HALAMAN ====================
st.set_page_config(
    page_title="LensaSiaga - Deteksi Bencana AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM CSS ====================
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Bebas+Neue&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Dark Mode Support */
    @media (prefers-color-scheme: dark) {
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #16213e 100%);
        }
    }
    
    /* Header Styling */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, rgba(255,0,0,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 2px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        animation: fadeInDown 1s ease-in-out;
    }
    
    .main-header h1 {
        font-family: 'Bebas Neue', cursive;
        font-size: 4rem;
        color: #fff;
        text-shadow: 0 0 20px rgba(255,0,0,0.5), 0 0 40px rgba(255,0,0,0.3);
        margin: 0;
        letter-spacing: 5px;
    }
    
    .main-header p {
        color: #e0e0e0;
        font-size: 1.2rem;
        margin-top: 0.5rem;
        font-weight: 300;
    }
    
    /* Card Styling */
    .info-card {
        background: rgba(255,255,255,0.05);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    
    .info-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(255,0,0,0.2);
        border-color: rgba(255,0,0,0.3);
    }
    
    /* Button Styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,0,0,0.3);
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255,0,0,0.5);
        background: linear-gradient(135deg, #cc0000 0%, #990000 100%);
    }
    
    /* Result Card */
    .result-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 2px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        animation: fadeIn 0.8s ease-in-out;
    }
    
    .result-card h3 {
        color: #fff;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #ff0000 0%, #ff6b6b 100%);
    }
    
    /* Sidebar Styling */
    .css-1d391kg {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Upload Area */
    .uploadedFile {
        border: 2px dashed rgba(255,0,0,0.5);
        border-radius: 15px;
        padding: 1rem;
        background: rgba(255,255,255,0.02);
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Alert Box */
    .alert-box {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-weight: 500;
        animation: fadeIn 0.5s ease-in-out;
    }
    
    .alert-danger {
        background: rgba(255,0,0,0.15);
        border-left: 4px solid #ff0000;
        color: #ffcccc;
    }
    
    .alert-warning {
        background: rgba(255,165,0,0.15);
        border-left: 4px solid #ffa500;
        color: #ffd699;
    }
    
    .alert-success {
        background: rgba(0,255,0,0.15);
        border-left: 4px solid #00ff00;
        color: #ccffcc;
    }
    
    .alert-info {
        background: rgba(0,150,255,0.15);
        border-left: 4px solid #0096ff;
        color: #cce7ff;
    }
    
    /* Image Container */
    .image-container {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        border: 2px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
    }
    
    .image-container:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 60px rgba(255,0,0,0.3);
    }
    
    /* Metric Cards */
    .metric-card {
        background: rgba(255,255,255,0.05);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #ff0000;
        text-shadow: 0 0 10px rgba(255,0,0,0.5);
    }
    
    .metric-label {
        color: #b0b0b0;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    
    /* History Table */
    .history-table {
        background: rgba(255,255,255,0.05);
        border-radius: 10px;
        overflow: hidden;
    }
    
    /* GPS Info */
    .gps-info {
        background: linear-gradient(135deg, rgba(0,150,255,0.1) 0%, rgba(0,100,200,0.05) 100%);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border: 1px solid rgba(0,150,255,0.3);
    }
    
    /* Confidence Bar */
    .confidence-bar {
        height: 25px;
        border-radius: 15px;
        background: rgba(255,255,255,0.1);
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .confidence-fill {
        height: 100%;
        background: linear-gradient(90deg, #ff0000 0%, #ff6b6b 100%);
        border-radius: 15px;
        transition: width 1s ease-in-out;
        box-shadow: 0 0 15px rgba(255,0,0,0.5);
    }
    
    /* Explanation Box */
    .explanation-box {
        background: rgba(255,255,255,0.08);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #0096ff;
        backdrop-filter: blur(10px);
    }
    
    .explanation-box h4 {
        color: #0096ff;
        margin-bottom: 1rem;
        font-size: 1.3rem;
    }
    
    .explanation-box p {
        color: #e0e0e0;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== FUNGSI LOTTIE ====================
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ==================== FUNGSI LOAD MODEL ====================
@st.cache_resource
def load_model_file():
    model_path = 'mobilenet_final_model.keras'
    try:
        # Gunakan safe_mode=False untuk mengatasi masalah input tensor ganda
        model = tf.keras.models.load_model(
            model_path, 
            compile=False, 
            safe_mode=False 
        )
        return model
    except Exception as e:
        # Jika masih gagal, gunakan pemuatan layer-by-layer
        st.error(f"❌ Masalah Struktur Model: {e}")
        return None

@st.cache_data
def load_class_names():
    try:
        with open('class_names.json', 'r') as f:
            data = json.load(f)
        return data['class_names']
    except Exception as e:
        st.error(f"Error loading class names: {e}")
        return []

# ==================== FUNGSI PREPROCESSING ====================
def preprocess_image(image):
    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ==================== FUNGSI PREDIKSI ====================
def predict_image(model, image, class_names):
    processed_img = preprocess_image(image)
    
    # Simulasi progress
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    
    predictions = model.predict(processed_img, verbose=0)
    predicted_class_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][predicted_class_idx]) * 100
    predicted_class = class_names[predicted_class_idx]
    
    return predicted_class, confidence, predictions[0]

# ==================== FUNGSI PENJELASAN ====================
def get_explanation(class_name):
    explanations = {
        "collapsed_building": {
            "title": "🏚️ Bangunan Runtuh Terdeteksi",
            "description": "Sistem mendeteksi adanya struktur bangunan yang mengalami keruntuhan atau kerusakan struktural parah. Kondisi ini menunjukkan bahwa telah terjadi bencana yang mengakibatkan kehancuran infrastruktur.",
            "details": [
                "• Keruntuhan struktural total atau parsial",
                "• Puing-puing dan material bangunan berserakan",
                "• Potensi korban tertimbun tinggi",
                "• Memerlukan tim SAR dan alat berat"
            ],
            "severity": "KRITIS"
        },
        "fire": {
            "title": "🔥 Kebakaran Terdeteksi",
            "description": "Sistem mendeteksi adanya api atau asap yang mengindikasikan terjadinya kebakaran. Situasi ini memerlukan respons cepat untuk mencegah penyebaran api dan menyelamatkan korban.",
            "details": [
                "• Api aktif atau asap tebal terlihat",
                "• Potensi penyebaran cepat",
                "• Risiko korban luka bakar atau sesak napas",
                "• Memerlukan pemadam kebakaran segera"
            ],
            "severity": "DARURAT"
        },
        "flooded_areas": {
            "title": "🌊 Area Banjir Terdeteksi",
            "description": "Sistem mendeteksi adanya genangan air atau banjir yang menutupi area permukaan. Kondisi ini mengindikasikan terjadinya banjir yang dapat membahayakan keselamatan dan kesehatan masyarakat.",
            "details": [
                "• Genangan air yang luas",
                "• Potensi arus deras di beberapa area",
                "• Risiko penyakit waterborne",
                "• Memerlukan evakuasi dan perahu karet"
            ],
            "severity": "TINGGI"
        },
        "traffic_incident": {
            "title": "🚗 Insiden Lalu Lintas Terdeteksi",
            "description": "Sistem mendeteksi adanya kecelakaan atau insiden lalu lintas. Situasi ini memerlukan bantuan medis dan pengaturan lalu lintas untuk menghindari kecelakaan sekunder.",
            "details": [
                "• Kecelakaan kendaraan bermotor",
                "• Kemungkinan ada korban luka",
                "• Kemacetan lalu lintas",
                "• Memerlukan ambulans dan polisi lalu lintas"
            ],
            "severity": "SEDANG"
        },
        "normal": {
            "title": "✅ Kondisi Normal",
            "description": "Sistem mendeteksi kondisi yang normal tanpa tanda-tanda bencana atau keadaan darurat. Area aman dan tidak memerlukan intervensi khusus.",
            "details": [
                "• Tidak ada tanda bahaya",
                "• Kondisi lingkungan stabil",
                "• Aktivitas normal berlangsung",
                "• Tidak memerlukan tindakan darurat"
            ],
            "severity": "AMAN"
        }
    }
    return explanations.get(class_name, {})

# ==================== FUNGSI SARAN TINDAKAN ====================
def get_action_suggestions(class_name):
    suggestions = {
        "collapsed_building": [
            "🚨 Hubungi tim SAR (Search and Rescue) segera",
            "⚠️ Jauhi area runtuhan untuk menghindari reruntuhan susulan",
            "📢 Periksa keberadaan korban dengan hati-hati",
            "🏥 Siapkan fasilitas medis darurat",
            "🔦 Gunakan alat deteksi kehidupan jika tersedia",
            "📞 Koordinasikan dengan BNPB/BPBD setempat"
        ],
        "fire": [
            "🚒 Hubungi pemadam kebakaran (113) SEGERA",
            "🏃 Evakuasi area dengan cepat dan tertib",
            "💨 Tutup hidung dan mulut dengan kain basah",
            "🚪 Jangan gunakan lift, gunakan tangga darurat",
            "🔥 Jangan kembali ke area kebakaran",
            "🏥 Berikan pertolongan pertama untuk korban"
        ],
        "flooded_areas": [
            "🚨 Evakuasi ke tempat tinggi segera",
            "⚠️ Hindari berjalan di air yang mengalir",
            "💡 Matikan listrik di area terdampak",
            "🚫 Jangan gunakan kendaraan bermotor",
            "🏥 Waspadai penyakit terkait air",
            "📞 Hubungi tim SAR jika terisolasi"
        ],
        "traffic_incident": [
            "🚑 Hubungi ambulans (118/119) jika ada korban",
            "🚓 Laporkan ke polisi (110)",
            "⚠️ Pasang segitiga pengaman",
            "🩹 Berikan pertolongan pertama jika memungkinkan",
            "📸 Dokumentasikan kondisi untuk keperluan asuransi",
            "🚦 Atur lalu lintas untuk mencegah kecelakaan susulan"
        ],
        "normal": [
            "✅ Kondisi aman, tidak ada tindakan darurat diperlukan",
            "📱 Tetap waspada dan pantau situasi sekitar",
            "🔔 Pastikan sistem peringatan dini aktif",
            "📚 Tingkatkan pengetahuan kesiapsiagaan bencana",
            "🤝 Koordinasi dengan komunitas lokal"
        ]
    }
    return suggestions.get(class_name, [])

# ==================== FUNGSI HISTORY ====================
def save_to_history(image, predicted_class, confidence, latitude, longitude):
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    # Simpan gambar sebagai base64
    import io
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    history_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "class": predicted_class,
        "confidence": confidence,
        "latitude": latitude,
        "longitude": longitude,
        "image": img_str
    }
    
    st.session_state.history.insert(0, history_entry)
    
    # Batasi history maksimal 50 entri
    if len(st.session_state.history) > 50:
        st.session_state.history = st.session_state.history[:50]

def clear_history():
    st.session_state.history = []

# ==================== FUNGSI SEVERITAS ====================
def get_severity_color(severity):
    colors = {
        "KRITIS": "#dc3545",
        "DARURAT": "#fd7e14",
        "TINGGI": "#ffc107",
        "SEDANG": "#0096ff",
        "AMAN": "#28a745"
    }
    return colors.get(severity, "#6c757d")

# ==================== MAIN APP ====================
def main():
    load_css()
    
    # Header
    st.markdown("""
        <div class="main-header">
            <h1>🚨 LENSASIAGA 🚨</h1>
            <p>Sistem Deteksi Bencana Berbasis AI untuk Kesiapsiagaan Darurat</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        # Lottie Animation
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_9wpyhdzo.json"
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=200, key="sidebar_animation")
        
        st.markdown("## 📱 Tentang LensaSiaga")
        st.info("""
        **LensaSiaga** adalah sistem deteksi bencana berbasis Deep Learning yang menggunakan MobileNet untuk mengidentifikasi:
        
        - 🏚️ Bangunan Runtuh
        - 🔥 Kebakaran
        - 🌊 Banjir
        - 🚗 Kecelakaan Lalu Lintas
        - ✅ Kondisi Normal
        """)
        
        st.markdown("## 📋 Cara Penggunaan")
        st.markdown("""
        1. 📤 Upload foto situasi darurat
        2. 📍 Masukkan koordinat GPS (opsional)
        3. 🔍 Klik tombol "Analisis Gambar"
        4. 📊 Lihat hasil deteksi dan saran tindakan
        5. 📜 Cek history scan di tab History
        """)
        
        st.markdown("## 👨‍💻 Pengembang")
        st.markdown("""
        **Tim LensaSiaga**
        
        Dikembangkan dengan ❤️ untuk meningkatkan kesiapsiagaan bencana di Indonesia.
        
        🔗 [GitHub](https://github.com) | 📧 support@lensasiaga.id
        """)
        
        st.markdown("---")
        st.caption("© 2026 LensaSiaga. All rights reserved.")
    
    # Tab Navigation
    tab1, tab2 = st.tabs(["🔍 Deteksi Bencana", "📜 History Scan"])
    
    with tab1:
        # Load model
        model = load_model_file()
        class_names = load_class_names()
        
        if model is None or not class_names:
            st.error("❌ Gagal memuat model atau class names!")
            return
        
        # Layout dengan columns
        col1, col2 = st.columns([1, 1], gap="large")
        
        with col1:
            st.markdown("### 📤 Upload Gambar")
            uploaded_file = st.file_uploader(
                "Pilih gambar untuk dianalisis",
                type=['png', 'jpg', 'jpeg'],
                help="Upload foto situasi yang ingin dideteksi"
            )
            
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.markdown('<div class="image-container">', unsafe_allow_html=True)
                st.image(image, caption="Gambar yang diupload", use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            # GPS Coordinates
            st.markdown("### 📍 Koordinat Lokasi (Opsional)")
            col_lat, col_lon = st.columns(2)
            with col_lat:
                latitude = st.number_input(
                    "Latitude",
                    value=3.5952,
                    format="%.6f",
                    help="Koordinat lintang lokasi"
                )
            with col_lon:
                longitude = st.number_input(
                    "Longitude",
                    value=98.6722,
                    format="%.6f",
                    help="Koordinat bujur lokasi"
                )
            
            # Tombol Analisis
            analyze_button = st.button("🔬 Analisis Gambar", use_container_width=True)
        
        with col2:
            if uploaded_file is not None and analyze_button:
                with st.spinner("🔄 Memproses gambar..."):
                    # Prediksi
                    predicted_class, confidence, all_predictions = predict_image(
                        model, image, class_names
                    )
                    
                    # Simpan ke history
                    save_to_history(image, predicted_class, confidence, latitude, longitude)
                    
                    # Dapatkan penjelasan
                    explanation = get_explanation(predicted_class)
                    severity = explanation.get("severity", "AMAN")
                    severity_color = get_severity_color(severity)
                    
                    # Tampilkan hasil
                    st.markdown(f"""
                        <div class="result-card">
                            <h3 style="color: {severity_color};">📊 HASIL DETEKSI</h3>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Metrics
                    metric_col1, metric_col2 = st.columns(2)
                    with metric_col1:
                        st.markdown(f"""
                            <div class="metric-card">
                                <div class="metric-value">{predicted_class.replace('_', ' ').title()}</div>
                                <div class="metric-label">Kelas Terdeteksi</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    with metric_col2:
                        st.markdown(f"""
                            <div class="metric-card">
                                <div class="metric-value">{confidence:.1f}%</div>
                                <div class="metric-label">Tingkat Kepercayaan</div>
                            </div>
                        """, unsafe_allow_html=True)
                    
                    # Confidence Bar
                    st.markdown("#### 📈 Confidence Score")
                    st.markdown(f"""
                        <div class="confidence-bar">
                            <div class="confidence-fill" style="width: {confidence}%;"></div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # GPS Info
                    st.markdown(f"""
                        <div class="gps-info">
                            <strong>📍 Lokasi Deteksi:</strong><br>
                            Latitude: {latitude:.6f}<br>
                            Longitude: {longitude:.6f}<br>
                            <a href="https://www.google.com/maps?q={latitude},{longitude}" target="_blank">
                                🗺️ Lihat di Google Maps
                            </a>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Tingkat Keparahan
                    severity_class = "alert-danger" if severity in ["KRITIS", "DARURAT"] else \
                                   "alert-warning" if severity in ["TINGGI", "SEDANG"] else "alert-success"
                    
                    st.markdown(f"""
                        <div class="alert-box {severity_class}">
                            <strong>⚠️ Tingkat Keparahan: {severity}</strong>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Penjelasan Hasil
                    if explanation:
                        st.markdown(f"""
                            <div class="explanation-box">
                                <h4>💡 Penjelasan Hasil Deteksi</h4>
                                <p><strong>{explanation['title']}</strong></p>
                                <p>{explanation['description']}</p>
                                <h5 style="color: #0096ff; margin-top: 1rem;">Karakteristik yang Terdeteksi:</h5>
                        """, unsafe_allow_html=True)
                        
                        for detail in explanation['details']:
                            st.markdown(f"<p style='margin: 0.3rem 0; color: #e0e0e0;'>{detail}</p>", unsafe_allow_html=True)
                        
                        st.markdown("</div>", unsafe_allow_html=True)
                    
                    # Saran Tindakan
                    st.markdown("### 🎯 Saran Tindakan")
                    suggestions = get_action_suggestions(predicted_class)
                    for suggestion in suggestions:
                        st.markdown(f"""
                            <div class="info-card">
                                {suggestion}
                            </div>
                        """, unsafe_allow_html=True)
                    
                    # Distribusi Prediksi
                    st.markdown("### 📊 Distribusi Probabilitas Semua Kelas")
                    chart_data = pd.DataFrame({
                        'Kelas': [name.replace('_', ' ').title() for name in class_names],
                        'Probabilitas (%)': all_predictions * 100
                    })
                    st.bar_chart(chart_data.set_index('Kelas'))
    
    with tab2:
        st.markdown("### 📜 History Scan")
        
        if 'history' not in st.session_state or len(st.session_state.history) == 0:
            st.info("Belum ada history scan. Silakan lakukan scan terlebih dahulu.")
        else:
            # Tombol clear history
            col_btn1, col_btn2, col_btn3 = st.columns([2, 1, 2])
            with col_btn2:
                if st.button("🗑️ Hapus Semua History", use_container_width=True):
                    clear_history()
                    st.rerun()
            
            st.markdown(f"**Total Scan: {len(st.session_state.history)}**")
            
            # Tampilkan history
            for idx, entry in enumerate(st.session_state.history):
                with st.expander(f"🔍 Scan #{idx+1} - {entry['timestamp']} - {entry['class'].replace('_', ' ').title()}"):
                    hist_col1, hist_col2 = st.columns([1, 2])
                    
                    with hist_col1:
                        # Decode dan tampilkan gambar
                        img_data = base64.b64decode(entry['image'])
                        img = Image.open(io.BytesIO(img_data))
                        st.image(img, use_container_width=True)
                    
                    with hist_col2:
                        st.markdown(f"""
                            **🕒 Waktu:** {entry['timestamp']}
                            
                            **📊 Kelas:** {entry['class'].replace('_', ' ').title()}
                            
                            **💯 Confidence:** {entry['confidence']:.2f}%
                            
                            **📍 Lokasi:**
                            - Latitude: {entry['latitude']:.6f}
                            - Longitude: {entry['longitude']:.6f}
                            
                            [🗺️ Lihat di Maps](https://www.google.com/maps?q={entry['latitude']},{entry['longitude']})
                        """)
                        
                        # Progress bar untuk confidence
                        st.progress(entry['confidence'] / 100)

if __name__ == "__main__":
    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    main()
