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
    /* Badge Warna untuk Reaksi Kimia */
    .badge-ungu { background-color: #8e44ad; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-cokelat { background-color: #795548; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-merah { background-color: #e74c3c; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-kuning { background-color: #f1c40f; color: black; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-jingga { background-color: #e67e22; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
    .badge-hijau { background-color: #2ecc71; color: white; padding: 2px 8px; border-radius: 4px; font-weight: bold; }
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
    st.info("""
    ### **RANGKUMAN MATERI PRAKTIKUM KIMIA ORGANIK**
    Silakan gunakan menu navigasi di sebelah kiri untuk membaca kesatuan rangkuman materi praktikum Kimia Organik yang komprehensif, menggabungkan seluruh informasi sifat fisika, sifat kimia, serta persamaan reaksi lengkap dari keempat bab secara sistematis.
    """)

# --- BAB I ---
elif pilihan_halaman == "📘 BAB I. HIDROKARBON":
    st.title("📘 BAB I. HIDROKARBON")
    st.write("---")
    
    st.info("💡 **Definisi:** Hidrokarbon adalah senyawa organik yang seluruh strukturnya hanya tersusun atas unsur karbon (C) dan hidrogen (H). Berdasarkan jenis ikatannya, hidrokarbon alifatik dibagi menjadi hidrokarbon jenuh (alkana) dan tidak jenuh (alkena dan alkuna). Sementara itu, hidrokarbon aromatik memiliki rantai siklik konjugasi yang sangat stabil.")
    
    # Menggunakan Tabs untuk tata letak yang rapi
    tab1, tab2 = st.tabs(["📊 A. Sifat Fisika", "🧪 B. Sifat Kimia & Reaksi Identifikasi"])
    
    with tab1:
        st.markdown("### **Karakteristik Fisika Hidrokarbon**")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Wujud Zat (Suhu Kamar)**\n\n"
                       "* **Suku rendah ($C_1 - C_4$):** Gas (Metana, etana, etena, etuna).\n"
                       "* **Suku sedang ($C_5 - C_{17}$):** Cair (Pentana, heksana, benzena).\n"
                       "* **Suku tinggi ($\ge C_{18}$):** Padat (Parafin padat).")
        with col2:
            st.warning("**Kelarutan & Densitas**\n\n"
                       "* **Kelarutan:** Bersifat nonpolar, sehingga **tidak larut dalam air** (polar). Larut baik dalam pelarut nonpolar seperti $CHCl_3$, $CCl_4$, atau eter.\n"
                       "* **Densitas:** Memiliki massa jenis lebih kecil dari air. Lapisan hidrokarbon selalu berada di **bagian atas**.")
        with col3:
            st.info("**Titik Didih & Leleh**\n\n"
                     "* Meningkat seiring bertambahnya massa molekul.\n"
                     "* Untuk isomer dengan jumlah C sama, **rantai lurus** memiliki titik didih lebih tinggi daripada rantai bercabang karena luas permukaan kontak antarmolekul lebih besar.")

    with tab2:
        st.markdown("### **Uji Identifikasi Laboratorium**")
        
        with st.expander("1. Alkana (Hidrokarbon Jenuh)", expanded=True):
            st.write("Disebut juga parafin (afinitas kecil) karena sangat tidak reaktif terhadap asam kuat, basa kuat, dan oksidator pada suhu kamar.")
            st.markdown("**Uji Iodo (Substitusi Halogen):** Bereaksi dengan halogen ($I_2$) melalui substitusi radikal bebas bantuan sinar UV atau pemanasan. Ditandai dengan memudarnya warna <span class='badge-ungu'>Ungu</span> iodium secara lambat.", unsafe_allow_html=True)
            st.latex(r"\text{CH}_4 + \text{I}_2 \xrightarrow{\text{Sinar UV / }\Delta} \text{CH}_3\text{I} + \text{HI}")
            
        with st.expander("2. Alkena dan Alkuna (Hidrokarbon Tidak Jenuh)", expanded=True):
            st.write("Sangat reaktif karena memiliki ikatan rangkap ($\text{C}=\text{C}$ atau $\text{C}\equiv\text{C}$) yang kaya elektron, mudah mengalami adisi.")
            st.markdown("**Uji Adisi Iodium:** Mengadisi halogen pada ikatan rangkap tanpa bantuan sinar UV. Warna <span class='badge-ungu'>Ungu</span> iodium memudar/hilang seketika.", unsafe_allow_html=True)
            st.latex(r"\text{R-CH}=\text{CH-R} + \text{I}_2 \rightarrow \text{R-CH(I)-CH(I)-R}")
            
            st.markdown("---")
            st.markdown("**Uji Bayer (Oksidasi dengan $KMnO_4$):** Dioksidasi oleh larutan kalium permanganat encer (netral/basa) menghasilkan glikol. Uji positif ditandai hilangnya warna <span class='badge-ungu'>Ungu</span> $KMnO_4$ dan terbentuk endapan <span class='badge-cokelat'>Cokelat</span> $MnO_2$.", unsafe_allow_html=True)
            st.latex(r"3\text{CH}_2=\text{CH}_2 + 2\text{KMnO}_4 + 4\text{H}_2\text{O} \rightarrow 3\text{HO-CH}_2\text{-CH}_2\text{-OH} + 2\text{MnO}_2\downarrow + 2\text{KOH}")
            
        with st.expander("3. Benzena (Hidrokarbon Aromatik)", expanded=True):
            st.write("Memiliki struktur siklik konjugasi yang memenuhi aturan Hückel ($4n+2$), membuat intinya sangat stabil.")
            st.markdown("**Uji Bakar:** Ketika dibakar di cawan porselin, menghasilkan nyala api berminyak disertai **jelaga hitam yang sangat tebal** karena persentase kadar karbon benzena sangat tinggi.", unsafe_allow_html=True)
            st.latex(r"\text{Benzena} + \text{O}_2 \rightarrow \text{C}_{(s)\text{ [Jelaga hitam]}} + \text{CO} + \text{H}_2\text{O}")
            
            st.markdown("---")
            st.markdown("**Reaksi Substitusi Elektrofilik:** Sukar mengalami adisi, cenderung substitusi. Contohnya reaksi Nitrasi menggunakan campuran asam nitrat pekat dan katalis asam sulfat pekat.")
            st.latex(r"\text{C}_6\text{H}_6 + \text{HNO}_3 \xrightarrow{\text{H}_2\text{SO}_4\text{ pekat}} \text{C}_6\text{H}_5\text{NO}_2 + \text{H}_2\text{O}")

# --- BAB II ---
elif pilihan_halaman == "📙 BAB II. ALKOHOL, ETER, DAN FENOL":
    st.title("📙 BAB II. ALKOHOL, ETER, DAN FENOL")
    st.write("---")
    
    tab1, tab2, tab3 = st.tabs(["📊 A. Sifat Fisika & Klasifikasi", "🧪 B. Reaksi Kimia Alkohol & Eter", "🔬 C. Reaksi Kimia Fenol"])
    
    with tab1:
        st.markdown("### **Klasifikasi & Sifat Fisika**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("**Alkohol ($R-OH$)**\n\n"
                    "Turunan alkana dengan gugus hidroksil ($-OH$). Dibagi menjadi $1^\circ$, $2^\circ$, dan $3^\circ$. Suku rendah mudah larut dalam air (ikatan hidrogen). Kelarutan turun jika rantai C memanjang, dan naik jika struktur bercabang banyak.")
        with col2:
            st.warning("**Eter ($R^1-O-R^2$)**\n\n"
                       "Isomer fungsional alkohol. Titik didih jauh lebih rendah karena tidak ada ikatan hidrogen antar-sesama eter. Kelarutan mirip alkohol karena O eter bisa menerima ikatan hidrogen dari air.")
        with col3:
            st.success("**Fenol ($C_6H_5OH$)**\n\n"
                       "Gugus $-OH$ terikat langsung pada cincin benzena. Berbentuk padatan/hablur pada suhu kamar, sedikit larut dalam air, bersifat **asam lemah** karena ion fenoksidanya distabilkan oleh resonansi.")

    with tab2:
        st.markdown("### **Identifikasi Alkohol dan Eter**")
        
        st.markdown("**1. Pereaksi Lucas (Substitusi Gugus $-OH$ oleh Cl):** Membedakan jenis alkohol lewat kecepatan reaksi menggunakan $HCl$ pekat + katalis $ZnCl_2$.")
        st.write("* **Alkohol $3^\circ$:** Bereaksi seketika (larutan langsung keruh/terbentuk 2 lapisan).")
        st.write("* **Alkohol $2^\circ$:** Bereaksi dalam waktu 5-10 menit dengan sedikit pemanasan.")
        st.write("* **Alkohol $1^\circ$:** Tidak bereaksi pada suhu kamar.")
        st.latex(r"\text{R}_3\text{C-OH} + \text{HCl} \xrightarrow{\text{ZnCl}_2} \text{R}_3\text{C-Cl}\downarrow \text{ (Keruh)} + \text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**2. Pereaksi Jones (Oksidasi Alkohol):** Menggunakan $CrO_3$ dalam $H_2SO_4$ pekat. Hasil positif ditandai perubahan warna dari <span class='badge-jingga'>Jingga</span> menjadi <span class='badge-hijau'>Hijau</span>.", unsafe_allow_html=True)
        st.write("* Alkohol $1^\circ$ $\rightarrow$ Aldehida $\rightarrow$ Asam Karboksilat.")
        st.write("* Alkohol $2^\circ$ $\rightarrow$ Keton.")
        st.write("* Alkohol $3^\circ$ $\rightarrow$ Tidak dapat dioksidasi (warna tetap jingga).")
        st.latex(r"\text{R-CH}_2\text{-OH} \xrightarrow{\text{CrO}_3/\text{H}_2\text{SO}_4} \text{R-COOH [Jingga }\rightarrow\text{ Hijau]}")
        
        st.markdown("---")
        st.markdown("**3. Uji Iodoform:** Khusus metil alfa alkohol ($\text{CH}_3\text{-CH(OH)-}$). Direaksikan dengan $I_2$ + $NaOH$ membentuk endapan <span class='badge-kuning'>Kuning</span> kristal iodoform ($CHI_3$) yang berbau khas.", unsafe_allow_html=True)
        st.latex(r"\text{R-CH(OH)-CH}_3 + 4\text{I}_2 + 6\text{NaOH} \rightarrow \text{R-COONa} + \text{CHI}_3\downarrow + 5\text{NaI} + 5\text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**4. Pereaksi Ceric Ammonium Nitrate (CAN):** Alkohol membentuk senyawa kompleks koordinasi berwarna <span class='badge-merah'>Merah Cerah</span>, eter memberikan hasil negatif.", unsafe_allow_html=True)
        st.latex(r"\text{ROH} + [ \text{Ce(NO}_3)_6 ]^{2-} \rightarrow [ \text{Ce(OR)(NO}_3)_5 ]^{2-} \text{ (Kompleks Merah)} + \text{HNO}_3")

    with tab3:
        st.markdown("### **Identifikasi Spesifik Fenol**")
        
        st.markdown("**1. Reaksi dengan Basa Kuat ($NaOH$):** Membentuk garam natrium fenoksida yang larut air (bukti fenol asam lemah).")
        st.latex(r"\text{C}_6\text{H}_5\text{OH} + \text{NaOH} \rightarrow \text{C}_6\text{H}_5\text{ONa} + \text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**2. Uji Besi(III) Klorida ($FeCl_3$):** Membentuk kompleks koordinasi dengan Besi(III) menghasilkan warna <span class='badge-ungu'>Ungu Tua / Kehitaman</span> yang khas.", unsafe_allow_html=True)
        st.latex(r"6\text{C}_6\text{H}_5\text{OH} + \text{FeCl}_3 \rightarrow [\text{Fe}(\text{OC}_6\text{H}_5)_6]^{3-} \text{ (Kompleks Ungu)} + 3\text{H}^+ + 3\text{Cl}^-")
        
        st.markdown("---")
        st.markdown("**3. Reaksi Substitusi Aromatik (Trisubstitusi Air Brom):** Cincin fenol sangat reaktif karena efek aktivasi gugus $-OH$. Direaksikan dengan air brom ($Br_2/H_2O$) langsung membentuk **endapan putih** 2,4,6-tribromofenol.")
        st.latex(r"\text{C}_6\text{H}_5\text{OH} + 3\text{Br}_2 \rightarrow \text{C}_6\text{H}_2\text{Br}_3\text{OH}\downarrow \text{ (Putih)} + 3\text{HBr}")

# --- BAB III ---
elif pilihan_halaman == "📗 BAB III. ALDEHID DAN KETON":
    st.title("📗 BAB III. ALDEHID DAN KETON")
    st.write("---")
    
    st.info("💡 **Kunci Perbedaan:** Aldehida ($\text{R-CHO}$) dan keton ($\text{R-CO-R'}$) adalah isomer fungsional bersisi gugus karbonil ($\text{C}=\text{O}$). Karbonil aldehida mengikat minimal satu atom hidrogen (bersifat reduktor kuat), sedangkan keton terikat pada dua gugus alkil/aril (tidak memiliki daya pereduksi).")
    
    tab1, tab2, tab3 = st.tabs(["📊 A. Sifat Fisika", "🧪 B. Reaksi Adisi Karbonil", "🔬 C. Reaksi Diferensiasi (Daya Reduksi)"])
    
    with tab1:
        st.markdown("### **Sifat Fisika Aldehida & Keton**")
        st.markdown("* **Metanal (Formaldehida):** Suku paling rendah, berwujud gas pada suhu kamar, bau menyengat.\n"
                    "* **Aldehida Suku Rendah Lain:** Cairan, aromanya semakin harum (aroma buah) seiring bertambah panjangnya rantai C.\n"
                    "* **Keton Suku Rendah (Aseton/Propanon):** Cairan encer, mudah larut air, mudah menguap, memiliki aroma yang segar.")

    with tab2:
        st.markdown("### **Reaksi Adisi pada Gugus Karbonil**")
        
        st.markdown("**1. Adisi Natrium Bisulfit ($NaHSO_3$):** Reaksi adisi nukleofilik pada aldehida atau metil keton menghasilkan senyawa aduk berupa **kristal padat berwarna putih** yang sukar larut.")
        st.latex(r"\text{R-CHO} + \text{NaHSO}_3 \rightarrow \text{R-CH(OH)-SO}_3\text{Na (Kristal Putih)}")
        
        st.markdown("---")
        st.markdown("**2. Pembentukan Hemiasetal dan Asetal:** Reaksi reversibel gugus karbonil dengan alkohol dalam suasana asam gas $HCl$.")
        st.latex(r"\text{R-CHO} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OH)(OR') (Hemiasetal)}")
        st.latex(r"\text{R-CH(OH)(OR')} + \text{R'OH} \xrightarrow{\text{HCl}} \text{R-CH(OR')}_2 + \text{H}_2\text{O}")

    with tab3:
        st.markdown("### **Uji Pembeda Aldehida (Positif) dan Keton (Negatif)**")
        
        st.markdown("**1. Uji Tollens (Cermin Perak):** Mereduksi ion kompleks perak beramoniak $[\text{Ag(NH}_3)_2]^+$ menjadi logam perak murni yang menempel di dinding tabung reaksi membentuk **cermin perak**.")
        st.latex(r"\text{R-CHO} + 2[\text{Ag(NH}_3)_2]^+ + 3\text{OH}^- \rightarrow \text{R-COO}^- + 2\text{Ag}\downarrow \text{ (Cermin Perak)} + 4\text{NH}_3 + 2\text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**2. Uji Fehling:** Mereduksi ion $\text{Cu}^{2+}$ (kompleks tartrat basa) menghasilkan endapan <span class='badge-merah'>Merah Bata</span> kupro oksida ($\text{Cu}_2\text{O}$).", unsafe_allow_html=True)
        st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow + 3\text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**3. Uji Benedict:** Serupa dengan Fehling, namun ion $\text{Cu}^{2+}$ dikomplekskan oleh sitrat dalam kondisi alkalis lemah. Menghasilkan endapan <span class='badge-merah'>Merah Bata</span> $\text{Cu}_2\text{O}$ saat direaksikan dengan aldehida.", unsafe_allow_html=True)
        st.latex(r"\text{R-CHO} + 2\text{Cu}^{2+}\text{(sitrat)} + 5\text{OH}^- \rightarrow \text{R-COO}^- + \text{Cu}_2\text{O}\downarrow + 3\text{H}_2\text{O}")

# --- BAB IV ---
elif pilihan_halaman == "📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA":
    st.title("📕 BAB IV. ASAM KARBOKSILAT DAN DERIVATNYA")
    st.write("---")
    
    st.info("💡 **Definisi:** Asam karboksilat memiliki gugus fungsi karboksil ($-COOH$), gabungan gugus karbonil dan hidroksil. Derivatnya (ester, halida asam, anhidrida asam, amida) terbentuk ketika gugus $-OH$ digantikan oleh nukleofil lain.")
    
    tab1, tab2, tab3 = st.tabs(["📊 A. Sifat Fisika", "🧪 B. Reaksi Kimia Asam Karboksilat", "🔬 C. Identifikasi Derivat (Uji Asam Hidroksamat)"])
    
    with tab1:
        st.markdown("### **Karakteristik Fisika**")
        st.markdown("* **Kelarutan:** Rantai pendek ($C_1 - C_4$) larut sangat baik dalam air karena gugus $-COOH$ membentuk ikatan hidrogen kuat (**dimer**). Kelarutan turun jika rantai alkil nonpolar semakin panjang.\n"
                    "* **Titik Didih:** Relatif tinggi dibandingkan senyawa organik lain dengan berat molekul setara akibat asosiasi ikatan hidrogen yang kuat.")

    with tab2:
        st.markdown("### **Reaksi Kimia Asam Karboksilat**")
        
        st.markdown("**1. Reaksi dengan Basa Kuat ($NaOH$):** Menghasilkan garam karboksilat yang larut air.")
        st.latex(r"\text{R-COOH} + \text{NaOH} \rightarrow \text{R-COONa} + \text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**2. Reaksi dengan Basa Lemah ($NaHCO_3$):** Mengalami deprotonasi menghasilkan pelepasan **gas karbon dioksida secara cepat (*effervescence*)**. Uji ini membedakan asam karboksilat dengan fenol (fenol tidak bereaksi).")
        st.latex(r"\text{R-COOH} + \text{NaHCO}_3 \rightarrow \text{R-COONa} + \text{H}_2\text{O} + \text{CO}_2\uparrow")
        st.write("Jika gas $CO_2$ dialirkan ke air barit ($\text{Ba(OH)}_2$), terbentuk **endapan putih** barium karbonat ($\text{BaCO}_3$):")
        st.latex(r"\text{CO}_2 + \text{Ba(OH)}_2 \rightarrow \text{BaCO}_3\downarrow + \text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**3. Esterifikasi Fischer:** Kondensasi antara asam karboksilat dengan alkohol dibantu katalis asam kuat pekat ($\text{H}_2\text{SO}_4$) menghasilkan senyawa ester yang **beraroma wangi khas buah-buahan**.")
        st.latex(r"\text{R-COOH} + \text{R'-OH} \xrightarrow{\text{H}_2\text{SO}_4\text{, }\Delta} \text{R-COOR'} + \text{H}_2\text{O}")
        
        st.markdown("---")
        st.markdown("**4. Oksidasi Asam Karboksilat:** Asam karboksilat tertentu yang masih mengikat hidrogen bebas (asam format/oksalat) dapat dioksidasi oleh $KMnO_4$ dalam $H_2SO_4$ menuju biloks maksimal +4 berupa gas $CO_2$.")
        st.latex(r"\text{R-COOH} \xrightarrow{\text{KMnO}_4 / \text{H}_2\text{SO}_4} \text{CO}_2\uparrow + \text{H}_2\text{O}")

    with tab3:
        st.markdown("### **Uji Identifikasi Derivat Asam Karboksilat (Uji Asam Hidroksamat)**")
        st.write("Derivat (contohnya ester) dikondensasikan dengan hidroksilamin ($\text{NH}_2\text{OH}$) menghasilkan asam hidroksamat. Sifat khasnya adalah mengkelat logam besi membentuk kompleks besi(III) hidroksamat yang menghasilkan warna <span class='badge-ungu'>Ungu Intens</span> saat ditambahkan $\text{FeCl}_3$.", unsafe_allow_html=True)
        
        st.markdown("**Tahap 1: Pembentukan Asam Hidroksamat dari Ester**")
        st.latex(r"\text{R-COOR'} + \text{NH}_2\text{OH} \rightarrow \text{R-CONH-OH} + \text{R'OH}")
        
        st.markdown("**Tahap 2: Pembentukan Kompleks Khelat Ungu dengan $\text{FeCl}_3$**")
        st.latex(r"3\text{R-CONH-OH} + \text{FeCl}_3 \rightarrow \text{Fe(R-CONHO)}_3 + 3\text{HCl}")

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
