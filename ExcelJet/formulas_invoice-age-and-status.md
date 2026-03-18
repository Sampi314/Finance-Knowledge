# Invoice age and status - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/invoice-age-and-status

---

[Skip to main content](https://exceljet.net/formulas/invoice-age-and-status#main-content)

[](https://exceljet.net/formulas/invoice-age-and-status#)

*   [Previous](https://exceljet.net/formulas/if-with-wildcards)
    
*   [Next](https://exceljet.net/formulas/nested-if-function-example)
    

[If](https://exceljet.net/formulas#If)

Invoice age and status
======================

by Dave Bruns · Updated 2 Aug 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[TODAY](https://exceljet.net/functions/today-function)

![Excel formula: Invoice age and status](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/invoice_age_and_status.png "Excel formula: Invoice age and status")

Summary
-------

To calculate age and invoice status ("OK", "Paid", "Overdue") you can use a simple nested IF formula. In the example shown, the formula in G5 is:

    =IF(F5="x","Paid",IF(E5<31,"OK","Overdue"))
    

As the formula is copied down, it returns "Paid" if there is an "x" in the "Paid" column. If there the invoice is not paid, the formula returns "OK" if the age is less than 31 days and "Overdue" if not.

Generic formula
---------------

    =IF(A1="x","Paid",IF(B1<31,"OK","Overdue"))

Explanation 
------------

The goal is to calculate the correct invoice status ("OK", "Paid", or "Overdue") using the following rules:

1.  If there is an "x" in the "Paid" column, return "Paid".
2.  If there is not an "x" in the "Paid" column, and if the age is less than 31 days, return "OK"
3.  If there is not an "x" in the "Paid" column, and if the age is not less than 31 days, return "Overdue"

This problem can be solved by nesting one IF function inside another.

### Calculating age

To calculate invoice age in days, the formula in cell E5, copied down, uses the [TODAY function](https://exceljet.net/functions/today-function)
:

    =TODAY()-C5

This works because [Excel dates](https://exceljet.net/glossary/excel-date)
 are just serial numbers. At the time of this writing, the date is May 20, 2023. In Excel's date system, this is the number 45066. The due date of March 30, 2023, is the number 45015. Excel evaluates the formula above like this:

    =TODAY()-C5
    =45066-45015
    =51

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 in Excel runs a test, then performs one action if the result is TRUE, and a different action if the result is FALSE. The generic syntax for IF looks like this:

    =IF(test,true_result,false_result)

The first [argument](https://exceljet.net/glossary/function-argument)
 is the logical test, and the second argument is the result (or calculation) to return when the test is TRUE. The third argument is the "else" — the value or calculation to return if the result of the logical test is FALSE.

### IF paid

In the example shown, the first thing to check is if the invoice has been paid or not. We do this by checking the Paid column for an "x" as seen below. Notice that both "x" and "Paid" are enclosed in double quotes because they are text values:

    =IF(F5="x","Paid")

Translation: _If F5 equals "x", return "Paid"._

At this point, we have not provided anything for the value if false. This means the IF function will return FALSE when F5 is empty. If this was the only thing we were checking, we might want to provide an [empty string](https://exceljet.net/glossary/empty-string)
 ("") like this:

    =IF(F5="x","Paid","")

In Excel, an empty string will not display anything. It will look like an empty cell.

### IF overdue

The remaining task is to check the age of the invoice. To extend the formula to check for an overdue status, we use another IF formula like this:

    IF(E5<31,"OK","Overdue")

Translation: _If E5 is less than 31, return "OK", else return "Overdue"._

Notice the value 31 is a number and, therefore, not enclosed in quotes. This formula will return "OK" for any age below 31 and "Overdue" for any age over 30. This number can be customized as desired.

The final step in the problem is to combine the two IF formulas above. We do this by starting off with the first IF:

    =IF(F5="x","Paid")

Then we extend the formula by nesting the second IF inside the first IF:

    =IF(F5="x","Paid",IF(E5<31,"OK","Overdue"))

Translation: If F5 equals "x", return "Paid". Else if E5 is less than 31, return "OK", else return "Overdue".

### Notes

1.  The technique of placing one IF inside another is called "[nesting](https://exceljet.net/glossary/nesting)
    ." You will sometimes hear a formula like this called a "Nested IF formula". [This page has many examples](https://exceljet.net/articles/nested-ifs)
    .
2.  Remember to enclose text values inside IF in double quotes (""), but do not quote numbers or operators. See [How to use the IF function](https://exceljet.net/functions/if-function)
     for more details.

Related formulas
----------------

[![Excel formula: Nested IF function example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nested_if_function_example.png "Excel formula: Nested IF function example")](https://exceljet.net/formulas/nested-if-function-example)

### [Nested IF function example](https://exceljet.net/formulas/nested-if-function-example)

The goal is to assign a grade to each score in column C according to the rules in the table in the range F4:G9. One way to do this in Excel is to use a series of nested IF functions. Generally, nested IFs formulas are used to test more than one condition and return a different result for each...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")](https://exceljet.net/formulas/subtotal-invoices-by-age)

### [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, age (E5:E16) and amount (D5:D16) are named ranges ...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

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
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [TODAY Function](https://exceljet.net/functions/today-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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