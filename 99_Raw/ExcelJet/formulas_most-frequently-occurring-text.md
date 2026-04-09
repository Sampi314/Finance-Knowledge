# Most frequently occurring text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/most-frequently-occurring-text

---

[Skip to main content](https://exceljet.net/formulas/most-frequently-occurring-text#main-content)

[](https://exceljet.net/formulas/most-frequently-occurring-text#)

*   [Previous](https://exceljet.net/formulas/most-frequent-text-with-criteria)
    
*   [Next](https://exceljet.net/formulas/normalize-text)
    

[Text](https://exceljet.net/formulas#Text)

Most frequently occurring text
==============================

by Dave Bruns · Updated 25 Apr 2022

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MODE](https://exceljet.net/functions/mode-function)

![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")

Summary
-------

To extract the text value that occurs most frequently in a range, you can use a formula based on several functions INDEX, MATCH, and MODE. In the example shown, the formula in H5 is:

    =INDEX(B5:F5,MODE(MATCH(B5:F5,B5:F5,0)))
    

The result is the text value that occurs most in the given range.

_Note: If you need to output a list of the most frequently occurring text values, [this Excel 365 formula](https://exceljet.net/formulas/10-most-common-text-values)
 is a more complete solution._

Generic formula
---------------

    =INDEX(rng,MODE(MATCH(rng,rng,0)))

Explanation 
------------

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5).

Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number represents a position. In the example shown, the array looks like this:

    {1,2,1,2,2}
    

Wherever "dog" appears, we see 2, and Wherever "cat" appears, we see 1. That's because the MATCH function always returns the first match, which means subsequent occurrences of a given value will return the same (first) position.

Next, this array is fed into the MODE function. MODE returns the most frequently occurring number, which in this case is 2. The number 2 represents the position at which we'll find the most frequently occurring value in the range.

Finally, we need to extract the value itself. For this, we use the INDEX function. For array, we use the range of values (B5:F5). The row number is provided by MODE.

INDEX returns the value at position 2, which is "dog".

### Empty cells

To deal with empty cells, you can use the following array formula, which adds an IF statement to test for empty cells:

    {=INDEX(B5:F5,MODE(IF(B5:F5<>"",MATCH(B5:F5,B5:F5,0))))}
    

This is an [array formula](https://exceljet.net/glossary/array-formula)
, and must be entered with control + shift + enter.

Related formulas
----------------

[![Excel formula: Most frequent text with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text%20with%20criteria.png "Excel formula: Most frequent text with criteria")](https://exceljet.net/formulas/most-frequent-text-with-criteria)

### [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)

In this example, the goal is to return the most frequently occurring text based on one or more supplied criteria. Working from the inside out, we use the MATCH function to match the text range against itself, by giving MATCH the same range for lookup value and lookup array, with zero for match type...

[![Excel formula: Summary count with COUNTIF](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20with%20COUNTIF.png "Excel formula: Summary count with COUNTIF")](https://exceljet.net/formulas/summary-count-with-countif)

### [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)

In this example, the goal is to return a count for each color that appears in column C, using the color values already in column E as criteria. When working with data, a common need is to perform summary calculations that show total counts in different ways. For example, total counts by category,...

[![Excel formula: Most frequently occurring number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequently%20occurring%20number.png "Excel formula: Most frequently occurring number")](https://exceljet.net/formulas/most-frequently-occurring-number)

### [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)

The MODE function is fully automatic and will return the most frequently occurring number in a set of numbers. For example: =MODE(1,2,4,4,5,5,5,6) // returns 5 In the example shown, we give MODE the range B4:K4, so the formula is solved like this: =MODE(B4:K4) =MODE({1,2,2,1,1,2,2,2,1,1}) =2

[![Excel formula: List most frequently occurring numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20most%20frequently%20occuring%20numbers.png "Excel formula: List most frequently occurring numbers")](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

### [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)

The core of this formula is the MODE function, which returns the most frequently occurring number in a range or array. The rest of the formula just constructs a filtered array for MODE to use in each row. The expanding range $D$4:D4 works to exclude numbers already output in $D$4:D4. Working from...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel MODE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mode%20function.png "Excel MODE function")](https://exceljet.net/functions/mode-function)

### [MODE Function](https://exceljet.net/functions/mode-function)

The Excel MODE function returns the most frequently occurring number in a numeric data set. For example, =MODE(1,2,4,4,5,5,5,6) returns 5.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20MATCH%20Function%20for%20exact%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

### [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)

The MATCH function finds the relative position of an item in a list. MATCH can find exact matches or approximate matches. In this video, we'll look at how to use MATCH to find an exact match. The MATCH function takes three arguments: the lookup\_value, which is the value you're looking up, the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)
    
*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    
*   [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to use the MATCH Function for exact matches](https://exceljet.net/videos/how-to-use-the-match-function-for-exact-matches)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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