# Cap percentage at specific amount - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cap-percentage-at-specific-amount

---

[Skip to main content](https://exceljet.net/formulas/cap-percentage-at-specific-amount#main-content)

[](https://exceljet.net/formulas/cap-percentage-at-specific-amount#)

*   [Previous](https://exceljet.net/formulas/cap-percentage-at-100)
    
*   [Next](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Cap percentage at specific amount
=================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")

Summary
-------

To cap the result of a percentage-based calculation at a specific amount, you can use the [MIN function](https://exceljet.net/functions/min-function)
. In the example shown, the formula in D6 is:

    =MIN(C6*10%,1000)
    

which ensures the result will never be greater than $1000.

Generic formula
---------------

    =MIN(A1*percent,1000)

Explanation 
------------

This formula uses the [MIN function](https://exceljet.net/functions/min-function)
 to make a decision that might otherwise be handled with the [IF function](https://exceljet.net/functions/if-function)
. Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations.

Inside MIN, the value in C6 is multiplied by 10%, and the result appears at the first number given to MIN. The number 1000 is supplied as the second value. The MIN function simply returns the smaller of the two values:

*   When C6\*10% is < 1000, the result is C6\*10%
*   When C6\*10% is > 1000, the result is 1000
*   When C6\*10% is = 1000, the result is 1000

### Replacement for IF

To return the smaller or greater of two values, MIN and MAX can be a [clever way to avoid a more complicated IF formula](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
.

Related formulas
----------------

[![Excel formula: Cap percentage at 100](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20100.png "Excel formula: Cap percentage at 100")](https://exceljet.net/formulas/cap-percentage-at-100)

### [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)

This formula uses the MIN function as an alternative to the IF function . Although MIN is frequently used to find the minimum value in a larger set of numbers, it also works fine with just two values. Inside MIN, the first value is hardcoded as 1, the equivalent of 100% when formatted as a...

[![Excel formula: Convert negative numbers to zero](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/convert%20negative%20numbers%20to%20zero.png "Excel formula: Convert negative numbers to zero")](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

### [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)

In this example, the goal is to convert negative numbers in column B to zero and leave positive numbers unchanged. Essentially, we want to force negative numbers to zero. With the MAX function The MAX function provides an elegant solution: =MAX(B5,0) This formula takes advantage of the fact that...

[![Excel formula: Get total from percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20total%20from%20percent_0.png "Excel formula: Get total from percentage")](https://exceljet.net/formulas/get-total-from-percentage)

### [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)

In this example, the goal is to work out the total of all expenses using a known percent of total of any one expense . If we know groceries are $200 and we know groceries represent 10.3% of total expenses, we want to calculate the total of all expenses ($1945). In other words, $200 is 10.3% of what...

[![Excel formula: Get amount with percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20amount%20with%20percent_0.png "Excel formula: Get amount with percentage")](https://exceljet.net/formulas/get-amount-with-percentage)

### [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)

In this example, the goal is to convert the percentages shown in column C to amounts, where the total of all amounts is given as $1945. In other words, if we know Rent is 36.0%, and the total of all expenses is $1945, we want to calculate that Rent is $700. With "x" as the number we want to find,...

[![Excel formula: Get percentage of total](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20of%20total_0.png "Excel formula: Get percentage of total")](https://exceljet.net/formulas/get-percentage-of-total)

### [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)

In this example, the goal is to work out the "percent of total" for each expense shown in the worksheet. In other words, given that we know the total is $1945, and we know Rent is $700, we want to determine that Rent is 36% of the total. The total already exists in the named range total (C15) which...

[![Excel formula: Get percentage discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20percent%20discount_0.png "Excel formula: Get percentage discount")](https://exceljet.net/formulas/get-percentage-discount)

### [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)

In this example, the goal is to determine the percentage discount for each item shown in the table, given an original price and a sale price. In other words, given the Charcoal grill has an original price of $70.00 and a Sale Price of $59.50, we want to calculate a percentage discount of 15%, based...

[![Excel formula: Increase by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Increase%20by%20percent_0.png "Excel formula: Increase by percentage")](https://exceljet.net/formulas/increase-by-percentage)

### [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)

In this example, the goal is to increase the prices shown in column C by the percentages shown in column D. For example, given the original price of $70.00, and an increase of 10%, the result should be $77.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1+...

[![Excel formula: Decrease by percentage](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/decrease%20by%20percent.png "Excel formula: Decrease by percentage")](https://exceljet.net/formulas/decrease-by-percentage)

### [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)

In this example, the goal is to decrease the prices shown in column C by the percentages shown in column D. For example, given an original price of $70.00, and an decrease of 10% ($7.00), the result should be $63.00. The general formula for this calculation, where "x" is the new price, is: x=old\*(1...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)
    
*   [Convert negative numbers to zero](https://exceljet.net/formulas/convert-negative-numbers-to-zero)
    
*   [Get total from percentage](https://exceljet.net/formulas/get-total-from-percentage)
    
*   [Get amount with percentage](https://exceljet.net/formulas/get-amount-with-percentage)
    
*   [Get percentage of total](https://exceljet.net/formulas/get-percentage-of-total)
    
*   [Get percentage discount](https://exceljet.net/formulas/get-percentage-discount)
    
*   [Increase by percentage](https://exceljet.net/formulas/increase-by-percentage)
    
*   [Decrease by percentage](https://exceljet.net/formulas/decrease-by-percentage)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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