import streamlit as st

# 1. KONFIGURASI HALAMAN (Harus paling atas)
st.set_page_config(
    page_title="OrganicChem | Edu-Lab",
    page_icon="🧪",
    layout="wide"
)

# 2. CUSTOM CSS (Untuk mempercantik tampilan kotak hasil prediktor dan card materi)
st.markdown("""
    <style>
    /* Styling untuk Kotak Hasil Prediktor */
    .kotak {
        border-left: 5px solid #2ecc71;
        border-radius: 6px;
        padding: 15px;
        margin-bottom: 15px;
        background-color: #f4faf6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .label {
        font-weight: bold;
        color: #27ae60;
        font-size: 1.1em;
        margin-bottom: 5px;
    }
    /* Styling Banner Selamat Datang */
    .banner-home {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        padding: 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)


# 3. SIDEBAR NAVIGASI
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022607.png", width=70) # Logo Lab Kimia mini
    st.title("OrganicChem v1.0")
    st.write("✨ *Platform Belajar Interaktif*")
    st.markdown("---")
    pilihan_halaman = st.radio(
        "Silakan Pilih Halaman:",
        ["🏠 Home", "📘 Bab 1: Pengantar", "📙 Bab 2: Hidrokarbon", "📗 Bab 3: Gugus Fungsi", "📕 Bab 4: Turunan & Nitrogen", "🔬 Post Test & Prediktor"]
    )
    st.markdown("---")
    st.caption("Dibuat untuk Praktikum Kimia Organik | © 2026")


# ================= HALAMAN 1: HOME =================
if pilihan_halaman == "🏠 Home":
    st.markdown("""
        <div class="banner-home">
            <h1 style='color: white; margin-bottom: 5px;'>Selamat Datang di OrganicChem! 👋</h1>
            <p style='font-size: 1.2em; opacity: 0.9;'>Platform Pembelajaran Digital & Prediktor Analisis Senyawa Organik</p>
        </div>
    """, unsafe_allow_html=True)
    
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.subheader("📚 Materi Terstruktur")
        st.write("Pelajari konsep dasar kimia organik, klasifikasi hidrokarbon, hingga berbagai identifikasi gugus fungsi spesifik mulai dari Bab 1 hingga Bab 4.")
    
    with col_info2:
        st.subheader("🧪 Simulasi Prediktor Lab")
        st.write("Uji pemahamanmu secara langsung di halaman **Post Test**! Pilih sampel senyawamu dan lihat bagaimana reaksinya terhadap berbagai indikator laboratorium secara langsung.")
        
    st.write("---")
    st.info("💡 **Tips Memulai:** Gunakan menu navigasi di sebelah kiri (sidebar) untuk berpindah halaman materi atau langsung mencoba alat prediktor.")


# ================= HALAMAN 2: BAB 1 =================
elif pilihan_halaman == "📘 Bab 1: Pengantar":
    st.title("📘 Bab 1: Pengantar Senyawa Organik")
    st.write("---")
    
    tab1, tab2 = st.tabs(["✨ Definisi Dasar", "🔬 Karakteristik Atom Karbon"])
    
    with tab1:
        st.markdown("### Apa itu Senyawa Organik?")
        st.write("Senyawa organik adalah golongan senyawa yang komponen utamanya terdiri dari atom karbon (C), hidrogen (H), oksigen (O), nitrogen (N), dan unsur lainnya.")
        
        c1, c2 = st.columns(2)
        with c1:
            st.success("**Senyawa Organik**\n- Titik didih/leleh relatif rendah\n- Umumnya tidak stabil terhadap pemanasan tinggi\n- Reaksi cenderung berjalan lambat")
        with c2:
            st.warning("**Senyawa Anorganik**\n- Titik didih/leleh relatif tinggi\n- Lebih stabil terhadap panas\n- Reaksi antar ion berjalan cepat")
            
    with tab2:
        st.markdown("### Kekhasan Atom Karbon")
        st.write("Mengapa atom karbon menjadi pusat dari jutaan jenis senyawa di bumi?")
        with st.expander("1. Memiliki 4 Elektron Valensi"):
            st.write("Memungkinkan atom karbon membentuk hingga 4 ikatan kovalen tunggal, rangkap dua, maupun rangkap tiga dengan atom lainnya.")
        with st.expander("2. Jari-jari Atom Relatif Kecil"):
            st.write("Ikatan koval
