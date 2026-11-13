# PT BARITO RENEWABLES ENERGY TBK (IDX: BREN)
## Capital Budgeting Defense, Project Finance Restructuring & Stochastic Real Options Valuation
### Studi Kasus Komprehensif: Proyek Pembangkit Listrik Tenaga Panas Bumi (PLTP) WKP Hamiding 60 MW (Masterplan 130 MW)

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Econometrics Engine](https://img.shields.io/badge/econometrics-Sobol%20QMC%20%7C%20Student--t%20Copula-orange.svg)]()
[![Valuation](https://img.shields.io/badge/valuation-BSM%20%7C%20LSMC%20Laguerre-purple.svg)]()
[![Academic Standard](https://img.shields.io/badge/standard-Academic%20Research-red.svg)]()
[![Defense Ready](https://img.shields.io/badge/status-Audited%20%26%20Public%20Ready-success.svg)]()

---

## 📌 Executive Summary

Repositori ini menyajikan program komputasi finansial kuantitatif, simulasi ekonometrika stokastik, serta kertas kerja teknis untuk evaluasi kelayakan investasi **Proyek PLTP WKP Gunung Hamiding 60 MW** (dengan opsi ekspansi masterplan hingga 130 MW) oleh **PT Barito Renewables Energy Tbk (BREN)**. 

Analisis ini mematahkan pendekatan penganggaran modal statis konvensional (*textbook approach*) yang memvonis proyek tidak layak (*unviable*), dan membuktikan secara empiris bahwa proyek ini membukukan **Dynamic Strategic Net Present Value (Expanded NPV) sebesar +USD 87,89 Juta hingga +USD 222,13 Juta**, dengan **Equity Internal Rate of Return (IRR) sebesar 14,39%**, jauh melampaui biaya modal tertimbang proyek (*hurdle rate* WACC 7,10%).

---

## 🎯 5 Tesis Utama Pertahanan Finansial (Kelompok 1)

```
                     ┌─────────────────────────────────────────────────────────┐
                     │          EVALUASI SILABUS STATIS vs KELOMPOK 1          │
                     └─────────────────────────────────────────────────────────┘
                                                  │
         ┌───────────────────┬────────────────────┼───────────────────┬───────────────────┐
         ▼                   ▼                    ▼                   ▼                   ▼
   [TESIS 1: CAPEX]    [TESIS 2: AKUNTANSI]  [TESIS 3: WACC]     [TESIS 4: PASAR]    [TESIS 5: DIVIDEN]
   Stage-Gated         PSAK 216 / IAS 16     Non-Recourse        Cornered Float      Residual Dividend
   De-risking          AUC Depresiasi $0     Project Finance     3,01% Free Float    Preservasi Solvabilitas
   Opsi Riil 130 MW    Tanah Non-Depr.       WACC 7,10%          Nilai Intrinsik     GGM USD 119,17M
   BSM: +USD 192,8M    Zero Saji Material    Tax Holiday 10 th   +Rp 14,70/saham     Validasi 30 Thn
```

### 1. Optimalisasi Belanja Modal & Teori Opsi Riil (Stage-Gating Protocol)
- **Koreksi:** Belanja modal Tahap 1 sebesar USD 720 Juta (USD 12,0M/MW) mencakup fasilitas infrastruktur bersama (*shared-platform infrastructure*) senilai USD 180 Juta (transmisi HVTL 150 kV 45 km dan lahan 1.500 ha) yang dirancang untuk mengevakuasi daya hingga **≥ 130 MW**.
- **Opsi Riil:** Belanja modal marjinal Tahap 2 (ekspansi 70 MW) hanya sebesar USD 380 Juta (USD 5,43M/MW), menurunkan *blended capex* keseluruhan fasilitas 130 MW menjadi **USD 8,46M/MW** (efisiensi 29,5%).
- **Kuantifikasi:** Formula Black-Scholes-Merton (BSM) dan simulasi numerik Least Squares Monte Carlo (LSMC) ortogonal Laguerre menghasilkan nilai opsi manajerial ekspansi sebesar **USD 192,79 Juta** (PV sebesar **USD 142,10 Juta**).

### 2. Integritas Standar Akuntansi Keuangan (PSAK 216 / IAS 16 & PSAK 223 / IAS 23)
- **Koreksi:** Pembebanan beban penyusutan mekanis USD 28,8 Juta pada tahun 2026 saat aset masih dalam tahap konstruksi adalah pelanggaran fundamental terhadap **PSAK 216 / IAS 16 Paragraf 55**, yang melarang depresiasi sebelum aset siap beroperasi komersial (COD 2030).
- **Preservasi Nilai:** Lahan konsesi senilai USD 110 Juta memiliki masa manfaat tak terbatas sehingga tidak dapat disusutkan (Paragraf 58). Koreksi ini mencegah distorsi laba bersih dan pengikisan ekuitas artifisial sebesar **USD 115,20 Juta**.

### 3. Rekonstruksi WACC Project Finance, Insentif Fiskal, dan Monetisasi Karbon
- **Koreksi:** Penggunaan WACC korporasi holding 10,20% keliru untuk pembiayaan proyek non-recourse. Struktur modal target 70% Utang Sindikasi Hijau multilateral : 30% Ekuitas menurunkan WACC menjadi **7,10%** (Hamada formula dengan $t = 0\%$, re-levered beta 1,164).
- **Proteksi Fiskal & Karbon:** Fasilitas *Tax Holiday* pembebasan PPh Badan 100% selama 10 tahun (Pasal 2 ayat 3 PMK 130/PMK.010/2020 untuk investasi Rp 5–15 Triliun) ditambah diskon 50% 2 tahun transisi, serta monetisasi kredit karbon SPE-GRK di IDXCarbon sebesar USD 3,20 s.d. USD 6,72 Juta/tahun (pada USD 8/ton $\text{CO}_2\text{e}$) mentransformasi nilai proyek:
  - **Dynamic NPV:** Melonjak dari defisit -USD 105,11 Juta menjadi **+USD 80,03 Juta** (Base Mitigated) hingga **+USD 222,13 Juta** (Total Strategic).
  - **Equity IRR:** Mencapai **14,39%** (*Project IRR* 12,85%).
  - **Discounted Payback Period:** Tuntas dalam **8,33 tahun** komersial.

### 4. Analisis Mikrostruktur Pasar Modal & Fenomena *Float Squeeze* (Free Float 3,01%)
- **Koreksi:** Kelipatan valuasi P/E 132,4x dan EV/EBITDA 48,5x saham BREN bukan merupakan cerminan gelembung fundamental murni (*pure speculative bubble*), melainkan dinamika mikrostruktur pasokan akibat konsentrasi kepemilikan 96,99% (Barito Pacific 64,666%, Green Era Energy 23,603%, Prajogo Pangestu & afiliasi 8,721%) dengan *free float* publik efektif hanya **3,01%**.
- **Dampak Intrinsik:** Proyek Hamiding menyuntikkan tambahan nilai intrinsik sebesar **+Rp 4,52 per saham** (Base DCF) hingga **+Rp 26,91 per saham** (Total Strategic), dengan risiko dilusi neraca induk 0,00% via isolasi SPV Non-Recourse.

### 5. Preservasi Solvabilitas Konstruksi & Rekonsiliasi Gordon Growth Model (GGM)
- **Koreksi:** Tuntutan pembagian dividen tunai selama fase konstruksi (saat pendapatan operasional masih USD 0,00) ditolak keras demi menjaga solvabilitas dan kovenan sindikasi perbankan.
- **Kebijakan Dividen Residual:** Dividen baru dibagikan pasca-COD 2030 berbasis FCFE positif. Kovenan perbankan Debt Service Coverage Ratio (DSCR) terjaga aman pada level rerata **1,45x s.d. 1,75x** (di atas batas kovenan proyek $\ge 1,30\times$).
- **Validasi GGM:** Model Gordon abadi ($P_{2030} = D_1 / (K_e - g) = \text{USD } 119,17\text{ Juta}$ atau PV sebesar **USD 78,50 Juta**) dikonfirmasi valid melalui model anuitas konsesi terbatas 30 tahun (**USD 93,32 Juta**).

---

## 📊 Ringkasan Metrik Finansial Komparatif

| Parameter Evaluasi Finansial | Pendekatan Silabus Kasus (Buku Teks Statis) | Rekonstruksi Finansial Terverifikasi (Kelompok 1) | Varian Deviasi | Dasar Regulasi / Rujukan Ilmiah |
| :--- | :---: | :---: | :---: | :--- |
| **Kapasitas Efektif Pembangkit** | 60 MW (Tunggal) | **60 MW s.d. 130 MW** (Masterplan 2 Tahap) | +70 MW (Opsi) | Dokumen WKP Hamiding ESDM |
| **Faktor Kapasitas Riil** | 199,77% *(Anomali Fisika)* | **92,20% s.d. 95,00%** *(Baseload Termal)* | -104,77% | Termodinamika Geotermal |
| **Tarif Listrik PPA PLN** | USD 0,097 / kWh | **USD 0,0970 / kWh** (Kontrak 30 Tahun) | Kontrak 30 Th | Perpres No. 112 Tahun 2022 |
| **Struktur Permodalan Proyek** | 100% Ekuitas Korporasi | **70% Utang Hijau : 30% Ekuitas SPV** | Non-Recourse | Sindikasi Bank Hijau Multilateral |
| **Biaya Modal Tertimbang (WACC)**| 10,20% (Statis Holding) | **7,10%** (Project Finance Diskon Greenium) | -310 bps | Model CAPM & Formula Hamada |
| **Beban Depresiasi Th 2026** | USD 28,80 Juta | **USD 0,00** *(Masa Konstruksi/AUC)* | -USD 28,80M | PSAK 216 / IAS 16 Paragraf 55 |
| **Net Present Value (NPV)** | **-USD 105,11 Juta** (Ditolak) | **+USD 37,31 Juta** (Base DCF Proyek)<br>**+USD 222,13 Juta** (Enhanced Strategic) | **+USD 142,4M s.d.<br>+USD 327,2M** | DCF Terproteksi & Opsi Riil BSM |
| **Internal Rate of Return (IRR)** | 8,29% | **Project IRR: 12,85% \| Equity IRR: 14,39%** | +610 bps | Model Arus Kas Proyek Terpadu |
| **Simple Payback Period** | 10,64 Tahun | **10,64 Tahun** (Simple) \| **8,33 Tahun** (Discounted) | -2,31 Tahun | Standar Penganggaran Modal |
| **Probabilitas Sukses $P(\text{NPV}>0)$**| 4,8% (Unlevered Stand-alone)| **73,8%** (Terproteksi Sindikasi & Fiskal) | +69,0% | Sobol QMC (16.384 Iterasi) |
| **Value at Risk 95% (VaR 95%)** | Ekuitas Terbuka Risiko | **-USD 71,00 Juta** *(Batas Proteksi Kritis)* | Terkendali | Student-t Copula (df = 4) |
| **Nilai Kapitalisasi Dividen GGM**| Klaim Tidak Konsisten | **USD 119,17 Juta** (Saat COD 2030)<br>**USD 78,50 Juta** (Nilai Sekarang t=0) | Konsisten 100% | Finite Gordon Model 30 Tahun |

---

## 🏗️ Struktur Repositori Terbuka

```
BREN-141126/
├── README.md                                  # Dokumentasi utama proyek & ringkasan eksekutif
├── requirements.txt                           # Dependensi pustaka komputasi Python
├── LICENSE                                    # Lisensi terbuka MIT License
├── .gitignore                                 # Filter privasi berkas internal & rahasia
│
├── models/                                    # Program Komputasi Finansial & Ekonometrika Mandiri
│   ├── 01_project_finance_dcf.py              # DCF 30 tahun, sindikasi utang, WACC 7,10%
│   ├── 02_monte_carlo_sobol_copula.py         # Sobol QMC (16.384 run), Copula, MCMC
│   ├── 03_real_options_lsmc_bsm.py            # BSM formula & LSMC Laguerre degree 2
│   ├── 04_market_microstructure_float.py      # Cornered market, free float 3,01%, EVA
│   └── 05_finite_gordon_dividend.py           # Finite GGM 30 tahun vs residual policy
│
├── docs/                                      # Hasil Analisis Mendalam & Kertas Kerja Teknis
│   ├── 01_SOBOL_QMC_COPULA_ECONOMETRICS.md    # Penurunan matematis konvergensi Sobol QMC
│   ├── 02_REAL_OPTIONS_MATHEMATICAL_PROOF.md  # Derivasi algoritma LSMC polinomial Laguerre
│   ├── 03_ACCOUNTING_TREATMENT_PSAK216.md     # Rekonsiliasi akuntansi kapitalisasi IDC/AUC
│   └── 04_MARKET_MICROSTRUCTURE_CORNERED.md   # Kajian empiris likuiditas FTSE Russell BREN
│
└── grafik/                                    # Visualisasi & Diagram Analisis Resolusi Tinggi
    ├── Gambar_1_Perbandingan_Multiples_BREN_vs_Peers.png
    ├── Gambar_2_Asset_Valuation_Depresiasi_Garis_Lurus.png
    ├── Gambar_3_DCF_Cumulative_Cash_Flow_Payback.png
    ├── Gambar_4_Heatmap_Sensitivitas_NPV_WACC_vs_Tarif.png
    ├── Gambar_5_Dampak_Monetisasi_Kredit_Karbon_Terhadap_NPV_IRR.png
    ├── Gambar_6_Gordon_Growth_Model_Sensitivity_Ke_vs_g.png
    ├── Gambar_7_Kebijakan_Dividen_Residual_vs_Capex_Ekspansi.png
    ├── Gambar_8_Tornado_Diagram_Sensitivitas_NPV.png
    ├── Gambar_9_Simulasi_Monte_Carlo_Distribusi_NPV_10000_Iterasi.png
    ├── Gambar_10_Valuasi_Opsi_Riil_Ekspansi_Hamiding_130MW.png
    └── ... (20 Grafik Analisis Kuantitatif Lengkap)
```

---

## ⚡ Panduan Replikasi Cepat (Quickstart)

Seluruh program model finansial dan simulasi dapat dijalankan secara langsung dengan langkah-langkah berikut:

### 1. Kloning Repositori
```bash
git clone https://github.com/nafianjaaay/BREN-141126.git
cd BREN-141126
```

### 2. Instalasi Dependensi Python
```bash
pip install -r requirements.txt
```

### 3. Eksekusi Program Komputasi Finansial & Ekonometrika
```bash
# 1. Menjalankan model DCF Proyek & Dekomposisi Waterfall
python models/01_project_finance_dcf.py

# 2. Menjalankan simulasi Scrambled Sobol Quasi-Monte Carlo (16.384 runs) & Copula
python models/02_monte_carlo_sobol_copula.py

# 3. Menjalankan valuasi Opsi Riil Black-Scholes-Merton (BSM) & LSMC
python models/03_real_options_lsmc_bsm.py

# 4. Menjalankan analisis mikrostruktur pasar & batasan Free Float 3,01%
python models/04_market_microstructure_float.py

# 5. Menjalankan model Finite Gordon Growth Model & kebijakan dividen residual
python models/05_finite_gordon_dividend.py
```

---

## 📜 Kepatuhan Regulasi dan Standar Hukum Republik Indonesia

1. **Undang-Undang Nomor 21 Tahun 2014 tentang Panas Bumi:** Landasan legal pelepasan panas bumi dari rezim pertambangan mineral serta pemberian izin pengusahaan panas bumi terpadu hulu-ke-hilir.
2. **Peraturan Presiden Nomor 112 Tahun 2022 tentang Percepatan Pengembangan EBT:** Penetapan skema kontrak jual beli tenaga listrik jangka panjang 30 tahun berbasis *Take-or-Pay* berdenominasi USD tanpa risiko eskalasi penurunan tarif, didukung penjaminan pemerintah melalui PT Penjaminan Infrastruktur Indonesia (Persero).
3. **Peraturan Menteri Keuangan Nomor 130/PMK.010/2020 tentang Fasilitas Pengurangan PPh Badan:** Pembebasan Pajak Penghasilan Badan sebesar 100% (*Tax Holiday*) selama 10 tahun untuk penanaman modal baru sektor ketenagalistrikan energi terbarukan dengan nilai investasi Rp 5–15 Triliun (Pasal 2 ayat 3), ditambah diskon 50% selama 2 tahun periode transisi pasca-holiday.
4. **Standar Akuntansi Keuangan (PSAK 216 / IAS 16, PSAK 106 / IFRS 6, dan PSAK 223 / IAS 23):** Penegasan pencatatan seluruh pengeluaran eksplorasi dan konstruksi ke dalam pos Aset Konstruksi dalam Pengerjaan (AUC), larangan beban depresiasi sebelum COD, dan kapitalisasi biaya pinjaman masa konstruksi (IDC).
5. **Peraturan OJK Nomor 14 Tahun 2023 tentang Bursa Karbon:** Kerangka hukum perdagangan Sertifikat Pengurangan Emisi Gas Rumah Kaca (SPE-GRK) di bursa karbon nasional (IDXCarbon).

---

## 👥 Tim Peneliti Akademik

**Program Magister Manajemen Teknologi (MMT)**  
**Institut Teknologi Sepuluh Nopember (ITS), Surabaya**

- **Kelompok 1 — Mata Kuliah Manajemen Keuangan (Kelas A)**
- **Studi Kasus:** Penganggaran Modal Strategis PT Barito Renewables Energy Tbk (BREN) — WKP Gunung Hamiding 60 MW / 130 MW
- **Tahun Akademik:** 2026

---

## 📄 Lisensi
Seluruh kode pemodelan, skrip simulasi, dan kertas kerja teknis pada repositori ini dilisensikan di bawah [MIT License](LICENSE). Repositori ini didedikasikan untuk keterbukaan ilmu pengetahuan (*Open Science*) dan reproduksibilitas pemodelan keuangan kuantitatif.
