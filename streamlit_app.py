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
        if senyawa in ["Formaldehida", "Aseton"]:
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
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Pasangan elektron bebas pada oksigen di gugus hidroksil (-OH) alkohol mendesak ligan nitrat dan berikatan koordinasi dengan logam Cerium pusat, menghasilkan perubahan serapan cahaya (menjadi merah)."
        elif senyawa == "Asam Asetat":
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Meskipun punya OH, gugus karboksil sangat menarik elektron (electron-withdrawing), sehingga atom oksigennya kurang nukleofilik untuk berkoordinasi dengan Cerium."
        else:
            pembahasan = "❌ <b>Kenapa TIDAK bereaksi:</b> Uji ini spesifik untuk gugus hidroksil (-OH) alifatik bebas. Senyawa ini tidak memiliki gugus tersebut."


    # ================= LOGIKA OUTPUT SETELAH KLIK =================
    if tombol_analisis:
        with st.spinner("⏳ Sedang mereaksikan sampel di dalam tabung reaksi..."):
            time.sleep(1.5)
            
        st.write("")
        st.markdown("### 📊 Lembar Hasil Analisis")
        
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
