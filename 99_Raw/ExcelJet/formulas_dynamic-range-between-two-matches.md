# Dynamic range between two matches - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/dynamic-range-between-two-matches

---

[Skip to main content](https://exceljet.net/formulas/dynamic-range-between-two-matches#main-content)

[](https://exceljet.net/formulas/dynamic-range-between-two-matches#)

*   [Previous](https://exceljet.net/formulas/dynamic-named-range-with-offset)
    
*   [Next](https://exceljet.net/formulas/first-column-number-in-range)
    

[Range](https://exceljet.net/formulas#Range)

Dynamic range between two matches
=================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[COUNT](https://exceljet.net/functions/count-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7934/download?token=3tE1zvAJ)
 (14.08 KB)

![Excel formula: Dynamic range between two matches](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/dynamic_range_between_two_matches.png "Excel formula: Dynamic range between two matches")

Summary
-------

To create a dynamic range between two matches, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
. In the example shown, the formula in cell F8 is:

    =SUM(XLOOKUP(F5,date,sales):XLOOKUP(F6,date,sales))

where **date** (B5:B16) and **sales** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is 7075, the sum of sales amounts between January 1 and June 1, inclusive. 

_Note: for the purpose of explanation, the worksheet above has just 12 rows of data. However, the same approach will work with a large set of data._

Generic formula
---------------

    XLOOKUP(A1,range1,range2):XLOOKUP(A2,range1,range2)

Explanation 
------------

In this example, we have **dates** in B5:B16 and **sales** in C5:C16. Both ranges are [named ranges](https://exceljet.net/glossary/named-range)
. The goal is to create a dynamic range between two specific dates: the start date in cell F5 and the end date in cell F6. We then use a formula in F8 to _sum_ the dynamic range, and a formula in F9 to _count_ the dynamic range. In the current version of Excel, this problem can be easily solved with the XLOOKUP function. In older versions of Excel without XLOOKUP, you can use INDEX and MATCH. Both approaches are described below. This problem is a nice demonstration of how both XLOOKUP and INDEX return a valid reference that can be used like any other cell reference.

### Range operator

One of Excel's most common [operators](https://exceljet.net/glossary/math-operators)
 is the colon (:), also known as a "range operator". The range operator (:) is used to construct ranges. For example, to create a reference from cell A1 to cell A9, you would use a range like this:

    =A1:A9

To sum all values in this range, you would simply embed the range in the [SUM function](https://exceljet.net/functions/sum-function)
:

    =SUM(A1:A9)

In this problem, we want to do essentially the same thing. However, the catch is that we want the range to be _dynamic_ so that the references to A1 and A9 are the result of user input. Conceptually, the generic syntax for what we want looks like this:

    =SUM(lookup1:lookup2)

In the code above, _lookup1_ should return a reference to the first cell in the range (the start date in F5), and _lookup2_ should be a reference to the last cell in the range (the end date in F6).

### XLOOKUP function

The trick in solving this problem is to understand that the XLOOKUP function returns a _reference_ and not just a value. This is not obvious in Excel, because even though XLOOKUP returns a reference, Excel will then immediately return the _value at that reference_. Nevertheless, the reference is there and can be used in other ways. In this case, we use this feature to assemble a range based on the results from two separate XLOOKUP formulas like this:

    =SUM(XLOOKUP(F5,date,sales):XLOOKUP(F6,date,sales))

Inside the SUM function, notice we are using two separate XLOOKUP formulas joined with the range operator (:). The first XLOOKUP formula locates the start date in F5 in column B and returns a reference to the corresponding cell in column C:

    XLOOKUP(F5,date,sales) // returns C5

With the _lookup\_value_ provided as F5, the _lookup\_array_ given as **date** (B5:B16), and the _return\_array_ given as **sales** (C5:C16), XLOOKUP matches January 1 in cell B5 and returns a reference to cell C5 as a result. The second XLOOKUP formula is configured in the same way, except the _lookup\_value_ is F6 (the end date):

    XLOOKUP(F6,date,sales) // returns C10

With June 1 in cell F6, the result from XLOOKUP is a reference to C10. Putting this all together, the formula in F8 is evaluated by Excel like this:

    =SUM(XLOOKUP(F5,date,sales):XLOOKUP(F6,date,sales))
    =SUM(C5:C10)
    =7075

When the dates in F5 or F6 are changed, XLOOKUP returns new references and the range is dynamically updated. The SUM then returns a new result. To _count_ results instead of summing results, just replace the SUM function with the COUNT function. In the worksheet shown, the formula in cell F9 looks like this:

    =COUNT(XLOOKUP(F5,date,sales):XLOOKUP(F6,date,sales))

For a detailed overview of XLOOKUP, see [How to use the XLOOKUP function](https://exceljet.net/functions/xlookup-function)
.

### INDEX and MATCH

In older versions of Excel without the XLOOKUP function, this problem can be solved in the same way with an INDEX and MATCH that uses the same structure:

    =SUM(INDEX(sales,MATCH(F5,date,0)):INDEX(sales,MATCH(F6,date,0)))

This works because the INDEX function, like XLOOKUP, returns a _reference_ when the array provided to INDEX is a range. Notice the range operator (:) sits between two separate INDEX and MATCH formulas. The first INDEX and MATCH formula locates the date entered in F5 (January 1) in column B and returns a corresponding reference from the sales amounts in column C:

    INDEX(sales,MATCH(F5,date,0)) // returns C5

The result is a reference to cell C5 since cell B5 contains January 1. The second INDEX and MATCH formula is the same, except that the lookup value comes from cell F6:

    INDEX(sales,MATCH(F6,date,0)) // returns C10

The result is a reference to cell C10 since cell B10 contains June 1. Excel evaluates this formula in the same way as the XLOOKUP version above, with exactly the same result:

    =SUM(INDEX(sales,MATCH(F5,date,0)):INDEX(sales,MATCH(F6,date,0)))
    =SUM(C5:C10)
    =7075

If the dates in F5 and F6 are changed, the INDEX and MATCH formulas return new references, and the range they create is dynamically updated. The SUM function then returns a new result. To _count_ results instead of summing results, just replace the SUM function with the COUNT function:

    =COUNT(INDEX(sales,MATCH(F5,date,0)):INDEX(sales,MATCH(F6,date,0)))

For a detailed overview of INDEX with MATCH see: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: Dynamic named range with INDEX](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/dynamic%20named%20range%20with%20index1.png "Excel formula: Dynamic named range with INDEX")](https://exceljet.net/formulas/dynamic-named-range-with-index)

### [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)

This page shows an example of a dynamic named range created with the INDEX function together with the COUNTA function. Dynamic named ranges automatically expand and contract when data is added or removed. They are an alternative to using an Excel Table , which also resizes as data is added or...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

### [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)

In this video we're going to combine INDEX and MATCH together to look things up. Here we have the city population data we looked at before. We used the INDEX function to retrieve information about a city with a hard-coded position value. When we supply a number, INDEX retrieves information for the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Dynamic named range with INDEX](https://exceljet.net/formulas/dynamic-named-range-with-index)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [How to look things up with INDEX and MATCH](https://exceljet.net/videos/how-to-look-things-up-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    
*   [XLOOKUP vs INDEX and MATCH](https://exceljet.net/articles/xlookup-vs-index-and-match)
    

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