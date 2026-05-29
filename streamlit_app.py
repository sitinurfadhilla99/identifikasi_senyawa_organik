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
        "sekalikos visualisasi reaksi uji kualitatif senyawa organik di laboratorium secara interaktif."
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
    st.title("📘 BAB 1 — HIDROKARBON")
    st.write("---")
    
    st.markdown("""
    ### Pengertian
    Hidrokarbon adalah senyawa organik yang tersusun dari atom karbon (C) dan hidrogen (H).
    
    ### Jenis Hidrokarbon
    
    **1. Alkana (jenuh)**
    * Ikatan tunggal C–C
    * Rumus umum: $C_nH_{2n+2}$
    * Sifat:
        * Sukar bereaksi
        * Mudah terbakar
        * Tidak larut dalam air
        
    **2. Alkena (tidak jenuh)**
    * Memiliki ikatan rangkap dua (C=C)
    * Rumus umum: $C_nH_{2n}$
    
    **3. Alkuna**
    * Memiliki ikatan rangkap tiga (C≡C)
    * Rumus umum: $C_nH_{2n-2}$
    
    **4. Senyawa Aromatik**
    * Contoh utama: benzena
    * Memiliki cincin aromatik yang stabil
    
    ---
    
    ### Sifat Fisika Hidrokarbon
    Semakin banyak atom C:
    * titik didih meningkat
    * titik leleh meningkat
    
    * Alkana rantai pendek $\\rightarrow$ gas
    * Rantai sedang $\\rightarrow$ cair
    * Rantai panjang $\\rightarrow$ padat
    
    ---
    
    ### Sifat Kimia Hidrokarbon
    * **Reaksi Pembakaran:** Menghasilkan $CO_2$ dan $H_2O$.
    * **Reaksi Substitusi:** Terjadi pada alkana.
    * **Reaksi Adisi:** Terjadi pada alkena dan alkuna karena adanya ikatan rangkap.
    
    ---
    
    ### Uji Penting
    * **Uji Brom:** Digunakan untuk membedakan senyawa jenuh dan tidak jenuh. Warna brom hilang $\\rightarrow$ senyawa tidak jenuh
    * **Uji Bayer:** Menggunakan $KMnO_4$. Warna ungu hilang $\\rightarrow$ terdapat ikatan rangkap
    """)

