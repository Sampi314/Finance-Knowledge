# Get stock price (latest close) - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-stock-price-latest-close

---

[Skip to main content](https://exceljet.net/formulas/get-stock-price-latest-close#main-content)

[](https://exceljet.net/formulas/get-stock-price-latest-close#)

*   [Previous](https://exceljet.net/formulas/get-current-stock-price)
    
*   [Next](https://exceljet.net/formulas/get-stock-price-last-n-days)
    

[Financial](https://exceljet.net/formulas#Financial)

Get stock price (latest close)
==============================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

[TODAY](https://exceljet.net/functions/today-function)

[LOOKUP](https://exceljet.net/functions/lookup-function)

[INDEX](https://exceljet.net/functions/index-function)

![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")

Summary
-------

To get the latest close price of a stock with a formula, you can use the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. In the example shown, the formula in cell D5, copied down, is:

    =STOCKHISTORY(B5,TODAY(),,2,0,1)
    

The result is the latest available close price in the current month. If there is no data yet in the current month, STOCKHISTORY will return a #VALUE! error. For a more general overview of the STOCKHISTORY function, [see this page](https://exceljet.net/functions/stockhistory-function)
.

Generic formula
---------------

    =STOCKHISTORY(symbol,TODAY(),,2,0,1)

Explanation 
------------

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. The main purpose of STOCKHISTORY is to retrieve _historical_ stock price information, and we need to make a few adjustments to prevent errors that might occur when a close price is not available on a given date. We also need to adjust arguments to return just a single value per symbol, instead of an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells.

The STOCKHISTORY function retrieves historical stock price information based on a given symbol and date range. For example, to return the closing price for Apple, Inc. on December 27, 2021, you can use:

    =STOCKHISTORY("AAPL","27-Dec-2021") // close price on Dec 27
    

The result is an array that includes headers, date, and close price:

![Apple's close price on December 27, 2022](https://exceljet.net/sites/default/files/images/formulas/inline/apple%20close%20price%2027-Dec-2022.png "Apple's close price on December 27, 2022")

To get a closing price for _today_, we can use the TODAY function instead of a fixed date.

    =STOCKHISTORY("AAPL",TODAY()) // close price today
    

However, this formula is a bit fragile. If the current date (today) is a holiday or weekend, or if the market is open but not yet closed, STOCKHISTORY will return a #VALUE error. One way to handle this problem is to set the _interval_ [argument](https://exceljet.net/glossary/function-argument)
 in STOCKHISTORY to monthly instead of daily:

    =STOCKHISTORY("AAPL",TODAY(),,2) // close price this month
    

The last argument, 2, sets _interval_ to monthly (2) instead of the default of daily (0). The result is the latest available close price in the current month. To adapt this example to work in the example, as shown above, we also need to get rid of the date and the header, since we only want the close price. We can do that by adjusting arguments like this:

    =STOCKHISTORY(B5,TODAY(),,2,0,1)
    

Here, the zero after _interval_ (2) sets the _headers_ argument to "no headers". The final 1 is a property setting that tells STOCKHISTORY to return the close price only. See the [table here](https://exceljet.net/functions/stockhistory-function#properties)
 for more information about properties available to the STOCKHISTORY function.

When this formula is copied down the table, the result is the last available close price for each symbol in the current month. Note the formula will fail with a #VALUE error if there is not yet close price data in the current month. See below for a workaround.

### Workarounds

The above formula works fine as long as there is at least one close price in the current month. However, if there is no price data yet in the current month, the formula will return a #VALUE error. As a workaround, we can modify the formula to retrieve the last week of close prices for a given symbol, then use the [LOOKUP function](https://exceljet.net/functions/lookup-function)
 to get the last value in the list:

    =LOOKUP(TODAY()+1,STOCKHISTORY("MSFT",TODAY()-7,TODAY()))
    

This works because LOOKUP has some unique behaviors that make it [useful for retrieving the last value in a list](https://exceljet.net/articles/how-to-lookup-first-and-last-match)
. Essentially, we are asking LOOKUP to find a value we know can't exist (TODAY()+1). LOOKUP always operates in approximate match mode, assuming data is sorted. It scans to the end of the values looking for TODAY+1 and when that value isn't found, it returns the last value in the second column. This is an example of the [BigNum](https://exceljet.net/glossary/bignum)
 concept.

If you want to retrieve the date as well (as a reference for the price that comes back) you can use a more involved formula based on the [LET function](https://exceljet.net/functions/let-function)
:

    =LET(results,STOCKHISTORY("MSFT",TODAY()-7,TODAY()),INDEX(results,ROWS(results),0))
    

Rather than rely on approximate matching, this formula explicitly requests the last result. First, the LET function stores results from STOCKHISTORY in a variable called _results_. Next, the [ROWS function](https://exceljet.net/functions/rows-function)
 counts the rows in _results_ and feeds this number into the [INDEX function](https://exceljet.net/functions/index-function)
 as _row\_num._ Finally, with _results_ provided as _array_, and _column\_number_ hardcoded as 0, INDEX returns the last row in _results_. This row contains two values: the date and the close price on that date.

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

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

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

*   [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    
*   [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    

### Functions

*   [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    
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