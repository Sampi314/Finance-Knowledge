# Get work hours between dates custom schedule - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule

---

[Skip to main content](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule#main-content)

[](https://exceljet.net/formulas/get-work-hours-between-dates-custom-schedule#)

*   [Previous](https://exceljet.net/formulas/get-work-hours-between-dates-and-times)
    
*   [Next](https://exceljet.net/formulas/get-workdays-between-dates)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get work hours between dates custom schedule
============================================

by Dave Bruns · Updated 1 Oct 2018

Related functions 
------------------

[MID](https://exceljet.net/functions/mid-function)

[ROW](https://exceljet.net/functions/row-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

[WEEKDAY](https://exceljet.net/functions/weekday-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Get work hours between dates custom schedule](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20work%20hours%20between%20dates%20custom2.png "Excel formula: Get work hours between dates custom schedule")

Summary
-------

To calculate work hours between two dates with a custom schedule, you can use a formula based on the WEEKDAY and SUMPRODUCT functions, with help from ROW, INDIRECT, and MID. In the example shown, the formula in F8 is:

    =SUMPRODUCT(MID(D6,WEEKDAY(ROW(INDIRECT(B6&":"&C6))),1)*ISNA(MATCH(ROW(INDIRECT(B6&":"&C6)),holidays,0)))
    

Which returns 36 hours, based on a custom schedule where 8 hours are worked Mon-Fri, 4 hours are worked on Saturday, and Monday September 3 is a holiday. Holidays are supplied as the [named range](https://exceljet.net/glossary/named-range)
 G6:G8. The work schedule is entered as a text string in column D and can be changed as desired.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
 that must be entered with Control + Shift + Enter. If you have a standard 8 hour workday, [this formula](https://exceljet.net/formulas/get-work-hours-between-dates)
 is simpler._

Generic formula
---------------

    =SUMPRODUCT(MID(schedule,WEEKDAY(ROW(INDIRECT(start&":"&end))),1)*ISNA(MATCH(ROW(INDIRECT(start&":"&end)),holidays,0)))

Explanation 
------------

At the core, this formula uses the WEEKDAY function to figure out the day of week (i.e. Monday, Tuesday, etc.) for every day between the two given dates. WEEKDAY returns a number between 1 and 7. With default settings, Sunday=1 and Saturday = 7.

The trick to this formula is assembling an array of dates that you can feed into the WEEKDAY function. This is done with ROW with INDIRECT:

    ROW(INDIRECT(B6&":"&C6))
    

ROW interprets the concatenated dates as row numbers and returns an array like this:

    {43346;43347;43348;43349;43350;43351;43352}
    

Each number in the array represents a date. The WEEKDAY function then evaluates the array and returns an array of weekday values:

    {2;3;4;5;6;7;1}
    

These numbers correspond to the day of week of each date. They are provided to the MID function as the start number argument, along with the value in D6, "0888884" for text:

    MID("0888884",{2;3;4;5;6;7;1},1)
    

Because we are giving MID an array of start numbers, it returns an array of results like this:

    {"8";"8";"8";"8";"8";"4";"0"}
    

These values correspond to the hours worked on each day from the start date to the end date. Note the values in this array are text, not numbers. To convert to actual numbers, we multiply by a second array created to manage holidays, as explained below. The math operation coerces the text to numeric values.

### Holidays

To handle holidays, we use ISNA, MATCH, and the [named range](https://exceljet.net/glossary/named-range)
 "holidays" like this:

    ISNA(MATCH(ROW(INDIRECT(B6&":"&C6)),holidays,0))
    

This expression uses MATCH to locate dates that are in the named range holidays using the same array of dates generated above with INDIRECT and ROW. MATCH returns a number when holidays are found and the #N/A error when not. The ISNA function "flips" the results so that TRUE represents holidays and FALSE represents non-holidays. ISNA returns an array or results like this:

    {FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE}
    

Finally, both arrays are multiplied by each other inside SUMPRODUCT. The math operation coerces TRUE and FALSE to 1 and zero, and the text values in the first array to numeric values (as explained above), so in the end we have:

    =SUMPRODUCT({8;8;8;8;8;4;0}*{0;1;1;1;1;1;1})
    

After multiplication, we have a single array inside SUMPRODUCT containing all working hours in the date range:

    =SUMPRODUCT({0;8;8;8;8;4;0})
    

SUMPRODUCT then sums all items in the array and returns a result of 36.

Related formulas
----------------

[![Excel formula: Get work hours between dates](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get%20work%20hours%20between%20dates2.png "Excel formula: Get work hours between dates")](https://exceljet.net/formulas/get-work-hours-between-dates)

### [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)

This formula uses the NETWORKDAYS function calculate total working days between two dates, taking into account weekends and (optionally) holidays. Holidays, if provided, must be a range of valid Excel dates. Once total work days are known, they are simply multiplied by a fixed number of hours per...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

Related functions
-----------------

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

[![Excel WEEKDAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20weekday%20function.png "Excel WEEKDAY function")](https://exceljet.net/functions/weekday-function)

### [WEEKDAY Function](https://exceljet.net/functions/weekday-function)

The Excel WEEKDAY function takes a date and returns a number between 1-7 representing the day of week. By default, WEEKDAY returns 1 for Sunday and 7 for Saturday, but this is configurable. You can use the WEEKDAY function inside other formulas to check the day of week.

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

*   [Get work hours between dates](https://exceljet.net/formulas/get-work-hours-between-dates)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    

### Functions

*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    
*   [WEEKDAY Function](https://exceljet.net/functions/weekday-function)
    
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