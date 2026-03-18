# Average salary by department - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/average-salary-by-department

---

[Skip to main content](https://exceljet.net/formulas/average-salary-by-department#main-content)

[](https://exceljet.net/formulas/average-salary-by-department#)

*   [Previous](https://exceljet.net/formulas/average-numbers-ignore-zero)
    
*   [Next](https://exceljet.net/formulas/average-top-3-scores)
    

[Average](https://exceljet.net/formulas#Average)

Average salary by department
============================

by Dave Bruns · Updated 28 Feb 2023

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[AVERAGEIFS](https://exceljet.net/functions/averageifs-function)

![Excel formula: Average salary by department](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/average_salary_by_department.png "Excel formula: Average salary by department")

Summary
-------

To calculate the average salary by department with a formula, you can use the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
 connected to the [spill range](https://exceljet.net/glossary/spill-range)
 returned by UNIQUE. In the example shown, the formula in cell G5 is:

    =AVERAGEIFS(data[Salary],data[Department],F5#)

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. The result from AVERAGEIFS [spills](https://exceljet.net/glossary/spill)
 into the range G5:G7. 

_Note: [Dynamic Array Formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 are available in [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021. In older versions you can manually enter the department names in F5:F9 and use the standard AVERAGEIFS formula explained below._

Generic formula
---------------

    =AVERAGEIFS(avg_range,criteria_range,criteria)

Explanation 
------------

In this example, the goal is to create a formula that calculates an average salary by department, where **data** is an Excel Table in the range B5:D16. The solution shown requires three general steps:

1.  Create an [Excel Table](https://exceljet.net/glossary/excel-table)
     called **data**
2.  List unique departments with the [UNIQUE function](https://exceljet.net/functions/unique-function)
    
3.  Calculate averages with the [AVERAGEIFS function](https://exceljet.net/functions/averageifs-function)
    

### Create the Excel Table

One of the key features of an [Excel Table](https://exceljet.net/articles/excel-tables)
 is its ability to dynamically resize when rows are added or removed. To create a table, place the cursor in the data and use the [keyboard shortcut Control + T](https://exceljet.net/shortcuts/insert-table)
. Then name the table "data".

Video: [How to create an Excel table](https://exceljet.net/videos/how-to-create-an-excel-table)

The table will now automatically expand or contract when new data is added or removed.

### List unique departments

The next step is to list unique department names starting in cell F5. For this we use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 like this:

    =UNIQUE(data[Department]) // unique departments
    

The result from UNIQUE is an [array](https://exceljet.net/glossary/array)
 with 5 values like this:

    {"Marketing";"IT";"Finance";"HR";"Sales"}

This array lands as a [spill range](https://exceljet.net/glossary/spill-range)
 in cell F5 and lists all of the unique department names in the Department column of the table. Note the UNIQUE function will continue to return a current list of unique departments when data changes.

Video: [Intro to the UNIQUE function](https://exceljet.net/videos/the-unique-function)

Video: [What is an array](https://exceljet.net/videos/what-is-an-array)
?

### Calculate average

We now have what we need to calculate the average for each department. To do this, we only need one condition: the department name. A good way to do this is to use the AVERAGEIFS function, which can calculate averages based on one or more criteria. Because we already have unique departments in column F, we can reference the list directly. The formula in G5 is:

    =AVERAGEIFS(data[Salary],data[Department],F5#)
    

The first [argument](https://exceljet.net/glossary/function-argument)
 in AVERAGEIFS is _average\_range_. This is the range that contains numbers to average. In this example, this is the Salary column in the table:

    =AVERAGEIFS(data[Salary],

The next two arguments specify the criteria. The _criteria range_ is **data\[Department\]**, and the _criteria_ is the [spill range](https://exceljet.net/glossary/spill-range)
:

    =AVERAGEIFS(data[Salary],data[Department],F5#)
    

Because the spill range F5# contains 5 values, the AVERAGEIFS function returns 5 averages in an array like this:

    {53333.3333333333;68500;71000;43500;59000}

Each number in the array is the average calculated for a given department. These values [spill](https://exceljet.net/videos/spilling-and-the-spill-range)
 into the range G5:G7.

### When data changes

The key advantage to using a Excel table with the UNIQUE function is that the formula responds instantly to changes in the data. If new rows are added that refer to _existing_ departments, the [spill range](https://exceljet.net/glossary/spill-range)
 returned by UNIQUE remains unchanged, and AVERAGEIFS calculates a new set of averages. If new rows are added that include _new_ departments, or if existing departments values are changed, these changes are captured by the UNIQUE function, which expands the spill range in F5 as needed. If rows are deleted from the table, the spill range contracts as needed. In all cases, the spill range represents the current list of unique departments, and the AVERAGEIFS function uses this list to calculate averages.

### Legacy Excel

In older versions of Excel without the UNIQUE function, the approach needs to be modified slightly. Instead of using the UNIQUE function to automatically extract unique departments, the departments can be entered manually. Then the formula in G5 becomes:

    =AVERAGEIFS(data[Salary],data[Department],F5)

Note the criteria is no longer a spill range. This formula can then be copied down to return an average for each department.

_Note: there are ways to [extract unique values in older versions of Excel,](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
 but they are more complicated._

### Pivot Table option

A [pivot table](https://exceljet.net/articles/excel-pivot-tables)
 would also be a [good way to solve this problem](https://exceljet.net/pivot-tables/pivot-table-two-way-average)
, and would provide additional features. However, one drawback is that pivot tables need to be refreshed to show the latest data. Formulas, on the other hand, update instantly when data changes.

Related formulas
----------------

[![Excel formula: Dynamic two-way count](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20count.png "Excel formula: Dynamic two-way count")](https://exceljet.net/formulas/dynamic-two-way-count)

### [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)

In this example, the goal is to create a formula that performs a dynamic two-way count of all color and size combinations in the range B5:D16. The solution shown requires four general steps: Create an Excel Table called data List unique colors with UNIQUE function List unique sizes with UNIQUE...

[![Excel formula: Dynamic two-way sum](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20two%20way%20sum.png "Excel formula: Dynamic two-way sum")](https://exceljet.net/formulas/dynamic-two-way-sum)

### [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)

In this example, the goal is to create a formula that performs a dynamic two-way sum of all City and Size combinations in the range B5:D17 . The solution shown requires four basic steps: Create an Excel Table called data List unique cities with the UNIQUE function List unique sizes with the UNIQUE...

[![Excel formula: Average by group](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/average_by_group.png "Excel formula: Average by group")](https://exceljet.net/formulas/average-by-group)

### [Average by group](https://exceljet.net/formulas/average-by-group)

In this example, the goal is to create a formula that calculates an average by group, using the group names in column C. The solution shown requires three general steps: Create an Excel Table called data List unique groups with the UNIQUE function Calculate averages with the AVERAGEIFS function...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel AVERAGEIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_averageifs.png "Excel AVERAGEIFS function")](https://exceljet.net/functions/averageifs-function)

### [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)

The Excel AVERAGEIFS function returns the average of cells that meet multiple conditions, referred to as criteria. To define criteria, AVERAGEIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20AVERAGEIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-averageifs-function)

### [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)

In this video we'll look at how to use the AVERAGEIFS function to calculate an average from numbers that meet multiple criteria. Here we have a list of 16 properties with prices and other information. Let's calculate some averages based on the criteria shown in column K. Note that this data already...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20UNIQUE%20function-Play.png)](https://exceljet.net/videos/the-unique-function)

### [The UNIQUE function](https://exceljet.net/videos/the-unique-function)

In this video, we'll introduce the UNIQUE function . One of the new functions that comes with the dynamic array version of Excel is UNIQUE. The UNIQUE function lets you extract unique values in a variety of ways. The UNIQUE function takes three arguments. The first argument, array is the source...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic two-way count](https://exceljet.net/formulas/dynamic-two-way-count)
    
*   [Dynamic two-way sum](https://exceljet.net/formulas/dynamic-two-way-sum)
    
*   [Average by group](https://exceljet.net/formulas/average-by-group)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [AVERAGEIFS Function](https://exceljet.net/functions/averageifs-function)
    

### Videos

*   [How to use the AVERAGEIFS function](https://exceljet.net/videos/how-to-use-the-averageifs-function)
    
*   [The UNIQUE function](https://exceljet.net/videos/the-unique-function)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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