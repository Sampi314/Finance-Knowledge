# Smaller of two values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/smaller-of-two-values

---

[Skip to main content](https://exceljet.net/formulas/smaller-of-two-values#main-content)

[](https://exceljet.net/formulas/smaller-of-two-values#)

*   [Previous](https://exceljet.net/formulas/nth-smallest-value-with-criteria)
    
*   [Next](https://exceljet.net/formulas/case-sensitive-lookup)
    

[Min and Max](https://exceljet.net/formulas#Min-and-Max)

Smaller of two values
=====================

by Dave Bruns · Updated 22 Feb 2023

Related functions 
------------------

[MIN](https://exceljet.net/functions/min-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Smaller of two values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/smaller_of_two_values.png "Excel formula: Smaller of two values")

Summary
-------

To get the smaller (or lesser), of two values, you can use the [MIN function](https://exceljet.net/functions/min-function)
. In the example shown, the formula in E5 is:

    =MIN(B5,C5)
    

As the formula is copied down, it returns the smaller of the two values seen in columns B and C.

Generic formula
---------------

    =MIN(value1,value2)

Explanation 
------------

In this example, the goal is to return the smaller of two values which appear in columns B and C. Although this problem could be solved with the IF function (see below), the simplest solution is to use the MIN function.

### MIN function

The [MIN function](https://exceljet.net/functions/min-function)
 returns the smallest numeric value in the data provided. In Excel, it's common to use the MIN function with a range like this:

    =MIN(range) // minimum value in range

However, because MIN can accept values in separate [arguments](https://exceljet.net/glossary/function-argument)
, you can easily use the MIN function to select the smaller of values in two cells like this:

    =MIN(A1,B1) // smaller of A1 or B1
    =MIN(A1,C1) // smaller of A1 or C1

This is the approach used in the worksheet shown, where  the formula in E5 is:

    =MIN(B5,C5)
    

As the formula is copied down, it returns the value in column B or the value in column C, whichever is smaller. The MIN function can be used to return the smallest value from _any_ type of numeric data. This means you can use MIN to solve a variety of "smallest of" problems:

*   Earlier of two dates
*   Earlier of two times
*   Faster of two times
*   Colder of two temperatures
*   Smaller of two fractions

### Alternative to IF function

As this example shows, the MIN function can be used as a compact and elegant replacement for the [IF function](https://exceljet.net/functions/if-function)
. For example, in the example shown, the IF function could be used to return the smaller of the two values like this:

    =IF(B5<C5,B5,C5)

The basic translation of this formula is "If B5 is less than C5 return B5. Otherwise return C5". This is a perfectly valid Excel formula, and you will often encounter IF formulas that follow this structure. However, the MIN version of the formula is simpler and contains no redundant references, so less prone to errors:

    =MIN(B5,C5)

Note that the references to B5 and C5 appear just once in the MIN version.

Related formulas
----------------

[![Excel formula: Larger of two values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/larger_of_two_values.png "Excel formula: Larger of two values")](https://exceljet.net/formulas/larger-of-two-values)

### [Larger of two values](https://exceljet.net/formulas/larger-of-two-values)

In this example, the goal is to return the greater of two values which appear in columns B and C. Although this problem could be solved with the IF function (see below), the simplest solution is to use the MAX function. MAX function The MAX function returns the largest numeric value in the data...

[![Excel formula: Cap percentage at specific amount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20specific%20amount.png "Excel formula: Cap percentage at specific amount")](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

### [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)

This formula uses the MIN function to make a decision that might otherwise be handled with the IF function . Although MIN is usually used to return the minimum value in a data set with many numbers, it also works fine for the "lesser of the two" situations. Inside MIN, the value in C6 is multiplied...

[![Excel formula: Cap percentage at 100](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/cap%20percentage%20at%20100.png "Excel formula: Cap percentage at 100")](https://exceljet.net/formulas/cap-percentage-at-100)

### [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)

This formula uses the MIN function as an alternative to the IF function . Although MIN is frequently used to find the minimum value in a larger set of numbers, it also works fine with just two values. Inside MIN, the first value is hardcoded as 1, the equivalent of 100% when formatted as a...

Related functions
-----------------

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20calculate%20maximum%20and%20minimum%20values-thumb.png)](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

### [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)

In this video we'll look at how to calculate minimum and maximum values in Excel. Let's take a look. Here we have a list of properties, that includes an address, a price, and a variety of other information. Let's calculate the maximum and minimum values in this list. First, I'm going to create a...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Simplified%20formula%20example%20401k%20Match-thumb.png)](https://exceljet.net/videos/simplified-formula-example-401k-match)

### [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)

In this video we'll look at how to simplify some formulas we created in a previous video by replacing IF statements with the MIN function and a bit of Boolean logic. Make sure you watch the first video if you haven't already. In the example we have formulas that calculate a company match for an...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Larger of two values](https://exceljet.net/formulas/larger-of-two-values)
    
*   [Cap percentage at specific amount](https://exceljet.net/formulas/cap-percentage-at-specific-amount)
    
*   [Cap percentage at 100](https://exceljet.net/formulas/cap-percentage-at-100)
    

### Functions

*   [MIN Function](https://exceljet.net/functions/min-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [How to calculate maximum and minimum values](https://exceljet.net/videos/how-to-calculate-maximum-and-minimum-values)
    
*   [Simplified formula example 401k Match](https://exceljet.net/videos/simplified-formula-example-401k-match)
    

### Articles

*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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