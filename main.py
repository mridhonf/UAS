import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# =====================
# Tampilan awal
# =====================
st.set_page_config(page_title="⛽ Model EOQ Produk Gasoline Motor", layout="centered")
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1, h3 {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📦 Model Persediaan EOQ (Economic Order Quantity) Gasoline Motor")
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("### 📘 Masukkan Data Persediaan:")

# =====================
# Input
# =====================
col1, col2 = st.columns(2)
with col1:
    D = st.number_input("⛽ Kebutuhan Gasoline (Liter/Tahun)", min_value=1, value=12000)
    S = st.number_input("📥 Total Biaya per pesanan (Rp)", min_value=1, value=100000)
with col2:
    H = st.number_input("🛢️ Biaya simpan Gasoline (Liter/Tahun) (Rp)", min_value=1, value=2500)

# Keterangan input
st.markdown("#### ℹ️ Keterangan:")
st.markdown("""
- **D** = Kebutuhan tahunan (permintaan barang dalam 1 tahun)
- **S** = Biaya setiap kali melakukan pemesanan
- **H** = Biaya menyimpan 1 unit barang selama 1 tahun
""")

# =====================
# Perhitungan EOQ
# =====================
EOQ = np.sqrt((2 * D * S) / H)
jumlah_pemesanan = D / EOQ
biaya_pesan_EOQ = jumlah_pemesanan * S
biaya_simpan_EOQ = (EOQ / 2) * H
total_biaya_EOQ = biaya_pesan_EOQ + biaya_simpan_EOQ

# =====================
# OUTPUT UTAMA
# =====================
st.markdown("### ✅ Hasil Perhitungan:")
st.success(f"1. 🛢️ EOQ (Jumlah optimal per pemesanan produk Gasoline):: {EOQ:.2f} Liter")
st.info(f"2. Jumlah Pemesanan dalam Setahun: {jumlah_pemesanan:.2f} kali")

st.markdown("#### ℹ️ Apa itu EOQ?")
st.markdown("""
EOQ (Economic Order Quantity) adalah jumlah unit optimal yang harus dipesan setiap kali agar biaya persediaan total (biaya pesan + simpan) minimal. 
Perhitungan menggunakan rumus:

\[
EOQ = (2 * D * S) / H
\]
""", unsafe_allow_html=True)

# =====================
# DETAIL BIAYA
# =====================
st.markdown("### 🔍 Rincian Biaya di Titik EOQ:")
st.write(f"🔵 **Biaya Pemesanan Tahunan:** Rp {biaya_pesan_EOQ:,.0f}")
st.write(f"🟢 **Biaya Penyimpanan Tahunan:** Rp {biaya_simpan_EOQ:,.0f}")
st.write(f"🟠 **Total Biaya Persediaan:** Rp {total_biaya_EOQ:,.0f}")

# =====================
# VISUALISASI GRAFIK
# =====================
st.markdown("### 📈 Kurva Komponen Biaya Persediaan")

Q_range = np.linspace(100, D, 200)
biaya_pesan = (D / Q_range) * S
biaya_simpan = (Q_range / 2) * H
biaya_total = biaya_pesan + biaya_simpan

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(Q_range, biaya_pesan, label="Biaya Pemesanan", color='blue', linestyle='--')
ax.plot(Q_range, biaya_total, label="Total Biaya", color='orange', linewidth=2)
ax.axvline(EOQ, color='red', linestyle=':', label=f'EOQ ≈ {EOQ:.0f}')
ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("📉 Grafik Biaya Pemesanan, Penyimpanan & Total")
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.markdown("<hr><center>📊 Dibuat dengan Streamlit untuk Analisis EOQ Designed By Ridho</center>", unsafe_allow_html=True)
