# If date is between two dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/if-date-is-between-two-dates

---

[Skip to main content](https://exceljet.net/formulas/if-date-is-between-two-dates#main-content)

[](https://exceljet.net/formulas/if-date-is-between-two-dates#)

*   [Previous](https://exceljet.net/formulas/if-complete-show-checkmark)
    
*   [Next](https://exceljet.net/formulas/if-else)
    

[If](https://exceljet.net/formulas#If)

If date is between two dates
============================

by Dave Bruns · Updated 30 May 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: If date is between two dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/if_date_is_between_two_dates.png "Excel formula: If date is between two dates")

Summary
-------

To identify when a date is between two given dates, you can use the [IF function](https://exceljet.net/functions/if-function)
 with the [AND function](https://exceljet.net/functions/and-function)
. In the example shown, the formula in C5, copied down, is:

    =IF(AND(B5>=start,B5<=end),"x","")
    

Where **start** (E5) and **end** (E8) are [named ranges](https://exceljet.net/glossary/named-range)
. As the formula is copied down, the formula returns "x" if the date in column B is between the start and end dates. Otherwise, the formula returns an empty string, which looks like an empty cell in Excel.

Generic formula
---------------

    =IF(AND(A1>=start,A1<=end),"x","")

Explanation 
------------

The goal is to identify dates in column B that fall between a given start date and end date. The start and end dates are exposed as inputs on the worksheet that can be changed at any time, labeled "Start" and "End" in the example shown.

### Named ranges

For convenience, both **start** (E5) and **end** (E8) are [named ranges](https://exceljet.net/glossary/named-range)
 that can be used directly in the formula. If you prefer not to use named ranges, use [absolute references](https://exceljet.net/glossary/absolute-reference)
 like $E$5 and $E$8 to prevent these references from changing as the formula is copied down the table.

    =IF(AND(B5>=$E$5,B5<=$E$8),"x","")
    

### Excel dates

[Excel dates are just large serial numbers](https://exceljet.net/glossary/excel-date)
 and can be used in any numeric calculation or comparison. This means we can compare one date to another date with a [logical operator](https://exceljet.net/glossary/logical-operators)
 like greater than or equal (>=) or less than or equal (<=) like any other number.

### AND function

 The [AND function](https://exceljet.net/functions/and-function)
 returns TRUE if all arguments are TRUE. For example, if cell A1 contains "Red" and B1 contains 10, then:

    =AND(A1="Red",B1>5) returns TRUE
    =AND(A1="Red",B1>12) returns FALSE
    =AND(A1="Blue",B1>5) returns FALSE
    

In this example, the main task is to construct a [logical test](https://exceljet.net/glossary/logical-test)
 to find dates that fall between the start and end dates. The first comparison is against the start date. We want to check if the date in B5 is greater than or equal (>=) to the date in cell E5, which is the named range **start**:

    =B5>=start
    

The second expression needs to check if the date in B5 is less than or equal (<=) to the end date in cell E5:

    =B5<=end
    

Since we want to test if both conditions are TRUE at the same time, we use the [AND function](https://exceljet.net/functions/and-function)
 like this:

    =AND(B5>=start,B5<=end) // returns TRUE
    

For cell B5, the result is TRUE, because 11-Jan-2022 is greater than 1-Jan-2022 AND is less than 30-Apr-2022. For cell B6 however, the result is FALSE. Although 1-May-2022 is greater than  1-Jan-2022, it _is not_ less than 30-Apr-2022:

    =AND(B6>=start,B6<=end) // returns FALSE
    

To summarize: the AND function will return TRUE when the date in column B is greater than or equal to **start** (E5) AND less than equal to **end** (E8) If either test fails, the AND function will return FALSE. We now have the logical test we can use in the IF function.

### IF function

The [IF function](https://exceljet.net/functions/if-function)
 runs a logical test and returns one value for a TRUE result, and another value for a FALSE result. The generic syntax for IF looks like this:

    =IF(logical_test,if_true,if_false)

We start off by placing the expression we developed above inside the IF function as the _logical\_test_ argument:

    =IF(AND(B5>=start,B5<=end),
    

Next, we add a _value\_if\_true_ argument. In this case, we  want to return an "x" when a date is between two dates, so we add "x" as a [text value](https://exceljet.net/glossary/text-value)
:

    =IF(AND(B5>=start,B5<=end),"x",
    

If the date in B5 is not between the start and end dates, we don't want to display anything, so we use an [empty string](https://exceljet.net/glossary/empty-string)
 ("") for _value\_if\_false_. The final formula in C5 is:

    =IF(AND(B5>=start,B5<=end),"x","")
    

As the formula is copied down, the formula returns "x" if the date in column B is between the start and end date. If not, the formula returns an empty string (""), which looks like an empty cell in Excel. The values returned by the IF function can be customized as desired.

Related formulas
----------------

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20IF%20function-thumb.png)](https://exceljet.net/videos/the-if-function)

### [The IF function](https://exceljet.net/videos/the-if-function)

Of all the many functions in Excel, the IF function is often the first function that new users turn to. It's a very flexible function that you can use in all sorts of ways. Let's take a look. To illustrate how IF works, let's look first at a case where we need to assign a "pass" or "fail" to a...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [If this AND that](https://exceljet.net/formulas/if-this-and-that)
    
*   [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Articles

*   [19 tips for nested IF formulas](https://exceljet.net/articles/nested-ifs)
    

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