import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Model Industri Motor", layout="wide")


st.title("Model Persediaan EOQ (Economic Order Quantity) dalam produk Gasoline Motor")

st.markdown("### 📘 Masukkan Parameter:")

# Input dari pengguna
D = st.number_input("Kebutuhan Gasoline (Liter/Tahun)", min_value=1, value=12000)
S = st.number_input("Total Biaya per pesanan (Rp)", min_value=1, value=100000)
H = st.number_input("Biaya simpan Gasoline (Liter/Tahun) (Rp)", min_value=1, value=2500)

# Perhitungan EOQ
EOQ = np.sqrt((2 * D * S) / H)
jumlah_pemesanan = D / EOQ
total_biaya = (jumlah_pemesanan * S) + ((EOQ / 2) * H)

st.markdown("### ✅ Hasil Perhitungan:")

st.write(f"1. **EOQ (Jumlah optimal per pemesanan produk Gasoline):** `{EOQ:.2f} Liter`")
st.write(f"2. **Jumlah Pemesanan per Tahun:** `{jumlah_pemesanan:.2f} kali`")
st.write(f"3. **Total Biaya Persediaan Tahunan:** `Rp {total_biaya:,.0f}`")

# Visualisasi Kurva Biaya Persediaan
Q_range = np.linspace(100, D, 100)
total_costs = (D / Q_range) * S + (Q_range / 2) * H

fig, ax = plt.subplots()
ax.plot(Q_range, total_costs, label="Total Biaya")
ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ ≈ {EOQ:.0f}')
ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Total Biaya (Rp)")
ax.set_title("Kurva Total Biaya Persediaan")
ax.legend()
st.pyplot(fig)
