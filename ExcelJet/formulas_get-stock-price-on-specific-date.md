# Get stock price on specific date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-stock-price-on-specific-date

---

[Skip to main content](https://exceljet.net/formulas/get-stock-price-on-specific-date#main-content)

[](https://exceljet.net/formulas/get-stock-price-on-specific-date#)

*   [Previous](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Next](https://exceljet.net/formulas/income-tax-bracket-calculation)
    

[Financial](https://exceljet.net/formulas#Financial)

Get stock price on specific date
================================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

![Excel formula: Get stock price on specific date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20stock%20price%20on%20specific%20date.png "Excel formula: Get stock price on specific date")

Summary
-------

To get the latest close price of a stock with a formula, you can use the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. In the example shown, the formula in cell D5, copied down, is:

    =STOCKHISTORY(B5,$F$5,,0,0,1)
    

The result is the close price for each symbol in the table on July 1, 2021. Note that if there is no close date on the date given, STOCKHISTORY will return a #VALUE! error. For a more general overview of the STOCKHISTORY function, [see this page](https://exceljet.net/functions/stockhistory-function)
.

Generic formula
---------------

    =STOCKHISTORY(B5,date,,0,0,1)

Explanation 
------------

In this example, the goal is to retrieve the close price on July 1, 2021 for each symbol shown in column B. This can be done with the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
, whose main purpose is to retrieve historical information for a financial instrument over time. In many configurations, STOCKHISTORY returns an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells. However, in this case, we want only a single result for each symbol. The formula is tied to the date entered in cell F5, which can be changed at any time.

STOCKHISTORY retrieves historical stock price information based on a given symbol and date range. For example, to return the closing price for Apple, Inc. on December 27, 2021, you can use STOCKHISTORY like this:

    =STOCKHISTORY("AAPL","27-Dec-2021") // close price on Dec 27
    

The result is an array that includes headers, date, and close price:

![Apple's close price on December 27, 2022](https://exceljet.net/sites/default/files/images/formulas/inline/apple%20close%20price%2027-Dec-2022.png "Apple's close price on December 27, 2022")

We only need to provide _start\_date_ because the _end\_date_ will automatically default to the _start\_date_ if not provided. This gives us the basic information we want, but we need to remove the date and the header, since we only want the close price. We start by providing a reference to the symbol in B5 and the date in cell F5:

    =STOCKHISTORY(B5,$F$5
    

Notice $F$5 is entered as an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 to prevent this reference from changing as the formula is copied down the table. The final formula looks like this:

    =STOCKHISTORY(B5,$F$5,,0,0,1)
    

In this version, _end\_date_ is left blank, _interval_ is set to 0 for daily, _headers_ is set to 0 (no headers), and the final argument is _property1_, which is given as 1 to retrieve the price. [More on STOCKHISTORY properties here](https://exceljet.net/functions/stockhistory-function#properties)
.

As the formula is copied down, STOCKHISTORY retrieves the close price for each symbol in column B on July 1, 2021. If the date in cell F5 is changed, STOCKHISTORY retrieves a new set of close prices.

Related formulas
----------------

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")](https://exceljet.net/formulas/get-stock-price-last-n-days)

### [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc. over the past n days, where n is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological...

[![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")](https://exceljet.net/formulas/get-stock-price-last-n-months)

### [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done...

[![Excel formula: Get current stock price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20current%20price.png "Excel formula: Get current stock price")](https://exceljet.net/formulas/get-current-stock-price)

### [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)

In this example, the goal is to retrieve the current stock price for the companies listed in Column B. Note these cells in the range B5:B16 have already been converted to the "Stocks" Data Type . Once the Stocks Data Type is available on the worksheet, you can retrieve various information using the...

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
    
*   [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    

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