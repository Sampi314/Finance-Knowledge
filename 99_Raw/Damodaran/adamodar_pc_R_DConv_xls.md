# Document

**Source:** https://pages.stern.nyu.edu/~adamodar/pc/R&DConv.xls

---

Inputs
------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| R & D Converter |     |     |     |     |     |
| This spreadsheet converts R&D expenses from operating to capital expenses. It makes the appropriate adjustments to operating income, net |     |     |     |     |     |
| income, the book value of assets and the book value of equity. |     |     |     |     |     |
| (It can also be used to convert other intangible assets, such as human capital, into capital invested. |     |     |     |     |     |
|     |     |     |     |     |     |
| Inputs |     |     |     |     |     |
|     | Current year's numbers |     |     |     |     |
| Pre-tax Operating income (EBIT) | 7231 |     |     |     |     |
| Tax rate | 0.134 |     |     |     |     |
| Net Income | 3763 |     |     |     |     |
| Book value of equity | 5022 |     |     |     |     |
| Book value of debt | 64020 |     |     |     |     |
| Cash | 9708 |     |     |     |     |
| Capital expenditures | 998 |     |     |     |     |
| Depreciation & Amortization | 863 |     |     |     |     |
|     |     |     |     |     |     |
| Over how many years do you want to amortize R&D expenses |     |     |     |     | 10  |
| Enter the current year's R&D expense = |     |     |     |     | 4755 |
| Enter R& D expenses for past years: the number of years that you will need to enter will be determined by the amortization period |     |     |     |     |     |
| Do not input numbers in the first column (Year). It will get automatically updated based on the input above. |     |     |     |     |     |
| Year | R& D Expenses |     |     |     |     |
| \-1 | 4434 |     |     |     |     |
| \-2 | 4819 |     |     |     |     |
| \-3 | 4207 |     |     |     |     |
| \-4 | 4116 |     |     |     |     |
| \-5 | 3737 |     |     |     |     |
| \-6 | 3562 |     |     |     |     |
| \-7 | 3840 |     |     |     |     |
| \-8 | 4006 |     |     |     |     |
| \-9 | 4248 |     |     |     |     |
| \-10 | 4083 |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |
| 0   |     |     |     |     |     |

R&D capitalizer
---------------

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| Output |     |     |     |     |
| Year | R&D Expense | Unamortized portion |     | Amortization this year |
| Current | 4755 | 1   | 4755 | 0   |
| \-1 | 4434 | 0.9 | 3990.6 | 443.4 |
| \-2 | 4819 | 0.8 | 3855.2000000000003 | 481.9 |
| \-3 | 4207 | 0.7 | 2944.8999999999996 | 420.7 |
| \-4 | 4116 | 0.6 | 2469.6 | 411.6 |
| \-5 | 3737 | 0.5 | 1868.5 | 373.7 |
| \-6 | 3562 | 0.4 | 1424.8000000000002 | 356.2 |
| \-7 | 3840 | 0.3 | 1152 | 384 |
| \-8 | 4006 | 0.2 | 801.2 | 400.6 |
| \-9 | 4248 | 0.1 | 424.8 | 424.8 |
| \-10 | 4083 | 0   | 0   | 408.3 |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| 0   | 0   | 0   | 0   | 0   |
| Value of Research Asset = |     |     | 23686.6 | 4105.2 |
|     |     |     |     |     |
| Expenditure on asset in current year = |     |     | 4755 |     |
| Amortization of asset for current year = |     |     | 4105.2 |     |
|     |     |     |     |     |
|     | Without capitalizing | With capitalizing |     |     |
| Operating income | 7231 | 7880.8 |     |     |
| Operating income after taxes | 6262.046 | 6911.8460000000005 |     |     |
| Net Income | 3763 | 4412.8 |     |     |
| Book value of equity | 5022 | 28708.6 |     |     |
| Invested Capital | 59334 | 83020.6 |     |     |
| Return on equity | 0.7493030665073676 | 0.15371003810704809 |     |     |
| Return on capital | 0.12186941719755957 | 0.09492583768365923 |     |     |
| Capital expenditures | 998 | 5753 |     |     |
| Depreciation & Amortization | 863 | 4968.2 |     |     |
| Net Capital expenditures | 135 | 784.8000000000002 |     |     |

Amortizable Lives Look-up Table
-------------------------------

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Industry Name | Amortization Period |     |     |     |     |
| Advertising | 2   |     |     |     |     |
| Aerospace/Defense | 10  |     | Non-technological Service |     | 2 years |
| Air Transport | 10  |     | Retail, Tech Service |     | 3 years |
| Aluminum | 5   |     | Light Manufacturing |     | 5 years |
| Apparel | 3   |     | Heavy Manufacturing |     | 10 years |
| Auto & Truck | 10  |     | Research, with Patenting |     | 10 years |
| Auto Parts (OEM) | 5   |     | Long Gestation Period |     | 10 years |
| Auto Parts (Replacement) | 5   |     |     |     |     |
| Bank | 2   |     |     |     |     |
| Bank (Canadian) | 2   |     |     |     |     |
| Bank (Foreign) | 2   |     |     |     |     |
| Bank (Midwest) | 2   |     |     |     |     |
| Beverage (Alcoholic) | 3   |     |     |     |     |
| Beverage (Soft Drink) | 3   |     |     |     |     |
| Building Materials | 5   |     |     |     |     |
| Cable TV | 10  |     |     |     |     |
| Canadian Energy | 10  |     |     |     |     |
| Cement & Aggregates | 10  |     |     |     |     |
| Chemical (Basic) | 10  |     |     |     |     |
| Chemical (Diversified) | 10  |     |     |     |     |
| Chemical (Specialty) | 10  |     |     |     |     |
| Coal/Alternate Energy | 5   |     |     |     |     |
| Computer & Peripherals | 5   |     |     |     |     |
| Computer Software & Svcs | 3   |     |     |     |     |
| Copper | 5   |     |     |     |     |
| Diversified Co. | 5   |     |     |     |     |
| Drug | 10  |     |     |     |     |
| Drugstore | 3   |     |     |     |     |
| Educational Services | 3   |     |     |     |     |
| Electric Util. (Central) | 10  |     |     |     |     |
| Electric Utility (East) | 10  |     |     |     |     |
| Electric Utility (West) | 10  |     |     |     |     |
| Electrical Equipment | 10  |     |     |     |     |
| Electronics | 5   |     |     |     |     |
| Entertainment | 3   |     |     |     |     |
| Environmental | 5   |     |     |     |     |
| Financial Services | 2   |     |     |     |     |
| Food Processing | 3   |     |     |     |     |
| Food Wholesalers | 3   |     |     |     |     |
| Foreign Electron/Entertn | 5   |     |     |     |     |
| Foreign Telecom. | 10  |     |     |     |     |
| Furn./Home Furnishings | 3   |     |     |     |     |
| Gold/Silver Mining | 5   |     |     |     |     |
| Grocery | 2   |     |     |     |     |
| Healthcare Info Systems | 3   |     |     |     |     |
| Home Appliance | 5   |     |     |     |     |
| Homebuilding | 5   |     |     |     |     |
| Hotel/Gaming | 3   |     |     |     |     |
| Household Products | 3   |     |     |     |     |
| Industrial Services | 3   |     |     |     |     |
| Insurance (Diversified) | 3   |     |     |     |     |
| Insurance (Life) | 3   |     |     |     |     |
| Insurance (Prop/Casualty) | 3   |     |     |     |     |
| Internet | 3   |     |     |     |     |
| Investment Co. (Domestic) | 3   |     |     |     |     |
| Investment Co. (Foreign) | 3   |     |     |     |     |
| Investment Co. (Income) | 3   |     |     |     |     |
| Machinery | 10  |     |     |     |     |
| Manuf. Housing/Rec Veh | 5   |     |     |     |     |
| Maritime | 10  |     |     |     |     |
| Medical Services | 3   |     |     |     |     |
| Medical Supplies | 5   |     |     |     |     |
| Metal Fabricating | 10  |     |     |     |     |
| Metals & Mining (Div.) | 5   |     |     |     |     |
| Natural Gas (Distrib.) | 10  |     |     |     |     |
| Natural Gas (Diversified) | 10  |     |     |     |     |
| Newspaper | 3   |     |     |     |     |
| Office Equip & Supplies | 5   |     |     |     |     |
| Oilfield Services/Equip. | 5   |     |     |     |     |
| Packaging & Container | 5   |     |     |     |     |
| Paper & Forest Products | 10  |     |     |     |     |
| Petroleum (Integrated) | 5   |     |     |     |     |
| Petroleum (Producing) | 5   |     |     |     |     |
| Precision Instrument | 5   |     |     |     |     |
| Publishing | 3   |     |     |     |     |
| R.E.I.T. | 3   |     |     |     |     |
| Railroad | 5   |     |     |     |     |
| Recreation | 5   |     |     |     |     |
| Restaurant | 2   |     |     |     |     |
| Retail (Special Lines) | 2   |     |     |     |     |
| Retail Building Supply | 2   |     |     |     |     |
| Retail Store | 2   |     |     |     |     |
| Securities Brokerage | 2   |     |     |     |     |
| Semiconductor | 5   |     |     |     |     |
| Semiconductor Cap Equip | 5   |     |     |     |     |
| Shoe | 3   |     |     |     |     |
| Steel (General) | 5   |     |     |     |     |
| Steel (Integrated) | 5   |     |     |     |     |
| Telecom. Equipment | 10  |     |     |     |     |
| Telecom. Services | 5   |     |     |     |     |
| Textile | 5   |     |     |     |     |
| Thrift | 2   |     |     |     |     |
| Tire & Rubber | 5   |     |     |     |     |
| Tobacco | 5   |     |     |     |     |
| Toiletries/Cosmetics | 3   |     |     |     |     |
| Trucking/Transp. Leasing | 5   |     |     |     |     |
| Utility (Foreign) | 10  |     |     |     |     |
| Water Utility | 10  |     |     |     |     |