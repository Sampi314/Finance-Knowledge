# Count non-blank cells by category - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-non-blank-cells-by-category

---

[Skip to main content](https://exceljet.net/formulas/count-non-blank-cells-by-category#main-content)

[](https://exceljet.net/formulas/count-non-blank-cells-by-category#)

*   [Previous](https://exceljet.net/formulas/count-missing-values)
    
*   [Next](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria)
    

[Count](https://exceljet.net/formulas#Count)

Count non-blank cells by category
=================================

by Dave Bruns · Updated 21 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Count non-blank cells by category](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20non-blank%20cells%20by%20category.png "Excel formula: Count non-blank cells by category")

Summary
-------

To count non-blank cells by category, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, the formula in G5 is:

    =COUNTIFS(data[Group],F5,data[Done],"<>")
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. As the formula is copied down, it returns a count of non-blank dates by Group as seen in the worksheet.

Generic formula
---------------

    =COUNTIFS(range1,criteria1,range2,"<>")

Explanation 
------------

In this example, the goal is to count non-blank dates in column D by group. All data is an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:D16. This problem can be solved with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, as explained below.

### COUNTIFS function

The Excel COUNTIFS function returns the count of cells that meet one or more criteria. COUNTIFS accepts ranges and criteria in pairs. For example, to count cells in A1:A10 that are equal to "red", you would use COUNTIFS like this:

    =COUNTIFS(A1:A10,"red")
    

To count cells in the range A1:A10 that have a corresponding value in B1:B10 that is greater than 5, you would add another _range/criteria_ pair like this:

    =COUNTIFS(A1:A10,"red",B1:B10,">5")
    

_Note: COUNTIFS is in a group of [8 functions that share a quirky syntax](https://exceljet.net/articles/excels-racon-functions)
._

In the example shown, to count total names by group, we can use COUNTIFS like this:

    =COUNTIFS(data[Group],"A") // returns 5
    

All data is in an [Excel Table](https://exceljet.net/glossary/excel-table)
 called **data** and **data\[Group\]** is a [structured reference](https://exceljet.net/glossary/structured-reference)
 that refers to the entire Group column.

Because there are 5 rows in the table where the group is "A", COUNTIFS returns 5. To extend the formula count names in group "A" where the Date value is not blank, we need to add another _range/criteria_ pair like this:

    =COUNTIFS(data[Group],"A",data[Date],"<>") // returns 4
    

For _range2_, we use **data\[Date\]** and for _criteria2_ we use "<>". The "<>" [operator](https://exceljet.net/glossary/logical-operators)
 means "not equal to" and because we do not provide a value with the operator, it means "not empty". Because there are 4 rows in the table where the group is "A", and the Date is not empty, COUNTIFS returns 4.

To complete the problem, we need to replace the hard-coded "A" in the formula with a reference to cell F5. The final formula in cell G5, copied down, is:

    =COUNTIFS(data[Group],F5,data[Date],"<>")
    

As the formula is copied down, it uses the Group values from column F to return a count of non-blank dates by group.

Related formulas
----------------

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

[![Excel formula: Summary count with percentage breakdown](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20%20couunt%20with%20percentage%20breakdown_0.png "Excel formula: Summary count with percentage breakdown")](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

### [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)

In this example, the goal is to calculate a count and percentage for each category shown in column B. For convenience, the category values in column B are in the named range category (B5:B122). To generate the count, we use the COUNTIF function . The formula in G5, copied through the range G5:G9 is...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

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
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    
*   [Summary count with percentage breakdown](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Videos

*   [How to build a simple summary table](https://exceljet.net/videos/how-to-build-a-simple-summary-table)
    
*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

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