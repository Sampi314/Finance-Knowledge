# List upcoming birthdays - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-upcoming-birthdays

---

[Skip to main content](https://exceljet.net/formulas/list-upcoming-birthdays#main-content)

[](https://exceljet.net/formulas/list-upcoming-birthdays#)

*   [Previous](https://exceljet.net/formulas/lambda-strip-trailing-characters-recursive)
    
*   [Next](https://exceljet.net/formulas/map-with-and-and-or-logic)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

List upcoming birthdays
=======================

by Dave Bruns · Updated 25 Sep 2022

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[LET](https://exceljet.net/functions/let-function)

[TEXT](https://exceljet.net/functions/text-function)

[INDEX](https://exceljet.net/functions/index-function)

[SEQUENCE](https://exceljet.net/functions/sequence-function)

[XMATCH](https://exceljet.net/functions/xmatch-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6956/download?token=c06qvcma)
 (16.39 KB)

![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")

Summary
-------

To list the next n upcoming birthdays from a larger table of names and birthdays, you can use a formula based on the [INDEX](https://exceljet.net/functions/index-function)
, [XMATCH](https://exceljet.net/functions/xmatch-function)
, and [SORTBY](https://exceljet.net/videos/basic-sortby-function-example)
 functions, with help from [TODAY](https://exceljet.net/functions/today-function)
, [TEXT](https://exceljet.net/functions/text-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, and [LET](https://exceljet.net/functions/let-function)
. In the example shown, the formula in E5 is:

    =LET(
      n,7,
      tday,TODAY(),
      calendar,TEXT(SEQUENCE(EDATE(tday,12)-tday,1,tday),"mmdd"),
      birthdays,TEXT(data[Birthday],"mmdd"),
      sorted,SORTBY(data,XMATCH(birthdays,calendar)),
      INDEX(
        sorted,
        SEQUENCE(MIN(n,ROWS(data))),
        SEQUENCE(1,COLUMNS(data))
      )
    )
    

where **data** (B5:C29) is an [Excel Table](https://exceljet.net/glossary/excel-table)
. This formula returns the next 7 upcoming birthdays in the data based on the current date, which is November 17, 2021 in the example shown.

Note: This formula displays _upcoming birthdays_. To sort and display _all birthdays_, see [this formula](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
.

Explanation 
------------

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an [Excel Table](https://exceljet.net/glossary/excel-table)
 named **data** in the range B5:C29. In the example shown, we are using 7 for _n_, so the result will be the next 7 upcoming birthdays, but this number can be changed as desired. The formula in E5 is:

    =LET(
      n,7,
      tday,TODAY(),
      calendar,TEXT(SEQUENCE(EDATE(tday,12)-tday,1,tday),"mmdd"),
      birthdays,TEXT(data[Birthday],"mmdd"),
      sorted,SORTBY(data,XMATCH(birthdays,calendar)),
      INDEX(
        sorted,
        SEQUENCE(MIN(n,ROWS(data))),
        SEQUENCE(1,COLUMNS(data))
      )
    )
    

The main challenge with a problem like this is to sort the list of birthdays into a rolling list of upcoming dates. This formula works in two parts: (1) sort all birthdays according to a rolling calendar and (2) return the first 7 birthdays from the sorted list.

### Setup

To make this formula easier to read and more efficient, we are using the [LET function](https://exceljet.net/functions/let-function)
 to define variables that we need later in the calculation. We start off by defining _n_ and _tday_:

    =LET(
      n,7,
      tday,TODAY(),
    

Although _n_ is used just once in the formula that follows, defining it here makes it easier to edit later. The _tday_ variable is defined with the [TODAY function](https://exceljet.net/functions/today-function)
, which returns the current date. The current date is used three times in the formula, so it makes sense to define the value as a variable.

### Sorting the birthdays

For this formula to work, we need to sort the birthdays in an "upcoming order" based on the current date. There are two challenges that we need to overcome to sort the birthdays like this. First, the birthdates include a birth year, so if we try to sort these dates ([which are just numbers underneath](https://exceljet.net/glossary/excel-date)
) as-is, the result will be birthdays sorted first by year, then by month and year, which won't work. The second challenge is that we need to sort the birthdays according to a rolling calendar year that always begins with the current date. The solution is to create a special sorting index based on day and month only, that begins on the current date.

### Rolling calendar

To make a rolling calendar, we use the following snippet to define _calendar_:

    calendar,TEXT(SEQUENCE(EDATE(tday,12)-tday,1,tday),"mmdd"),
    

Here we create a list of all dates in the next year with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
:

    SEQUENCE(EDATE(tday,12)-tday,1,tday) // next 365 days
    

Working from the inside out, we use the [EDATE function](https://exceljet.net/functions/edate-function)
 to get a count:

    EDATE(tday,12)-tday // count days
    

Starting with the current date, EDATE returns a date 12 months (1 year) in the future. From this date, the current date is subtracted. The result is a count of days between the current date and the same date next year. This is done to catch the 366 days that might occur in a leap year that includes February 29. In the example shown, the current year is 2021, and the following year is 2022, so the result is 365. This number is returned as the _rows_ argument to SEQUENCE:

    SEQUENCE(365,1,tday)
    

SEQUENCE then builds an [array](https://exceljet.net/glossary/array)
 of 365 dates, beginning with _tday_ (the current date). The resulting [array](https://exceljet.net/glossary/array)
 is handed off to the [TEXT function](https://exceljet.net/functions/text-function)
:

    TEXT(SEQUENCE(EDATE(tday,12)-tday,1,tday),"mmdd")
    

Inside TEXT, _value_ is the array returned by SEQUENCE, and _format\_text_ is provided as "mmdd". The result is an array of text values in the form "mmdd". So, for instance, the date November 2, 2021 becomes "1102". Notice the year value is simply discarded. Inside the [LET function](https://exceljet.net/functions/let-function)
, the result from TEXT is assigned to the variable _calendar_.

### Birthdays

At this point, we have a rolling calendar, _calendar_, but the birthdays in the Excel table still include a birth year. To sort the birthdays according to the calendar we created above, we need to process them with the TEXT function in the same way we created the rolling calendar above:

    birthdays,TEXT(data[Birthday],"mmdd"),
    

The TEXT returns an array of text values in the same format as _calendar_, and this result is assigned to the variable _birthdays_.

### Sorting the birthdays

At this point, we have what we need to sort the list of birthdays. The trick is we need to sort the birthdays by the order they will occur in the next year. To do this, we use the [SORTBY function](https://exceljet.net/functions/sortby-function)
 together with the [XMATCH function](https://exceljet.net/functions/xmatch-function)
:

    sorted,SORTBY(data,XMATCH(birthdays,calendar)),
    

The entire table (**data**) is given to SORTBY as _array_. The _by\_array1_ argument is generated with the XMATCH function like this:

    XMATCH(birthdays,calendar) // get position of birthdays in calendar
    

XMATCH is used to get the _position_ of each birthday inside the rolling calendar. XMATCH performs an exact match by default, so no other arguments are required. We want an exact match in this case because _calendar_ is not sorted in ascending or descending order, but rather in the order the dates occur in the next year.

The result from XMATCH is an _array of positions._ Each number in this array is the position at which a birthday will occur in the rolling calendar. This result is provided to SORTBY as _by\_array1_, which uses these positions to sort the birthday table in the same order as calendar. The result from SORTBY is assigned to the variable _sorted_.

### Next n birthdays

At this point, we have a list of upcoming birthdays sorted in the order that they will occur over the next year, defined as _sorted_. The last step is to slice off just the first 7 entries. For this, we use the [INDEX function](https://exceljet.net/functions/index-function)
:

      INDEX(
        sorted,
        SEQUENCE(MIN(n,ROWS(data))),
        SEQUENCE(1,COLUMNS(data))
    

For _array_, we give INDEX _sorted_, which is the entire list of sorted birthdays. For _row\_num_ and _col\_num_, we use the [SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
 to create the arrays we need. For _row\_num_, we generate an array with 7 rows, or the count of all birthdays in the table, whichever is smaller:

    SEQUENCE(MIN(n,ROWS(data))) // returns {1;2;3;4;5;6;7}
    

Notice the actual number given to SEQUENCE is either 7 or the count of all birthdays in **data**, whichever is smaller. This prevents errors from appearing in the final output when _n_ is larger than the total birthdays available in the table. This little trick is handled by the [MIN function](https://exceljet.net/functions/min-function)
, which is a nice alternative to the [IF function](https://exceljet.net/functions/if-function)
 in a situation like this:

    MIN(n,ROWS(data)) // smaller of 7 or birthday count
    

For _col\_num_, we create a two column array, since there are two columns in the source data:

    SEQUENCE(1,COLUMNS(data)) // returns {1,2}
    

The final result from INDEX is the first 7 rows from the sorted birthdays. The birthdays in column F have the [custom number format](https://exceljet.net/articles/custom-number-formats)
 "mmm d" applied, to show only the month name and day.

Related formulas
----------------

[![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

### [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people...

[![Excel formula: Basic filter example](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/basic%20filter%20example.png "Excel formula: Basic filter example")](https://exceljet.net/formulas/basic-filter-example)

### [Basic filter example](https://exceljet.net/formulas/basic-filter-example)

In this example the goal is to return rows in the range B5:E15 that have a specific state value in column E. To make the example dynamic, the state is a variable entered in cell H4. When the state in H4 is changed, the formula should return a new set of records. This is a perfect application for...

[![Excel formula: FILTER on first or last n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/FILTER%20on%20first%20or%20last%20n%20values.png "Excel formula: FILTER on first or last n values")](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

### [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)

In this example, the goal is to extract the first 3 values or the last 3 values from the named range data (B5:B15). We also want to exclude any empty cells from our results. In the worksheet shown the formula in cell D5 is: =INDEX(FILTER(data,data<>""),SEQUENCE(3,1,1,1)) Working from the...

[![Excel formula: Sort by custom list](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20custom%20list.png "Excel formula: Sort by custom list")](https://exceljet.net/formulas/sort-by-custom-list)

### [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)

In this example, we are sorting a table with 10 rows and 3 columns. In the range J5:J7 (the named range custom ), the colors "red", "blue", and "green" are listed in the desired sort order. The goal is to sort the table using values in the Group column in this same custom order. The SORTBY function...

[![Excel formula: Zodiac sign lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/zodiac%20sign%20lookup_0.png "Excel formula: Zodiac sign lookup")](https://exceljet.net/formulas/zodiac-sign-lookup)

### [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)

The goal of this example is to look up the correct astrological or zodiac sign for a given birthdate, using the table shown in B5:F15. These are based on the Western zodiac signs described here . Zodiac signs are used in horoscopes, which are a kind of forecast of a person's future, based on the...

Related functions
-----------------

[![Excel SORTBY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sortby_function.png "Excel SORTBY function")](https://exceljet.net/functions/sortby-function)

### [SORTBY Function](https://exceljet.net/functions/sortby-function)

The Excel SORTBY function sorts the contents of a range or array based on the values from another range or array. The range or array used to sort does not need to be in the source data or in the output.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel SEQUENCE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sequence_function.png "Excel SEQUENCE function")](https://exceljet.net/functions/sequence-function)

### [SEQUENCE Function](https://exceljet.net/functions/sequence-function)

The Excel SEQUENCE function generates a list of sequential numbers in an array. The array can be one dimensional, or two-dimensional, determined by _rows_ and _columns_ arguments. ...

[![Excel XMATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_xmatch_function.png "Excel XMATCH function")](https://exceljet.net/functions/xmatch-function)

### [XMATCH Function](https://exceljet.net/functions/xmatch-function)

The Excel XMATCH function performs a lookup and returns a _position_ of a value in a range. It is a more robust and flexible successor to the MATCH function. XMATCH supports approximate and exact matching, reverse search, and wildcards (\* ?) for partial matches. ...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/The%20SEQUENCE%20function-Play.png)](https://exceljet.net/videos/the-sequence-function)

### [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)

In this video, we'll introduce the SEQUENCE function. One of the new functions that comes with the dynamic array version of Excel is SEQUENCE. The SEQUENCE function lets you generate numeric sequences, which can be used for dates, times, and more. The SEQUENCE function takes four arguments . The...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Basic%20SORTBY%20function%20example-play.png)](https://exceljet.net/videos/basic-sortby-function-example)

### [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)

In this video, we’ll look at a basic example of sorting with the SORTBY function . In this worksheet, we have a list of names, scores, and groups. Currently, the data is not sorted. Our goal is to sort this data by group, then by score in descending order. I’ll start off by placing the cursor in...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
    
*   [Basic filter example](https://exceljet.net/formulas/basic-filter-example)
    
*   [FILTER on first or last n values](https://exceljet.net/formulas/filter-on-first-or-last-n-values)
    
*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    
*   [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [SEQUENCE Function](https://exceljet.net/functions/sequence-function)
    
*   [XMATCH Function](https://exceljet.net/functions/xmatch-function)
    

### Videos

*   [The SEQUENCE function](https://exceljet.net/videos/the-sequence-function)
    
*   [Basic SORTBY function example](https://exceljet.net/videos/basic-sortby-function-example)
    

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