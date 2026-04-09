# Document

**Source:** https://pages.stern.nyu.edu/~adamodar/pc/apv.xls

---

READ ME FIRST
-------------

|     |     |
| --- | --- |
| PRELIMINARY STUFF AND INPUTS |     |
| Objective | This spreadsheet allows you to compute the optimal capital structure for a non-financial |
|     | service firm. If you have a financial service firm use capstrfin.xls |
| Before you start | Open preferences in excel, go into calculation options and put a check in the iteration box. |
|     | If it is already checked, leave it as is. |
| Inputs | The inputs are primarily in the input sheet. If your company has operating leases, |
|     | use the operating lease worksheet to enter your lease or rental commitments. |
| Units | Enter all numbers in the same units (000s, millions or even billions) |
| Income inputs | The key income inputs are EBITDA, depreciation and amortization and interest expenses. |
|     | Enter the most updated numbers you have for each (even if they are 12-month trailing |
|     | numbers). If the most recent period for which you have data has an operating income that |
|     | is abnormal, either because of extraordinary losses/gains or some other occurrence, use |
|     | an average operating income over the last few years. |
|     | From the statement of cash flows, also enter the capital spending from the recent period. |
|     | P.S: If you have negative operating income and you expect to continue having negative |
|     | operating income, your optimal debt ratio will be zero. |
| Balance Sheet | Enter the book value of all interest-bearing debt. If you have a market value enter that |
|     | number. Alternatively, input the average maturity of the debt and I will estimate the |
|     | market value of debt. |
| Market Data | Enter the current stock price, the current long-term government bond rate, the risk |
|     | premium you would like to use to estimate your cost of equity and the current rating for |
|     | your firm. If you do not have a rating, there is an option for you at the very bottom of |
|     | the spreadsheet to compute a synthetic rating. |
| Tax Rate | Enter a marginal tax rate, if you can estimate it. Otherwise, use the effective tax rate. |
| Default Spreads | This spreadsheet has interest coverage ratios, ratings and default spreads built into it in |
|     | the worksheet. This spreadsheet treats the imputed interest expense on operating leases as part of the |
|     | interest expense when computing the interest coverage ratio. You can choose between ratings for large firms |
|     | (firms with market capitalizations that exceed $ 5 billion is a simple cut off but you can deviate from it) |
|     | a more conservatve for small or risky firms. If you want, you can change the interest |
|     | coverage ratios and ratings in these tables. |
| READING THE OUTPUT |     |
| Summary | The summary provides a picture of your firm's current cost of capital and debt ratio, and |
|     | compares it to your firm's value at every debt raito, incorporating the tax benefits from debt & the expected |
|     | bankruptcy costs at each level of debt. |
| Details | The details of the calculation at each debt ratio are below the summary. |
|     |     |
| References |     |
| Corporate Finance: Theory and Practice, Chapter 18 |     |
| Applied Corporate Finance: Chapter 8 |     |

FAQs
----

|     |     |
| --- | --- |
| Question | Answer |
| Q1: What do I do excel says there are circular references? | Go into preferences, choose calculation options and make sure the iteration box has a check in it. |
| Q2: My spreadsheet has gone crazy. I get errors all over. | I am sorry to say this, but you probably just made an input error. While you might have |
| What did I do wrong? | fixed it, the iterations in the spreadsheet make it very sensitive and the errors will not |
|     | go away. The only fix (Sorry, sorry…) is to copy the inputs into a fresh version of the spreadsheet. |
| Q3: I am entering the inputs for my company but the | You probably forgot to check the iteration box (see Q1) |
| optimal numbers do not seem to change from the |     |
| originals |     |
| Q4: I am getting an optimal debt ratio of 0%. This can't | Sure. If your operating income is either negative or very low, relative to your firm value, |
| be right. Can it? | you can end up at an optimal debt ratio of 0%. For instance, if you have EBIT of 100 on a |
|     | firm value of 10000, a 10% debt ratio would probably push you into a C rating and give |
|     | you a very high cost of capital. |

Inputs
------

|     |     |     |
| --- | --- | --- |
| Inputs |     |     |
| Please enter the name of the company you are analyzing: | Hormel |     |
| Date of analysis | 39924 |     |
| Financial Information |     |     |
| Earnings before interest, taxes and depreciation (EBITDA) | 635 |     |
| Depreciation and Amortization: | 126 |     |
| Capital Spending: | 126 |     |
| Interest expense on debt: | 28  |     |
| Tax rate on ordinary income: | 0.4 |     |
| Cost of Bankrtupcy as a percent of market value of firm = | 0.25 |     |
| Current Rating on debt (if available): | Aaa/AAA |     |
| Interest rate based upon rating: | 0.0275 |     |
| Market Information |     |     |
| Number of shares outstanding: | 134.526 |     |
| Market price per share: | 31.08 |     |
| Beta of the stock: | 0.83 |     |
| Book value of debt: | 450 |     |
| Can you estimate the market value of the outstanding debt? | No  |     |
| If so, enter the market value of debt: |     |     |
| Do you want me to try and estimate market value of debt? | Yes |     |
| If yes, enter the average maturity of outstanding debt? | 0   |     |
| Do you have any operating leases? | Yes |     |
| General Market Data |     |     |
| Current long-term (LT) government bond rate: | 0.0235 | (in percent) |
| Risk premium (for use in the CAPM) | 0.06 | (in percent) |
| Country default spread (for cost of debt) | 0   |     |
|     |     |     |
| General Data |     |     |
| Which spread/ratio table would you like to use for your anlaysis? | 2   |     |
| Do you want to assume that existing debt is refinanced at the 'new' rate? | Yes | (Yes or No) |
| Do you want the firm's current rating to be adjusted to the synthetic rating? | Yes | (Yes or No) |

