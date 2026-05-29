import streamlit as st
import time

# ==============================================================================
# 1. KONFIGURASI HALAMAN
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
    .banner-utama {
        background: linear-gradient(135deg, #11998e, #38ef7d);
        padding: 40px;
        border-radius: 12px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(56, 239, 125, 0.2);
    }
    .mekanisme-box {
        background-color: #f8f9fa;
        border-left: 4px solid #007bff;
        padding: 15px;
        margin: 10px 0;
        border-radius: 4px;
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
        "Platform ini dirancang untuk menjembatani pemahaman teoritis kimia organik dengan aplikasi praktis "
        "di laboratorium. Melalui visualisasi interaktif dan pangkalan data reaksi, Anda dapat mempelajari karakteristik "
        "gugus fungsi sekaligus memprediksi hasil uji kualitatif secara akurat."
    )

# --- BAB 1 ---
elif pilihan_halaman == "📘 BAB 1 HIDROKARBON":
    st.title("📘 BAB 1 — HIDROKARBON")
    st.write("---")
    
    st.markdown("""
    ### 1. Klasifikasi Utama Hidrokarbon
    Hidrokarbon dikelompokkan berdasarkan jenis ikatan antar-karbon dan struktur rantainya:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Alifatik Jenuh (Alkana)**\n* Memiliki ikatan tunggal C–C.\n* Rumus Umum: $C_nH_{2n+2}$\n* Karakteristik: Cenderung inert pada suhu kamar karena kuatnya ikatan $\sigma$ (sigma).")
        st.success("**Alifatik Tak Jenuh (Alkena & Alkuna)**\n* **Alkena ($C_nH_{2n}$):** Memiliki ikatan rangkap dua ($C=C$).\n* **Alkuna ($C_nH_{2n-2}$):** Memiliki ikatan rangkap tiga ($C\\equiv C$).\n* Karakteristik: Reaktif akibat tingginya kerapatan elektron pada ikatan $\pi$ (pi).")
    
    with col2:
        st.warning("**Aromatik (Benzena dan Turunannya)**\n* Senyawa siklis konjugasi tak jenuh yang memiliki stabilitas tinggi akibat resonansi/delokalisasi elektron $\pi$.\n* Tidak mudah mengalami reaksi adisi meskipun memiliki ikatan rangkap formal.")

    st.markdown("""
    ### 2. Tren Sifat Fisika
    * **Titik Didih & Leleh:** Berbanding lurus dengan massa molekul ($M_r$) dan luas permukaan kontak antar-molekul (gaya Van der Waals). Isomer rantai lurus memiliki titik didih lebih tinggi dibandingkan isomer rantai bercabang karena pengemasan molekul yang lebih rapat.
    * **Kelarutan:** Bersifat non-polar, sehingga larut dalam pelarut non-polar (seperti n-heksana, kloroform) dan tidak larut dalam air (*like dissolves like*).

    ### 3. Sifat Kimia & Reaktivitas
    * **Reaksi Substitusi Radikal Bebas (Alkana):** Terjadi melalui bantuan radiasi UV atau termal.
      $$CH_4 + Cl_2 \\xrightarrow{h\\nu} CH_3Cl + HCl$$
    * **Reaksi Adisi Elektrofilik (Alkena/Alkuna):** Pemutusan ikatan $\pi$ oleh pereaksi elektrofil. Mengikuti **Aturan Markovnikov** (hidrogen dari pereaksi masuk ke karbon yang mengikat hidrogen lebih banyak).
      $$CH_2=CH-CH_3 + HCl \\rightarrow CH_3-CH(Cl)-CH_3$$

    ### 4. Analisis Identifikasi Laboratorium
    * **Uji Bromin ($Br_2/CCl_4$):** Alkena dan alkuna akan mendiscolorisasi (menghilangkan warna merah-cokelat) bromin secara cepat tanpa menghasilkan gas $HBr$. Alkana tidak bereaksi kecuali dipicu sinar UV.
    * **Uji Baeyer ($KMnO_4$ encer/basa):** Alkena/alkuna mengoksidasi ion permanganat menjadi endapan cokelat $MnO_2$, mengubah warna larutan dari ungu menjadi pudar/hilang.
    """)

# --- BAB 2 ---
elif pilihan_halaman == "📙 BAB 2 ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB 2 — ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    st.markdown("""
    ### 1. Struktur Molekul & Hubungan Sifat Fisika
    Ketiga kelas senyawa ini merupakan turunan dari air ($H_2O$) di mana atom hidrogen digantikan oleh gugus alkil ($R$) atau aril ($Ar$).
    """)
    
    tab1, tab2, tab3 = st.tabs(["Alkohol (R-OH)", "Eter (R-O-R')", "Fenol (Ar-OH)"])
    
    with tab1:
        st.markdown("""
        * **Ikatan Hidrogen:** Keberadaan gugus $-OH$ yang sangat polar memungkinkan terbentuknya ikatan hidrogen antar-molekul yang kuat. Hal ini menyebabkan alkohol memiliki titik didih yang jauh lebih tinggi dibandingkan eter atau hidrokarbon dengan berat molekul setara.
        * **Kelarutan:** Alkohol rantai pendek ($C_1 - C_3$) bercampur sempurna dengan air. Seiring bertambah panjangnya rantai alkil (hidrofobik), kelarutan dalam air menurun drastis.
        """)
        
    with tab2:
        st.markdown("""
        * **Karakteristik Fisika:** Tidak dapat membentuk ikatan hidrogen sesama molekulnya karena tidak memiliki atom $H$ yang terikat langsung pada oksigen. Titik didihnya relatif rendah dan mendekati alkana padanannya.
        * **Sifat Kimia:** Sangat inert secara kimiawi, menjadikannya senyawa yang ideal sebagai pelarut organik ekstraksi (misalnya dietil eter).
        """)
        
    with tab3:
        st.markdown("""
        * **Keasaman:** Fenol memiliki keasaman yang signifikan lebih tinggi dibanding alkohol alifatik ($K_a \\approx 10^{-10}$). Hal ini disebabkan oleh ion fenoksida yang terbentuk distabilkan oleh delokalisasi muatan negatif ke dalam cincin aromatik benzena.
        """)

    st.markdown("""
    ### 2. Diferensiasi Laboratorium (Uji Spesifik)
    Untuk membedakan jenis-jenis alkohol dan fenol secara eksperimental, digunakan metode berikut:
    
    * **Pereaksi Lucas ($ZnCl_2$ dalam $HCl$ pekat):**
      Bekerja melalui mekanisme substitusi nukleofilik ($S_N1$). Kecepatan pembentukan fasa keruh (alkil klorida yang tidak larut) mengikuti stabilitas karbokation:
      $$\\text{Alkohol Tersier (Seketika)} > \\text{Alkohol Sekunder (5-10 menit)} > \\text{Alkohol Primer (Tidak bereaksi/Sangat lambat)}$$
    
    * **Pereaksi Jones ($CrO_3 / H_2SO_4$):**
      Mengoksidasi alkohol primer menjadi asam karboksilat dan alkohol sekunder menjadi keton, ditandai dengan perubahan warna dari **oranye ($Cr^{VI}$)** menjadi **hijau ($Cr^{III}$)**. Alkohol tersier memberikan hasil negatif.
      
    * **Uji Besi(III) Klorida ($FeCl_3$):**
      Uji selektif untuk fenol. Ion $Fe^{3+}$ membentuk kompleks koordinasi berwarna ungu, biru, atau hijau pekat dengan senyawa fenolik. Alkohol alifatik tidak memberikan perubahan warna ini.
    """)

# --- BAB 3 ---
elif pilihan_halaman == "📗 BAB 3 ALDEHID DAN KETON":
    st.title("📗 BAB 3 — ALDEHID DAN KETON")
    st.write("---")
    
    st.markdown("""
    ### 1. Karakteristik Gugus Karbonil ($C=O$)
    Gugus karbonil bersifat sangat polar karena perbedaan elektronegativitas yang besar antara atom karbon ($\delta^+$) dan oksigen ($\delta^-$). Karbon yang bermuatan parsial positif ini menjadikannya sangat rentan terhadap serangan dari **nukleofil**.
    
    ### 2. Perbedaan Struktural dan Reaktivitas
    * **Aldehid ($R-CHO$):** Memiliki setidaknya satu atom hidrogen yang terikat pada karbon karbonil. Kurang terhalang secara sterik dan memiliki kerapatan elektron yang lebih rendah pada karbon karbonil, menjadikannya **lebih reaktif** daripada keton.
    * **Keton ($R-CO-R'$):** Memiliki dua gugus alkil/aril yang terikat pada karbon karbonil. Gugus alkil memberikan efek induksi positif (mendonasikan elektron), yang menstabilkan parsial positif karbon karbonil sehingga menurunkan reaktivitasnya.
    """)

    st.markdown("""
    <div class="mekanisme-box">
        <h4>Adisi Nukleofilik pada Karbonil</h4>
        <p>Reaksi fundamental pada aldehid/keton melibatkan penyerangan nukleofil pada karbon sp² yang planar, mengubah hibridisasi menjadi sp³ tetrahedral.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 3. Diferensiasi Redoks Laboratorium
    Karena aldehid memiliki hidrogen karbonil, senyawa ini mudah dioksidasi menjadi asam karboksilat, sedangkan keton resisten terhadap oksidasi ringan.
    
    1. **Pereaksi Tollens ($[Ag(NH_3)_2]^+ / OH^-$):**
       Aldehid mereduksi kompleks perak diamina menjadi logam perak murni yang mengendap pada dinding tabung reaksi membentuk **cermin perak**.
       $$R-CHO + 2[Ag(NH_3)_2]^+ + 3OH^- \\rightarrow R-COO^- + 2Ag_{(s)} \\downarrow + 4NH_3 + 2H_2O$$
    
    2. **Pereaksi Fehling ($Cu^{2+}$ kompleks tartrat):**
       Aldehid alifatik mereduksi ion $Cu^{2+}$ (warna biru tua) menjadi endapan tembaga(I) oksida ($Cu_2O$) yang berwarna **merah bata**.
       $$R-CHO + 2Cu^{2+} + 5OH^- \\rightarrow R-COO^- + Cu_2O_{(s)} \\downarrow + 3H_2O$$
       
    3. **Uji Iodoform ($I_2 / NaOH$):**
       Uji spesifik untuk senyawa yang memiliki gugus **metil keton** ($CH_3-CO-$) seperti aseton, atau metil karbinol. Menghasilkan endapan kuning kristalin iodoform ($CHI_3$) berbau khas obat.
    """)

# --- BAB 4 ---
elif pilihan_halaman == "📕 BAB 4 ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB 4 — ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.markdown("""
    ### 1. Asam Karboksilat ($R-COOH$)
    Senyawa polar yang mampu membentuk dimer stabil melalui dua ikatan hidrogen antar-molekul. Hal ini menyebabkan titik didihnya sangat tinggi, melebihi alkohol padanannya.
    
    * **Sifat Asam:** Larut dalam air menghasilkan ion karboksilat yang muatan negatifnya terdelokalisasi secara merata di antara dua atom oksigen melalui resonansi.
    * **Uji Karbonat:** Dapat dideteksi dengan penambahan $NaHCO_3$ 5%, yang memicu pelepasan gas karbon dioksida ($CO_2$) berupa gelembung-gelembung gas (*effervescence*).
      $$R-COOH + NaHCO_3 \\rightarrow R-COONa + H_2O + CO_2 \\uparrow$$

    ### 2. Derivat Asam Karboksilat
    Derivat terbentuk melalui penggantian gugus $-OH$ karboksilat dengan gugus pergi (*leaving group*) lainnya.
    """)
    
    # Tabel komparasi fungsional dan reaktivitas
    st.markdown("#### Hierarki Reaktivitas Substitusi Asil Nukleofilik")
    st.markdown("Urutan reaktivitas dipengaruhi oleh kemampuan gugus pergi (*leaving group*) dan efek resonansi donor elektron:")
    
    data_derivat = {
        "Struktur / Kelas": ["Asil Halida (R-COCl)", "Anhidrida Asam (R-CO-O-COR)", "Ester (R-COOR')", "Amida (R-CONH2)"],
        "Gugus Pergi (-X)": ["Klorida (Cl-)", "Karboksilat (R-COO-)", "Alkoksida (R'O-)", "Amida (NH2-)"],
        "Tingkat Reaktivitas": ["Sangat Tinggi (Paling Reaktif)", "Tinggi", "Sedang", "Sangat Rendah (Paling Stabil)"]
    }
    st.table(data_derivat)

    st.markdown("""
    ### 3. Reaksi Esterifikasi Fischer
    Merupakan reaksi kesetimbangan antara asam karboksilat dengan alkohol yang dikatalisis oleh asam kuat ($H_2SO_4$ pekat) untuk menghasilkan ester yang beraroma buah/harum.
    $$R-COOH + R'-OH \\rightleftharpoons R-COOR' + H_2O$$
    """)
    
    # Menampilkan tabel kegunaan riil
    st.markdown("#### Aplikasi Industri Senyawa Karboksilat & Derivat")
    data_fungsi = {
        "Senyawa": ["Asam Asetat (Karboksilat)", "Isopentil Asetat (Ester)", "Nylon-6,6 (Poliamida)", "Asetil Klorida (Asil Halida)"],
        "Aplikasi Utama": ["Pengatur keasaman pangan (cuka), bahan baku polimer vinyl asetat.", "Essen sintetik rasa pisang untuk industri makanan.", "Serat sintetik kekuatan tinggi tekstil dan suku cadang.", "Agen asilasi kuat pada sintesis obat (misal: Aspirin)."]
    }
    st.table(data_fungsi)

# --- POST TEST ---
elif pilihan_halaman == "🔬 POST TEST":
    st.title("🔬 POST TEST: Alat Prediktor Uji Laboratorium")
    st.write("Silakan pilih kombinasi Senyawa Organik dan Pereaksi di bawah ini, lalu klik tombol analisis untuk melihat hasilnya.")
    st.write("---")

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
    hasil = "(-)
