# Quantitative Software Architecture Specification
## Institutional Refactoring of Financial & Econometrics Models (`TUGAS4/models/`)

**Author:** Quantitative Software Architect (`@quant-architect`)  
**Status:** Approved Architectural Blueprint  
**Target Directory:** `e:\mankeu\TUGAS4\models\`  
**Target Files:**
1. `01_project_finance_dcf.py` (Generalized Project Finance & Waterfall DCF Engine)
2. `02_monte_carlo_sobol_copula.py` (Quasi-Monte Carlo Sobol Sequence & Student-t Copula)
3. `03_real_options_lsmc_bsm.py` (Multi-Stage BSM & American Longstaff-Schwartz Engine)
4. `04_market_microstructure_float.py` (Market Microstructure, Free Float & Multiples)
5. `05_finite_gordon_dividend.py` (Finite-Horizon Gordon Growth & Residual Dividend Engine)

---

## 1. Executive Summary & Anti-Slop Directives

The existing codebase in `e:\mankeu\TUGAS4\models/` exhibits critical markers of artificial generation ("AI slop") and lack of software engineering discipline:
1. **Decorative Banners & Academic Slogans**: Every file features 10-line ASCII headers with institutional names ("PROGRAM MAGISTER MANAJEMEN TEKNOLOGI ITS", "KELOMPOK 1"), violating professional repository standards.
2. **Hardcoded Numbers Masquerading as Calculations**:
   - In `01_project_finance_dcf.py`: Waterfall benefits (`wacc_benefit = 142.42`, `tax_holiday_benefit = 24.20`, `carbon_benefit = 18.52`, `expansion_real_option = 142.10`) are hardcoded scalars rather than derived from dynamic cash flow vectors.
   - In `02_monte_carlo_sobol_copula.py`: Monte Carlo output is faked via an artificial rank-normal transform (`npv_baseline_calibrated = -105.11 + 63.1 * stats.norm.ppf(...)`) instead of evaluating cash flows path-by-path across the 16,384 simulated paths.
   - In `03_real_options_lsmc_bsm.py`: Abandonment option is hardcoded (`v_abandonment_calibrated = 28.40`).
   - In `05_finite_gordon_dividend.py`: Operating cash flow parameters (`ebitda_op = 44.14`, `debt_service_avg = 40.0`) are hardcoded singletons.
3. **Procedural Print Sprawls**: Modules cannot be imported cleanly as libraries. Calling functions triggers dozens of print statements instead of returning structured data.
4. **Zero Generalization**: All models are hardcoded to a single case study without parameterization or reusability for other energy or infrastructure projects.

### Mandatory Refactoring Principles:
- **Object-Oriented & Functional Design**: Dataclass-driven configurations with sensible defaults matching the BREN Hamiding case study, but fully parameterized for arbitrary project valuation.
- **Dynamic Calculation Invariant**: All values must be calculated from first principles (cash flow schedules, compounding discount factors, dynamic tax holidays, Cholesky decompositions, backward induction regressions).
- **Silent Computation**: Core methods return structured dataclasses, dictionaries, or `pandas.DataFrame` objects. Console output is strictly confined to `if __name__ == '__main__':` and formatted as concise, professional tabular summaries.
- **Complete Elimination of AI Slop**: Zero ASCII art, zero "KELOMPOK 1", zero decorative padding. Standard PEP 257 docstrings and PEP 484 type annotations throughout.

---

## 2. Detailed Technical Specifications per Model

### Model 1: `01_project_finance_dcf.py`
**Target Class:** `ProjectFinanceDCF`

#### A. Configuration Dataclass: `ProjectParameters`
```python
@dataclass(frozen=True)
class ProjectParameters:
    # Capacity and Physical Metrics
    capacity_mw: float = 60.0
    capacity_factor: float = 0.9220  # 92.20%
    annual_degradation: float = 0.005  # 0.5% annual degradation
    
    # Capital Expenditure & Construction
    capex_total_usd_m: float = 720.0
    construction_years: int = 4
    operational_years: int = 30
    
    # Commercial & Tariff
    tariff_usd_per_mwh: float = 97.0  # USD 97 / MWh (equivalent to 9.7 cents / kWh)
    carbon_price_usd_per_ton: float = 8.0  # SPE-GRK IDXCarbon
    grid_emission_factor: float = 0.75  # tCO2 avoided per MWh
    
    # Operating Expenditures
    opex_fixed_usd_m: float = 12.0
    opex_variable_usd_per_mwh: float = 8.50
    opex_escalation_rate: float = 0.025  # 2.5% inflation
    
    # Capital Structure & Cost of Capital
    debt_ratio: float = 0.70  # 70% Debt / 30% Equity
    cost_of_debt: float = 0.0450  # 4.50% Green Loan Syndication
    risk_free_rate: float = 0.0450  # 10Y Benchmark
    market_risk_premium: float = 0.0650  # 6.50%
    unlevered_beta: float = 0.65  # Geothermal asset beta
    
    # Fiscal Policy & Incentives
    statutory_tax_rate: float = 0.22  # 22% Indonesian Corporate Income Tax
    tax_holiday_years: int = 10  # 100% CIT reduction (PMK 130/2020)
    tax_holiday_transition_years: int = 2  # 50% CIT reduction (Years 11-12)
    
    # Benchmark Comparison Parameters (Syllabus DCF)
    syllabus_wacc: float = 0.1020  # 10.20%
    syllabus_capex: float = 720.0
    syllabus_annual_cf: float = 66.31
    syllabus_payback_cf: float = 67.70
