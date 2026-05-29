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
    st.write("Asam karboksilat adalah senyawa organik yang mengandung gugus fungsi karboksil **-COOH**.")
    st.latex(r"R-COOH")
    st.write("**Contoh Senyawa:** Asam format (asam semut), Asam asetat (asam cuka), Asam propionat.")
    
    col_sifat1, col_sifat2 = st.columns(2)
    with col_sifat1:
        with st.container(border=True):
            st.markdown("#### 🌡️ Sifat Fisika")
            st.write("- Memiliki aroma menyengat yang khas.")
            st.write("- Rantai pendek dapat larut dengan baik di dalam air.")
            st.write("- Memiliki titik didih relatif tinggi karena kemampuannya membentuk dimer ikatan hidrogen.")
    with col_sifat2:
        with st.container(border=True):
            st.markdown("#### ⚡ Sifat Kimia")
            st.write("- Bersifat sebagai asam lemah.")
            st.write("- Bereaksi dengan basa untuk menghasilkan garam organik.")
            st.write("- Bereaksi dengan senyawa alkohol menghasilkan senyawa ester.")

    st.markdown("#### 🔄 Reaksi Penting: Esterifikasi")
    st.write("Reaksi antara asam karboksilat dengan alkohol yang dikatalisis oleh asam untuk membentuk ester dan air. Reaksi ini menghasilkan aroma harum khas ester.")
    st.latex(r"CH_3COOH + C_2H_5OH \rightarrow CH_3COOC_2H_5 + H_2O")
    
    st.markdown("#### 🔍 Uji Karakteristik Asam Karboksilat")
    st.info("- **Uji Lakmus:** Larutannya bersifat asam sehingga mengubah lakmus biru menjadi merah.\n- **Reaksi dengan $NaHCO_3$:** Terjadi reaksi penetralan asam yang melepas gelembung gas karbondioksida ($CO_2$).")

    st.markdown("---")
    st.subheader("🧩 2. Derivat Asam Karboksilat")
    st.write("Derivat (turunan) asam karboksilat adalah senyawa organik di mana gugus **-OH** dari karboksil telah digantikan oleh gugus nukleofil lain.")
    
    d1, d2, d3, d4 = st.columns(4)
    with d1:
        with st.container(border=True):
            st.markdown("##### **Ester**")
            st.latex(r"R-COOR'")
            st.caption("Berbau harum buah-buahan. Banyak digunakan sebagai komponen utama parfum, perasa makanan (flavor), dan pelarut.")
    with d2:
        with st.container(border=True):
            st.markdown("##### **Amida**")
            st.latex(r"R-CONH_2")
            st.caption("Memiliki gaya antarmolekul kuat dan titik didih tinggi. Banyak diaplikasikan pada industri serat plastik dan sintesis obat.")
    with d3:
        with st.container(border=True):
            st.markdown("##### **Anhidrida Asam**")
            st.write("Terbentuk dari dehidrasi dua molekul asam karboksilat. Bersifat sangat reaktif dan mudah terhidrolisis kembali oleh air.")
    with d4:
        with st.container(border=True):
            st.markdown("##### **Asil Halida**")
            st.latex(r"R-COCl")
            st.caption("Senyawa turunan yang paling reaktif. Sangat mudah terhidrolisis dan melepaskan gas asam halida.")

    st.markdown("#### 📉 Perbandingan Reaktivitas Derivat")
    st.write("Urutan tingkat reaktivitas turunan asam karboksilat terhadap substitusi asil nukleofilik:")
    st.warning("⚠️ **Asil Halida > Anhidrida Asam > Ester > Amida** (Semakin reaktif senyawa, maka semakin mudah mengalami reaksi substitusi).")

    st.markdown("#### 💼 Tabel Fungsi dan Kegunaan")
    data_kegunaan = {
        "Nama Senyawa": ["Asam asetat", "Ester", "Amida", "Asil halida"],
        "Kegunaan Utama": ["Cuka makanan / pengawet", "Parfum dan esens perasa makanan", "Pembuatan komponen plastik dan industri obat", "Bahan perantara sintesis organik"]
    }
    st.table(data_kegunaan)

    st.markdown("#### 🏁 Kesimpulan Bab 4")
    st.success("Asam karboksilat dicirikan oleh gugus fungsi -COOH yang bersifat asam lemah serta dapat disintesis menjadi turunannya melalui penggantian gugus -OH. Derivatnya meliputi ester, amida, anhidrida, dan asil halida yang memiliki peran besar dalam kehidupan sehari-hari maupun sintesis industri.")

