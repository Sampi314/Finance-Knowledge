# SUMPRODUCT count multiple OR criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria

---

[Skip to main content](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria#main-content)

[](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria#)

*   [Previous](https://exceljet.net/formulas/summary-count-with-percentage-breakdown)
    
*   [Next](https://exceljet.net/formulas/two-way-summary-count)
    

[Count](https://exceljet.net/formulas#Count)

SUMPRODUCT count multiple OR criteria
=====================================

by Dave Bruns · Updated 27 Jul 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")

Summary
-------

To count matching rows with multiple OR criteria, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in F10 is:

    =SUMPRODUCT(ISNUMBER(MATCH(B5:B11,{"A","B"},0))*
    ISNUMBER(MATCH(C5:C11,{"X","Y","Z"},0)))
    

This formula returns a count of rows where the value in column one is A or B and the value in column two is X, Y, or Z.

Generic formula
---------------

    =SUMPRODUCT(ISNUMBER(MATCH(rng1,{"A","B"},0))*ISNUMBER(MATCH(rng2,{"X","Y","Z"},0)))

Explanation 
------------

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using [array constants](https://exceljet.net/glossary/array-constant)
 to hold the values of interest, but the article also shows how to use cell references instead. In simple scenarios, you can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 and [the addition operator (+) to count with OR logic](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
, but as the number of values being testing increases, the formula becomes unwieldy. To keep the formula as tidy as possible, this example uses the [MATCH function](https://exceljet.net/functions/match-function)
 together with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 to check more than one value at a time.

### ISNUMBER + MATCH

Working from the inside out, each condition is applied with a separate ISNUMBER + MATCH expression. To generate a count of rows in column one where the value is A or B we use the following code:

    ISNUMBER(MATCH(B5:B11,{"A","B"},0)
    

Notice the values "A" and "B" are supplied as an [array constant](https://exceljet.net/glossary/array-constant)
 and _match\_type_ is set to zero for an exact match.

_Note: the configuration for MATCH may appear "reversed" from what you might expect. This is necessary in order to preserve the structure of the source data in the results returned by MATCH, i.e. we get back seven results, one for each row in B5:B11._

Since we give the [MATCH function](https://exceljet.net/functions/match-function)
 7 values to look for, MATCH returns an [array](https://exceljet.net/glossary/array)
 that contains 7 results like this:

    {1;2;#N/A;1;2;1;2}
    

Each number in this array represents a match on "A" or "B" in Column B (1="A", 2="B"). An #N/A error indicates a row where neither value was found. These results are delivered directly to the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
, which is used to convert the values from MATCH into simple TRUE and FALSE results:

    ISNUMBER({1;2;#N/A;1;2;1;2})
    

ISNUMBER returns a new array that looks like this:

    {TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE}
    

In this array, TRUE values represent rows where "A" or "B" were found in column B.  The next step is to test for "X","Y",or "Z" in column C, and for this we use exactly the same approach:

    ISNUMBER(MATCH(C5:C11,{"X","Y","Z"},0))
    

With the above configuration, the MATCH function returns the following array:

    {1;2;3;3;#N/A;1;2}
    

As before, the ISNUMBER function converts these results to TRUE and FALSE values and returns an array like this:

    {TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE}
    

We now have everything we need to perform the count, and for this we use the SUMPRODUCT function.

### SUMPRODUCT function

The final step in the formula is to tally up the rows that meet the criteria outlined above. In the example shown, the formula in F10 is:

    =SUMPRODUCT(ISNUMBER(MATCH(B5:B11,{"A","B"},0))*
    ISNUMBER(MATCH(C5:C11,{"X","Y","Z"},0)))

After the two MATCH and ISNUMBER expressions are evaluated, the formula simplifies to the following:

    =SUMPRODUCT({TRUE;TRUE;FALSE;TRUE;TRUE;TRUE;TRUE}*{TRUE;TRUE;TRUE;TRUE;FALSE;TRUE;TRUE})
    

Next, the two arrays are multiplied together inside SUMPRODUCT, which automatically converts TRUE FALSE values to 1s and 0s as a result of the math operation:

    =SUMPRODUCT({1;1;0;1;1;1;1}*{1;1;1;1;0;1;1})
    

Once the two arrays are multiplied together, we have a single array like this:

    =SUMPRODUCT({1;1;0;1;0;1;1}) // returns 5
    

In this array, a 1 signifies a row that meets all criteria and a 0 indicates a row that does not. With just a single array to process, SUMPRODUCT sums the array and returns a final result of 5.

### With cell references

The example above uses hardcoded array constants, but you can also use cell references:

    =SUMPRODUCT(ISNUMBER(MATCH(B5:B11,E5:E6,0))*ISNUMBER(MATCH(C5:C11,F5:F7,0)))
    

This approach can be "scaled up" to handle more criteria. You can [see an example in this formula challenge](https://exceljet.net/challenges/formula-challenge-multiple-or-criteria)
.

_Note: The SUMPRODUCT function is used below for compatibility with [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. In the current version of Excel, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead. For more on this topic, see: [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

Related formulas
----------------

[![Excel formula: Count rows with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20multiple%20OR%20criteria.png "Excel formula: Count rows with multiple OR criteria")](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

### [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

In this example, the goal is to count rows using OR logic based on the criteria shown in column F. For example, in cell G5 we want to count rows where Color is "Blue" OR Pet is "Dog". This can be done with Boolean logic and the SUMPRODUCT function , as explained below. Notes This formula uses an...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: Count matching values in matching columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20matching%20values%20in%20matching%20columns.png "Excel formula: Count matching values in matching columns")](https://exceljet.net/formulas/count-matching-values-in-matching-columns)

### [Count matching values in matching columns](https://exceljet.net/formulas/count-matching-values-in-matching-columns)

In this example, the goal is to count "z" or "c" values in the named range data , but only when the column header is "A" or "B". The formula used to perform this calculation is based on the SUMPRODUCT function : =SUMPRODUCT(ISNUMBER(MATCH(headers,{"A","B"},0))\*ISNUMBER(MATCH(data,{"z","c"},0)))...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Count matching values in matching columns](https://exceljet.net/formulas/count-matching-values-in-matching-columns)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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