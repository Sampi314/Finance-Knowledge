# Count total matches in two ranges - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-total-matches-in-two-ranges

---

[Skip to main content](https://exceljet.net/formulas/count-total-matches-in-two-ranges#main-content)

[](https://exceljet.net/formulas/count-total-matches-in-two-ranges#)

*   [Previous](https://exceljet.net/formulas/count-sold-and-remaining)
    
*   [Next](https://exceljet.net/formulas/count-unique-dates)
    

[Count](https://exceljet.net/formulas#Count)

Count total matches in two ranges
=================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[MATCH](https://exceljet.net/functions/match-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[COUNT](https://exceljet.net/functions/count-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7400/download?token=LkUYAnSt)
 (14.32 KB)

![Excel formula: Count total matches in two ranges](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20total%20matches%20in%20two%20ranges.png "Excel formula: Count total matches in two ranges")

Summary
-------

To count total matches in two ranges, you can use a formula that combines the [COUNTIF function](https://exceljet.net/functions/countif-function)
 with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in cell F5 is:

    =SUMPRODUCT(COUNTIF(range1,range2))
    

where **range1** (B5:B16) and **range2** (D5:D13) are [named ranges](https://exceljet.net/glossary/named-range)
.

_Note: this formula does not care about the location or order of the items in each range._

Generic formula
---------------

    =SUMPRODUCT(COUNTIF(range1,range2))

Explanation 
------------

In this example, the goal is to count the number of exact matches in two ranges, ignoring the sort order or location of the values in each range. This problem can be solved with the COUNTIF function or with the MATCH function. Each approach is explained below.

_Note: Both formulas below use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to "tally up" the final count, because SUMPRODUCT [handles arrays natively](https://exceljet.net/articles/why-sumproduct)
 in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. In the current version of Excel, which supports [dynamic arrays](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead._

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 counts values in a range that meet supplied criteria. Normally, you would give COUNTIF a range like A1:A10 and criteria like "red":

    =COUNTIF(A1:A10,"red")  // count "red" cells
    

COUNTIF would then return a count of cells in A1:A10 that are equal to "red". In this case, however, we are giving COUNTIF a _range_ of values for criteria, which causes COUNTIF to return a count for each value. The formula in cell F5 is:

    =SUMPRODUCT(COUNTIF(range1,range2))
    

Working from the inside out, we provide **range1** (B5:B16) for _range_ and **range2** (D5;D13) for _criteria:_

    COUNTIF(range1,range2)
    

Because we are giving COUNTIF a range that contains 9 values for _criteria_, COUNTIF will return 9 counts in an [array](https://exceljet.net/glossary/array)
 like this:

    {1;1;1;0;0;1;1;1;1}
    

Each item in this array represents a count. A positive number represents the count of a value in **range2** that was found in **range1**. A zero indicates a value that was not found. COUNTIF returns this array of counts directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
:

    =SUMPRODUCT({1;1;1;0;0;1;1;1;1}) // returns 7
    

With just one array to process, SUMPRODUCT sums the array and returns 7 as a final result.

### MATCH function

Another way to solve this problem is with the [MATCH function](https://exceljet.net/functions/match-function)
 like this:

    =SUMPRODUCT(--ISNUMBER(MATCH(range1,range2,0)))
    

Working from the inside out, the MATCH function is configured with **range1** as _lookup\_value_, **range2** as _lookup\_array_, and _match\_type_ as 0 for an exact match.:

    MATCH(range1,range2,0)
    

Because we are asking MATCH to find 12 values, we get back an array with 12 results like this:

    {8;#N/A;#N/A;1;9;6;#N/A;2;#N/A;7;#N/A;3}
    

In this array, a number represents the position of a matched value, and the #N/A error indicates a value that was _not found_. To convert this array to TRUE and FALSE values, we use the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
:

    --ISNUMBER({8;#N/A;#N/A;1;9;6;#N/A;2;#N/A;7;#N/A;3})
    

ISNUMBER returns TRUE for any number and FALSE for anything else, so the resulting array looks like this:

    {TRUE;FALSE;FALSE;TRUE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE;TRUE}
    

By default, the SUMPRODUCT function will ignore the logical values TRUE and FALSE, so we use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values to 1s and 0s.  The resulting array is returned to the SUMPRODUCT function:

    =SUMPRODUCT({1;0;0;1;1;1;0;1;0;1;0;1}) // returns 7
    

With only one array to process, SUMPRODUCT sums the array and returns a final result of 7.

### MATCH with COUNT

As I mentioned above, in the current version of Excel, which supports [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of the SUMPRODUCT function like this:

    =SUM(--ISNUMBER(MATCH(range1,range2,0)))
    

The reason SUMPRODUCT is traditionally used is that it [avoids the requirement of entering the formula as an array formula](https://exceljet.net/articles/why-sumproduct)
 with control + shift + enter in older versions of Excel. However, an interesting result of [dynamic arrays](https://exceljet.net/glossary/dynamic-array)
 in Excel is that they make new solutions possible, because the native array behavior affects older functions as well. For example, in the current version of Excel, we can use the [COUNT function](https://exceljet.net/functions/count-function)
 directly like this:

    =COUNT(MATCH(range1,range2,0))
    

COUNT is programmed to count only numeric values — it returns the count of numbers in the array returned by MATCH and simply ignores the #N/A errors. The formula evaluates like this:

    =COUNT(MATCH(range1,range2,0))
    =COUNT({8;#N/A;#N/A;1;9;6;#N/A;2;#N/A;7;#N/A;3})
    =7
    

To be clear, this formula will also work in older versions of Excel. However, it must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with control + shift + enter. In the [current version of Excel](https://exceljet.net/glossary/dynamic-excel)
, it just works.

### Match across rows

The formulas above do not care about the location of values in the two ranges. If you want to compare two ranges and count matches at the row level (i.e. only count matches when the same item appears in the same position), you'll need a [different formula](https://exceljet.net/formulas/count-matches-between-two-columns)
.

Related formulas
----------------

[![Excel formula: Count if two criteria match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20if%20two%20criteria%20match.png "Excel formula: Count if two criteria match")](https://exceljet.net/formulas/count-if-two-criteria-match)

### [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)

In this example, the goal is to count orders where the color is "blue" and the quantity is greater than 15. All data is in the range B5:B15. There are two primary ways to solve this problem, one with the COUNTIFS function, the other with the SUMPRODUCT function. Both approaches are explained below...

[![Excel formula: Count sold and remaining](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20sold%20and%20remaining.png "Excel formula: Count sold and remaining")](https://exceljet.net/formulas/count-sold-and-remaining)

### [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)

In this example, the goal is to count the number of items sold and remaining, based on the data visible in columns B and C. The ID column holds unique ids, and the Sold column is used to record a sale. An "x" in the Sold column indicates the item has been sold. As is typical in Excel, there are...

[![Excel formula: Count matches between two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20matches%20between%20two%20columns.png "Excel formula: Count matches between two columns")](https://exceljet.net/formulas/count-matches-between-two-columns)

### [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)

In this example, the goal is to compare two columns and return the count of matches in corresponding rows. A good way to solve this problem is to use the SUMPRODUCT function or the SUM function, as explained below. SUMPRODUCT function The SUMPRODUCT function is a versatile function that handles...

[![Excel formula: Filter to extract matching values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20to%20extract%20matching%20values.png "Excel formula: Filter to extract matching values")](https://exceljet.net/formulas/filter-to-extract-matching-values)

### [Filter to extract matching values](https://exceljet.net/formulas/filter-to-extract-matching-values)

This formula relies on the FILTER function to retrieve data based on a logical test built with the COUNTIF function: =FILTER(list1,COUNTIF(list2,list1)) working from the inside out, the COUNTIF function is used to create the actual filter: COUNTIF(list2,list1) Notice we are using list2 as the range...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20find%20missing%20values%20with%20COUNTIF-Thumb.png)](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

### [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)

In this video we'll take a look at how to use the COUNTIF function to solve a common problem: how to find values in one list that appear in another list. Or, how to find values in a list that don't appear in another list. Let's take a look. In this worksheet, on the left, I have a list of 20 names...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count if two criteria match](https://exceljet.net/formulas/count-if-two-criteria-match)
    
*   [Count sold and remaining](https://exceljet.net/formulas/count-sold-and-remaining)
    
*   [Count matches between two columns](https://exceljet.net/formulas/count-matches-between-two-columns)
    
*   [Filter to extract matching values](https://exceljet.net/formulas/filter-to-extract-matching-values)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    

### Videos

*   [How to find missing values with COUNTIF](https://exceljet.net/videos/how-to-find-missing-values-with-countif)
    

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