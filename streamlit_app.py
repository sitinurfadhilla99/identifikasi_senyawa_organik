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
            st.write("Ikatan kovalen yang terbentuk menjadi sangat kuat dan stabil.")


# ================= HALAMAN 3: BAB 2 =================
elif pilihan_halaman == "📙 Bab 2: Hidrokarbon":
    st.title("📙 Bab 2: Hidrokarbon (Alkana, Alkena, Alkuna)")
    st.write("---")
    
    t1, t2, t3 = st.tabs(["🔹 Alkana", "🔸 Alkena", "🔺 Alkuna"])
    with t1:
        st.subheader("Alkana (Hidrokarbon Jenuh)")
        st.code("Rumus Umum: C_n H_{2n+2}", language="text")
        st.write("Seluruh ikatannya adalah ikatan kovalen tunggal tunggal. Contoh paling sederhana: Metana ($CH_4$).")
    with t2:
        st.subheader("Alkena (Hidrokarbon Tak Jenuh)")
        st.code("Rumus Umum: C_n H_{2n}", language="text")
        st.write("Memiliki setidaknya satu ikatan rangkap dua ($C=C$). Contoh: Etena ($C_2H_4$).")
    with t3:
        st.subheader("Alkuna (Hidrokarbon Tak Jenuh)")
        st.code("Rumus Umum: C_n H_{2n-2}", language="text")
        st.write("Memiliki setidaknya satu ikatan rangkap tiga ($C≡C$). Contoh: Etuna ($C_2H_2$).")


# ================= HALAMAN 4: BAB 3 =================
elif pilihan_halaman == "📗 Bab 3: Gugus Fungsi":
    st.title("📗 Bab 3: Gugus Fungsi")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.markdown("### 🍷 Alkohol & Eter")
            # Teks di bawah ini sudah disatukan dalam satu baris agar tidak memicu SyntaxError
            st.write("**Alkohol (-OH):** Memiliki gugus hidroksil, mudah larut dalam air (rantai pendek), bereaksi dengan logam natrium.")
            st.write("**Eter (-O-):** Isomer fungsi alkohol, cenderung kurang reaktif, sering digunakan sebagai pelarut non-polar.")
            
    with col2:
        with st.container(border=True):
            st.markdown("### 🧪 Aldehid & Keton")
            st.write("**Aldehid (-CHO):** Memiliki hidrogen pada gugus karbonil, merupakan reduktor kuat (positif Tollens/Fehling).")
            st.write("**Keton (-CO-):** Tidak memiliki hidrogen pada karbonil, hanya bisa dioksidasi oleh oksidator sangat kuat.")


# ================= HALAMAN 5: BAB 4 =================
elif pilihan_halaman == "📕 Bab 4: Turunan & Nitrogen":
    st.title("📕 Bab 4: Asam Karboksilat, Ester, dan Senyawa Nitrogen")
    st.write("---")
    
    with st.container(border=True):
        st.subheader("🍋 Asam Karboksilat (-COOH) & Ester (-COOR)")
        st.write("- **Asam Karboksilat:** Memiliki sifat asam lemah organik, memerahkan lakmus, melepaskan gas $CO_2$ jika ditambah bikarbonat.")
        st.write("- **Ester:** Hasil reaksi esterifikasi antara asam karboksilat dan alkohol. Memiliki aroma khas buah-buahan.")
        
    st.write("")
    with st.container(border=True):
        st.subheader("🧬 Senyawa Organik Nitrogen (Amina & Amida)")
        st.write("- **Amina ($R-NH_2$):** Senyawa turunan amonia bersifat basa lemah, memberikan bau khas (seperti bau ikan busuk).")
        st.write("- **Amida ($R-CONH_2$):** Senyawa turunan asam karboksilat yang berikatan dengan gugus amina, membentuk dasar ikatan peptida pada protein.")


