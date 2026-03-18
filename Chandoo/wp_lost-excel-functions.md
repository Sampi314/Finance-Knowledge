# Excel’s Undocumented, Unloved and Rarely used Functions

**Source:** https://chandoo.org/wp/lost-excel-functions

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Lost Excel Functions
====================

*   Last updated on May 18, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

**Undocumented, Unloved and Unused Excel Functions**
----------------------------------------------------

Following on from Chandoo’s [MLookup](http://chandoo.org/wp/2011/04/01/march-2011-is-best-month-ever-and-other-news/ "MLookup")
 function published on 1st April 2011, I thought it might be worth documenting a few undocumented, no-longer documented and rarely used Excel functions.

Although some of the functions below aren’t documented they still work as of Excel 2010.

Users should be cautious with their use going forward as Microsoft may withdraw them from future versions of Excel.

But if you see them appear in older Excel models at least you’ll be the full bottle.

This post will look at the following functions:

*   Datedif
*   Roundup
*   RoundDown
*   Evaluate
*   Convert
*   Roman
*   FactDouble
*   Bahttext

Worked examples of all these functions are presented in the [Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Lost-Excel-Functions.xls "Lost Excel Examples")
 which is compatible with all versions of Excel.

**Datedif**
-----------

The **DATEDIF** function computes the difference between two dates in a variety of different intervals, such number of years, months, or days.

This function is available in all versions of Excel since at least version 5/95, but is documented in the help file only for Excel 2000.

By the way, do not confuse the **DATEDIF** _worksheet_ function with the VBA **DateDiff** function.

### Use:

**\=DATEDIF(Start Date, End Date, Interval)**

Where:  
**Start** **Date** must be less than the **End** **Date.**

**Interval** is the interval type to return.

**Interval** value must be one of the following:

|     |     |     |
| --- | --- | --- |
| **Interval** | **Meaning** | **Description** |
| m   | Months | Complete calendar months between the dates. |
| d   | Days | Number of days between the dates. |
| y   | Years | Complete calendar years between the dates. |
| ym  | Months Excluding Years | Complete calendar months between the dates as if they were of the same year. |
| yd  | Days Excluding Years | Complete calendar days between the dates as if they were of the same year. |
| md  | Days Excluding Years And Months | Complete calendar days between the dates as if they were of the same month and same year. |

If you are including the **Interval** string directly within the formula, you must enclose it in double quotes:

**\=DATEDIF(Date1,Date2,”m”)**

### **Examples:**

|     |     |     |     |
| --- | --- | --- | --- |
|     | **Start Date** | 13/01/1963 |     |
|     | **End Date** | 12/05/2011 |     |
|     |     |     |     |
| Years | \=DATEDIF($B$5,$C$5,”Y”) |     | 48  |
| Months | \=DATEDIF($B$5,$C$5,”M”) |     | 579 |
| Days | \=DATEDIF($B$5,$C$5,”D”) |     | 17651 |
|     |     |     |     |
| Months Exc. Years | \=DATEDIF($B$5,$C$5,”ym”) |     | 3   |
| Days Exc. Years | \=DATEDIF($B$5,$C$5,”yd”) |     | 119 |
| Days Exc. Years & Months | \=DATEDIF($B$5,$C$5,”mD”) |     | 29  |
|     |     |     |     |
| Start Date **\>** End Date | \=DATEDIF($D$5,$D$4,”Y”) |     | #NUM! |

### **Use of the Datedif function on Chandoo.org:**

Datedif has been used a number of times at Chandoo.org

[http://chandoo.org/forums/topic/how-to-calculate-age-from-their-dob](https://chandoo.org/forums/topic/how-to-calculate-age-from-their-dob)

[http://chandoo.org/wp/2009/09/22/elapsed-time-excel/](https://chandoo.org/2009/09/22/elapsed-time-excel/)

[http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/](https://chandoo.org/2008/08/26/date-time-tips-ms-excel/)

**Disclaimer:**

Although the Datedif function above isn’t documented it still works as of Excel 2010. Users should be cautious with their use going forward as Microsoft may withdraw support for them in future Excel versions.

**ROUNDUP() and ROUNDDOWN()**
-----------------------------

The **Roundup** and Rounddown functions rounds a number up or down, away from zero and have pretty much been replaced by the Round function.

### **Use:**

The **Roundup** function rounds a number up, away from zero.

\=ROUNDUP(number, num\_digits)

The **Rounddown** function rounds a number down, towards zero.

\=ROUNDDOWN(number, num\_digits)

**Roundup**() behaves similarly to the **Round**() function, except that it always rounds a number up based on the following rules:

*   If num\_digits is greater than 0, then number is rounded up to the specified number of decimal places.
*   If num\_digits is 0 or omitted, then number is rounded up to the nearest integer.
*   If num\_digits is less than 0, then number is rounded up to the left of the decimal point.

### **Examples:**

ROUNDUP(4.1,0) equals 5

ROUNDUP(106.9,0) equals 107

ROUNDUP(3.14159, 3) equals 3.142

ROUNDUP(-3.14159, 1) equals -3.2

ROUNDUP(31415.926, -2) equals 31500  
**Rounddown**() behaves similarly to the **Round**() function, except that it always rounds a number down based on the following rules:

*   If num\_digits is greater than 0, then number is rounded down to the specified number of decimal places.
*   If num\_digits is 0 or omitted, then number is rounded down to the nearest integer.
*   If num\_digits is less than 0, then number is rounded down to the left of the decimal point.

### **Examples:**

ROUNDDOWN(4.1, 0) equals 4

ROUNDDOWN(106.9,0) equals 106

ROUNDDOWN(3.14159, 3) equals 3.141

ROUNDDOWN(-3.14159, 1) equals -3.1

ROUNDDOWN(31415.92654, -2) equals 31400

### **Use on the Roundup and Rounddown functions on Chandoo.org:**

The Roundup and Rounddown functions have been used several times at Chandoo.org

**Roundup**

[http://chandoo.org/wp/2010/04/29/quarterly-totals-from-monthly-data/](https://chandoo.org/2010/04/29/quarterly-totals-from-monthly-data/)

[http://chandoo.org/wp/2010/04/30/quarterly-totals-multi-year-data/](https://chandoo.org/2010/04/30/quarterly-totals-multi-year-data/)

**Rounddown**

[http://chandoo.org/wp/2010/04/30/quarterly-totals-multi-year-data/](https://chandoo.org/2010/04/30/quarterly-totals-multi-year-data/)

[http://chandoo.org/wp/2009/07/06/excel-formulas-round-sort/](https://chandoo.org/2009/07/06/excel-formulas-round-sort/)

**Evaluate**
------------

Evaluate is an Excel ver 4.0 macro function which is still supported and functional in Excel 2010.

The Evaluate function allows for the evaluation of a text equation as an algebraic equation.

The evaluate function cannot be used as a spreadsheet function but can be used in Named Ranges.

It is probably best described by example; **Evaluate 1**, from the Example File.

### **Example:**

Say you have a polynomial equation in a cell as Text **A1: ‘=X2 + 5\*Y – Z**

Setup 3 named ranges, X, Y , Z with values X=10, Y=5 and Z=3

You can use Evaluate in a a Named Range eg: **Result =Evaluate(SheetName!$A$1)**

And then on a worksheet **\=Result**, which will return the answer **122** = **102 + 5\*5 – 3**

Evaluate can be used to allow graphing of equations without use of worksheet functions or even worksheet ranges, an example of each is shown in the examples file as **Evaluate 2** and **Evaluate 3** .

Evaluate 2: Uses a Range as the X Values and a Named Range using the Evaluate function as the calculated Y Values

Evaluate 3: Uses Named Ranges as the X Values and as the calculated Y Values based on an Evaluate function

[![](https://chandoo.org/wp/wp-content/uploads/2011/05/Evaluate-Pic.png "Evaluate-Pic")](https://chandoo.org/wp/wp-content/uploads/2011/05/Evaluate-Pic.png)

**Use of the Evaluate function on Chandoo.org:**

Not Used

**Convert**
-----------

Converts a number from one measurement system to another.

For example, CONVERT can translate a table of distances in Kilometres to a table of distances in Miles.

Convert includes 49 units spread amongst the following 10 categories

|     |     |
| --- | --- |
| **Category** | **No Units** |
| Weights & Mass, | 5   |
| Time | 5   |
| Force | 3   |
| Power | 2   |
| Temperature | 3   |
| Distance | 8   |
| Pressure | 3   |
| Energy | 9   |
| Magnetism | 2   |
| Liquid Measures | 9   |

### **Use:**

**\=Convert**(**number**, From Unit, To Unit)

A list of all the Conversion Units and Conversion Prefixes is included on the Conversion Factors tab of the Examples File.

### **Examples:**

|     |     |     |
| --- | --- | --- |
| **Example** | **Result** | **Description (Result)** |
| \=CONVERT(5, “lbm”, “kg”) | 2.27 | Converts a 5 pound mass to kilograms (2.267) |
| \=CONVERT(80, “F”, “C”) | 6.67 | Converts 80 degrees Fahrenheit to Celsius (26.6) |
| \=CONVERT(1, “ft”, “kg”) | #N/A | Data types are not the same so an error is returned (#N/A) |
| ‘=CONVERT(CONVERT(100,”ft”,”m”),”ft”,”m”) | 9.29 | Converts 100 square feet into square meters (9.290304). |

A list of all the Conversion Units and Conversion Prefixes is included on the Conversion Factors tab of the Examples File.

### **Use of the Convert function on Chandoo.org**

[http://chandoo.org/forums/topic/convert-function](http://chandoo.org/forums/topic/convert-function "Convert Function Use")

**Roman**
---------

The Roman function converts a number to Roman format.

### **Use:**

**\=ROMAN**(**number**, form)

**\=ROMAN**(45 ) = XLV

**Form** is a number specifying the type of roman numeral you want. The roman numeral style ranges from Classic to Simplified, becoming more concise as the value of form increases.

|     |     |
| --- | --- |
| **Form** | **Type** |
| 0 or omitted | Classic. |
| 1   | More concise. See example below. |
| 2   | More concise. See example below. |
| 3   | More concise. See example below. |
| 4   | Simplified. |
| TRUE | Classic. |
| FALSE | Simplified. |

### **Example:**

|     |     |     |     |
| --- | --- | --- | --- |
| **Example** |     | **Formula** | **Description (Result)** |
| \=ROMAN(2011) |     | MMXI | Converts 2011 to Roman (MMXI) |
| \=ROMAN(499,0) | Classic or Omited | CDXCIX | Converts 499 to Roman (CDXCIX) |
| \=ROMAN(499, True) | Classic | CDXCIX | Converts 499 to Roman (CDXCIX) |
| \=ROMAN(499,1) | More Concise | LDVLIV | Converts 499 to Roman (LDVLIV) |
| \=ROMAN(499,2) | More Concise | XDIX | Converts 499 to Roman (XDIX) |
| \=ROMAN(499,3) | More Concise | VDIV | Converts 499 to Roman (VDIV) |
| \=ROMAN(499,4) | Simplified | ID  | Converts 499 to Roman (ID) |
| \=ROMAN(499, False) | Simplified | ID  | Converts 499 to Roman (ID) |

### **Use of the Roman function on Chandoo.org:**

Nil

**Factdouble**
--------------

Factdouble returns the double factorial of a number and is expressed in mathematics as n!!

Double factorials are used in probability theory and other higher levels of mathematics and is really just a way to simplify an otherwise complex expression

If the number is Even **Factdouble** = n(n-2)(n-4)…(4)(2)

If the number is Odd **Factdouble** = n(n-2)(n-4)…(3)(1)

So it is simpler to write 10!! than 10x8x6x4x2

### **Use:**

**\=Factdouble**( **number** )

### **Example:**

|     |     |     |
| --- | --- | --- |
| **Example** | **Result** | **Description (Result)** |
| \=Factdouble(8) | 384 | Factdouble of 8 = 8x6x4x2 = 384 |
| \=Factdouble(9) | 945 | Factdouble of 9 = 9x7x5x3x1 = 945 |

### **Use of the Factdouble function on Chandoo.org**

Not used

**Bahttext**
------------

Converts a number to Thai Text represention of the number

****Use:****

**\=Battext( Number)**

### **Example:**

\=**Bahttext(250)** , Returns [![](https://chandoo.org/wp/wp-content/uploads/2011/05/Bahttext.png "Bahttext")](https://chandoo.org/wp/wp-content/uploads/2011/05/Bahttext.png)

### **Use of the Bahttext function on Chandoo.org:**

Not used

Examples
--------

An example file with worked examples from all the above functions is available from the following link; [Example File](https://chandoo.org/wp/wp-content/uploads/2011/05/Lost-Excel-Functions.xls "Example File")

The file is compatible with all Excel versions.

**What Functions Have You Discovered?**
---------------------------------------

What Functions Have You Stumbled Onto?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [40 Comments](https://chandoo.org/wp/lost-excel-functions/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/lost-excel-functions/#respond)
    
*   Tagged under [Convert](https://chandoo.org/wp/tag/convert/)
    , [Datedif](https://chandoo.org/wp/tag/datedif/)
    , [Evaluate](https://chandoo.org/wp/tag/evaluate/)
    , [FactDouble](https://chandoo.org/wp/tag/factdouble/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [Roman](https://chandoo.org/wp/tag/roman/)
    , [rounddown()](https://chandoo.org/wp/tag/rounddown/)
    , [roundup](https://chandoo.org/wp/tag/roundup/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousIntroduction to Programming – Demo Lesson from our VBA Class](https://chandoo.org/wp/introduction-to-programming/)

[NextCount-down Timer App in VBA to Remind you about the VBAClasses Closing Time!!!Next](https://chandoo.org/wp/vba-classes-countdown-timer/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/lost-excel-functions/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/lost-excel-functions/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/lost-excel-functions/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