# Summary count with percentage breakdown - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/summary-count-with-percentage-breakdown

---

[Skip to main content](https://exceljet.net/formulas/summary-count-with-percentage-breakdown#main-content)

[](https://exceljet.net/formulas/summary-count-with-percentage-breakdown#)

*   [Previous](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Next](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Summary count with percentage breakdown
=======================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")

Summary
-------

To generate a count by category with a percentage breakdown, you can use the [COUNTIF function](https://exceljet.net/functions/countif-function)
 together with the [COUNTA function](https://exceljet.net/functions/counta-function)
. In the example shown, the formula in H5 is:

    =COUNTIF(category,F5)/COUNTA(category)
    

where **category** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B122. The results in column H are decimal values with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

Generic formula
---------------

    =COUNTIF(range,criteria)/COUNTA(range)

Explanation 
------------

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the [named range](https://exceljet.net/glossary/named-range)
 **category** (B5:B122). To generate the count, we use the [COUNTIF function](https://exceljet.net/functions/countif-function)
. The formula in G5, copied through the range G5:G9 is:

    =COUNTIF(category,F5)
    

The _range_ is the [named range](https://exceljet.net/glossary/named-range)
 **category** (B5:B122), and the _criteria_ as is supplied as a reference to F5, which simply picks up the text value in column F. As the formula is copied down, it returns the count of each category listed F5:F9. 

To calculate the percentage shown in column H, we need to divide the count per category by the total count. The formula in H5 is:

    =COUNTIF(category,F5)/COUNTA(category)
    

On the left, COUNTIF is configured as explained above. On the right, we use COUNTA to count total values in the named range **category** (B5:B122) to generate a total count. The formula is evaluated like this:

    =COUNTIF(category,F5)/COUNTA(category)
    =41/118
    =0.3475
    

The results in column H are decimal values formatted with the [Percentage" number format](https://exceljet.net/glossary/percentage-number-format)
.

_Note: since we already have a count per category in column G, it would be more efficient to pick that count in this formula instead of recalculating the same count again in column H. However, COUNTIFS and COUNTA are shown together here as a standalone solution._

### Formatting percentages in Excel

In mathematics, a percentage is a number expressed as a fraction of 100. For example, 65% is read as "Sixty-five percent" and is equivalent to 65/100 or 0.65. Accordingly, the values in column H are _decimal values_, with the [Percentage number format](https://exceljet.net/glossary/percentage-number-format)
 applied.

### Pivot table option

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be a good way to solve this problem.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Project complete percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/project%20complete%20percentage_0.png "Excel formula: Project complete percentage")](https://exceljet.net/formulas/project-complete-percentage)

### [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)

In this example if a task is marked "Done", then it is considered complete. The goal is to calculate the percent complete for the project by showing the ratio of complete tasks to total tasks, expressed as a percentage. The formula in F6 is: =COUNTA(C5:C11)/COUNTA(B5:B11) At the core, this formula...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Project complete percentage](https://exceljet.net/formulas/project-complete-percentage)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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