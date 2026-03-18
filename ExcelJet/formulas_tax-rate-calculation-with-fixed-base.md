# Tax rate calculation with fixed base - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base

---

[Skip to main content](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base#main-content)

[](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base#)

*   [Previous](https://exceljet.net/formulas/simple-investing-worksheet)
    
*   [Next](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)
    

[Financial](https://exceljet.net/formulas#Financial)

Tax rate calculation with fixed base
====================================

by Dave Bruns · Updated 29 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Tax rate calculation with fixed base](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/tax_rate_calculation_with_fixed_base.png "Excel formula: Tax rate calculation with fixed base")

Summary
-------

This example shows how to set up simple formula using the [IF function](https://exceljet.net/functions/if-function)
 to calculate a tax amount with both fixed and variable components. In the example shown, the formula in C5 is:

    =IF(B5<limit,base,base+(B5-limit)*rate)
    

Where **rate** (F4), **base** (F5), and **limit** (F6) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, it calculates a tax for each amount shown in column B. If the amount is below $1000, only the base tax applies. If the amount is greater than or equal to $1000, the formula returns the base tax plus a 15% tax on the amount greater than $1000.

_Note: The named ranges are optional and for readability and convenience only. See below for a version of the formula that uses absolute references instead._

Generic formula
---------------

    =IF(B5<limit,base,base+(B5-limit)*rate)

Explanation 
------------

The goal is to calculate a tax amount with both fixed and variable components according to the following logic:

1.  If the amount is less than $1000, only the base tax applies.
2.  If the amount is $1000 or greater, the result is the base tax + 15% \* the amount over $1000

This problem can be easily solved with the IF function. The formula in C5 is:

    =IF(B5<limit,base,base+(B5-limit)*rate)
    

Where **rate** (F4), **base** (F5), and **limit** (F6) are [named ranges](https://exceljet.net/glossary/named-range)
. The logical test inside the IF function checks if the amount in column B is less than the **limit** entered in cell F6:

    =IF(B5<limit,
    

If the amount in B5 is less than $1000 (F6), the test is TRUE and IF returns $100 (F5):

    =IF(B5<limit,base,
    

If the amount in B5 is _not_ less than $1000, the test is FALSE, and IF returns $100 (F6) plus 15% (F4) of the amount over $1000 (F5):

    base+(B5-limit)*rate
    

As the formula is copied down, the formula calculates a tax for each amount in column B. 

### Without named ranges

If you prefer not to use named ranges you can use absolute references instead like this:

    =IF(B5<$F$6,$F$5,$F$5+(B5-$F$6)*$F$4)

![Tax rate calculation with fixed base absolute references](https://exceljet.net/sites/default/files/images/formulas/inline/tax_rate_calculation_with_fixed_base_absolute.png "Tax rate calculation with fixed base absolute references")

Note the B5 is still a [relative reference](https://exceljet.net/glossary/relative-reference)
 because we want that reference to change as the formula is copied down. However, the other references are [absolute](https://exceljet.net/glossary/absolute-reference)
 because they should not change as the formula is copied.

Related formulas
----------------

[![Excel formula: VLOOKUP tax rate calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_tax_rate_calculation.png "Excel formula: VLOOKUP tax rate calculation")](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

### [VLOOKUP tax rate calculation](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

In this example, the goal is to look up a given income value in a tax table and return the correct tax rate for that income. The tax rate is organized into 5 tiers in the range F5:F9 with the corresponding tax rate in the range G5:G9. For convenience, the range F5:G9 is named tax\_data . The...

[![Excel formula: Tax rate calculation with two rates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_two_rates.png "Excel formula: Tax rate calculation with two rates")](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)

### [Tax rate calculation with two rates](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)

The goal is to calculate a tax of 6% on amounts up to 20,000 and a tax of 10% on amounts of 20,000 or greater. This problem illustrates how to use the IF function to return different calculations. At the core, this formula uses a single IF function . The logical test is based on this expression: B5...

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20create%20a%20named%20range-thumb.png)](https://exceljet.net/videos/how-to-create-a-named-range)

### [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)

Named ranges are one of the most useful features in Excel. They make your formulas much easier to read and understand; they automatically give you absolute references , and they reduce errors. Let's take a look at a few ways to create named ranges. The simplest way to create a named range is to use...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP tax rate calculation](https://exceljet.net/formulas/vlookup-tax-rate-calculation)
    
*   [Tax rate calculation with two rates](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates)
    
*   [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    
*   [How to create a named range](https://exceljet.net/videos/how-to-create-a-named-range)
    

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