# FILTER on top n values with criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/filter-on-top-n-values-with-criteria

---

[Skip to main content](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria#main-content)

[](https://exceljet.net/formulas/filter-on-top-n-values-with-criteria#)

*   [Previous](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Next](https://exceljet.net/formulas/filter-text-contains)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

FILTER on top n values with criteria
====================================

by Dave Bruns · Updated 25 Aug 2022

Related functions 
------------------

[FILTER](https://exceljet.net/functions/filter-function)

[LARGE](https://exceljet.net/functions/large-function)

[SORT](https://exceljet.net/functions/sort-function)

![Excel formula: FILTER on top n values with criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/FILTER%20on%20top%20n%20values%20with%20criteria.png "Excel formula: FILTER on top n values with criteria")

Summary
-------

To filter data to show the top n values that meet specific criteria, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 together with the [LARGE](https://exceljet.net/functions/large-function)
 and [IF](https://exceljet.net/functions/if-function)
 functions. In the example shown, the formula in F5 is:

    =FILTER(data,(score>=LARGE(IF(group="b",score),3))*(group="b"))
    

where **data** (B5:D16), **group** (C5:C16) and **score** (D5:D16) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =FILTER(data,(range>=LARGE(IF(criteria),n))*(criteria))
    

Explanation 
------------

This formula uses the FILTER function to retrieve data based on a logical test constructed with the [LARGE](https://exceljet.net/functions/large-function)
 and [IF](https://exceljet.net/functions/if-function)
 functions. The result is the top 3 scores in group B.

The FILTER function applies criteria with the _include_ argument. In this example, criteria are constructed with [boolean logic](https://exceljet.net/glossary/boolean-logic)
 like this:

    (score>=LARGE(IF(group="b",score),3))*(group="b")
    

The left side of the expression targets scores greater than or equal to the 3rd highest score in group B:

    score>=LARGE(IF(group="b",score),3)
    

The IF function is used to make sure LARGE is only working with group B scores. Because we have 12 scores total, IF returns an [array](https://exceljet.net/glossary/array)
 with 12 results like this:

    {FALSE;65;FALSE;80;FALSE;88;FALSE;76;FALSE;86;FALSE;83}
    

Notice the only scores that survive the operation are from Group B. All other scores are FALSE. This array is returned directly to LARGE as the _array_ argument:

    LARGE({FALSE;65;FALSE;80;FALSE;88;FALSE;76;FALSE;86;FALSE;83},3)
    

LARGE ignores the FALSE values and returns the 3rd highest score, 83.

We can now simplify the formula to:

    =FILTER(data,(score>=83)*(group="b"))
    

which resolves to:

    =FILTER(data,{0;0;0;0;0;1;0;0;0;1;0;1})
    

Finally, FILTER returns records for Mason, Annie, and Cassidy, which spill into the range F5:H7.

### Sort results by score

By default, FILTER will return matching records in the same order they appear in the source data. To sort results in _descending order by score_, you can [nest](https://exceljet.net/glossary/nesting)
 the original FILTER formula inside the [SORT function](https://exceljet.net/videos/basic-sort-function-example)
 like this:

    =SORT(FILTER(data,(score>=LARGE(IF(group="b",score),3))*(group="b")),3,-1)
    

Here, FILTER returns results directly to the SORT function as the _array_ argument. _Sort\_index_ is set to 3 (score) and _sort\_order_ is set to -1, for _descending_ order.

Related formulas
----------------

[![Excel formula: FILTER on top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20top%20n%20values.png "Excel formula: FILTER on top n values")](https://exceljet.net/formulas/filter-on-top-n-values)

### [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)

This formula uses the FILTER function to retrieve data based on a logical test constructed with the LARGE function. The LARGE function is a simple way to get the nth largest value in a range. Simply provide a range for the first argument ( array ), and a value for n as the second argument ( k ): =...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: Filter this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20this%20or%20that.png "Excel formula: Filter this or that")](https://exceljet.net/formulas/filter-this-or-that)

### [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)

This formula relies on the FILTER function to retrieve data based on a logical test built with simple expressions and boolean logic : (D5:D14="red")+(D5:D14="blue") After each expression is evaluated, we have the following two arrays : ({TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE...

[![Excel formula: Filter text contains](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20text%20contains.png "Excel formula: Filter text contains")](https://exceljet.net/formulas/filter-text-contains)

### [Filter text contains](https://exceljet.net/formulas/filter-text-contains)

This formula relies on the FILTER function to retrieve data based on a logical test. The array argument is provided as B5:D14, which contains the full set of data without headers. The include argument is based on a logical test based on the ISNUMBER and SEARCH functions: ISNUMBER(SEARCH("rd",B5:B14...

[![Excel formula: Filter exclude blank values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/filter%20exclude%20blank%20values.png "Excel formula: Filter exclude blank values")](https://exceljet.net/formulas/filter-exclude-blank-values)

### [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)

The FILTER function is designed to extract data that matches one or more criteria. In this case, we want to apply criteria that requires all three columns in the source data (Name, Group, and Room) to have data. In other words, if a row is missing any of these values, we want to exclude that row...

[![Excel formula: Name of nth largest value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/name%20of%20nth%20largest%20value.png "Excel formula: Name of nth largest value")](https://exceljet.net/formulas/name-of-nth-largest-value)

### [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)

In a nutshell, this formula uses the LARGE function to find the nth largest value in a set of data. Once we have that value, we plug it into a standard INDEX and MATCH formula to retrieve the associated name. In other words, we use the nth largest value like a "key" to retrieve associated...

Related functions
-----------------

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

[![Excel LARGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20large%20function_0.png "Excel LARGE function")](https://exceljet.net/functions/large-function)

### [LARGE Function](https://exceljet.net/functions/large-function)

The Excel LARGE function returns a numeric value based on its position in a list when sorted by value in _descending_ order. In other words, LARGE can retrieve the "nth largest" value – 1st largest value, 2nd largest value, 3rd largest value, etc.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20show%20top%20or%20bottom%20results-Play.png)](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

### [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)

In this video, we'll use the FILTER function to show the top or bottom results in a set of data. Here we have some test scores for a group of students. In column F, I want to set up a formula to display the top students by score. Now, I'm going to use the FILTER function, but we'll need a way to...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [FILTER on top n values](https://exceljet.net/formulas/filter-on-top-n-values)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [Filter this or that](https://exceljet.net/formulas/filter-this-or-that)
    
*   [Filter text contains](https://exceljet.net/formulas/filter-text-contains)
    
*   [Filter exclude blank values](https://exceljet.net/formulas/filter-exclude-blank-values)
    
*   [Name of nth largest value](https://exceljet.net/formulas/name-of-nth-largest-value)
    

### Functions

*   [FILTER Function](https://exceljet.net/functions/filter-function)
    
*   [LARGE Function](https://exceljet.net/functions/large-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    

### Videos

*   [How to show top or bottom n results](https://exceljet.net/videos/how-to-show-top-or-bottom-n-results)
    

### Articles

*   [Dynamic array formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
    
*   [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    

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