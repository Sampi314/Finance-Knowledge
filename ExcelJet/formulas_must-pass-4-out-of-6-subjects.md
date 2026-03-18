# Must pass 4 out of 6 subjects - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/must-pass-4-out-of-6-subjects

---

[Skip to main content](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects#main-content)

[](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects#)

*   [Previous](https://exceljet.net/formulas/moving-average-formula)
    
*   [Next](https://exceljet.net/formulas/weighted-average)
    

[Average](https://exceljet.net/formulas#Average)

Must pass 4 out of 6 subjects
=============================

by Dave Bruns · Updated 22 Jan 2023

Related functions 
------------------

[IF](https://exceljet.net/functions/if-function)

[COUNTIF](https://exceljet.net/functions/countif-function)

[AND](https://exceljet.net/functions/and-function)

![Excel formula: Must pass 4 out of 6 subjects](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/must_pass_4_out_of_6_subjects.png "Excel formula: Must pass 4 out of 6 subjects")

Summary
-------

To return "Pass" if any 4 subjects have a passing score, and "Fail" if not, you can use a formula based on the [IF function](https://exceljet.net/functions/if-function)
 and [COUNTIF function](https://exceljet.net/functions/countif-function)
. In the example shown, the formula in K5 is:

    =IF(COUNTIF(C5:H5,">=70")>=4,"Pass","Fail")
    

where 70 represents a passing score for all subjects. As the formula is copied down, it returns "Pass" or "Fail".

Generic formula
---------------

    =IF(COUNTIF(range,">=70")>=4,"Pass","Fail")

Explanation 
------------

In this example, the goal is to create a formula that will return "Pass" or "Fail" depending on whether a student has a passing score in at least 4 out of 6 subjects. This problem can be easily solved with a formula based on the [COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
 together with the [IF function](https://exceljet.net/videos/the-if-function)
 in a formula like this:

    =IF(COUNTIF(C5:H5,">=70")>=4,"Pass","Fail")

### COUNTIF function

The COUNTIF function counts cells in a range that meet a single condition, referred to as _criteria_. COUNTIF supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,<=,>=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. The generic syntax for COUNTIF looks like this:

    =COUNTIF(range,criteria)

In this case, we need to configure COUNTIF to count passing scores in columns C:H for each name listed in column B. We start off with the _range_:

    =COUNTIF(C5:H5,

For _criteria_, we need to use the greater than or equal to operator (>=) with the passing score of 70:

    =COUNTIF(C5:H5,">=70")

Notice the criteria is entered in double quotes (""), which is a quirk of [RACON functions in Excel](https://exceljet.net/articles/excels-racon-functions)
. The formula above is in fact the formula entered in cell J5, copied down. As you can see in the worksheet shown above, COUNTIF returns a count of passing scores in each row. If desired, column J could be used as a [helper column](https://exceljet.net/glossary/helper-column)
, but in this example the formula in column K is an all-in-one formula and the formula in column J is just for reference.

### IF function

To return "Pass" or "Fail", we use the [IF function](https://exceljet.net/videos/the-if-function)
. We start off by [nesting](https://exceljet.net/glossary/nesting)
 COUNTIF inside IF like this:

    =IF(COUNTIF(C5:H5,">=70")

We know from above that the COUNTIF formula returns a _count_ of passing scores. Because the goal in the example is to return "Pass" when there are at least 4 subjects with passing scores, we add logic to test the result from COUNTIF:

    =IF(COUNTIF(C5:H5,">=70")>=4,

This is the _logical\_test_ inside the IF function. If COUNTIF returns the number 4 or greater, the logical test will return TRUE. Otherwise, the logical test will return FALSE. Finally, we need to add the _value\_if\_true_ and _value\_if\_false_ arguments and close up the formula. The final formula in K5 is:

    =IF(COUNTIF(C5:H5,">=70")>=4,"Pass","Fail")

As the formula is copied down, if 4 or more subjects have a passing score of at least 70, IF returns "Pass". Otherwise, the IF function returns "Fail".

### Must pass Math and English

If Math and English _must have passing scores_, regardless of other scores, the formula can be adjusted like this:

    =IF(AND(COUNTIF(C5:H5,">=70")>=4,C5>=70,F5>=70),"Pass","Fail")
    

Here the [AND function](https://exceljet.net/functions/and-function)
 is used for the _logical\_test_ inside IF:

    AND(COUNTIF(C5:H5,">=70")>=4,C5>=70,F5>=70)
    

With this configuration, AND will return TRUE only when these three conditions are TRUE:

1.  Passing score in 4 out of 6 subjects
2.  Passing score in Math
3.  Passing score in English

If any condition is not true, AND will return FALSE and the IF function will return "Fail" as a final result

Related formulas
----------------

[![Excel formula: If this AND that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that.png "Excel formula: If this AND that")](https://exceljet.net/formulas/if-this-and-that)

### [If this AND that](https://exceljet.net/formulas/if-this-and-that)

The goal is to mark records with an "x" when the color is "Red" and the size is "Small". To perform this task, you can use the IF function in combination with the AND function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different value if the...

[![Excel formula: If this AND that OR that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/if_this_and_that_or_that.png "Excel formula: If this AND that OR that")](https://exceljet.net/formulas/if-this-and-that-or-that)

### [If this AND that OR that](https://exceljet.net/formulas/if-this-and-that-or-that)

The goal is to mark rows where the color is "Red" AND the size is "Small" or "Medium". To perform this task, you can use the IF function in combination with the AND function and the OR function . IF function The IF function runs a test, then returns one value if the result is TRUE, and a different...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Score quiz answers with key](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/score%20quiz%20answers%20with%20key.png "Excel formula: Score quiz answers with key")](https://exceljet.net/formulas/score-quiz-answers-with-key)

### [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)

This formula uses the named range key (C4:G4) for convenience only. Without the named range, you'll want to use an absolute reference so the formula can be copied. In cell I7, we have this formula: =SUM(--(C7:G7=key)) working from the inside-out, this expression is evaluated first: C7:G7=key //...

Related functions
-----------------

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel AND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_and_0.png "Excel AND function")](https://exceljet.net/functions/and-function)

### [AND Function](https://exceljet.net/functions/and-function)

The Excel AND function is a logical function used to test multiple conditions at the same time. AND returns TRUE _only if all the conditions are met_. If any conditions are not met, the AND function returns FALSE. The AND function is commonly used with other...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIF%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countif-function)

### [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

In this video we'll look at how to use the COUNTIF function to count cells that meet a single criteria. Let's take a look. The COUNTIF function counts cells that satisfy a single condition that you supply. It takes two arguments: range and criteria. For example, if I want to count the cells in this...

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
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Score quiz answers with key](https://exceljet.net/formulas/score-quiz-answers-with-key)
    

### Functions

*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [AND Function](https://exceljet.net/functions/and-function)
    

### Videos

*   [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)
    
*   [The IF function](https://exceljet.net/videos/the-if-function)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [Excel formulas and functions](https://exceljet.net/articles/excel-formulas-and-functions)
    

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