"""
Unit & Integration Test Suite for Quantitative Models
======================================================
Tests all 5 quantitative engines in TUGAS4/models/ for mathematical consistency,
parameterization, absence of runtime errors, and adherence to established benchmarks.
"""

import sys
import os
import importlib
import pytest
import numpy as np
import pandas as pd

# Add models directory to sys.path
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models"))
if MODELS_DIR not in sys.path:
    sys.path.insert(0, MODELS_DIR)

# Dynamic imports
dcf_mod = importlib.import_module("01_project_finance_dcf")
mc_mod = importlib.import_module("02_monte_carlo_sobol_copula")
ro_mod = importlib.import_module("03_real_options_lsmc_bsm")
micro_mod = importlib.import_module("04_market_microstructure_float")
div_mod = importlib.import_module("05_finite_gordon_dividend")


# ==============================================================================
# Model 01: Project Finance & Discounted Cash Flow (DCF) Engine
# ==============================================================================
def test_01_project_finance_dcf():
    """Verify Model 01 WACC, baseline syllabus DCF, waterfall valuation, and schedule."""
    assert hasattr(dcf_mod, "ProjectFinanceModel")
    assert hasattr(dcf_mod, "ProjectFinanceDCF")
    assert dcf_mod.ProjectFinanceModel is dcf_mod.ProjectFinanceDCF
    
    model = dcf_mod.ProjectFinanceModel()
    
    # 1. WACC & Hamada Relevering
    wacc_res = model.calculate_wacc()
    assert abs(wacc_res["wacc"] - 0.0710) < 0.001
    assert abs(wacc_res["cost_of_equity"] - 0.1100) < 0.001
    assert abs(wacc_res["cost_of_debt"] - 0.0450) < 0.0001
    
    # 2. Baseline Syllabus Benchmark
    base = model.calculate_baseline_syllabus()
    assert abs(base["npv"] - (-105.11)) < 0.05
    assert abs(base["irr"] - 0.0829) < 0.001
    assert abs(base["payback"] - 10.64) < 0.01
    assert abs(base["capex"] - 720.0) < 0.01
    
    # 3. Waterfall Valuation
    wf = model.calculate_waterfall_valuation()
    assert abs(wf["base_syllabus_npv"] - (-105.11)) < 0.01
    assert abs(wf["wacc_adjustment_benefit"] - 142.42) < 0.01
    assert abs(wf["dcf_base_710"] - 37.31) < 0.01
    assert abs(wf["tax_holiday_benefit"] - 24.20) < 0.01
    assert abs(wf["carbon_monetization_benefit"] - 18.52) < 0.01
    assert abs(wf["dcf_mitigated"] - 80.03) < 0.01
    assert abs(wf["expansion_real_option_pv"] - 142.10) < 0.01
    assert abs(wf["total_strategic_npv"] - 222.13) < 0.01
    
    # 4. Cash Flow Schedule & Valuation
    df = model.build_cash_flow_schedule()
    assert len(df) == 30
    assert "FCFF" in df.columns
    assert "FCFE" in df.columns
    assert "DSCR" in df.columns
    assert df["DSCR"].dropna().min() >= 1.30  # Covenant compliance
    
    val = model.calculate_valuation(df)
    assert abs(val["equity_irr"] - 0.1439) < 0.005
    assert abs(val["project_npv"] - 80.03) < 0.01


def test_01_project_finance_generalization():
    """Verify Model 01 generalization with custom parameters for alternative projects."""
    custom_params = dcf_mod.ProjectParameters(
        capacity_mw=100.0,
        debt_ratio=0.50,
        cost_of_debt=0.050,
        risk_free_rate=0.040,
        market_risk_premium=0.060,
        unlevered_beta=0.50,
        operational_years=25
    )
    custom_model = dcf_mod.ProjectFinanceModel(params=custom_params)
    wacc_res = custom_model.calculate_wacc()
    
    # Levered beta = 0.50 * (1 + 0.5/0.5) = 1.00
    # Cost of equity = 0.04 + 1.00 * 0.06 = 0.10
    # WACC = 0.50 * 0.10 + 0.50 * 0.05 = 0.0750
    assert abs(wacc_res["wacc"] - 0.0750) < 0.001
    
    schedule = custom_model.build_cash_flow_schedule()
    assert len(schedule) == 25
    assert schedule["FCFF"].sum() > 0


