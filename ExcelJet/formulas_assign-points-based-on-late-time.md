# Assign points based on late time - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/assign-points-based-on-late-time

---

[Skip to main content](https://exceljet.net/formulas/assign-points-based-on-late-time#main-content)

[](https://exceljet.net/formulas/assign-points-based-on-late-time#)

*   [Previous](https://exceljet.net/formulas/add-years-to-date)
    
*   [Next](https://exceljet.net/formulas/basic-timesheet-formula-with-breaks)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Assign points based on late time
================================

by Dave Bruns · Updated 1 Sep 2019

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[VALUE](https://exceljet.net/functions/value-function)

![Excel formula: Assign points based on late time](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/assign%20penalty%20points%20based%20on%20late%20time2.png "Excel formula: Assign points based on late time")

Summary
-------

To assign penalty points based on an amount of time late, you can use a nested IF formula.In the example shown, the formula in E5 is:

    =
    IF(D5<VALUE("0:05"),0,
    IF(D5<VALUE("0:15"),1,
    IF(D5<VALUE("0:30"),2,
    IF(D5<VALUE("0:60"),3,
    IF(D5<VALUE("4:00"),4,
    5)))))
    

Note: [line breaks added for readability](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
.

Generic formula
---------------

    =
    IF(time<VALUE("0:05"),0,
    IF(time<VALUE("0:15"),1,
    IF(time<VALUE("0:30"),2,
    IF(time<VALUE("0:60"),3,
    IF(time<VALUE("4:00"),4,
    5)))))

Explanation 
------------

This formula is a classic example of a nested IF formula that tests threshold values in ascending order. To match the schedule shown in G5:G11, the formula first checks the late by time in D5 to see if it's less than 5 minutes. If so, zero points are assigned:

    IF(D5<VALUE("0:05"),0,
    

If the result of the logical test above is FALSE, the formula checks to see if D5 is less than the next threshold, which is 15 minutes:

    IF(D5<VALUE("0:15"),1,
    

The same pattern repeats at each threshold. Because the tests are run in order, from smallest to largest, there is no need for more complicated bracketing.

The [VALUE function](https://exceljet.net/functions/countifs-function)
 is used to make Excel treat time value at each threshold as a number instead of next.

_Note: you can also [use VLOOKUP to replace nested IFs](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
 if you like._

Related formulas
----------------

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

[![Excel formula: Invoice age and status](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/invoice_age_and_status.png "Excel formula: Invoice age and status")](https://exceljet.net/formulas/invoice-age-and-status)

### [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)

The goal is to calculate the correct invoice status ("OK", "Paid", or "Overdue") using the following rules: If there is an "x" in the "Paid" column, return "Paid". If there is not an "x" in the "Paid" column, and if the age is less than 31 days, return "OK" If there is not an "x" in the "Paid"...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20formula%20with%20nested%20IFs-thumb.png)](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

### [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)

In this video I'll show you how to create a formula that uses multiple, nested IF statements. This is a common technique to handle multiple conditions. Let's take a look. This worksheet shows a class of students with five test scores in columns D through H, and an average in column I. In column J...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20make%20a%20nested%20IF%20formula%20easier%20to%20read.png)](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

### [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)

In this video we're going to look at how to make a nested IF formula more readable by adding line breaks. Here I have a worksheet that calculates sales commissions based on the commission structure shown in the table. For example, we can see that King sold $124,500 and gets a commission of 5%,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)
    
*   [Invoice age and status](https://exceljet.net/formulas/invoice-age-and-status)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [VALUE Function](https://exceljet.net/functions/value-function)
    

### Videos

*   [How to create a formula with nested IFs](https://exceljet.net/videos/how-to-create-a-formula-with-nested-ifs)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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