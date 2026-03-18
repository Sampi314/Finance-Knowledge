# Break ties with helper column and COUNTIF - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/break-ties-with-helper-column-and-countif

---

[Skip to main content](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif#main-content)

[](https://exceljet.net/formulas/break-ties-with-helper-column-and-countif#)

*   [Previous](https://exceljet.net/formulas/data-validation-with-conditional-list)
    
*   [Next](https://exceljet.net/formulas/rank-function-example)
    

[Rank](https://exceljet.net/formulas#Rank)

Break ties with helper column and COUNTIF
=========================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[SMALL](https://exceljet.net/functions/small-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Break ties with helper column and COUNTIF](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/break%20ties%20with%20helper%20column%20and%20COUNTIF.png "Excel formula: Break ties with helper column and COUNTIF")

Summary
-------

To break ties, you can use a [helper column](https://exceljet.net/glossary/helper-column)
 and the [COUNTIF function](https://exceljet.net/functions/countif-function)
 to adjust values so that they don't contain duplicates, and therefore won't result in ties. In the example shown, the formula in D5 is:

    =C5+(COUNTIF($C$5:C5,C5)-1)*0.01
    

_Note: in Excel 2021 and later, a better approach to this kind of problem is to use the [FILTER function](https://exceljet.net/functions/filter-function)
 as [explained here](https://exceljet.net/formulas/filter-on-top-n-values)
._

Generic formula
---------------

    =A1+(COUNTIF(exp_rng,A1)-1)*adjustment

Explanation 
------------

In this example, the goal is to retrieve information about the lowest three estimates in the data shown. The problem is that there are some duplicate values in the estimate column. This means we will have some trouble trying to display the names of the 2nd and 3rd lowest suppliers because the tie values will cause INDEX to return the same name. One way to break ties like this is to add a helper column with values that have been adjusted, and then rank those values instead of the originals. In this example, the logic used to adjust values is random - the first duplicate value will "win", but you can adjust the formula to use logic that fits your particular situation and use case.

### COUNTIF with expanding reference

At the core, this formula uses the COUNTIF function and an expanding range to count occurrences of values. The [expanding reference](https://exceljet.net/glossary/expanding-reference)
 is used so that COUNTIFS returns a [running count of occurrences](https://exceljet.net/formulas/running-count-of-occurrence-in-list)
, instead of a total count for each value:

    COUNTIF($C$5:C5,C5)
    

Next, 1 is subtracted from the result (which makes the count of all non-duplicate values zero) and the result is multiplied by 0.01. This value is the "adjustment", and is intentionally small so as not to materially impact the original value.

In the example shown, Metrolux and Diamond both have the same estimate of $5000. Since Metrolux appears first in the list, the running count of 5000 is 1 and is canceled out by subtracting 1, so the estimate remains unchanged in the helper column:

    =C8+(COUNTIF($C$5:C8,C8)-1)*0.01
    =C8+(1-1)*0.01
    =C8+0
    =C8
    

However, for Diamond, the running count of 5000 is 2, so the estimate is adjusted:

    =C11+(COUNTIF($C$5:C11,C11)-1)*0.01
    =C11+(2-1)*0.01
    =C11+1*0.01
    =C11+0.01
    

Finally, the adjusted values are used for ranking instead of the original values in columns G and H. The formula in G5 is:

    =SMALL($D$5:$D$12,F5)
    
    

The formula in H5:

    =INDEX($B$5:$B$12,MATCH(G5,$D$5:$D$12,0))
    

For a detailed explanation of these formulas, [see this example](https://exceljet.net/formulas/find-lowest-n-values)
.

### Temporary helper column

If you don't want to use a helper column in the final solution, you can use a helper column temporarily to get calculated values, then use Paste Special to convert values "in place" and delete the helper column afterward. [This video](https://exceljet.net/videos/shortcuts-for-paste-special)
 demonstrates the technique.

Related formulas
----------------

[![Excel formula: nth smallest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_smallest_value.png "Excel formula: nth smallest value")](https://exceljet.net/formulas/nth-smallest-value)

### [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)

In this example, the goal is to extract the 3 best race times for each name from the 5 race times that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the fastest time, the 2nd fastest time, and the 3rd fastest time. This problem can be solved with the SMALL...

[![Excel formula: nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/nth_largest_value.png "Excel formula: nth largest value")](https://exceljet.net/formulas/nth-largest-value)

### [nth largest value](https://exceljet.net/formulas/nth-largest-value)

In this example, the goal is to extract the top 3 quiz scores for each name from the 5 scores that appear in columns C, D, E, F, and G. In other words, for each name listed, we want the best score, the 2nd best score, and the 3rd best score. This problem can be solved with the LARGE function. Note...

[![Excel formula: Sum bottom n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20bottom%20n%20values.png "Excel formula: Sum bottom n values")](https://exceljet.net/formulas/sum-bottom-n-values)

### [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)

In this example, the goal is to sum the smallest n values in a set of data, where n is a variable that can be easily changed. At a high level, the solution breaks down into two steps (1) extract the n smallest values from the data set and (2) sum the extracted values. This problem can be solved...

[![Excel formula: Find lowest n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Find%20lowest%20n%20values.png "Excel formula: Find lowest n values")](https://exceljet.net/formulas/find-lowest-n-values)

### [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)

The SMALL function retrieves the smallest values from data based on a given rank. For example: =SMALL(range,1) // smallest =SMALL(range,2) // 2nd smallest =SMALL(range,3) // 3rd smallest In the worksheet shown, the rank (which is provided to SMALL as the k argument) comes from numbers in column E...

Related functions
-----------------

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20get%20nth%20values%20with%20SMALL%20and%20LARGE_thumb.png)](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

In this video we'll look at how to calculate the "nth" smallest or largest values in a range using the SMALL or LARGE function s. This would be, for example, the 1st, 2nd, and 3rd smallest or largest values. In this first sheet, we have a list of students with five test scores. I'll use the LARGE...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [nth smallest value](https://exceljet.net/formulas/nth-smallest-value)
    
*   [nth largest value](https://exceljet.net/formulas/nth-largest-value)
    
*   [Sum bottom n values](https://exceljet.net/formulas/sum-bottom-n-values)
    
*   [Find lowest n values](https://exceljet.net/formulas/find-lowest-n-values)
    

### Functions

*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to get nth values with SMALL and LARGE](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)
    

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