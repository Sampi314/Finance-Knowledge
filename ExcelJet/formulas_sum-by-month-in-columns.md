# Sum by month in columns - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-by-month-in-columns

---

[Skip to main content](https://exceljet.net/formulas/sum-by-month-in-columns#main-content)

[](https://exceljet.net/formulas/sum-by-month-in-columns#)

*   [Previous](https://exceljet.net/formulas/sum-by-month-ignore-year)
    
*   [Next](https://exceljet.net/formulas/sum-by-quarter)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum by month in columns
=======================

by Dave Bruns · Updated 19 Jun 2024

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: Sum by month in columns](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_by_month_in_columns.png "Excel formula: Sum by month in columns")

Summary
-------

To sum by month in columns you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 together with the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. In the example shown, the formula in G5 is:

    =SUMIFS(amount,client,$F5,date,">="&G$4,date,"<="&EOMONTH(G$4,0))
    

where **amount** (D5:D16), **client** (B5:B16), and **date** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Explanation 
------------

In this example, the goal is to construct a formula that will subtotal the amounts in column D by client and month as seen in the range G5:I8. A big part of the problem is to set up the proper references so that the formula can be entered once, and copied throughout G5:I8. The solution explained below is based on the SUMIFS function.

### Summary table setup

The first step in solving this problem is creating the summary table seen in the range F4:I8.  The values in F4:F9 are text values. However, the month names in G4:I5 are actually valid [Excel dates](https://exceljet.net/glossary/excel-date)
, formatted with the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmm":

![The month names in the summary table are actually dates](https://exceljet.net/sites/default/files/images/formulas/inline/sum%20by%20month%20in%20columns%20summary%20table%20setup.png "The month names in the summary table are actually dates")

### SUMIFS solution

The [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 can sum values in ranges based on multiple criteria. Multiple criteria are entered in range/criteria pairs like this:

    =SUMIFS(sum_range,range1,criteria1,range2,criteria2,...)
    

To sum amounts by client and month with SUMIFS, we will need to enter three criteria

1.  Client = client in column F
2.  Date >= first of month (from date in row 4)
3.  Date <= end of month (from date in row 4)

The first step in configuring SUMIFS is to enter the _sum\_range_, which contains the values to sum in column D. For _sum\_range_, we use the named range **amount**:

    =SUMIFS(amount
    

Next, we need to enter the first range/criteria pair to target values in column B:

    =SUMIFS(amount,client,$F5
    

Notice F5 is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
, with the column locked and the row relative. This allows the row to change as the formula is copied down the table, but the client name in column F does not change as the formula is copied to the right.

Next, we need to enter the second range/criteria pair, which is used to target dates that are greater than or equal to the month in G4. For the range, we use the named range **date**. For criteria, we use the greater than or equal to (>=) [operator](https://exceljet.net/glossary/logical-operators)
 [concatenated](https://exceljet.net/articles/how-to-concatenate-in-excel)
 to the value in G4:

    =SUMIFS(amount,client,$F5,date,">="&G$4
    

Notice G$4 this is another mixed reference, this time with the row locked. This allows the column to change as the formula is copied across the table, but keeps the row number fixed as the formula is copied down. The [concatenation](https://exceljet.net/glossary/concatenation)
 with an ampersand (&) is necessary when building [criteria](https://exceljet.net/articles/how-to-use-formula-criteria)
 that use a logical operator and a value from another cell, because the SUMIFS function is in a [group of eight functions](https://exceljet.net/articles/excels-racon-functions)
 that split criteria into two parts.

Finally, we need to enter the third range/criteria pair to check dates against the last day of the month. For the range, we again use the named range **date**. For criteria, we use the less than or equal to (<=) operator [concatenated](https://exceljet.net/glossary/concatenation)
 to the EOMONTH function:

    =SUMIFS(amount,client,$F5,date,">="&G$4,date,"<="&EOMONTH(G$4,0))
    

We use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
 to get the last day of the month of the date in G4. As before, we need to concatenate the result from EOMONTH to the logical operator. Again, the reference to G$4 is mixed to keep the row from changing.

As the formula is copied into the range G5:I8, the SUMIFS function returns a sum for each client and month.

### Pivot Table solution

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would be an excellent solution for this problem, because it can automatically group by month without any formulas at all. For a side-by-side comparison of formulas vs. pivot tables, see this video: [Why pivot tables](https://exceljet.net/plc/why-pivot-tables)
.

Related formulas
----------------

[![Excel formula: Sum by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_by_month.png "Excel formula: Sum by month")](https://exceljet.net/formulas/sum-by-month)

### [Sum by month](https://exceljet.net/formulas/sum-by-month)

In this example, the goal is to sum the amounts shown in column C by month using the dates in column B. The article below explains two approaches. One approach is based on the SUMIFS function , which can sum numeric values based on multiple criteria. The second approach is based on the SUMPRODUCT...

[![Excel formula: Sum by year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20year.png "Excel formula: Sum by year")](https://exceljet.net/formulas/sum-by-year)

### [Sum by year](https://exceljet.net/formulas/sum-by-year)

In this example, the goal is to calculate a total for each year that appears in column F. All data is in an Excel Table called data in the range B5:D16. The main challenge is that we have dates in column B, but we don't have separate year values to work with. The simplest way to solve this problem...

[![Excel formula: Sum by week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20week.png "Excel formula: Sum by week")](https://exceljet.net/formulas/sum-by-week)

### [Sum by week](https://exceljet.net/formulas/sum-by-week)

In this example, the goal is to sum the amounts in column C by week, using the dates in the range E5:E10 which are all Mondays. All data is in an Excel Table named data in the range B5:C16. This problem can be solved in a straightforward way with the SUMIFS function . In the current version of...

[![Excel formula: Sum by month ignore year](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20month%20ignore%20year.png "Excel formula: Sum by month ignore year")](https://exceljet.net/formulas/sum-by-month-ignore-year)

### [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)

In this example, the goal is to sum numeric values by month while ignoring the year that contains the date. The solution below is based on the SUMPRODUCT function, the MONTH function, and Boolean algebra . For convenience, amount (C5:C16) and date (B5:B16) are named ranges . Basic concept The basic...

[![Excel formula: Get month name from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20month%20name%20from%20date_0.png "Excel formula: Get month name from date")](https://exceljet.net/formulas/get-month-name-from-date)

### [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)

In this example, the goal is to get and display the month name from any given date. There are several ways to go about this in Excel, depending on whether you want to extract the month name as text, or just display a valid Excel using the month name. To extract the month name from a date as text ,...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum by month](https://exceljet.net/formulas/sum-by-month)
    
*   [Sum by year](https://exceljet.net/formulas/sum-by-year)
    
*   [Sum by week](https://exceljet.net/formulas/sum-by-week)
    
*   [Sum by month ignore year](https://exceljet.net/formulas/sum-by-month-ignore-year)
    
*   [Get month name from date](https://exceljet.net/formulas/get-month-name-from-date)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    
*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    

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