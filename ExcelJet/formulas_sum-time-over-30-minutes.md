# Sum time over 30 minutes - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-time-over-30-minutes

---

[Skip to main content](https://exceljet.net/formulas/sum-time-over-30-minutes#main-content)

[](https://exceljet.net/formulas/sum-time-over-30-minutes#)

*   [Previous](https://exceljet.net/formulas/sum-time-by-week-and-project)
    
*   [Next](https://exceljet.net/formulas/sum-time-with-sumifs)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Sum time over 30 minutes
========================

by Dave Bruns · Updated 16 Sep 2018

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[TIME](https://exceljet.net/functions/time-function)

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Sum time over 30 minutes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum%20time%20over%2030%20minutes.png "Excel formula: Sum time over 30 minutes")

Summary
-------

To sum the total amount of time over 30 minutes, given a set of times that represent duration, you can use the SUMPRODUCT and TIME functions. In the example shown, the formula in G5 is:

    =SUMPRODUCT((times-TIME(0,30,0))*(times>TIME(0,30,0)))
    

where "times" is the [named range](https://exceljet.net/glossary/named-range)
 C5:C14.

Generic formula
---------------

    =SUMPRODUCT((range-TIME(0,30,0))*(range>TIME(0,30,0)))

Explanation 
------------

This formula uses the SUMPRODUCT function to sum the result of two expressions that yield arrays. The goal is to sum only time greater than 30 minutes, the "surplus" or "extra" time. The first expression subtracts 30 minutes from every time in the named range "times":

    times-TIME(0,30,0)
    

This results in an array like this:

    {-0.00347222222222222;0.00694444444444444;0.00347222222222222;-0.00694444444444444;0.0138888888888889;0.00694444444444444;0;0.00486111111111111;0.00833333333333333;-0.0104166666666667}
    

The second expression is a logical test for all times greater than 30 minutes:

    times>TIME(0,30,0)
    

This creates an array of TRUE FALSE values:

    {FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;TRUE;FALSE}
    

Inside SUMPRODUCT, these two arrays are multiplied together to create this array:

    {0;0.00694444444444444;0.00347222222222222;0;0.0138888888888889;0.00694444444444444;0;0.00486111111111111;0.00833333333333333;0}
    

Notice negative values in the first array are now zeros. During multiplication, the TRUE FALSE values are converted to 1 and zero, so FALSE values "cancel out" times that are not greater than 30 min. Finally, SUMPRODUCT returns the sum of all values in the array, 1 hour and 4 minutes (1:04).

### Alternative with SUMIFS and COUNTIFS

By itself, SUMIFS cannot sum the delta of time values greater than 30 minutes. SUMIFS and COUNTIFS can be used together to get the same result as SUMPRODUCT above:

    =SUMIFS(times,times,">0:30")-(COUNTIFS(times,">0:30")*"0:30")
    

### Times over 24 hours

If total times may exceed 24 hours, use this a [custom time format](https://exceljet.net/articles/custom-number-formats)
 like this:

    [h]:mm:ss
    

The square bracket syntax tells Excel not to "roll over" times greater than 24 hours.

### With a helper column

As shown in the example, you can also add a helper column to calculate and sum time deltas. The formula in D5, copied down, is:

    =MAX(C5-"00:30",0)
    

Here, MAX is used to get rid of negative time deltas, caused by times in column C that are less than 30 minutes. Notice the result in D15 is the same as the result in G5.

Related formulas
----------------

[![Excel formula: Sum race time splits](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sum%20race%20time%20splits.png "Excel formula: Sum race time splits")](https://exceljet.net/formulas/sum-race-time-splits)

### [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)

Excel times are fractional numbers . This means you can add times together with the SUM function to get total durations. However, you must take care to enter times with the right syntax and use a suitable time format to display results, as explained below. Enter times in the correct format You must...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel TIME function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_time.png "Excel TIME function")](https://exceljet.net/functions/time-function)

### [TIME Function](https://exceljet.net/functions/time-function)

The Excel TIME function is a built-in function that allows you to create a time with individual hour, minute, and second components. The TIME function is useful when you want to assemble a proper time inside another formula.

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum race time splits](https://exceljet.net/formulas/sum-race-time-splits)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [TIME Function](https://exceljet.net/functions/time-function)
    
*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Articles

*   [Excel custom number formats](https://exceljet.net/articles/custom-number-formats)
    
*   [Replace ugly IFs with MAX or MIN](https://exceljet.net/articles/replace-ugly-ifs-with-max-or-min)
    

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