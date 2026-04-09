# New customers per month - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/new-customers-per-month

---

[Skip to main content](https://exceljet.net/formulas/new-customers-per-month#main-content)

[](https://exceljet.net/formulas/new-customers-per-month#)

*   [Previous](https://exceljet.net/formulas/multiplication-table-formula)
    
*   [Next](https://exceljet.net/formulas/nightly-hotel-rate-calculation)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

New customers per month
=======================

by Dave Bruns · Updated 15 Apr 2019

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

![Excel formula: New customers per month](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/new%20customers%20per%20month.png "Excel formula: New customers per month")

Summary
-------

To count new customers by month, you can use a helper column and the COUNTIFS function. In the example shown, the formula in H5 is:

    =COUNTIFS(new,1,date,">="&G5,date,"<="&EOMONTH(G5,0))
    

where "new" (E5:E15), and "date" (C5:C15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =COUNTIFS(rng1,1,rng2,">="&A1,rng2,"<="&EOMONTH(A1,0))

Explanation 
------------

This formula relies on a helper column, which is column E in the example shown. The formula in E5, copied down, is:

    =(COUNTIFS($B$5:B5,B5)=1)+0
    

This formula returns a 1 for new customers and a 0 for repeat customers, and is [explained in detail here](https://exceljet.net/formulas/customer-is-new)
. Once this formula is in place, the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 can be used to count new customers in each month.

The first range and criteria inside COUNTIFS counts 1's in the "new" column:

    =COUNTIFS(new,1
    

without further criteria, this would return a count of all unique customers in the data. However, we want a count by month, so we need to restrict the count to each month shown in column G.

The month names in column G are actually the "first of month" dates: 1-Jan-2019, 1-Feb-2019, and 1-Mar-2019. The dates are formatted with the [customer number format](https://exceljet.net/articles/custom-number-formats)
 "mmm" to display as 3 letter month names: This allows us to write simple criteria to count by month using the dates directly.

To limit the count to only 1's that are greater than or equal to the first of month in column G we use the named range "date" [concatenated](https://exceljet.net/glossary/concatenation)
 to the greater than or equal to operator:

    =COUNTIFS(new,1,date,">="&G5
    

To limit the count further to include only 1's the occur by the end of each month, we add one last range/criteria pair:

    =COUNTIFS(new,1,date,">="&G5,date,"<="&EOMONTH(G5,0))
    

Here again we use the named range "date", and we concatenate the less than or equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<=) to the last day of the month, created with the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
.

As this formula is copied down, it returns the count of new customers in each month.

### Repeat customers per month

To count repeat customers by month, you can adjust the formula to count zeros instead of 1's. The formula in I5, copied down, is:

    =COUNTIFS(new,0,date,">="&G5,date,"<="&EOMONTH(G5,0))
    

Related formulas
----------------

[![Excel formula: Customer is new](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/customer%20is%20new..png "Excel formula: Customer is new")](https://exceljet.net/formulas/customer-is-new)

### [Customer is new](https://exceljet.net/formulas/customer-is-new)

This formula uses an expanding range for the criteria range inside COUNTIFS: COUNTIFS($B$5:B5,B5) Because the first reference is absolute and the second reference is relative, the range expands as the formula is copied down the column. The criteria is simply the value in the current row of column B...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Flag first duplicate in a list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/flag%20first%20duplicate%20in%20a%20list.png "Excel formula: Flag first duplicate in a list")](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

### [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)

At the core, this formula is composed of two sets of the COUNTIF function wrapped in the IF function . The outer IF + COUNTIF first checks to see if the value in question (B4) appears more than once in the list: =IF(COUNTIF($B$4:$B$11,B4)>1 If not, the outer IF function returns an empty string...

[![Excel formula: Highlight duplicate values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20duplicate%20values.png "Excel formula: Highlight duplicate values")](https://exceljet.net/formulas/highlight-duplicate-values)

### [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)

COUNTIF simply counts the number of times each value appears in the range. When the count is more than 1, the formula returns TRUE and triggers the rule. When you use a formula to apply conditional formatting, the formula is evaluated relative to the active cell in the selection at the time the...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Customer is new](https://exceljet.net/formulas/customer-is-new)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Flag first duplicate in a list](https://exceljet.net/formulas/flag-first-duplicate-in-a-list)
    
*   [Highlight duplicate values](https://exceljet.net/formulas/highlight-duplicate-values)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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