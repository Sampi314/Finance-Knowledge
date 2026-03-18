# Group numbers at uneven intervals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/group-numbers-at-uneven-intervals

---

[Skip to main content](https://exceljet.net/formulas/group-numbers-at-uneven-intervals#main-content)

[](https://exceljet.net/formulas/group-numbers-at-uneven-intervals#)

*   [Previous](https://exceljet.net/formulas/group-arbitrary-text-values)
    
*   [Next](https://exceljet.net/formulas/group-numbers-with-vlookup)
    

[Grouping](https://exceljet.net/formulas#Grouping)

Group numbers at uneven intervals
=================================

by Dave Bruns · Updated 28 Jun 2019

Related functions 
------------------

[LOOKUP](https://exceljet.net/functions/lookup-function)

![Excel formula: Group numbers at uneven intervals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Group%20numbers%20at%20uneven%20intervals3.png "Excel formula: Group numbers at uneven intervals")

Summary
-------

To group numbers into intervals of unequal size, you can use the LOOKUP function. In the example shown, the LOOKUP function is used to group people by age into at intervals of unequal size. The formula in D5 is:

    =LOOKUP(C5,age,group)
    

Where "age" is the [named range](https://exceljet.net/glossary/named-range)
 F5:F8 and "group" is the named range G5:G8.

Generic formula
---------------

    =LOOKUP(value,intervals,groups)

Explanation 
------------

To do this, LOOKUP is configured as follows:

*   Lookup values are ages in column C
*   The lookup vector is the named range "age" (F5:F8)
*   The result vector is the named range "group" (G5:G8)

With this setup, LOOKUP performs an approximate match on the numeric values in column F, and returns the associated value from column G.

The LOOKUP function always performs an approximate match, with the following behavior:

*   If LOOKUP finds an exact match in the age column, the corresponding group is returned.
*   If no exact match is found, LOOKUP will traverse the age column until a larger value is found, then "step back" to the previous row.
*   If an age is greater than 50 (the highest value), LOOKUP will return the group associated with 50 ("50+").
*   If age is less than the smallest value in the age column, LOOKUP will return #N/A.

_Note: ages must appear in ascending order. Double-check custom intervals - it's easy to make a mistake :)_

### With hardcoded values

If you want to do this kind of grouping without a table on the worksheet, you can hardcode values into LOOKUP as [array constants](https://exceljet.net/glossary/array-constant)
 like this:

    =LOOKUP(C5,{0,10,36,50},{"<10","10-35","36-49","50+"})
    

Related formulas
----------------

[![Excel formula: Group times into unequal buckets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20times%20into%20unequal%20buckets.png "Excel formula: Group times into unequal buckets")](https://exceljet.net/formulas/group-times-into-unequal-buckets)

### [Group times into unequal buckets](https://exceljet.net/formulas/group-times-into-unequal-buckets)

If you need to group times into buckets that are not the same size (i.e. 12 AM-7 AM, 7 AM-12 PM, etc.) you can use the VLOOKUP function in approximate match mode. The problem There are several ways to group times in Excel. If you just need to group times by the hour, a pivot table is very quick and...

[![Excel formula: Group arbitrary text values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/group%20arbitrary%20text%20values.png "Excel formula: Group arbitrary text values")](https://exceljet.net/formulas/group-arbitrary-text-values)

### [Group arbitrary text values](https://exceljet.net/formulas/group-arbitrary-text-values)

This formula uses the value in cell E5 for a lookup value, the named range "key" (H5:I9) for the lookup table, 2 to indicate "2nd column", and 0 as the last argument indicate exact match. You can also use FALSE instead of zero if you like. VLOOKUP simply looks up the value and returns the group...

[![Excel formula: Map inputs to arbitrary values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/map%20inputs%20to%20arbitrary%20values.png "Excel formula: Map inputs to arbitrary values")](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

### [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)

In this example, the goal is to map the numbers 1-6 to the arbitrary values seen in the table below. For example: If the input is 1, the output should be 10 If the input is 2, the output should be 81 If the input is 3, the output should be 17 If the input is 4, the output should be 23 And so on.....

Related functions
-----------------

[![Excel LOOKUP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20lookup%20function.png "Excel LOOKUP function")](https://exceljet.net/functions/lookup-function)

### [LOOKUP Function](https://exceljet.net/functions/lookup-function)

The Excel LOOKUP function performs an approximate match lookup in a one-column or one-row range, and returns the corresponding value from another one-column or one-row range. LOOKUP's default behavior makes it useful for solving certain problems in Excel.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20a%20pivot%20table%20by%20age%20range-play.png)](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)

### [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)

One of the most powerful features of pivot tables is their ability to group data, especially by number or date. In this video, I'll show you how to group data by age range. Here we have a set of data that represents voting results. There are 300 results total, and, in each row, we have name, gender...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20group%20a%20pivot%20table%20manually-thumb.png)](https://exceljet.net/videos/how-to-group-a-pivot-table-manually)

### [How to group a pivot table manually](https://exceljet.net/videos/how-to-group-a-pivot-table-manually)

The ability to group data is one of the most powerful and useful features in a pivot table. And although pivot tables can automatically group things like dates, times, and numbers, you can also manually group data into your own groups. Let’s take a look. This pivot table shows a breakdown of sales...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Group times into unequal buckets](https://exceljet.net/formulas/group-times-into-unequal-buckets)
    
*   [Group arbitrary text values](https://exceljet.net/formulas/group-arbitrary-text-values)
    
*   [Map inputs to arbitrary values](https://exceljet.net/formulas/map-inputs-to-arbitrary-values)
    

### Functions

*   [LOOKUP Function](https://exceljet.net/functions/lookup-function)
    

### Videos

*   [How to group a pivot table by age range](https://exceljet.net/videos/how-to-group-a-pivot-table-by-age-range)
    
*   [How to group a pivot table manually](https://exceljet.net/videos/how-to-group-a-pivot-table-manually)
    

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