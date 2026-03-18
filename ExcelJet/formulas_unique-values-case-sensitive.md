# Unique values case-sensitive - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unique-values-case-sensitive

---

[Skip to main content](https://exceljet.net/formulas/unique-values-case-sensitive#main-content)

[](https://exceljet.net/formulas/unique-values-case-sensitive#)

*   [Previous](https://exceljet.net/formulas/unique-values-by-count)
    
*   [Next](https://exceljet.net/formulas/unique-values-from-multiple-ranges)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Unique values case-sensitive
============================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[REDUCE](https://exceljet.net/functions/reduce-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[EXACT](https://exceljet.net/functions/exact-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

![Excel formula: Unique values case-sensitive](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unique_values_case_sensitive.png "Excel formula: Unique values case-sensitive")

Summary
-------

The [UNIQUE function](https://exceljet.net/functions/unique-function)
 is not case-sensitive. However, you can create a case-sensitive unique formula with the [REDUCE function](https://exceljet.net/functions/reduce-function)
. In the example shown, the formula in cell D5 is

    =REDUCE(,data,LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v))))

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

_Note: I learned this formula from fellow Excel MVP, [Sergei Baklan](https://www.linkedin.com/in/baklan/)
._

Generic formula
---------------

    =REDUCE(,data,LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v))))

Explanation 
------------

In this example, the goal is to create a formula that will extract unique values from a range of data in a case-sensitive way. Normally, we would use the UNIQUE function to extract unique values. However, UNIQUE is not case-sensitive so it won't work in this situation. One way to solve this problem is to use the REDUCE function with a custom LAMBDA function, as explained below.

### REDUCE function

The [REDUCE function](https://exceljet.net/functions/reduce-function)
 applies a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 to each element in a given array and accumulates results to a single value. The generic syntax for the REDUCE function looks like this:

    =REDUCE([initial_value], array, lambda)

The calculation performed by REDUCE is determined by a custom [LAMBDA function](https://exceljet.net/functions/lambda-function)
 with this generic syntax:

    LAMBDA(a,v,calculation)
    

The first argument, _a_, is the accumulator. The accumulator begins as the _initial\_value_ provided to REDUCE and changes as REDUCE loops over the elements in the array and applies a calculation. The _v_ represents the value of each element in the array. _Calculation_ is the formula logic that creates the final accumulated result.

### REDUCE + LAMBDA

In the worksheet shown, the formula in cell D5 is:

    =REDUCE(,data,LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v))))

Notice that the initial value is purposely not provided, because we want to start with a null value. The custom LAMBDA function inside of REDUCE looks like this:

    LAMBDA(a,v,IF(SUM(--EXACT(a,v)),a,VSTACK(a,v)))

At a high level, the REDUCE function loops over the values in **data** one at a time. At each new value, _v_, the custom LAMBDA function checks if _v_ is already in the accumulator, _a_. If _v_ is already in _a_, the current value of _a_ is returned. If _v_ is not already present in _a_, the function combines _a_ and _v_ with the [VSTACK function](https://exceljet.net/functions/vstack-function)
. The final result is an array that contains case-sensitive unique values.

### Details

The [EXACT function](https://exceljet.net/functions/exact-function)
 is what makes this formula case-sensitive, and the [IF function](https://exceljet.net/functions/if-function)
 is used to test values and control flow:

    IF(SUM(--EXACT(a,v)),a,VSTACK(a,v))

The _logical\_test_ inside of IF is based on the EXACT function and the SUM function:

    SUM(--EXACT(a,v))

Normally, the EXACT function checks if _two_ values are exactly equal, including upper and lowercase characters. In this case, EXACT is comparing _a_ and _v_. Because _a_ is an array, the result will be an [array](https://exceljet.net/glossary/array)
 of TRUE and FALSE values. The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) is used to convert the TRUE and FALSE values from EXACT into 1s and 0s, which are then summed by the SUM function. If SUM returns a positive number (which evaluates to TRUE in Excel), it means the _v_ already exists in _a_, and IF returns _a_. If SUM returns zero (which evaluates to FALSE in Excel), it means _v_ does not yet exist in _a_, and IF runs the VSTACK function, which is configured to combine _a_ and _v_ by stacking _v_ vertically below _a_.

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

[![Excel formula: Unique values with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20with%20criteria.png "Excel formula: Unique values with criteria")](https://exceljet.net/formulas/unique-values-with-criteria)

### [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove limit data to values associated with group A only: FILTER(B5:B16,C5:C16=E4) Notice we are picking up the value "A" directly from the header in cell E4...

Related functions
-----------------

[![Excel REDUCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20reduce%20function.png "Excel REDUCE function")](https://exceljet.net/functions/reduce-function)

### [REDUCE Function](https://exceljet.net/functions/reduce-function)

The Excel REDUCE function applies a custom LAMBDA function to each element in a given array and accumulates results to a single value.

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel EXACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_%20exact.png "Excel EXACT function")](https://exceljet.net/functions/exact-function)

### [EXACT Function](https://exceljet.net/functions/exact-function)

The Excel EXACT function compares two text strings, taking into account upper and lower case characters, and returns TRUE if they are the same, and FALSE if not. EXACT is case-sensitive.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    
*   [Unique values with criteria](https://exceljet.net/formulas/unique-values-with-criteria)
    

### Functions

*   [REDUCE Function](https://exceljet.net/functions/reduce-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [EXACT Function](https://exceljet.net/functions/exact-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    

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