# Get current stock price - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-current-stock-price

---

[Skip to main content](https://exceljet.net/formulas/get-current-stock-price#main-content)

[](https://exceljet.net/formulas/get-current-stock-price#)

*   [Previous](https://exceljet.net/formulas/future-value-vs.-present-value)
    
*   [Next](https://exceljet.net/formulas/get-stock-price-latest-close)
    

[Financial](https://exceljet.net/formulas#Financial)

Get current stock price
=======================

by Dave Bruns · Updated 16 Jun 2022

Related functions 
------------------

[FIELDVALUE](https://exceljet.net/functions/fieldvalue-function)

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

![Excel formula: Get current stock price](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20stock%20price%20current%20price.png "Excel formula: Get current stock price")

Summary
-------

To get the current market price of a stock, you can use the "Stocks" [Data Type](https://exceljet.net/glossary/data-type)
 and a simple formula. In the example shown, Data Types are in column B, and the formula in cell D5, copied down, is:

    =B5.Price
    

The result in column C is the current price for each of the stock Data Types in column B. These prices will change when the Data Type is refreshed.

_Note: you can use the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
 to get the [last available close price](https://exceljet.net/formulas/get-stock-price-latest-close)
 and other historical pricing at daily, weekly, and monthly intervals. The STOCKHISTORY function is a "pure" formula approach, the approach described here requires the Stocks Data Type._

Generic formula
---------------

    =A1.Price

Explanation 
------------

In this example, the goal is to retrieve the current stock price for the companies listed in Column B. Note these cells in the range B5:B16 have already been converted to the "Stocks" [Data Type](https://exceljet.net/glossary/data-type)
. Once the Stocks Data Type is available on the worksheet, you can retrieve various information using the simple formulas described below. These formulas follow a "dot" syntax like this:

    =A1.field
    

With a valid Data Type in A1, Excel will automatically display available fields once the "." is typed.

_Note: the Stocks Data Type is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
._

### Previous close

The formula for "Last close" in column C is:

    =B5.[Previous close]
    

Notice the field name "Previous close" is enclosed in square brackets. This is a requirement for any field name that contains a space character.

### Current Price

The formula for "Last close" in column D is:

    =B5.Price
    

### Change %

The formula for "Change %" in column E is:

    =B5.[Change (%)]
    

This is equivalent to the manual formula:

    =(D5-C5)/C5 // manual change %
    

### FIELDVALUE function

The [FIELDVALUE function](https://exceljet.net/functions/fieldvalue-function)
 can also be used as an alternative to the "dot" syntax formulas above. The equivalent formulas are:

    =FIELDVALUE(B5,"Previous close")
    =FIELDVALUE(B5,"Price")
    =FIELDVALUE(B5,"Change (%)")
    

Notice square brackets are not required, but the field names are enclosed in double quotes ("").

Related formulas
----------------

[![Excel formula: Get stock price on specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20on%20specific%20date.png "Excel formula: Get stock price on specific date")](https://exceljet.net/formulas/get-stock-price-on-specific-date)

### [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)

In this example, the goal is to retrieve the close price on July 1, 2021 for each symbol shown in column B. This can be done with the STOCKHISTORY function , whose main purpose is to retrieve historical information for a financial instrument over time. In many configurations, STOCKHISTORY returns...

[![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")](https://exceljet.net/formulas/get-stock-price-last-n-days)

### [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc. over the past n days, where n is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological...

[![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")](https://exceljet.net/formulas/get-stock-price-last-n-months)

### [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done...

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

Related functions
-----------------

[![Excel FIELDVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20fieldvalue%20function.png "Excel FIELDVALUE function")](https://exceljet.net/functions/fieldvalue-function)

### [FIELDVALUE Function](https://exceljet.net/functions/fieldvalue-function)

The Excel FIELDVALUE function extracts a given field value from a data type. The field is specified by name and provided as a text value.

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

*   [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    
*   [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)
    

### Functions

*   [FIELDVALUE Function](https://exceljet.net/functions/fieldvalue-function)
    
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