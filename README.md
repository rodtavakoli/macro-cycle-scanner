# Macro-Cycle-Scanner

Macro-financial regime diagnostics using topological data analysis.

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Overview

To understand the now, you need to understand what happened before.

Macro-Cycle-Scanner is a system initially designed for personal macro economic understanding and speculation that evolved into a comprehensive regime coherence tool across century wide horizons. 

Rather than forecasting prices, this project focuses on identifying when macroeconomic and market systems lose structural alignment, which is a condition historically associated with elevated systemic stress and asymmetric downside risk.

The core output is a composite diagnostic signal, the Coherence Collapse Index (CCI), which summarizes cross-system fragmentation using nonlinear and validation-first techniques.

> Note: This repository is intended as a research showcase.  
> Core model logic, parameterization, and production workflows are intentionally abstracted.


## Conceptual Motivation

Traditional correlation analysis answers whether assets move together locally.  
This project instead asks a different question:

> Are macro-financial systems exhibiting coherent structural behavior over time?

To answer this, the system evaluates cyclical recurrence, dispersion, and alignment across multiple macro and asset-level signals, emphasizing regime awareness over point prediction.

The framework is inspired by:
- long-cycle macro analysis (e.g. Ray Dalio / Robert E. Dewey-style cycle research),
- persistent homology applications in finance,
- regime-based macro frameworks,
- and modern nonlinear time-series analysis.


## What the System Produces

At a high level, the system provides:

- Regime diagnostics (stable, transitionary, fragmented)
- Cross-system coherence measures
- Stress-conditioned outcome analysis
- Asset-level signal usability comparisons
- Validation context across lead–lag structures

The outputs are explicitly diagnostic and speculative rather than predictive and are designed to support reasoning under uncertainty.


## Dashboard Outputs

Results are explored and summarized through an interactive Power BI dashboard composed of several analytical layers:

### Macro Overview  
Long-run macro indicators including inflation, liquidity, labor conditions, yield curve structure, and composite stress metrics.

### Metals  
Precious-metals behavior, relative value relationships, and momentum context.

### Metals vs Macro  
Cross-system relationships between metals, liquidity conditions, and macro composites.

### Cycle Analysis  
Cycle-length exploration and rolling validation under multiple temporal assumptions.

### Macro Confidence Snapshot  
Primary diagnostic view: current coherence regime, confidence state, and macro stress assessment.

### Regime Validation & Stress Behavior  
Historical validation context, drawdown behavior during similar regimes, and asset-level signal usability.

Visual exports are included for reference; underlying dashboard logic is not distributed.


## Key Empirical Observations

Across historical samples, periods characterized by elevated coherence fragmentation tend to coincide with:

- reduced cross-asset alignment,
- increased dispersion across systems,
- and asymmetric downside behavior in risk assets.

Validation strength varies meaningfully across assets and time horizons, reinforcing the importance of regime-aware interpretation rather than signal optimization.


## Methodological Perspective

This project applies nonlinear state-space reasoning and topological persistence concepts to macro-financial time series in order to distinguish genuine structural behavior from noise.

Parameterization and construction choices follow established practices in the academic literature and are evaluated through stability and sensitivity checks. The emphasis is on robust diagnostics, not optimized performance.

Full mathematical and implementation details are intentionally omitted from this public repository.


## Repository Contents

This repository includes:

- Research notebooks demonstrating exploratory analysis and conceptual workflows  
- Business Intelligence Dashboard to visualize aggregated results
- Supporting scripts and configuration scaffolding  
- Documentation and figures used for portfolio presentation  

Raw data sources, intermediate research artifacts, and full production logic are deliberately excluded.


## Limitations

- In-sample analysis only; no walk-forward deployment  
- Sensitivity to regime definition and temporal assumptions  
- Uneven historical coverage across macro variables (normalized)
- No formal null-hypothesis testing via surrogate data

These limitations are acknowledged by design and motivate ongoing research rather than definitive claims.


## Intended Use

This project is intended for:

- personal tool for macro-economic understanding and speculation
- research discussion
- methodological exploration
- portfolio demonstration

It is not intended for trading, forecasting, or operational decision-making.


## References

1. Takens, F. (1981). *Detecting strange attractors in turbulence.*  
2. Edelsbrunner, H. & Harer, J. (2010). *Computational Topology.*  
3. Perea, J.A. & Harer, J. (2015). *Sliding windows and persistence.*  
4. Gidea, M. & Katz, Y. (2018). *Topological data analysis of financial time series.*


## Author

Rod Tavakoli  
GitHub: https://github.com/rodtavakoli