# ================= HALAMAN 6: POST TEST & PREDIKTOR =================
elif pilihan_halaman == "🔬 Post Test & Prediktor":
    import time

    st.title("🔬 Alat Prediktor Uji Laboratorium")
    st.write("Gunakan simulasi di bawah ini untuk memprediksi hasil uji kualitatif senyawa organik pilihanmu.")
    st.write("---")

    with st.container(border=True):
        st.markdown("### ⚙️ Pengaturan Parameter Uji")

        col1, col2 = st.columns(2)

        with col1:
            senyawa = st.selectbox(
                "🎯 Pilih Senyawa Target:",
                [
                "Alkohol Primer",
                "Alkohol Sekunder",
                "Alkohol Tersier",
                "Formaldehida",
                "Aseton",
                "Heksana",
                "Etil Asetat",
                "Asam Asetat"
                ]
            )

        with col2:
            pereaksi = st.selectbox(
                "🧪 Pilih Pereaksi / Indikator:",
                [
                "Oksidator (K2Cr2O7 / H+)",
                "Pereaksi Lucas (ZnCl2 / HCl)",
                "Pereaksi Tollens",
                "Pereaksi Fehling",
                "Uji Iodoform (I2 / NaOH)",
                "Pereaksi Jones (CrO3 / H2SO4)",
                "Pereaksi Schiff",
                "Natrium Bisulfit (NaHSO3)",
                "Hidroksilamin (NH2OH)",
                "NaHCO3 + Uji Barit (Ba(OH)2)",
                "Uji Ceric Nitrat"
                ]
            )

    st.write("")

    tombol=st.button(
        "🔍 Analisis Sekarang",
        use_container_width=True,
        type="primary"
    )

    if not tombol:
        st.info("⬆️ Pilih senyawa dan pereaksi lalu klik tombol Analisis Sekarang")
        st.stop()

    if tombol:

        with st.spinner("Menganalisis sampel laboratorium..."):
            time.sleep(2)

        progress=st.progress(0)

        for i in range(100):
            time.sleep(0.01)
            progress.progress(i+1)

        st.success("✅ Analisis berhasil")

        # Hasil benar-benar baru muncul setelah tombol ditekan

        hasil="(-) Tidak Bereaksi"
        reaksi="Tidak ada persamaan reaksi"
        pembahasan=""

        def alasan_negatif_umum(senyawa):
            if senyawa=="Heksana":
                return "Heksana sangat stabil dan tidak memiliki gugus fungsi reaktif"
            if senyawa=="Etil Asetat":
                return "Etil asetat adalah ester yang relatif stabil"
            return f"{senyawa} tidak memiliki gugus fungsi yang sesuai"


        # Oksidator
        if pereaksi=="Oksidator (K2Cr2O7 / H+)":
            if senyawa in ["Alkohol Primer","Alkohol Sekunder","Formaldehida"]:
                hasil="(+) Warna jingga → hijau"
                reaksi="Cr₂O₇²⁻ → Cr³⁺"
                pembahasan="Senyawa mengalami oksidasi sehingga ion dikromat tereduksi menjadi Cr³⁺ hijau"
            else:
                pembahasan=alasan_negatif_umum(senyawa)


        elif pereaksi=="Pereaksi Tollens":
            if senyawa=="Formaldehida":
                hasil="(+) Cermin perak terbentuk"
                reaksi="RCHO + Ag+ → Ag"
                pembahasan="Aldehid mereduksi ion perak menjadi logam perak"
            else:
                pembahasan="Tidak memiliki sifat pereduksi aldehid"


        elif pereaksi=="Pereaksi Fehling":
            if senyawa=="Formaldehida":
                hasil="(+) Endapan merah bata"
                reaksi="Cu²⁺ → Cu₂O"
                pembahasan="Aldehid mereduksi Cu²⁺"
            else:
                pembahasan="Tidak bereaksi"


        elif pereaksi=="Uji Iodoform (I2 / NaOH)":
            if senyawa=="Aseton":
                hasil="(+) Endapan kuning"
                reaksi="CHI₃ terbentuk"
                pembahasan="Aseton memiliki gugus metil keton"
            else:
                pembahasan="Tidak memiliki gugus metil keton"


        st.markdown("---")
        st.markdown("## 📊 Lembar Hasil Analisis")

        st.info(f"Hasil : {hasil}")

        st.code(reaksi)

        with st.expander("📖 Lihat Pembahasan"):
            st.write(pembahasan) 

    # ================= LOGIKA DATABASE REAKSI & ALASAN =================
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


    # ================= KOTAK OUTPUT BERDERET =================
    st.markdown("### 📊 Lembar Hasil Analisis")
    
    warna_hasil = '#d35400' if '(+)' in hasil else '#7f8c8d'
    
    st.markdown(f"""
    <div class="kotak">
        <div class="label">Hasil Pengamatan (+)/(-)</div>
        <p style="font-size: 1.2em; color: {warna_hasil}; font-weight: bold; margin: 0;">{hasil}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="kotak">
        <div class="label">Persamaan Reaksi Kimia</div>
        <p style="font-size: 1.1em; font-family: 'Courier New', monospace; white-space: pre-wrap; margin: 0; background: #fff; padding: 10px; border-radius: 4px; border: 1px solid #e0e0e0;">{reaksi}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="kotak">
        <div class="label">Pembahasan Teoritis & Analisis Mekanisme</div>
        <p style="margin: 0; line-height: 1.5;">{pembahasan}</p>
    </div>
    """, unsafe_allow_html=True)
