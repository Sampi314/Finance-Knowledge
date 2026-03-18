# XLOOKUP approximate match with multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria#main-content)

[](https://exceljet.net/formulas/xlookup-approximate-match-with-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Next](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    

[Lookup](https://exceljet.net/formulas#Lookup)

XLOOKUP approximate match with multiple criteria
================================================

by Dave Bruns · Updated 2 May 2025

Related functions 
------------------

[XLOOKUP](https://exceljet.net/functions/xlookup-function)

[IF](https://exceljet.net/functions/if-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: XLOOKUP approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/XLOOKUP_approximate_match_with_multiple_criteria.png "Excel formula: XLOOKUP approximate match with multiple criteria")

Summary
-------

To perform an approximate match lookup with multiple criteria, you can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
, with help from the [IF function](https://exceljet.net/videos/the-if-function)
. In the example shown, the formula in G8 is:

    =XLOOKUP(G7,IF(data[Service]=G6,data[Weight]),data[Cost],,-1)

where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D16. With "2-Day Air" in cell G6 and 72 in cell G7, XLOOKUP returns $45.00.

_Note: you can use the same approach with an_ [_INDEX and MATCH formula_](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)
_._

Generic formula
---------------

    =XLOOKUP(value,IF(range=A1,range),range,,-1)

Explanation 
------------

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the weight of the item. The challenge is that we also need to filter by service. This means we need to apply criteria in two steps: (1) match based on Service, and (2) match based on Weight. The screen below shows the basic idea:

![XLOOKUP with 2 conditions in 2 steps](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/XLOOKUP_approximate_match_2_steps.png "XLOOKUP with 2 conditions in 2 steps")

One way to solve this problem is with XLOOKUP + the [IF function](https://exceljet.net/functions/if-function)
 to perform the required filtering. One reason this works nicely is that the IF function returns 12 results, which correspond to the 12 rows in the table. This means XLOOKUP can return the right value in the table because all 12 rows are still intact. You could instead use the [FILTER function](https://exceljet.net/functions/filter-function)
, with a bit more configuration. See below for details.

### Background reading

This article assumes you are familiar with Excel Tables and XLOOKUP. If not, see:

*   [Excel Tables](https://exceljet.net/articles/excel-tables)
     - introduction and overview
*   [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
     - overview with examples and videos

### Basic XLOOKUP

In XLOOKUP formulas, a _lookup\_array_ and _return\_array_ are provided as arguments. XLOOKUP locates the lookup value in the lookup array. Then it returns the corresponding value in the return array. If you are new to XLOOKUP, [this short video](https://exceljet.net/videos/basic-xlookup-example)
 shows a basic example.

Looking at this problem from the inside out, the core of the solution is an approximate match lookup based on weight. To illustrate, the screen below shows a simplified version of the same problem with the Service removed:

![XLOOKUP simple approximate match example](https://exceljet.net/sites/default/files/images/formulas/inline/XLOOKUP_simple_approximate_match_example.png "XLOOKUP simple approximate match example")

The formula in cell F5 is:

    =XLOOKUP(F4,B5:B8,C5:C8,,-1)

The _lookup\_array_ is the weight in the range B5:B8, and the _return\_array_ is the cost in the range C5:C8. Notice the _match\_mode_ argument inside XLOOKUP is set to -1, to find the largest value in B5:B8 that is _less than or equal to_ the lookup value in cell F4. In this case, the largest value less than or equal to 72 is 60, so XLOOKUP matches the 60 and returns $18.00 as a final result:

    =INDEX(C5:C8,3) // returns 18

So far, so good. We have a simple working XLOOKUP formula that returns the correct cost based on an approximate match lookup. The challenge is that we also need to match based on the Service. To do that, we need to extend the formula to handle another condition.

### Adding criteria for service

We know how to look up costs based on weight. The remaining challenge is that we also need to take into account the Service. For simple exact-match scenarios, we can use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, [as explained here](https://exceljet.net/formulas/xlookup-with-multiple-criteria)
. But in this example, we need to perform an _approximate match_, so using Boolean logic will not work well. Another approach is to "filter out" extraneous entries in the table so we are left only with entries that correspond to the Service we are looking up. The classic way to do this is with the [IF function](https://exceljet.net/functions/if-function)
. This is the approach used in the example shown, where the formula in cell G8 is:

    =XLOOKUP(G7,IF(data[Service]=G6,data[Weight]),data[Cost],,-1)

The filtering is done with the IF function, which appears inside the XLOOKUP function like this:

    IF(data[Service]=G6,data[Weight])

This code tests the values in the Service column to see if they match the value in G6. Where there is a match, the corresponding values in with Weight column are returned. If there is no match, the IF function returns FALSE. Because there are 12 rows in the table, the IF function returns an [array](https://exceljet.net/glossary/array)
 that contains 12 results like this:

    {FALSE;FALSE;FALSE;FALSE;1;16;60;120;FALSE;FALSE;FALSE;FALSE}

Notice the only weights that remain in the array are those that correspond to the "2-Day-Air" service; all other weights have been replaced with FALSE. You can visualize this operation in the original data as shown below:

![After the IF function runs](https://exceljet.net/sites/default/files/images/formulas/inline/XLOOKUP_approximate_match_after_IF_function.png "After the IF function runs")

This [array](https://exceljet.net/glossary/array)
 is delivered directly to XLOOKUP as the _lookup\_array:_

    =XLOOKUP(G7,{FALSE;FALSE;FALSE;FALSE;1;16;60;120;FALSE;FALSE;FALSE;FALSE},data[Cost],,-1)

With a weight of 72 in cell G7, XLOOKUP matches 60 and returns $45.00 as the final result. Notice that we are using -1 inside XLOOKUP as the _match\_mode_ argument. This will cause XLOOKUP to match a value that is less than or equal to the lookup value.

### XLOOKUP with FILTER

Another way to solve this problem is with XLOOKUP and the [FILTER function,](https://exceljet.net/functions/filter-function)
 like this:

    =XLOOKUP(G7,FILTER(data[Weight],data[Service]=G6),FILTER(data[Cost],data[Service]=G6),,-1)

In this formula, we remove data for other services with the FILTER function. Inside XLOOKUP, FILTER creates the _lookup\_array_ like this:

    FILTER(data[Weight],data[Service]=G6) // returns {1;16;60;120}

The _return\_array_ is created in the same way:

    FILTER(data[Cost],data[Service]=G6) // returns {22.5;30;45;60}

After FILTER runs, XLOOKUP is only working with values associated with the 2-Day air service:

    =XLOOKUP(G7,{1;16;60;120},{22.5;30;45;60},,-1)

With 72 in cell G7, XLOOKUP returns the same result as before, a cost of $45.00. This formula works nicely and is perhaps more intuitive than XLOOKUP + IF. However, the tradeoff is a more complex formula since FILTER must be used twice.

Related formulas
----------------

[![Excel formula: XLOOKUP basic approximate match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20basic%20approximate%20match.png "Excel formula: XLOOKUP basic approximate match")](https://exceljet.net/formulas/xlookup-basic-approximate-match)

### [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)

In the example shown, the table in B4:C13 contains quantity-based discounts. As the quantity increases, the discount also increases. The table in E4:F10 shows the discount returned by XLOOKUP for several random quantities. XLOOKUP is configured to use the quantity in column E to find the...

[![Excel formula: XLOOKUP with logical criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP%20with%20logical%20criteria.png "Excel formula: XLOOKUP with logical criteria")](https://exceljet.net/formulas/xlookup-with-logical-criteria)

### [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)

XLOOKUP can handle arrays natively, which makes it a very useful function when constructing criteria based on multiple logical expressions. In the example shown, we are looking for the order number of the first order to Chicago over $250. We are constructing a lookup array using the following...

[![Excel formula: INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_approximate_match_with_multiple_criteria.png "Excel formula: INDEX and MATCH approximate match with multiple criteria")](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

### [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)

In this example, the goal is to look up the correct shipping cost for an item based on the shipping service selected and the item's weight. At the core, this is an approximate match lookup based on weight. The challenge is that we also need to filter by service. This means we must apply criteria in...

Related functions
-----------------

[![Excel XLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xlookup_function.png "Excel XLOOKUP function")](https://exceljet.net/functions/xlookup-function)

### [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)

The Excel XLOOKUP function is a powerful tool designed to look up a value in one range and return a corresponding value in another range — it supports approximate and exact matching, wildcards, regular expressions (regex), reverse searches, and lookups in vertical or horizontal ranges....

[![Excel IF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_If_function.png "Excel IF function")](https://exceljet.net/functions/if-function)

### [IF Function](https://exceljet.net/functions/if-function)

The Excel IF function performs a logical test and returns one result when the logical test returns TRUE and another when the logical test returns FALSE. For example, to "pass" scores above 70: =IF(A1>70,"Pass","Fail"). More than one condition can be tested by nesting IF functions. The IF...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20Example-play.png)](https://exceljet.net/videos/basic-xlookup-example)

### [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)

In this video, we’ll set up the XLOOKUP function with a basic example. The XLOOKUP function is a more flexible replacement for VLOOKUP , and it's just as easy to use. In this worksheet, we have population data for some of the largest cities in the world. Let's configure the XLOOKUP function to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20XLOOKUP%20approximate%20match-Play.png)](https://exceljet.net/videos/basic-xlookup-approximate-match)

### [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)

In this video, we’ll set up the XLOOKUP function to perform an approximate match. In this worksheet, the table in B5:C9 contains quantity-based discounts. As the quantity increases, the discount also increases. Let's set up the XLOOKUP function to calculate the correct discount for each quantity...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [XLOOKUP basic approximate match](https://exceljet.net/formulas/xlookup-basic-approximate-match)
    
*   [XLOOKUP with logical criteria](https://exceljet.net/formulas/xlookup-with-logical-criteria)
    
*   [INDEX and MATCH approximate match with multiple criteria](https://exceljet.net/formulas/index-and-match-approximate-match-with-multiple-criteria)
    

### Functions

*   [XLOOKUP Function](https://exceljet.net/functions/xlookup-function)
    
*   [IF Function](https://exceljet.net/functions/if-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [Basic XLOOKUP example](https://exceljet.net/videos/basic-xlookup-example)
    
*   [Basic XLOOKUP approximate match](https://exceljet.net/videos/basic-xlookup-approximate-match)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
*   [Excel Tables](https://exceljet.net/training/excel-tables)
    

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