# --- BAB 2 ---
elif pilihan_halaman == "📙 BAB 2 ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB 2 — ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    st.markdown("""
    ### 1. Alkohol
    
    **Pengertian**
    Alkohol adalah senyawa yang memiliki gugus hidroksil (-OH).
    * Rumus umum: R-OH
    * Contoh: Metanol, Etanol, Propanol
    
    ---
    
    **Klasifikasi Alkohol**
    * **Alkohol Primer:** Gugus -OH terikat pada atom C primer.
    * **Alkohol Sekunder:** Gugus -OH terikat pada atom C sekunder.
    * **Alkohol Tersier:** Gugus -OH terikat pada atom C tersier.
    
    ---
    
    **Sifat Alkohol**
    * **Sifat Fisika:**
        * Alkohol rantai pendek larut dalam air
        * Memiliki titik didih tinggi
        * Beberapa memiliki bau khas
    * **Sifat Kimia:**
        * Mengalami oksidasi
        * Mengalami substitusi
        * Dapat membentuk ester
        
    ---
    
    **Uji Identifikasi Alkohol**
    * **Pereaksi Lucas:** Membedakan alkohol primer, sekunder, dan tersier. Tersier $\\rightarrow$ paling cepat keruh
    * **Pereaksi Jones:** Mendeteksi alkohol primer dan sekunder. Warna berubah dari oranye menjadi hijau
    * **Uji Iodoform:** Positif pada alkohol tertentu dan metil keton. Menghasilkan endapan kuning
    
    ---
    
    ### 2. Eter
    
    **Pengertian**
    Eter adalah senyawa dengan gugus: R-O-R
    
    **Sifat Eter**
    * Titik didih lebih rendah dari alkohol
    * Kurang larut dalam air
    * Banyak digunakan sebagai pelarut
    
    ---
    
    ### 3. Fenol
    
    **Pengertian**
    Fenol adalah senyawa aromatik yang memiliki gugus -OH pada cincin benzena.
    
    **Sifat Fenol**
    * Bersifat asam lemah
    * Lebih reaktif dibanding alkohol
    
    ---
    
    **Uji Fenol**
    * **Uji $FeCl_3$:** Membentuk warna ungu/biru/hijau
    * **Uji Brom:** Membentuk endapan putih
    """)

# --- BAB 3 ---
elif pilihan_halaman == "📗 BAB 3 ALDEHID DAN KETON":
    st.title("📗 BAB 3 — ALDEHID DAN KETON")
    st.write("---")
    
    st.markdown("""
    ### Pengertian
    Aldehid dan keton adalah senyawa yang memiliki gugus karbonil: C=O
    
    ---
    
    ### Perbedaan Aldehid dan Keton
    
    **Aldehid**
    * Gugus karbonil di ujung rantai
    * Mudah dioksidasi
    * Contoh: Formaldehid, Asetaldehid
    
    **Keton**
    * Gugus karbonil di tengah rantai
    * Sulit dioksidasi
    * Contoh: Aseton
    
    ---
    
    ### Sifat Fisika
    * Suku rendah mudah larut dalam air
    * Memiliki bau khas
    * Titik didih lebih tinggi dari hidrokarbon
    
    ---
    
    ### Sifat Kimia
    **Reaksi Adisi**  
    Dapat bereaksi dengan:
    * Na-bisulfit
    * Alkohol
    * Pereaksi Schiff
    
    ---
    
    ### Uji Identifikasi
    * **Pereaksi Schiff:** Aldehid $\\rightarrow$ warna ungu/merah muda, Keton $\\rightarrow$ negatif
    * **Pereaksi Na-Bisulfit:** Membentuk kristal/endapan
    * **Uji Daya Reduksi:** Aldehid dapat mereduksi pereaksi tertentu, sedangkan keton tidak.
    """)

# --- BAB 4 ---
elif pilihan_halaman == "📕 BAB 4 ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB 4 — ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.markdown("""
    ### 1. Asam Karboksilat
    
    **Pengertian**  
    Asam karboksilat adalah senyawa organik yang memiliki gugus karboksil: **-COOH**  
    * Rumus umum: R-COOH
    * Contoh: Asam format, Asam asetat, Asam propionat
    
    ---
    
    **Sifat Asam Karboksilat**
    * **Sifat Fisika:**
        * Memiliki bau khas
        * Larut dalam air untuk rantai pendek
        * Titik didih tinggi karena ikatan hidrogen
    * **Sifat Kimia:**
        * Bersifat asam lemah
        * Bereaksi dengan basa membentuk garam
        * Bereaksi dengan alkohol membentuk ester
        
    ---
    
    **Reaksi Penting**  
    * **Reaksi Esterifikasi:**  
      Asam karboksilat + alkohol $\\rightarrow$ ester + air  
      Contoh:  
      $CH_3COOH + C_2H_5OH \\rightarrow CH_3COOC_2H_5 + H_2O$  
      Reaksi ini menghasilkan aroma harum khas ester.
      
    ---
    
    **Uji Asam Karboksilat**
    * **Uji Lakmus:** Mengubah lakmus biru menjadi merah
    * **Reaksi dengan $NaHCO_3$:** Menghasilkan gelembung gas $CO_2$.
    
    ---
    
    ### 2. Derivat Asam Karboksilat
    
    **Pengertian**  
    Derivat asam karboksilat adalah turunan asam karboksilat yang gugus -OH nya diganti gugus lain.
    
    ---
    
    **Jenis Derivat**
    
    **1. Ester**
    * Rumus: R-COOR
    * Sifat:
        * Berbau harum
        * Banyak digunakan sebagai: parfum, perasa makanan, pelarut
    * Pembentukan: Melalui reaksi esterifikasi.
    
    ---
    
    **2. Amida**
    * Rumus: $R-CONH_2$
    * Sifat:
        * Memiliki titik didih tinggi
        * Digunakan dalam industri plastik dan obat
        
    ---
    
    **3. Anhidrida Asam**
    * Terbentuk dari dua molekul asam karboksilat.
    * Sifat:
        * Mudah bereaksi dengan air
        * Bersifat reaktif
        
    ---
    
    **4. Asil Halida**
    * Contoh: R-COCl
    * Sifat:
        * Sangat reaktif
        * Mudah terhidrolisis
        
    ---
    
    **Perbandingan Reaktivitas Derivat**  
    Urutan reaktivitas:  
    Asil Halida > Anhidrida > Ester > Amida  
    Semakin reaktif $\\rightarrow$ semakin mudah mengalami substitusi.
    
    ---
    
    **Fungsi dan Kegunaan**
    """)
    
    # Menampilkan tabel kegunaan menggunakan format bawaan Streamlit
    data_fungsi = {
        "Senyawa": ["Asam asetat", "Ester", "Amida", "Asil halida"],
        "Kegunaan": ["Cuka makanan", "Parfum dan perasa", "Plastik dan obat", "Sintesis organik"]
    }
    st.table(data_fungsi)
    
    st.markdown("""
    ---
    
    ### Kesimpulan Bab 4
    * Asam karboksilat memiliki gugus fungsi -COOH.
    * Bersifat asam lemah dan dapat membentuk ester.
    * Derivat asam karboksilat meliputi: ester, amida, anhidrida, asil halida.
    * Banyak digunakan dalam industri makanan, parfum, obat, dan kimia organik.
    """)

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
