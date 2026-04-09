# Summary count by month with COUNTIFS - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/summary-count-by-month-with-countifs

---

[Skip to main content](https://exceljet.net/formulas/summary-count-by-month-with-countifs#main-content)

[](https://exceljet.net/formulas/summary-count-by-month-with-countifs#)

*   [Previous](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
    
*   [Next](https://exceljet.net/formulas/summary-count-with-countif)
    

[Count](https://exceljet.net/formulas#Count)

Summary count by month with COUNTIFS
====================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[EDATE](https://exceljet.net/functions/edate-function)

![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")

Summary
-------

To create a summary count by month, you can use the COUNTIFS function and the EDATE function with two criteria. In the example shown, the formula in G5 is:

    =COUNTIFS(dates,">="&F5,dates,"<"&EDATE(F5,1))
    

Generic formula
---------------

    =COUNTIFS(dates,">="&A1,dates,"<"&EDATE(A1,1))

Explanation 
------------

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the [named range](https://exceljet.net/glossary/named-range)
 **dates** for C5:C104 and **priorities** for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month per priority.

We are using the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 to generate a count. The first column of the summary table (F) is a date for the first of each month in 2015. To generate a total count per month, we need to supply criteria that will isolate all the issues that appear in each month.

Since we have actual dates in column F, we can construct the criteria we need using the date itself, and a second date created with the [EDATE function](https://exceljet.net/functions/edate-function)
. These two criteria appear inside COUNTIFS like so:

    dates,">="&F5,dates,"<"&EDATE(F5,1)
    

Roughly translated: "dates greater than or equal to the date in F5 and less than the date in F5 plus one month". This is a convenient way to generate "brackets" for each month based on a single date.

When the formula is copied down column G, COUNTIFS generates the correct count for each month.

Note: if you don't want to see full dates in column F, just apply the [custom date formats](https://exceljet.net/articles/custom-number-formats)
 "mmm" or "mmmm" to display the month names only.

### With Priority

To generate a count by priority, we need to extend criteria. The formula in H5 is:

    =COUNTIFS(dates,">="&$F5,dates,"<"&EDATE($F5,1),priorities,H$4)
    

Here we've added an additional criteria, the named range **priorities** paired with H4 for the criteria itself. In this version of the formula, we get a count by month broken down by the priority, which is picked up directly from the header in row 5. This formula uses both [mixed references](https://exceljet.net/glossary/mixed-reference)
 and [absolute references](https://exceljet.net/glossary/absolute-reference)
 to facilitate copying:

1.  The reference to H4 has the row locked (H$4) so priority doesn't change as the formula is copied down.
2.  The reference to F5 has the column locked ($F5) so the date doesn't change as the formula is copied across.
3.  The named ranges **dates** and **priorities** are automatically absolute.

### Pivot table approach

A pivot table is a [good alternative solution to this problem](https://exceljet.net/pivot-tables/pivot-table-issue-count-by-priority)
. In general, pivot tables are easier and faster to set up when data is well-structured.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")](https://exceljet.net/formulas/count-cells-between-dates)

### [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two named ranges...

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

[![Excel formula: Two-way summary count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Two-way%20summary%20count.png "Excel formula: Two-way summary count")](https://exceljet.net/formulas/two-way-summary-count)

### [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)

In this example, the goal is to count the people shown in the table by both Department (Dept) and Group as shown in the worksheet. A simple way to do this is with the COUNTIFS function. COUNTIFS function The COUNTIFS function is designed to count things based on more than one condition. Conditions...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20build%20a%20simple%20summary%20table-thumb.png)](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

### [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)

In this video, I want to show you how to build a quick summary table using the COUNTIF and SUMIF functions. Here we have a sample set of data that shows t-shirt sales. You can see we have columns for date, item, color, and amount. So let's break this data down by color. Now, before we start, I want...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

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
    
*   [Count cells between dates](https://exceljet.net/formulas/count-cells-between-dates)
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Two-way summary count](https://exceljet.net/formulas/two-way-summary-count)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [EDATE Function](https://exceljet.net/functions/edate-function)
    

### Videos

*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

### Articles

*   [Why Pivot Tables?](https://exceljet.net/plc/why-pivot-tables)
    

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