```

#### B. Mathematical Equations & Methods:
1. **Cost of Capital & Hamada Relevering**:
   $$\beta_L = \beta_U \left[1 + (1 - \tau) \frac{D}{E}\right]$$
   $$K_e = R_f + \beta_L \times MRP$$
   $$WACC = \frac{E}{V} K_e + \frac{D}{V} K_d (1 - \tau)$$
2. **Annual Cash Flow Engine (`build_cash_flow_schedule`)**:
   For year $t \in \{1, \dots, N_{ops}\}$:
   - Generation: $E_t = \text{Capacity} \times 8,760 \times \text{CF} \times (1 - \delta)^{t-1}$ (MWh)
   - Energy Revenue: $R_{energy, t} = E_t \times \text{Tariff}$
   - Carbon Revenue: $R_{carbon, t} = E_t \times \text{EmissionFactor} \times P_{carbon}$
   - Total Revenue: $R_t = R_{energy, t} + R_{carbon, t}$
   - OPEX: $OPEX_t = (\text{OPEX}_{fixed} + \text{OPEX}_{var} \times E_t) \times (1 + \pi_{inf})^{t-1}$
   - $EBITDA_t = R_t - OPEX_t$
   - Straight-Line Depreciation: $\text{Depr}_t = \frac{\text{Capex}}{N_{depr}}$
   - $EBIT_t = EBITDA_t - \text{Depr}_t$
   - Debt Schedule: $D_0 = \text{Capex} \times \text{Debt Ratio}$. Level principal repayment $P_t = D_0 / N_{debt}$. Interest $I_t = D_{t-1} \times K_d$.
   - Taxable Income: $EBT_t = EBIT_t - I_t$.
   - Dynamic Tax Rate:
     $$\tau_t = \begin{cases} 0.0 & t \le 10 \\ 0.5 \times \tau_{statutory} & 11 \le t \le 12 \\ \tau_{statutory} & t > 12 \end{cases}$$
     $$\text{Tax}_t = \max(0, EBT_t) \times \tau_t$$
   - $NOPAT_t = EBIT_t \times (1 - \tau_t)$
   - $FCFF_t = NOPAT_t + \text{Depr}_t - \text{Capex Maintenance}_t - \Delta NWC_t$
   - $FCFE_t = FCFF_t - I_t (1 - \tau_t) - P_t$
   - $DSCR_t = \frac{CFADS_t}{\text{Debt Service}_t} = \frac{EBITDA_t - \text{Tax}_t}{P_t + I_t}$
3. **Discounted Valuation & Root-Finding**:
   - Discount factor: $DF_t = (1 + WACC)^{-t}$
   - $NPV = \sum_{t=1}^{N} FCFF_t \cdot DF_t - \text{Capex}_0$
   - $IRR$: Exact root finding via `scipy.optimize.brentq` of $NPV(\rho) = 0$.
   - Discounted and simple payback periods.
4. **Strategic Waterfall Valuation**:
   Calculate exact PV differences between:
   - Base Syllabus DCF ($WACC = 10.20\%$, no carbon, no tax holiday)
   - WACC correction (recomputed at $WACC = 7.10\%$)
   - Tax Holiday fiscal benefit (PV of tax savings over standard 22% rate)
   - Carbon credit monetization (PV of SPE-GRK credits)
   - Real options expansion value (imported or passed as parameter)

---

### Model 2: `02_monte_carlo_sobol_copula.py`
**Target Class:** `SobolCopulaMonteCarlo`

#### A. Configuration Dataclass: `MonteCarloConfig`
```python
@dataclass
class MonteCarloConfig:
    n_simulations: int = 16384  # 2^14 for Sobol low-discrepancy optimality
    random_seed: int = 42
    scramble_sobol: bool = True
    copula_df: int = 4  # Heavy-tail Student-t copula degrees of freedom
    
    # Correlation Matrix (Spearman Rank): [Enthalpy, FX USD/IDR, O&M Escalation, Capacity Factor]
    correlation_matrix: np.ndarray = field(default_factory=lambda: np.array([
        [ 1.00,  0.05, -0.15,  0.72],
        [ 0.05,  1.00,  0.48, -0.10],
        [-0.15,  0.48,  1.00, -0.25],
        [ 0.72, -0.10, -0.25,  1.00]
    ]))
