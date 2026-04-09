# Student class enrollment with table - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/student-class-enrollment-with-table

---

[Skip to main content](https://exceljet.net/formulas/student-class-enrollment-with-table#main-content)

[](https://exceljet.net/formulas/student-class-enrollment-with-table#)

*   [Previous](https://exceljet.net/formulas/standard-deviation-calculation)
    
*   [Next](https://exceljet.net/formulas/sum-every-3-cells)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Student class enrollment with table
===================================

by Dave Bruns · Updated 23 Dec 2020

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

![Excel formula: Student class enrollment with table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Student%20class%20enrollment%20tracking.png "Excel formula: Student class enrollment with table")

Summary
-------

To track student class enrollment when classes may appear in any order, you can create a table with additional columns, one for each class, to mark and count enrollment. In the example shown, the formula in G6 is:

    =IF(COUNTIF($C6:$F6,G$5),"x","")
    

Once you have classes marked, you can turn enable an autofilter and then filter on each class as needed to list enrolled students.

Generic formula
---------------

    =IF(COUNTIF(range,class),"x","")

Explanation 
------------

Note the purpose of this example is to how one way to "normalize" data when the order of values is random. There are many ways to approach this problem.

The formula in G6 relies on the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to count the presence of a given class (i.e. "math", art", etc.) in a columns C through F:

    =IF(COUNTIF($C6:$F6,G$5),"x","")
    

Class names are pulled from row 5, and references are mixed to allow the formula to be copied across and down the table.

When COUNTIF finds a class in the range, it returns a positive number . The IF function will evaluate any positive result as TRUE and return "x". If a class isn't found, COUNTIF will return zero and IF will return an [empty string](https://exceljet.net/glossary/empty-string)
 ("").

### Formula to count enrollment

The formula used in row 4 to count students in each class looks like this:

    =COUNTIF(Table1[Math],"x")
    

The structured reference is added automatically in this case since all data is in a table. The equivalent formula without structured references is:

    =COUNTIF(G6:G15,"x")
    

Related formulas
----------------

[![Excel formula: Course completion status summary](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/course%20completion%20status%20summary.png "Excel formula: Course completion status summary")](https://exceljet.net/formulas/course-completion-status-summary)

### [Course completion status summary](https://exceljet.net/formulas/course-completion-status-summary)

The table in B3:D11 is a log that shows courses completed by various people. If a course has been completed by a person, there will be an entry in the table with name, course, and date. For the purpose of this example, if we find and entry for a given name/course, we can assume that course is...

[![Excel formula: Course completion summary with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Course%20completion%20summary%20with%20criteria.png "Excel formula: Course completion summary with criteria")](https://exceljet.net/formulas/course-completion-summary-with-criteria)

### [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)

Note: there are many ways to summarize data with COUNTIFS, SUMIFS, etc. This example shows one specific and arbitrary way. Before you go the formula route, consider a pivot table first , since pivot tables are far simpler to set up and do most of the hard work for you. The table in B3:F11 is a log...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

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
    
*   [Course completion summary with criteria](https://exceljet.net/formulas/course-completion-summary-with-criteria)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    

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