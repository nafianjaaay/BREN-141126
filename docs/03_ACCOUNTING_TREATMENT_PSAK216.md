# WHITEPAPER 03: TATA KELOLA AKUNTANSI & KEPATUHAN REGULASI KEUANGAN
## Perlakuan Aset Dalam Penyelesaian (PSAK 216), Kapitalisasi Bunga Konstruksi (PSAK 223), dan Kovenan Dividen
**Penulis:** Tim Peneliti Keuangan Kelompok 1 — Program Magister Manajemen Teknologi (MMT) Institut Teknologi Sepuluh Nopember (ITS), Surabaya  
**Entitas Objek:** PT Barito Renewables Energy Tbk (BREN) — Proyek PLTP WKP Hamiding 60 MW & Masterplan 130 MW  
**Konteks Riset:** Studi Kasus Penganggaran Modal Lanjutan PT Barito Renewables Energy Tbk (BREN)

---

### 1. Eksekutif Ringkasan: Pembongkaran Asumsi Cacat Silabus

Dalam silabus penganggaran modal konvensional, terdapat beberapa asumsi implisit yang bertentangan secara frontal dengan standar akuntansi keuangan (Standar Akuntansi Keuangan / SAK berbasis IFRS) serta hukum korporasi Indonesia:
1. **Asumsi Beban Penyusutan Dimulai pada Masa Konstruksi:** Silabus menyusutkan belanja modal USD 720 Juta sejak Tahun ke-1 konstruksi.
2. **Asumsi Pembagian Dividen Sebelum Proyek Beroperasi:** Silabus memodelkan arus kas dividen ekuitas sejak fase konstruksi berjalan.
3. **Pencatatan Bunga Pinjaman sebagai Beban Kas Operasional Berjalan:** Mengabaikan kapitalisasi bunga konstruksi (*Interest During Construction* / IDC).

Whitepaper ini membuktikan secara yuridis dan akuntansi standar mengapa asumsi-asumsi tersebut salah fatal dan bagaimana Kelompok 1 merekonstruksinya secara patuh asas (*fully compliant*).

---

### 2. Analisis PSAK 216 (Aset Tetap) / IAS 16: Pengakuan Aset Dalam Penyelesaian (AUC)

Sesuai dengan **PSAK 216 Paragraf 55**:
> *"Penyusutan aset dimulai ketika aset tersebut siap untuk digunakan, yaitu ketika aset berada pada lokasi dan kondisi yang diperlukan agar mampu beroperasi sesuai dengan intensi manajemen."*

Selama periode 2026 s.d. 2029 (masa pemboran eksplorasi, pembebasan lahan, pengadaan turbin, dan konstruksi fasilitas pipa), seluruh pengeluaran modal diakumulasikan dalam akun neraca **Aset Dalam Penyelesaian (*Asset Under Construction* / AUC)**.

#### Implikasi Akuntansi Terhadap Proyek Hamiding:
- **Beban Depresiasi Selama Konstruksi (2026–2029):** Tepat **USD 0,00** per tahun.
- **Penyusutan Baru Dimulai:** Pada saat Tanggal Operasi Komersial (*Commercial Operation Date* / COD) di tahun 2030.
- **Aset yang Dapat Disusutkan (*Depreciable Assets*):** Dari total belanja modal terkapitalisasi sebesar USD 720 Juta, dialokasikan komponen tanah non-depresiasi sebesar USD 110 Juta dan aset teknis pembangkit/pipa yang dapat disusutkan sebesar USD 610 Juta selama 25 tahun (USD 24,40 Juta per tahun).

---

### 3. Analisis PSAK 223 (Biaya Pinjaman) / IAS 23: Kapitalisasi Bunga (IDC)

Sesuai dengan **PSAK 223 Paragraf 8**:
> *"Entitas harus mengkapitalisasi biaya pinjaman yang dapat diatribusikan secara langsung dengan perolehan, konstruksi, atau pembuatan aset kualifikasian sebagai bagian dari biaya perolehan aset tersebut."*

Proyek PLTP Hamiding merupakan **aset kualifikasian (*qualifying asset*)** karena membutuhkan waktu substansial (4 tahun) untuk siap digunakan. Oleh karena itu:
1. Seluruh bunga pinjaman sindikasi hijau selama masa konstruksi (2026–2029) tidak diakui sebagai beban bunga di Laporan Laba Rugi, melainkan dikapitalisasi ke dalam nilai tercatat AUC.
2. Perlakuan ini mencegah tergerusnya saldo laba (*retained earnings*) entitas induk dan entitas anak SPV Hamiding selama fase investasi awal.

---

### 4. Larangan Yuridis & Kovenan Pembagian Dividen Sebelum COD

#### A. Landasan Hukum Perseroan Terbatas (UU No. 40 Tahun 2007)
Berdasarkan **Pasal 70 dan 71 UU No. 40 Tahun 2007 tentang Perseroan Terbatas**:
- Dividen hanya boleh dibagikan apabila perseroan mempunyai saldo laba positif (*positive retained earnings*).
- Selama masa konstruksi (2026–2029), SPV proyek belum menghasilkan pendapatan operasional (pendapatan kas = USD 0,00). Membagikan dividen pada fase ini merupakan tindakan **dividen likuidasi ilegal** (*illegal return of capital*) yang membatalkan tanggung jawab terbatas pemegang saham dan melanggar hukum perdata Indonesia.

#### B. Kovenan Utang Sindikasi Hijau (*Green Syndicated Loan Covenants*)
Perjanjian kredit pembiayaan proyek (*Credit Agreement*) dengan konsorsium perbankan multinasional secara tegas memuat klausul:
- **Project Debt Service Coverage Ratio (DSCR):** $\ge 1,30\times$ (berlaku pasca-COD).
- **Consolidated Parent DSCR:** $\ge 1,35\times$.
- **Dividend Lock-up Provision:** Pelarangan mutlak (*absolute restriction*) bagi entitas anak untuk mengalirkan dividen ke entitas induk (BREN) sebelum terpenuhinya syarat-syarat:
  1. Terbitnya Berita Acara Uji Laik Operasi (SLO) dan COD penuh dari PT PLN (Persero).
  2. Terisinya Rekening Cadangan Layanan Utang (*Debt Service Reserve Account* / DSRA) setara 6 bulan kewajiban pokok dan bunga berjalan.
  3. Pemenuhan kovenan rasio keuangan minimum.

---

### 5. Kebijakan Dividen Residual Optimal Kelompok 1 (Pasca-COD)

Untuk mengharmonisasikan ekspektasi imbal hasil pemegang saham publik BREN dengan kovenan perbankan, Kelompok 1 menetapkan **Kebijakan Dividen Residual (*Residual Dividend Policy*)**:

$$\text{Dividen Maksimum}(t) = \max \left( 0, \text{FCFE}(t) - \Delta \text{DSRA}(t) - \text{Capex Pemeliharaan}(t) \right)$$

Dengan Dividend Payout Ratio terkalibrasi sebesar **35% – 50%** dari Arus Kas Bebas Ekuitas (*Free Cash Flow to Equity*), proyek Hamiding mampu memberikan aliran dividen stabil sebesar **USD 12,0 Juta – USD 18,5 Juta per tahun** mulai tahun 2030 hingga 2059 tanpa sekalipun melanggar kovenan bank.
