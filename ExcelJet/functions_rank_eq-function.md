# Excel RANK.EQ function | Exceljet

**Source:** https://exceljet.net/functions/rank.eq-function

---

[Skip to main content](https://exceljet.net/functions/rank.eq-function#main-content)

[](https://exceljet.net/functions/rank.eq-function#)

*   [Previous](https://exceljet.net/functions/rank.avg-function)
    
*   [Next](https://exceljet.net/functions/skew-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

RANK.EQ Function
================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[RANK.AVG](https://exceljet.net/functions/rank.avg-function)

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

![Excel RANK.EQ function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_rank.eq_function.png "Excel RANK.EQ function")

Summary
-------

The Excel RANK.EQ function returns the rank of a number against a list of other numeric values. When values contain duplicates, RANK.EQ will assign the same rank to each tie value and the subsequent rank will be skipped. 

Purpose 
--------

Rank a number against a range of numbers

Return value 
-------------

A number that indicates rank.

Syntax
------

    =RANK.EQ(number,ref,[order])

*   _number_ - The number to rank.
*   _ref_ - A range that contains the numbers to rank against.
*   _order_ - \[optional\] Rank ascending or descending. Default is zero.

Using the RANK.EQ function 
---------------------------

The RANK.EQ function returns the rank of a numeric value compared to a list of other numeric values. RANK.EQ can rank values from largest to smallest (i.e., the rank of highest test scores) and smallest to largest (i.e., the rank of fastest times in a race). You can use the RANK.EQ function to calculate the rank of each value in a dataset. When values contain duplicates, RANK.EQ will assign the same rank to each tie value, and the subsequent rank will be skipped. RANK.EQ works fine with sorted or unsorted data — it is not necessary to sort the values in the list before RANK.EQ.

### Key Features

*   Returns the rank of a single number against a list of other numbers
*   Works with both _ascending order_ (smallest = rank 1) and _descending order_ (largest = rank 1)
*   _Does not require sorted data_ - works with data in any order
*   _Handles tied values_ by assigning the _same rank_ to duplicates and skipping subsequent ranks
*   _Requires actual ranges_ - cannot use an array for the _ref_ argument
*   _Recommended function_ for ranking - Microsoft's preferred replacement for the [RANK](https://exceljet.net/functions/rank-function)
     function
*   Works in Excel 2010 and all later versions

> Unlike most other Excel functions, RANK.EQ requires an actual range for the _ref_ argument. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula.

### Syntax

The basic syntax for RANK.EQ looks like this:

    =RANK.EQ(number,ref,[order])

where _number_ is the value you want to rank, _ref_ is a range that contains numbers to rank against, and _order_ is an optional argument that controls ranking direction. By default, RANK.EQ will rank values in _descending_ order and assign 1 to the _largest_ value in the list. However, this behavior can be reversed using the optional _order_ argument as explained below.

_Note: The RANK.EQ function is the recommended function for ranking in Excel, as RANK is now classified as a compatibility function. RANK is still available for backward compatibility. RANK.EQ and RANK are essentially the same function and there should be no cases where they return different results._

### Ranking in descending or ascending order

The RANK.EQ function has two modes of operation, descending and ascending, which are controlled by the _order_ argument. To rank values where the largest value is ranked number 1, set _order_ to zero (0) or omit the argument altogether:

    =RANK.EQ(A1,range) // rank descending (default)
    =RANK.EQ(A1,range,0) // rank descending
    

To rank values where the smallest value should be 1, set _order_ to 1:

    =RANK.EQ(A1,range,1) // rank ascending
    

Set _order_ to zero (0) when you want to rank something like top sales, where the largest sales number should rank #1, and set order to one (1) when you want to rank something like race results, where the shortest (fastest) time should rank #1.

### Example - ranking test scores in descending order

In the worksheet below, the goal is to rank test scores. For test scores, the highest score should be assigned a rank of 1, so the RANK.EQ function is used in its default mode. The formula in cell D5 is:

    =RANK.EQ(C5,$C$5:$C$12)

![RANK.EQ example - ranking test scores](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.eq_example_rank_test_scores.png "RANK.EQ example - ranking test scores")

Notice that the range is provided as the [absolute reference](https://exceljet.net/glossary/absolute-reference)
 $C$5:$C$12 so that it won't change when the formula is copied down. The optional _order_ argument is not provided, since RANK.EQ will assign 1 to the largest value by default.

### Example - ranking race times in ascending order

In the example below, the goal is to rank race times. This is an example of where we want to assign a rank of 1 to the fastest time, which will be the smallest time. The formula in cell D5 is:

    =RANK.EQ(C5,$C$5:$C$12,1)

Notice the range $C$5:$C$12 is _absolute_ to prevent the reference from changing when the formula is copied down while the reference to C5 is _relative_ so that it _will change_ as the formula is copied down. Also, note that the optional _order_ argument is provided as 1 to force RANK.EQ to rank the times in _ascending_ order.

![RANK.EQ example - ranking race results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.eq_example_rank_race_times.png "RANK.EQ example - ranking race results")

### Ranking ties

The RANK.EQ function handles ties in a specific manner: it assigns the _same rank_ to both items. A tie occurs when two or more items in the data have the same value or, in other words, the data being ranked contains duplicates. For example, if a certain value has a rank of 3, and there are two instances of the value in the data, the RANK.EQ function will assign _both instances_ a rank of 3. The next rank assigned will be 5, and _no value will receive the rank of 4_. The process looks like this:

1.  **Ties are identified** - When two or more values in the list are the same, they are considered tied. For example, if two students have a score of 91, they are in a tie.
2.  **Ties are ranked** - Excel assigns the same rank to the tied values. For instance, if two students are tied for the third-highest score, both will receive a rank of 3.
3.  **The subsequent rank is skipped** - After a tie, Excel skips the next rank(s). If two students are tied for third place, the next student (with a lower score) receives a rank of 5, not 4. The tie essentially absorbs the fourth rank.

You can see the result of this process in the worksheet below, where Aisha and Mia have a score of 91 and are both tied for third place. The RANK.EQ function assigns both a rank of 3 and the next rank, 4, is skipped.

![RANK.EQ example - ranking tie values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.eq_example_ranking_tied_values.png "RANK.EQ example - ranking tie values")

If tied ranks are a problem, one workaround is to employ a [tie-breaking strategy](https://exceljet.net/formulas/rank-without-ties)
.

### RANK.EQ versus RANK and RANK.AVG

Excel contains three functions for assigning rank: RANK, RANK.EQ, and RANK.AVG. RANK.EQ is the updated function for ranking in Excel, recommended over the older RANK function for its consistency and intuitive use. RANK and RANK.EQ are essentially the same function, and there should be no cases where they return different results. RANK.AVG, on the other hand, assigns ranks to numeric values but provides a different behavior when there are tie values, assigning tie values an _average rank_. For example, if two numbers are tied for third place, RANK.AVG will assign both numbers a rank of 3.5.

### Recommendations

*   For older worksheets that use RANK, consider replacing RANK with RANK.EQ to ensure consistent behavior and results.
*   In new worksheets, use RANK.EQ instead of RANK to align with Microsoft's recommendations and to prepare for any future updates where RANK might be deprecated.
*   Use RANK.AVG if you require an _average rank_ for tie values in the data (i.e., duplicates). This is the only reason to use RANK.AVG since in other respects it works the same as RANK.EQ and RANK.

### Notes

*   The default for _order_ is zero (0). If _order_ is 0 or omitted, _number_ is ranked against the numbers sorted in descending order: smaller numbers receive a higher rank value, and the largest value in a list will be ranked #1.
*   If _order_ is 1, _number_ is ranked against the numbers sorted in ascending order: smaller numbers receive a lower rank value, and the smallest value in a list will be ranked #1.
*   It is not necessary to sort the values in the list before using the RANK.EQ function.
*   In the event of a tie (i.e., the list contains duplicates), RANK.EQ will assign the _same rank_ value to each duplicate (tie) value and the next rank will be skipped.
*   Some documentation suggests _ref_ can be an [array](https://exceljet.net/glossary/array)
    , but in our testing, ref must be a range. Otherwise, Excel will display the "There's a problem with this formula" error dialog.

Related functions
-----------------

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel RANK.AVG function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank.avg_function.png "Excel RANK.AVG function")](https://exceljet.net/functions/rank.avg-function)

### [RANK.AVG Function](https://exceljet.net/functions/rank.avg-function)

The Excel RANK.AVG function returns the rank of a number against a list of other numeric values. When values contain duplicates, the RANK.AVG function will assign an average rank to each set of duplicates....

[![Excel SMALL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20small%20function_0.png "Excel SMALL function")](https://exceljet.net/functions/small-function)

### [SMALL Function](https://exceljet.net/functions/small-function)

The Excel SMALL function returns a numeric value based on its position in a list when sorted by value in _ascending_ order. In other words, SMALL can return the "nth smallest" value (1st smallest value, 2nd smallest value, 3rd smallest value, etc.) from a set of numeric data.

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [RANK Function](https://exceljet.net/functions/rank-function)
    
*   [RANK.AVG Function](https://exceljet.net/functions/rank.avg-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    

### Links

*   [Microsoft RANK.EQ function documentation](https://support.office.com/en-us/article/rank-eq-function-284858ce-8ef6-450e-b662-26245be04a40)
    

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