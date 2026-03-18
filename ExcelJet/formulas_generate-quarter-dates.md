# Generate quarter dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/generate-quarter-dates

---

[Skip to main content](https://exceljet.net/formulas/generate-quarter-dates#main-content)

[](https://exceljet.net/formulas/generate-quarter-dates#)

*   [Previous](https://exceljet.net/formulas/future-time-intervals)
    
*   [Next](https://exceljet.net/formulas/get-age-from-birthday)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Generate quarter dates
======================

by Dave Bruns · Updated 11 Jul 2024

Related functions 
------------------

[EDATE](https://exceljet.net/functions/edate-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[EOMONTH](https://exceljet.net/functions/eomonth-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8412/download?token=Y1T0-jhd)
 (20.24 KB)

![Excel formula: Generate quarter dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/generate_quarter_dates.png "Excel formula: Generate quarter dates")

Summary
-------

To generate a list of quarter dates, you can use the [EDATE function](https://exceljet.net/functions/edate-function)
 with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
. In the worksheet shown, the formula in D5 is:

    =EDATE(B5,SEQUENCE(12,,0,3))

The result is a list of the next 12 quarter-start dates, beginning on the date in B5, which is January 1, 2024. The quarter-end dates in column E are based on a similar formula explained below.

Generic formula
---------------

    =EDATE(A1,SEQUENCE(n,,0,3))

Explanation 
------------

In this example, the goal is to generate a list of quarter start and quarter end dates. This can be done by combining the SEQUENCE function with the EDATE and EOMONTH functions, as explained below.

### The SEQUENCE function

The [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 generates a list of sequential numbers in an array. For example, the formula below generates a sequence of 5 numbers that begin with 1 and end with 5:

    =SEQUENCE(5) // returns {1;2;3;4;5}

SEQUENCE has optional arguments for the _start_ value and the _step_ value. For example, if we provide zero as the _start_ value, we get an array of 5 numbers that begin with zero and end with 4:

    =SEQUENCE(5,,0) // returns {0;1;2;3;4}

If we provide 3 for the _step_ argument, we get an array of numbers that begin with zero and end with 12:

    =SEQUENCE(5,,0,3) // returns {0;3;6;9;12}

We use this behavior in the formulas below.

> By default, SEQUENCE will generate data in _rows_. To generate data in _columns_, use the optional second argument, _columns_, and leave _rows_ empty. For a brief overview, watch this video: [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
> .

### Quarter start dates

To create a list of quarter start dates, we use the [EDATE function](https://exceljet.net/functions/edate-function)
, which is designed to add months to a given start date. For example, if we use "1-Jan-2024" as the start date, we can create four quarter start dates by providing 0, 3, 6, and 9 to EDATE as the _months_ argument:

    =EDATE("1-Jan-2024",0) // returns 1-Jan-2024
    =EDATE("1-Jan-2024",3) // returns 1-Apr-2024
    =EDATE("1-Jan-2024",6) // returns 1-Jul-2024
    =EDATE("1-Jan-2024",9) // returns 1-Oct-2024

The first formula does not change the date since the number of months is zero. The second formula adds 3 months, the third adds 6 months, and the fourth adds 9 months to the date. In all cases, EDATE returns the first of the month since the start date is also the first. In the worksheet shown, our goal is to generate a list of 12 quarter start dates beginning on January 1, 2024 (in cell B5). We do this by combining the EDATE function with the SEQUENCE function in a formula like this:

    =EDATE(B5,SEQUENCE(12,,0,3))

Working from the inside out, the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 is configured to create a sequence of 12 numbers, starting at zero and incrementing by 3:

    SEQUENCE(12,,0,3)

*   _rows_ - provided as 12 since we want 12 dates at the end
*   _columns_ - empty (defaults to 1)
*   _start_ - given as zero because we want to use begin on the start date
*   _step_ - given as 3 because we want to increment each number by 3

In this configuration, SEQUENCE returns an array of 12 numbers like this:

    {0;3;6;9;12;15;18;21;24;27;30;33}

This array is passed directly to the EDATE function as the _months_ argument.

    =EDATE(B5,{0;3;6;9;12;15;18;21;24;27;30;33})

EDATE then returns 12 dates that begin with 1-Jan-2024 in an array like this:

    {45292;45383;45474;45566;45658;45748;45839;45931;46023;46113;46204;46296}

The array is delivered to cell D5 and spills into the range D5:D16. These are Excel dates in their [raw serial number format](https://exceljet.net/glossary/excel-date)
. Once the range is formatted with the number format "d-mmm-yyyy", the numbers will display the quarter start dates seen in the worksheet:

    {"1-Jan-2024";"1-Apr-2024";"1-Jul-2024";"1-Oct-2024";"1-Jan-2025";"1-Apr-2025";"1-Jul-2025";"1-Oct-2025";"1-Jan-2026";"1-Apr-2026";"1-Jul-2026";"1-Oct-2026"}

### Quarter end dates

To create a list of quarter-end dates, we use the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
. EOMONTH works just like the EDATE function. However, instead of returning a date on the _same day of the month_, EOMONTH returns the _last day of the month_. For example, if we use "1-Jan-2024" as the start date, we can create four quarter-end dates by providing 2, 5, 8, and 11 to EOMONTH as the _months_ argument:

    =EOMONTH("1-Jan-2024",2) // returns 31-Mar-2024
    =EOMONTH("1-Jan-2024",5) // returns 30-Jun-2024
    =EOMONTH("1-Jan-2024",8) // returns 30-Sep-2024
    =EOMONTH("1-Jan-2024",11) // returns 31-Dec-2024

Notice that EOMONTH returns the _last day of the month_ even though the start date is the _first day of the month_. In the worksheet shown, we want to list 12 quarter-end dates based on a start date of January 1, 2024 (in cell B5). We do this with EOMONTH and SEQUENCE like this:

    =EOMONTH(B5,SEQUENCE(12,,2,3))

This formula is very similar to the EDATE + SEQUENCE formula we used to create quarter start dates above. The difference is that (1) we use the EOMONTH function instead of EDATE, and (2) we configure SEQUENCE in a slightly different way, starting the sequence at 2 instead of zero:

    SEQUENCE(12,,2,3)

*   _rows_ - given as 12 because we want 12 dates
*   _columns_ - empty (defaults to 1)
*   _start_ - given as 2 to add 2 months to the start date
*   _step_ - given as 3 because we want to increment each date by 3 months

In this configuration, SEQUENCE returns an array of 12 numbers like this:

    {2;5;8;11;14;17;20;23;26;29;32;35}

This array is returned directly to the EOMONTH function as the _months_ argument:

    =EOMONTH(B5,{2;5;8;11;14;17;20;23;26;29;32;35})

EOMONTH then returns 12 dates that begin with 31-Mar-2024 in an array like this:

    {45382;45473;45565;45657;45747;45838;45930;46022;46112;46203;46295;46387}

The array is delivered to cell E5 and spills into the range E5:E16. When the number format "d-mmm-yyyy" is applied, the numbers will display the quarter-end dates seen in the worksheet:

    {"31-Mar-2024";"30-Jun-2024";"30-Sep-2024";"31-Dec-2024";"31-Mar-2025";"30-Jun-2025";"30-Sep-2025";"31-Dec-2025";"31-Mar-2026";"30-Jun-2026";"30-Sep-2026";"31-Dec-2026"}

In the worksheet, the formula looks like this:

![Listing quarter end dates with the  EOMONTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/generate_quarter_end_dates.png "Listing quarter end dates with the  EOMONTH function")

You might wonder if we can use the existing quarter start dates directly. Yes. Since we already have a list of quarter start dates in column D, another option is to use the EOMONTH function directly with the [spill range](https://exceljet.net/glossary/spill-range)
 like this:

    =EOMONTH(+D5#,2)

This formula simply shifts each quarter's start date forward 2 months and returns the last day of that month. The result is exactly the same.

_The plus sign (+) is needed before the spill range in this case. Without it, the formula will return a #VALUE! error. Some older functions, like EOMONTH, "resist" spilling when provided with a range. For example, EOMONTH(A1:A5,1) will return #VALUE even with valid dates in A1:A5. This limitation comes from certain functions expecting a single value instead of a range. The #VALUE! error is essentially reporting the range as an unexpected value. However, adding an operator in front of the reference will often fix the problem because it forces Excel to evaluate the expression first before the function runs. For an overview, see [Dynamic Array Formulas in Excel](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

### Formula abbreviations

The quarter abbreviations seen in column F are generated with a formula like this in cell F5:

    ="Q"&MOD(SEQUENCE(12,,0),4)+1

At the core, this is a [formula that repeats numeric sequences](https://exceljet.net/formulas/repeat-sequence-of-numbers)
 using the SEQUENCE function and the [MOD function](https://exceljet.net/functions/mod-function)
. We then concatenate a "Q" to the output. You can see the formula and result below:

![Formula to generate quarter abbreviations](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/generate_quarter_abbreviations.png "Formula to generate quarter abbreviations")

Related formulas
----------------

[![Excel formula: Repeat sequence of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/repeat_sequence_of_numbers.png "Excel formula: Repeat sequence of numbers")](https://exceljet.net/formulas/repeat-sequence-of-numbers)

### [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)

In this example, the goal is to repeat a sequence of numbers. This is a useful way to create repeating sequences of numbers by itself. In addition, this formula is a building block to the more general formula here , which can repeat ranges and arbitrary values that are not sequential numbers...

[![Excel formula: Get quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20quarter%20from%20date.png "Excel formula: Get quarter from date")](https://exceljet.net/formulas/get-quarter-from-date)

### [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)

In this example, the goal is to return a number that represents quarter (i.e. 1,2,3,4) for any given date. In other words, we want to return the quarter that the date resides in. ROUNDUP formula solution In the example shown, the formula in cell C5 is: =ROUNDUP(MONTH(B5)/3,0) The ROUNDUP function...

[![Excel formula: Get fiscal quarter from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20quarter%20from%20date.png "Excel formula: Get fiscal quarter from date")](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

### [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)

The choose function uses the first argument to "select" remaining elements. For example, in a scheme where 1 = small, 2 = medium, and 3 = large, this formula will "map" the number 2 to "medium". =CHOOSE(2,"small","medium","large") In the case of fiscal quarters, we can use this same idea to map any...

[![Excel formula: Sum by quarter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20by%20quarter.png "Excel formula: Sum by quarter")](https://exceljet.net/formulas/sum-by-quarter)

### [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)

In this example, the goal is to sum the amounts in column C by quarter in column G. Column D is a helper column , and the formula to calculate quarters from the dates in column B is explained below. All data is in an Excel Table named data in the range B5:E16. This problem can be solved with the...

Related functions
-----------------

[![Excel EDATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_edate_function.png "Excel EDATE function")](https://exceljet.net/functions/edate-function)

### [EDATE Function](https://exceljet.net/functions/edate-function)

The Excel EDATE function adds and subtracts complete months from a given date. You can use EDATE to calculate expiration dates, maturity dates, and other due dates derived from a start date.

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel EOMONTH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_eomonth_function.png "Excel EOMONTH function")](https://exceljet.net/functions/eomonth-function)

### [EOMONTH Function](https://exceljet.net/functions/eomonth-function)

The Excel EOMONTH function returns the last day of the month, n months in the past or future. You can use EOMONTH to calculate expiration dates, due dates, and other dates that need to land on the last day of a month. Use a positive value for months to move forward in time, and a negative number...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Repeat sequence of numbers](https://exceljet.net/formulas/repeat-sequence-of-numbers)
    
*   [Get quarter from date](https://exceljet.net/formulas/get-quarter-from-date)
    
*   [Get fiscal quarter from date](https://exceljet.net/formulas/get-fiscal-quarter-from-date)
    
*   [Sum by quarter](https://exceljet.net/formulas/sum-by-quarter)
    

### Functions

*   [EDATE Function](https://exceljet.net/functions/edate-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [EOMONTH Function](https://exceljet.net/functions/eomonth-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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