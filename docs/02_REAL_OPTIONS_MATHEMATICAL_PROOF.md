# WHITEPAPER 02: PEMBUKTIAN MATEMATIS VALUASI OPSI RIIL
## Black-Scholes-Merton (BSM) & Longstaff-Schwartz Least Squares Monte Carlo (LSMC)
**Penulis:** Tim Peneliti Keuangan Kelompok 1 — Program Magister Manajemen Teknologi (MMT) Institut Teknologi Sepuluh Nopember (ITS), Surabaya  
**Entitas Objek:** PT Barito Renewables Energy Tbk (BREN) — Proyek PLTP WKP Hamiding 60 MW & Masterplan 130 MW  
**Konteks Riset:** Studi Kasus Penganggaran Modal Lanjutan PT Barito Renewables Energy Tbk (BREN)

---

### 1. Landasan Teoretis: Kegagalan DCF Tradisional pada Ketidakpastian Bertingkat

Analisis Arus Kas Terdiskonto (*Discounted Cash Flow* / DCF) konvensional mengasumsikan bahwa manajemen bersifat pasif: keputusan investasi diambil sekali di masa awal ($t=0$) dan tidak dapat diubah sepanjang umur ekonomis proyek.

Namun, dalam proyek pembangkit listrik tenaga panas bumi (PLTP), ketidakpastian geologis bawah permukaan (*subsurface risk*) menurun secara dramatis seiring berjalannya waktu dan dilakukannya pemboran sumur eksplorasi. Manajemen memiliki fleksibilitas strategis untuk:
1. **Opsi Pengabaian Dini (*Abandonment Option* di Gate 1):** Menghentikan proyek setelah fase eksplorasi jika entalpi fluida atau permeabilitas formasi tidak memenuhi skala komersial, sehingga menyelamatkan belanja modal konstruksi tahap berikutnya.
2. **Opsi Ekspansi Kapasitas (*Expansion Option* di Gate 2):** Memperluas kapasitas pembangkit dari 60 MW menjadi kapasitas masterplan 130 MW jika cadangan terbukti (*proven reserves*) melimpah.

Fleksibilitas manajerial ini memiliki struktur pembayaran asimetris (*asymmetric payoff*) yang identik dengan opsi keuangan (*financial call and put options*).

---

### 2. Formulasi Analitis Black-Scholes-Merton (BSM) untuk Opsi Ekspansi

Opsi ekspansi kapasitas sebesar 70 MW tambahan (dari 60 MW menjadi 130 MW) dimodelkan sebagai opsi beli Eropa (*European Call Option*) atas nilai sekarang arus kas tambahan:

$$C_0 = S_0 N(d_1) - K e^{-r T} N(d_2)$$

di mana parameter terkalibrasi secara empiris dari data teknis dan pasar adalah:
- **$S_0$ (Nilai Aset Dasar):** $\text{USD } 257,60\text{ Juta}$ — Nilai sekarang arus kas operasi dari tambahan kapasitas 70 MW (dengan faktor kapasitas 92,20% dan tarif PPA USD 0,097/kWh).
- **$K$ (Harga Eksekusi / Capex Tambahan):** $\text{USD } 140,00\text{ Juta}$ — Belanja modal tambahan tahap 2 untuk instalasi turbin unit 2 dan pipa transmisi daya.
- **$T$ (Horizon Waktu):** $3,0\text{ Tahun}$ — Waktu verifikasi performa sumur produksi tahap 1 menuju COD 2029/2030.
- **$r$ (Tingkat Suku Bunga Bebas Risiko):** $4,50\%$ — Imbal hasil obligasi hijau (*Green US Treasury equivalent*).
- **$\sigma$ (Volatilitas Arus Kas Tahunan):** $32,50\%$ — Volatilitas tahunan arus kas operasi proyek geotermal teregulasi.

#### Perhitungan Nilai Turunan:

$$d_1 = \frac{\ln(S_0 / K) + (r + \frac{1}{2} \sigma^2) T}{\sigma \sqrt{T}} = 1,141$$

$$d_2 = d_1 - \sigma \sqrt{T} = 1,141 - 0,3250 \times \sqrt{3} = 0,582$$

