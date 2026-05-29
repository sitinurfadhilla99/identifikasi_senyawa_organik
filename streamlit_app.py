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

# --- BAB 1 ---
elif pilihan_halaman == "📘 BAB 1 HIDROKARBON":
    st.title("📘 BAB I. HIDROKARBON")
    st.write("---")
    
    st.markdown("""
    Hidrokarbon adalah senyawa organik yang hanya terdiri dari unsur karbon (C) dan hidrogen (H). Berdasarkan jenis ikatannya, hidrokarbon alifatik dibagi menjadi hidrokarbon jenuh (alkana) dan tidak jenuh (alkena dan alkuna).

    #### **A. Sifat Fisika Hidrokarbon**

    1. **Wujud Zat (pada suhu kamar):**
       * Suku rendah ($C_1 - C_4$) berwujud gas (misalnya metana, etana, etena, etuna).
       * Suku sedang ($C_5 - C_{17}$) berwujud cair (misalnya pentana, heksana, benzena).
       * Suku tinggi ($\ge C_{18}$) berwujud padat (misalnya parafin padat).
    2. **Kelarutan:** Bersifat nonpolar, sehingga **tidak larut dalam air** (pelarut polar), tetapi larut dengan baik dalam pelarut organik nonpolar seperti kloroform ($CHCl_3$), karbon tetraklorida ($CCl_4$), atau eter.
    3. **Titik Didih dan Titik Leleh:** Meningkat seiring dengan bertambahnya massa molekul (panjang rantai karbon). Untuk isomer dengan jumlah karbon sama, senyawa dengan rantai lurus memiliki titik didih lebih tinggi daripada rantai bercabang karena luas permukaan kontak antarmolekul yang lebih besar.
    4. **Densitas:** Memiliki massa jenis yang lebih kecil daripada air, sehingga jika dicampur dengan air, lapisan hidrokarbon akan berada di bagian atas.

    #### **B. Sifat Kimia & Reaksi Identifikasi Hidrokarbon**

    1. **Alkana (Hidrokarbon Jenuh)**
       * Disebut juga *parafin* (afinitas kecil) karena sangat tidak reaktif terhadap sebagian besar pereaksi seperti asam kuat, basa kuat, dan oksidator pada suhu kamar.
       * **Uji Iodo (Substitusi Halogen):** Alkana dapat bereaksi dengan halogen ($I_2$) melalui reaksi substitusi radikal bebas dengan bantuan paparan sinar ultraviolet (UV) atau pemanasan tinggi. Reaksi ini berjalan lambat dan ditandai dengan memudarnya warna ungu dari iodium.
    """)
    
    st.latex(r"\text{CH}_4 + \text{I}_2 \xrightarrow{\text{Sinar UV / }\Delta} \text{CH}_3\text{I} + \text{HI}")
    
    st.markdown("""
    2. **Alkena dan Alkuna (Hidrokarbon Tidak Jenuh)**
       * Sangat reaktif karena memiliki ikatan rangkap ($\text{C}=\text{C}$ atau $\text{C}\equiv\text{C}$) yang kaya akan elektron, sehingga mudah mengalami reaksi adisi (pemutusan ikatan rangkap).
       * **Uji Adisi Bromin/Iodium:** Mengadisi halogen pada ikatan rangkap tanpa memerlukan bantuan sinar UV.
    """)
    
    st.latex(r"\text{R-CH}=\text{CH-R} + \text{I}_2 \rightarrow \text{R-CH(I)-CH(I)-R (Warna iodium memudar)}")
    
    st.markdown("""
       * **Uji Bayer (Oksidasi dengan $KMnO_4$):** Alkena/alkuna dioksidasi oleh larutan kalium permanganat encer dalam suasana netral/basa menghasilkan glikol. Uji positif ditandai dengan **hilangnya warna ungu $KMnO_4$** dan terbentuknya **endapan cokelat $MnO_2$**.
    """)
    
    st.latex(r"3\text{CH}_2=\text{CH}_2 + 2\text{KMnO}_4 + 4\text{H}_2\text{O} \rightarrow 3\text{HO-CH}_2\text{-CH}_2\text{-OH} + 2\text{MnO}_2\downarrow \text{ (cokelat)} + 2\text{KOH}")
    
    st.markdown("""
    3. **Benzena (Hidrokarbon Aromatik)**
       * Memiliki struktur siklik dengan elektron pi yang terdelokalisasi (resonansi) sehingga sangat stabil.
       * **Uji Bakar:** Ketika dibakar, benzena menghasilkan **nyala api berminyak dengan jelaga hitam yang sangat tebal**. Hal ini disebabkan oleh tingginya kadar persentase karbon dalam molekul benzena dibandingkan hidrogennya.
    """)
    
    st.latex(r"2\text{C}_6\text{H}_6 + 15\text{O}_2 \rightarrow 12\text{CO}_2 + 6\text{H}_2\text{O (Pembakaran sempurna)}")
    st.latex(r"\text{Benzena} + \text{O}_2 \rightarrow \text{C}_{(s)\text{ [Jelaga hitam]}} + \text{CO} + \text{H}_2\text{O (Pembakaran tidak sempurna)}")
    
    st.markdown("""
       * **Reaksi Substitusi Elektrofilik:** Benzena sukar diadisi, tetapi mudah mengalami substitusi. Contohnya adalah reaksi Nitrasi menggunakan campuran asam nitrat pekat dan asam sulfat pekat.
    """)
    
    st.latex(r"\text{C}_6\text{H}_6 + \text{HNO}_3 \xrightarrow{\text{H}_2\text{SO}_4\text{ pekat}} \text{C}_6\text{H}_5\text{NO}_2 \text{ (Nitrobenzena)} + \text{H}_2\text{O}")

