import streamlit as st
import time

# ==============================================================================
# 1. KONFIGURASI HALAMAN (Harus diletakkan di baris paling atas)
# ==============================================================================
st.set_page_config(
    page_title="OrganicChem | Edu-Lab Platform",
    page_icon="🧪",
    layout="wide"
)

# ==============================================================================
# 2. CUSTOM CSS INTERAKTIF
# ==============================================================================
st.markdown("""
    <style>
    /* Desain Kotak Hasil Analisis yang Unik & Modern */
    .kotak-analisis {
        border-left: 6px solid #2ecc71;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f5fbf7;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
    }
    .label-analisis {
        font-weight: bold;
        color: #27ae60;
        font-size: 1.15em;
        margin-bottom: 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    /* Desain Banner Gradasi untuk Halaman Utama */
    .banner-utama {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        padding: 35px;
        border-radius: 12px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(56, 239, 125, 0.2);
    }
    /* Card Khusus Materi Bab */
    .card-materi {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e6ebf4;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. SIDEBAR NAVIGASI
# ==============================================================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022607.png", width=75)
    st.title("OrganicChem v1.0")
    st.write("🔬 *E-Learning & Lab Simulator*")
    st.markdown("---")
    
    pilihan_halaman = st.radio(
        "Navigasi Menu:",
        [
            "🏠 HALAMAN UTAMA", 
            "📘 BAB 1 HIDROKARBON", 
            "📙 BAB 2 ALKOHOL, ETER, DAN FENOL", 
            "📗 BAB 3 ALDEHID DAN KETON", 
            "📕 BAB 4 ASAM KARBOKSILAT DAN DERIVATNYA", 
            "🔬 POST TEST"
        ]
    )
    st.markdown("---")
    st.caption("E-Learning Kimia Organik | © 2026")

# ==============================================================================
# 4. LOGIKA KONTEN TIAP HALAMAN
# ==============================================================================

# --- HALAMAN UTAMA ---
if pilihan_halaman == "🏠 HALAMAN UTAMA":
    st.markdown("""
        <div class="banner-utama">
            <h1 style='color: white; margin-bottom: 5px; font-weight: 700;'>Selamat Datang di OrganicChem! 👋</h1>
            <p style='font-size: 1.2em; opacity: 0.95;'>Platform Media Pembelajaran Mandiri & Simulasi Identifikasi Gugus Fungsi</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("💡 Tentang Platform Ini")
    st.write(
        "Platform ini dirancang khusus untuk membantu mahasiswa/siswa memahami materi teoritis "
        "sekaligus visualisasi reaksi uji kualitatif senyawa organik di laboratorium secara interaktif."
    )
    
    st.markdown("---")
    col_petunjuk1, col_petunjuk2 = st.columns(2)
    with col_petunjuk1:
        with st.container(border=True):
            st.markdown("### 📖 Pelajari Materi")
            st.write("Silakan akses **BAB 1 sampai BAB 4** melalui sidebar untuk membaca materi dasar, struktur molekul, dan karakteristik setiap gugus fungsi.")
    with col_petunjuk2:
        with st.container(border=True):
            st.markdown("### 🧪 Uji Pemahaman")
            st.write("Buka halaman **POST TEST** untuk menjalankan simulasi reaksi lab interaktif menggunakan alat prediktor yang akurat.")

# --- BAB 1 ---
elif pilihan_halaman == "📘 BAB 1 HIDROKARBON":
    st.title("📘 BAB 1: HIDROKARBON")
    st.write("---")
    
    st.subheader("📌 Pengertian")
    st.write("Hidrokarbon adalah senyawa organik yang tersusun dari atom karbon (C) dan hidrogen (H).")
    
    st.subheader("🌿 Jenis Hidrokarbon")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("#### 1. Alkana (Jenuh)")
            st.write("- **Ikatan:** Tunggal C–C")
            st.latex(r"C_n H_{2n+2}")
            st.markdown("**Sifat:**")
            st.write("- Sukar bereaksi")
            st.write("- Mudah terbakar")
            st.write("- Tidak larut dalam air")
            
        with st.container(border=True):
            st.markdown("#### 2. Alkena (Tidak Jenuh)")
            st.write("- **Ikatan:** Memiliki ikatan rangkap dua (C=C)")
            st.latex(r"C_n H_{2n}")
            
    with col2:
        with st.container(border=True):
            st.markdown("#### 3. Alkuna (Tidak Jenuh)")
            st.write("- **Ikatan:** Memiliki ikatan rangkap tiga (C≡C)")
            st.latex(r"C_n H_{2n-2}")
            
        with st.container(border=True):
            st.markdown("#### 4. Senyawa Aromatik")
            st.write("- **Contoh utama:** Benzena")
            st.write("- Memiliki cincin aromatik yang konjugasi dan stabil.")

    st.markdown("---")
    st.subheader("🌡️ Sifat Fisika Hidrokarbon")
    st.write("Semakin banyak jumlah atom C pada rantai molekul, maka:")
    st.write("- Titik didih meningkat")
    st.write("- Titik leleh meningkat")
    st.info("💡 **Fase Zat Berdasarkan Panjang Rantai:** Alkana rantai pendek berupa **Gas**, rantai sedang berupa **Cair**, dan rantai panjang berupa **Padat**.")

    st.markdown("---")
    st.subheader("⚡ Sifat Kimia Hidrokarbon")
    st.markdown("- **Reaksi Pembakaran:** Menghasilkan gas $CO_2$ dan uap air $H_2O$.")
    st.markdown("- **Reaksi Substitusi:** Umumnya terjadi pada senyawa jenuh (Alkana).")
    st.markdown("- **Reaksi Adisi:** Terjadi pada senyawa tidak jenuh (Alkena dan Alkuna) karena adanya pemutusan ikatan rangkap.")

    st.markdown("---")
    st.subheader("🔬 Uji Identifikasi Penting")
    col_uji1, col_uji2 = st.columns(2)
    with col_uji1:
        st.success("**🧪 Uji Brom:** Digunakan untuk membedakan senyawa jenuh dan tidak jenuh. Jika warna brom hilang, berarti sampel merupakan senyawa tidak jenuh.")
    with col_uji2:
        st.success("**🧪 Uji Bayer:** Menggunakan larutan $KMnO_4$. Jika warna ungu khasnya hilang, mengindikasikan terdapatnya ikatan rangkap.")

# --- BAB 2 ---
elif pilihan_halaman == "📙 BAB 2 ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB 2: ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    tab1, tab2, tab3 = st.tabs(["💧 1. Alkohol", "🧪 2. Eter", "🏛️ 3. Fenol"])
    
    with tab1:
        st.subheader("Pengertian Alkohol")
        st.write("Alkohol adalah senyawa organik yang memiliki gugus fungsi hidroksil (-OH) yang terikat pada atom karbon jenuh.")
        st.latex(r"R-OH")
        st.write("**Contoh:** Metanol, Etanol, Propanol.")
        
        st.markdown("#### 🧱 Klasifikasi Alkohol")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.info("**Alkohol Primer:** Gugus -OH terikat pada atom C primer (C yang mengikat 1 atom C lain).")
        with c2:
            st.info("**Alkohol Sekunder:** Gugus -OH terikat pada atom C sekunder (C yang mengikat 2 atom C lain).")
        with c3:
            st.info("**Alkohol Tersier:** Gugus -OH terikat pada atom C tersier (C yang mengikat 3 atom C lain).")
            
        st.markdown("#### ⚙️ Sifat-Sifat Alkohol")
        st.markdown("**Sifat Fisika:**\n- Alkohol rantai pendek larut dengan baik dalam air.\n- Memiliki titik didih tinggi akibat adanya ikatan hidrogen antarmolekul.\n- Beberapa senyawa memiliki aroma khas yang kuat.")
        st.markdown("**Sifat Kimia:**\n- Dapat mengalami reaksi oksidasi.\n- Dapat mengalami substitusi gugus fungsi.\n- Dapat bereaksi dengan asam karboksilat membentuk ester.")
        
        st.markdown("#### 🔍 Uji Identifikasi Alkohol")
        st.warning("- **Pereaksi Lucas:** Membedakan alkohol primer, sekunder, dan tersier. Alkohol tersier bereaksi paling cepat ditandai larutan menjadi keruh seketika.\n- **Pereaksi Jones:** Mendeteksi alkohol primer dan sekunder. Warna berubah dari oranye (jingga) menjadi hijau.\n- **Uji Iodoform:** Memberikan hasil positif pada alkohol tertentu (yang mengandung gugus metil karbinol) dan metil keton, ditandai endapan kuning.")

    with tab2:
        st.subheader("Pengertian Eter")
        st.write("Eter adalah senyawa organik dengan gugus fungsi oksi (-O-) yang menjembatani dua gugus alkil.")
        st.latex(r"R-O-R")
        st.markdown("#### ⚙️ Sifat Eter")
        st.write("- Memiliki titik didih yang jauh lebih rendah daripada alkohol dengan jumlah atom C yang sama.")
        st.write("- Kurang larut di dalam air karena sifatnya yang cenderung non-polar.")
        st.write("- Bersifat relatif inert sehingga banyak digunakan sebagai pelarut organik di laboratorium.")

    with tab3:
        st.subheader("Pengertian Fenol")
        st.write("Fenol adalah senyawa aromatik yang memiliki gugus hidroksil (-OH) yang terikat langsung pada cincin benzena.")
        st.markdown("#### ⚙️ Sifat Fenol")
        st.write("- Bersifat asam lemah (namun lebih asam daripada alkohol alifatik).")
        st.write("- Jauh lebih reaktif terhadap substitusi aromatik elektrofilik dibandingkan benzena murni.")
        
        st.markdown("#### 🔍 Uji Identifikasi Fenol")
        st.warning("- **Uji $FeCl_3$:** Membentuk kompleks koordinasi berwarna unik (ungu, biru, atau hijau).\n- **Uji Brom:** Bereaksi cepat membentuk endapan putih dari senyawa tribromofenol.")

# --- BAB 3 ---
elif pilihan_halaman == "📗 BAB 3 ALDEHID DAN KETON":
    st.title("📗 BAB 3: ALDEHID DAN KETON")
    st.write("---")
    
    st.subheader("📌 Pengertian Umum")
    st.write("Aldehid dan keton adalah rumpun senyawa organik yang sama-sama memiliki gugus fungsi karbonil:")
    st.latex(r"C=O")
    
    st.markdown("---")
    col_ak1, col_ak2 = st.columns(2)
    with col_ak1:
        with st.container(border=True):
            st.markdown("### 🧪 Aldehid (Alkanal)")
            st.write("- **Posisi Gugus:** Gugus karbonil selalu terletak di **ujung rantai** karbon.")
            st.write("- **Karakteristik:** Sangat mudah dioksidasi.")
            st.write("- **Contoh:** Formaldehid (Metanal), Asetaldehid (Etanal).")
            
    with col_ak2:
        with st.container(border=True):
            st.markdown("### 🧪 Keton (Alkanon)")
            st.write("- **Posisi Gugus:** Gugus karbonil terletak di **tengah rantai** (diapit atom C).")
            st.write("- **Karakteristik:** Sulit dioksidasi oleh oksidator lemah.")
            st.write("- **Contoh:** Aseton (Propanon).")

    st.markdown("---")
    st.subheader("🌡️ Sifat Fisika")
    st.write("- Senyawa dengan suku rendah (rantai pendek) mudah larut dalam air.")
    st.write("- Memiliki aroma/bau yang khas.")
    st.write("- Memiliki titik didih yang lebih tinggi dibandingkan senyawa hidrokarbon padanannya karena sifat kutub gugus karbonil.")

    st.markdown("---")
    st.subheader("⚡ Sifat Kimia & Reaksi Adisi")
    st.write("Karena sifat ikatan rangkap pada gugus karbonil, aldehid dan keton dapat mengalami reaksi adisi dengan:")
    st.write("1. **Natrium Bisulfit ($NaHSO_3$)**")
    st.write("2. **Alkohol**")
    st.write("3. **Pereaksi Schiff**")

    st.markdown("---")
    st.subheader("🔬 Uji Identifikasi")
    st.success("**1. Pereaksi Schiff:** Aldehid memberikan hasil warna merah muda/magenta, sedangkan Keton memberikan hasil negatif.")
    st.success("**2. Pereaksi Na-Bisulfit:** Baik aldehid maupun keton reaktif dapat membentuk produk adisi berbentuk kristal/endapan putih.")
    st.success("**3. Uji Daya Reduksi:** Aldehid memiliki atom hidrogen alfa karbonil sehingga dapat mereduksi pereaksi Tollens atau Fehling, sedangkan keton tidak dapat mereduksi pereaksi tersebut.")

# --- BAB 4 ---
elif pilihan_halaman == "📕 BAB 4 ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB 4: ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.subheader("📌 1. Asam Karboksilat")
    st.write("Asam karboksilat adalah senyawa organik yang mengandung
