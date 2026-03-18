# VLOOKUP tax rate calculation - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-tax-rate-calculation

---

[Skip to main content](https://exceljet.net/formulas/vlookup-tax-rate-calculation#main-content)

[](https://exceljet.net/formulas/vlookup-tax-rate-calculation#)

*   [Previous](https://exceljet.net/formulas/vlookup-override-output)
    
*   [Next](https://exceljet.net/formulas/vlookup-two-way-lookup)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP tax rate calculation
============================

by Dave Bruns · Updated 27 Mar 2023

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

![Excel formula: VLOOKUP tax rate calculation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_tax_rate_calculation.png "Excel formula: VLOOKUP tax rate calculation")

Summary
-------

This example uses the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 to calculate a simple tax rate. In the example shown, the formula in C5 is:

    =VLOOKUP(B5,tax_data,2,1)
    

where **tax\_data** is the [named range](https://exceljet.net/glossary/named-range)
 F5:G9. As the formula is copied down column C, the VLOOKUP function looks up the income in column B in the range F5:F9 and returns the correct tax rate from the range G5:G9. A formula in column D multiples the income by the tax rate to display the total tax amount.

_Note: this formula calculates a tax rate in a simple one-tier scheme. To calculate tax based on a progressive system where income is taxed at different rates in multiple tiers, [see this example](https://exceljet.net/formulas/income-tax-bracket-calculation)
._

Generic formula
---------------

    =VLOOKUP(amount,tax_data,2,TRUE)

Explanation 
------------

In this example, the goal is to look up a given income value in a tax table and return the correct tax rate for that income. The tax rate is organized into 5 tiers in the range F5:F9 with the corresponding tax rate in the range G5:G9. For convenience, the range F5:G9 is named **tax\_data**. The explanation below shows how to retrieve the correct tax rate for each income with the VLOOKUP function.

### VLOOKUP function

VLOOKUP is an Excel function to get data from a table organized _vertically_. Lookup values must appear in the _first column_ of the table passed into VLOOKUP, and the information to retrieve is specified by column number. For a complete introduction to VLOOKUP with many examples and video links, [see this article](https://exceljet.net/functions/vlookup-function)
.

### VLOOKUP solution

In the worksheet shown, the formula in cell C5 is:

    =VLOOKUP(B5,tax_data,2,TRUE)

VLOOKUP requires lookup values to be in the first column of the lookup table. To retrieve the correct tax rate for the income in column B, VLOOKUP is configured like this:

*   The _lookup\_value_ comes from cell B5
*   The _table\_array_ is the [named range](https://exceljet.net/glossary/named-range)
     **tax\_data** (F5:G9)
*   The _col\_index\_num_ is 2 since the tax rates are in the _second_ column of **tax\_data**
*   The _range\_lookup_ argument is set to TRUE = approximate match

With this configuration, VLOOKUP scans the lookup values until it finds a value greater than the value in B5, then VLOOKUP "drops back" to the previous row and returns the corresponding tax rate from that row. Because we are using VLOOKUP in approximate match mode, with _range\_lookup_ set to TRUE, the lookup values in F5:F9 _must be sorted in ascending order_.

As the formula is copied down column C, the VLOOKUP function looks up the income in column B in the range F5:F9 and returns the correct tax rate from the range G5:G9. A formula in column D multiples the income by the tax rate to display the total tax amount.

_Note: this formula calculates a tax rate in a simple one-tier scheme. To calculate tax based on a progressive system where income is taxed at different rates in multiple tiers, [see this example](https://exceljet.net/formulas/income-tax-bracket-calculation)
._

### Named range optional

The named range in this example is optional and used for convenience only because it makes the formula easier to read and means that the tax rate does not need to be locked. To avoid a named range, use an [absolute reference](https://exceljet.net/glossary/absolute-reference)
 like this:

    =VLOOKUP(B5,$F$5:$G$9,2,TRUE)

### VLOOKUP match modes

VLOOKUP has two match modes: exact match and approximate match, controlled by an optional fourth argument called range\_lookup. When _range\_lookup_ is omitted, it defaults to TRUE and VLOOKUP performs an approximate match. This means we could leave out the last argument and get the same result:

    =VLOOKUP(B5,tax_data,2)

However,  in this example, the fourth argument has been set to TRUE explicitly for clarity. For a complete overview of VLOOKUP with many examples [see our VLOOKUP page](https://exceljet.net/functions/vlookup-function)
.

_Note: I think the default behavior of VLOOKUP is [dangerous](https://exceljet.net/articles/danger-beware-vlookup-defaults)
 because it can easily produce incorrect results that look normal. For that reason, I recommend that you always provide a value for range\_lookup as a reminder to yourself and others of the behavior you intend._

### Total tax

The tax rates in column D are decimal values formatted with the [percentage number format](https://exceljet.net/glossary/percentage-number-format)
. The formula to calculate the total tax in cell D5 multiples Income by the Tax rate:

    =B5*C5

As the formula is copied down, it returns the total tax for each row in the data.

Related formulas
----------------

[![Excel formula: Income tax bracket calculation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/income%20tax%20bracket%20calculation_0.png "Excel formula: Income tax bracket calculation")](https://exceljet.net/formulas/income-tax-bracket-calculation)

### [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)

In this example, the goal is to calculate the total income tax owed in a progressive tax system with multiple tax brackets, as shown in the worksheet. The article below first reviews how taxes are computed in a progressive system. Next, it shows how to accomplish this task in Excel using two...

[![Excel formula: VLOOKUP calculate shipping cost](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_shipping_cost.png "Excel formula: VLOOKUP calculate shipping cost")](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

### [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)

This example shows how to use the VLOOKUP function to calculate the total shipping cost for an item in one formula, where the cost per kilogram (kg) varies according to weight. This requires an "approximate match" since in most cases the actual weight will not appear in the shipping cost table. For...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Tax rate calculation with fixed base](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/tax_rate_calculation_with_fixed_base.png "Excel formula: Tax rate calculation with fixed base")](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

### [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)

The goal is to calculate a tax amount with both fixed and variable components according to the following logic: If the amount is less than $1000, only the base tax applies. If the amount is $1000 or greater, the result is the base tax + 15% \* the amount over $1000 This problem can be easily solved...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Why%20VLOOKUP%20is%20better%20than%20nested%20IFs-thumb.png)](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

### [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)

In this video we look at a few reasons why VLOOKUP is a better option than nested IF statements. In our last video, we used nested IF statements to calculate a commission rate based on a sales number. As a quick recap: The first formula is created with nested IF statements normally. The second...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Income tax bracket calculation](https://exceljet.net/formulas/income-tax-bracket-calculation)
    
*   [VLOOKUP calculate shipping cost](https://exceljet.net/formulas/vlookup-calculate-shipping-cost)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Tax rate calculation with fixed base](https://exceljet.net/formulas/tax-rate-calculation-with-fixed-base)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [Why VLOOKUP is better than nested IFs](https://exceljet.net/videos/why-vlookup-is-better-than-nested-ifs)
    

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