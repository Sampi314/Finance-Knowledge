# Calculate sales commission with if - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-sales-commission-with-if

---

[Skip to main content](https://exceljet.net/formulas/calculate-sales-commission-with-if#main-content)

[](https://exceljet.net/formulas/calculate-sales-commission-with-if#)

*   [Previous](https://exceljet.net/formulas/zodiac-sign-lookup)
    
*   [Next](https://exceljet.net/formulas/if-cell-begins-with-x-y-or-z)
    

[If](https://exceljet.net/formulas#If)

Calculate sales commission with if
==================================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[IFS](https://exceljet.net/functions/ifs-function)

![Excel formula: Calculate sales commission with if](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate_sales_commission_with_if.png "Excel formula: Calculate sales commission with if")

Summary
-------

One way to calculate a sales commission with separate tiers and rates is to use the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in D5 is:

    =IF(C5<10000,0.1,IF(C5<=20000,0.15,IF(C5<=30000,0.2,0.25)))
    

The result in cell D5 is 10%, which is the commission rate for sales amounts up to $10,000. As the formula is copied down, it returns the correct commission rate for each sales figure in column B. The actual commission in column E is calculated by multiplying the sales value in column B by the commission rate calculated in column D. See below for details and an alternative formula based on the [IFS function.](https://exceljet.net/functions/ifs-function)

Generic formula
---------------

    =IF(A1<10000,0.1,IF(A1<=20000,0.15,IF(A1<=30000,0.2,0.25)))

Explanation 
------------

Imagine a company that uses a tiered commission structure for its sales team. Each salesperson is assigned a commission rate based on the total sales they have made. The commission tiers are structured like this:

*   For sales less than $10,000, the commission rate is 10%.
*   For sales from $10,000 to $20,000, the commission rate is 15%.
*   For sales from $20,000 to $30,000, the commission rate is 20%.
*   For sales over $30,000, the commission rate is 25%.

The goal is to calculate a commission for each person using the tiered structure above.

_Note: the formulas below use decimal values like 0.1 for 10%, but you can use percentages like 10%, 15%, etc., directly inside the formulas if you prefer, and Excel will correctly evaluate the percentage values._

### IF function

One way to solve this problem is with the [IF function](https://exceljet.net/functions/if-function)
, as seen in the worksheet above, where the formula in cell D5 is:

    =IF(C5<10000,0.1,IF(C5<=20000,0.15,IF(C5<=30000,0.2,0.25)))

This kind of formula is referred to as a "[nested if](https://exceljet.net/articles/nested-ifs)
" because we have several IF functions nested inside each other. Here's how the formula works step by step:

    =IF(C5<10000,0.1,...)

The first IF statement checks if the sales amount in C5 is less than $10,000. If so, it returns 0.1 as the commission rate. If not, it proceeds to the next IF statement.

    IF(C5<=20000,0.15,...)

The second IF statement is nested inside the first. It checks if the sales amount is less than or equal to $20,000. If so, it returns 0.15 as the commission rate. If not, it moves on to the final IF statement:

    IF(C5<=30000,0.2,0.25)

The third and final IF statement checks if the sales amount is less than or equal to $30,000. If so, it returns 0.2 as the commission rate. If not, it returns 0.25. Notice the last value is the value returned if _none of the previous conditions are met_, which only occurs if the sales amount is more than $30,000, the formula returns 0.25 as the commission rate.

_For more examples of nested if formulas, see_ [_How to use the IF function_](https://exceljet.net/functions/if-function)
 _and_ [_19 tips for nested if formulas_](https://exceljet.net/articles/nested-ifs)
_._

### IFS function

Nested IFs can become complicated and hard to read as more conditions are added because additional conditions result in additional IF statements. The [IFS function](https://exceljet.net/functions/ifs-function)
 offers a more streamlined way to manage multiple conditions in Excel because it eliminates the need to nest multiple IF statements together. As a result, the syntax is much simpler:

    =IFS(test1,result1,test2,result2,test2,result2,...)

For example, to solve this same problem with the IFS function, you can use the formula below in cell D5:

    =IFS(C5<10000,0.1,C5<=20000,0.15,C5<=30000,0.2,C5>30000,0.25)

For more details, see: [How to use the IFS function](https://exceljet.net/functions/ifs-function)
.

### Calculating commission

Both formulas above calculate the correct _commission rate_ for each sales amount in column B, but they don't calculate the commission itself. This is done in a separate formula in cell E5:

    =C5*D5

Alternatively, you can calculate the commission rate and the commission all in one formula like this:

    =C5*IF(C5<10000,0.1,IF(C5<=20000,0.15,IF(C5<=30000,0.2,0.25)))

Or with the IFS function like this:

    =C5*IFS(C5<10000,0.1,C5<=20000,0.15,C5<=30000,0.2,C5>30000,0.25)

Personally, I prefer to keep the calculations separate when possible because it makes the formulas simpler and easier to check.

Related formulas
----------------

[![Excel formula: VLOOKUP variable commission split](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_variable_commission_split.png "Excel formula: VLOOKUP variable commission split")](https://exceljet.net/formulas/vlookup-variable-commission-split)

### [VLOOKUP variable commission split](https://exceljet.net/formulas/vlookup-variable-commission-split)

In this example, the goal is to calculate the correct commission for both Agent and Broker based on a 3% commission which is split according to the table in G7:I11, which is named split . Notice the amount going to the Agent and Broker changes as the total amount increases, which the Agent getting...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel IFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ifs.png "Excel IFS function")](https://exceljet.net/functions/ifs-function)

### [IFS Function](https://exceljet.net/functions/ifs-function)

The Excel IFS function can run multiple tests and return a value corresponding to the first TRUE result. Use the IFS function to evaluate multiple conditions without multiple nested IF statements. IFS allows shorter, easier to read formulas....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

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

*   [VLOOKUP variable commission split](https://exceljet.net/formulas/vlookup-variable-commission-split)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [IFS Function](https://exceljet.net/functions/ifs-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    
*   [How to make a nested IF formula easier to read](https://exceljet.net/videos/how-to-make-a-nested-if-formula-easier-to-read)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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