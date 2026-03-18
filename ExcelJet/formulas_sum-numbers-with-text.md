# Sum numbers with text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-numbers-with-text

---

[Skip to main content](https://exceljet.net/formulas/sum-numbers-with-text#main-content)

[](https://exceljet.net/formulas/sum-numbers-with-text#)

*   [Previous](https://exceljet.net/formulas/sort-values-by-columns)
    
*   [Next](https://exceljet.net/formulas/textsplit-get-numeric-values)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sum numbers with text
=====================

by Dave Bruns · Updated 9 Jun 2022

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[UNIQUE](https://exceljet.net/functions/unique-function)

[LET](https://exceljet.net/functions/let-function)

[LAMBDA](https://exceljet.net/functions/lambda-function)

[BYROW](https://exceljet.net/functions/byrow-function)

![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")

Summary
-------

To sum numbers that appear inside a [text string](https://exceljet.net/glossary/text-value)
, you can use a formula based on the [SUM function](https://exceljet.net/functions/sum-function)
, with help from several other functions including [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
, [TEXTAFTER](https://exceljet.net/functions/textafter-function)
, [UNIQUE](https://exceljet.net/functions/unique-function)
, and others. In the example shown, the formula in F4 is:

    =SUM(--TEXTAFTER(data," "))
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16, and each text string includes both a label and a number separated by a single space (" "). See below for more details and for the formulas used to generate the summary table in E7:F9.

Generic formula
---------------

    =SUM(--TEXTAFTER(data," "))

Explanation 
------------

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B16.

### Total sum

To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5 is:

    =SUM(--TEXTAFTER(data," "))
    

Working from the inside out, the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 is used to extract the numbers like this:

    TEXTAFTER(data," ") // get all numbers
    

TEXTAFTER is configured to extract the text that occurs after a single space character (" "). Because we are giving TEXTAFTER 12 separate text strings in **data** (B5:B16), TEXTAFTER returns 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {"10";"25";"25";"5";"50";"15";"10";"15";"12";"12";"10";"5"}
    

Notice that at this point the numbers are still text, as you can see by the double quotes ("). To coerce these text strings into actual numbers, we use a [double negative](https://exceljet.net/glossary/double-unary)
 (--):

    --{"10";"25";"25";"5";"50";"15";"10";"15";"12";"12";"10";"5"}
    

The result is an array that contains numbers only:

    {10;25;25;5;50;15;10;15;12;12;10;5}
    

This array is returned directly to the SUM function:

    =SUM({10;25;25;5;50;15;10;15;12;12;10;5}) // returns 194
    

SUM returns 194 as the final result.

### Summary table in two parts

One easy way to create the summary table seen in the worksheet is to use two formulas, one to list unique colors, and one to sum the numbers associated with each color. To list the unique colors starting in cell E8, you can use:

    =UNIQUE(TEXTBEFORE(B5:B16," ")) // unique colors
    

This is a variation of the formula explained above. Instead of using TEXTAFTER, we are using the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
 to get the text before the space (" "):

    TEXTBEFORE(B5:B16," ") // get all colors
    

TEXTBEFORE returns an array of 12 colors like this:

    {"Red";"Blue";"Green";"White";"Black";"Red";"Blue";"Green";"White";"Black";"Red";"Blue"}
    

This array is returned directly to the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
, which returns an array with 5 unique colors:

    {"Red";"Blue";"Green";"White";"Black"}
    

The array is returned to cell E8, and [spills](https://exceljet.net/glossary/spill)
 into the range E8:E12.

To sum the numbers associated with each color in column F, you can enter this formula in cell F8 and copy it down:

    =SUM((TEXTBEFORE(data," ")=E8)*TEXTAFTER(data," "))
    

Note: we can't use the [SUMIF function](https://exceljet.net/functions/sumif-function)
 in this case (which would be easier) because we don't have the colors without numbers in an actual [range](https://exceljet.net/glossary/range)
. Instead, the colors exist in an [array](https://exceljet.net/glossary/array)
 returned by the TEXTBEFORE function. [SUMIF requires a range](https://exceljet.net/articles/excels-racon-functions)
 for the _range_ argument.

### All-in-one summary table

To create an all-in-one summary table that lists the unique dates along with a count for each date, you can use an advanced formula like this:

    LET(
        c, TEXTBEFORE(data, " "),
        n, --TEXTAFTER(data, " "),
        u, UNIQUE(c),
        HSTACK(
            u,
            BYROW(u, LAMBDA(x, SUM(--(c = x) * n)))
        )
    

This is how the formula looks in the worksheet:

![sum numbers with text all in one lambda formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/sum%20numbers%20with%20text%20all%20in%20one%20formula.png?itok=Jzh8SU-c "sum numbers with text all in one lambda formula")

This formula utilizes the same patterns used in the formulas explained above, but now we move into more advanced functions like LET, LAMBDA, and BYROW.

The [LET function](https://exceljet.net/functions/let-function)
 is used to assign intermediate results to named variables. First, we use TEXTBEFORE to separate the colors from the numbers and assign the result to c. We use TEXTAFTER to separate the numbers and assign the result to n. Then we feed c into UNIQUE (to get _unique_ colors) and assign the result to u. Next, we use the [HSTACK function](https://exceljet.net/functions/hstack-function)
 to combine two arrays. _Array1_ is u (the unique colors), and _array2_ is generated with the [BYROW function](https://exceljet.net/functions/byrow-function)
:

    BYROW(u, LAMBDA(x, SUM(--(c = x) * n)))
    

BYROW loops through each unique color in u and runs a custom LAMBDA function to sum the numbers associated with each color:

    LAMBDA(x, SUM(--(c = x) * n))
    

The sum is generated with [boolean logic](https://exceljet.net/glossary/boolean-logic)
 and the [SUM function](https://exceljet.net/functions/sum-function)
:

    SUM(--(c = x) * n)
    

The first part of the expression checks all colors (c) against the current row (x), generating an array of TRUE and FALSE values:

    --(c = x)
    

The [double negative](https://exceljet.net/glossary/double-unary)
 (--) converts the TRUE and FALSE values to 1s and 0s. This array is then multiplied by all numbers (n). The numbers that survive are associated with the current row color (x) and the other numbers are converted to zero. SUM then returns the result for that row.

_Note: Technically, the double negative (--) operation is not needed above because the multiplication step will automatically coerce the TRUE and FALSE values to 1s and 0s. However, it does no harm and perhaps makes the pattern of this formula easier to understand. In addition, if you remove the multiplication step, the result will be a count of each color rather than a sum. So the double negative allows the count variation of the formula to work without further adjustment._

The final result from the BYROW is an array with 5 sums:

    {35;40;40;17;62}
    

This array is returned to HSTACK as _array2_. HSTACK joins _array1_ and _array2_ together horizontally, and returns a 2-column array as a final result.

Related formulas
----------------

[![Excel formula: Count unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20values.png "Excel formula: Count unique values")](https://exceljet.net/formulas/count-unique-values)

### [Count unique values](https://exceljet.net/formulas/count-unique-values)

This example uses the UNIQUE function to extract unique values. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. These are returned directly to the COUNTA function as an array like this: =COUNTA({"red";"amber";"green";"blue";"...

[![Excel formula: Count unique dates ignore time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20unique%20dates%20ignore%20time.png "Excel formula: Count unique dates ignore time")](https://exceljet.net/formulas/count-unique-dates-ignore-time)

### [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)

In this example, the goal is to count the unique dates in a range of timestamps (i.e. dates that contain dates and times). In addition, we also want to create the table of results seen in E7:F9. For convenience, data is the named range B5:B16. Basic count To get a count of individual dates that...

Related functions
-----------------

[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)

### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)

The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel LAMBDA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lambda.png "Excel LAMBDA function")](https://exceljet.net/functions/lambda-function)

### [LAMBDA Function](https://exceljet.net/functions/lambda-function)

The Excel LAMBDA function provides a way to create custom functions that can be reused throughout a workbook, without VBA or macros.

[![Excel BYROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exxeljet%20byrow%20function.png "Excel BYROW function")](https://exceljet.net/functions/byrow-function)

### [BYROW Function](https://exceljet.net/functions/byrow-function)

The Excel BYROW function applies a function to each row of a given array and returns one result per row. BYROW can apply stock functions like SUM, COUNT, and AVERAGE or a custom LAMBDA function. All results are returned at the same time in a single array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count unique values](https://exceljet.net/formulas/count-unique-values)
    
*   [Count unique dates ignore time](https://exceljet.net/formulas/count-unique-dates-ignore-time)
    

### Functions

*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [LAMBDA Function](https://exceljet.net/functions/lambda-function)
    
*   [BYROW Function](https://exceljet.net/functions/byrow-function)
    

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