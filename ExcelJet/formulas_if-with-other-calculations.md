# IF with other calculations - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-with-other-calculations

---

[Skip to main content](https://exceljet.net/formulas/if-with-other-calculations#main-content)

[](https://exceljet.net/formulas/if-with-other-calculations#)

*   [Previous](https://exceljet.net/formulas/if-with-boolean-logic)
    
*   [Next](https://exceljet.net/formulas/if-with-wildcards)
    

[If](https://exceljet.net/formulas#If)

IF with other calculations
==========================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: IF with other calculations](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_with_other_calculations.png "Excel formula: IF with other calculations")

Summary
-------

The [IF function](https://exceljet.net/functions/if-function)
 can be combined with other calculations by nesting other formulas and functions inside IF. In the example shown, the formula in E5, copied down, is:

    =IF(C5>20, C5*D5*0.9, C5*D5)
    

If more than 20 items were sold, the formula applies a 10% discount to the total price. Otherwise, it just calculates the total price without any discount. 

Generic formula
---------------

    =IF(logical_test,calculation1,calculation2)

Explanation 
------------

The goal is to demonstrate how other formulas and functions can be [nested](https://exceljet.net/glossary/nesting)
 inside the [IF function](https://exceljet.net/videos/the-if-function)
. The example is a simple quantity-based discount formula.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 evaluates a logical test and returns one value if the result is TRUE, and a different value if the result is FALSE. The generic syntax for IF looks like this:

    =IF(logical_test,value_if_true,value_if_false)

 For example, if cell A1 contains the value 75, then you could use IF to return "Pass" or "Fail" like this:

    =IF(A1>70,"Pass","Fail") // returns "Pass"

If the value in A1 is 65, then the same formula will return "Fail":

    =IF(A1>70,"Pass","Fail") // returns "Fail"

What is not obvious with IF is that the _logical\_test_, the _value\_if\_true,_ and the _value\_if\_false_ can all be _other formulas_. The example below shows how this works.

### Example

In the worksheet shown, the goal is to apply a simple quantity-based discount to the total calculated in column E. If the quantity is greater than 20, we want to discount the total by 10%. Otherwise, we want to calculate the total normally. In cell E5, the formula used to perform this task is:

    =IF(C5>20,C5*D5*0.9,C5*D5)

The formula works like this:

*   The logical test is C5>20. This checks if the quantity of items sold (in cell C5) is more than 20.
*   The value if true is C5\*D5\*0.9. This calculates the total price as the quantity sold times the price per item and then applies a 10% discount by multiplying the result by 0.9.
*   The value if false is C5\*D5. This calculates the total price as the quantity sold times the price per item, without any discount.

So, if more than 20 items were sold, the formula applies a 10% discount to the total price. Otherwise, it just calculates the total price without any discount. You can then copy the formula down column E to apply it to all items in the spreadsheet.

### Other calculations

The calculations used inside the IF function can be customized as needed. For a more general formula that applies the discount itself, you can use the following:

    =IF(C5>20,C5*D5*(1-discount),C5*D5)

For example, to apply an 18% discount, you would use:

    =IF(C5>20,C5*D5*(1-18%),C5*D5)

This works because Excel will automatically evaluate the [percentage](https://exceljet.net/glossary/percentage-number-format)
 18% as the number 0.18. You can also adjust calculations in the logical test as needed. To apply a 20% discount to apples only, you could use the [AND function](https://exceljet.net/functions/and-function)
 in the logical test like this:

    =IF(AND(C5>20,B5="apples"),C5*D5*(1-20%),C5*D5)

In Excel, nesting other calculations inside a function or formula is a common practice in many more advanced formulas. You can find [many examples in this list](https://exceljet.net/formulas)
.

### Detailed quantity-based calculation

If you are interested in a more detailed example of a quantity-based discount formula, [this example](https://exceljet.net/formulas/quantity-based-discount)
 uses XLOOKUP instead of IF to apply more granular discounts based on a lookup operation.

Related formulas
----------------

[![Excel formula: If cell is this OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20is%20this%20or%20that.png "Excel formula: If cell is this OR that")](https://exceljet.net/formulas/if-cell-is-this-or-that)

### [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)

In the example shown, we want to mark or "flag" records where the color is red OR green. In other words, we want to check the color in column B, and then leave a marker (x) if we find the word "red" or "green". In D6, the formula is: =IF(OR(B6="red",B6="green"),"x","") This is an example of nesting...

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If NOT this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If_not_this_or_that.png "Excel formula: If NOT this or that")](https://exceljet.net/formulas/if-not-this-or-that)

### [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)

The goal is to "flag" records that are neither "Red" nor "Green". More specifically, we want to check the color in column B, and leave an "x" in rows where the color is NOT "Red" OR "Green". If the color is "Red" OR "Green", we want to display nothing. IF function logic The IF function is commonly...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

[![Excel formula: Quantity based discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/quantity_based_discount.png "Excel formula: Quantity based discount")](https://exceljet.net/formulas/quantity-based-discount)

### [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)

The goal is to calculate discounts on a per-item and per-quantity basis using the discount table at the right in the workbook shown. The purpose of the discount table is to allow each item to have its own set of discounts. Notice that Donuts have a different discount for a quantity of 24. The...

[![Excel formula: Tax rate calculation with fixed base](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_fixed_base.png "Excel formula: Tax rate calculation with fixed base")](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

### [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

The goal is to calculate a tax amount with both fixed and variable components according to the following logic: If the amount is less than $1000, only the base tax applies. If the amount is $1000 or greater, the result is the base tax + 15% \* the amount over $1000 This problem can be easily solved...

[![Excel formula: Tax rate calculation with two rates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_two_rates.png "Excel formula: Tax rate calculation with two rates")](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)

### [Tax rate calculation with two rates](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)

The goal is to calculate a tax of 6% on amounts up to 20,000 and a tax of 10% on amounts of 20,000 or greater. This problem illustrates how to use the IF function to return different calculations. At the core, this formula uses a single IF function . The logical test is based on this expression: B5...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/If%20this%20OR%20that-thumb.png)](https://exceljet.net/videos/if-this-or-that)

### [If this OR that](https://exceljet.net/videos/if-this-or-that)

Sometimes, you might need to write a formula that uses the IF function to test for this OR that, or this AND that. There are two special functions, AND and OR, that make this easy to do. Let's take a look. In this first worksheet, we have a list of employees. Let's assume that you need to group...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If cell is this OR that](https://exceljet.net/formulas/if-cell-is-this-or-that)
    
*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If NOT this or that](https://exceljet.net/formulas/if-not-this-or-that)
    
*   [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)
    
*   [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)
    
*   [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)
    
*   [Tax rate calculation with two rates](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [If this OR that](https://exceljet.net/videos/if-this-or-that)
    

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