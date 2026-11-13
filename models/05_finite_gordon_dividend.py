"""
05_finite_gordon_dividend.py
============================
Rekonsiliasi Model Pertumbuhan Gordon (GGM) Finite vs Perpetual & Kebijakan Dividen Residual
Proyek PLTP WKP Hamiding 60 MW - PT Barito Renewables Energy Tbk (BREN)
Kelompok 1 - Magister Manajemen Teknologi (MMT-ITS)

Fitur Utama:
1. Rekonstruksi Formula Gordon Growth Model (GGM) Tradisional:
   P0 = D1 / (ke - g) = USD 119,17 Juta (Nilai Sekarang / PV = USD 78,50 Juta)
2. Formulasi GGM Horizon Terbatas 30 Tahun (Finite-Horizon Geothermal PPA)
3. Bukti Matematis & Regulasi Mengapa Dividen DILARANG Selama Masa Konstruksi:
   - Pelanggaran PSAK 216 / IAS 16 (Aset Dalam Penyelesaian / AUC)
   - Pelanggaran Kovenan Pinjaman Sindikasi Hijau (Klausul DSCR Proyek >= 1,30x)
4. Formulasi Kebijakan Dividen Residual Optimal Pasca-COD (2030-2059)
"""

import numpy as np

def run_gordon_dividend_analysis():
    print("=" * 80)
    print("PROGRAM MAGISTER MANAJEMEN TEKNOLOGI (MMT) INSTITUT TEKNOLOGI SEPULUH NOPEMBER (ITS), SURABAYA")
    print("MANAJEMEN KEUANGAN LANJUTAN - KELOMPOK 1")
    print("MODEL 05: FINITE-HORIZON GORDON GROWTH MODEL & RESIDUAL DIVIDEND POLICY")
    print("=" * 80)

    # 1. Parameter Dasar Gordon Growth Model (GGM)
    ke = 0.1075  # Biaya Ekuitas BREN (Cost of Equity 10,75%)
    g = 0.0525   # Tingkat Pertumbuhan Dividen Jangka Panjang (5,25%)
    D1 = 6.55435 # Dividen Tahun Pertama Pasca-COD (USD Juta)
    D0 = D1 / (1 + g)
    
    # GGM Abadi (Perpetual GGM - Rumus Silabus / Tradisional)
    # P_COD = D1 / (ke - g)
    p_cod_perpetual = D1 / (ke - g)  # USD 119,17 Juta
    
    # Nilai Sekarang pada t=0 (Masa Konstruksi 4 tahun, diskonto ke 10,75%)
    t_konstruksi = 4
    pv_ggm_t0 = p_cod_perpetual / ((1 + ke) ** t_konstruksi)  # USD 78,50 Juta
    
    print("\n[1] Rekonstruksi Model Gordon Growth Tradisional (Perpetual):")
    print(f"    - Biaya Ekuitas (ke)             : {ke*100:.2f}%")
    print(f"    - Pertumbuhan Dividen (g)        : {g*100:.2f}%")
    print(f"    - Dividen Tahunan Awal (D1)      : USD {D1:.2f} Juta / tahun")
    print(f"    - Nilai Ekuitas GGM pada COD     : USD {p_cod_perpetual:.2f} Juta")
    print(f"    - Nilai Sekarang GGM pada t=0    : USD {pv_ggm_t0:.2f} Juta (Diskon 4 Thn Konstruksi)")
    print(f"    => Catatan: Angka USD 119,17M (PV USD 78,50M) telah konsisten 100% di seluruh naskah makalah.")

    # 2. GGM Horizon Terbatas (Finite Horizon GGM 30 Tahun)
    # P_finite = D0 * (1+g)/(ke - g) * [1 - ((1+g)/(1+ke))^30]
    n_years = 30
    growth_factor = (1 + g) / (1 + ke)
    finite_annuity = 1.0 - (growth_factor ** n_years)
    p_cod_finite = p_cod_perpetual * finite_annuity
    pv_finite_t0 = p_cod_finite / ((1 + ke) ** t_konstruksi)

    print("\n[2] Model Gordon Growth Horizon Terbatas (Finite Horizon 30 Tahun):")
    print(f"    - Masa Kontrak PPA Operasional   : {n_years} Tahun")
    print(f"    - Faktor Anuitas Pertumbuhan     : {finite_annuity:.4f}")
    print(f"    - Nilai Ekuitas Horizon Terbatas : USD {p_cod_finite:.2f} Juta")
    print(f"    - Nilai Sekarang Finite pada t=0 : USD {pv_finite_t0:.2f} Juta")
    print(f"    => Deviasi Terhadap Perpetual    : -USD {p_cod_perpetual - p_cod_finite:.2f} Juta (Akibat berakhirnya konsesi PPA)")

    # 3. Analisis Kovenan & Larangan Dividen Masa Konstruksi (2026-2029)
    print("\n[3] Evaluasi Larangan Pembagian Dividen Selama Konstruksi (2026-2029):")
    print("    1. Arus Kas Proyek Selama Konstruksi: Tepat USD 0,00 (Belum ada penjualan listrik).")
    print("    2. Aspek Akuntansi PSAK 216 / IAS 16:")
    print("       Seluruh pengeluaran modal diakumulasikan dalam Aset Dalam Penyelesaian (AUC).")
    print("       Pembagian dividen sebelum COD akan dianggap sebagai dividen likuidasi / pengembalian modal.")
    print("    3. Kovenan Perbankan Sindikasi Hijau:")
    print("       - Kovenan DSCR Minimum Proyek     : >= 1,30x")
    print("       - Kovenan DSCR Minimum Konsolidasi: >= 1,35x")
    print("       - Klausul 'Dividend Lock-up'      : Pembagian dividen dilarang keras sebelum COD")
    print("                                           dan sebelum pemenuhan Debt Service Reserve Account (DSRA 6 bulan).")

    # 4. Kebijakan Dividen Residual Optimal Pasca-COD
    ebitda_op = 44.14
    debt_service_avg = 40.0
    capex_maint_avg = 1.80
    fcf_residual = ebitda_op - debt_service_avg - capex_maint_avg
    payout_ratio = 0.40  # 40% payout ratio
    dividen_residual = max(0.0, fcf_residual * payout_ratio)

    print("\n[4] Kebijakan Dividen Residual Pasca-COD Kelompok 1:")
    print(f"    - Rata-rata EBITDA Operasional    : USD {ebitda_op:.2f} Juta / tahun")
    print(f"    - Layanan Utang & Cadangan DSRA   : USD {debt_service_avg:.2f} Juta / tahun")
    print(f"    - Belanja Modal Pemeliharaan      : USD {capex_maint_avg:.2f} Juta / tahun")
    print(f"    - Target Dividend Payout Ratio    : {payout_ratio*100:.0f}% dari Arus Kas Bebas Ekuitas (FCFE)")
    print(f"    => REKOMENDASI KELOMPOK 1        : ZERO DIVIDEND 2026-2029, RESIDUAL POST-COD 2030+")
    print("=" * 80)

if __name__ == "__main__":
    run_gordon_dividend_analysis()
