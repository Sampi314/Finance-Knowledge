# 10 most common text values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/10-most-common-text-values

---

[Skip to main content](https://exceljet.net/formulas/10-most-common-text-values#main-content)

[](https://exceljet.net/formulas/10-most-common-text-values#)

*   [Previous](https://exceljet.net/formulas/sequence-of-years)
    
*   [Next](https://exceljet.net/formulas/abbreviate-names-or-words)
    

[Text](https://exceljet.net/formulas#Text)

10 most common text values
==========================

by Dave Bruns · Updated 29 Aug 2024

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

[SORT](https://exceljet.net/functions/sort-function)

[TAKE](https://exceljet.net/functions/take-function)

![Excel formula: 10 most common text values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/10%20most%20common%20text%20values.png "Excel formula: 10 most common text values")

Summary
-------

To list the 10 most common text values in a range, you can use a formula based on several functions, including [UNIQUE](https://exceljet.net/functions/unique-function)
, [COUNTIF](https://exceljet.net/functions/countif-function)
, [SORT](https://exceljet.net/functions/sort-function)
, and [TAKE](https://exceljet.net/functions/take-function)
. In the example shown, the formula in cell E5 is:

     =LET(u,UNIQUE(data),TAKE(SORT(HSTACK(u,COUNTIF(data,u)),2,-1),10))
    

Where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B104. The result is the two-column table in E5:F14, with values sorted in descending order by count.

_Note: This formula requires a current version of Excel. For Excel 2019 and older [this formula](https://exceljet.net/formulas/most-frequently-occurring-text)
 will get the single most frequent text value. To list other frequently occurring values, a [pivot table would be easiest](https://exceljet.net/pivot-tables/pivot-table-most-frequently-occurring)
._

_, [see this page.](https://exceljet.net/formulas/most-frequently-occurring-text)
_

Generic formula
---------------

    =LET(u,UNIQUE(data),TAKE(SORT(HSTACK(u,COUNTIF(data,u)),2,-1),n))

Explanation 
------------

In this example, the goal is to list the 10 most frequently occurring text values in a range, in descending order by count, as seen in the range in E5:F14. This is an advanced formula that requires a number of [nested](https://exceljet.net/glossary/nesting)
 functions. However, it is an excellent example of the power of [dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. For convenience, **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B104. This range contains 100 random color names.

### Get unique values

The first step in this problem is to get a list of unique colors from the data. This is easy to do with the [UNIQUE function](https://exceljet.net/videos/the-unique-function)
:

    UNIQUE(data) // get unique colors
    

Since there 23 unique colors in B5:B104, UNIQUE returns an [array](https://exceljet.net/glossary/array)
 containing 23 color names:

    {"Violet";"Maroon";"Blue";"Pink";"Lime";"Navy";"Yellow";"White";"Cyan";"Teal";"Gold";"Orange";"Peach";"Black";"Turquoise";"Tan";"Red";"Green";"Gray";"Indigo";"Brown";"Purple";"Silver"} 
    

### Count unique values

Now that we have a list of values, the next step is to get a count for each unique value. This can be done with the [COUNTIF function](https://exceljet.net/functions/countif-function)
 like this:

    =COUNTIF(data,UNIQUE(data))
    

Here, the UNIQUE function returns the unique values in the data as the criteria argument, and COUNTIF calculates a count for each value. The result is an array with 23 counts like this:

    {11;5;4;9;3;4;4;7;3;8;2;5;6;5;3;2;3;3;4;4;3;1;1}
    

We now have the basic ingredients we need to solve the problem.

### Combine values and counts

The next step is to combine the list of unique colors with the counts to form the two-column table seen in column E and F. This can be done with the [HSTACK function](https://exceljet.net/functions/hstack-function)
, which is designed to combine arrays horizontally. We can use HSTACK like this:

    =HSTACK(UNIQUE(data),COUNTIF(data,UNIQUE(data)))
    

The result from HSTACK is a list of 23 unique colors on the left, combined with 23 counts on the right:

![Counts for all 23 values unsorted](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/counts%20for%20all%2023%20values%20unsorted.png?itok=26iJUCrv "Counts for all 23 values unsorted")

We are getting close to a solution, but we still need to reorder the list to show the highest counts first, and drop all but the top 10 counts.

### Sort by count

To sort the table by count, we can use the [SORT function](https://exceljet.net/functions/sort-function)
 like this:

    =SORT(HSTACK(UNIQUE(data),COUNTIF(data,UNIQUE(data))),2,-1)
    

Now we have the values sorted by count in descending order:

![Most common text values sorted by count](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/most%20common%20text%20values%20sorted%20by%20count.png?itok=l04SpZ7r "Most common text values sorted by count")

### Top 10 values by count

The final step is to remove all but the top 10 values. The easiest way to do this is with the [TAKE function](https://exceljet.net/functions/take-function)
, which is designed to extract rows and columns from arrays. In this case, we want the first 10 rows, so we provide 10 for rows:

    =TAKE(SORT(HSTACK(UNIQUE(data),COUNTIF(data,UNIQUE(data))),2,-1),10)
    

The screen below shows the output of this formula:

![The final table, listing just the top 10 values by count, sorted in descending order](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/most%20common%20text%20values%20final%20top%2010%20table.png?itok=kUJrjE_V "The final table, listing just the top 10 values by count, sorted in descending order")

### Optimize

The formula above works fine, but it is a bit inefficient, since UNIQUE values are calculated twice. This might impact performance in larger sets of data. To streamline the formula, we can use the [LET function](https://exceljet.net/functions/let-function)
. The LET function is used to declare and assign values to variables. In this case, we can use LET like this:

    =LET(u,UNIQUE(data),TAKE(SORT(HSTACK(u,COUNTIF(data,u)),2,-1),10))
    

Here, we use UNIQUE to get unique values and assign the result to a variable named _u_. Then we replace UNIQUE(data) with _u_ where it occurs in the formula. The result is that UNIQUE values are calculated just one time.

Related formulas
----------------

[![Excel formula: Most frequently occurring text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text2.png "Excel formula: Most frequently occurring text")](https://exceljet.net/formulas/most-frequently-occurring-text)

### [Most frequently occurring text](https://exceljet.net/formulas/most-frequently-occurring-text)

Working from the inside out, the MATCH function matches the range against itself. That is, we give the MATCH function the same range for lookup value and lookup array (B5:F5). Because the lookup value contains more than one value (an array), MATCH returns an array of results, where each number...

[![Excel formula: Most frequent text with criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequent%20text%20with%20criteria.png "Excel formula: Most frequent text with criteria")](https://exceljet.net/formulas/most-frequent-text-with-criteria)

### [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)

In this example, the goal is to return the most frequently occurring text based on one or more supplied criteria. Working from the inside out, we use the MATCH function to match the text range against itself, by giving MATCH the same range for lookup value and lookup array, with zero for match type...

[![Excel formula: Most frequently occurring number](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/most%20frequently%20occurring%20number.png "Excel formula: Most frequently occurring number")](https://exceljet.net/formulas/most-frequently-occurring-number)

### [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)

The MODE function is fully automatic and will return the most frequently occurring number in a set of numbers. For example: =MODE(1,2,4,4,5,5,5,6) // returns 5 In the example shown, we give MODE the range B4:K4, so the formula is solved like this: =MODE(B4:K4) =MODE({1,2,2,1,1,2,2,2,1,1}) =2

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel TAKE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20take%20function.png "Excel TAKE function")](https://exceljet.net/functions/take-function)

### [TAKE Function](https://exceljet.net/functions/take-function)

The Excel TAKE function returns a subset of a given array. The number of rows and columns to return is provided by separate _rows_ and _columns_ arguments. Rows and columns can be extracted from the start or end of the given array.

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
    
*   [Most frequent text with criteria](https://exceljet.net/formulas/most-frequent-text-with-criteria)
    
*   [Most frequently occurring number](https://exceljet.net/formulas/most-frequently-occurring-number)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [TAKE Function](https://exceljet.net/functions/take-function)
    

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