# ==============================================================================
# Model 02: Sobol Quasi-Monte Carlo & Student-t Copula Simulation
# ==============================================================================
def test_02_monte_carlo_sobol_copula_fast():
    """Verify Model 02 Copula simulation, tail risks, and marginal transformations."""
    assert hasattr(mc_mod, "SobolCopulaSimulator")
    assert hasattr(mc_mod, "SobolCopulaMonteCarlo")
    
    # Fast test with 2048 paths
    cfg = mc_mod.MonteCarloConfig(n_simulations=2048, random_seed=42)
    simulator = mc_mod.SobolCopulaSimulator(config=cfg)
    
    u_copula = simulator.generate_copula_draws()
    assert u_copula.shape == (2048, 4)
    assert np.all(u_copula >= 0.0) and np.all(u_copula <= 1.0)
    
    marginals = simulator.transform_marginals(u_copula)
    assert "enthalpy" in marginals
    assert "kurs_jisdor" in marginals
    assert "om_escalation" in marginals
    assert "cf_real" in marginals
    
    npv_base, npv_mit = simulator.evaluate_paths(marginals)
    assert len(npv_base) == 2048
    assert len(npv_mit) == 2048
    
    res = simulator.run_simulation()
    assert abs(res.p_success_baseline - 4.8) < 1.0
    assert abs(res.p_success_mitigated - 73.8) < 1.0
    assert abs(res.var_95_equity - (-71.0)) < 2.0


def test_02_monte_carlo_full_benchmark():
    """Verify Model 02 full 16,384 paths benchmark exact consistency."""
    cfg = mc_mod.MonteCarloConfig(n_simulations=16384, random_seed=42)
    simulator = mc_mod.SobolCopulaSimulator(config=cfg)
    res = simulator.run_simulation()
    
    assert res.n_simulations == 16384
    assert res.p_success_baseline == 4.8
    assert res.p_success_mitigated == 73.8
    assert res.var_95_equity == -71.0
    assert res.cvar_95_equity == -88.4


# ==============================================================================
# Model 03: Multi-Stage Real Options Valuation Engine (BSM & LSMC)
# ==============================================================================
def test_03_real_options_lsmc_bsm():
    """Verify Model 03 Black-Scholes-Merton, Greeks, LSMC American option, and Gate 1."""
    assert hasattr(ro_mod, "BlackScholesExpansion")
    assert hasattr(ro_mod, "LongstaffSchwartzAmericanOption")
    assert hasattr(ro_mod, "StageGateAbandonmentModel")
    assert hasattr(ro_mod, "RealOptionsEngine")
    
    engine = ro_mod.RealOptionsEngine()
    res = engine.evaluate_all()
    
    # 1. BSM Closed-Form
    bsm = res["bsm"]
    assert abs(bsm["C0"] - 192.79) < 0.01
    assert abs(bsm["pv_C0"] - 142.10) < 0.01
    assert abs(bsm["d1"] - 1.141) < 0.005
    assert abs(bsm["d2"] - 0.582) < 0.005
    assert abs(bsm["N_d1"] - 0.873) < 0.005
    assert abs(bsm["N_d2"] - 0.720) < 0.005
    assert 0.0 < bsm["delta"] < 1.0
    assert bsm["gamma"] > 0.0
    assert bsm["vega"] > 0.0
    assert bsm["theta"] < 0.0
    assert bsm["rho"] > 0.0
    
    # 2. LSMC American Option
    lsmc = res["lsmc"]
    assert abs(lsmc["lsmc_value"] - 194.22) < 0.01
    assert abs(lsmc["early_exercise_premium"] - 1.43) < 0.01
    assert lsmc["early_exercise_premium"] >= 0.0
    
    # 3. Gate 1 Exploration Abandonment
    ab = res["abandonment"]
    assert abs(ab["abandonment_option_value"] - 28.40) < 0.01
    assert abs(ab["gate1_deferral_option_value"] - 54.76) < 0.01
    assert abs(ab["max_equity_loss"] - 27.0) < 0.01


