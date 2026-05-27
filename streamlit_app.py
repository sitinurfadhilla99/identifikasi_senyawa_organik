import streamlit as st

# Pengaturan konfigurasi halaman
st.set_page_config(
    page_title="Identifikasi Senyawa Organik",
    page_icon="🧪",
    layout="centered"
)

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("🔬 Menu Utama")
pilihan_halaman = st.sidebar.radio(
    "Silakan Pilih Halaman:",
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
    st.title("📝 LEMBAR POST TEST")
    st.subheader("Uji Kompetensi Identifikasi Senyawa Organik")
    st.write("---")
    
    # 1. BAGIAN IDENTITAS (Form Terpisah agar aman saat submit jawaban utama)
    st.markdown("### **I. Identitas Praktikan**")
    nama = st.text_input("Nama Lengkap:", placeholder="Masukkan nama Anda...")
    nim = st.text_input("NIM / NIS:", placeholder="Masukkan NIM atau NIS Anda...")
    kelas = st.selectbox("Kelas / Kelompok:", ["Pilih Kelas", "Kimia A", "Kimia B", "Kelompok 1", "Kelompok 2", "Kelompok 3"])
    
    st.write("---")
    
    # 2. BAGIAN SOAL IDENTIFIKASI (Menggunakan form agar pengerjaan stabil)
    st.markdown("### **II. Kasus Analisis Laboratorium**")
    st.caption("Analisis data di bawah ini dan tentukan identitas senyawa organik terlarut dengan tepat!")
    
    with st.form("form_pengerjaan_post_test"):
        
        # --- Sampel 1 ---
        st.markdown("#### **[Sampel Misterius 01]**")
        st.info("🔬 **Hasil Uji:** Sampel berupa zat cair bening. Ketika direaksikan dengan **Larutan KMnO₄**, warna ungu dari kalium permanganat langsung pudar dan terbentuk endapan cokelat ($MnO_2$).")
        ans1 = st.radio(
            "Berdasarkan uji tersebut, jenis senyawa apakah Sampel 01?",
            ["Belum Memilih", "Alkana (Hidrokarbon Jenuh)", "Alkena (Hidrokarbon Tak Jenuh)", "Eter"],
            key="s1"
        )
        st.write("")
        
        # --- Sampel 2 ---
        st.markdown("#### **[Sampel Misterius 02]**")
        st.info("🔬 **Hasil Uji:** Sampel direaksikan dengan **Pereaksi Fehling A & B** lalu dipanaskan. Hasil pengamatan menunjukkan terbentuknya **endapan merah bata ($Cu_2O$)**.")
        ans2 = st.radio(
            "Gugus fungsi yang terdapat pada Sampel 02 adalah...",
            ["Belum Memilih", "Alkohol (Alkanol)", "Keton (Alkanon)", "Aldehid (Alkanal)"],
            key="s2"
        )
        st.write("")
        
        # --- Sampel 3 ---
        st.markdown("#### **[Sampel Misterius 03]**")
        st.info("🔬 **Hasil Uji:** Sampel merupakan senyawa alkohol. Ketika diuji menggunakan **Pereaksi Lucas**, larutan tetap jernih pada suhu kamar dan baru membentuk kekeruhan setelah dipanaskan cukup lama.")
        ans3 = st.radio(
            "Kategori struktur alkohol pada Sampel 03 adalah...",
            ["Belum Memilih", "Alkohol Primer", "Alkohol Sekunder", "Alkohol Tersier"],
            key="s3"
        )
        st.write("")
        
        # --- Sampel 4 ---
        st.markdown("#### **[Sampel Misterius 04]**")
        st.info("🔬 **Hasil Uji:** Sampel padat dilarutkan ke dalam air. Saat ditambahkan padatan **Natrium Karbonat ($Na_2CO_3$)**, langsung terjadi reaksi spontan yang menghasilkan **efervesensi (gelembung gas $CO_2$)**.")
        ans4 = st.radio(
            "Senyawa organik tersebut termasuk dalam golongan...",
            ["Belum Memilih", "Ester", "Asam Karboksilat", "Amina"],
            key="s4"
        )
        st.write("---")
        
        # Tombol Submit di dalam form
        tombol_submit = st.form_submit_button("KIRIM JAWABAN & LIHAT HASIL")
        
        if tombol_submit:
            # Validasi pengisian identitas & jawaban sebelum diproses
            if not nama or not nim or kelas == "Pilih Kelas":
                st.error("❌ Gagal mengirim! Mohon lengkapi **Nama, NIM, dan Kelas** terlebih dahulu di bagian atas.")
            elif "Belum Memilih" in [ans1, ans2, ans3, ans4]:
                st.error("❌ Gagal mengirim! Anda belum menyelesaikan semua jawaban sampel uji.")
            else:
                # Menghitung skor (Nilai maksimal 100, 4 soal berarti masing-masing 25 poin)
                skor_akhir = 0
                log_jawaban = []
                
                # Cek Jawaban Soal 1
                if ans1 == "Alkena (Hidrokarbon Tak Jenuh)": 
                    skor_akhir += 25
                    log_jawaban.append("✅ Soal 1 Benar (Uji Baeyer / KMnO4 mendeteksi ikatan rangkap)")
                else: 
                    log_jawaban.append("❌ Soal 1 Salah")
                
                # Cek Jawaban Soal 2
                if ans2 == "Aldehid (Alkanal)": 
                    skor_akhir += 25
                    log_jawaban.append("✅ Soal 2 Benar (Fehling positif menghasilkan endapan merah bata pada aldehid)")
                else: 
                    log_jawaban.append("❌ Soal 2 Salah")
                    
                # Cek Jawaban Soal 3
                if ans3 == "Alkohol Primer": 
                    skor_akhir += 25
                    log_jawaban.append("✅ Soal 3 Benar (Alkohol primer bereaksi sangat lambat dengan pereaksi Lucas)")
                else: 
                    log_jawaban.append("❌ Soal 3 Salah")
                    
                # Cek Jawaban Soal 4
                if ans4 == "Asam Karboksilat": 
                    skor_akhir += 25
                    log_jawaban.append("✅ Soal 4 Benar (Asam organik membebaskan gas CO2 dari garam karbonat)")
                else: 
                    log_jawaban.append("❌ Soal 4 Salah")

                # --- OUTPUT HASIL / REPORT ---
                st.write("### 📊 HASIL EVALUASI")
                st.success(f"Terima kasih **{nama}** ({nim}) dari **{kelas}**, jawaban Anda telah terekam!")
                
                # Tampilkan skor
                st.metric(label="Skor Post Test Anda", value=f"{skor_akhir} / 100")
                
                # Tampilkan detail koreksi
                st.markdown("#### **Detail Koreksi:**")
                for log in log_jawaban:
                    st.write(log)
                
                # Pesan kelulusan & Animasi
                if skor_akhir >= 75:
                    st.balloons()
                    st.success("🎉 Selamat! Anda dinyatakan LULUS dalam post test identifikasi senyawa ini.")
                else:
                    st.warning("⚠️ Nilai Anda masih di bawah batas kelulusan (75). Silakan pelajari kembali bab materi sebelum mencoba lagi.")
