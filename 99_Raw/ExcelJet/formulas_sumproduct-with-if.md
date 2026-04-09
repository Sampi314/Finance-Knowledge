# SUMPRODUCT with IF - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumproduct-with-if

---

[Skip to main content](https://exceljet.net/formulas/sumproduct-with-if#main-content)

[](https://exceljet.net/formulas/sumproduct-with-if#)

*   [Previous](https://exceljet.net/formulas/sumifs-with-multiple-criteria-and-or-logic)
    
*   [Next](https://exceljet.net/formulas/average-and-ignore-errors)
    

[Sum](https://exceljet.net/formulas#Sum)

SUMPRODUCT with IF
==================

by Dave Bruns · Updated 6 Jan 2023

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: SUMPRODUCT with IF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sumproduct_with_if.png "Excel formula: SUMPRODUCT with IF")

Summary
-------

To create a conditional sum with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 you can use the [IF function](https://exceljet.net/functions/if-function)
 or use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. In the example shown, the formula in H5 is:

    =SUMPRODUCT(IF(C5:C16="red",1,0),D5:D16,E5:E16)
    

The result is $750, the total value of items with a color of "Red" in the data as shown. Note that SUMPRODUCT is _not_ case-sensitive. Using the IF function inside SUMPRODUCT makes this into an [array formula](https://exceljet.net/articles/what-is-an-array-formula)
 that must be entered with control + shift + enter in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. See below for an alternative Boolean syntax that does not need special handling.

Generic formula
---------------

    =SUMPRODUCT(IF(criteria,1,0),values)

Explanation 
------------

In this example, the goal is to calculate a conditional sum with the SUMPRODUCT function to match the criteria shown in G5:G7. One way to do this is to use the IF function directly inside of SUMPRODUCT. Another more common alternative is to use Boolean logic to apply criteria. Both approaches are explained below.

### Basic SUMPRODUCT

The SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. The classic SUMPRODUCT problem multiplies two ranges together and sums the product directly without a [helper column](https://exceljet.net/glossary/helper-column)
. For example, in the worksheet above, we have Quantity and Price, but no line item total. You can use SUMPRODUCT to get the total value of all records in the data like this:

    =SUMPRODUCT(D5:D16,E5:E16)

In the worksheet shown, the result is $1,882, the sum of all quantities in D5:D16 multiplied by all prices in E5:E16. This formula works nicely. However, it's not obvious how to calculate a _conditional sum_ with SUMPRODUCT. For example, how can you calculate the value of all records where the color is "Red"? One option is to use the [IF function](https://exceljet.net/functions/if-function)
 directly, as explained in the next section.

### SUMPRODUCT + IF function

One way to apply conditions with the SUMPRODUCT function is to use the IF function directly. This is the approach seen in the worksheet shown, where the formula in cell H5 is:

    =SUMPRODUCT(IF(C5:C16="red",1,0),D5:D16,E5:E16)

In this configuration, SUMPRODUCT has been given three arguments, _array1_, _array2_, and _array3_. Note that _array2_ holds Quantity and _array3_ holds Price. It is _array1_ that applies the conditional logic with the IF function like this:

    IF(C5:C16="red",1,0)

Notice we are using 1 and 0 for the _value\_if\_true_ and _value\_if\_false_ arguments instead of the default TRUE and FALSE values. We do this because we want a _numeric result_, for reasons that become clear below. Because there are 12 values in the range C5:C16, IF returns an array with 12 results like this:

    {1;0;1;0;0;0;1;0;0;0;1;1}

In this array, 1s indicate records where the color is "Red" and 0s indicate other colors. Dropping this array back into the SUMPRODUCT function, we have:

    =SUMPRODUCT({1;0;1;0;0;0;1;0;0;0;1;1},D5:D16,E5:E16)

Now you can see how the logic works. The Boolean values that make up _array1_ act like a filter when the arrays are multiplied together. After multiplication, there is just a single array like this:

    =SUMPRODUCT({150;0;210;0;0;0;120;0;0;0;126;144})

Note that the value of records where the color is not "Red" have been "zeroed out". The final result returned by SUMPRODUCT is $750. Additional conditions can be added with additional IF statements. To calculate a total for Color = "Red" and State = "TX", you can use the IF function twice like this:

    =SUMPRODUCT(IF(C5:C16="red",1,0),IF(B5:B16="tx",1,0),D5:D16,E5:E16)

The result is $270, as you can see in cell H6. The formula in cell H7 calculates a total for color = "Blue" and State = "CO" like this:

    =SUMPRODUCT(IF(C5:C16="blue",1,0),IF(B5:B16="co",1,0),D5:D16,E5:E16)

Although this formula works fine, one consequence of using the IF function inside of SUMPRODUCT is that it makes this into an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with control + shift + enter in older versions of Excel that do not support [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. This is a bit unexpected, because one of SUMPRODUCT's key strengths is the ability to handle [array operations](https://exceljet.net/glossary/array-operation)
 natively, but the IF function defeats this feature. The traditional solution to this problem is to switch to [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, as explained below.

### SUMPRODUCT + Boolean logic

An alternative to using the IF function directly inside of SUMPRODUCT is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. For example, to calculate the total value of records where the color is "Red", you can use a formula like this:

    =SUMPRODUCT(--(C5:C16="red"),D5:D16,E5:E16)

This example illustrates one of the key strengths of the SUMPRODUCT function – the ability to handle [array operations](https://exceljet.net/glossary/array-operation)
 natively. Inside SUMPRODUCT, the first [array](https://exceljet.net/glossary/array)
 is a logical expression to filter on the color "red":

    --(C5:C16="red")
    

SUMPRODUCT is not case-sensitive, so "red" will match "red", "Red", and "RED". Because there are 12 values in the range C5:C16, this expression returns an array with 12 results like this:

    --({TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;TRUE})

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) then converts the TRUE and FALSE values to 1s and zeros:

    {1;0;1;0;0;0;1;0;0;0}
    

Back in SUMPRODUCT, we now have:

    =SUMPRODUCT({1;0;1;0;0;0;1;0;0;0;1;1},D5:D16,E5:E16)

Notice this is the same result we had with the IF function example above. As before, _array1_ acts like a filter when the arrays are multiplied together. After multiplication, there is just a single array like this:

    =SUMPRODUCT({150;0;210;0;0;0;120;0;0;0;126;144})

All values associated with colors that are _not_ "Red" have been "zeroed out", and the final result is $750. As with the IF function, the same pattern can be repeated to add more conditions. To calculate a total for Color = "Red" and State = "TX", you can use a formula like this:

    =SUMPRODUCT(--(B5:B16="tx"),--(C5:C16="red"),D5:D16,E5:E16)

To calculate a total for color = "Blue" and State = "CO", the formula is:

    =SUMPRODUCT(--(B5:B16="co"),--(C5:C16="blue"),D5:D16,E5:E16)

### Simplifying with a single array

Excel pros will often simplify the syntax inside SUMPRODUCT by placing the conditional logic into a single argument like this

    =SUMPRODUCT((B5:B16="co")*(C5:C16="blue"),D5:D16,E5:E16)
    

One advantage of this approach is that the math operation in _array1_ automatically coerces TRUE and FALSE into 1s and 0s, so we don't need a [double negative](https://exceljet.net/glossary/double-unary)
 (--). Another advantage is that the math operation can be changed to apply a different type of logic. Instead of multiplication (\*), which corresponds to AND logic in [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
, you can use addition (+), which corresponds to OR logic. For example, to sum the value of all records that are either "Red" or "Blue", you could use a formula like this:

    =SUMPRODUCT((C5:C16="red")+(C5:C16="blue"),D5:D16,E5:E16)

As you can see, using Boolean logic with SUMPRODUCT is a flexible alternative to using the IF function, and it offers a major advantage: the formula will work fine in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, with no need to enter as an [array formula](https://exceljet.net/videos/what-is-an-array-formula)
 with control + shift + enter.

Related formulas
----------------

[![Excel formula: Subtotal by color](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/subtotal%20by%20color_0.png "Excel formula: Subtotal by color")](https://exceljet.net/formulas/subtotal-by-color)

### [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)

In this example, the goal is to subtotal (count and sum) values based on cell color. This is a tricky problem, because there is no Excel function that will let you count cells by color directly. There are several different approaches, as explained below. Standard formula logic If color is being...

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: Subtotal invoices by age](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Subtotal%20invoices%20by%20age.png "Excel formula: Subtotal invoices by age")](https://exceljet.net/formulas/subtotal-invoices-by-age)

### [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)

In this example, the goal is to subtotal invoices by age, where age represents the number of days since the invoice was issued. This problem can be solved with the SUMIFS function and the COUNTIFS function, as explained below. For convenience, age (E5:E16) and amount (D5:D16) are named ranges ...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/intro%20to%20boolean%20logic-thumb.png)](https://exceljet.net/videos/intro-to-boolean-logic)

### [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)

In this video, I'm going to show you the basics of Boolean logic. Boolean logic is a great tool for simplifying formulas, especially those with many IF statements. So, to start off, what's a Boolean? A Boolean is a data type with only two possible values, TRUE or FALSE. You'll often see Boolean...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20operations%20in%20array%20formulas-Play.png)](https://exceljet.net/videos/boolean-operations-in-array-formulas)

### [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)

In this video, we'll look at why boolean operations are important in array formulas. Boolean operations are a key building block in the world of dynamic array formulas. To illustrate, let's look at some simple order data. Given the data shown, how can we total orders from Texas using an array...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Subtotal by color](https://exceljet.net/formulas/subtotal-by-color)
    
*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [Subtotal invoices by age](https://exceljet.net/formulas/subtotal-invoices-by-age)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

### Videos

*   [Intro to Boolean Logic](https://exceljet.net/videos/intro-to-boolean-logic)
    
*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    
*   [Boolean operations in array formulas](https://exceljet.net/videos/boolean-operations-in-array-formulas)
    

### Articles

*   [The double negative in Excel formulas](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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