# --- BAB 2 ---
elif pilihan_halaman == "📙 BAB 2 ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB II. ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    st.markdown("""
    #### **A. Reaksi Alkohol dan Eter**

    1. **Pereaksi Lucas (Substitusi Gugus $-OH$ oleh Cl):** Digunakan untuk membedakan alkohol primer, sekunder, dan tersier menggunakan campuran $HCl$ pekat dan katalis $ZnCl_2$.
       * *Alkohol $3^\circ$:* Bereaksi seketika (larutan langsung keruh/terbentuk dua lapisan).
       * *Alkohol $2^\circ$:* Bereaksi dalam waktu 5–10 menit dengan sedikit pemanasan.
       * *Alkohol $1^\circ$:* Tidak bereaksi pada suhu kamar.
    """)
    
    st.latex(r"\text{R}_3\text{C-OH (Alkohol }3^\circ) + \text{HCl} \xrightarrow{\text{ZnCl}_2} \text{R}_3\text{C-Cl}\downarrow \text{ (Keruh/Alkil klorida)} + \text{H}_2\text{O}")
    
    st.markdown("""
    2. **Pereaksi Jones (Oksidasi Alkohol):** Menggunakan kromium trioksida ($CrO_3$) dalam asam sulfat.
       * *Alkohol 1°* $\rightarrow$ Aldehida $\rightarrow$ Asam Karboksilat.
       * *Alkohol 2°* $\rightarrow$ Keton.
       * *Alkohol 3°* $\rightarrow$ Tidak dapat dioksidasi (Warna jingga pereaksi tidak berubah).
    """)
    
    st.latex(r"\text{R-CH}_2\text{-OH (Alkohol }1^\circ) \xrightarrow{\text{CrO}_3/\text{H}_2\text{SO}_4} \text{R-COOH (Asam Karboksilat) [Warna berubah Jingga }\rightarrow\text{ Hijau]}")
    st.latex(r"\text{R}_2\text{CH-OH (Alkohol }2^\circ) \xrightarrow{\text{CrO}_3/\text{H}_2\text{SO}_4} \text{R}_2\text{C}=\text{O (Keton) [Warna berubah Jingga }\rightarrow\text{ Hijau]}")
    
    st.markdown("""
    3. **Uji Iodoform:** Khusus untuk alkohol yang memiliki gugus metil alfa ($\text{CH}_3\text{-CH(OH)-}$), seperti etanol atau 2-propanol. Bereaksi dengan $I_2$ dalam suasana basa membentuk endapan kuning iodoform ($CHI_3$).
    """)
    
    st.latex(r"\text{R-CH(OH)-CH}_3 + 4\text{I}_2 + 6\text{NaOH} \rightarrow \text{R-COONa} + \text{CHI}_3\downarrow \text{ (Endapan Kuning)} + 5\text{NaI} + 5\text{H}_2\text{O}")
    
    st.markdown("""
    4. **Pereaksi Ceric Ammonium Nitrate (CAN):** Alkohol membentuk kompleks berwarna merah, sedangkan eter memberikan hasil negatif.
    """)
    
    st.latex(r"\text{ROH} + [ \text{Ce(NO}_3)_6 ]^{2-} \rightarrow [ \text{Ce(OR)(NO}_3)_5 ]^{2-} \text{ (Kompleks Merah)} + \text{HNO}_3")
    
    st.markdown("""
    #### **B. Reaksi Fenol**

    1. **Uji Besi(III) Klorida ($FeCl_3$):** Fenol membentuk senyawa kompleks koordinasi yang menghasilkan warna ungu tua/kehitaman yang khas.
    """)
    
    st.latex(r"6\text{C}_6\text{H}_5\text{OH} + \text{FeCl}_3 \rightarrow [\text{Fe}(\text{OC}_6\text{H}_5)_6]^{3-} \text{ (Kompleks Ungu)} + 3\text{H}^+ + 3\text{Cl}^-")
    
    st.markdown("""
    2. **Reaksi Substitusi (Brominasi Air Brom):** Fenol sangat reaktif terhadap substitusi aromatik sehingga langsung mengalami trisubstitusi menghasilkan endapan putih 2,4,6-tribromofenol tanpa bantuan katalis.
    """)
    
    st.latex(r"\text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2\text{ (dalam H}_2\text{O)} \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow \text{ (Endapan Putih)} + 3\text{HBr}")

# --- BAB 3 ---
elif pilihan_halaman == "📗 BAB 3 ALDEHID DAN KETON":
    st.title("📗 BAB III. ALDEHID DAN KETON")
    st.write("---")
    
    st.markdown("""
    Aldehida dan keton sama-sama memiliki gugus karbonil ($\text{C}=\text{O}$), namun aldehida bertindak sebagai reduktor kuat karena memiliki atom hidrogen yang terikat langsung pada karbon karbonil ($\text{R-CHO}$).

    #### **A. Reaksi Adisi Karbonil**

    1. **Adisi Natrium Bisulfit ($NaHSO_3$):** Baik aldehida maupun keton (terutama metil keton) dapat diadisi oleh bisulfit membentuk kristal padat berwarna putih.
    """)
    
    st.latex(r"\text{R-CHO} + \text{NaHSO}_3 \rightarrow \text{R-CH(OH)-SO}_3\text{Na (Kristal Putih)}")
    
    st.markdown("""
    2. **Pembentukan Hemiasetal/Asetal:** Reaksi nukleofilik reversibel dengan alkohol dalam suasana asam ($HCl$).
    """)
    
    st.latex(r"\text{R-CHO (Aldehida)} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OH)(OR') (Hemiasetal)}")
    st.latex(r"\text{R-CH(OH)(OR')} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OR')}_2 \text{ (Asetal)} + \text{H}_2\text{O}")
    
    st.markdown("""
    #### **B. Reaksi Diferensiasi (Uji Daya Reduksi Aldehida)**

    1. **Uji Tollens (Cermin Perak):** Aldehida mereduksi ion kompleks $[\text{Ag(NH}_3)_2]^+$ menjadi logam perak yang melapisi dinding tabung reaksi, sementara keton tidak bereaksi.
    """)
    
    st.latex(r"\text{R-CHO} + 2[\text{Ag(NH}_3)_2]^+ + 3\text{OH}^- \rightarrow \text{R-COO}^- + 2\text{Ag}\downarrow \text{ (Cermin Perak)} + 4\text{NH}_3 + 2\text{H}_2\text{O}")
    
    st.markdown("""
    2. **Uji Fehling:** Aldehida mereduksi ion $\text{Cu}^{2+}$ yang dikomplekskan oleh ion tartrat dalam suasana basa, menghasilkan endapan merah bata kupro oksida ($\text{Cu}_2\text{O}$).
    """)
    
    st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow \text{ (Endapan Merah Bata)} + 3\text{H}_2\text{O}")
    
    st.markdown("""
    3. **Uji Benedict:** Prinsipnya sama dengan Fehling, namun menggunakan pengkompleks sitrat. Mengonfirmasi adanya aldehida pereduksi melalui pembentukan endapan merah bata.
    """)
    
    st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+}\text{(sitrat)} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow \text{ (Endapan Merah Bata)} + 3\text{H}_2\text{O}")

# --- BAB 4 ---
elif pilihan_halaman == "📕 BAB 4 ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.markdown("""
    #### **A. Reaksi Asam Karboksilat**

    1. **Reaksi dengan Basa Lemah ($NaHCO_3$):** Asam karboksilat cukup asam untuk mendeprotonasi natrium bikarbonat, menghasilkan garam, air, dan **pelepasan gas karbon dioksida ($CO_2$) secara cepat (*effervescence*)**. Fenol tidak dapat mengalami reaksi ini.
    """)
    
    st.latex(r"\text{R-COOH} + \text{NaHCO}_3 \rightarrow \text{R-COONa} + \text{H}_2\text{O} + \text{CO}_2\uparrow \text{ (Gas)}")
    
    st.markdown("""
    Jika gas $CO_2$ dialirkan ke dalam air barit ($\text{Ba(OH)}_2$), akan terbentuk endapan putih:
    """)
    
    st.latex(r"\text{CO}_2 + \text{Ba(OH)}_2 \rightarrow \text{BaCO}_3\downarrow \text{ (Endapan Putih)} + \text{H}_2\text{O}")
    
    st.markdown("""
    2. **Esterifikasi Fischer:** Kondensasi antara asam karboksilat dengan alkohol menggunakan katalis asam kuat ($\text{H}_2\text{SO}_4$) menghasilkan senyawa ester yang beraroma harum (seperti buah-buahan).
    """)
    
    st.latex(r"\text{R-COOH} + \text{R'-OH} \xrightarrow{\text{H}_2\text{SO}_4\text{, }\Delta} \text{R-COOR'} \text{ (Ester beraroma)} + \text{H}_2\text{O}")
    
    st.markdown("""
    3. **Oksidasi Asam Karboksilat:** Karena atom C karbonil memiliki bilangan oksidasi +3, asam karboksilat tertentu (seperti asam oksalat atau asam format) masih dapat dioksidasi oleh $\text{KMnO}_4$ menjadi $\text{CO}_2$ (biloks +4).
    """)
    
    st.latex(r"\text{R-COOH} \xrightarrow{\text{KMnO}_4 / \text{H}_2\text{SO}_4} \text{CO}_2\uparrow + \text{H}_2\text{O}")
    
    st.markdown("""
    #### **B. Reaksi Identifikasi Derivat Asam Karboksilat (Uji Asam Hidroksamat)**

    Derivat asam karboksilat (ester, amida, anhidrida, asil halida) direaksikan terlebih dahulu dengan hidroksilamin ($\text{NH}_2\text{OH}$) menghasilkan asam hidroksamat. Sifat khas asam hidroksamat ini adalah membentuk senyawa kompleks khelat berwarna ungu intens jika ditambahkan larutan $\text{FeCl}_3$.

    1. *Pembentukan Asam Hidroksamat (dari Ester):*
    """)
    
    st.latex(r"\text{R-COOR'} \text{ (Ester)} + \text{NH}_2\text{OH} \rightarrow \text{R-CONH-OH (Asam Hidroksamat)} + \text{R'OH}")
    
    st.markdown("""
    2. *Pembentukan Kompleks Berwarna dengan $\text{FeCl}_3$:*
    """)
    
    st.latex(r"3\text{R-CONH-OH} + \text{FeCl}_3 \rightarrow \text{Fe(R-CONHO)}_3 \text{ (Kompleks Ungu)} + 3\text{HCl}")

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
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Hidroksilamin menyerang karbonil pada aldehid/keton, melepaskan air (kondensasi), and membentuk ikatan rangkap C=N baru (oksim) yang mengendap."
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
            time.sleep(1.5)
            
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
