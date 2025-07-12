import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Layout & Style
st.set_page_config(page_title="Model EOQ | UAS MTK", layout="centered")

st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stApp {font-family: 'Segoe UI', sans-serif;}
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# Judul Aplikasi
st.title("📦 Model Persediaan EOQ (Economic Order Quantity)")
st.markdown("### 🔍 Perhitungan untuk Efisiensi Biaya Pemesanan & Penyimpanan Barang")

# -------------------------------
# Input
with st.sidebar:
    st.header("📘 Parameter Persediaan")
    D = st.number_input("Kebutuhan per tahun (unit)", min_value=1, value=12000)
    S = st.number_input("Biaya pemesanan per pesanan (Rp)", min_value=1, value=100000)
    H = st.number_input("Biaya penyimpanan per unit per tahun (Rp)", min_value=1, value=2500)

# -------------------------------
# Perhitungan EOQ dan Biaya
EOQ = np.sqrt((2 * D * S) / H)
jumlah_pemesanan = D / EOQ
biaya_pesan_EOQ = jumlah_pemesanan * S
biaya_simpan_EOQ = (EOQ / 2) * H
total_biaya_EOQ = biaya_pesan_EOQ + biaya_simpan_EOQ

# -------------------------------
# Output Utama
st.markdown("## ✅ Hasil Perhitungan EOQ")
col1, col2 = st.columns(2)
with col1:
    st.metric("📦 EOQ (unit / order)", f"{EOQ:.2f}")
    st.metric("🔁 Pemesanan / Tahun", f"{jumlah_pemesanan:.2f} kali")
with col2:
    st.metric("💰 Biaya Pemesanan", f"Rp {biaya_pesan_EOQ:,.0f}")
    st.metric("🏢 Biaya Penyimpanan", f"Rp {biaya_simpan_EOQ:,.0f}")

st.success(f"🧾 **Total Biaya Persediaan Tahunan:** Rp {total_biaya_EOQ:,.0f}")

# -------------------------------
# Grafik Visualisasi Biaya
st.markdown("## 📊 Grafik Komponen Biaya vs Jumlah Pemesanan (Q)")
Q_range = np.linspace(100, D, 200)
biaya_pesan = (D / Q_range) * S
biaya_simpan = (Q_range / 2) * H
biaya_total = biaya_pesan + biaya_simpan

fig, ax = plt.subplots()
ax.plot(Q_range, biaya_pesan, label="🔵 Biaya Pemesanan", color='blue')
ax.plot(Q_range, biaya_simpan, label="🟢 Biaya Penyimpanan", color='green')
ax.plot(Q_range, biaya_total, label="🟠 Total Biaya", color='orange')
ax.axvline(EOQ, color='red', linestyle='--', label=f'📍 EOQ ≈ {EOQ:.0f}')
ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("📉 Kurva Biaya vs Q")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# -------------------------------
# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("📘 Dibuat untuk UAS Matematika Industri - by [Your Name Here]")
