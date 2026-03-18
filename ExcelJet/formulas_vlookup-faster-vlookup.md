# VLOOKUP faster VLOOKUP - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/vlookup-faster-vlookup

---

[Skip to main content](https://exceljet.net/formulas/vlookup-faster-vlookup#main-content)

[](https://exceljet.net/formulas/vlookup-faster-vlookup#)

*   [Previous](https://exceljet.net/formulas/vlookup-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/vlookup-from-another-sheet)
    

[Lookup](https://exceljet.net/formulas#Lookup)

VLOOKUP faster VLOOKUP
======================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[VLOOKUP](https://exceljet.net/functions/vlookup-function)

[NA](https://exceljet.net/functions/na-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7818/download?token=CH0VmsEy)
 (14.18 MB)

![Excel formula: VLOOKUP faster VLOOKUP](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/VLOOKUP_faster_VLOOKUP.png "Excel formula: VLOOKUP faster VLOOKUP")

Summary
-------

With large sets of data, exact match VLOOKUP can be painfully slow, taking minutes to calculate. However, one way to speed up VLOOKUP in this situation is to use VLOOKUP twice, both times in approximate match mode. In the example shown, the formula in F5 is:

    =IF(VLOOKUP(E5,data,1)=E5,VLOOKUP(E5,data,2),NA())

where **data** is an [Excel Table](https://exceljet.net/articles/excel-tables)
 in the range B5:C1000004. Note that both instances of VLOOKUP are configured to use approximate match mode by omitting the _range\_lookup_ argument. If the invoice number is found, we get the correct amount for the invoice. If the invoice number is not found, the result is an #N/A error, which means the invoice number does not exist in the data.

_Notes: (1) I ran into this formula several years ago [in an article by Charles Williams](https://fastexcel.wordpress.com/2012/03/29/vlookup-tricks-why-2-vlookups-are-better-than-1-vlookup/)
. Charles is a Microsoft Excel MVP who specializes in speed and performance. (2) This approach approximates a binary search with VLOOKUP. The [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 can support a [binary search](https://exceljet.net/formulas/xlookup-binary-search)
 directly. (3) The attached worksheet is large (about 14 MB) because it contains 1 million rows of data._

Generic formula
---------------

    =IF(VLOOKUP(A1,data,1)=A1,VLOOKUP(A1,data,n),NA())

Explanation 
------------

In this example, VLOOKUP is configured to look up 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, _most of the invoice numbers do not appear in column B_. This means we need to configure VLOOKUP to use an _exact match_, and exact match lookups on large data sets can be painfully slow. However, because the data is sorted by invoice number, we can use the modified VLOOKUP formula seen in the worksheet. Although this formula uses VLOOKUP twice, it runs quickly.

### Exact-match VLOOKUP is slow

When you use VLOOKUP in "exact match mode" on a large set of data, it can really slow down the calculation time in a worksheet. With very large sets of data, the calculation time can be _minutes_. To use VLOOKUP in exact match mode, provide FALSE or zero as the fourth argument, _range\_lookup_:

    =VLOOKUP(value,data,n,FALSE) // exact match
    

The reason VLOOKUP is slow in this mode is that there is _no requirement_ that the lookup values be sorted. As a result, VLOOKUP must check every record in the data set until a match is found, or not. This is sometimes referred to as a _linear search_.

### Approximate-match VLOOKUP is very fast

In approximate-match mode, VLOOKUP is extremely fast. To use approximate-match VLOOKUP, sort the data by the first column (the lookup column), then specify TRUE for _range\_lookup_ or omit the argument:

    =VLOOKUP(value,data,n,TRUE) // approximate match
    =VLOOKUP(value,data,n) // approximate match
    

With very large sets of data, changing to approximate-match VLOOKUP can mean a _dramatic_ speed increase. This is because VLOOKUP will assume data _is sorted_ and use a different algorithm to speed up searching, sometimes called a binary search.

_For a complete VLOOKUP overview with many examples, see [How to use VLOOKUP](https://exceljet.net/functions/vlookup-function)
._

### The problem

At first glance, a solution seems simple: sort the data, and use VLOOKUP in approximate match mode. However, the problem is that VLOOKUP won't return an error if a value is not found. Instead, it may return an incorrect result that looks completely normal. For example, in the worksheet shown, if we configure VLOOKUP to find the Amount for invoice 500010 with _range\_lookup_ set to TRUE, the result is 9225 even though invoice 500010 _does not exist in the table_:

    =VLOOKUP(500010,data,2,TRUE) // returns 9225

This happens because VLOOKUP's behavior with approximate match enabled is "exact match or next smaller value". When VLOOKUP can't find invoice 500010, it matches the next smaller invoice number, which is 500008, and returns 9225. So, while the formula runs very quickly, the result is not reliable. Obviously, this is not something you want to explain to your boss.

### A solution with VLOOKUP + VLOOKUP

One way to speed up VLOOKUP in this situation is to use VLOOKUP twice, both times in approximate match mode. This may seem counterintuitive because we are calling VLOOKUP twice. However, two fast operations are better than one slow operation. The trick is to structure the formula in a way that _requires an exact match result_. We do that by testing the result of the first VLOOKUP to see if did actually find the lookup value. In the worksheet shown, the formula in F5, copied down, is:

    =IF(VLOOKUP(E5,data,1)=E5,VLOOKUP(E5,data,2),NA())

Notice the IF function controls the flow of the formula. If we _do find the lookup value_, we run the second lookup. Otherwise, we return an error. The _logical\_test_ inside the IF function looks like this:

    VLOOKUP(E5,data,1)=E5

Here, we use VLOOKUP to find and return the lookup value itself, and we do so in approximate match mode by omitting the _range\_lookup_ argument. Remember, _VLOOKUP defaults to an approximate match_. Then we test the result against the lookup value. If this test returns TRUE, we know the lookup value exists in the data and we run the second VLOOKUP to fetch the desired value:

    VLOOKUP(E5,data,2)

However, if the test returns FALSE, it means we _didn't find the lookup value_. In that case, we simply return an #N/A error with the [NA function](https://exceljet.net/functions/na-function)
:

    NA()  // returns #N/A

To summarize: if we find the invoice number, we look up the amount. If we don't find an invoice number return #N/A error, which tells us the invoice number does not exist in the data. Even though the formula uses the VLOOKUP function two times, performance is good, because both instances of VLOOKUP use approximate match mode, which runs very quickly.

### Summary

With large sets of data, exact match VLOOKUP can run painfully slow when configured for an exact match. This is because there is no requirement that the lookup values be sorted and VLOOKUP must perform a linear search, which is a slow operation when there are many values to check. On the other hand, if data is sorted, VLOOKUP can be configured for an approximate match by setting _range\_lookup_ to TRUE, or by omitting _range\_lookup_ altogether. In this configuration, VLOOKUP _r__uns very fast._ However, VLOOKUP may return an incorrect result. This happens because VLOOKUP's behavior with approximate match enabled is "exact match or next smaller value", so VLOOKUP matches the previous value when a match is not found. One way around this problem is to use VLOOKUP twice, both times in approximate match mode. The trick is to structure the formula in a way that leverages two fast lookups in a way that still ensures an exact match result.

### Notes

1.  _This approach is overkill unless lookup_ _performance is an issue._
2.  _Data must be sorted by lookup value in ascending order._
3.  _The newer [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
     has a very fast binary search option._

Related formulas
----------------

[![Excel formula: VLOOKUP two-way lookup ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_two-way_lookup.png "Excel formula: VLOOKUP two-way lookup ")](https://exceljet.net/formulas/vlookup-two-way-lookup)

### [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)

In this example, the goal is to perform a two-way lookup based on the name in cell H4 and the month in cell H5 with the VLOOKUP function. Inside the VLOOKUP function, the column index argument is normally hard-coded as a static number. However, you can create a dynamic column index number by using...

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Get employee information with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_employee_information_with_VLOOKUP.png "Excel formula: Get employee information with VLOOKUP")](https://exceljet.net/formulas/get-employee-information-with-vlookup)

### [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)

The goal is to look up and retrieve employee information in a table that contains unique id values in the first column. The VLOOKUP function is straightforward to use with data in this format, but you can easily use the XLOOKUP function as well. See below for a detailed explanation of both...

[![Excel formula: Merge tables with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20calculated%20column.png "Excel formula: Merge tables with VLOOKUP")](https://exceljet.net/formulas/merge-tables-with-vlookup)

### [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)

This is a standard "exact match" VLOOKUP formula with one exception: the column index is calculated using the COLUMN function. When the COLUMN function is used without any arguments, it returns a number that corresponds to the current column. In this case, the first instance of the formula in...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: XLOOKUP binary search](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_binary_search.png "Excel formula: XLOOKUP binary search")](https://exceljet.net/formulas/xlookup-binary-search)

### [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)

In this example, the goal is to look up amounts for 1000 invoice numbers in a table that contains 1 million invoices. The catch is that not all of the 1000 invoice numbers exist in the source data. In fact, most of the invoice numbers do not appear in column B . This means we need to take care to...

Related functions
-----------------

[![Excel VLOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_vlookup_function.png "Excel VLOOKUP function")](https://exceljet.net/functions/vlookup-function)

### [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)

The Excel VLOOKUP function is used to retrieve information from a table using a lookup value. The lookup values must appear in the _first_ column of the table, and the information to retrieve is specified by _column number_. VLOOKUP supports approximate and exact...

[![Excel NA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20na%20function.png "Excel NA function")](https://exceljet.net/functions/na-function)

### [NA Function](https://exceljet.net/functions/na-function)

The Excel NA function returns the #N/A error. #N/A means "not available" or "no value available". You can use the NA function to display the #N/A error when information is missing.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup)

### [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)

VLOOKUP is one of the most important lookup functions in Excel. The V stands for "vertical" which means you can use VLOOKUP to look up values in a table that's arranged vertically. Let's take a look. Here we have a list of employees in a table. Let's use VLOOKUP to build a simple form that...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20VLOOKUP%20for%20approximate%20matches-thumb.png)](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

### [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)

In a lot of cases, you'll use VLOOKUP to find exact matches based on some kind of unique id, but there are many situations where you'll want to use VLOOKUP to find non-exact matches. A classic case is using VLOOKUP to find a commission rate based on a sales number. Let's take a look. Here we have...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20replace%20nested%20IFs%20with%20VLOOKUP-thumb.png)](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

### [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)

You might build or inherit a worksheet that uses a series of nested IF statements to assign values of some kind. Many people use nested IF statements this way because the approach is easy once you get the hang of it. But nested IF statements can be difficult to maintain and debug. Let's look at how...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP two-way lookup](https://exceljet.net/formulas/vlookup-two-way-lookup)
    
*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Get employee information with VLOOKUP](https://exceljet.net/formulas/get-employee-information-with-vlookup)
    
*   [Merge tables with VLOOKUP](https://exceljet.net/formulas/merge-tables-with-vlookup)
    
*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [XLOOKUP binary search](https://exceljet.net/formulas/xlookup-binary-search)
    

### Functions

*   [VLOOKUP Function](https://exceljet.net/functions/vlookup-function)
    
*   [NA Function](https://exceljet.net/functions/na-function)
    

### Videos

*   [How to use VLOOKUP](https://exceljet.net/videos/how-to-use-vlookup)
    
*   [How to use VLOOKUP for approximate matches](https://exceljet.net/videos/how-to-use-vlookup-for-approximate-matches)
    
*   [How to replace nested IFs with VLOOKUP](https://exceljet.net/videos/how-to-replace-nested-ifs-with-vlookup)
    

### Articles

*   [23 things you should know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
    

### Links

*   [Why 2 VLOOKUPs are better than 1 VLOOKUP (Charles Williams)](https://fastexcel.wordpress.com/2012/03/29/vlookup-tricks-why-2-vlookups-are-better-than-1-vlookup/)
    

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