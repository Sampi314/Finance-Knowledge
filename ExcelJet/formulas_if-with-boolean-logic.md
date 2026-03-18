# IF with boolean logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-with-boolean-logic

---

[Skip to main content](https://exceljet.net/formulas/if-with-boolean-logic#main-content)

[](https://exceljet.net/formulas/if-with-boolean-logic#)

*   [Previous](https://exceljet.net/formulas/if-this-and-that-or-that)
    
*   [Next](https://exceljet.net/formulas/if-with-other-calculations)
    

[If](https://exceljet.net/formulas#If)

IF with boolean logic
=====================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: IF with boolean logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_with_boolean_logic.png "Excel formula: IF with boolean logic")

Summary
-------

This formula shows how a nested IF formula can be replaced with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to sum values based on three conditions. In the example shown, the formula in F5 is:

    {=SUM(IF((color="red")*(region="East")*(quantity>7),quantity))}
    

where **color** (B5:B13), **region** (C5:C13), and **quantity** (D5:D13) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is 18, the sum of quantity for rows where the color is "Red", the region is "East", and the quantity is greater than 7.

_Note: In Excel 2019 and earlier, this is an_ [_array formula_](https://exceljet.net/glossary/array-formula)
_, and must be entered with control + shift + enter._

Generic formula
---------------

    = IF(criteria1*criteria2*criteria3,result)

Explanation 
------------

The goal is to sum the quantity for rows where the color is "Red", the region is "East", and the quantity is greater than 7. Although there are a number of ways to solve this problem in Excel purpose of this example is to demonstrate how to replace a [nested IF](https://exceljet.net/articles/nested-ifs)
 with a single IF using Boolean logic. This technique can be used to reduce the complexity of certain formulas. However, the example is for illustration only. This particular problem could be easily solved with [SUMIFS](https://exceljet.net/functions/sumifs-function)
 or [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
.

### Nested IF approach

One way to solve this problem is by using three separate IF formulas like this:

    IF(color="red",IF(region="east",IF(quantity>7,quantity)))

Each IF statement generates an array of TRUE and FALSE values like this:

    =IF({TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE},
    IF({TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE},
    IF({FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE},quantity)))
    

Only quantities where all three logical tests return TRUE "survive" the operation. Other quantities become FALSE and are evaluated by SUM as zero. The final result inside the SUM function is an array of values like this:

    =SUM({FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;8;FALSE;10})
    

The SUM function ignores the FALSE values and returns 18 as a final result.

### Boolean logic approach

Another way to solve this problem is with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the worksheet shown, we have this formula:

    =SUM(IF((color="red")*(region="East")*(quantity>7),quantity))
    

Notice this formula contains just one IF function. Inside, IF, the logical test is this part:

    (color="red")*(region="East")*(quantity>7)

Each expression generates an array of TRUE and FALSE values:

    {TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE}*{TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE}*{FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}

When these arrays are multiplied together, the math operation coerces the TRUE and FALSE values to 1s and 0s. The result is a single array inside the IF function like this:

    IF({0;0;0;0;0;0;1;0;1},quantity)
    

The array of 1s and 0s works to filter out quantities that don't meet all three conditions, and the result from IF is the same as we saw above with the nested IF approach:

    =SUM({FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;8;FALSE;10})
    

As before, SUM returns a final result of 18.

### Without the IF function

It is possible to remove the IF function altogether and use only Boolean algebra like this:

    =SUM((color="red")*(region="East")*(quantity>7)*quantity)

This formula works fine, but it must be entered as an array formula in Excel 2019 and older. To avoid that requirement, you can switch to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT((color="red")*(region="East")*(quantity>7),quantity)
    =SUMPRODUCT((color="red")*(region="East")*(quantity>7)*quantity)

Both formulas above return the same result and don't require special handling in older versions of Excel since SUMPRODUCT can [handle many array operations natively](https://exceljet.net/articles/why-sumproduct)
. For a more detailed example, see [SUMPRODUCT with IF](https://exceljet.net/formulas/sumproduct-with-if)

_Note: Boolean logic works especially well in formulas that sum values, because non-matching values result in zeros, and zeros do not affect the final sum. However, if the goal is to average values or get the minimum value based on one or more conditions, the Boolean approach can cause an incorrect result because the 0s may affect the final calculation._

Related formulas
----------------

[![Excel formula: SUMPRODUCT with IF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sumproduct_with_if.png "Excel formula: SUMPRODUCT with IF")](https://exceljet.net/formulas/sumproduct-with-if)

### [SUMPRODUCT with IF](https://exceljet.net/formulas/sumproduct-with-if)

In this example, the goal is to calculate a conditional sum with the SUMPRODUCT function to match the criteria shown in G5:G7. One way to do this is to use the IF function directly inside of SUMPRODUCT. Another more common alternative is to use Boolean logic to apply criteria. Both approaches are...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/intro%20to%20boolean%20logic-thumb.png)](https://exceljet.net/videos/intro-to-boolean-logic)

### [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)

In this video, I'm going to show you the basics of Boolean logic. Boolean logic is a great tool for simplifying formulas, especially those with many IF statements. So, to start off, what's a Boolean? A Boolean is a data type with only two possible values, TRUE or FALSE. You'll often see Boolean...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [SUMPRODUCT with IF](https://exceljet.net/formulas/sumproduct-with-if)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
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