Operating Lease Information
---------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Operating Lease Converter |     |     |     |     |     |
| Operating lease expenses are really financial expenses, and should be treated as such. Accounting standards allow them to |     |     |     |     |     |
| be treated as operating expenses. This program will convert commitments to make operating leases into debt and |     |     |     |     |     |
| adjust the operating income accordingly, by adding back the imputed interest expense on this debt. |     |     |     |     |     |
|     |     |     |     |     |     |
| Inputs |     |     |     |     |     |
| Operating lease expense in current year = |     |     |     | 21.9 |     |
| Operating Lease Commitments (From footnote to financials) |     |     |     |     |     |
| Year | Commitment | ! Year 1 is next year, …. |     |     |     |
| 1   | 10  |     |     |     |     |
| 2   | 8.07 |     |     |     |     |
| 3   | 6.76 |     |     |     |     |
| 4   | 5.21 |     |     |     |     |
| 5   | 4.51 |     |     |     |     |
| 6 and beyond | 11.94 |     |     |     |     |
|     |     |     |     |     |     |
| Pre-tax Cost of Debt = |     | 0.028 | ! If you do not have a cost of debt, use the attached ratings estimator |     |     |
|     |     |     |     |     |     |
| From the current financial statements, enter the following |     |     |     |     |     |
| Reported Operating Income (EBIT) = |     |     | 509 | ! This is the EBIT reported in the current income statement |     |
| Reported Interest Expenses = |     |     | 28  |     |     |
| Output |     |     |     |     |     |
| Number of years embedded in yr 6 estimate = |     |     | 1   | ! I use the average lease expense over the first five years |     |
|     |     |     |     | to estimate the number of years of expenses in yr 6 |     |
| Converting Operating Leases into debt |     |     |     |     |     |
| Year | Commitment | Present Value |     |     |     |
| 1   | 10  | 9.727626459143968 |     |     |     |
| 2   | 8.07 | 7.636376023861073 |     |     |     |
| 3   | 6.76 | 6.222535055774238 |     |     |     |
| 4   | 5.21 | 4.665146265596404 |     |     |     |
| 5   | 4.51 | 3.928357180862862 |     |     |     |
| 6 and beyond | 11.94 | 10.116857640069753 | ! Commitment beyond year 6 converted into an annuity for ten years |     |     |
| Debt Value of leases = |     | 42.2968986253083 |     |     |     |
|     |     |     |     |     |     |
| Restated Financials |     |     |     |     |     |
| Operating Income with Operating leases reclassified as debt = |     |     |     |     | 530.9 |
| Interest expenses with Operating leases classified as debt = |     |     |     |     | 29.184313161508634 |

Default Spreads and Ratios
--------------------------

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| Inputs for synthetic rating estimation |     |     |     |     |     |     |
| Enter the type of firm = |     | 2   | (Enter 1 if large manufacturing firm, 2 if smaller or riskier firm, 3 if financial service firm) |     |     |     |
| Enter current Earnings before interest and taxes (EBIT) = |     |     |     |     | 530.9 | (Add back only long term interest expense for financial firms) |
| Enter current interest expenses = |     |     |     |     | 29.184313161508634 | (Use only long term interest expense for financial firms) |
| Enter current long term government bond rate = |     |     |     |     | 0.0235 |     |
| Output |     |     |     |     |     |     |
| Interest coverage ratio = |     |     | 18.191279577557687 |     |     |     |
| Estimated Bond Rating = |     |     | Aaa/AAA |     |     |     |
| Estimated Default Spread = |     |     | 0.0045 |     |     |     |
| Estimated Cost of Debt = |     |     | 0.028 |     |     |     |
|     |     |     |     |     |     |     |
| For large or stable firms |     |     |     |     |     |     |
| If interest coverage ratio is |     |     |     |     |     |     |
| \>  | ≤ to | Rating is | Spread is | Bankruptcy Probability |     |     |
| \-100000 | 0.199999 | D2/D | 0.19 | 1   |     |     |
| 0.2 | 0.649999 | C2/C | 0.155 | 0.85 |     |     |
| 0.65 | 0.799999 | Ca2/CC | 0.101 | 0.7 |     |     |
| 0.8 | 1.249999 | Caa/CCC | 0.0728 | 0.5901 |     |     |
| 1.25 | 1.499999 | B3/B- | 0.0442 | 0.45 |     |     |
| 1.5 | 1.749999 | Ba1/BB+ | 0.03 | 0.1 |     |     |
| 1.75 | 1.999999 | Ba2/BB | 0.0261 | 0.1663 |     |     |
| 2   | 2.2499999 | B1/B+ | 0.0183 | 0.25 |     |     |
| 2.25 | 2.49999 | B2/B | 0.0155 | 0.368 |     |     |
| 2.5 | 2.999999 | Baa2/BBB | 0.012 | 0.0754 |     |     |
| 3   | 4.249999 | A3/A- | 0.0095 | 0.025 |     |     |
| 4.25 | 5.499999 | A2/A | 0.0085 | 0.0066 |     |     |
| 5.5 | 6.499999 | A1/A+ | 0.0077 | 0.006 |     |     |
| 6.5 | 8.499999 | Aa2/AA | 0.006 | 0.0051 |     |     |
| 8.5 | 100000 | Aaa/AAA | 0.0045 | 0.0007 |     |     |
|     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
| For smaller and riskier firms |     |     |     |     |     |     |
| If interest coverage ratio is |     |     |     |     |     |     |
| greater than | ≤ to | Rating is | Spread is | Bankruptcy Probability |     |     |
| \-100000 | 0.499999 | D2/D | 0.19 | 1   |     |     |
| 0.5 | 0.799999 | C2/C | 0.155 | 0.85 |     |     |
| 0.8 | 1.249999 | Ca2/CC | 0.101 | 0.7 |     |     |
| 1.25 | 1.499999 | Caa/CCC | 0.0728 | 0.5901 |     |     |
| 1.5 | 1.999999 | B3/B- | 0.0442 | 0.45 |     |     |
| 2   | 2.499999 | Ba1/BB+ | 0.03 | 0.1 |     |     |
| 2.5 | 2.999999 | Ba2/BB | 0.0261 | 0.1663 |     |     |
| 3   | 3.499999 | B1/B+ | 0.0183 | 0.25 |     |     |
| 3.5 | 3.9999999 | B2/B | 0.0155 | 0.368 |     |     |
| 4   | 4.499999 | Baa2/BBB | 0.012 | 0.0754 |     |     |
| 4.5 | 5.999999 | A3/A- | 0.0095 | 0.025 |     |     |
| 6   | 7.499999 | A2/A | 0.0085 | 0.0066 |     |     |
| 7.5 | 9.499999 | A1/A+ | 0.0077 | 0.006 |     |     |
| 9.5 | 12.499999 | Aa2/AA | 0.006 | 0.0051 |     |     |
| 12.5 | 100000 | Aaa/AAA | 0.0045 | 0.0007 |     |     |

