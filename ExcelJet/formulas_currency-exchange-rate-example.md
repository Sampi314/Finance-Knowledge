# Currency exchange rate example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/currency-exchange-rate-example

---

[Skip to main content](https://exceljet.net/formulas/currency-exchange-rate-example#main-content)

[](https://exceljet.net/formulas/currency-exchange-rate-example#)

*   [Previous](https://exceljet.net/formulas/compare-effect-of-compounding-periods)
    
*   [Next](https://exceljet.net/formulas/effective-annual-interest-rate)
    

[Financial](https://exceljet.net/formulas#Financial)

Currency exchange rate example
==============================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

![Excel formula: Currency exchange rate example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/currency%20exchange%20rate%20example.png "Excel formula: Currency exchange rate example")

Summary
-------

To get historical currency exchange rates over time, you can use the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. In the example shown, the formula in cell B4 is:

    =STOCKHISTORY(F5&":"&F6,F7,F8,2)
    

The result is the monthly exchange rate for the USD > EUR currency pair shown in cells F5 and F6. Note that STOCKHISTORY returns an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells. The STOCKHISTORY is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
.

Generic formula
---------------

    =STOCKHISTORY(currency1&":"&currency2,start,end)

Explanation 
------------

In this example, the goal is to get monthly currency exchange rates for a given currency pair (i.e., USD > EUR, USD > GBP, CAD > JPY, etc.). Currency abbreviations are entered in cells F5 and F6, and the start and end dates are entered in cells F7 and F8. If any of these four inputs are changed, the results seen in columns B and C will update dynamically. This can be done with the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
, whose purpose is to retrieve historical information for a financial instrument over time.

> STOCKHISTORY only returns _historical_ information recorded after market close. Keep in mind that to get the latest data, you may need to refresh the worksheet manually (Data › Refresh All). The data provided by STOCKHISTORY comes from [LSEG Data & Analytics](https://support.microsoft.com/en-us/office/about-the-stocks-financial-data-sources-98a03e23-37f6-4776-beea-c5a6c8e787e6)
>  (previously Refinitiv). Microsoft cautions that all figures are provided “as‑is” and may be delayed, so use them for analysis only, not real‑time trading decisions.

### Overview

Although the name suggests otherwise, the STOCKHISTORY function can work with a variety of financial instruments, including bonds, index funds, mutual funds, bonds, and currency pairs. To work with currency exchange rates, STOCKHISTORY requires a currency pair entered as text.

STOCKHISTORY takes up to 11 [arguments](https://exceljet.net/glossary/function-argument)
, most of which are optional. The syntax for the first 4 arguments looks like this:

    =STOCKHISTORY(stock,start_date,[end_date],[interval])
    

_Stock_ is a unique key for the instrument being retrieved, entered as a text value. For currency exchange rates, _stock_ will be a currency pair like "USD:CAD". _Start\_date_ and _end\_date_ are [Excel dates](https://exceljet.net/glossary/excel-date)
 that define the time period being requested. _Interval_ is the time interval – daily, weekly, or monthly. For a more complete description of all arguments and properties, see our [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
 page.

### Basic currency exchange example

To get exchange rates for a given currency pair with STOCKHISTORY, enter the two 3-letter codes separated by a colon (:) as the _stock_ argument. For example, to get the currency exchange rate between the US Dollar ("USD") and the Euro ("EUR") for the months of January 2021 through March 2021, you can use STOCKHISTORY like this:

    =STOCKHISTORY("USD:EUR","1-Jan-2021","1-Mar-2021",2)
    

In this example, the _stock_ argument is the [text value](https://exceljet.net/glossary/text-value)
 "USD:EUR", _start\_date_ is "1-Jan-2021", _end\_date_ is "1-Mar-2021". The _interval_ argument specifies the time period to use between prices. The options are daily (0), weekly (1), or monthly (2). In this case, we want a monthly interval, so we provide 2. The result is an array with three months of rates:

![Currency exchange rate USD to EUR example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/currency%20exchange%20rate%20USD%20to%20EUR%20example.png?itok=dKD20ye8 "Currency exchange rate USD to EUR example")

To reverse the direction of the exchange, just swap the order of the currency pairs:

    =STOCKHISTORY("EUR:USD","1-Jan-2021","1-Mar-2021",2)
    

Returns exchange rates in the opposite direction:

![Currency exchange rate EUR to USD example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/currency%20exchange%20rate%20EUR%20to%20USD%20example.png?itok=N09jBjEl "Currency exchange rate EUR to USD example")

_Note: in general, it's safer to use the_ [_DATE function_](https://exceljet.net/functions/date-function)
 _to enter dates in other formulas because it eliminates the risk of a text value being misinterpreted on other systems with different locale settings, but in this case, dates are entered as text to keep things simple._

### Connecting the input cells

To connect the basic formula above with the input cells in the example shown, we need to substitute cell references for the hardcoded values. The final formula in cell B4 is:

    =STOCKHISTORY(F5&":"&F6,F7,F8,2)
    

Notice we assemble the stock argument by [concatenating](https://exceljet.net/glossary/concatenation)
 the currency symbols in cells F5 and F6 together, separated by a colon:

    F5&":"&F6 // returns ""USD:EUR"
    

The result is fully dynamic. If any of these four inputs are changed, STOCKHISTORY will immediately return a new set of exchange rates. In the screen below, currency 1 has been set to "USD" (US Dollar) and currency 2 has been set to "JPY" (Japanese Yen):

![Currency exchange rate USD to JPY example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/currency%20exchange%20rate%20USD%20to%20JPY%20example.png?itok=BvvfphWI "Currency exchange rate USD to JPY example")

The STOCKHISTORY function automatically sets the currency symbol as needed.

_Note: When the interval is set to monthly (2) as in this example, the STOCKHISTORY function will return the last available exchange rate in a given month._

Related formulas
----------------

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Get stock price on specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20on%20specific%20date.png "Excel formula: Get stock price on specific date")](https://exceljet.net/formulas/get-stock-price-on-specific-date)

### [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)

In this example, the goal is to retrieve the close price on July 1, 2021 for each symbol shown in column B. This can be done with the STOCKHISTORY function , whose main purpose is to retrieve historical information for a financial instrument over time. In many configurations, STOCKHISTORY returns...

[![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")](https://exceljet.net/formulas/get-stock-price-last-n-days)

### [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc. over the past n days, where n is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological...

[![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")](https://exceljet.net/formulas/get-stock-price-last-n-months)

### [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done...

Related functions
-----------------

[![Excel STOCKHISTORY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20stockhistory%20function.png "Excel STOCKHISTORY function")](https://exceljet.net/functions/stockhistory-function)

### [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)

The Excel STOCKHISTORY function retrieves historical stock price information based on a given symbol and date range. The primary purpose of STOCKHISTORY is to get the history of a financial instrument over time. The result is an array of values that spill onto the worksheet into...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)
    
*   [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    
*   [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    

### Functions

*   [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)