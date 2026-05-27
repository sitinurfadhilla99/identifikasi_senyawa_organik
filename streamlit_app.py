import streamlit as st
import time

# ================= KONFIGURASI HALAMAN =================

st.set_page_config(
    page_title="ChemReact",
    page_icon="🧪",
    layout="centered"
)

# ================= CSS =================

st.markdown("""
<style>

.stApp{
background: linear-gradient(to bottom,#edf7ff,#f6fff6);
}

.main-title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#0f766e;
margin-bottom:0px;
}

.sub{
text-align:center;
color:#666;
margin-bottom:20px;
font-size:17px;
}

.kotak{
background:white;
padding:20px;
border-radius:20px;
box-shadow:0px 4px 15px rgba(0,0,0,.1);
margin-bottom:20px;
border-left:8px solid #10b981;
}

.footer{
text-align:center;
font-size:13px;
color:gray;
margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================

st.markdown("""
<div class='main-title'>
🧪 ChemReact
</div>

<div class='sub'>
Prediktor Uji Senyawa Organik Interaktif
</div>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================

with st.sidebar:

    st.title("🧪 Menu")

    st.info("""
Website ini membantu:

✔ Prediksi hasil uji

✔ Persamaan reaksi

✔ Analisis reaksi

✔ Alasan spesifik
""")

    st.write("---")

    st.success("Kelompok 3")

# ================= METRIC =================

c1,c2,c3=st.columns(3)

with c1:
    st.metric(
        "Senyawa",
        "8"
    )

with c2:
    st.metric(
        "Pereaksi",
        "11"
    )

with c3:
    st.metric(
        "Jenis",
        "Organik"
    )

st.write("---")

# ================= TEORI =================

with st.expander("📖 Teori Singkat Pereaksi"):

    st.write("""
Tollens → identifikasi aldehid

Fehling → endapan merah bata

Lucas → membedakan alkohol primer, sekunder, tersier

Jones → oksidasi alkohol

Schiff → aldehid menghasilkan warna magenta

Iodoform → mendeteksi metil keton
""")

# ================= INPUT =================

col1,col2=st.columns(2)

with col1:

    senyawa=st.selectbox(
        "Pilih Senyawa",
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

    pereaksi=st.selectbox(
        "Pilih Pereaksi",
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
    "🔍 Prediksi Sekarang"
)

# ================= DEFAULT =================

hasil="(-) Tidak Bereaksi"
reaksi="Tidak ada persamaan reaksi."
pembahasan=""

# ===========================================
# LETAKKAN SELURUH LOGIKA REAKSI PUNYA KAMU
# MULAI:
#
# if pereaksi=="....":
# dst
#
# sampai akhir
#
# JANGAN DIUBAH
# ===========================================


# ================= OUTPUT =================

if prediksi:

    with st.spinner(
        "Menganalisis reaksi..."
    ):

        time.sleep(1)

    progress=st.progress(0)

    for i in range(100):

        time.sleep(.01)

        progress.progress(i+1)

    st.write("")

    tab1,tab2,tab3=st.tabs(
        [
        "🧪 Hasil",
        "⚗ Reaksi",
        "📚 Analisis"
        ]
    )

    with tab1:

        if "(+)" in hasil:

            st.balloons()

            st.success(
                hasil
            )

        else:

            st.error(
                hasil
            )

    with tab2:

        st.code(
            reaksi
        )

    with tab3:

        st.markdown(
            pembahasan,
            unsafe_allow_html=True
        )


# ================= FOOTER =================

st.write("---")

st.markdown("""
<div class='footer'>

ChemReact © 2026

Web Identifikasi Senyawa Organik
berbasis Python + Streamlit

</div>
""", unsafe_allow_html=True)
