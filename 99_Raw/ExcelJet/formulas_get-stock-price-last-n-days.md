# Get stock price last n days - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-stock-price-last-n-days

---

[Skip to main content](https://exceljet.net/formulas/get-stock-price-last-n-days#main-content)

[](https://exceljet.net/formulas/get-stock-price-last-n-days#)

*   [Previous](https://exceljet.net/formulas/get-stock-price-latest-close)
    
*   [Next](https://exceljet.net/formulas/get-stock-price-last-n-months)
    

[Financial](https://exceljet.net/formulas#Financial)

Get stock price last n days
===========================

by Dave Bruns · Updated 22 Oct 2023

Related functions 
------------------

[STOCKHISTORY](https://exceljet.net/functions/stockhistory-function)

[SORT](https://exceljet.net/functions/sort-function)

![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")

Summary
-------

To get the daily closing stock price for the last n days (i.e. last 7 days, last 14 days, last 30 days, etc.) you can use a formula based on the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
. In the example shown, the formula in cell D4 is:

    =SORT(STOCKHISTORY(I5,TODAY()-I8,TODAY(),,,0,1,2,3,4,5),1,-1)
    

The result is detailed historical pricing for Microsoft Corporation ("MSFT") over the last 30 days. Note that STOCKHISTORY returns an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells. The data appears in reverse chronological order because the STOCKHISTORY is [nested](https://exceljet.net/glossary/nesting)
 inside the [SORT function](https://exceljet.net/functions/sort-function)
, which is configured to sort in descending order.

> The STOCKHISTORY function is only available in [Excel 365](https://exceljet.net/glossary/excel-365)
>  

Generic formula
---------------

    =SORT(STOCKHISTORY(symbol,TODAY()-n,TODAY(),,,0,1,2,3,4,5),1,-1)

Explanation 
------------

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc.  over the past n days, where **n** is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological order, with the latest information appearing first.

This can be done with the [STOCKHISTORY function](https://exceljet.net/functions/stockhistory-function)
, whose main purpose is to retrieve historical information for a financial instrument over time.

### Simple example

STOCKHISTORY retrieves historical stock price information based on a given symbol and date range. For example, to return the closing price for Apple, Inc. on December 27, 2021, you can use STOCKHISTORY like this:

    =STOCKHISTORY("AAPL","27-Dec-2021") // close price on Dec 27
    

The result is an array that includes headers, date, and close price:

![Apple's close price on December 27, 2022](https://exceljet.net/sites/default/files/images/formulas/inline/apple%20close%20price%2027-Dec-2022.png "Apple's close price on December 27, 2022")

STOCKHISTORY takes a number of [function arguments](https://exceljet.net/glossary/function-argument)
, but in this simple case, we only need to provide _symbol_ and _start\_date_. All other arguments are optional with default values: e_nd\_date_ defaults to _start\_date_, _interval_ defaults to daily, _headers_ are on by default, and Date and Close are the default information retrieved. For a more detailed discussion, see our [STOCKHISTORY function page](https://exceljet.net/functions/stockhistory-function)
.

### STOCKHISTORY configuration

In the more complex example shown above, we need to supply additional information. We start by providing a reference to the symbol in I5: 

    =STOCKHISTORY(I5
    

Next, we add the _start\_date_ and _end\_date_, which are calculated with the [TODAY function](https://exceljet.net/functions/today-function)
:

    =STOCKHISTORY(I5,TODAY()-I8,TODAY()
    

Notice that _start\_date_ is the current date minus I8, which is 30 in the example shown. This results in a date 30 days earlier than the date returned by TODAY. This works because [Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
. The _end\_date_ is simply the value returned by TODAY – the current date.

The next two arguments are _interval_ and _headers_, and we leave these at their defaults, by using empty commas:

    STOCKHISTORY(I5,TODAY()-I8,TODAY(),,,
    

Finally, we need to specify the properties we want. The STOCKHISTORY function supports [six properties that are specified by number](https://exceljet.net/functions/stockhistory-function#properties)
. In this case, we want all properties (Date, Close, Open, High, Low, and Volume), so we list out all 6 numbers in the order that we want them:

    STOCKHISTORY(I5,TODAY()-I8,TODAY(),,,0,1,2,3,4,5)
    

This completes the configuration for STOCKHISTORY. When entered, the result will be an [array](https://exceljet.net/glossary/array)
 that will [spill](https://exceljet.net/glossary/spill)
 into multiple cells. By default, STOCKHISTORY will return information in chronological order with older dates appearing first. Note that the number of rows returned will vary according to the number in cell I8, and the number of days the market is not open in the date range provided; STOCKHISTORY will simply omit dates on which the market is not open. The output also depends on the time of day. If the market is already closed, STOCKHISTORY will return information for the current date.

### Sorting results

In the example shown, we want to sort results in reverse chronological order. To do this we can nest the STOCKHISTORY function inside the SORT function like this:

    =SORT(STOCKHISTORY(I5,TODAY()-I8,TODAY(),,,0,1,2,3,4,5),1,-1)
    

Inside SORT, the [array](https://exceljet.net/glossary/array)
 returned by STOCKHISTORY becomes the _array_ argument. _Sort\_index_ is provided as 1 since dates are in the first column, and _sort\_order_ is given as -1, since we want to sort dates in descending order.

The output of this formula is fully dynamic. If the symbol in cell I5 is changed, or the number for n in cell I8 is changed, the formula returns a new set of results.

Related formulas
----------------

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Get stock price on specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20on%20specific%20date.png "Excel formula: Get stock price on specific date")](https://exceljet.net/formulas/get-stock-price-on-specific-date)

### [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)

In this example, the goal is to retrieve the close price on July 1, 2021 for each symbol shown in column B. This can be done with the STOCKHISTORY function , whose main purpose is to retrieve historical information for a financial instrument over time. In many configurations, STOCKHISTORY returns...

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

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

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
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    

### Functions

*   [STOCKHISTORY Function](https://exceljet.net/functions/stockhistory-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

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