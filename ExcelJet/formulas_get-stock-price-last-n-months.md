# Get stock price last n months - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-stock-price-last-n-months

---

[Skip to main content](https://exceljet.net/formulas/get-stock-price-last-n-months#main-content)

[](https://exceljet.net/formulas/get-stock-price-last-n-months#)

*   [Previous](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Next](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    

[Financial](https://exceljet.net/formulas#Financial)

Get stock price last n months
=============================

by Dave Bruns · Updated 20 Jun 2022

Related functions 
------------------

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

[TODAY](https://exceljet.net/functions/today-function)

[EDATE](https://exceljet.net/functions/edate-function)

[INDEX](https://exceljet.net/functions/index-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7052/download?token=uSbJ7Bmt)
 (23.78 KB)

![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")

Summary
-------

To get the monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) you can use a formula based on the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. In the example shown, the formula in cell D5, copied down, is:

    =TRANSPOSE(STOCKHISTORY(B5,EDATE(TODAY(),-5),TODAY(),2,0,1))
    

The result is the monthly close price for each symbol listed in column B over the past 6 months. Note that STOCKHISTORY returns an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells. The STOCKHISTORY is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
.

Generic formula
---------------

    =TRANSPOSE(STOCKHISTORY(A1,EDATE(TODAY(),-(n-1)),TODAY(),2,0,1))

Explanation 
------------

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done with the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
, whose purpose is to retrieve historical information for a financial instrument over time.

### Basic example

STOCKHISTORY retrieves historical stock price information for a given symbol and date range. STOCKHISTORY takes up to 11 [arguments](https://exceljet.net/glossary/function-argument)
, most of which are optional. The syntax for the first 5 arguments looks like this:

    =STOCKHISTORY(stock,start_date,[end_date],[interval],[headers])
    

The _interval_ argument specifies the time period to use between prices. The options are daily (0), weekly (1), or monthly (2). In this case, we want a monthly interval, so we provide 2. For example, to retrieve the close price for Apple ("AAPL") for the last 6 months beginning in August 2022, we can use a formula like this:

    =STOCKHISTORY("AAPL","1-Aug-2021","1-Jan-2022",2)
    

The result is an [array](https://exceljet.net/glossary/array)
 that includes headers, date, and close price:

![AAPL stock price Aug 2021 to Jan 2022](https://exceljet.net/sites/default/files/images/formulas/inline/example%20get%20aapl%20stock%20price%20last%20Aug%202021-Jan%202022.png "AAPL stock price Aug 2021 to Jan 2022")

The remaining arguments (property1 to property5) specify the information STOCKHISTORY can return, which includes Date, Close, Open, High, Low, and volume.  If we extend the formula to include all 6 properties, the formula looks like this:

    =STOCKHISTORY("AAPL","1-Aug-2021","1-Jan-2022",2,,0,1,2,3,4,5)
    

And the result is an array with much more detail:

![AAPL stock price Aug 2021 to Jan 2022 with details](https://exceljet.net/sites/default/files/images/formulas/inline/example%20get%20aapl%20stock%20price%20last%206%20months%20detailed.png "AAPL stock price Aug 2021 to Jan 2022 with details")

These properties can be reordered as desired by changing the order that the property numbers are listed. For example, to list Volume second, we can move Volume (5) to the second position after date (0):

    =STOCKHISTORY("AAPL","1-Aug-2021","1-Jan-2022",2,,0,5,1,2,3,4)
    

For a more detailed overview of options, see our [STOCKHISTORY function page](https://exceljet.net/functions/stockhistory-function)
.

### Dynamic dates

In the basic example above, the dates are hardcoded as text values. This works fine for a one-off formula, but in this case we want the formula to calculate the dates for us on an ongoing basis. We can do this by adding the [TODAY function](https://exceljet.net/functions/today-function)
 and the [EDATE function](https://exceljet.net/functions/edate-function)
 to the formula. To calculate a start date 6 months in the past, we use the EDATE function like this:

    =EDATE(TODAY(),-5) // date 6 months in the past
    

The TODAY function returns the current date directly to EDATE. If the date is January 8, 2021, EDATE returns the date August 8, 2021. To calculate the _end\_date_, we use the TODAY() function by itself. Once we update the basic example above, we have a formula like this:

    =STOCKHISTORY("AAPL",EDATE(TODAY(),-5),TODAY(),2)
    

The result is the same as before:

![AAPL stock price Aug 2021 to Jan 2022](https://exceljet.net/sites/default/files/images/formulas/inline/example%20get%20aapl%20stock%20price%20last%20Aug%202021-Jan%202022.png "AAPL stock price Aug 2021 to Jan 2022")

The difference is that this result will continue to update automatically as time goes by.

_Note: There is no need to supply a first of month or last of month date to STOCKHISTORY. When interval is set to monthly (2), the STOCKHISTORY function will use the last close price for a date that lands anywhere in the month. For complete months in the past, this will be the last trading day of the month. For months not yet complete, STOCKHISTORY will return the latest close price available._

### Horizontal layout

In order to display the last 6 months for each symbol in column B, we need to rotate the vertical format that STOCKHISTORY outputs by default to a _horizontal_ layout. Along with this change, we also need to remove the date field and suppress the header. To start off, we can use the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 to transpose vertical to horizontal:

    =TRANSPOSE(STOCKHISTORY("AAPL",EDATE(TODAY(),-5),TODAY(),2))
    

This flips the layout to horizontal:

![Horizontal layout with transpose function](https://exceljet.net/sites/default/files/images/formulas/inline/horizontal%20layout%20with%20transpose%20function.png "Horizontal layout with transpose function")

To remove Date and header, we need to adjust the value for _header_ and customize _properties._ We use 0 for _header_ and supply 1 for the first property to retrieve just the closing price. The formula now looks like this:

    =TRANSPOSE(STOCKHISTORY("AAPL",EDATE(TODAY(),-5),TODAY(),2,0,1))
    

And the resulting array looks like this:

![Horizontal layout without date and header](https://exceljet.net/sites/default/files/images/formulas/inline/horizontal%20layout%20without%20date%20and%20header.png "Horizontal layout without date and header")

This is close to the final formula. To finalize, we just need to replace the hardcoded symbol "AAPL" with a reference to B5:

    =TRANSPOSE(STOCKHISTORY(B5,EDATE(TODAY(),-5),TODAY(),2,0,1))
    

This is the formula used in cell D5, copied down the column.

### The header

The last piece of the puzzle is the header. Note that we don't want a header that says "Date" or "Price". Instead, for each price that appears in a separate column, we want a header that shows a corresponding date. To keep things consistent, it would be nice if we could just adjust the arguments in STOCKHISTORY to return only a header, but this won't work; STOCKHISTORY will return a #VALUE error if only the date field is selected. As a workaround, we can adjust the formula to output both date and close price. First, we adjust the STOCKHISTORY function to remove only the header:

    =TRANSPOSE(STOCKHISTORY(B5,EDATE(TODAY(),-5),TODAY(),2,0))
    

By default, STOCKHISTORY will return both Date and Price, so we no longer need to request the Price only, since we need the Dates. The result looks like this:

![Dates and prices together with no header](https://exceljet.net/sites/default/files/images/formulas/inline/dates%20and%20prices%20together%20with%20no%20header.png "Dates and prices together with no header")

Next, we use the INDEX function to return just the first row of the array (the Dates):

    =INDEX(TRANSPOSE(STOCKHISTORY(B5,EDATE(TODAY(),-5),TODAY(),2,0)),1,0)
    

Inside INDEX, _row\_num_ is 1, and _column\_number_ is set 0, in order to return the entire row. The result is an array of dates that can be used as a header:

![Getting date row only with the INDEX function](https://exceljet.net/sites/default/files/images/formulas/inline/getting%20date%20row%20only%20with%20the%20INDEX%20function.png "Getting date row only with the INDEX function")

This is the formula used in D4 in the example. Note when _interval_ is set to monthly (2), STOCKHISTORY will always show "first of month" dates. However, you can apply a custom [date format](https://exceljet.net/glossary/number-format)
 to display the dates as you like. In the example shown, the date format used is "mmm-yyyy".

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

[![Excel formula: Get current stock price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20current%20price.png "Excel formula: Get current stock price")](https://exceljet.net/formulas/get-current-stock-price)

### [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)

In this example, the goal is to retrieve the current stock price for the companies listed in Column B. Note these cells in the range B5:B16 have already been converted to the "Stocks" Data Type . Once the Stocks Data Type is available on the worksheet, you can retrieve various information using the...

Related functions
-----------------

[![Excel STOCKHISTORY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20stockhistory%20function.png "Excel STOCKHISTORY function")](https://exceljet.net/functions/stockhistory-function)

### [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)

The Excel STOCKHISTORY function retrieves historical stock price information based on a given symbol and date range. The primary purpose of STOCKHISTORY is to get the history of a financial instrument over time. The result is an array of values that spill onto the worksheet into...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

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
    
*   [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    

### Functions

*   [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    

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