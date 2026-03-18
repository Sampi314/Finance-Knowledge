# Course completion status summary - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/course-completion-status-summary

---

[Skip to main content](https://exceljet.net/formulas/course-completion-status-summary#main-content)

[](https://exceljet.net/formulas/course-completion-status-summary#)

*   [Previous](https://exceljet.net/formulas/count-with-repeating-values)
    
*   [Next](https://exceljet.net/formulas/course-completion-summary-with-criteria)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Course completion status summary
================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Course completion status summary](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/course%20completion%20status%20summary.png "Excel formula: Course completion status summary")

Summary
-------

To build a summary to show course completion status based on a data log, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 together with the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in G4 is:

    =IF(COUNTIFS(name,$F4,course,G$3),"x","")
    

Generic formula
---------------

    =IF(COUNTIFS(rng1,crit1,rng2,crit2),"x","")

Explanation 
------------

The table in B3:D11 is a log that shows courses completed by various people. If a course has been completed by a person, there will be an entry in the table with name, course, and date. For the purpose of this example, if we find and entry for a given name/course, we can assume that course is complete.

In the summary table in F3 to I7, we have the 4 names that appear in the data log in rows, and 3 courses we want to track as column headers. Note names and courses match entries in the data log exactly.

The core of the formula is the COUNTIFS function, which is configured with 2 range/criteria pairs. The first pair matches on the named range "name" (K5:K11) with criteria coming from $F4 (with column locked to allow the formula to be copied across the table). The second pair matches on the named range "course" (L5:L11) with criteria coming from G$3 (with row locked to allow the formula to be copied down the table).

The COUNTIFS function counts instances of each name and course in the log, using values in the summary table. When a name and course is found, COUNTIFS returns the number 1. When a name and course is not found, COUNTIFS returns zero.

We catch these results with the IF function, where COUNTIFS appears as the logical test. IF will evaluate any positive number as TRUE, and any zero result as FALSE, so we simply provide "x" for value if TRUE and an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for value if false.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

[![Excel formula: Course completion summary with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Course%20completion%20summary%20with%20criteria.png "Excel formula: Course completion summary with criteria")](https://exceljet.net/formulas/course-completion-summary-with-criteria)

### [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)

Note: there are many ways to summarize data with COUNTIFS, SUMIFS, etc. This example shows one specific and arbitrary way. Before you go the formula route, consider a pivot table first , since pivot tables are far simpler to set up and do most of the hard work for you. The table in B3:F11 is a log...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

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
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)
    
*   [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

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