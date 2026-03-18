# Range contains one of many values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/range-contains-one-of-many-values

---

[Skip to main content](https://exceljet.net/formulas/range-contains-one-of-many-values#main-content)

[](https://exceljet.net/formulas/range-contains-one-of-many-values#)

*   [Previous](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    
*   [Next](https://exceljet.net/formulas/range-contains-specific-text)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Range contains one of many values
=================================

by Dave Bruns · Updated 4 Jan 2021

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[SEARCH](https://exceljet.net/functions/search-function)

![Excel formula: Range contains one of many values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Range%20contains%20one%20of%20many%20values.png "Excel formula: Range contains one of many values")

Summary
-------

To test if one of several values exists in a range of cells, you can use a formula based on the SUMPRODUCT function. In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(--(rng=B5:D5))>0
    

where "rng" is the [named range](https://exceljet.net/glossary/named-range)
 H4:H10 and contains the values to look for.

Generic formula
---------------

    =SUMPRODUCT(--(rng=values))>0

Explanation 
------------

Each item in **rng** is compared to each item in values and the result is an array of TRUE or FALSE values.

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 will force the TRUE and FALSE values to 1 and 0 respectively. Since SUMPRODUCT receives just one array, it simply adds up the items in the array and returns the result.

Logically, any result greater than zero means that at least one value exists in the range. So, the final step is to evaluate the SUMPRODUCT result to see if its greater than zero. Any result greater than zero returns TRUE, and any result equal to zero returns FALSE.

### With hard-coded values

You can also hard code the search values into the formula, using what is known as an "[array constant](https://exceljet.net/glossary/array-constant)
". For example, if you want to look for 3 values: red, cyan, and magenta inside the range H2:H8, you can use:

    =SUMPRODUCT(--(H2:H8={"red","cyan","magenta"}))>0
    

In the above example {"red","cyan","magenta"} is the array constant, which is one way to supply multiple values in a single argument.

### Partial matches or substrings

The formula above tests for equivalency only and will not find partial matches or substrings in the range. If you need to look for substrings, you can [use this formula instead](https://exceljet.net/formulas/range-contains-specific-text)
.

Related formulas
----------------

[![Excel formula: Value exists in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Value_exists_in_a_range.png "Excel formula: Value exists in a range")](https://exceljet.net/formulas/value-exists-in-a-range)

### [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)

In this example, the goal is to use a formula to check if a specific value exists in a range. The easiest way to do this is to use the COUNTIF function to count occurrences of a value in a range, then use the count to create a final result. COUNTIF function The COUNTIF function counts cells that...

[![Excel formula: Range contains specific text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20specific%20text.png "Excel formula: Range contains specific text")](https://exceljet.net/formulas/range-contains-specific-text)

### [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)

The COUNTIF function counts cells that meet supplied criteria, and returns a count of occurrences found. If no cells meet criteria, COUNTIF returns zero. The asterisk (\*) is a wildcard for one or more characters. By concatenating asterisks before and after the value in D5, the formula will count...

[![Excel formula: Range contains one of many substrings](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Range%20contains%20one%20of%20many%20substrings.png "Excel formula: Range contains one of many substrings")](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

### [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)

All the hard work is done by the COUNTIF function, which is configured to count the values in the named range "substrings" that appear the named range "rng" with like this: COUNTIF(rng,"\*"&substrings&"\*")) By wrapping substrings in the asterisks, Excel evaluates the formula like this: =...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel SEARCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20search.png "Excel SEARCH function")](https://exceljet.net/functions/search-function)

### [SEARCH Function](https://exceljet.net/functions/search-function)

The Excel SEARCH function returns the location of one text string inside another. SEARCH returns the position of _find\_text_ inside _within\_text_ as a number. SEARCH supports wildcards, and is _not_ case-sensitive....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Value exists in a range](https://exceljet.net/formulas/value-exists-in-a-range)
    
*   [Range contains specific text](https://exceljet.net/formulas/range-contains-specific-text)
    
*   [Range contains one of many substrings](https://exceljet.net/formulas/range-contains-one-of-many-substrings)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [SEARCH Function](https://exceljet.net/functions/search-function)
    

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