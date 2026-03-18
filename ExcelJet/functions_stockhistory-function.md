# Excel STOCKHISTORY function | Exceljet

**Source:** https://exceljet.net/functions/stockhistory-function

---

[Skip to main content](https://exceljet.net/functions/stockhistory-function#main-content)

[](https://exceljet.net/functions/stockhistory-function#)

*   [Previous](https://exceljet.net/functions/sortby-function)
    
*   [Next](https://exceljet.net/functions/take-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

STOCKHISTORY Function
=====================

by Dave Bruns · Updated 18 Jun 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8427/download?token=fn8XamrS)
 (63.45 KB)

![Excel STOCKHISTORY function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20stockhistory%20function.png "Excel STOCKHISTORY function")

Summary
-------

The Excel STOCKHISTORY function retrieves historical stock price information based on a given symbol and date range. The primary purpose of STOCKHISTORY is to get the history of a financial instrument over time. The result is an array of values that spill onto the worksheet into multiple cells.

Purpose 
--------

Retrieve stock price information

Return value 
-------------

Array of stock price information

Syntax
------

    =STOCKHISTORY(stock,start_date,[end_date],[interval],[headers],[properties],...)

*   _stock_ - A ticker symbol in double quotes ("MSFT", "AAPL", "GOOG", etc.).
*   _start\_date_ - The start date for data to be retrieved.
*   _end\_date_ - \[optional\] The end date for data to be retrieved. Default is start\_date.
*   _interval_ - \[optional\] Time interval. Daily = 0, weekly = 1, monthly = 2. Default is 0.
*   _headers_ - \[optional\] No header = 0, basic header = 1, instrument + header = 2. Default is 1.
*   _properties_ - \[optional\] Additional data to retrieve. Default is Date and Close. See below.

Using the STOCKHISTORY function 
--------------------------------

The STOCKHISTORY function retrieves historical stock price information based on a given symbol and date range. The main purpose of STOCKHISTORY is to get the history of a financial instrument over time. Although the name suggests that STOCKHISTORY is meant to work only with stocks, STOCKHISTORY can also work with bonds, index funds, mutual funds, and currency exchange rates. Note that STOCKHISTORY retrieves multiple results. The result is an [array](https://exceljet.net/glossary/array)
 of values that [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells.

> STOCKHISTORY only returns _historical_ information recorded after market close. If you need a _current_ stock price, use the stock datatype, as explained here: [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
> . The data provided by STOCKHISTORY comes from [LSEG Data & Analytics](https://support.microsoft.com/en-us/office/about-the-stocks-financial-data-sources-98a03e23-37f6-4776-beea-c5a6c8e787e6)
>  (previously Refinitiv). The feed updates [once per trading day](https://techcommunity.microsoft.com/blog/excelblog/announcing-stockhistory/1404338)
> , after markets close. Keep in mind that to get the latest data you may need to refresh the worksheet manually (Data › Refresh All). Microsoft cautions that all figures are provided “as‑is” and may be delayed, so use them for analysis only, not real‑time trading decisions.

### Table of Contents

*   [Primary arguments](https://exceljet.net/functions/stockhistory-function#primary-arguments)
    
*   [Additional properties](https://exceljet.net/functions/stockhistory-function#properties)
    
*   [Specifying the exchange](https://exceljet.net/functions/stockhistory-function#specifying-an-exchange)
    
*   [Example - Daily close prices](https://exceljet.net/functions/stockhistory-function#example-get-daily-close-prices-for-a-stock)
    
*   [Example - Monthly close prices](https://exceljet.net/functions/stockhistory-function#example-monthly-close-prices-for-a-stock)
    
*   [Example - Make inputs variable](https://exceljet.net/functions/stockhistory-function#example-make-inputs-variable)
    
*   [Example - Specifying additional properties](https://exceljet.net/functions/stockhistory-function#example-specifying-additional-properties)
    
*   [Example - A horizontal layout for multiple stocks](https://exceljet.net/functions/stockhistory-function#example-a-horizontal-layout-for-multiple-stocks)
    
*   [Example - Last 6 months](https://exceljet.net/functions/stockhistory-function#example-last-6-months)
    
*   [Example - Make exchange variable](https://exceljet.net/functions/stockhistory-function#example-make-exchange-variable)
    
*   [Example - Retrieve currency exchange rates](https://exceljet.net/functions/stockhistory-function#example-retrieving-currency-exchange-rates)
    

### Primary arguments

The STOCKHISTORY function accepts five primary [arguments](https://exceljet.net/glossary/function-argument)
, and six additional property arguments to retrieve additional information. _Stock_ and _start\_date_ are the only required arguments. Each argument is described in detail below. Additional properties are described in the [table here](https://exceljet.net/functions/stockhistory-function#properties)
.

*   _Stock_ - the ticker symbol used to retrieve historical prices. _Stock_ should be supplied as a [text value](https://exceljet.net/glossary/text-value)
     in double quotes ("") when hardcoded, for example, "MSFT", "GOOG", "AAPL", "TSLA", etc. Results are retrieved from the default exchange for the instrument.
*   _Start\_date_ - The date at which to start retrieving data. Note that _start\_date_ is not necessarily the first date that will appear in the results. If the _interval_ is set to daily (0), the first date in the results will be the first date that the exchange is open and data is available. If the _interval_ is set to weekly (1) or monthly (2), the first date will be set to the first date in the period, i.e., the first day of the week or the first day of the month.
*   _End\_date_ - The date at which to stop retrieving data. Like _start\_date_, the actual last date in results may be different from the _end\_date_ provided. If the _interval_ is set to daily (0), the last date in the results will be the last date in the date range that data is available. If the _interval_ is set to weekly (1) or monthly (2), the last date will be the last date in the period, i.e., the last day of the week or the last day of the month. _End\_date_ is optional and will default to _start\_date_ if not supplied.
*   _Interval_ - the time period between data points. The available options are Daily (0), Weekly (1), and Monthly (2). _Interval_ is optional and will default to Daily (0) if not provided.
*   _Headers_ - the _headers_ argument controls header information that will appear at the top of the data retrieved. The available options are No header (0), Basic header (1), and header with instrument information (2). _Headers_ is optional and will default to basic header (1) when not provided.
*   _Properties_ - six arguments for additional information that can be retrieved. See the table below for details.

_Note: The safest way to provide the start\_date and end\_date is as a reference to a cell that contains a valid date or with the DATE function because dates as text values can sometimes be misinterpreted._

### Additional Properties

The table below shows the additional information the STOCKHISTORY function can retrieve, which are described as properties. Properties are specified with the numeric code seen in the "Code" column.

| Code | Value | Description |
| --- | --- | --- |
| 0   | Date | The first trading day in the period |
| 1   | Close | Closing price on the last trading day in the period |
| 2   | Open | The opening price on the last trading day in the period |
| 3   | High | The highest price in the period |
| 4   | Low | The lowest price in the period |
| 5   | Volume | Volume traded during the period |

The order in which you request properties is the order in which they will appear. See: [STOCKHISTORY properties example](https://exceljet.net/functions/stockhistory-function#example-specifying-additional-properties)
.

> Note that by default, STOCKHISTORY will return the Date and Close properties, so there is no need to ask for Date and Close if these are the only properties you need. However, if you request _any properties_, you will override this default behavior and will need to specify _all the properties you want_.

### Specifying the exchange

When requesting the price for a stock symbol, results are retrieved from the _default exchange_ for the instrument. To request information from a specific exchange, prefix the symbol with a 4-character ISO market identifier code (MIC), followed by a colon. For example, to refer to Microsoft Corporation on the Nasdaq Stock Market, use "XNAS:MSFT". To refer to Microsoft Corporation on Austria's Wiener Boerse exchange, use "XWBO:MSFT". The table below lists the 4-character code for a few common exchanges.

|     |     |     |
| --- | --- | --- |
| **Exchange Name** | **Code** | **Country** |
| New York Stock Exchange | XNYS | United States |
| Nasdaq Stock Market | XNAS | United States |
| London Stock Exchange | XLON | United Kingdom |

You can find a full list of supported exchange codes [here](https://support.microsoft.com/en-us/office/about-the-stocks-financial-data-sources-98a03e23-37f6-4776-beea-c5a6c8e787e6)
.

### Example - Get daily close prices for a stock

To retrieve the daily close price for Apple ("AAPL") for the month of January 2021, the formula in cell B4 is:

    =STOCKHISTORY("AAPL",DATE(2021,1,1),DATE(2021,1,31))
    

_Interval_ is not provided and defaults to Daily (0). _Headers_ is not provided and defaults to Date and Close. With this configuration, the STOCKHISTORY function returns 19 results. Note that weekends are excluded and the first date retrieved is January 4 since the exchange was closed January 1-3. Also note the [DATE function](https://exceljet.net/functions/date-function)
 is used to supply the start and end dates.

![STOCKHISTORY function - daily results example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory%20daily%20results%20example.png?itok=cfebXMeX "STOCKHISTORY function - daily results example")

For a more detailed explanation, [see this example](https://exceljet.net/formulas/get-stock-price-last-n-days)
.

### Example - Monthly close prices

The STOCKHISTORY function can retrieve daily (0), weekly (1), and monthly (2) price data by setting a value for the _interval_ argument. For example, to get monthly close prices for Apple, Inc. ("AAPL") for all of 2023, set the interval to 2. In the workbook below, the formula in cell B4 is:

    =STOCKHISTORY("AAPL",DATE(2023,1,1),DATE(2023,12,31),2)

![STOCKHISTORY function - monthly close prices](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory_monthly_results_example.png "STOCKHISTORY function - monthly close prices")

Note that the _interval_ argument is now provided as 2 in order to retrieve _monthly_ results.

_Note: When the interval is provided as 2, STOCKHISTORY will return the last closing price in a given month, regardless of the date. In other words, the result for the first of the month will be the same as the last day of the month._

### Example - Make inputs variable

In the example below, the inputs for _stock_, _start\_date_, and _end\_date_ are made variable by exposing them on the worksheet in cells F6, F7, and F8. The formula in cell B4 is:

    =STOCKHISTORY(F6,F7,F8,2)
    

Note that the fourth argument, _interval_, is set to 2, which outputs monthly results.

![STOCKHISTORY function - variable inputs example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory%20variable%20inputs%20example.png?itok=NNEVpfF2 "STOCKHISTORY function - variable inputs example")

The result is the close price for Tesla ("TSLA") for the 12 months in 2021. If the values in F6:F8 are changed, the results from STOCKHISTORY will automatically update.

### Example - Additional properties

The properties returned by STOCKHISTORY can be controlled by customizing and/or reordering numbers starting with the sixth argument (_property1_). In the example shown below, the formula in cell B4 is:

    =STOCKHISTORY(I6,I7,I8,2,1,0,5,3,4,1)
    

The result is monthly stock price information for The 3M Company ("MMM") for the year 2021. The [properties](https://exceljet.net/functions/stockhistory-function#properties)
 requested include Date (0), Volume (5), High (3), Low (4), and Close (1). Notice these are the _last 5 arguments_ in the function.

![STOCKHISTORY function - custom properties example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory%20variable%20additional%20properties%20example.png?itok=Lde8_JED "STOCKHISTORY function - custom properties example")

Note that the reason STOCKHISTORY uses numeric codes for properties is so they can be easily reordered. In the worksheet below, we are returning the same five properties in a new order: Date, Close, High, Low, and Volume. The formula in cell B4 is now:

    =STOCKHISTORY(I6,I7,I8,2,1,0,1,3,4,5)

![STOCKHISTORY function - same properties, different order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory_same_properties_different_order_rexample.png "STOCKHISTORY function - same properties, different order")

For a full list of properties with codes and descriptions, see the [Properties section](https://exceljet.net/functions/stockhistory-function#properties)
.

### Example - A horizontal layout for multiple stocks

By default, STOCKHISTORY returns information in a _vertical_ layout. To display results in a _horizontal_ layout, you can use the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
. In the example shown below, the formula in C5, copied down, is:

    =TRANSPOSE(STOCKHISTORY(B5,DATE(2024,1,1),DATE(2024,6,1),2,0,1))
    

The result is the trailing monthly close price for each symbol for the first 6 months of 2024:

![STOCKHISTORY function - horizontal layout example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory%20horizontal%20layout%20example.png?itok=Cizq_fS2 "STOCKHISTORY function - horizontal layout example")

TRANSPOSE takes what would normally be a vertical layout and converts it to a horizontal layout.

### Example - last 6 months

To get the monthly close price for a list of stocks for the last 6 complete months, you can use a formula based on the TODAY function. You can see the result in the workbook below, where the formula in C5 is:

    =TRANSPOSE(STOCKHISTORY(B5,EOMONTH(TODAY(),-7)+1,EOMONTH(TODAY(),-1)+1,2,0,1))

![STOCKHISTORY function - last 6 complete months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory_function_last_6_months_example.png "STOCKHISTORY function - last 6 complete months")

This formula is dynamic and will continue to return data for the last 6 months over time. The [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 and the [TODAY function](https://exceljet.net/functions/today-function)
 are used to create a start date on the [first day of the month](https://exceljet.net/formulas/get-first-day-of-previous-month)
, 6 months before the current month. The end date is created in the same way and is the first day of the previous month. The formula here is a variation of an [example explained in greater detail here](https://exceljet.net/formulas/get-stock-price-last-n-months)
.

_Notes: (1) Because the TODAY function will recalculate each time a worksheet is opened, the STOCKHISTORY function also recalculates when the worksheet is opened. (2) The trend line is created by selecting a range like C5:H5 and inserting a sparkling at Insert > Sparklines > Line._

### Example - Make exchange variable

To request information from a specific exchange, prefix the symbol with a 4-character [code](https://support.microsoft.com/en-us/office/about-the-stocks-financial-data-sources-98a03e23-37f6-4776-beea-c5a6c8e787e6)
, followed by a colon (:). In the worksheet below, the exchange is variable and entered in cell F5. The formula in cell B4 is:

    =STOCKHISTORY(F5&":"&F6,F7,F8,2)
    

The result is the monthly close price for Caterpillar, Inc. on the [Wiener-Borse](https://www.wienerborse.at/)
 exchange:

![STOCKHISTORY function - variable exchange example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/stockhistory%20variable%20exchange%20example.png?itok=xF0Qx26Q "STOCKHISTORY function - variable exchange example")

If the value in F5 is changed to "XNYS," STOCKHISTORY will return Caterpillar's monthly close price on the New York Stock Exchange.

### Example - Retrieve currency exchange rates

To get the currency exchange rate for a given currency pair with STOCKHISTORY, enter the two 3-letter codes separated by a colon (:) as the _stock_ argument. For example, to get the monthly currency exchange rate between the US Dollar ("USD") and the Euro ("EUR") for the months of January 2021 through March 2021, you can use STOCKHISTORY like this:

    =STOCKHISTORY("USD:EUR","1-Jan-2021","1-Mar-2021",2)
    

The result is an array with three months of rates:

![STOCKHISTORY function - currency exchange rate example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/currency%20exchange%20rate%20USD%20to%20EUR%20example.png?itok=VBsEQXYO "STOCKHISTORY function - currency exchange rate example")

To reverse the direction of the exchange, just swap the order of the currency pairs:

    =STOCKHISTORY("EUR:USD","1-Jan-2021","1-Mar-2021",2)
    

For a more detailed explanation, [see this example](https://exceljet.net/formulas/currency-exchange-rate-example)
.

### Notes

*   If data is not available for the period requested, STOCKHISTORY returns a #VALUE! error.
*   When _interval_ is monthly (2), STOCKHISTORY returns the _latest_ data in a given month. In other words, you will get the latest closing price when a month is not yet complete.
*   By default, STOCKHISTORY will return the date and closing price, but this behavior can be adjusted by [specifying custom properties](https://exceljet.net/functions/stockhistory-function#example-specifying-additional-properties)
    .
*   STOCKHISTORY only returns historical information recorded after market close. If you need a _current stock price_, use the stock datatype, as explained here: [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    .

STOCKHISTORY function examples
------------------------------

[![Excel formula: Get stock price last n months](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20months.png "Excel formula: Get stock price last n months")](https://exceljet.net/formulas/get-stock-price-last-n-months)

### [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)

In this example, the goal is to get monthly closing stock price over the past n months (i.e. last 6 months, last 12 months, last 24 months, etc.) for the list of symbols that appear in column B. In addition, we want a rolling time period, that stays in sync with the current date. This can be done...

[![Excel formula: Get stock price on specific date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20on%20specific%20date.png "Excel formula: Get stock price on specific date")](https://exceljet.net/formulas/get-stock-price-on-specific-date)

### [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)

In this example, the goal is to retrieve the close price on July 1, 2021 for each symbol shown in column B. This can be done with the STOCKHISTORY function , whose main purpose is to retrieve historical information for a financial instrument over time. In many configurations, STOCKHISTORY returns...

[![Excel formula: Get stock price (latest close)](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20latest%20close.png "Excel formula: Get stock price (latest close)")](https://exceljet.net/formulas/get-stock-price-latest-close)

### [Get stock price (latest close)](https://exceljet.net/formulas/get-stock-price-latest-close)

In this example, the goal is to retrieve the last available close price for each symbol shown in column B. This can be done with the STOCKHISTORY function . The main purpose of STOCKHISTORY is to retrieve historical stock price information, and we need to make a few adjustments to prevent errors...

[![Excel formula: Get stock price last n days](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20last%20n%20days.png "Excel formula: Get stock price last n days")](https://exceljet.net/formulas/get-stock-price-last-n-days)

### [Get stock price last n days](https://exceljet.net/formulas/get-stock-price-last-n-days)

In this example, the goal is to retrieve historical stock price information for a given stock, provided as a ticker symbol like "MSFT", "AAPL", "MMM", etc. over the past n days, where n is a variable that can be changed as desired. In addition, the data should be sorted in reverse chronological...

[![Excel formula: Get current stock price](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20stock%20price%20current%20price.png "Excel formula: Get current stock price")](https://exceljet.net/formulas/get-current-stock-price)

### [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)

In this example, the goal is to retrieve the current stock price for the companies listed in Column B. Note these cells in the range B5:B16 have already been converted to the "Stocks" Data Type . Once the Stocks Data Type is available on the worksheet, you can retrieve various information using the...

[![Excel formula: Currency exchange rate example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/currency%20exchange%20rate%20example.png "Excel formula: Currency exchange rate example")](https://exceljet.net/formulas/currency-exchange-rate-example)

### [Currency exchange rate example](https://exceljet.net/formulas/currency-exchange-rate-example)

In this example, the goal is to get monthly currency exchange rates for a given currency pair (i.e., USD > EUR, USD > GBP, CAD > JPY, etc.). Currency abbreviations are entered in cells F5 and F6, and the start and end dates are entered in cells F7 and F8. If any of these four inputs are...

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
    
*   [Get current stock price](https://exceljet.net/formulas/get-current-stock-price)
    
*   [Currency exchange rate example](https://exceljet.net/formulas/currency-exchange-rate-example)
    
*   [Get stock price last n months](https://exceljet.net/formulas/get-stock-price-last-n-months)
    
*   [Get stock price on specific date](https://exceljet.net/formulas/get-stock-price-on-specific-date)
    

### Links

*   [Microsoft STOCKHISTORY function documentation](https://support.microsoft.com/en-us/office/stockhistory-function-1ac8b5b3-5f62-4d94-8ab8-7504ec7239a8)
    

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