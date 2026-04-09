# Most frequent text with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/most-frequent-text-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/most-frequent-text-with-criteria#main-content)

[](https://exceljet.net/formulas/most-frequent-text-with-criteria#)

*   [Previous](https://exceljet.net/formulas/make-words-plural)
    
*   [Next](https://exceljet.net/formulas/most-frequently-occurring-text)
    

[Text](https://exceljet.net/formulas#Text)

Most frequent text with criteria
================================

by Dave Bruns · Updated 16 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[MODE](https://exceljet.net/functions/mode-function)

[IF](https://exceljet.net/functions/if-function)

![Excel formula: Most frequent text with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/most%20frequent%20text%20with%20criteria.png "Excel formula: Most frequent text with criteria")

Summary
-------

To find the most frequently occurring text in a range, based on the criteria you supply, you can use an array formula based on several Excel functions, including [INDEX](https://exceljet.net/functions/index-function)
, [MATCH](https://exceljet.net/functions/match-function)
, [MODE](https://exceljet.net/functions/mode-function)
, and [IF](https://exceljet.net/functions/if-function)
. In the example shown, the formula in G5 is:

    =INDEX(supplier,MODE(IF(client=F5,MATCH(supplier,supplier,0))))
    

where "supplier" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C15, and "client" is the named range B5:B15.

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter, except in [Excel 365](https://exceljet.net/glossary/excel-365)
._

Generic formula
---------------

    =INDEX(rng1,MODE(IF(rng2=criteria,MATCH(rng1,rng1,0))))

Explanation 
------------

In this example, the goal is to return the most frequently occurring text based on one or more supplied criteria. Working from the inside out, we use the [MATCH function](https://exceljet.net/functions/match-function)
 to match the text range against itself, by giving MATCH the same range for lookup value and lookup array, with zero for match type:

    MATCH(supplier,supplier,0)
    

Since the lookup value is an array with 10 values, MATCH returns an [array](https://exceljet.net/glossary/array)
 of 10 results:

    {1;1;3;3;5;1;7;3;1;5;5}
    

Each item in this array represents the first position at which a supplier name appears in the data. This array is fed into the [IF function](https://exceljet.net/videos/the-if-function)
, which is used to filter results for Client A only:

    IF(client=F5,{1;1;3;3;5;1;7;3;1;5;5})
    

IF returns the filtered array to the [MODE function](https://exceljet.net/functions/mode-function)
:

    {1;FALSE;3;FALSE;5;1;FALSE;FALSE;1;5;FALSE}
    

Notice only positions associated with Client A remain in the array. MODE ignores FALSE values and returns the most frequently occurring number to the [INDEX function](https://exceljet.net/functions/index-function)
 as the row number:

    =INDEX(supplier,1)
    

Finally, with the [named range](https://exceljet.net/glossary/named-range)
 "supplier" as the array, INDEX returns "Brown", the most frequently occurring supplier for Client A.

### Mode of text from every other row

Following the example above, the formula below has been adapted to return the most frequent text from every other row. The formulas in E5 and E6 are:

    =INDEX(text,MODE(IF(MOD(ROW(text),2)=1,MATCH(text,text,0)))) // odd
    =INDEX(text,MODE(IF(MOD(ROW(text),2)=0,MATCH(text,text,0)))) // even
    

![Formula for mode of text in every other row](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/mode%20of%20text%20from%20every%20other%20row.png?itok=ZXYst5-a "Formula for mode of text in every other row")

The overall structure of the formulas above is the same as the original example above. The key difference is the logical test used to check even and odd rows with the [named range](https://exceljet.net/glossary/named-range)
 **text** (B5:B15). Both formulas use the [MOD function](https://exceljet.net/functions/mod-function)
 with a divisor of 2:

    MOD(ROW(text),2)=1 // check for odd
    MOD(ROW(text),2)=0 // check for even
    

If the remainder is 1, we have an odd row. If the remainder is 0 (zero), we have an even row. These tests act as a filter for incoming text so that the result from the first formula is the most frequently occurring text in odd rows, and the result from the second formula is the most frequently occurring text in even rows.

Related formulas
----------------

[![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")](https://exceljet.net/formulas/most-frequently-occurring-text)

### [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5). Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number...

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

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

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

*   [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)
    
*   [Summary count with COUNTIF](https://exceljet.net/formulas/summary-count-with-countif)
    
*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    
*   [List most frequently occurring numbers](https://exceljet.net/formulas/list-most-frequently-occurring-numbers)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [MODE Function](https://exceljet.net/functions/mode-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    

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