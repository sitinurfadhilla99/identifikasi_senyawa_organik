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
    
    pilihan_halaman = st.sidebar.radio(
        "Navigasi Menu:",
        [
            "🏠 HALAMAN UTAMA", 
            "📘 BAB I. HIDROKARBON", 
            "📙 BAB II. ALKOHOL, ETER, DAN FENOL", 
            "📗 BAB III. ALDEHID DAN KETON", 
            "📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA", 
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
    st.markdown("""
    ### **RANGKUMAN MATERI PRAKTIKUM KIMIA ORGANIK**
    Silakan gunakan menu navigasi di sebelah kiri untuk membaca kesatuan rangkuman materi praktikum Kimia Organik yang komprehensif, menggabungkan seluruh informasi sifat fisika, sifat kimia, serta persamaan reaksi lengkap dari keempat bab secara sistematis.
    """)

# --- BAB I ---
elif pilihan_halaman == "📘 BAB I. HIDROKARBON":
    st.title("📘 BAB I. HIDROKARBON")
    st.write("---")
    
    st.markdown("""
    Hidrokarbon adalah senyawa organik yang seluruh strukturnya hanya tersusun atas unsur karbon (C) dan hidrogen (H). Berdasarkan jenis ikatannya, hidrokarbon alifatik dibagi menjadi hidrokarbon jenuh (alkana) dan tidak jenuh (alkena dan alkuna). Sementara itu, hidrokarbon aromatik memiliki rantai siklik konjugasi yang sangat stabil.

    #### **A. Sifat Fisika Hidrokarbon**

    * **Wujud Zat (pada suhu kamar):** * Suku rendah ($C_1 - C_4$) berwujud gas (contoh: metana, etana, etena, etuna).
      * Suku sedang ($C_5 - C_{17}$) berwujud cair (contoh: pentana, heksana, benzena).
      * Suku tinggi ($\ge C_{18}$) berwujud padat (contoh: parafin padat).
    * **Kelarutan:** Bersifat nonpolar, sehingga tidak larut dalam air (pelarut polar). Hidrokarbon larut dengan baik dalam sesama pelarut organik nonpolar seperti kloroform ($CHCl_3$), karbon tetraklorida ($CCl_4$), atau eter.
    * **Titik Didih dan Titik Leleh:** Meningkat seiring bertambahnya massa molekul (panjang rantai karbon). Untuk isomer dengan jumlah atom karbon sama, senyawa dengan rantai lurus memiliki titik didih lebih tinggi dibandingkan rantai bercabang karena luas permukaan kontak antarmolekul yang lebih besar.
    * **Densitas:** Memiliki massa jenis (densitas) yang lebih kecil daripada air. Jika dicampur dengan air, lapisan hidrokarbon akan selalu berada di bagian atas.

    #### **B. Sifat Kimia & Reaksi Identifikasi Hidrokarbon**

    **1. Alkana (Hidrokarbon Jenuh)**
    * Disebut juga parafin (afinitas kecil) karena sangat tidak reaktif terhadap sebagian besar pereaksi seperti asam kuat, basa kuat, dan oksidator pada suhu kamar.
    * **Uji Iodo (Substitusi Halogen):** Alkana dapat bereaksi dengan halogen ($I_2$) melalui reaksi substitusi radikal bebas dengan bantuan paparan sinar ultraviolet (UV) atau pemanasan tinggi. Reaksi berjalan lambat dan ditandai dengan memudarnya warna ungu dari iodium.
    """)
    
    st.latex(r"\text{CH}_4 + \text{I}_2 \xrightarrow{\text{Sinar UV / }\Delta} \text{CH}_3\text{I} + \text{HI}")
    
    st.markdown("""
    **2. Alkena dan Alkuna (Hidrokarbon Tidak Jenuh)**
    * Sangat reaktif karena memiliki ikatan rangkap ($\text{C}=\text{C}$ atau $\text{C}\equiv\text{C}$) yang kaya akan elektron, sehingga mudah mengalami pemutusan ikatan rangkap (adisi).
    * **Uji Adisi Iodium:** Mengadisi halogen pada ikatan rangkap tanpa memerlukan bantuan sinar UV. Ditandai dengan warna ungu iodium yang memudar/hilang seketika.
    """)
    
    st.latex(r"\text{R-CH}=\text{CH-R} + \text{I}_2 \rightarrow \text{R-CH(I)-CH(I)-R}")
    
    st.markdown("""
    * **Uji Bayer (Oksidasi dengan $KMnO_4$):** Alkena atau alkuna dioksidasi oleh larutan kalium permanganat encer dalam suasana netral/basa menghasilkan senyawa glikol. Uji positif ditandai dengan hilangnya warna ungu $KMnO_4$ dan terbentuknya endapan cokelat $MnO_2$.
    """)
    
    st.latex(r"3\text{CH}_2=\text{CH}_2 + 2\text{KMnO}_4 + 4\text{H}_2\text{O} \rightarrow 3\text{HO-CH}_2\text{-CH}_2\text{-OH} + 2\text{MnO}_2\downarrow \text{ (contoh cokelat)} + 2\text{KOH}")
    
    st.markdown("""
    **3. Benzena (Hidrokarbon Aromatik)**
    * Memiliki struktur siklik dengan elektron pi yang terdelokalisasi (resonansi) yang memenuhi aturan Hückel ($4n+2$), membuat intinya sangat stabil.
    * **Uji Bakar:** Ketika dibakar dengan api langsung pada cawan porselin, benzena menghasilkan nyala api berminyak disertai jelaga hitam yang sangat tebal. Jelaga ini terbentuk akibat tingginya persentase kadar karbon dalam benzena dibandingkan kadar hidrogennya.
    """)
    
    st.latex(r"\text{Benzena} + \text{O}_2 \rightarrow \text{C}_{(s)\text{ [Jelaga hitam]}} + \text{CO} + \text{H}_2\text{O (Pembakaran tidak sempurna)}")
    
    st.markdown("""
    * **Reaksi Substitusi Elektrofilik:** Benzena sukar mengalami adisi melainkan cenderung mengalami reaksi substitusi. Contohnya adalah reaksi Nitrasi menggunakan campuran asam nitrat pekat dan asam sulfat pekat sebagai katalis.
    """)
    
    st.latex(r"\text{C}_6\text{H}_6 + \text{HNO}_3 \xrightarrow{\text{H}_2\text{SO}_4\text{ pekat}} \text{C}_6\text{H}_5\text{NO}_2 \text{ (Nitrobenzena)} + \text{H}_2\text{O}")

# --- BAB II ---
elif pilihan_halaman == "📙 BAB II. ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB II. ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    st.markdown("""
    #### **A. Sifat Fisika & Klasifikasi**

    * **Alkohol ($R-OH$):** Turunan alkana di mana satu atau lebih atom H digantikan oleh gugus hidroksil ($-OH$). Alkohol diklasifikasikan menjadi alkohol primer ($1^\circ$), sekunder ($2^\circ$), dan tersier ($3^\circ$) berdasarkan jenis atom C yang mengikat gugus $-OH$. Alkohol suku rendah mudah larut dalam air karena sanggup membentuk ikatan hidrogen dengan molekul air. Kelarutan berkurang seiring bertambah panjangnya rantai karbon, namun meningkat pada struktur yang bercabang banyak.
    * **Eter ($R^1-O-R^2$):** Isomer fungsional dari alkohol. Titik didih eter jauh lebih rendah dibandingkan alkohol isomernya karena tidak memiliki ikatan hidrogen antar-sesama molekul eter. Kelarutannya dalam air mirip dengan alkohol karena oksigen pada eter masih bisa menerima ikatan hidrogen dari air.
    * **Fenol ($C_6H_5OH$):** Senyawa hidrokarbon aromatik yang mengikat gugus fungsi $-OH$ langsung pada cincin benzena. Berapa padatan/hablur pada suhu kamar, sedikit larut dalam air, dan larutannya bersifat asam lemah karena ion fenoksida yang terbentuk distabilkan oleh resonansi.

    #### **B. Persamaan Reaksi Kimia Alkohol & Eter**

    **1. Pereaksi Lucas (Substitusi Gugus $-OH$ oleh Cl):** Menggunakan campuran $HCl$ pekat dan katalis $ZnCl_2$ untuk membedakan jenis alkohol berdasarkan kecepatan reaksinya.
    * Alkohol $3^\circ$: Bereaksi seketika (larutan langsung keruh/terbentuk dua lapisan terpisah).
    * Alkohol $2^\circ$: Bereaksi dalam waktu 5–10 menit dengan sedikit pemanasan.
    * Alkohol $1^\circ$: Tidak bereaksi pada suhu kamar.
    """)
    
    st.latex(r"\text{R}_3\text{C-OH (Alkohol }3^\circ) + \text{HCl} \xrightarrow{\text{ZnCl}_2} \text{R}_3\text{C-Cl}\downarrow \text{ (Keruh/Alkil klorida)} + \text{H}_2\text{O}")
    
    st.markdown("""
    **2. Pereaksi Jones (Oksidasi Alkohol):** Menggunakan kromium trioksida ($CrO_3$) dalam asam sulfat pekat. Uji positif ditandai dengan perubahan warna pereaksi dari jingga menjadi hijau.
    * Alkohol $1^\circ$ dioksidasi menjadi Aldehida, lalu berlanjut menjadi Asam Karboksilat.
    * Alkohol $2^\circ$ dioksidasi menjadi Keton.
    * Alkohol $3^\circ$ tidak dapat dioksidasi (warna tetap jingga).
    """)
    
    st.latex(r"\text{R-CH}_2\text{-OH (Alkohol }1^\circ) \xrightarrow{\text{CrO}_3/\text{H}_2\text{SO}_4} \text{R-COOH (Asam Karboksilat) [Jingga }\rightarrow\text{ Hijau]}")
    st.latex(r"\text{R}_2\text{CH-OH (Alkohol }2^\circ) \xrightarrow{\text{CrO}_3/\text{H}_2\text{SO}_4} \text{R}_2\text{C}=\text{O (Keton) [Jingga }\rightarrow\text{ Hijau]}")
    
    st.markdown("""
    **3. Uji Iodoform:** Khusus untuk alkohol yang memiliki gugus metil alfa ($\text{CH}_3\text{-CH(OH)-}$), seperti etanol atau 2-propanol. Bereaksi dengan $I_2$ dalam suasana basa ($NaOH$) membentuk endapan kuning kristal iodoform ($CHI_3$) yang berbau khas.
    """)
    
    st.latex(r"\text{R-CH(OH)-CH}_3 + 4\text{I}_2 + 6\text{NaOH} \rightarrow \text{R-COONa} + \text{CHI}_3\downarrow \text{ (Endapan Kuning)} + 5\text{NaI} + 5\text{H}_2\text{O}")
    
    st.markdown("""
    **4. Pereaksi Ceric Ammonium Nitrate (CAN):** Alkohol bereaksi membentuk senyawa kompleks koordinasi berwarna merah cerah, sedangkan eter memberikan hasil negatif (warna tetap).
    """)
    
    st.latex(r"\text{ROH} + [ \text{Ce(NO}_3)_6 ]^{2-} \rightarrow [ \text{Ce(OR)(NO}_3)_5 ]^{2-} \text{ (Kompleks Merah)} + \text{HNO}_3")
    
    st.markdown("""
    #### **C. Persamaan Reaksi Kimia Fenol**

    **1. Reaksi dengan Basa Kuat ($NaOH$):** Membentuk garam natrium fenoksida yang larut dalam air (menunjukkan sifat asam lemah fenol).
    """)
    
    st.latex(r"\text{C}_6\text{H}_5\text{OH} + \text{NaOH} \rightarrow \text{C}_6\text{H}_5\text{ONa (Natrium fenoksida)} + \text{H}_2\text{O}")
    
    st.markdown("""
    **2. Uji Besi(III) Klorida ($FeCl_3$):** Ion fenoksida membentuk senyawa kompleks koordinasi dengan besi(III) yang menghasilkan warna ungu tua/kehitaman yang khas.
    """)
    
    st.latex(r"6\text{C}_6\text{H}_5\text{OH} + \text{FeCl}_3 \rightarrow [\text{Fe}(\text{OC}_6\text{H}_5)_6]^{3-} \text{ (Kompleks Ungu)} + 3\text{H}^+ + 3\text{Cl}^-")
    
    st.markdown("""
    **3. Reaksi Substitusi Aromatik (Trisubstitusi Air Brom):** Cincin aromatik pada fenol sangat reaktif karena efek aktivasi dari gugus $-OH$. Jika direaksikan dengan air brom ($Br_2/H_2O$) yang bersifat polar, akan langsung mengalami trisubstitusi membentuk endapan putih 2,4,6-tribromofenol.
    """)
    
    st.latex(r"\text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2\text{ (dalam H}_2\text{O)} \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow \text{ (Endapan Putih)} + 3\text{HBr}")

# --- BAB III ---
elif pilihan_halaman == "📗 BAB III. ALDEHID DAN KETON":
    st.title("📗 BAB III. ALDEHID DAN KETON")
    st.write("---")
    
    st.markdown("""
    Aldehida ($\text{R-CHO}$) dan keton ($\text{R-CO-R'}$) adalah senyawa organik isomer fungsional yang sama-sama memiliki gugus fungsi karbonil ($\text{C}=\text{O}$). Perbedaan utamanya terletak pada atom C karbonil aldehida yang mengikat minimal satu atom hidrogen, sedangkan pada keton terikat pada dua gugus alkil/aril.

    #### **A. Sifat Fisika**

    Metanal (formaldehida) merupakan suku paling rendah yang berwujud gas pada suhu kamar dengan bau menyengat. Suku-suku aldehida rendah lainnya berupa cairan dengan bau yang semakin harum (seperti aroma buah-buahan) seiring bertambah panjangnya rantai C. Keton suku rendah (seperti aseton atau propanon) berupa cairan encer, mudah larut dalam air, mudah menguap, dan memiliki aroma yang segar.

    #### **B. Reaksi Adisi Karbonil**

    **1. Adisi Natrium Bisulfit ($NaHSO_3$):** Reaksi adisi nukleofilik pada gugus karbonil aldehida atau metil keton menghasilkan senyawa aduk berupa kristal padat berwarna putih yang sukar larut.
    """)
    
    st.latex(r"\text{R-CHO} + \text{NaHSO}_3 \rightarrow \text{R-CH(OH)-SO}_3\text{Na (Kristal Putih)}")
    
    st.markdown("""
    **2. Pembentukan Hemiasetal dan Asetal:** Reaksi reversibel gugus karbonil dengan alkohol dalam suasana asam gas $HCl$.
    """)
    
    st.latex(r"\text{R-CHO (Aldehida)} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OH)(OR') (Hemiasetal)}")
    st.latex(r"\text{R-CH(OH)(OR')} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OR')}_2 \text{ (Asetal)} + \text{H}_2\text{O}")
    
    st.markdown("""
    #### **C. Reaksi Diferensiasi (Uji Daya Reduksi Aldehida)**

    Aldehida bertindak sebagai reduktor kuat karena keberadaan atom hidrogen pada karbon karbonilnya, sedangkan keton tidak memiliki daya pereduksi dan memberikan hasil negatif pada uji-uji berikut:

    **1. Uji Tollens (Cermin Perak):** Aldehida mengeksidasi dirinya menjadi asam karboksilat sekaligus mereduksi ion kompleks perak beramoniak $[\text{Ag(NH}_3)_2]^+$ menjadi logam perak mendesak yang menempel di dinding tabung reaksi membentuk cermin perak.
    """)
    
    st.latex(r"\text{R-CHO} + 2[\text{Ag(NH}_3)_2]^+ + 3\text{OH}^- \rightarrow \text{R-COO}^- + 2\text{Ag}\downarrow \text{ (Cermin Perak)} + 4\text{NH}_3 + 2\text{H}_2\text{O}")
    
    st.markdown("""
    **2. Uji Fehling:** Aldehida mereduksi ion $\text{Cu}^{2+}$ yang berada dalam bentuk kompleks tartrat basa, menghasilkan endapan merah bata kupro oksida ($\text{Cu}_2\text{O}$).
    """)
    
    st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow \text{ (Endapan Merah Bata)} + 3\text{H}_2\text{O}")
    
    st.markdown("""
    **3. Uji Benedict:** Memiliki prinsip kerja yang serupa dengan Uji Fehling, namun ion $\text{Cu}^{2+}$ dikomplekskan oleh sitrat. Pereaksi berada dalam kondisi alkalis lemah untuk menghasilkan endapan merah bata $\text{Cu}_2\text{O}$ saat direaksikan dengan aldehida.
    """)
    
    st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+}\text{(sitrat)} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow \text{ (Endapan Merah Bata)} + 3\text{H}_2\text{O}")

# --- BAB IV ---
elif pilihan_halaman == "📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.markdown("""
    Asam karboksilat memiliki gugus fungsi karboksil ($-COOH$), senyawa gabungan dari gugus karbonil dan hidroksil. Derivat atau turunan asam karboksilat (seperti ester, halida asam/asil halida, anhidrida asam, dan amida) terbentuk ketika gugus $-OH$ pada karboksilat digantikan oleh nukleofil lain.

    #### **A. Sifat Fisika**

    Asam karboksilat rantai pendek ($C_1 - C_4$) memiliki kelarutan yang sangat baik di dalam air karena kemampuan gugus $-COOH$ membentuk ikatan hidrogen antarmolekul yang kuat membentuk dimer. Kelarutan senyawa akan semakin menurun seiring dengan bertambah tingginya bobot molekul (rantai alkil nonpolar semakin panjang). Titik didih asam karboksilat relatif tinggi dibandingkan senyawa organik lain dengan berat molekul setara.

    #### **B. Persamaan Reaksi Kimia Asam Karboksilat**

    **1. Reaksi dengan Basa Kuat ($NaOH$):** Menghasilkan garam karboksilat yang larut dan air.
    """)
    
    st.latex(r"\text{R-COOH} + \text{NaOH} \rightarrow \text{R-COONa} + \text{H}_2\text{O}")
    
    st.markdown("""
    **2. Reaksi dengan Basa Lemah ($NaHCO_3$):** Asam karboksilat tergolong cukup asam untuk mendeprotonasi natrium bikarbonat, menghasilkan garam, air, dan pelepasan gas karbon dioksida secara cepat (effervescence). Reaksi ini membedakan asam karboksilat dengan fenol (fenol tidak bereaksi dengan $NaHCO_3$).
    """)
    
    st.latex(r"\text{R-COOH} + \text{NaHCO}_3 \rightarrow \text{R-COONa} + \text{H}_2\text{O} + \text{CO}_2\uparrow \text{ (Gas)}")
    
    st.markdown("""
    Jika gas $CO_2$ yang terbentuk dialirkan ke dalam air barit ($\text{Ba(OH)}_2$), akan terbentuk endapan putih barium karbonat ($\text{BaCO}_3$):
    """)
    
    st.latex(r"\text{CO}_2 + \text{Ba(OH)}_2 \rightarrow \text{BaCO}_3\downarrow \text{ (Endapan Putih)} + \text{H}_2\text{O}")
    
    st.markdown("""
    **3. Esterifikasi Fischer:** Reaksi kondensasi antara asam karboksilat dengan alkohol dibantu katalis asam kuat pekat ($\text{H}_2\text{SO}_4$) menghasilkan senyawa ester yang beraroma wangi khas seperti buah-buahan.
    """)
    
    st.latex(r"\text{R-COOH} + \text{R'-OH} \xrightarrow{\text{H}_2\text{SO}_4\text{, }\Delta} \text{R-COOR'} \text{ (Ester beraroma)} + \text{H}_2\text{O}")
    
    st.markdown("""
    **4. Oksidasi Asam Karboksilat:** Atom C karbonil pada asam karboksilat mengemban bilangan oksidasi +3. Asam karboksilat tertentu yang masih mengikat hidrogen bebas (seperti asam format atau asam oksalat) dapat dioksidasi lebih lanjut oleh oksidator kuat ($KMnO_4$ dalam $H_2SO_4$) menuju bilangan oksidasi maksimal +4 berupa gas $CO_2$.
    """)
    
    st.latex(r"\text{R-COOH} \xrightarrow{\text{KMnO}_4 / \text{H}_2\text{SO}_4} \text{CO}_2\uparrow + \text{H}_2\text{O}")
    
    st.markdown("""
    #### **C. Persamaan Reaksi Identifikasi Derivat Asam Karboksilat (Uji Asam Hidroksamat)**

    Derivat asam karboksilat (contohnya ester) terlebih dahulu dikondensasikan dengan hidroksilamin ($\text{NH}_2\text{OH}$) menghasilkan senyawa asam hidroksamat. Sifat kimia khas dari asam hidroksamat adalah kemampuannya mengkelat logam besi membentuk senyawa kompleks besi(III) hidroksamat yang menghasilkan warna ungu intens saat ditambahkan larutan $\text{FeCl}_3$.

    *Pembentukan Asam Hidroksamat dari Ester:*
    """)
    
    st.latex(r"\text{R-COOR'} \text{ (Ester)} + \text{NH}_2\text{OH} \rightarrow \text{R-CONH-OH (Asam Hidroksamat)} + \text{R'OH}")
    
    st.markdown("""
    *Pembentukan Kompleks Khelat Ungu dengan $\text{FeCl}_3$:*
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
            pembahasan = "✅ <b>Kenapa bereaksi:</b> Aseton memiliki gugus metil keton (CH₃-CO-). Atom hidrogen alfa pada metil ini sangat asam, sehingga tersubstitusi oleh iodin lalu terputus membentuk endapan kuning iodoform (CHI₃)."
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
