import streamlit as st

# Pengaturan konfigurasi halaman
st.set_page_config(
    page_title="Identifikasi Senyawa Organik",
    page_icon="🧪",
    layout="centered"
)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("Navigasi")
pilihan_halaman = st.sidebar.radio(
    "Pilih Halaman:",
    ["Home", "Bab 1", "Bab 2", "Bab 3", "Bab 4", "Post Test"]
)

# --- HALAMAN 1: HOME ---
if pilihan_halaman == "Home":
    st.title("Selamat Datang! 👋")
    st.subheader("Web Analisis dan Identifikasi Senyawa Organik")
    st.write("---")
    st.write("""
    Selamat datang di platform pembelajaran digital untuk Identifikasi Senyawa Organik. 
    Web ini dirancang untuk membantu Anda memahami teori, konsep, serta pengujian 
    terkait senyawa organik secara terstruktur.
    """)
    st.info("Silakan gunakan menu di sebelah kiri (sidebar) untuk mulai menjelajahi materi bab dan mengikuti post-test.")

# --- HALAMAN 2: BAB 1 ---
elif pilihan_halaman == "Bab 1":
    st.title("Bab 1: Pengantar Senyawa Organik")
    st.write("---")
    st.header("Teori Bab 1")
    st.write("""
    Masukkan teori atau materi Bab 1 di sini. Contoh:
    - Definisi senyawa organik.
    - Karakteristik atom karbon.
    - Perbedaan senyawa organik dan anorganik.
    """)
    # Anda bisa menambahkan komponen lain seperti gambar atau video jika diperlukan

# --- HALAMAN 3: BAB 2 ---
elif pilihan_halaman == "Bab 2":
    st.title("Bab 2: Hidrokarbon (Alkana, Alkena, Alkuna)")
    st.write("---")
    st.header("Teori Bab 2")
    st.write("""
    Masukkan teori atau materi Bab 2 di sini. Contoh:
    - Struktur dan tata nama hidrokarbon.
    - Sifat fisik dan kimia alkana, alkena, dan alkuna.
    - Reaksi-reaksi khas pada hidrokarbon.
    """)

# --- HALAMAN 4: BAB 3 ---
elif pilihan_halaman == "Bab 3":
    st.title("Bab 3: Gugus Fungsi (Alkohol, Eter, Aldehid, Keton)")
    st.write("---")
    st.header("Teori Bab 3")
    st.write("""
    Masukkan teori atau materi Bab 3 di sini. Contoh:
    - Identifikasi gugus fungsi oksigen.
    - Reaksi pembeda antara alkohol primer, sekunder, dan tersier.
    - Ujian tiazol atau pereaksi Tollens/Fehling untuk aldehid.
    """)

# --- HALAMAN 5: BAB 4 ---
elif pilihan_halaman == "Bab 4":
    st.title("Bab 4: Asam Karboksilat, Ester, dan Senyawa Nitrogen")
    st.write("---")
    st.header("Teori Bab 4")
    st.write("""
    Masukkan teori atau materi Bab 4 di sini. Contoh:
    - Karakteristik asam karboksilat dan turunan esternya.
    - Identifikasi senyawa organik yang mengandung nitrogen (amina, amida).
    """)

# --- HALAMAN 6: POST TEST ---
elif pilihan_halaman == "Post Test":
    st.title("📝 Post Test")
    st.write("---")
    st.subheader("Jawablah pertanyaan di bawah ini dengan benar!")
    
    # Form untuk Post Test agar input tidak langsung mereset halaman
    with st.form("post_test_form"):
        q1 = st.radio(
            "1. Senyawa organik manakah yang bereaksi positif dengan pereaksi Tollens membentuk cermin perak?",
            ["Alkana", "Alkohol", "Aldehid", "Eter"]
        )
        
        q2 = st.radio(
            "2. Ikatan apa yang menjadi ciri khas dari senyawa Alkena?",
            ["Ikatan tunggal", "Ikatan rangkap dua", "Ikatan rangkap tiga", "Ikatan ionik"]
        )
        
        # Tombol submit didalam form
        submitted = st.form_submit_button("Kirim Jawaban")
        
        if submitted:
            st.success("Jawaban Anda telah berhasil dikirim!")
            # Logika pemeriksaan skor bisa ditambahkan di sini
            skor = 0
            if q1 == "Aldehid": skor += 50
            if q2 == "Ikatan rangkap dua": skor += 50
            st.write(f"Skor Anda: {skor}/100")
