# Average with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/average-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/average-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/average-top-3-scores)
    
*   [Next](https://exceljet.net/formulas/basic-average-example)
    

[Average](https://exceljet.net/formulas#Average)

Average with multiple criteria
==============================

by Dave Bruns · Updated 18 Jan 2023

Related functions 
------------------

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel formula: Average with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_with_multiple_criteria.png "Excel formula: Average with multiple criteria")

Summary
-------

To average numbers based on multiple criteria, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. In the example shown, the formula in H5 is:

    =AVERAGEIFS(sales,group,F5,region,G5)
    

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. As the formula is copied down, it calculates an average for each group and region in the summary table using the values in columns F and G for criteria.

Generic formula
---------------

    =AVERAGEIFS(values,range1,criteria1,range2,criteria2)

Explanation 
------------

In this example, the goal is to calculate an average for each group and region in the data as shown in the worksheet. For convenience, **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:D16. This problem can be easily solved with the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
. Like the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 and [SUMIFS function](https://exceljet.net/functions/sumifs-function)
, the AVERAGEIFS function is designed to accept _multiple criteria_ entered in \[range, criteria\] pairs. As long as this information is supplied correctly, the behavior of AVERAGEIFS is fully automatic.

Video: [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

### AVERAGEIFS function

The [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
 calculates the average of cells in a [range](https://exceljet.net/glossary/range)
 that meet one or more conditions, referred to as _criteria_. The generic syntax for AVERAGEIFS looks like this:

    =AVERAGEIFS(avg_range,range1,criteria1,range2,criteria2,...)

In this problem, we need to configure AVERAGEIFS to average sales with two criteria:  (1) group and (2) region. We start off with the _average range_, which contains the values to average in column D:

    =AVERAGEIFS(data[Sales],

Next, we need to enter the criteria needed to target the group. The criteria range is **data\[Group\]**. For the criteria, since we already have group names in column F, we will pick up those values directly with a reference to F5:

    =AVERAGEIFS(data[Sales],data[Group],F5,

If we entered this formula as-is, it would calculate an average for group "A", ignoring regions. Next, we need to enter the criteria needed to target the regions. In this case, the criteria range is **data\[Region\]** and the criteria itself comes from cell G5:

    =AVERAGEIFS(data[Sales],data[Group],F5,data[Region],G5)

This is the final formula entered in cell H5. As the formula is copied down, it calculates an average for each group and region in the summary table using the values in columns F and G for criteria.

Related formulas
----------------

[![Excel formula: Average numbers ignore zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_numbers_ignore_zero.png "Excel formula: Average numbers ignore zero")](https://exceljet.net/formulas/average-numbers-ignore-zero)

### [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)

In this example, the goal is to calculate an average of the quiz scores in columns C, D, E, and F for each person. However, the result needs to ignore any zeros that appear in the data. This formula can be easily solved with the AVERAGEIF function or the AVERAGEIFS function . It can also be solved...

[![Excel formula: Average by month](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_month.png "Excel formula: Average by month")](https://exceljet.net/formulas/average-by-month)

### [Average by month](https://exceljet.net/formulas/average-by-month)

In this example, the goal is to calculate a monthly average for the amounts shown in column C using the dates in column B. The article below explains two approaches. One approach is based on the AVERAGEIFS function , which is designed to calculate averages using multiple criteria. The second...

[![Excel formula: Average by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_group.png "Excel formula: Average by group")](https://exceljet.net/formulas/average-by-group)

### [Average by group](https://exceljet.net/formulas/average-by-group)

In this example, the goal is to create a formula that calculates an average by group, using the group names in column C. The solution shown requires three general steps: Create an Excel Table called data List unique groups with the UNIQUE function Calculate averages with the AVERAGEIFS function...

[![Excel formula: Average salary by department](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_salary_by_department.png "Excel formula: Average salary by department")](https://exceljet.net/formulas/average-salary-by-department)

### [Average salary by department](https://exceljet.net/formulas/average-salary-by-department)

In this example, the goal is to create a formula that calculates an average salary by department, where data is an Excel Table in the range B5:D16. The solution shown requires three general steps: Create an Excel Table called data List unique departments with the UNIQUE function Calculate averages...

Related functions
-----------------

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20an%20Excel%20Table-Thumb.png)](https://exceljet.net/videos/how-to-create-an-excel-table)

### [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)

In this video, we'll look at how to create an Excel table. Here we have some data that is a good candidate for a table. Each row represents an entry or record with information that belongs together. Each column has a unique name. The first step in creating a table is to remove any blank rows or...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Average numbers ignore zero](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Average by month](https://exceljet.net/formulas/average-by-month)
    
*   [Average by group](https://exceljet.net/formulas/average-by-group)
    
*   [Average salary by department](https://exceljet.net/formulas/average-salary-by-department)
    

### Functions

*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Videos

*   [How to create an Excel Table](https://exceljet.net/videos/how-to-create-an-excel-table)
    
*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    

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