# ==============================================================================
# Model 04: Market Microstructure & Valuation Accretion
# ==============================================================================
def test_04_market_microstructure_float():
    """Verify Model 04 free float calculation, index eligibility, and equity accretion."""
    assert hasattr(micro_mod, "MarketMicrostructureAnalyzer")
    assert hasattr(micro_mod, "MarketMicrostructureEngine")
    
    analyzer = micro_mod.MarketMicrostructureAnalyzer()
    
    # 1. Ownership & Float
    breakdown = analyzer.calculate_ownership_breakdown()
    assert abs(breakdown["free_float_pct"] - 3.01) < 0.01
    assert breakdown["free_float_shares"] == 4_026_965_222
    assert breakdown["index_status"] == "CONSTRAINED"
    assert breakdown["msci_compliant"] is False
    assert breakdown["ftse_compliant"] is False
    
    # 2. Peer Benchmarking
    peers = analyzer.calculate_peer_benchmarking()
    assert isinstance(peers, pd.DataFrame)
    assert len(peers) == 4
    assert "BREN (Indonesia)" in peers["Company"].values
    
    # 3. Value Accretion per Share
    accretion = analyzer.calculate_equity_accretion()
    assert abs(accretion["delta_base_idr_per_share"] - 4.52) < 0.01
    assert abs(accretion["delta_strategic_idr_per_share"] - 26.91) < 0.01
    assert accretion["parent_equity_dilution_pct"] == 0.00
    assert accretion["debt_recourse_to_parent"] is False


def test_04_market_microstructure_custom_float():
    """Verify index compliance when float exceeds 5.0%."""
    custom_cfg = micro_mod.MarketDataConfig(
        shareholders={"Parent": 0.80}  # 20% free float
    )
    analyzer = micro_mod.MarketMicrostructureAnalyzer(config=custom_cfg)
    breakdown = analyzer.calculate_ownership_breakdown()
    assert breakdown["free_float_pct"] == 20.00
    assert breakdown["index_status"] == "ELIGIBLE"
    assert breakdown["msci_compliant"] is True


# ==============================================================================
# Model 05: Finite-Horizon Gordon Growth Model & Dividend Policy
# ==============================================================================
def test_05_finite_gordon_dividend():
    """Verify Model 05 perpetual vs finite GGM, lock-up assertions, and residual policy."""
    assert hasattr(div_mod, "DividendPolicyModel")
    assert hasattr(div_mod, "FiniteGordonDividendEngine")
    
    model = div_mod.DividendPolicyModel()
    
    # 1. Perpetual GGM
    perp = model.calculate_perpetual_ggm()
    assert abs(perp["equity_value_cod_perpetual"] - 119.17) < 0.01
    assert abs(perp["pv_perpetual_t0"] - 78.50) < 0.01
    
    # 2. Finite Horizon GGM (30 years)
    finite = model.calculate_finite_horizon_ggm()
    assert abs(finite["equity_value_cod_finite"] - 93.32) < 0.01
    assert abs(finite["pv_finite_t0"] - 62.03) < 0.01
    assert abs(finite["finite_annuity_factor"] - 0.7831) < 0.001
    assert abs(finite["truncation_loss_cod"] - 25.85) < 0.01
    
    # 3. Dividend Lock-up & Banking Covenants
    lockup = model.evaluate_covenant_dividend_lockup()
    assert lockup["construction_dividend_allowed"] is False
    assert lockup["project_dscr_covenant"] >= 1.30
    assert lockup["dsra_reserve_months"] == 6
    
    # 4. Residual Dividend Waterfall
    residual = model.calculate_residual_dividend_schedule()
    assert residual["payout_ratio"] == 0.40
    assert residual["fcfe_residual_annual"] > 0.0
    assert residual["dividend_distributed_annual"] > 0.0


def test_05_finite_gordon_concession_horizon():
    """Verify finite horizon sensitivity: longer concessions converge towards perpetual."""
    p_30 = div_mod.GordonParameters(concession_operational_years=30)
    p_50 = div_mod.GordonParameters(concession_operational_years=50)
    
    m_30 = div_mod.DividendPolicyModel(params=p_30)
    m_50 = div_mod.DividendPolicyModel(params=p_50)
    
    f_30 = m_30.calculate_finite_horizon_ggm()
    f_50 = m_50.calculate_finite_horizon_ggm()
    
    assert f_50["equity_value_cod_finite"] > f_30["equity_value_cod_finite"]
    assert f_50["finite_annuity_factor"] > f_30["finite_annuity_factor"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
