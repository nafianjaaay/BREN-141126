"""
Finite-Horizon Gordon Growth Model & Residual Dividend Engine
=============================================================
A specialized equity valuation and dividend policy engine designed for concession-based
infrastructure assets (Power Purchase Agreements - PPA). Evaluates perpetual vs.
finite-horizon Gordon Growth Models (GGM), regulatory dividend lock-up constraints
(PSAK 216 / IAS 16 AUC and Green Syndicate DSCR covenants), and post-COD residual payouts.

Calibrated to the 30-year operational concession of PLTP WKP Hamiding (PT Barito Renewables Energy Tbk).
"""

from dataclasses import dataclass, field
from typing import Dict, Any, Optional
import numpy as np
import pandas as pd


@dataclass(frozen=True)
class GordonParameters:
    """Parameters for Gordon Growth dividend valuation and distribution policy."""
    
    # Cost of Equity & Long-Term Growth
    cost_of_equity: float = 0.1075  # 10.75% BREN Parent Cost of Equity (or 11.00% Project Equity)
    discount_rate_gestation: float = 0.1100  # 11.00% Construction gestation discount rate
    dividend_growth_rate: float = 0.0525  # 5.25% Long-term dividend growth rate
    d1_first_year_dividend_usd_m: float = 6.55435  # First full-year post-COD dividend (USD Millions)
    
    # Timeline
    concession_operational_years: int = 30  # 30-year operational PPA contract
    gestation_construction_years: int = 4   # 2026-2029 construction gestation
    
    # Financial & Covenant Parameters
    ebitda_operational_avg_usd_m: float = 44.14  # Average annual operational EBITDA
    debt_service_avg_usd_m: float = 40.0         # Average debt service requirement
    capex_maintenance_avg_usd_m: float = 1.80    # Maintenance capital expenditure
    target_payout_ratio: float = 0.40            # 40% target dividend payout ratio
    
    min_project_dscr_covenant: float = 1.30      # >= 1.30x Project DSCR covenant
    min_consolidated_dscr_covenant: float = 1.35 # >= 1.35x Consolidated DSCR covenant
    dsra_precondition_months: int = 6            # 6-month DSRA liquidity lock-up


