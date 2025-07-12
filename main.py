import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

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
ax.plot(Q_range, biaya_simpan, label="Biaya Penyimpanan", color='green', linestyle='-.')
ax.plot(Q_range, biaya_total, label="Total Biaya", color='orange', linewidth=2)

# Garis vertikal EOQ
ax.axvline(EOQ, color='red', linestyle=':', label=f'EOQ ≈ {EOQ:.0f}')

# Label dan tampilan
ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("📉 Grafik Biaya Pemesanan, Penyimpanan & Total")
ax.legend()
ax.grid(True)

st.pyplot(fig)

st.markdown("<hr><center>📊 Dibuat dengan Streamlit untuk Analisis EOQ Designed By Ridho</center>", unsafe_allow_html=True)
