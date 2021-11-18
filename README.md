# Portfolio-Performance-Indicator

This Portfolio Performance Indicator script calculates the following performance indicators of a certain fund or asset and compares it with selected benchmark:

  1. Portfolio Sharpe Ratio
  2. Benchmark Sharpe Ratio
  3. Jenson Index
  4. Treynor Index
  5. Sortino Ratio
  6. Modigliani-Modigliani Ratio
  7. Information Ratio

# Portfolio Sharpe Ratio
Sharpe ratio of a portfolio measures the performance of the portfolio compared to a risk-free asset, after adjusting for its risk. Sharpe ratio is one of the most widely used methods for calculating risk-adjusted return. 

# Benchmark Sharpe Ratio
Sharpe ratio of a benchmark measures the performance of the benchmark compared to a risk-free asset, after adjusting for its risk.

# Jenson Index
Jenson index is a risk-adjusted performance measure that represents the average return on a portfolio or investment. Jenson's measure is commonly referred to as alpha in finance that determines the abnormal return of a portfolio or investment over the theoretical expected return.

# Treynor Index
Treynor Index measures the risk-adjusted performance of an investment portfolio by analyzing a portfolio's excess return per unit of risk. Beta (measure of overall market risk or systematic risk) is used as a measure of market risk for Treynor Index.

# Sortino Ratio
Sortino ratio measures the risk-adjusted return of an investment asset, portfolio, or strategy. Similar to the Sharpe Ratio, but instead of dividing the excess return by the standard deviation of the returns, the division of Sortino ratio is made by the semi-deviation of the returns, which measures only the downside risk and not the full variability of the returns.

# Modigliani-Modigliani Ratio
Modigliani-Modigliani Ratio is used to derive the risk-adjusted return of an investment in comparison to a benchmark. This ratio is the expected return that the portfolio would have if it was leveraged to have the same standard deviation as its benchmark.

# Information Ratio
Information Ratio compares the active return of an investment compared to a benchmark index relative to the volatility of the active return. This ratio is defined as the active return divided by the tracking error. Information ratio is used to choose between funds following the sam benchmark.

# Implementing the Python Scripts to Calculate the Performance Indicators (Example)
Example 1: Comparing Fidelity® ZERO Large Cap Index Fund with benchmark S&P 500

Input:
```ruby
print("Fidelity® ZERO Large Cap Index Fund VS S&P 500")
F = fund("FNILX", "SPY")
F.getPriceData("2018-09-30", "2020-10-31")
# Let's assume the risk-free rate is 1% (0.01)
rf = 0.01
print(f"Risk free rate is {rf}")
print(f"Portfolio's Sharpe Ratio: {F.portSharpe(rf)}")
print(f"Benchmark's Sharpe Ratio: {F.benchSharpe(rf)}")
print(f"Jenson Index: {F.jensonIndex(rf)}")
print(f"Treynor Index: {F.treynorIndex(rf)}")
print(f"Sortino Ratio: {F.sortinoRatio(rf)}")
print(f"Modigliani-Modigliani Ratio: {F.ModiglianiModigliani(rf)}")
print(f"Information Ratio: {F.informationRatio(rf)}")
```

Output:
```ruby
Fidelity® ZERO Large Cap Index Fund VS S&P 500
Risk free rate is 0.01
Portfolio's Sharpe Ratio: FNILX    0.369035
dtype: float64
Benchmark's Sharpe Ratio: SPY    0.299871
dtype: float64
Jenson Index: 0.018623353686259475
Treynor Index: 0.0957152669269726
Sortino Ratio: 0.3398858245307759
Modigliani-Modigliani Ratio: FNILX    0.105383
dtype: float64
Information Ratio: 0.8916507816489615
```

Example 2: Comparing Bitcoin with benchmark NASDAQ

Input:
```ruby
print("Bitcoin VS NASDAQ")
F = fund("BTC-USD", "^IXIC")
F.getPriceData("2018-09-30", "2020-10-31")
# Let's assume the risk-free rate is 1% (0.01)
rf = 0.01
print(f"Risk free rate is {rf}")
print(f"Portfolio's Sharpe Ratio: {F.portSharpe(rf)}")
print(f"Benchmark's Sharpe Ratio: {F.benchSharpe(rf)}")
print(f"Jenson Index: {F.jensonIndex(rf)}")
print(f"Treynor Index: {F.treynorIndex(rf)}")
print(f"Sortino Ratio: {F.sortinoRatio(rf)}")
print(f"Modigliani-Modigliani Ratio: {F.ModiglianiModigliani(rf)}")
print(f"Information Ratio: {F.informationRatio(rf)}")
```

Output:
```ruby
Bitcoin VS NASDAQ
Risk free rate is 0.01
Portfolio's Sharpe Ratio: BTC-USD    0.697782
dtype: float64
Benchmark's Sharpe Ratio: ^IXIC    0.621606
dtype: float64
Jenson Index: 0.2988949834229446
Treynor Index: 0.6515367043373947
Sortino Ratio: 0.6979993126647258
Modigliani-Modigliani Ratio: BTC-USD    0.208742
dtype: float64
Information Ratio: 0.37699064243468977
```
