# Split payment across months - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-payment-across-months

---

[Skip to main content](https://exceljet.net/formulas/split-payment-across-months#main-content)

[](https://exceljet.net/formulas/split-payment-across-months#)

*   [Previous](https://exceljet.net/formulas/sort-text-and-numbers-with-formula)
    
*   [Next](https://exceljet.net/formulas/square-root-of-number)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Split payment across months
===========================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Split payment across months](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split%20payments%20across%20months.png "Excel formula: Split payment across months")

Summary
-------

To evenly distribute a payment or other amount over a given number of months, with a variable start month, you can use a simple formula together with the AND function and a bit of [boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the example shown, the formula in E5 is:

    =amount/months*AND(E4>=start,E4<(start+months))
    

Where **amount** is the named range C4, **months** is the named range C5, and **start** is the named range C6

Generic formula
---------------

    =amount/months*AND(month>=start,month<(start+months))

Explanation 
------------

At the core, this is a simple formula that simply divides the total amount by the number of months given:

    =amount/months
    

The trick is to "cancel out" this amount in months where it doesn't apply.

To do this, we use this logical expression:

    AND(E4>=start,E4<(start+months))
    

Here we use the AND function to test each month in row 4 to see if it's both greater than or equal to the given start month, and less than the end month, calculated by adding the start month to total months.

AND will return TRUE only when both conditions are TRUE, and return FALSE in another other case. This effectively zeros out calculations in months that fall outside the range of interest. This works because during math operations, FALSE is coerced to zero, and TRUE is coerced to 1.

### Without named ranges

The formula in the example shown uses three [named ranges](https://exceljet.net/glossary/named-range)
. Without these named ranges, the formula can be written like this:

    =$C$4/$C$5*AND(E4>=$C$6,E4<($C$6+$C$5))
    

Related functions
-----------------

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Simplified%20formula%20example%20401k%20Match-thumb.png)](https://exceljet.net/videos/simplified-formula-example-401k-match)

### [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)

In this video we'll look at how to simplify some formulas we created in a previous video by replacing IF statements with the MIN function and a bit of Boolean logic. Make sure you watch the first video if you haven't already. In the example we have formulas that calculate a company match for an...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Complex%20formula%20example%20401k%20Match-thumb.png)](https://exceljet.net/videos/complex-formula-example-401k-match)

### [Complex formula example 401k Match](https://exceljet.net/videos/complex-formula-example-401k-match)

In this video we'll look at how to build a formula that calculates a 401k match using several nested IF statements . In the US, many companies match an employee's retirement deferral up to a certain percent. In this example, the match has two tiers: In Tier 1, the company matches 100% up to 4% of...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)
    
*   [Complex formula example 401k Match](https://exceljet.net/videos/complex-formula-example-401k-match)
    

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