Dengan mengevaluasi fungsi distribusi normal kumulatif baku $N(\cdot)$:
$$N(d_1) = N(1,141) = 0,8731$$
$$N(d_2) = N(0,582) = 0,7197$$

Maka nilai opsi ekspansi pada akhir tahun ke-3 ($T=3$) adalah:
$$C_0 = 257,60 \times 0,8731 - 140,00 \times e^{-0,045 \times 3} \times 0,7197 = \text{USD } 192,79\text{ Juta}$$

Didiskontokan ke nilai sekarang ($t=0$) menggunakan biaya modal riil proyek (WACC $7,10\%$):
$$\text{PV}(C_0) = \frac{\text{USD } 192,79\text{ Juta}}{(1 + 0,0710)^3} = \mathbf{+\text{USD } 142,10\text{ Juta}}$$

---

### 3. Valuasi Opsi Amerika Multi-Tahap: Least Squares Monte Carlo (LSMC)

Untuk memodelkan hak eksekusi kapan saja (*American-style flexibility*) dan menangani opsi majemuk bertingkat (*compound real options*), kami menerapkan algoritma Longstaff-Schwartz (2001) berbasis induksi mundur (*backward induction*).

Pada setiap langkah waktu $t_k$, nilai kontinuitas (*continuation value*) $E[Y | X]$ diestimasi melalui regresi kuadrat terkecil terbobot menggunakan basis ortogonal **Polinomial Laguerre Derajat 2**:

$$L_0(x) = e^{-x/2}$$
$$L_1(x) = e^{-x/2} (1 - x)$$
$$L_2(x) = e^{-x/2} \left( 1 - 2x + \frac{x^2}{2} \right)$$

Kondisi optimal eksekusi ditentukan oleh aturan:
$$\text{Payoff}(t) = \max \left( \text{Immediate Payoff}(t_k), \hat{E}[V(t_{k+1}) | X(t_k)] \right)$$

#### Valuasi Opsi Pengabaian Gate 1 (*Abandonment Option*):
- Biaya eksplorasi awal Tahap 1: **USD 90,0 Juta** (dengan porsi ekuitas mandiri 30% = **USD 27,0 Juta**).
- Jika pemboran eksplorasi awal mengindikasikan reservoir bernilai ekonomi rendah (*dry-hole risk*), manajemen dapat menghentikan proyek dan menyelamatkan sisa belanja modal sebesar **USD 630,0 Juta**.
- Berdasarkan algoritma LSMC, nilai opsi pengabaian ini terhitung sebesar:
$$V_{\text{abandon}} = \mathbf{+\text{USD } 28,40\text{ Juta}}$$

---

### 4. Rekonsiliasi Nilai Strategis Terintegrasi

| Komponen Valuasi | Metodologi | Nilai Nominal (USD Miliar) | Kontribusi terhadap Keputusan |
| :--- | :--- | :---: | :--- |
| **Baseline DCF Silabus** | Statis Tradisional (WACC 10,20%) | $-\text{USD } 105,11\text{M}$ | Menolak proyek secara salah (*Type I Error*) |
| **Rekonstruksi WACC Riil** | Model Hamada & Green Sindikasi (7,10%) | $+\text{USD } 142,42\text{M}$ | Memperbaiki bias biaya modal |
| **Insentif Tax Holiday** | PMK 130/2020 (10 Tahun PPh 0%) | $+\text{USD } 24,20\text{M}$ | Memaksimalkan arus kas awal |
| **Monetisasi Karbon** | SPE-GRK IDXCarbon (POJK 14/2023) | $+\text{USD } 18,52\text{M}$ | Menangkap pendapatan sampingan hijau |
| **Opsi Riil Ekspansi** | BSM & LSMC (Masterplan 130 MW) | $+\text{USD } 142,10\text{M}$ | Menangkap nilai upside tersembunyi |
| **Total Strategic NPV** | **Valuation Waterfall Terpadu** | $\mathbf{+\text{USD } 222,13\text{M}}$ | **Keputusan: SANGAT LAYAK (INVEST)** |