```

#### B. Mathematical Pipeline:
1. **Quasi-Random Sampling**:
   - `scipy.stats.qmc.Sobol(d=4, scramble=True, seed=seed).random(n=n_simulations)`
   - Uniform to Gaussian marginals: $Z_0 = \Phi^{-1}(\text{clip}(U, 10^{-6}, 1 - 10^{-6}))$.
2. **Correlation Induction**:
   - Cholesky decomposition of rank correlation $\Sigma = L L^T$.
   - $Z = Z_0 L^T$.
3. **Student-t Copula Transformation**:
   - Generate independent $\chi^2(\nu)$ samples: $W \sim \chi^2(\nu)$.
   - Student-t vectors: $T_i = Z_i / \sqrt{W_i / \nu}$.
   - Uniform marginals via Student-t CDF: $U_i = F_{\nu}(T_i)$.
4. **Marginal Inverse Transforms**:
   - Enthalpy ($kJ/kg$): Log-normal distribution with $\mu_{log} = \ln(2250), \sigma_{log} = 0.053$.
   - FX Rate (USD/IDR): Truncated normal on $[14500, 19500]$, mean 16205, std 1200.
   - O&M Escalation (%): Normal with mean 0.032, std 0.008.
   - Capacity Factor (%): Beta distribution scaled to $[0.82, 0.9988]$, mean $92.20\%$.
5. **Path-by-Path Cash Flow Valuation**:
   - Vectorized evaluation of project cash flows across all 16,384 paths.
   - True trajectory NPV computation (no rank-normal faking!).
6. **Risk Metrics**:
   - $P(NPV > 0)$
   - $VaR_{95\%} = \text{Percentile}(NPV, 5)$
   - $CVaR_{95\%} = \mathbb{E}[NPV \mid NPV \le VaR_{95\%}]$

---

### Model 3: `03_real_options_lsmc_bsm.py`
**Target Classes:** `BlackScholesExpansion`, `LongstaffSchwartzAmericanOption`

#### A. BSM Closed-Form Engine (`BlackScholesExpansion`):
- Inputs: Underlying Asset PV $S_0$ (USD 257.60M), Strike $K$ (USD 140.00M), Horizon $T$ (3.0 yrs), Risk-free rate $r$ (4.50%), Volatility $\sigma$ (32.50%), WACC (7.10%).
- Computes:
  $$d_1 = \frac{\ln(S_0 / K) + (r + 0.5 \sigma^2) T}{\sigma \sqrt{T}}, \quad d_2 = d_1 - \sigma \sqrt{T}$$
  $$C_0 = S_0 N(d_1) - K e^{-r T} N(d_2)$$
  $$PV(C_0) = \frac{C_0}{(1 + WACC)^T}$$
- Greeks: $\Delta, \Gamma, \Theta, \mathcal{V}, \rho$.

#### B. American LSMC Engine (`LongstaffSchwartzAmericanOption`):
- Simulates Geometric Brownian Motion paths for asset value:
  $$S_{t+\Delta t} = S_t \exp\left( (r - 0.5 \sigma^2)\Delta t + \sigma \sqrt{\Delta t} Z \right)$$
- Backward induction with orthogonal Laguerre polynomials:
  Basis functions: $L_0(x) = 1$, $L_1(x) = 1 - x$, $L_2(x) = 1 - 2x + \frac{x^2}{2}$.
  Regresses discounted continuation value on in-the-money paths.
- Evaluates early exercise boundary at each intermediate decision node.

#### C. Stage-Gate Abandonment Option:
- Evaluates Gate 1 Exploration Phase (Exploration Capex $USD 90M$ vs remaining $USD 630M$ protected).
- Formulates abandonment value as an American put / decision tree salvage option:
  $$V_{abandon} = \mathbb{E}\left[\max(K_{salvage} - S_{explor}, 0)\right]$$
  Derived from geological risk probability and Capex savings.

---

### Model 4: `04_market_microstructure_float.py`
**Target Class:** `MarketMicrostructureEngine`

#### A. Configuration Dataclass: `MarketDataConfig`
```python
@dataclass
class MarketDataConfig:
    ticker: str = "BREN.JK"
    total_shares_outstanding: int = 133_786_220_000
    current_share_price_idr: float = 8250.0
    usd_idr_exchange_rate: float = 16205.0
    
    # Ownership Breakdown
    shareholders: Dict[str, float] = field(default_factory=lambda: {
        "PT Barito Pacific Tbk": 0.64666,
        "Green Era Energy Pte. Ltd.": 0.23603,
        "Prajogo Pangestu & Affiliates": 0.08721,
    })
