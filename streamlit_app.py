import streamlit as st
import time

# ===================== KONFIG ======================

st.set_page_config(
    page_title="ChemReact",
    page_icon="🧪",
    layout="wide"
)

# ===================== CSS ======================

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#edf8ff,#f7fff7);
}

.hero{
padding:35px;
border-radius:25px;
background: linear-gradient(90deg,#0f766e,#10b981);
color:white;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
margin-bottom:25px;
}

.hero-title{
font-size:42px;
font-weight:800;
}

.hero-sub{
font-size:18px;
opacity:0.9;
}

.card{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0 4px 20px rgba(0,0,0,0.08);
margin-bottom:20px;
}

.footer{
text-align:center;
font-size:12px;
color:gray;
padding-top:30px;
}

.badge-pos{
background:#dcfce7;
padding:8px;
border-radius:12px;
color:#166534;
font-weight:bold;
}

.badge-neg{
background:#fee2e2;
padding:8px;
border-radius:12px;
color:#991b1b;
font-weight:bold;
}

</style>
""",unsafe_allow_html=True)

# ===================== HERO ======================

st.markdown("""

<div class='hero'>

<div class='hero-title'>
🧪 ChemReact
</div>

<div class='hero-sub'>
Prediktor Uji Senyawa Organik Interaktif Berbasis Python & Streamlit
<br>
Memprediksi hasil reaksi, persamaan kimia, dan analisis senyawa.
</div>

</div>

""",unsafe_allow_html=True)

# ================= SIDEBAR =================

with st.sidebar:

    st.title("📚 Dashboard")

    menu = st.radio(
        "Pilih Halaman",
        [

        "🏠 Home",

        "🧪 BAB 1 HIDROKARBON",

        "🍃 BAB 2 ALKOHOL, ETER DAN FENOL",

        "⚗ BAB 3 ALDEHID DAN KETON",

        "🧫 BAB 4 ASAM KARBOKSILAT",

        "📝 POST TEST"

        ]
    )


# ================= HOME =================

if menu=="🏠 Home":

    st.markdown("""
    <div style='
    background:linear-gradient(90deg,#0f766e,#10b981);
    padding:35px;
    border-radius:25px;
    color:white;
    text-align:center;
    margin-bottom:30px;
    '>

    <h1>🧪 Media Pembelajaran Identifikasi Senyawa Organik</h1>

    <p style='font-size:18px;'>

    Website ini dirancang sebagai sarana pembelajaran
    untuk memahami teori dan proses identifikasi
    berbagai senyawa organik berdasarkan sifat
    dan reaksinya.

    </p>

    </div>
    """, unsafe_allow_html=True)


    c1,c2=st.columns(2)

    with c1:

        if st.button(
        "📚 Jelajahi Materi",
        use_container_width=True
        ):

            st.success(
            "Silakan pilih BAB pada Dashboard"
            )

    with c2:

        if st.button(
        "📝 Uji Pemahaman",
        use_container_width=True
        ):

            st.info(
            "Buka menu POST TEST di Dashboard"
            )
            


    st.write("")

    m1,m2,m3=st.columns(3)

    with m1:
        st.metric(
        "BAB Materi",
        "4"
        )

    with m2:
        st.metric(
        "Post Test",
        "1"
        )

    with m3:
        st.metric(
        "Mode",
        "Interaktif"
        )

# ================= BAB 1 =================

elif menu=="🧪 BAB 1 HIDROKARBON":

    st.header(
    "BAB 1 HIDROKARBON"
    )

    st.subheader(
    "Pengertian"
    )

    st.write("""

Hidrokarbon merupakan senyawa
organik yang hanya tersusun
oleh atom karbon (C)
dan hidrogen (H).

""")

    st.subheader(
    "Jenis Hidrokarbon"
    )

    st.write("""

• Alkana

• Alkena

• Alkuna

• Aromatik

""")

    st.info("""
Alkana memiliki ikatan tunggal,
alkena ikatan rangkap dua,
dan alkuna ikatan rangkap tiga.
""")


# ================= BAB 2 =================

elif menu=="🍃 BAB 2 ALKOHOL, ETER DAN FENOL":

    st.header(
    "BAB 2 ALKOHOL"
    )

    st.subheader(
    "Pengertian"
    )

    st.write("""

Alkohol adalah senyawa organik
yang memiliki gugus fungsi:

R-OH

""")

    st.subheader(
    "Klasifikasi"
    )

    st.write("""

• Alkohol primer

• Alkohol sekunder

• Alkohol tersier

""")

    st.success("""
Alkohol primer dan sekunder
dapat dioksidasi.
""")


# ================= BAB 3 =================

elif menu=="⚗ BAB 3 ALDEHID DAN KETON":

    st.header(
    "BAB 3 ALDEHID DAN KETON"
    )

    st.subheader(
    "Aldehid"
    )

    st.write("""

Memiliki gugus:

R-CHO

Mudah teroksidasi

Positif Tollens

Positif Fehling

""")

    st.subheader(
    "Keton"
    )

    st.write("""

Memiliki gugus:

R-CO-R

Tidak bereaksi
dengan Tollens

""")

    st.warning("""
Aldehid lebih mudah
dioksidasi dibanding keton.
""")


# ================= BAB 4 =================

elif menu=="🧫 BAB 4 ASAM KARBOKSILAT":

    st.header(
    "BAB 4 ASAM KARBOKSILAT"
    )

    st.write("""

Asam karboksilat memiliki
gugus:

R-COOH

""")

    st.subheader(
    "Sifat"
    )

    st.write("""

• Bersifat asam

• Bereaksi dengan NaHCO₃

• Membentuk ester

""")

    st.info("""
Contoh:
Asam asetat
(CH3COOH)
""")

# ================= POST TEST =================

elif menu=="📝 POST TEST":

    st.header("🧪 ChemReact")

    st.write("""
    Prediksi hasil reaksi
    berdasarkan pereaksi
    dan senyawa
    """)

    # ===== METRIC =====

    m1,m2,m3,m4=st.columns(4)

    with m1:
        st.metric("Senyawa","8")

    with m2:
        st.metric("Pereaksi","11")

    with m3:
        st.metric("Jenis Uji","Organik")

    with m4:
        st.metric("Mode","Virtual Lab")

    st.write("")

    # ===== INPUT =====

    left,right=st.columns([1,1])

    with left:

        st.markdown("### 🧫 Pilih Sampel")

        senyawa=st.selectbox(
            "",
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

    with right:

        st.markdown("### ⚗ Pilih Pereaksi")

        pereaksi=st.selectbox(
            "",
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

    prediksi=st.button(
    "🔬 Jalankan Analisis",
    use_container_width=True
    )

    hasil="(-) Tidak Bereaksi"
    reaksi="Tidak ada persamaan reaksi"
    pembahasan=""

    # ==========================================
    # TEMPEL BLOK LOGIKA REAKSI PUNYA KAMU
    # mulai dari:
    #
    # if pereaksi=="..."
    #
    # sampai selesai
    # ==========================================


    if prediksi:

        with st.spinner("Menganalisis..."):

            bar=st.progress(0)

            for i in range(100):

                time.sleep(.01)

                bar.progress(i+1)

        st.success("Analisis selesai")

        tab1,tab2,tab3,tab4=st.tabs([

        "🧪 Hasil",

        "⚗ Reaksi",

        "📚 Analisis",

        "📖 Teori"

        ])

        with tab1:

            if "(+)" in hasil:

                st.balloons()

                st.markdown(
                f"""
                <div class='badge-pos'>
                {hasil}
                </div>
                """,
                unsafe_allow_html=True
                )

            else:

                st.markdown(
                f"""
                <div class='badge-neg'>
                {hasil}
                </div>
                """,
                unsafe_allow_html=True
                )

            st.info(f"Sampel : {senyawa}")

            st.info(f"Pereaksi : {pereaksi}")


        with tab2:

            st.markdown(
            "### Persamaan Reaksi"
            )

            st.code(
            reaksi
            )


        with tab3:

            st.markdown(
            pembahasan,
            unsafe_allow_html=True
            )


        with tab4:

            st.markdown("""

### Ringkasan Pereaksi

🧪 Tollens  
Mendeteksi aldehid

⚗ Fehling  
Endapan merah bata

🧫 Lucas  
Membedakan alkohol

🔬 Jones  
Oksidasi alkohol

🌈 Schiff  
Warna magenta aldehid

""")

# ===================== INPUT ======================

left,right=st.columns([1,1])

with left:

    st.markdown("### 🧫 Pilih Sampel")

    senyawa=st.selectbox(
        "",
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

with right:

    st.markdown("### ⚗ Pilih Pereaksi")

    pereaksi=st.selectbox(
        "",
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

prediksi=st.button(
"🔬 Jalankan Analisis",
use_container_width=True
)

hasil="(-) Tidak Bereaksi"
reaksi="Tidak ada persamaan reaksi"
pembahasan=""

# ==========================================
# TEMPEL SELURUH BLOK LOGIKA PUNYA KAMU
#
# mulai:
#
# if pereaksi=="..."
#
# sampai akhir
#
# ==========================================


# ===================== OUTPUT ======================

if prediksi:

    with st.spinner(
    "Menganalisis..."
    ):

        bar=st.progress(0)

        for i in range(100):

            time.sleep(.01)

            bar.progress(i+1)

    st.success("Analisis selesai")

    tab1,tab2,tab3,tab4=st.tabs([

    "🧪 Hasil",

    "⚗ Reaksi",

    "📚 Analisis",

    "📖 Teori"

    ])

    with tab1:

        if "(+)" in hasil:

            st.balloons()

            st.markdown(
            f"""
            <div class='badge-pos'>
            {hasil}
            </div>
            """,
            unsafe_allow_html=True
            )

        else:

            st.markdown(
            f"""
            <div class='badge-neg'>
            {hasil}
            </div>
            """,
            unsafe_allow_html=True
            )

        st.write("")
        st.info(
        f"Sampel : {senyawa}"
        )

        st.info(
        f"Pereaksi : {pereaksi}"
        )

    with tab2:

        st.markdown("### Persamaan Reaksi")

        st.code(
        reaksi
        )

    with tab3:

        st.markdown(
        pembahasan,
        unsafe_allow_html=True
        )

    with tab4:

        st.markdown("""

### Ringkasan Pereaksi

🧪 Tollens  
Mendeteksi aldehid

⚗ Fehling  
Endapan merah bata

🧫 Lucas  
Membedakan alkohol

🔬 Jones  
Oksidasi alkohol

🌈 Schiff  
Warna magenta aldehid

""")

st.write("---")

st.markdown("""

<div class='footer'>

ChemReact © 2026

Web Identifikasi Senyawa Organik Interaktif

Dibuat menggunakan Python + Streamlit

</div>

""",unsafe_allow_html=True)