Adjusted Present Value
----------------------

|     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Hormel |     |     |     |     |     |     |     |     |     |     |
| 39924 |     |     |     |     |     |     |     |     |     |     |
| Capital Structure |     |     | Financial Market |     |     | Income Statement |     |     |     |     |
| Current MV of Equity = |     | 4181.06808 | Current Beta for Stock = |     | 0.83 | Current EBITDA = |     | 656.9 |     |     |
| Market Value of interest-bearing debt = |     | 450 | Current Bond Rating = |     | Aaa/AAA | Current Depreciation = |     | 126 |     |     |
| \# of Shares Outstanding = |     | 134.526 | Summary of Inputs |     |     | Current Tax Rate = |     | 0.4 |     |     |
| Debt Value of Operating leases (if any) |     | 42.2968986253083 | Long Term Government Bond Rate = |     | 0.0235 | Current Capital Spending= |     | 126 |     |     |
| Risk Premium = |     | 0.06 | Pre-tax cost of debt = |     | 0.0275 | Current Interest Expense = |     | 29.184313161508634 |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     | Maximum firm value = | 5749.644962986145 |     |     |     |     |     |
|     |     |     |     | Optimal debt ratio = | 0.7 |     |     |     |     |     |
|     |     | Adjusted Present Value Estimates |     |     |     |     |     |     |     |     |
|     |     | Debt Ratio | $ Debt | Unlevered firm value | Tax Benefits from Debt | Expected Bankruptcy Cost | Levered Firm Value |     |     |     |
|     |     | 0   | 0   | 4477.264058046444 | 0   | 0.7835212101581277 | 4476.480536836286 |     |     |     |
|     |     | 0.1 | 467.33649786253085 | 4477.264058046444 | 186.93459914501236 | 0.8162347650085049 | 4663.382422426448 |     |     |     |
|     |     | 0.2 | 934.6729957250617 | 4477.264058046444 | 373.8691982900247 | 0.848948319858882 | 4850.284308016609 |     |     |     |
|     |     | 0.3 | 1402.0094935875925 | 4477.264058046444 | 560.803797435037 | 0.8816618747092592 | 5037.186193606772 |     |     |     |
|     |     | 0.4 | 1869.3459914501234 | 4477.264058046444 | 747.7383965800494 | 7.83750368193974 | 5217.164950944553 |     |     |     |
|     |     | 0.5 | 2336.682489312654 | 4477.264058046444 | 934.6729957250617 | 8.929696138722985 | 5403.007357632783 |     |     |     |
|     |     | 0.6 | 2804.018987175185 | 4477.264058046444 | 1121.607594870074 | 34.992947830728234 | 5563.878705085789 |     |     |     |
|     |     | 0.7 | 3271.3554850377154 | 4477.264058046444 | 1308.5421940150864 | 36.161289075384566 | 5749.644962986145 |     |     |     |
|     |     | 0.8 | 3738.691982900247 | 4477.264058046444 | 1495.4767931600989 | 1045.229648961145 | 4927.511202245398 |     |     |     |
|     |     | 0.9 | 4206.028480762778 | 4477.264058046444 | 1189.6918767507004 | 1204.2281361443931 | 4462.7277986527515 |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
| We use the following default spreads in our analysis. Change them in the input sheet if necessary: |     |     |     |     |     |     | Ratings comparison at current debt ratio |     |     |     |
|     |     | Rating | Coverage gt | and lt | Spread | Default Probability | Current Interest coverage ratio = |     |     | 18.191279577557687 |
|     |     | AAA | 12.5 | 100000 | 0.0045 | 0.0007 | Rating based upon coverage = |     |     | Aaa/AAA |
|     |     | AA  | 9.5 | 12.499999 | 0.006 | 0.0051 | Interest rate based upon coverage = |     |     | 0.028 |
|     |     | A+  | 7.5 | 9.499999 | 0.0077 | 0.006 | Current rating for company = |     |     | Aaa/AAA |
|     |     | A   | 6   | 7.499999 | 0.0085 | 0.0066 | Current interest rate on debt = |     |     | 0.0275 |
|     |     | A-  | 4.5 | 5.999999 | 0.0095 | 0.025 | Current Bankruptcy Probability = |     |     | 0.0007 |
|     |     | BBB | 4   | 4.499999 | 0.012 | 0.0754 |     |     |     |     |
|     |     | BB  | 3   | 3.499999 | 0.0183 | 0.25 |     |     |     |     |
|     |     | B+  | 2.5 | 2.999999 | 0.0261 | 0.1663 |     |     |     |     |
|     |     | B   | 2   | 2.499999 | 0.03 | 0.1 |     |     |     |     |
|     |     | B-  | 1.5 | 1.999999 | 0.0442 | 0.45 |     |     |     |     |
|     |     | CCC | 1.25 | 1.499999 | 0.0728 | 0.5901 |     |     |     |     |
|     |     | CC  | 0.8 | 1.249999 | 0.101 | 0.7 |     |     |     |     |
|     |     | C   | 0.5 | 0.799999 | 0.155 | 0.85 |     |     |     |     |
|     |     | D   | \-100000 | 0.499999 | 0.19 | 1   |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
| Current beta= | 0.83 |     | Current Equity= |     | 4181.06808 |     | Current Depreciation= |     | 126 |     |
| Current Debt= | 492.2968986253083 |     | Current EBITDA= |     | 656.9 |     | Current Interest rate (Company)= |     | 0.0275 |     |
| Tax rate= | 0.4 |     | Current Rating= |     | Aaa/AAA |     | Current T.Bond rate= |     | 0.0235 |     |
|     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     | WORKSHEET FOR ESTIMATING RATINGS/INTEREST RATES |     |     |     |     |     |
| D/(D+E) | 0   | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| D/E | 0   | 0.11111111111111112 | 0.25 | 0.4285714285714286 | 0.6666666666666667 | 1   | 1.4999999999999998 | 2.333333333333333 | 4.000000000000001 | 9.000000000000002 |
| $ Debt | 0   | 467.33649786253085 | 934.6729957250617 | 1402.0094935875925 | 1869.3459914501234 | 2336.682489312654 | 2804.018987175185 | 3271.3554850377154 | 3738.691982900247 | 4206.028480762778 |
| Beta | 0.7752324805187593 | 0.8269146458866765 | 0.891517352596573 | 0.9745779755092974 | 1.085325472726263 | 1.240371968830015 | 1.4729417129856426 | 1.8605579532450218 | 2.635790433763782 | 5.778826503889161 |
| Cost of Equity | 0.07001394883112555 | 0.07311487875320058 | 0.07699104115579439 | 0.08197467853055784 | 0.08861952836357578 | 0.0979223181298009 | 0.11187650277913855 | 0.1351334771947013 | 0.1816474260258269 | 0.37022959023334967 |
|     |     |     |     |     |     |     |     |     |     |     |
| EBITDA | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 | 656.9 |
| Depreciation | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 |
| EBIT | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 | 530.9 |
| Interest | 0   | 13.085421940150864 | 26.170843880301728 | 39.25626582045259 | 58.32359493324385 | 74.77383965800493 | 92.53262657678111 | 107.95473100624461 | 465.4671518710807 | 750.7760838161557 |
| Taxable Income | 530.9 | 517.8145780598492 | 504.72915611969825 | 491.6437341795474 | 472.57640506675614 | 456.12616034199505 | 438.36737342321885 | 422.94526899375535 | 65.43284812891926 | \-219.87608381615576 |
| Tax | 212.36 | 207.12583122393968 | 201.8916624478793 | 196.65749367181897 | 189.03056202670246 | 182.45046413679802 | 175.34694936928756 | 169.17810759750216 | 26.173139251567704 | \-87.9504335264623 |
| Net Income | 318.53999999999996 | 310.68874683590946 | 302.83749367181895 | 294.98624050772844 | 283.5458430400537 | 273.675696205197 | 263.02042405393127 | 253.7671613962532 | 39.25970887735156 | \-131.92565028969346 |
| (+)Deprec'n | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 | 126 |
| Funds from Op. | 444.53999999999996 | 436.68874683590946 | 428.83749367181895 | 420.98624050772844 | 409.5458430400537 | 399.675696205197 | 389.02042405393127 | 379.7671613962532 | 165.25970887735156 | \-5.925650289693465 |
|     |     |     |     |     |     |     |     |     |     |     |
| Pre-tax Int. cov | ∞   | 40.57186710739563 | 20.285933553697816 | 13.523955702465212 | 9.102662492043892 | 7.1000767437942365 | 5.737435752560998 | 4.917802073623713 | 1.1405745773163432 | 0.7071349386909915 |
| Funds/Debt | ∞   | 0.9344203776790475 | 0.4588101888395238 | 0.3002734592263492 | 0.2190850944197619 | 0.17104407553580953 | 0.13873672961317457 | 0.11608862538272109 | 0.04420254720988094 | \-0.0014088469245502654 |
| Likely Rating | AAA | Aaa/AAA | Aaa/AAA | Aaa/AAA | A1/A+ | A2/A | A3/A- | A3/A- | Ca2/CC | C2/C |
| Pre-tax cost of debt | 0.028 | 0.028 | 0.028 | 0.028 | 0.0312 | 0.032 | 0.033 | 0.033 | 0.1245 | 0.1785 |
| Probability of Bankruptcy | 0.0007 | 0.0007 | 0.0007 | 0.0007 | 0.006 | 0.0066 | 0.025 | 0.025 | 0.7 | 0.85 |
| Eff. Tax Rate | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.4 | 0.2828539754763966 |
|     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
|     |     |     | Interest cov | Interest cov | RATING | Interest rate | Bankruptcy |     |     |     |
|     |     |     | Low | High |     |     | Probability |     |     |     |
|     |     |     | \-100000 | 0.499999 | D2/D | 0.2135 | 1   |     |     |     |
|     |     |     | 0.5 | 0.799999 | C2/C | 0.1785 | 0.85 |     |     |     |
|     |     |     | 0.8 | 1.249999 | Ca2/CC | 0.1245 | 0.7 |     |     |     |
|     |     |     | 1.25 | 1.499999 | Caa/CCC | 0.0963 | 0.5901 |     |     |     |
|     |     |     | 1.5 | 1.999999 | B3/B- | 0.06770000000000001 | 0.45 |     |     |     |
|     |     |     | 2   | 2.499999 | Ba1/BB+ | 0.0535 | 0.1 |     |     |     |
|     |     |     | 2.5 | 2.999999 | Ba2/BB | 0.049600000000000005 | 0.1663 |     |     |     |
|     |     |     | 3   | 3.499999 | B1/B+ | 0.041800000000000004 | 0.25 |     |     |     |
|     |     |     | 3.5 | 3.9999999 | B2/B | 0.039 | 0.368 |     |     |     |
|     |     |     | 4   | 4.499999 | Baa2/BBB | 0.035500000000000004 | 0.0754 |     |     |     |
|     |     |     | 4.5 | 5.999999 | A3/A- | 0.033 | 0.025 |     |     |     |
|     |     |     | 6   | 7.499999 | A2/A | 0.032 | 0.0066 |     |     |     |
|     |     |     | 7.5 | 9.499999 | A1/A+ | 0.0312 | 0.006 |     |     |     |
|     |     |     | 9.5 | 12.499999 | Aa2/AA | 0.0295 | 0.0051 |     |     |     |
|     |     |     | 12.5 | 100000 | Aaa/AAA | 0.028 | 0.0007 |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
| Adjusted Present Value Approach |     |     |     |     |     |     |     |     |     |     |
| Current Value of the Firm = |     |     | 4673.364978625308 |     |     |     |     |     |     |     |
| \- Tax Benefit on Current Debt = |     |     | 196.91875945012333 |     | Cost of Bankruptcy (% of Value) = |     |     | 0.25 |     |     |
| \+ Expected Current Bankruptcy Cost = |     |     | 0.8178388712594289 |     | Current Probability of Bankrupcy = |     |     | 0.0007 |     |     |
| Unlevered Value of Firm = |     |     | 4477.264058046444 |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
| Debt Ratio | 0   | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 |
| $ Debt | 0   | 467.33649786253085 | 934.6729957250617 | 1402.0094935875925 | 1869.3459914501234 | 2336.682489312654 | 2804.018987175185 | 3271.3554850377154 | 3738.691982900247 | 4206.028480762778 |
| Unlev. Firm Value | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 | 4477.264058046444 |
| Tax Benefits | 0   | 186.93459914501236 | 373.8691982900247 | 560.803797435037 | 747.7383965800494 | 934.6729957250617 | 1121.607594870074 | 1308.5421940150864 | 1495.4767931600989 | 1189.6918767507004 |
| Bond Rating | AAA | Aaa/AAA | Aaa/AAA | Aaa/AAA | A1/A+ | A2/A | A3/A- | A3/A- | Ca2/CC | C2/C |
| Prob. of Default | 0.0007 | 0.0007 | 0.0007 | 0.0007 | 0.006 | 0.0066 | 0.025 | 0.025 | 0.7 | 0.85 |
| Bankruptcy Cost | 0.7835212101581277 | 0.8162347650085049 | 0.848948319858882 | 0.8816618747092592 | 7.83750368193974 | 8.929696138722985 | 34.992947830728234 | 36.161289075384566 | 1045.229648961145 | 1204.2281361443931 |
| Index variable | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   | 0   |
| Levered Firm Value | 4476.480536836286 | 4663.382422426448 | 4850.284308016609 | 5037.186193606772 | 5217.164950944553 | 5403.007357632783 | 5563.878705085789 | 5749.644962986145 | 4927.511202245398 | 4462.7277986527515 |
|     |     |     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |
| Debt Ratio | $ Debt | Tax Rate | Unlevered Firm Value | Tax Benefits | Bond Rating | Probability of Default | Expected Bankruptcy Cost | Value of Levered Firm |     |     |
| 0   | 0   | 0.4 | 4477.264058046444 | 0   | AAA | 0.0007 | 0.7835212101581277 | 4476.480536836286 |     |     |
| 0.1 | 467.33649786253085 | 0.4 | 4477.264058046444 | 186.93459914501236 | Aaa/AAA | 0.0007 | 0.8162347650085049 | 4663.382422426448 |     |     |
| 0.2 | 934.6729957250617 | 0.4 | 4477.264058046444 | 373.8691982900247 | Aaa/AAA | 0.0007 | 0.848948319858882 | 4850.284308016609 |     |     |
| 0.3 | 1402.0094935875925 | 0.4 | 4477.264058046444 | 560.803797435037 | Aaa/AAA | 0.0007 | 0.8816618747092592 | 5037.186193606772 |     |     |
| 0.4 | 1869.3459914501234 | 0.4 | 4477.264058046444 | 747.7383965800494 | A1/A+ | 0.006 | 7.83750368193974 | 5217.164950944553 |     |     |
| 0.5 | 2336.682489312654 | 0.4 | 4477.264058046444 | 934.6729957250617 | A2/A | 0.0066 | 8.929696138722985 | 5403.007357632783 |     |     |
| 0.6 | 2804.018987175185 | 0.4 | 4477.264058046444 | 1121.607594870074 | A3/A- | 0.025 | 34.992947830728234 | 5563.878705085789 |     |     |
| 0.7 | 3271.3554850377154 | 0.4 | 4477.264058046444 | 1308.5421940150864 | A3/A- | 0.025 | 36.161289075384566 | 5749.644962986145 |     |     |
| 0.8 | 3738.691982900247 | 0.4 | 4477.264058046444 | 1495.4767931600989 | Ca2/CC | 0.7 | 1045.229648961145 | 4927.511202245398 |     |     |
| 0.9 | 4206.028480762778 | 0.2828539754763966 | 4477.264058046444 | 1189.6918767507004 | C2/C | 0.85 | 1204.2281361443931 | 4462.7277986527515 |     |     |