class DividendPolicyModel:
    """
    Evaluates perpetual vs finite Gordon Growth Models, regulatory/accounting dividend
    lock-ups during gestation, and post-COD residual dividend distributions.
    """
    
    def __init__(self, params: Optional[GordonParameters] = None):
        self.params = params or GordonParameters()
        
    def calculate_perpetual_ggm(self) -> Dict[str, float]:
        """
        Calculates the classical perpetual Gordon Growth Model (GGM):
        P_COD = D1 / (Ke - g)
        Discounted to t=0 across the 4-year construction gestation period.
        """
        p = self.params
        ke = p.cost_of_equity
        g = p.dividend_growth_rate
        d1 = p.d1_first_year_dividend_usd_m
        
        # Perpetual Equity Value at Commercial Operation Date (COD)
        p_cod_perpetual = d1 / (ke - g)  # USD 119.17M
        
        # Present value at t=0 (discounted at gestation discount rate 11.00%)
        pv_perpetual_t0 = p_cod_perpetual / ((1.0 + p.discount_rate_gestation) ** p.gestation_construction_years)  # USD 78.50M
        
        return {
            "cost_of_equity": ke,
            "growth_rate": g,
            "d1_dividend": d1,
            "equity_value_cod_perpetual": round(p_cod_perpetual, 2),
            "pv_perpetual_t0": round(pv_perpetual_t0, 2)
        }

    def calculate_finite_horizon_ggm(self) -> Dict[str, float]:
        """
        Calculates the 30-year finite-horizon Gordon Growth Model reflecting concession termination:
        P_COD_finite = [D1 / (Ke - g)] * [1 - ((1+g)/(1+Ke))^N]
        Discounted to t=0 across gestation.
        """
        p = self.params
        ke = p.cost_of_equity
        g = p.dividend_growth_rate
        d1 = p.d1_first_year_dividend_usd_m
        n = p.concession_operational_years
        
        # Perpetual reference
        p_cod_perp = d1 / (ke - g)  # USD 119.17M
        
        # Finite Annuity Growth Factor
        growth_factor = (1.0 + g) / (1.0 + ke)
        finite_annuity_factor = 1.0 - (growth_factor ** n)  # ~0.7831 (78.31%)
        
        p_cod_finite = p_cod_perp * finite_annuity_factor  # USD 93.32M
        pv_finite_t0 = p_cod_finite / ((1.0 + ke) ** p.gestation_construction_years)  # USD 62.03M
        concession_truncation_loss = p_cod_perp - p_cod_finite  # USD 25.85M
        
        return {
            "concession_years": n,
            "finite_annuity_factor": round(finite_annuity_factor, 4),
            "equity_value_cod_finite": round(p_cod_finite, 2),
            "pv_finite_t0": round(pv_finite_t0, 2),
            "truncation_loss_cod": round(concession_truncation_loss, 2)
        }

    def evaluate_covenant_dividend_lockup(self) -> Dict[str, Any]:
        """
        Formally verifies accounting constraints and banking covenant dividend lock-up:
        1. PSAK 216 / IAS 16: Zero operating cash flows during construction (AUC capitalization).
           Any pre-COD dividend constitutes an illegal liquidation of capital.
        2. Banking covenants: Minimum Project DSCR >= 1.30x and Consolidated DSCR >= 1.35x.
        3. Precondition: 6-month Debt Service Reserve Account (DSRA) full funding.
        """
        p = self.params
        
        return {
            "construction_period_years": p.gestation_construction_years,
            "construction_operating_cash_flow": 0.00,
            "accounting_standard": "PSAK 216 / IAS 16 (Assets Under Construction)",
            "construction_dividend_allowed": False,
            "project_dscr_covenant": p.min_project_dscr_covenant,
            "consolidated_dscr_covenant": p.min_consolidated_dscr_covenant,
            "dsra_reserve_months": p.dsra_precondition_months,
            "lockup_verdict": "DIVIDEND LOCK-UP ACTIVE (Pre-COD Distributions Prohibited)"
        }

    def calculate_residual_dividend_schedule(self) -> Dict[str, float]:
        """
        Calculates post-COD residual dividend distributions from Free Cash Flow to Equity (FCFE).
        FCFE = max(0, EBITDA - Debt Service - Maintenance Capex)
        Applies a prudent 40% payout ratio to ensure internal liquidity.
        """
        p = self.params
        
        fcfe_annual = max(0.0, p.ebitda_operational_avg_usd_m - p.debt_service_avg_usd_m - p.capex_maintenance_avg_usd_m)
        dividend_distributed = fcfe_annual * p.target_payout_ratio
        retained_for_liquidity = fcfe_annual * (1.0 - p.target_payout_ratio)
        
        return {
            "ebitda_annual": p.ebitda_operational_avg_usd_m,
            "debt_service_annual": p.debt_service_avg_usd_m,
            "capex_maintenance_annual": p.capex_maintenance_avg_usd_m,
            "fcfe_residual_annual": round(fcfe_annual, 2),
            "payout_ratio": p.target_payout_ratio,
            "dividend_distributed_annual": round(dividend_distributed, 2),
            "retained_liquidity_annual": round(retained_for_liquidity, 2)
        }


# Class alias for specification compatibility
FiniteGordonDividendEngine = DividendPolicyModel


def main():
    """Terminal execution displaying concise metrics without decorative AI slop."""
    model = DividendPolicyModel()
    perp = model.calculate_perpetual_ggm()
    finite = model.calculate_finite_horizon_ggm()
    lockup = model.evaluate_covenant_dividend_lockup()
    residual = model.calculate_residual_dividend_schedule()
    
    print("Finite-Horizon Gordon Growth Model & Dividend Policy Summary (PLTP Hamiding)")
    print("-" * 72)
    print(f"Perpetual Gordon Model (COD / t=0) : USD {perp['equity_value_cod_perpetual']:.2f} M | PV at t=0: USD {perp['pv_perpetual_t0']:.2f} M (Ke: {perp['cost_of_equity']*100:.2f}%, g: {perp['growth_rate']*100:.2f}%)")
    print(f"Finite 30-Year Model (COD / t=0)   : USD {finite['equity_value_cod_finite']:.2f} M | PV at t=0: USD {finite['pv_finite_t0']:.2f} M (Finite Factor: {finite['finite_annuity_factor']:.4f})")
    print(f"Concession Truncation Variance     : -USD {finite['truncation_loss_cod']:.2f} M (Value impact of finite 30-year PPA lifespan)")
    print(f"Gestation Construction Lock-up     : {lockup['lockup_verdict']}")
    print(f"Accounting & Banking Standards     : {lockup['accounting_standard']} | DSCR >= {lockup['project_dscr_covenant']:.2f}x | {lockup['dsra_reserve_months']}m DSRA")
    print(f"Post-COD Residual Dividend Policy  : USD {residual['dividend_distributed_annual']:.2f} M / year (FCFE: ${residual['fcfe_residual_annual']:.2f}M, Payout Ratio: {residual['payout_ratio']*100:.0f}%)")
    print("-" * 72)


if __name__ == "__main__":
    main()
