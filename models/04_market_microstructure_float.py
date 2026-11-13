"""
04_market_microstructure_float.py
=================================
Analisis Mikrostruktur Pasar, Batasan Free Float, dan Valuasi Komparatif Peer
PT Barito Renewables Energy Tbk (BREN) - Proyek PLTP Hamiding 60 MW
Kelompok 1 - Magister Manajemen Teknologi (MMT-ITS)

Fitur Utama:
1. Dekomposisi Kepemilikan Saham Pengendali vs Batasan Free Float Publik (3,01%)
2. Analisis Likuiditas Pasar & Sensitivitas Harga (Amihud Illiquidity Metric)
3. Komparasi Kelipatan Valuasi (EV/EBITDA & P/E) vs Peer Geotermal Global (PGEO, ACEN, Ormat)
4. Dampak Penambahan Nilai Proyek Hamiding terhadap Nilai Intrinsik per Lembar Saham BREN
5. Perlindungan Neraca Induk melalui Struktur SPV Non-Recourse Project Finance
"""

import numpy as np

def run_market_microstructure_analysis():
    print("=" * 80)
    print("PROGRAM MAGISTER MANAJEMEN TEKNOLOGI (MMT) INSTITUT TEKNOLOGI SEPULUH NOPEMBER (ITS), SURABAYA")
    print("MANAJEMEN KEUANGAN LANJUTAN - KELOMPOK 1")
    print("MODEL 04: MARKET MICROSTRUCTURE, FREE FLOAT CONSTRAINT & PEER MULTIPLES")
    print("=" * 80)

    # 1. Struktur Modal Saham BREN (Berdasarkan Laporan Keuangan Auditan FY2024 / BEI)
    total_lembar_saham = 133_786_220_000  # 133,78 Miliar Lembar
    harga_saham_saat_ini = 8_250.0        # IDR per lembar (estimasi pasar)
    kurs_usd_idr = 16_205.0               # Rerata JISDOR
    
    kapitalisasi_pasar_idr = total_lembar_saham * harga_saham_saat_ini
    kapitalisasi_pasar_usd = kapitalisasi_pasar_idr / kurs_usd_idr / 1e9 # USD Miliar
    
    # Rincian Pemegang Saham Pengendali & Afiliasi (Audited BREN FY2024)
    pemegang_saham = {
        "PT Barito Pacific Tbk (Pengendali Utama)": 0.64666,
        "Green Era Energy Pte. Ltd.": 0.23603,
        "Prajogo Pangestu & Afiliasi Terkendali": 0.08721,
    }
    total_locked = sum(pemegang_saham.values())  # 96.99%
    free_float_share = 1.0 - total_locked        # 3.01% (Free float publik efektif)
    lembar_free_float = total_lembar_saham * free_float_share
    
    print("\n[1] Struktur Kepemilikan & Keterbatasan Free Float:")
    print(f"    - Total Saham Beredar             : {total_lembar_saham:,.0f} lembar")
    print(f"    - Kapitalisasi Pasar BREN         : Rp {kapitalisasi_pasar_idr/1e12:,.1f} Triliun (~USD {kapitalisasi_pasar_usd:,.2f} Miliar)")
    for entitas, porsi in pemegang_saham.items():
        print(f"      * {entitas:<38} : {porsi*100:6.3f}% ({total_lembar_saham*porsi:,.0f} lembar)")
    print(f"    - Free Float Publik Efektif       : {free_float_share*100:6.2f}% ({lembar_free_float:,.0f} lembar)")
    print(f"    => Catatan Likuiditas: Free float 3,01% sangat rentan terhadap squeeze likuiditas dan gesekan bobot indeks FTSE/MSCI.")

    # 2. Perbandingan Kelipatan Valuasi Terhadap Peer
    peers_data = {
        "BREN (Indonesia)": {"EV_EBITDA": 48.5, "PE": 132.4, "Kapasitas_MW": 886},
        "PGEO (Pertamina Geothermal)": {"EV_EBITDA": 10.8, "PE": 19.2, "Kapasitas_MW": 672},
        "ACEN Corp (Filipina)": {"EV_EBITDA": 14.2, "PE": 24.5, "Kapasitas_MW": 4800},
        "Ormat Technologies (AS/Global)": {"EV_EBITDA": 12.5, "PE": 28.1, "Kapasitas_MW": 1160}
    }
    
    print("\n[2] Benchmarking Valuasi Pasar Relatif (Multiples Analysis):")
    print(f"    {'Perusahaan / Entitas':<32} {'EV/EBITDA':<12} {'P/E Ratio':<12} {'Kapasitas Operasi'}")
    print("    " + "-" * 70)
    for peer, metrics in peers_data.items():
        print(f"    {peer:<32} {metrics['EV_EBITDA']:<12.1f} {metrics['PE']:<12.1f} {metrics['Kapasitas_MW']} MW")
    print("    " + "-" * 70)
    print("    => Temuan Multiples: Premium BREN didorong oleh kelangkaan aset EBT murni dan float terbatas.")

    # 3. Dampak Nilai Tambah Proyek Hamiding
    # Net Strategic NPV = +USD 222,13 Juta (Kelompok 1 Waterfall)
    strategic_npv_usd = 222.13
    strategic_npv_idr = strategic_npv_usd * 1e6 * kurs_usd_idr
    
    # Nilai Intrinsik Tambahan per Lembar Saham (Dilusi = 0 karena pendanaan SPV Non-recourse)
    delta_nilai_per_lembar = strategic_npv_idr / total_lembar_saham
    
    # Base Case DCF (+USD 37,31M) dampak minimum:
    base_npv_usd = 37.31
    delta_base_per_lembar = (base_npv_usd * 1e6 * kurs_usd_idr) / total_lembar_saham

    print("\n[3] Dampak Penciptaan Nilai Proyek Hamiding terhadap Saham BREN:")
    print(f"    - Nilai Sekarang Bersih Dasar (Base DCF)   : +USD {base_npv_usd:.2f} Juta (Rp {base_npv_usd*1e6*kurs_usd_idr/1e12:,.2f} Triliun)")
    print(f"    - Peningkatan Nilai Saham Dasar (Base)     : +Rp {delta_base_per_lembar:.2f} per lembar")
    print(f"    - Total Nilai Strategis (With Real Option) : +USD {strategic_npv_usd:.2f} Juta (Rp {strategic_npv_idr/1e12:,.2f} Triliun)")
    print(f"    - Peningkatan Nilai Saham Strategis        : +Rp {delta_nilai_per_lembar:.2f} per lembar")
    print(f"    - Risiko Dilusi Ekuitas Induk              : 0,00% (Diisolasi pada SPV Hamiding)")
    print("=" * 80)

if __name__ == "__main__":
    run_market_microstructure_analysis()