Country ERP
-----------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Mature Market ERP + | 0.0433 | Updated January 1, 2025 |     |     |     |
| Changing this number will update all your country equity risk premiums. |     |     |     |     |     |
|     |     |     |     |     |     |
| Country | Moody's rating | Adj. Default Spread | Equity Risk Premium | Country Risk Premium | Corporate Tax Rate |
| Abu Dhabi | Aa2 | 0.0048889784279692525 | 0.04989108781210082 | 0.006591087812100819 | 0.15 |
| Albania | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.15 |
| Algeria | NR  | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.15 |
| Andorra (Principality of) | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.1898 |
| Angola | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.25 |
| Anguilla | NR  | 0.06012263625836532 | 0.12435447404039451 | 0.08105447404039451 | 0.25228018689443577 |
| Antigua & Barbuda | NR  | 0.0601 | 0.1243122477280291 | 0.08101224772802909 | 0.2523 |
| Argentina | Ca  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.35 |
| Armenia | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.18 |
| Aruba | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.25 |
| Australia | Aaa | 0   | 0.0433 | 0   | 0.3 |
| Austria | Aa1 | 0.003957744441689394 | 0.048635642514557806 | 0.005335642514557805 | 0.24 |
| Azerbaijan | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.2 |
| Bahamas | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0   |
| Bahrain | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0   |
| Bangladesh | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.3 |
| Barbados | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.055 |
| Belarus | C   | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.18 |
| Belgium | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.25 |
| Belize | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.2853 |
| Benin | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.3 |
| Bermuda | A2  | 0.00838110587651872 | 0.05459900767788712 | 0.011299007677887121 | 0   |
| Bolivia | Caa3 | 0.09906001529051987 | 0.17684799352613806 | 0.13354799352613805 | 0.25 |
| Bosnia and Herzegovina | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.1 |
| Botswana | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.22 |
| Brazil | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.34 |
| British Virgin Islands | NR  | 0.06012263625836532 | 0.12435447404039451 | 0.08105447404039451 | 0.25228018689443577 |
| Brunei | NR  | 0.005936616662534092 | 0.051303463771836706 | 0.00800346377183671 | 0.34 |
| Bulgaria | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.1 |
| Burkina Faso | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.28 |
| Cambodia | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.2 |
| Cameroon | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.33 |
| Canada | Aaa | 0   | 0.0433 | 0   | 0.265 |
| Cape Verde | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0   |
| Cayman Islands | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0   |
| Channel Islands | NR  | 0.008274105096747005 | 0.05445475432397499 | 0.011154754323974989 | 0.24775219614916172 |
| Chile | A2  | 0.00838110587651872 | 0.05459900767788712 | 0.011299007677887121 | 0.27 |
| China | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0.25 |
| Colombia | Baa2 | 0.01885748822216712 | 0.06872276727524602 | 0.025422767275246023 | 0.35 |
| Congo (Democratic Republic of) | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.3 |
| Congo (Republic of) | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.28 |
| Cook Islands | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.2974 |
| Costa Rica | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.3 |
| Croatia | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.18 |
| Cuba | Ca  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.2853 |
| Curaçao | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.22 |
| Cyprus | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.125 |
| Czech Republic | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.19 |
| Denmark | Aaa | 0   | 0.0433 | 0   | 0.22 |
| Dominican Republic | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.27 |
| Ecuador | Caa3 | 0.09906001529051987 | 0.17684799352613806 | 0.13354799352613805 | 0.25 |
| Egypt | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.225 |
| El Salvador | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.3 |
| Estonia | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0.2 |
| Ethiopia | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.3 |
| Falkland Islands | NR  | 0.03576937686394985 | 0.09152256988201701 | 0.048222569882017015 | 0.3155395256169791 |
| Fiji | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.2 |
| Finland | Aa1 | 0.003957744441689394 | 0.048635642514557806 | 0.005335642514557805 | 0.2 |
| France | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.25 |
| French Guiana | NR  | 0.03576937686394985 | 0.09152256988201701 | 0.048222569882017015 | 0.3155395256169791 |
| Gabon | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.3 |
| Gambia | NR  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.3 |
| Georgia | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.15 |
| Germany | Aaa | 0   | 0.0433 | 0   | 0.3 |
| Ghana | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.25 |
| Gibraltar | NR  | 0.008274105096747005 | 0.05445475432397499 | 0.011154754323974989 | 0.24775219614916172 |
| Greece | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.22 |
| Greenland | NR  | 0.008274105096747005 | 0.05445475432397499 | 0.011154754323974989 | 0.24775219614916172 |
| Guatemala | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.25 |
| Guernsey (States of) | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0   |
| Guinea | NR  | 0.08916565418629635 | 0.1635088872397435 | 0.1202088872397435 | 0   |
| Guinea-Bissau | NR  | 0.06437154930159514 | 0.1300826561926608 | 0.08678265619266079 | 0   |
| Guyana | NR  | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0   |
| Haiti | NR  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0   |
| Honduras | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.25 |
| Hong Kong | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.165 |
| Hungary | Baa2 | 0.01885748822216712 | 0.06872276727524602 | 0.025422767275246023 | 0.09 |
| Iceland | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0.2 |
| India | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.3 |
| Indonesia | Baa2 | 0.01885748822216712 | 0.06872276727524602 | 0.025422767275246023 | 0.22 |
| Iran | NR  | 0.06437154930159514 | 0.1300826561926608 | 0.08678265619266079 | 0.22 |
| Iraq | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.15 |
| Ireland | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.125 |
| Isle of Man | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0   |
| Israel | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.23 |
| Italy | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.24 |
| Ivory Coast | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.25 |
| Jamaica | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.25 |
| Japan | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0.3062 |
| Jersey (States of) | Aa2 | 0.0048889784279692525 | 0.04989108781210082 | 0.006591087812100819 | 0   |
| Jordan | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.2 |
| Kazakhstan | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.2 |
| Kenya | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.3 |
| Korea, D.P.R. | NR  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.25 |
| Kuwait | A1  | 0.006984254897098934 | 0.052715839731572595 | 0.0094158397315726 | 0.15 |
| Kyrgyzstan | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.1 |
| Laos | Caa3 | 0.09906001529051987 | 0.17684799352613806 | 0.13354799352613805 | 0.2686 |
| Latvia | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.2 |
| Lebanon | C   | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.17 |
| Liberia | NR  | 0.08916565418629635 | 0.1635088872397435 | 0.1202088872397435 | 0.17 |
| Libya | NR  | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.17 |
| Liechtenstein | Aaa | 0   | 0.0433 | 0   | 0.125 |
| Lithuania | A2  | 0.00838110587651872 | 0.05459900767788712 | 0.011299007677887121 | 0.15 |
| Luxembourg | Aaa | 0   | 0.0433 | 0   | 0.2494 |
| Macau | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.2686 |
| Macedonia | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.1 |
| Madagascar | NR  | 0.054477188197371657 | 0.11674354990626626 | 0.07344354990626625 | 0.1 |
| Malawi | NR  | 0.08916565418629635 | 0.1635088872397435 | 0.1202088872397435 | 0.1 |
| Malaysia | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.24 |
| Maldives | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.2686 |
| Mali | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.2686 |
| Malta | A2  | 0.00838110587651872 | 0.05459900767788712 | 0.011299007677887121 | 0.35 |
| Martinique | NR  | 0.06012263625836532 | 0.12435447404039451 | 0.08105447404039451 | 0.25228018689443577 |
| Mauritius | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.15 |
| Mexico | Baa2 | 0.01885748822216712 | 0.06872276727524602 | 0.025422767275246023 | 0.3 |
| Moldova | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.12 |
| Monaco | Aaa | 0   | 0.0433 | 0   | 0.24775219614916172 |
| Mongolia | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.25 |
| Montenegro | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.15 |
| Montserrat | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.2853 |
| Morocco | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.32 |
| Mozambique | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.32 |
| Myanmar | NR  | 0.09906001529051986 | 0.17684799352613806 | 0.13354799352613805 | 0.32 |
| Namibia | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.32 |
| Nepal | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.25 |
| Netherlands | Aaa | 0   | 0.0433 | 0   | 0.258 |
| Netherlands Antilles | NR  | 0.06012263625836532 | 0.12435447404039451 | 0.08105447404039451 | 0.25228018689443577 |
| New Zealand | Aaa | 0   | 0.0433 | 0   | 0.28 |
| Nicaragua | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.3 |
| Niger | Caa3 | 0.09906001529051987 | 0.17684799352613806 | 0.13354799352613805 | 0.2686 |
| Nigeria | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.3 |
| Norway | Aaa | 0   | 0.0433 | 0   | 0.22 |
| Oman | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0.15 |
| Pakistan | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.29 |
| Palestinian Authority | NR  | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.17 |
| Panama | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.25 |
| Papua New Guinea | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.3 |
| Paraguay | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.1 |
| Peru | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.295 |
| Philippines | Baa2 | 0.01885748822216712 | 0.06872276727524602 | 0.025422767275246023 | 0.25 |
| Poland | A2  | 0.00838110587651872 | 0.05459900767788712 | 0.011299007677887121 | 0.19 |
| Portugal | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.21 |
| Qatar | Aa2 | 0.0048889784279692525 | 0.04989108781210082 | 0.006591087812100819 | 0.1 |
| Ras Al Khaimah (Emirate of) | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0   |
| Reunion | NR  | 0.010708616059682126 | 0.05773684602731119 | 0.014436846027311188 | 0.2534417911673511 |
| Romania | Baa3 | 0.021767594429291676 | 0.07264603383006794 | 0.029346033830067942 | 0.16 |
| Russia | NR  | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.2 |
| Rwanda | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.3 |
| Saint Lucia | NR  | 0.06012263625836532 | 0.12435447404039451 | 0.08105447404039451 | 0.25228018689443577 |
| Saudi Arabia | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.2 |
| Senegal | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.3 |
| Serbia | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.15 |
| Sharjah | Ba1 | 0.024794104884701216 | 0.07672623104708273 | 0.03342623104708274 | 0   |
| Sierra Leone | NR  | 0.08916565418629635 | 0.1635088872397435 | 0.1202088872397435 | 0   |
| Singapore | Aaa | 0   | 0.0433 | 0   | 0.17 |
| Slovakia | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.21 |
| Slovenia | A3  | 0.011873233325068186 | 0.05930692754367342 | 0.016006927543673423 | 0.19 |
| Solomon Islands | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.3 |
| Somalia | NR  | 0.09906001529051986 | 0.17684799352613806 | 0.13354799352613805 | 0.3 |
| South Africa | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.27 |
| South Korea | Aa2 | 0.0048889784279692525 | 0.04989108781210082 | 0.006591087812100819 | 0.25 |
| Spain | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.25 |
| Sri Lanka | Ca  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.24 |
| St. Maarten | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.2853 |
| St. Vincent & the Grenadines | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.2853 |
| Sudan | NR  | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.2853 |
| Suriname | Caa1 | 0.07426591040581865 | 0.1434217624790553 | 0.10012176247905531 | 0.36 |
| Swaziland | B2  | 0.05447718819737168 | 0.11674354990626629 | 0.07344354990626628 | 0.275 |
| Sweden | Aaa | 0   | 0.0433 | 0   | 0.20600000000000002 |
| Switzerland | Aaa | 0   | 0.0433 | 0   | 0.146 |
| Syria | NR  | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.146 |
| Taiwan | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.2 |
| Tajikistan | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.18 |
| Tanzania | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.3 |
| Thailand | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.2 |
| Togo | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.2686 |
| Trinidad &' Tobago | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.3 |
| Tunisia | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.15 |
| Turkey | B1  | 0.04458282709314818 | 0.10340444361987178 | 0.06010444361987177 | 0.25 |
| Turks & Caicos Islands | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0   |
| Uganda | B3  | 0.06437154930159515 | 0.1300826561926608 | 0.0867826561926608 | 0.3 |
| Ukraine | Ca  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.18 |
| United Arab Emirates | Aa2 | 0.0048889784279692525 | 0.04989108781210082 | 0.006591087812100819 | 0.25 |
| United Kingdom | Aa3 | 0.005936616662534093 | 0.05130346377183671 | 0.008003463771836711 | 0.25 |
| United States | Aaa | 0   | 0.0433 | 0   | 0.25 |
| Uruguay | Baa1 | 0.015830977766757577 | 0.06464257005823122 | 0.02134257005823122 | 0.25 |
| Uzbekistan | Ba3 | 0.035619699975204554 | 0.09132078263102025 | 0.048020782631020255 | 0.15 |
| Venezuela | C   | 0.175 | 0.27922666323069684 | 0.23592666323069683 | 0.34 |
| Vietnam | Ba2 | 0.029799487560955448 | 0.08347424952137643 | 0.04017424952137643 | 0.2 |
| Yemen | NR  | 0.11884873749896685 | 0.2035262060989271 | 0.1602262060989271 | 0.2 |
| Zambia | Caa2 | 0.08916565418629636 | 0.16350888723974355 | 0.12020888723974354 | 0.35 |
| Zimbabwe | NR  | 0.08916565418629635 |     | 0.1202088872397435 | 0.35 |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
|     |     |     |     |     |     |
| Region | ERP | Default Spread | Tax Rate | CRP |     |
| Africa | 0.12636516288511693 | 0.06163973704915901 | 0.274219145008639 | 0.08306516288511694 |     |
| Asia | 0.0587 | 0.010708616059682126 | 0.2534417911673511 | 0.0154 |     |
| Australia & New Zealand | 0.04334293324209606 | 0.00003185924955241504 | 0.29743620926523207 | 0.000042933242096058726 |     |
| Caribbean | 0.12432073131656701 | 0.06012263625836532 | 0.25228018689443577 | 0.08102073131656702 |     |
| Central and South America | 0.09150249497712071 | 0.03576937686394985 | 0.3155395256169791 | 0.0482024949771207 |     |
| Eastern Europe | 0.07727703456653685 | 0.02521316281878702 | 0.1723057803112369 | 0.033977034566536855 |     |
| Middle East | 0.0642857466003489 | 0.015572784754721281 | 0.18937682936327277 | 0.0209857466003489 |     |
| North America | 0.0433 | 0   | 0.25108814145744907 | 0   |     |
| Western Europe | 0.054450110634666364 | 0.008274105096747005 | 0.24775219614916172 | 0.011150110634666366 |     |
| Global | 0.0576 | 0.010377275529176463 | 0.2522103140192217 | 0.0143 |     |

Input choices page
------------------

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rating is |     |     |     |     | Yes/No | IBC | Type of firm |
| Aaa/AAA |     |     |     |     | Yes | High | 1   |
| Aa2/AA |     |     |     |     | No  | Medium | 2   |
| A1/A+ |     |     |     |     |     | Low |     |
| A2/A |     |     |     |     |     |     |     |
| A3/A- |     |     |     |     |     |     |     |
| Baa2/BBB |     |     |     |     |     |     |     |
| Ba1/BB+ |     |     |     |     |     |     |     |
| Ba2/BB |     |     |     |     |     |     |     |
| B1/B+ |     |     |     |     |     |     |     |
| B2/B |     |     |     |     |     |     |     |
| B3/B- |     |     |     |     |     |     |     |
| Caa/CCC |     |     |     |     |     |     |     |
| Ca2/CC |     |     |     |     |     |     |     |
| C2/C |     |     |     |     |     |     |     |
| D2/D |     |     |     |     |     |     |     |