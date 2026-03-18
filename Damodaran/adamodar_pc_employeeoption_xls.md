# Document

**Source:** https://pages.stern.nyu.edu/~adamodar/pc/employeeoption.xls

---

Warrant Valuation
-----------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Valuing Management Options or Warrants when there is dilution |     |     |     |     |     |
| This program is designed to value options, the exercise of which can create more shares and thus affect the stock price. This is the case |     |     |     |     |     |
| with warrants and management options. It is also the case with convertible bonds. As a general rule, using an unadjusted |     |     |     |     |     |
| option pricing model to value these options will overstate their value. |     |     |     |     |     |
| Note: Before you run this program, check under preferences (under tools), and calculations, and ensure that there is a check against the iteration |     |     |     |     |     |
| box. You will get a circular reasoning warning, but this program needs circular reasoning to compute the option value. |     |     |     |     |     |
|     |     |     |     |     |     |
| Enter the current stock price = | 20.83 |     |     |     |     |
| Enter the strike price on the option = | 22.68 |     |     |     |     |
| Enter the expiration of the option = | 2.53 |     |     |     |     |
| Enter the standard deviation in stock prices = | 0.272 | (annualized) |     |     |     |
| Enter the annualized dividend yield on stock = | 0.015 |     |     |     |     |
| Enter the treasury bond rate = | 0.002 |     |     |     |     |
| Enter the number of warrants (options) outstanding = | 520 |     |     |     |     |
| Enter the number of shares outstanding = | 5330 |     |     |     |     |
|     |     |     |     |     |     |
| Do you want to adjust the stated maturity for the fact that employee options are illiquid and get exercised early? |     |     |     |     | No  |
| If yes, enter the maturity you would like to use in the option pricing model = |     |     |     |     | 1.5 |
| Do you want to tax adjust the value of the options? |     |     |     |     | Yes |
| If yes, enter the tax rate to use for tax adjusting the value of the options |     |     |     |     | 0.26 |
| The option value below is not adjusted for non-vesting. Do you want to adjust for vesting? |     |     |     |     | No  |
| If yes, enter the likelihood that these options will be vested |     |     |     |     | 0.9 |
|     |     |     |     |     |     |
| VALUING WARRANTS WHEN THERE IS DILUTION |     |     |     |     |     |
| Stock Price= | 20.83 | \# Warrants issued= |     | 520 |     |
| Strike Price= | 22.68 | \# Shares outstanding= |     | 5330 |     |
| Adjusted S = | 19.13946262651833 | T.Bond rate= |     | 0.002 |     |
| Adjusted K= | 22.68 | Variance= |     | 0.07398400000000001 |     |
| Expiration (in years) = | 2.53 | Annualized dividend yield= |     | 0.015 |     |
|     |     | Div. Adj. interest rate= |     | \-0.013 |     |
|     |     |     |     |     |     |
| d1 = | \-0.25201271927320684 |     |     |     |     |
| N (d1) = | 0.40051561623942006 |     |     |     |     |
|     |     |     |     |     |     |
| d2 = | \-0.6846552044731696 |     |     |     |     |
| N (d2) = | 0.24678076127762832 |     |     |     |     |
|     |     |     |     |     |     |
| Value per option = | 1.8114545483312297 |     |     |     |     |
| Value of all options (pre-tax) | 941.9563651322394 |     |     |     |     |
| Value of all options (pre-tax & adjusted for vesting) | 941.9563651322394 |     |     |     |     |
| Value of all options (after-tax) | 697.0477101978571 |     |     |     |     |