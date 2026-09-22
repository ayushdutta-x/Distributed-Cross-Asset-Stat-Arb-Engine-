# Distributed Cross Asset Statistical Arbitrage engine


### Tech stack:
1. Python 3.9+
2. statsmodels
3. CVXPY
4. Redis / ZeroMQ
5. asyncio
6. NumPy / Pandas
7. scipy.optimize


### Concepts required:
1) Johansen Test & eigenvalue interpretation
2) Vector Error Correction Models (VECM)
3) Distributed Pub/Sub Systems
4) Convex Optimization under constraints
5) Square root market impact model
6) Short borrow cost modelling


### Data Sources
1) yfinance (Yahoo finance) - daily adjusted close
2) Binance / Bybit API - live crypto HFT data
3) Alpaca / Polygon.io - minute level sector ETFs


## The problem I tried to solve
Standard pairs trading relies on identifying simple, two-asset mean-reverting
relationships. However, modern financial markets are highly correlated ecosystems. In
institutional quantitative trading, alpha is extracted not just from pairs, but from
complex, high-dimensional baskets of assets moving together in an equilibrium state.
The ability to mathematically identify these multivariate relationships and build the
infrastructure to trade them synchronously is a highly sought-after skill on quantitative
trading desks.
This project bridges the gap between advanced multivariate econometrics and
distributed systems engineering. You will build a "Large" statistical arbitrage system that
identifies cointegration in a k-dimensional space, models the speed of mean reversion,
and executes dynamic hedges across a distributed, event-driven architecture.
The true challenge of this project isn't just the math, it is the system constraints. You will
need to maintain market-neutrality when an asset suddenly becomes illiquid, handle
non-synchronous data streams without blocking your math engine, and explicitly model
the physical drag of market impact and borrow fees.

## Goals

1) Build an N-Dimensional Alpha Engine — Johansen Test across 6–8 assets, construct hedge ratios (β) and speed of adjustment (α).

2) Implement a Distributed Data Pipeline — Redis/ZeroMQ Pub/Sub architecture where microservices push order book states without blocking the math engine.

3) Develop a Dynamic Risk & Hedging Engine — if an asset faces a trading halt or becomes hard-to-borrow, recalculate optimal weights for remaining N-1 assets via convex optimization

4) Build a microstructure aware backtester - maker/taker fees, annualised short borrow costs and square-root market impact based on ADV
tructure-Aware Backtester — maker/taker fees, annualized short borrow market impact based on ADV.

5) Integrate Cointegration Breakdown Protocol — rolling Johansen validation; trigger liquidation if rank r drops.


## Deliverables from this project

1) Modular codebase — separate modules for VECM math, message broker logic, and backtesting engine.

2) System Architecture Diagram showing data flow from APIs → Redis/ZeroMQ → dynarisk engine → portfolio allocator.

3) Performance Tear Sheet — Sharpe, max drawdown, and capacity analysis (at what AUM does market impact destroy alpha).

4) GitHub README documenting econometric decisions, distributed architecture rationale, and local backtest setup guide.