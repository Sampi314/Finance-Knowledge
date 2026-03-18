# Course completion summary with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/course-completion-summary-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/course-completion-summary-with-criteria#main-content)

[](https://exceljet.net/formulas/course-completion-summary-with-criteria#)

*   [Previous](https://exceljet.net/formulas/course-completion-status-summary)
    
*   [Next](https://exceljet.net/formulas/create-array-of-numbers)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Course completion summary with criteria
=======================================

by Dave Bruns · Updated 21 Mar 2017

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Course completion summary with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Course%20completion%20summary%20with%20criteria.png "Excel formula: Course completion summary with criteria")

Summary
-------

This example illustrates one way to summarize course completion data using a criteria, in this case "group". In the example shown, the formula in I4 is:

    =COUNTIFS($B$4:$B$11,$H4,D$4:D$11,"<>")/COUNTIFS($B$4:$B$11,$H4)
    

Generic formula
---------------

    =COUNTIFS(rng1,group,rng2,"<>")/COUNTIFS(rng1,group)

Explanation 
------------

_Note: there are many ways to summarize data with COUNTIFS, SUMIFS, etc. This example shows one specific and arbitrary way. Before you go the formula route, [consider a pivot table first](https://exceljet.net/plc/why-pivot-tables)
, since pivot tables are far simpler to set up and do most of the hard work for you._

The table in B3:F11 is a log of course data where dates in columns D:F indicate course completion. The summary table in H3:K5 summarizes course completion by group instead of user. In this example, group represents the additional criteria.

For Course A, completion by group is calculated with COUNTIFS like this:

    COUNTIFS($B$4:$B$11,$H4,D$4:D$11,"<>")
    

The first range/criteria pair counts only data from the red group by using the group value in H4. The second range/criteria pair counts non-blank entries in column D. The result is a count of all Course A completions for the Red group, 3 in this case.

To generate a total count of people in group Red, in order to calculate percent complete, another COUNTIFS is used:

    COUNTIFS($B$4:$B$11,$H4)
    

The range/criteria pair counts total users in the red group by using the group value in H4, returning 3 in this case.

The result from the first COUNTIFS is divided by the result from the second COUNTIFS, and formatted with the Percentage number format to show percent complete.

Related formulas
----------------

[![Excel formula: Course completion status summary](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/course%20completion%20status%20summary.png "Excel formula: Course completion status summary")](https://exceljet.net/formulas/course-completion-status-summary)

### [Course completion status summary](https://exceljet.net/formulas/course-completion-status-summary)

The table in B3:D11 is a log that shows courses completed by various people. If a course has been completed by a person, there will be an entry in the table with name, course, and date. For the purpose of this example, if we find and entry for a given name/course, we can assume that course is...

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

*   [Course completion status summary](https://exceljet.net/formulas/course-completion-status-summary)
    
*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)
    

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