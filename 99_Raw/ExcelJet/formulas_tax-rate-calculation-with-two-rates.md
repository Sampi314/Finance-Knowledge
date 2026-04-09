# Tax rate calculation with two rates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/tax-rate-calculation-with-two-rates

---

[Skip to main content](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates#main-content)

[](https://exceljet.net/formulas/tax-rate-calculation-with-two-rates#)

*   [Previous](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)
    
*   [Next](https://exceljet.net/formulas/area-of-a-circle)
    

[Financial](https://exceljet.net/formulas#Financial)

Tax rate calculation with two rates
===================================

by Dave Bruns · Updated 23 Oct 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Tax rate calculation with two rates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/tax_rate_calculation_with_two_rates.png "Excel formula: Tax rate calculation with two rates")

Summary
-------

To calculate a sales tax with two rates (brackets), you can use the [IF function](https://exceljet.net/functions/if-function)
. In the example shown, the formula in C5, copied down, is:

    =IF(B5<=limit,B5*rate1,limit*rate1+(B5-limit)*rate2)
    

where **limit** (F6), **rate1** (F4), and **rate2** (F5) are [named ranges](https://exceljet.net/glossary/dynamic-named-range)
. As the formula is copied down, it calculates a tax of 6% on amounts up to 20,000 and a tax of 10% on amounts over 20,000.

_Note: The named ranges are optional and for readability and convenience only. See below for a version of the formula that uses absolute references instead._

Generic formula
---------------

    =IF(A1<=limit,A1*rate1,limit*rate1+(A1-limit)*rate2)

Explanation 
------------

The goal is to calculate a tax of 6% on amounts up to 20,000 and a tax of 10% on amounts of 20,000 or greater. This problem illustrates how to use the IF function to return different calculations. At the core, this formula uses a single [IF function](https://exceljet.net/functions/if-function)
. The logical test is based on this expression:

    B5<=limit
    

When B5 (the current amount) is less than the **limit** in cell F6 (20,000), the test returns TRUE and the IF function applies **rate1** only:

    B5*rate1
    

When B5 is greater than 20,000, the test returns FALSE and the IF function applies **rate1** and **rate2**:

    limit*rate1+(B5-limit)*rate2
    

Translation:

1.  Calculate **rate1** by multiplying the **limit** (20,000) by 6% (F4).
2.  Calculate **rate2** by subtracting the **limit** from the amount, and multiplying the result by 10% (F5)
3.  Add #1 and #2 together

### Without named ranges

[Named ranges](https://exceljet.net/glossary/named-range)
 can make formulas easier to write and read. The same formula without named ranges looks like this:

    =IF(B5<=$F$6,B5*$F$4,$F$6*$F$4+(B5-$F$6)*$F$5)
    

![Tax rate calculation with two rates with absolute references](https://exceljet.net/sites/default/files/images/formulas/inline/tax_rate_calculation_with_two_rates_absolute.png "Tax rate calculation with two rates with absolute references")

References to F4, F5, and F5 are [locked](https://exceljet.net/glossary/absolute-reference)
 to prevent changes when the formula is copied down the table. Notice B5 is still a [relative reference](https://exceljet.net/glossary/relative-reference)
 because we want the reference to change as the formula is copied.

Related formulas
----------------

[![Excel formula: VLOOKUP tax rate calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_tax_rate_calculation.png "Excel formula: VLOOKUP tax rate calculation")](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

### [VLOOKUP tax rate calculation](https://exceljet.net/formulas/vlookup-tax-rate-calculation)

In this example, the goal is to look up a given income value in a tax table and return the correct tax rate for that income. The tax rate is organized into 5 tiers in the range F5:F9 with the corresponding tax rate in the range G5:G9. For convenience, the range F5:G9 is named tax\_data . The...

[![Excel formula: Tax rate calculation with fixed base](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_fixed_base.png "Excel formula: Tax rate calculation with fixed base")](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

### [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

The goal is to calculate a tax amount with both fixed and variable components according to the following logic: If the amount is less than $1000, only the base tax applies. If the amount is $1000 or greater, the result is the base tax + 15% \* the amount over $1000 This problem can be easily solved...

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
    
*   [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)
    
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