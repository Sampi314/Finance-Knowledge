# Brand New Excel Function: STOCKHISTORY

**Source:** https://sumproduct.com/news/brand-new-excel-function-stockhistory/

---

[Home](https://sumproduct.com/)

\> Brand New Excel Function: STOCKHISTORY

*   June 11, 2020

Brand New Excel Function: STOCKHISTORY
======================================

Brand New Excel Function: STOCKHISTORY
======================================

11 June 2020

_Microsoft announces a new Excel function for Microsoft 365, Excel for Microsoft 365 for Mac and Excel for the web._

**The STOCKHISTORY function**

You might think that current stock trajectories are like my career path – well now you can prove it!

There’s a new function in town, albeit currently a “**Beta feature**”, which means it is only available to a portion – and not all – of the Office Insider community. However, once it has been tested further and “optimised” it will roll out to the rest of Office Insider and eventually become Generally Available in Microsoft 365 and online.

This **STOCKHISTORY** function retrieves historical data about a financial instrument and loads it as a [dynamic array](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
, which will spill when required (_i.e._ Excel will dynamically create an appropriately sized range once you press **ENTER**).

**STOCKHISTORY** has the following syntax:

**\=STOCKHISTORY(stock, start\_date, \[end\_date\], \[interval\], \[headers\], \[property0\], \[property1\], \[property2\], \[property3\], \[property4\], \[property5\])**

where:

*   **stock:** this is required and is a function which returns historical price data about the financial instrument corresponding to the value entered. You should enter a ticker symbol in double quotes (_e.g_. “MSFT”) or else it should be a reference to a cell containing the **[Stocks](https://www.sumproduct.com/news/article/new-data-types-and-fieldvalue-function-now-generally-available-sort-of)
    ** data type. This will pull data from the default exchange for the instrument. You may also refer to a specific exchange by entering a four (4) character ISO market identifier code (MIC), followed by a colon, followed by the ticker symbol (_e.g_. “XNAS:MSFT”)
*   **start\_date:** this argument is also required, and represents the earliest date for which data is to be retrieved. It should be noted that if **interval**_(see below)_ is not 0 (daily), the first data point may be earlier than the **start\_date** provided: instead, it will be the first date of the period requested
*   **end\_date:** this argument is the first optional element. This represents the latest date for which data will be retrieved. If omitted, the default is today (**TODAY()**). It should be noted in this instance that history for the current day is not provided if the market has not yet closed, but that the historical data table will be updated within a few hours of the close of the market. In the meantime, the **Stock** data type may be refreshed to show the current price, even though the **STOCKHISTORY** function cannot presently display it
*   **interval:** this argument is option and denotes the interval each data value represents as follows:

![](<Base64-Image-Removed>)

*   **headers:** another optional argument. This specifies whether to display headings as follows:

![](<Base64-Image-Removed>)

When included, headers are rows of text that are part of the array returned by the function.

It is noted that on initial release the headers may not always display, but we are sure this bug will be fixed shortly. In the meantime, it’s a small price to pay for this very useful function!

*   **property0** to **property5:** these arguments are also optional. The columns that are retrieved for each stock are as follows:

![](<Base64-Image-Removed>)

It should be noted that there are six placeholders (_i.e._ **property0** through **property5**), but this does not mean ‘Date’ (0) has to be **property0**, ‘Close’ has to be **property1**_etc_. If any of them are present, only the indicated columns are returned in the order provided. The default settins is 0,1 (_i.e._ ‘Date’ and ‘Close’) if omitted.

You can tell STOCKHISTORY is not yet a “mature” function as Excel Help is a little confused. Presently, it appears you may have 249 properties!

![](<Base64-Image-Removed>)

It should be noted that:

*   the **STOCKHISTORY** function does not stamp a format on the cells that it spills into. If you delete the formula, the cells that it filled have the General format
*   especially if you omit the final comma, the result may not display immediately (for instance, until another action is taken); you may see the _#BUSY!_ message instead. This is not an error (please see **[ERROR.TYPE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-error-dot-type-function)
    ** for more information) – Excel is just busy!
*   when you enter the **property** arguments, you type a number for each property 0 through 5, in the order you want to see them. The value you enter for each property corresponds to the property number. For example, to include Date, Open and Close, enter **0,2,1**
*   date arguments may be a date enclosed in double quotes (_e.g_. “01-01-2020”) or a formula (_e.g._**TODAY()**) or a cell reference to a cell with a date
*   the date returned may be earlier than the date provided. For example, if December 31, 2019 is provided as the start date and interval is monthly, then December 1, 2019 will be returned as that is the start date for the period requested
*   when you use the **Stocks** data type or the **STOCKHISTORY** function to obtain stock prices and other company information, that information is provided by another company. Full details of the third party providers may be found [here](https://support.microsoft.com/en-us/office/about-the-stocks-financial-data-sources-98a03e23-37f6-4776-beea-c5a6c8e787e6)
    .

When first used, you may note the disclaimer above the formula bar, _viz._

![](<Base64-Image-Removed>)

*   the **STOCKHISTORY** function belongs to the **Lookup & Reference** family of functions.

Please see my example below:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Pretty cool, eh?

_Check out our [A to Z of Excel Functions](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
 for other Excel functions and explanations._

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/brand-new-excel-function-stockhistory/#0)
    
*   [Register](https://sumproduct.com/news/brand-new-excel-function-stockhistory/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/brand-new-excel-function-stockhistory/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/brand-new-excel-function-stockhistory/#0)

[](https://sumproduct.com/news/brand-new-excel-function-stockhistory/#0 "close")

top