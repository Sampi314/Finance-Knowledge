# Excel RANK.AVG function | Exceljet

**Source:** https://exceljet.net/functions/rank.avg-function

---

[Skip to main content](https://exceljet.net/functions/rank.avg-function#main-content)

[](https://exceljet.net/functions/rank.avg-function#)

*   [Previous](https://exceljet.net/functions/rank-function)
    
*   [Next](https://exceljet.net/functions/rank.eq-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

RANK.AVG Function
=================

by Dave Bruns · Updated 8 Jun 2025

Related functions 
------------------

[RANK](https://exceljet.net/functions/rank-function)

[RANK.EQ](https://exceljet.net/functions/rank.eq-function)

[SMALL](https://exceljet.net/functions/small-function)

[LARGE](https://exceljet.net/functions/large-function)

![Excel RANK.AVG function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_rank.avg_function.png "Excel RANK.AVG function")

Summary
-------

The Excel RANK.AVG function returns the rank of a number against a list of other numeric values. When values contain duplicates, the RANK.AVG function will assign an average rank to each set of duplicates.

Purpose 
--------

Rank a number against a range of numbers

Return value 
-------------

A number that indicates rank.

Syntax
------

    =RANK.AVG(number,ref,[order])

*   _number_ - The number to rank.
*   _ref_ - A range that contains the numbers to rank against.
*   _order_ - \[optional\] Rank ascending or descending. Default is zero.

Using the RANK.AVG function 
----------------------------

The RANK.AVG function returns the rank of a numeric value compared to a list of other numeric values. RANK.AVG can rank values from largest to smallest (i.e., the rank of highest test scores) and smallest to largest (i.e., the rank of fastest times in a race). When RANK.AVG encounters duplicates, it will assign an _average rank_ to each set of duplicates. RANK.AVG works fine with sorted or unsorted data — it is not necessary to sort the values in the list before RANK.AVG.

### Key Features

*   Returns the rank of a single number against a list of other numbers
*   Works with both _ascending order_ (smallest = rank 1) and _descending order_ (largest = rank 1)
*   _Does not require sorted data_ - works with data in any order
*   _Handles tied values_ by assigning an _average rank_ to duplicates (e.g., 3.5 for values tied at 3rd place)
*   _Requires actual ranges_ - cannot use an array for the _ref_ argument
*   _Preserves sum of ranks_ when averaging tied values
*   Works in Excel 2010 and all later versions

> Unlike most other Excel functions, RANK.AVG requires an actual range for the _ref_ argument. If you try to use an [array](https://exceljet.net/glossary/array)
> , Excel will not let you enter the formula.

### Synax

The basic syntax for RANK.AVG looks like this:

    =RANK.AVG(number,ref,[order])

where _number_ is the value you want to rank, _ref_ is a range that contains numbers to rank against, and _order_ is an optional argument for controlling the ranking direction. By default, RANK.AVG will rank values in _descending_ order and assign an average rank to tied values in the list. This behavior can be reversed using the optional _order_ argument as explained below.

Video: [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

_Note: The RANK.AVG function is designed to handle ties by assigning them an average rank, which is different from RANK.EQ or RANK._ 

### Ranking in descending or ascending order

The RANK.AVG function has two modes of operation, descending and ascending, which are controlled by the _order_ argument. To rank values where the largest value is ranked number 1, set _order_ to zero (0) or omit the argument altogether:

    =RANK.AVG(A1,range) // rank descending (default)
    =RANK.AVG(A1,range,0) // rank descending
    

To rank values where the _smallest value_ should be 1, set _order_ to 1:

    =RANK.AVG(A1,range,1) // rank ascending
    

To recap: set _order_ to zero (0) when you want to rank something like top sales, where the largest sales number should rank #1, and set order to one (1) when you want to rank something like race results, where the smallest (fastest) time should rank #1.

### Example - ranking test scores in descending order

In the worksheet below, the goal is to rank test scores. For test scores, the highest score should be assigned a rank of 1, so the RANK.AVG function is used in its default mode. The formula in cell D5 is:

    =RANK.AVG(C5,$C$5:$C$12)

![RANK.AVG example - ranking test scores](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.avg_example_rank_test_scores.png "RANK.AVG example - ranking test scores")

Notice that the range is provided as the [absolute reference](https://exceljet.net/glossary/absolute-reference)
 $C$5:$C$12 so that it won't change when the formula is copied down. The optional _order_ argument is not provided, since RANK.AVG will assign an average rank to tied values by default.

### Example - ranking race times in ascending order

In the example below, the goal is to rank race times. This is an example of where we want to assign a rank of 1 to the fastest time, which will be the smallest time. The formula in cell D5 is:

    =RANK.AVG(C5,$C$5:$C$12,1)

Notice the range $C$5:$C$12 is _absolute_ to prevent the reference from changing when the formula is copied down while the reference to C5 is _relative_ so that it _will change_ as the formula is copied down. Also, note that the _order_ argument is provided as 1 to force RANK.AVG to rank the times in _ascending_ order.

![RANK.AVG example - ranking race results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.avg_example_rank_race_results.png "RANK.AVG example - ranking race results")

### Ranking ties

When the data contains duplicate (tied) values, you have to decide how you want to rank tied values. There are two basic approaches: (1) assign the same rank to each tie value or (2) assign an average rank to each tie value. The RANK.AVG function is designed to follow the second approach. For example, in the data {90,85,95,80}, there are no ties and RANK.AVG would assign ranks of {2,3,1,4}. In the data {85}, there are two tied values and RANK.AVG would assign ranks of {2,3.5,1,3.5}. One advantage of using an average rank is that the sum of ranks (10) is preserved.

As mentioned above, the RANK.AVG function handles ties by assigning an _average rank_ to tied values. For example, if two or more values in the data have the same rank, RANK.AVG will assign them an average rank rather than giving them the same rank. You can see how this works in the worksheet below. Aisha and Mia are tied for third place with a score of 91 and RANK.AVG assigns a rank of 3.5 to each. Notice the subsequent rank of 4 is skipped entirely:

![RANK.AVG example - ranking tie values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/rank.avg_example_ranking_tie_values.png "RANK.AVG example - ranking tie values")

Note: the fact that RANK.AVG averages tied values is the main reason to use RANK.AVG, since in other respects it operates like RANK and RANK.EQ. 

### RANK.AVG versus RANK and RANK.EQ

Excel contains three functions for assigning rank: RANK, RANK.EQ, and RANK.AVG. RANK is the original ranking function in Excel. RANK.EQ and RANK.AVG were introduced in Excel 2010 as part of a broader effort by Microsoft to make Excel functions more consistent and intuitive. RANK and RANK.EQ are essentially the same function. There should be no cases where RANK and RANK.EQ return different results. RANK and RANK.EQ will assign tie values the _same rank_ and the "EQ" in the name indicates this "equal rank" behavior. In contrast, the RANK.AVG function will assign tie values an _average rank_. For example, if two numbers are tied for third place, RANK.AVG will assign both numbers a rank of 3.5. The "AVG" in the name denotes the "average rank" behavior.

### Recommendations

*   The RANK function should continue to work fine in older worksheets. If you are updating an older worksheet, you could optionally replace RANK with RANK.EQ and get the same behavior and results.
*   In new worksheets, Microsoft recommends RANK.EQ instead of RANK, since there is a possibility that RANK will be unsupported at some point in the future. Both RANK.EQ and RANK will return the same results and both will assign the same rank to tie values.
*   If you specifically want an average rank for tie values in the data (i.e. duplicates) use the RANK.AVG function. This is the primary reason to use RANK.AVG since in other respects it works the same as RANK.EQ and RANK.
*   The names for RANK.EQ and RANK.AVG identify the expected ranking behavior explicitly. So, while the names seem more complicated and fussy at first glance, they do have a purpose.

### Notes

*   The default for _order_ is zero (0). If _order_ is 0 or omitted, _number_ is ranked against the numbers sorted in descending order, where ties are given an average rank, reflecting their equal standing.
*   If _order_ is 1, _number_ is ranked against the numbers sorted in ascending order, again with ties receiving an average rank.
*   Sorting values in the list before using the RANK.AVG function is not necessary.
*   RANK.AVG averages ties and preserves the "sum of ranks".
*   Some documentation suggests _ref_ can be an [array](https://exceljet.net/glossary/array)
    , but in our testing, ref must be a range. Otherwise, Excel will display the "There's a problem with this formula" error dialog.

Related functions
-----------------

[![Excel RANK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank_0.png "Excel RANK function")](https://exceljet.net/functions/rank-function)

### [RANK Function](https://exceljet.net/functions/rank-function)

The Excel RANK function returns the rank of a numeric value when compared to a list of other numeric values. RANK can rank values from largest to smallest (i.e. top sales) as well as smallest to largest (i.e. fastest time).

[![Excel RANK.EQ function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_rank.eq_function.png "Excel RANK.EQ function")](https://exceljet.net/functions/rank.eq-function)

### [RANK.EQ Function](https://exceljet.net/functions/rank.eq-function)

The Excel RANK.EQ function returns the rank of a number against a list of other numeric values. When values contain duplicates, RANK.EQ will assign the same rank to each tie value and the subsequent rank will be skipped. ...

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
    
*   [RANK.EQ Function](https://exceljet.net/functions/rank.eq-function)
    
*   [SMALL Function](https://exceljet.net/functions/small-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    

### Links

*   [Microsoft RANK.AVG function documentation](https://support.office.com/en-us/article/rank-avg-function-bd406a6f-eb38-4d73-aa8e-6d1c3c72e83a)
    

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