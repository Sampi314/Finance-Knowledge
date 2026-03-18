# Count holidays between two dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-holidays-between-two-dates

---

[Skip to main content](https://exceljet.net/formulas/count-holidays-between-two-dates#main-content)

[](https://exceljet.net/formulas/count-holidays-between-two-dates#)

*   [Previous](https://exceljet.net/formulas/count-day-of-week-between-dates)
    
*   [Next](https://exceljet.net/formulas/count-times-in-a-specific-range)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Count holidays between two dates
================================

by Dave Bruns · Updated 3 Apr 2017

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count holidays between two dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20holidays%20between%20two%20dates.png "Excel formula: Count holidays between two dates")

Summary
-------

To count holidays that occur between two dates, you can use the SUMPRODUCT function.

In the example shown, the formula in F8 is:

    =SUMPRODUCT((B4:B12>=F5)*(B4:B12<=F6))
    

Generic formula
---------------

    =SUMPRODUCT((holidays>=start)*(holidays<=end))

Explanation 
------------

This formula uses two expressions in a single array inside the SUMPRODUCT function.

The first expression tests every holiday date to see if it's greater than or equal to the start date in F5:

    (B4:B12>=F5)
    

This returns an array of TRUE/FALSE values like this:

{FALSE;FALSE;FALSE;FALSE;TRUE;TRUE;TRUE;TRUE;TRUE}

The second expression tests every holiday date to see if it's less than or equal to the end date in F6:

    (B4:B12<=F6)
    

which returns an array of TRUE/FALSE values like this:

{TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE}

The multiplication of these two arrays automatically coerces the TRUE/FALSE values to ones and zeros, resulting in arrays that look like this:

    =SUMPRODUCT(({0;0;0;0;1;1;1;1;1})*({1;1;1;1;1;1;1;1;0}))
    

After multiplication, we have just one array like this:

    =SUMPRODUCT({0;0;0;0;1;1;1;1;0})
    

Finally, SUMPRODUCT sums the items in the array and returns 4.

### Holidays on weekdays only

To count holidays that occur on weekdays only (Mon-Fri), you can extend the formula like this:

    =SUMPRODUCT((rng>=F5)*(rng<=F6)*(WEEKDAY(rng,2)<6))
    

where **rng** is a range containing holiday dates.

Related formulas
----------------

[![Excel formula: List holidays between two dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20holidays%20between%20two%20dates.png "Excel formula: List holidays between two dates")](https://exceljet.net/formulas/list-holidays-between-two-dates)

### [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)

At a high level, this formula uses a nested IF function to return an array of holidays between two dates. This array is then processed by the TEXTJOIN function, which converts the array to text using a comma as the delimiter. Working from the inside out, we generate the array of matching holidays...

[![Excel formula: Count dates by day of week](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20dates%20by%20day%20of%20week.png "Excel formula: Count dates by day of week")](https://exceljet.net/formulas/count-dates-by-day-of-week)

### [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)

You might wonder why we aren't using COUNTIF or COUNTIFS . These functions seem like the obvious solution. However, without adding a helper column that contains a weekday value, there is no way to create criteria for COUNTIF to count weekdays in a range of dates. Instead, we use the versatile...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List holidays between two dates](https://exceljet.net/formulas/list-holidays-between-two-dates)
    
*   [Count dates by day of week](https://exceljet.net/formulas/count-dates-by-day-of-week)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

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