# --- POST TEST ---
elif pilihan_halaman == "🔬 POST TEST":
    st.title("🔬 POST TEST: Alat Prediktor Uji Laboratorium")
    st.write("Silakan pilih kombinasi Senyawa Organik dan Pereaksi di bawah ini, lalu klik tombol analisis untuk melihat hasilnya.")
    st.write("---")

    # Kontainer Input Parameter Uji
    with st.container(border=True):
        st.markdown("#### ⚙️ Pengaturan Parameter Uji")
        col1, col2 = st.columns(2)

        with col1:
            senyawa = st.selectbox("🎯 Pilih Senyawa Target:", [
                "Alkohol Primer", "Alkohol Sekunder", "Alkohol Tersier", 
                "Formaldehida", "Aseton", "Heksana", "Etil Asetat", "Asam Asetat"
            ])

        with col2:
            pereaksi = st.selectbox("🧪 Pilih Pereaksi / Indikator Lab:", [
                "Oksidator (K2Cr2O7 / H+)", "Pereaksi Lucas (ZnCl2 / HCl)", 
                "Pereaksi Tollens", "Pereaksi Fehling", "Uji Iodoform (I2 / NaOH)",
                "Pereaksi Jones (CrO3 / H2SO4)", "Pereaksi Schiff", "Natrium Bisulfit (NaHSO3)",
                "Hidroksilamin (NH2OH)", "NaHCO3 + Uji Barit (Ba(OH)2)", "Uji Ceric Nitrat"
            ])
        
        st.write("")
        tombol_analisis = st.button("Mulai Analisis Reaksi 🧪", type="primary", use_container_width=True)

    # ================= DATABASE LOGIKA & REAKSI KIMIA =================
    hasil = "(-) Tidak Bereaksi"
    reaksi = "Tidak ada persamaan reaksi."
    pembahasan = ""

    def alasan_negatif_umum(senyawa):
        if senyawa == "Heksana": return "Heksana adalah alkana rantai lurus (non-polar dan jenuh) yang sangat stabil dan tidak memiliki gugus fungsi reaktif."
        if senyawa == "Etil Asetat": return "Etil asetat adalah ester yang cukup stabil. Gugus karbonilnya terstabilkan oleh resonansi sehingga kurang reaktif terhadap pereaksi ini."
        return f"{senyawa} tidak memiliki gugus fungsi yang sesuai untuk berinteraksi dengan pereaksi ini."

    # 1. K2Cr2O7
    if pereaksi == "Oksidator (K2Cr2O7 / H+)":
        if senyawa in ["Alkohol Primer", "Alkohol Sekunder", "Formaldehida"]:
            hasil = "(+) Warna berubah jingga menjadi hijau"
            reaksi = "Cr₂O₇²⁻ (jingga) + Senyawa → Cr³⁺ (hijau) + Hasil Oksidasi"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Senyawa ini memiliki atom Hidrogen yang terikat pada atom Karbon pembawa gugus fungsi, sehingga dapat dioksidasi. Ion dikromat (jingga) tereduksi menjadi ion Cr³⁺ (hijau)."
        elif senyawa == "Alkohol Tersier":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Karbon yang mengikat gugus -OH pada alkohol tersier tidak memiliki atom hidrogen (hidrogen alfa) sama sekali, sehingga ikatan C-C harus diputus untuk oksidasi, yang mana tidak bisa dilakukan oleh dikromat."
        elif senyawa in ["Aseton", "Asam Asetat"]:
            pembahasan = f"❌ <b>Kenapa TIDAK bereaksi:</b> {senyawa} sudah berada pada tingkat oksidasi yang tinggi (karbonil keton/asam karboksilat stabil) sehingga tidak dapat dioksidasi lebih lanjut oleh oksidator sedang."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> " + alasan_negatif_umum(senyawa)

    # 2. LUCAS
    elif pereaksi == "Pereaksi Lucas (ZnCl2 / HCl)":
        if senyawa == "Alkohol Tersier":
            hasil = "(+) Keruh seketika"
            reaksi = "R₃C-OH + HCl → R₃C-Cl↓ + H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Alkohol tersier sangat mudah mengalami reaksi substitusi nukleofilik (SN1) karena membentuk karbokation tersier yang sangat stabil, langsung menghasilkan alkil klorida yang tak larut air."
        elif senyawa == "Alkohol Sekunder":
            hasil = "(+) Keruh setelah 5-10 menit"
            reaksi = "R₂CH-OH + HCl → R₂CH-Cl↓ + H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Reaksi berjalan lambat melalui mekanisme SN1 karena karbokation sekunder kurang stabil dibanding tersier. Butuh waktu untuk menghasilkan endapan alkil klorida."
        elif senyawa == "Alkohol Primer":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Karbokation primer sangat tidak stabil. Tanpa pemanasan ekstrem, alkohol primer tidak akan bereaksi dengan pereaksi Lucas."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Pereaksi Lucas dirancang khusus untuk mensubstitusi gugus hidroksil (-OH) pada alkohol. Senyawa ini tidak memiliki gugus -OH alkoholik bebas."

    # 3. TOLLENS
    elif pereaksi == "Pereaksi Tollens":
        if senyawa == "Formaldehida":
            hasil = "(+) Terbentuk Cermin Perak"
            reaksi = "R-CHO + 2[Ag(NH₃)₂]⁺ + 3OH⁻ → R-COO⁻ + 2Ag↓ + 4NH₃ + 2H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Gugus aldehid sangat mudah dioksidasi. Ia mampu mereduksi ion perak kompleks menjadi logam perak murni (Ag) yang menempel mengkilap di dinding tabung."
        elif senyawa == "Aseton":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Keton (aseton) tidak memiliki atom hidrogen yang menempel pada gugus karbonil, sehingga tidak bisa dioksidasi oleh oksidator lemah seperti Tollens."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Senyawa ini tidak mengandung gugus aldehid yang punya sifat pereduksi."

    # 4. FEHLING
    elif pereaksi == "Pereaksi Fehling":
        if senyawa == "Formaldehida":
            hasil = "(+) Terbentuk Endapan Merah Bata"
            reaksi = "R-CHO + 2Cu²⁺ + 5OH⁻ → R-COO⁻ + Cu₂O↓ (merah bata) + 3H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Aldehid memiliki sifat pereduksi yang kuat, mereduksi ion tembaga(II) kompleks berwarna biru menjadi endapan tembaga(I) oksida yang berwarna merah bata."
        elif senyawa == "Aseton":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Sama seperti Tollens, keton tidak bisa dioksidasi oleh oksidator lemah seperti Fehling karena ketiadaan ikatan C-H pada gugus karbonilnya."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Hanya senyawa aldehid alifatik yang memiliki sifat pereduksi untuk mereduksi ion Cu²⁺ pada suhu pemanasan."

    # 5. IODOFORM
    elif pereaksi == "Uji Iodoform (I2 / NaOH)":
        if senyawa == "Aseton":
            hasil = "(+) Endapan Kuning Iodoform"
            reaksi = "CH₃-CO-CH₃ + 3I₂ + 4NaOH → CHI₃↓ (kuning) + CH₃COONa + 3NaI + 3H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Aseton memiliki gugus metil keton (CH₃-C=O). Atom hidrogen alfa pada metil ini sangat asam, sehingga tersubstitusi oleh iodin lalu terputus membentuk endapan kuning iodoform (CHI₃)."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Senyawa ini tidak memiliki struktur metil keton (CH₃-CO-) ataupun alkohol sekunder dengan struktur metil di sebelahnya (CH₃-CH(OH)-)."

    # 6. JONES
    elif pereaksi == "Pereaksi Jones (CrO3 / H2SO4)":
        if senyawa in ["Alkohol Primer", "Alkohol Sekunder", "Formaldehida"]:
            hasil = "(+) Warna berubah merah-jingga ke hijau/biru-hijau"
            reaksi = "CrO₃ (jingga) + H₂SO₄ + Senyawa → Cr³⁺ (hijau) + Hasil Oksidasi"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Jones adalah oksidator kuat. Memiliki atom hidrogen alfa membuat senyawa ini teroksidasi, sementara Kromium(VI) tereduksi menjadi Kromium(III) hijau."
        elif senyawa == "Alkohol Tersier":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Tidak ada hidrogen pada karbon pengikat -OH. Oksidasi gagal terjadi."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Senyawa sudah berada pada titik oksidasi maksimumnya (seperti asam asetat) atau tidak punya gugus yang bisa dioksidasi (seperti heksana)."

    # 7. SCHIFF
    elif pereaksi == "Pereaksi Schiff":
        if senyawa == "Formaldehida":
            hasil = "(+) Larutan berwarna Merah / Magenta"
            reaksi = "Aldehid + Pereaksi Schiff → Kompleks warna magenta"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Aldehid mudah bereaksi dengan fuksin-asam sulfit (Schiff) tanpa hambatan sterik (ruang), memulihkan kembali warna asli magenta dari fuksin."
        elif senyawa == "Aseton":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Keton memiliki hambatan sterik (ruang lingkup molekul yang lebih besar) sehingga tidak bisa berikatan kuat dengan pereaksi Schiff untuk memunculkan warna."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Pereaksi ini sangat spesifik bereaksi secara adisi nukleofilik hanya dengan gugus aldehid."

    # 8. NA-BISULFIT
    elif pereaksi == "Natrium Bisulfit (NaHSO3)":
        if font_senyawa := senyawa in ["Formaldehida", "Aseton"]:
            hasil = "(+) Endapan Putih Kristalin"
            reaksi = "R₂C=O + NaHSO₃ → R₂C(OH)SO₃Na↓ (kristal putih)"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Gugus karbonil polar (C=O) pada aldehid/keton mengalami adisi nukleofilik oleh ion bisulfit yang kaya elektron, menghasilkan produk garam yang sukar larut."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Senyawa tidak memiliki gugus karbonil reaktif. Pada asam asetat/etil asetat, efek resonansi membuat karbon karbonilnya tidak cukup positif untuk diserang bisulfit."

    # 9. HIDROKSILAMIN
    elif pereaksi == "Hidroksilamin (NH2OH)":
        if senyawa in ["Formaldehida", "Aseton"]:
            hasil = "(+) Terbentuk Kristal Oksim"
            reaksi = "R₂C=O + NH₂OH → R₂C=N-OH (Oksim) + H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Hidroksilamin menyerang karbonil pada aldehid/keton, melepaskan air (kondensasi), dan membentuk ikatan rangkap C=N baru (oksim) yang mengendap."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Hanya senyawa aldehid dan keton murni yang bereaksi membentuk oksim. Gugus lain kurang elektrofilik atau tidak memilikinya sama sekali."

    # 10. NaHCO3 + UJI BARIT
    elif pereaksi == "NaHCO3 + Uji Barit (Ba(OH)2)":
        if senyawa == "Asam Asetat":
            hasil = "(+) Gelembung Gas & Air Barit Keruh"
            reaksi = "1) CH₃COOH + NaHCO₃ → CH₃COONa + H₂O + CO₂↑ \n2) CO₂ + Ba(OH)₂ → BaCO₃↓ (keruh) + H₂O"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Asam asetat bersifat cukup asam untuk mendonasikan proton (H⁺) ke ion bikarbonat (HCO₃⁻), menghasilkan asam karbonat yang terurai jadi gas CO₂. Gas ini lalu bereaksi dengan barit membentuk BaCO₃ yang keruh."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Senyawa ini tidak bersifat asam atau keasamannya sangat lemah (seperti alkohol), sehingga tidak mampu bereaksi dengan garam basa lemah seperti NaHCO₃."

    # 11. CERIC NITRAT
    elif pereaksi == "Uji Ceric Nitrat":
        if senyawa in ["Alkohol Primer", "Alkohol Sekunder", "Alkohol Tersier"]:
            hasil = "(+) Warna kuning menjadi merah/merah muda"
            reaksi = "R-OH + [Ce(NO₃)₆]²⁻ → [Ce(OR)(NO₃)₅]²⁻ (kompleks merah) + HNO₃"
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Pasangan elektron bebas pada oksigen di gugus hidroksil (-OH) alkohol mendesak ligan nitkat dan berikatan koordinasi dengan logam Cerium pusat, menghasilkan perubahan serapan cahaya (menjadi merah)."
        elif senyawa == "Asam Asetat":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Meskipun punya OH, gugus karboksil sangat menarik elektron (electron-withdrawing), sehingga atom oksigennya kurang nukleofilik untuk berkoordinasi dengan Cerium."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Uji ini spesifik untuk gugus hidroksil (-OH) alifatik bebas. Senyawa ini tidak memiliki gugus tersebut."


    # ================= LOGIKA MUNCUL SETELAH KLIK TOMBOL + LOADING =================
    if tombol_analisis:
        # Menambahkan animasi loading spinner selama 1.5 detik
        with st.spinner("⏳ Sedang mereaksikan sampel di dalam tabung reaksi..."):
            time.sleep(1.5) # Durasi waktu loading sengaja dibuat agar animasi terasa nyata
            
        st.write("")
        st.markdown("### 📊 Lembar Hasil Analisis")
        
        # Deteksi warna dinamis untuk status (+) atau (-)
        warna_teks_hasil = '#d35400' if '(+)' in hasil else '#7f8c8d'
        
        st.markdown(f"""
        <div class="kotak-analisis">
            <div class="label-analisis">Hasil Pengamatan (+)/(-)</div>
            <p style="font-size: 1.25em; color: {warna_teks_hasil}; font-weight: bold; margin: 0;">{hasil}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="kotak-analisis">
            <div class="label-analisis">Persamaan Reaksi Kimia</div>
            <p style="font-size: 1.1em; font-family: 'Courier New', monospace; white-space: pre-wrap; margin: 0; background: #ffffff; padding: 12px; border-radius: 5px; border: 1px solid #e2e8f0;">{reaksi}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="kotak-analisis">
            <div class="label-analisis">Pembahasan Teoritis & Analisis Mekanisme</div>
            <p style="margin: 0; line-height: 1.6; color: #2d3748;">{pembahasan}</p>
        </div>
        """, unsafe_allow_html=True)