```

#### B. Core Capabilities:
1. **Ownership & Free Float Mechanics**:
   - Calculates effective public free float percentage ($1.0 - \sum \text{controlled} = 3.01\%$).
   - Calculates free float shares and free float market capitalization.
   - Evaluates compliance against MSCI / FTSE minimum free float threshold (5.00%).
2. **Liquidity Friction & Amihud Illiquidity Estimator**:
   - Implementation of Amihud (2002) ratio:
     $$ILLIQ = \frac{1}{D} \sum_{t=1}^D \frac{|R_t|}{\text{Volume}_{IDR, t}}$$
   - Roll (1984) bid-ask spread proxy:
     $$\text{Spread} = 2 \sqrt{-\operatorname{Cov}(\Delta P_t, \Delta P_{t-1})} \quad (\text{if Cov} < 0)$$
3. **Peer Valuation Multiples Matrix**:
   - Accepts arbitrary peer dictionary/DataFrame.
   - Computes peer median, mean, EV/EBITDA, P/E, and EV/MW.
   - Measures premium / discount of subject firm.
4. **Project Equity Value Accretion**:
   - Accretion per share:
     $$\Delta \text{Equity Value per Share (IDR)} = \frac{\Delta \text{Project Equity NPV (USD)} \times FX}{\text{Total Shares Outstanding}}$$
   - Non-recourse debt isolation verification (parent debt covenants undisturbed).

---

### Model 5: `05_finite_gordon_dividend.py`
**Target Class:** `FiniteGordonDividendEngine`

#### A. Configuration Dataclass: `GordonParameters`
```python
@dataclass
class GordonParameters:
    cost_of_equity: float = 0.1075  # 10.75%
    dividend_growth_rate: float = 0.0525  # 5.25%
    d1_first_year_dividend_usd_m: float = 6.55435
    concession_years: int = 30
    gestation_years: int = 4
```

#### B. Core Capabilities:
1. **Perpetual vs. Finite-Horizon Gordon Growth Model**:
   - Perpetual GGM:
     $$P_{COD}^{perp} = \frac{D_1}{K_e - g}$$
   - Finite Horizon GGM (30-year concession):
     $$P_{COD}^{finite} = \frac{D_1}{K_e - g} \left[ 1 - \left( \frac{1 + g}{1 + K_e} \right)^N \right]$$
   - Gestation Discounting to $t=0$:
     $$P_{t=0} = \frac{P_{COD}}{(1 + K_e)^{t_{gestation}}}$$
2. **Accounting & Covenant Dividend Lock-Up**:
   - Evaluates PSAK 216 / IAS 16 Assets Under Construction (AUC) constraint: zero operating dividends during construction gestation.
   - Evaluates Green Syndicate Loan Covenants:
     - Minimum Project DSCR $\ge 1.30\times$.
     - Minimum Consolidated DSCR $\ge 1.35\times$.
     - 6-month Debt Service Reserve Account (DSRA) funding precondition.
3. **Residual Dividend Policy**:
   - Computes Free Cash Flow to Equity (FCFE):
     $$FCFE_t = \max(0, EBITDA_t - \text{Debt Service}_t - \text{Capex Maintenance}_t)$$
   - Annual dividend projection under configurable target payout ratio ($40\%$).

---

## 3. Acceptance Criteria (`AC-NNN`)

- **AC-001 [Configurability]**: All 5 models are encapsulated in classes with type-hinted `@dataclass` configuration objects. Every hardcoded number has been replaced with a configurable parameter.
- **AC-002 [Dynamic Mathematics]**: Hardcoded scalar dictionary dumps are eliminated. Cash flow tables, tax holidays, debt schedules, discounting, and copula paths are dynamically computed.
- **AC-003 [True Monte Carlo]**: Model 02 runs true path-by-path stochastic simulation across all 16,384 paths using Scrambled Sobol sequences and Student-t copula, with zero rank-normal calibration faking.
- **AC-004 [Clean CLI & Zero AI Slop]**: All ASCII art banners, "KELOMPOK 1", and cosmetic print statements are eliminated. Direct execution prints clean, institutional tables.
- **AC-005 [Importability & Testing]**: Every model can be cleanly imported as a library (`from models.project_finance_dcf import ProjectFinanceDCF`), runs without errors, and passes programmatic unit assertions.

---

## 4. Work Delegation & Handoff Specification

- **Architect (`@quant-architect`)**: Deliver this specification and spawn/direct `@quant-coder`.
- **Implementer (`@quant-coder`)**: Refactor all 5 files in `e:\mankeu\TUGAS4\models\` to strictly comply with this specification and pass test verification.
