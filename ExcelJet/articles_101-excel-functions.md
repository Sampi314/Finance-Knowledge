# 101 Excel Functions you should know | Exceljet

**Source:** https://exceljet.net/articles/101-excel-functions

---

[Skip to main content](https://exceljet.net/articles/101-excel-functions#main-content)

[](https://exceljet.net/articles/101-excel-functions#)

*   [Previous](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
    
*   [Next](https://exceljet.net/articles/how-to-use-formula-criteria)
    

101 Excel Functions you should know
===================================

by Dave Bruns · Updated 27 Sep 2024

![101 Excel Functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Excel_functions_you_should_know.jpeg)

Summary
-------

Excel contains over 500 functions, with more functions added every year. That is a huge number, so where should you start? This guide provides a walkthrough of over 100 important functions in Excel with many examples and links. Click function names for details and more examples.

Below is a brief overview of about 100 important Excel functions you should know, with links to detailed examples. We also have a [large list of example formulas](https://exceljet.net/formulas)
, a [more complete list of Excel functions](https://exceljet.net/functions)
, and [video training](https://exceljet.net/training)
. If you are new to Excel formulas, [see this introduction](https://exceljet.net/articles/excel-formulas-and-functions)
.

Note: Excel now includes [Dynamic Array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, and [almost 50 new functions](https://exceljet.net/new-excel-functions)
.

> Download: [101 Excel Functions PDF](https://exceljet.net/resources/101-excel-functions-pdf)

Date and Time Functions
-----------------------

Excel provides many functions to work with [dates](https://exceljet.net/glossary/excel-date)
 and [times](https://exceljet.net/glossary/excel-time)
. 

### NOW and TODAY

You can get the current date with the [TODAY function](https://exceljet.net/functions/today-function)
 and the current date and time with the [NOW Function](https://exceljet.net/functions/now-function)
. Technically, the NOW function returns the current date and time, but you can format as time only, as seen below:

![NOW and TODAY functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/now%20and%20today%20functions_0.png?itok=19Fo41NF "NOW and TODAY functions")

    TODAY() // returns current date
    NOW() // returns current time

Copy

Note: these are [volatile functions](https://exceljet.net/glossary/volatile-function)
 and will recalculate with every worksheet change. If you want a static value, use [date](https://exceljet.net/shortcuts/insert-current-date)
 and [time](https://exceljet.net/shortcuts/insert-current-time)
 shortcuts.

### DAY, MONTH, YEAR, and DATE

You can use the [DAY,](https://exceljet.net/functions/day-function)
 [MONTH](https://exceljet.net/functions/month-function)
, and [YEAR](https://exceljet.net/functions/year-function)
 functions to disassemble any date into its raw components, and the [DATE function](https://exceljet.net/functions/date-function)
 to put things back together again.

![Functions to disassemble and reassemble dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/year%20month%20day%20date%20functions.png?itok=TGdU4dTw "Functions to disassemble and reassemble dates")

    =DAY("14-Nov-2018") // returns 14
    =MONTH("14-Nov-2018") // returns 11
    =YEAR("14-Nov-2018") // returns 2018
    =DATE(2018,11,14) // returns 14-Nov-2018

Copy

### HOUR, MINUTE, SECOND, and TIME

Excel provides a set of parallel functions for times. You can use the [HOUR](https://exceljet.net/functions/hour-function)
, [MINUTE](https://exceljet.net/functions/minute-function)
, and [SECOND](https://exceljet.net/functions/second-function)
 functions to extract pieces of a time, and you can assemble a TIME from individual components with the [TIME function](https://exceljet.net/functions/time-function)
.

![Time function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/hour%20minute%20second%20time%20functions.png?itok=xGkoF6mi "Time function examples")

    =HOUR("10:30") // returns 10
    =MINUTE("10:30") // returns 30
    =SECOND("10:30") // returns 0
    =TIME(10,30,0) // returns 10:30

Copy

### DATEDIF and YEARFRAC

You can use the [DATEDIF function](https://exceljet.net/functions/datedif-function)
 to get time between dates in years, months, or days. DATEDIF can also be configured to get total time in "normalized" denominations, i.e. "2 years and 6 months and 27 days".

![DATEDIF function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/datedif%20function.png?itok=qlnkxZ02 "DATEDIF function example")

Use [YEARFRAC](https://exceljet.net/functions/yearfrac-function)
 to get fractional years:

![YEARFRAC function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/yearfrac%20function.png?itok=EVANX8nt "YEARFRAC function example")

    =YEARFRAC("14-Nov-2018","10-Jun-2021") // returns 2.57

Copy

### EDATE and EOMONTH

A common task with dates is to shift a date forward (or backward) by a given number of months. You can use the [EDATE](https://exceljet.net/functions/edate-function)
 and [EOMONTH functions](https://exceljet.net/functions/eomonth-function)
 for this. EDATE moves by month and retains the day. EOMONTH works the same way, but always returns the last day of the month.

![EDATE and EOMONTH function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/edate%20and%20eomonth%20functions.png?itok=-ePKm1E1 "EDATE and EOMONTH function examples")

    EDATE(date,6) // 6 months forward
    EOMONTH(date,6) // 6 months forward (end of month)

Copy

### WORKDAY and NETWORKDAYS

To figure out a date **n** working days in the future, you can use the [WORKDAY function](https://exceljet.net/functions/workday-function)
. To calculate the number of workdays between two dates, you can use [NETWORKDAYS](https://exceljet.net/functions/networkdays-function)
.

![WORKDAY function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/workday%20function.png?itok=P3AdQhG_ "WORKDAY function example")

    WORKDAY(start,n,holidays) // date n workdays in future

Copy

Video: [How to calculate due dates with WORKDAY](https://exceljet.net/videos/how-to-calculate-due-dates-with-workday)

![NETWORKDAYS function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/networkdays%20function_0.png?itok=H9O-LuZ8 "NETWORKDAYS function example")

    NETWORKDAYS(start,end,holidays) // number of workdays between dates

Copy

Note: Both functions automatically skip weekends (Saturday and Sunday) and will also skip holidays, if provided. If you need more flexibility on what days are considered weekends, see the [WORKDAY.INTL function](https://exceljet.net/functions/workday.intl-function)
 and [NETWORKDAYS.INTL function](https://exceljet.net/functions/networkdays.intl-function)
. 

### WEEKDAY and WEEKNUM

To figure out the day of week from a date, Excel provides the [WEEKDAY function](https://exceljet.net/functions/weekday-function)
. WEEKDAY returns a number between 1-7 that indicates Sunday, Monday, Tuesday, etc. Use the [WEEKNUM function](https://exceljet.net/functions/weeknum-function)
 to get the week number in a given year.

![WEEKDAY and WEEKNUM function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/weekday%20and%20weeknum%20functions.png?itok=06fepsWl "WEEKDAY and WEEKNUM function examples")

    =WEEKDAY(date) // returns a number 1-7
    =WEEKNUM(date) // returns week number in year

Copy

Engineering
-----------

### CONVERT

Most Engineering functions are pretty technical...you'll find a lot of functions for complex numbers in this section. However, the [CONVERT function](https://exceljet.net/functions/convert-function)
 is quite useful for everyday unit conversions. You can use CONVERT to change units for distance, weight, temperature, and much more.

![CONVERT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/convert%20function.png?itok=7wX1E13v "CONVERT function example")

    =CONVERT(72,"F","C") // returns 22.2

Copy

Information Functions
---------------------

### ISBLANK, ISERROR, ISNUMBER, and ISFORMULA

Excel provides many functions for checking the value in a cell, including [ISNUMBER](https://exceljet.net/functions/isnumber-function)
,  [ISTEXT](https://exceljet.net/functions/istext-function)
, [ISLOGICAL](https://exceljet.net/functions/islogical-function)
, [ISBLANK](https://exceljet.net/functions/isblank-function)
, [ISERROR](https://exceljet.net/functions/iserror-function)
, and [ISFORMULA](https://exceljet.net/functions/isformula-function)
  These functions are sometimes called the "IS" functions, and they all return TRUE or FALSE based on a cell's contents.

![ISNUMBER ISTEXT ISLOGICAL ISBLANK ISERROR ISFORMULA](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/the%20is%20functions.png?itok=qZp3yfsz "ISNUMBER ISTEXT ISLOGICAL ISBLANK ISERROR ISFORMULA")

Excel also has [ISODD](https://exceljet.net/functions/isodd-function)
 and [ISEVEN](https://exceljet.net/functions/iseven-function)
 functions that will test a number to see if it's even or odd.

By the way, the green fill in the screenshot above is applied automatically with a [conditional formatting](https://exceljet.net/conditional-formatting-formulas)
 formula.

Logical Functions
-----------------

Excel's logical functions are a key building block of many advanced formulas. Logical functions return the boolean values TRUE or FALSE. If you need a primer on logical formulas, t[his video goes through many examples](https://exceljet.net/plc/how-to-build-logical-formulas)
.

### AND, OR and NOT

The core of Excel's logical functions are the [AND function](https://exceljet.net/functions/and-function)
, the [OR function](https://exceljet.net/functions/or-function)
, and the [NOT function](https://exceljet.net/functions/not-function)
. In the screen below, each of these function is used to run a simple test on the values in column B:

![AND, OR, and NOT functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/and%20or%20not%20functions.png?itok=2n5IPo_t "AND, OR, and NOT functions")

    =AND(B5>3,B5<9)
    =OR(B5=3,B5=9)
    =NOT(B5=2)

Copy

*   Video: [How to build logical formulas](https://exceljet.net/plc/how-to-build-logical-formulas)
    
*   Guide: [50 examples of formula criteria](https://exceljet.net/articles/how-to-use-formula-criteria)
    

### IFERROR and IFNA

The [IFERROR function](https://exceljet.net/functions/iferror-function)
 and [IFNA function](https://exceljet.net/functions/ifna-function)
 can be used as a simple way to trap and handle errors. In the screen below, [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 is used to retrieve cost from a menu item. Column F contains just a [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
, with no error handling. Column G shows how to use IFNA with VLOOKUP to display a custom message when an unrecognized item is entered.

![IFNA function with VLOOKUP example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/ifna%20function.png?itok=PO_60nqf "IFNA function with VLOOKUP example")

    =VLOOKUP(E5,menu,2,0) // no error trapping
    =IFNA(VLOOKUP(E5,menu,2,0),"Not found") // catch errors

Copy

Whereas IFNA only catches an #N/A error, the [IFERROR function](https://exceljet.net/functions/iferror-function)
 will catch any formula error.

### IF and IFS functions

The [IF function](https://exceljet.net/functions/if-function)
 is one of the most used functions in Excel. In the screen below, IF checks test scores and assigns "pass" or "fail":

![IF function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/if%20function.png?itok=e6Y1FgPW "IF function example")

Multiple IF functions [can be nested together](https://exceljet.net/articles/nested-ifs)
 to perform more complex logical tests.

New in Excel 2019 and [Excel 365](https://exceljet.net/glossary/excel-365)
, the [IFS function](https://exceljet.net/functions/ifs-function)
 can run multiple logical tests without [nesting IFs](https://exceljet.net/articles/nested-ifs)
.

![IFS function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/ifs%20function.png?itok=YxWWUElk "IFS function example")

    =IFS(C5<60,"F",C5<70,"D",C5<80,"C",C5<90,"B",C5>=90,"A")

Copy

Lookup and Reference Functions
------------------------------

### VLOOKUP and HLOOKUP

Excel offers a number of functions to lookup and retrieve data. Most famous of all is [VLOOKUP](https://exceljet.net/functions/vlookup-function)
:

![VLOOKUP function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/vlookup%20function.png?itok=iG_X6u9f "VLOOKUP function example")

    =VLOOKUP(C5,$F$5:$G$7,2,TRUE)

Copy

More: [23 things to know about VLOOKUP](https://exceljet.net/articles/things-you-should-know-about-vlookup)
.

[HLOOKUP](https://exceljet.net/functions/hlookup-function)
 works like [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, but expects data arranged horizontally:

![HLOOKUP function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/hlookup%20function_0.png?itok=JmCxQBJi "HLOOKUP function example")

    =HLOOKUP(C5,$G$4:$I$5,2,TRUE)

Copy

### INDEX and MATCH

For more complicated lookups, [INDEX](https://exceljet.net/functions/index-function)
 and [MATCH](https://exceljet.net/functions/match-function)
 offers more flexibility and power:

![INDEX and MATCH function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/index%20and%20match.png?itok=gWsVJ1i7 "INDEX and MATCH function example")

    =INDEX(C5:E12,MATCH(H4,B5:B12,0),MATCH(H5,C4:E4,0))

Copy

Both the I[NDEX function](https://exceljet.net/functions/index-function)
 and the [MATCH function](https://exceljet.net/functions/match-function)
 are powerhouse functions that turn up in all kinds of formulas.

More: [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)

### LOOKUP

The [LOOKUP function](https://exceljet.net/functions/lookup-function)
 has default behaviors that make it useful when solving certain problems. LOOKUP assumes values are sorted in ascending order and always performs an approximate match. When LOOKUP can't find a match, it will match the next smallest value. In the example below we are using LOOKUP to find the last entry in a column:

![LOOKUP function example - last non-empty cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/lookup%20function.png?itok=Jb4u8d3G "LOOKUP function example - last non-empty cell")

### ROW and COLUMN

You can use the [ROW function](https://exceljet.net/functions/row-function)
 and [COLUMN function](https://exceljet.net/functions/column-function)
 to find row and column numbers on a worksheet. Notice both ROW and COLUMN return values for the _current cell_ if no reference is supplied:

![ROW and COLUMN function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/row%20and%20column%20functions.png?itok=0gy2izre "ROW and COLUMN function example")

The row function also shows up often in advanced formulas that process data with [relative row numbers](https://exceljet.net/formulas/get-relative-row-numbers-in-range)
.

### ROWS and COLUMNS

The [ROWS function](https://exceljet.net/functions/rows-function)
 and [COLUMNS function](https://exceljet.net/functions/columns-function)
 provide a count of rows in a reference. In the screen below, we are counting rows and columns in an [Excel Table](https://exceljet.net/things-to-know-about-excel-tables)
 named "Table1".

![ROWS and COLUMNS function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rows%20and%20columns%20functions.png?itok=i_2X9T7d "ROWS and COLUMNS function example")

Note ROWS returns a count of data rows in a table, excluding the header row. By the way, here are [23 things to know about Excel Tables](https://exceljet.net/articles/excel-tables)
.

### HYPERLINK

You can use the [HYPERLINK function](https://exceljet.net/functions/hyperlink-function)
 to construct a link with a formula. Note HYPERLINK lets you build both external links and internal links:

![HYPERLINK function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/hyperlink%20function.png?itok=pYuC_1IU "HYPERLINK function example")

    =HYPERLINK(C5,B5)

Copy

### GETPIVOTDATA

The [GETPIVOTDATA function](https://exceljet.net/functions/getpivotdata-function)
 is useful for retrieving information from existing pivot tables.

![GETPIVOTDATA function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/getpivotdata%20function.png?itok=qRVg8-h5 "GETPIVOTDATA function example")

    =GETPIVOTDATA("Sales",$B$4,"Region",I6,"Product",I7)

Copy

### CHOOSE

The [CHOOSE function](https://exceljet.net/functions/choose-function)
 is handy any time you need to make a choice based on a number:

![CHOOSE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/choose%20function.png?itok=rp0RNONW "CHOOSE function example")

    =CHOOSE(2,"red","blue","green") // returns "blue"

Copy

Video: [How to use the CHOOSE function](https://exceljet.net/videos/how-to-use-the-choose-function)

### TRANSPOSE

The [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 gives you an easy way to transpose vertical data to horizontal, and vice versa.

![TRANSPOSE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/transpose%20function.png?itok=8hct6IqD "TRANSPOSE function example")

    {=TRANSPOSE(B4:C9)}

Copy

Note: TRANSPOSE is a formula and is, therefore, dynamic. If you just need to do a one-time transpose operation, use [Paste Special](https://exceljet.net/videos/shortcuts-for-paste-special)
 instead.

### OFFSET

The [OFFSET function](https://exceljet.net/functions/offset-function)
 is useful for all kinds of dynamic ranges. From a starting location, it lets you specify row and column offsets, and also the final row and column size. The result is a _range_ that can respond dynamically to changing conditions and inputs. You can feed this range to other functions, as in the screen below, where OFFSET builds a range that is fed to the [SUM function](https://exceljet.net/functions/sum-function)
:

![OFFSET function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/offset%20function.png?itok=1gDKkXH5 "OFFSET function example")

    =SUM(OFFSET(B4,1,I4,4,1)) // sum of Q3

Copy

### INDIRECT

The [INDIRECT function](https://exceljet.net/functions/indirect-function)
 allows you to build references as text. This concept is a bit tricky to understand at first, but it can be useful in many situations. Below, we are using INDIRECT to get values from cell A1 in 5 different worksheets. Each reference is dynamic. If a sheet name changes, the reference will update.

![INDIRECT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/indirect%20function.png?itok=ftY7JD5X "INDIRECT function example")

    =INDIRECT(B5&"!A1") // =Sheet1!A1

Copy

The INDIRECT function is also used to "lock" references so they won't change, when rows or columns are added or deleted. For more details, see linked examples at the bottom of the [INDIRECT function page](https://exceljet.net/functions/indirect-function)
.

_Caution: both OFFSET and INDIRECT are [volatile functions](https://exceljet.net/glossary/volatile-function)
 and can slow down large or complicated spreadsheets._

STATISTICAL Functions
---------------------

### COUNT and COUNTA

You can count numbers with the [COUNT function](https://exceljet.net/functions/count-function)
 and non-empty cells with [COUNTA](https://exceljet.net/functions/counta-function)
. You can count blank cells with [COUNTBLANK](https://exceljet.net/functions/countblank-function)
, but in the screen below we are counting blank cells with [COUNTIF](https://exceljet.net/functions/countif-function)
, which is more generally useful.

![COUNT and COUNTA function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/count%20and%20counta%20functions.png?itok=ZnlDpjBo "COUNT and COUNTA function examples")

    =COUNT(B5:F5) // count numbers
    =COUNTA(B5:F5) // count numbers and text
    =COUNTIF(B5:F5,"") // count blanks

Copy

### COUNTIF and COUNTIFS

For conditional counts, the [COUNTIF function](https://exceljet.net/functions/countif-function)
 can apply one criteria. The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 can apply multiple criteria at the same time:

![COUNTIF and COUNTIFS function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/countif%20and%20countifs.png?itok=C4QfYG8V "COUNTIF and COUNTIFS function examples")

    =COUNTIF(C5:C12,"red") // count red
    =COUNTIF(F5:F12,">50") // count total > 50
    =COUNTIFS(C5:C12,"red",D5:D12,"TX") // red and tx
    =COUNTIFS(C5:C12,"blue",F5:F12,">50") // blue > 50

Copy

Video: [How to use the COUNTIF function](https://exceljet.net/videos/how-to-use-the-countif-function)

### SUM, SUMIF, SUMIFS

To sum everything, use the [SUM function](https://exceljet.net/functions/sum-function)
. To sum conditionally, use SUMIF or SUMIFS. Following the same pattern as the counting functions, the [SUMIF function](https://exceljet.net/functions/sumif-function)
 can apply only one criteria while the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 can apply multiple criteria.

![SUM, SUMIFS, and SUMIFS function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sum%20sumif%20sumifs%20functions.png?itok=p6Cx0qld "SUM, SUMIFS, and SUMIFS function examples")

    =SUM(F5:F12) // everything
    =SUMIF(C5:C12,"red",F5:F12) // red only
    =SUMIF(F5:F12,">50") // over 50
    =SUMIFS(F5:F12,C5:C12,"red",D5:D12,"tx") // red & tx
    =SUMIFS(F5:F12,C5:C12,"blue",F5:F12,">50") // blue & >50

Copy

Video: [How to use the SUMIF function](https://exceljet.net/videos/how-to-use-the-sumif-function)

### AVERAGE, AVERAGEIF, and AVERAGEIFS

Following the same pattern, you can calculate an average with [AVERAGE](https://exceljet.net/functions/average-function)
, [AVERAGEIF](https://exceljet.net/functions/averageif-function)
, and [AVERAGEIFS](https://exceljet.net/functions/averageifs-function)
.

![AVERAGE, AVERAGEIF, and AVERAGEIFS function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/average%20averageif%20averageifs%20functions.png?itok=R42xrA4B "AVERAGE, AVERAGEIF, and AVERAGEIFS function examples")

    =AVERAGE(F5:F12) // all
    =AVERAGEIF(C5:C12,"red",F5:F12) // red only
    =AVERAGEIFS(F5:F12,C5:C12,"red",D5:D12,"tx") // red and tx

Copy

### MIN, MAX, LARGE, SMALL

You can find largest and smallest values with [MAX](https://exceljet.net/functions/max-function)
 and [MIN](https://exceljet.net/functions/min-function)
, and nth largest and smallest values with [LARGE](https://exceljet.net/functions/large-function)
 and [SMALL](https://exceljet.net/functions/small-function)
. In the screen below, **data** is the [named range](https://exceljet.net/glossary/named-range)
 C5:C13, used in all formulas.

![MAX, MIN, LARGE, and SMALL function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/max%20min%20small%20large%20functions.png?itok=GMZFtaXm "MAX, MIN, LARGE, and SMALL function examples")

    =MAX(data) // largest
    =MIN(data) // smallest
    =LARGE(data,1) // 1st largest
    =LARGE(data,2) // 2nd largest
    =LARGE(data,3) // 3rd largest
    =SMALL(data,1) // 1st smallest
    =SMALL(data,2) // 2nd smallest
    =SMALL(data,3) // 3rd smallest

Copy

Video: [How to find the nth smallest or largest value](https://exceljet.net/videos/how-to-get-nth-values-with-small-and-large)

### MINIFS, MAXIFS

The [MINIFS](https://exceljet.net/functions/minifs-function)
 and [MAXIFS](https://exceljet.net/functions/maxifs-function)
. These functions let you find minimum and maximum values with conditions:

![MINIFS and MAXIFS function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/minif%20and%20maxifs%20functions.png?itok=kS5v816i "MINIFS and MAXIFS function examples")

    =MAXIFS(D5:D15,C5:C15,"female") // highest female
    =MAXIFS(D5:D15,C5:C15,"male") // highest male
    =MINIFS(D5:D15,C5:C15,"female") // lowest female
    =MINIFS(D5:D15,C5:C15,"male") // lowest male

Copy

Note: MINIFS and MAXIFS are new in Excel via Office 365 and Excel 2019.

### MODE

The [MODE function](https://exceljet.net/functions/mode-function)
 returns the most commonly occurring number in a range:

![MODE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/mode%20function.png?itok=tjcmBGIG "MODE function example")

    =MODE(B5:G5) // returns 1

Copy

### RANK

To rank values largest to smallest, or smallest to largest, use the [RANK function](https://exceljet.net/functions/rank-function)
:

![RANK function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rank%20function.png?itok=5EekOr7k "RANK function example")

Video: [How to rank values with the RANK function](https://exceljet.net/videos/how-to-rank-values-with-the-rank-function)

MATH Functions
--------------

### ABS

To change negative values to positive use the [ABS function](https://exceljet.net/functions/abs-function)
.

![ABS function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/abs%20function.png?itok=Z8CBOWy0 "ABS function example")

    =ABS(-134.50) // returns 134.50

Copy

### RAND and RANDBETWEEN

Both the [RAND function](https://exceljet.net/functions/rand-function)
 and [RANDBETWEEN function](https://exceljet.net/functions/randbetween-function)
 can generate random numbers on the fly. RAND creates long decimal numbers between zero and 1. RANDBETWEEN generates random integers between two given numbers.

![RAND and RANDBETWEEN function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/rand%20and%20randbetween%20functions.png?itok=LuTh7pis "RAND and RANDBETWEEN function examples")

    =RAND() // between zero and 1
    =RANDBETWEEN(1,100) // between 1 and 100

Copy

### ROUND, ROUNDUP, ROUNDDOWN, INT

To round values up or down, use the [ROUND function](https://exceljet.net/functions/round-function)
. To force rounding up to a given number of digits, use [ROUNDUP](https://exceljet.net/functions/roundup-function)
. To force rounding down, use [ROUNDDOWN](https://exceljet.net/functions/rounddown-function)
. To discard the decimal part of a number altogether, use the [INT function](https://exceljet.net/functions/int-function)
.

![ROUND, ROUNDUP, ROUNDDOWN, INT function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/round%20roundup%20rounddown%20int%20functions.png?itok=bvLUmEeR "ROUND, ROUNDUP, ROUNDDOWN, INT function examples")

    =ROUND(11.777,1) // returns 11.8
    =ROUNDUP(11.777) // returns 11.8
    =ROUNDDOWN(11.777,1) // returns 11.7
    =INT(11.777) // returns 11

Copy

### MROUND, CEILING, FLOOR

To round values to the nearest _multiple_ use the [MROUND function](https://exceljet.net/functions/mround-function)
. The [FLOOR function](https://exceljet.net/functions/floor-function)
 and [CEILING function](https://exceljet.net/functions/ceiling-function)
 also round to a given multiple. FLOOR forces rounding down, and CEILING forces rounding up.

![MROUND, CEILING, FLOOR functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/mround%20ceiling%20floor%20functions.png?itok=LZv3gWZy "MROUND, CEILING, FLOOR functions")

    =MROUND(13.85,.25) // returns 13.75
    =CEILING(13.85,.25) // returns 14
    =FLOOR(13.85,.25) // returns 13.75

Copy

### MOD

The [MOD function](https://exceljet.net/functions/mod-function)
 returns the remainder after division. This sounds boring and geeky, but MOD turns up in all kinds of formulas, especially formulas that need to do something "every nth time". In the screen below, you can see how MOD returns zero every third number when the divisor is 3:

![MOD function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/mod%20function.png?itok=t6Gnhz_U "MOD function example")

### SUMPRODUCT

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 is a powerful and versatile tool when dealing with all kinds of data. You can use SUMPRODUCT to easily count and sum based on criteria, and you can use it in elegant ways that just don't work with COUNTIFS and SUMIFS. In the screen below, we are using SUMPRODUCT to count and sum orders in March. See the [SUMPRODUCT page](https://exceljet.net/functions/sumproduct-function)
 for details and links to many examples.

![SUMPRODUCT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/sumproduct%20function.png?itok=4akE_vK_ "SUMPRODUCT function example")

    =SUMPRODUCT(--(MONTH(B5:B12)=3)) // count March
    =SUMPRODUCT(--(MONTH(B5:B12)=3),C5:C12) // sum March

Copy

### SUBTOTAL

The [SUBTOTAL function](https://exceljet.net/functions/subtotal-function)
 is an "aggregate function" that can perform a number of operations on a set of data. All told, SUBTOTAL can perform 11 operations, including SUM, AVERAGE, COUNT, MAX, MIN, etc. (see [this page](https://exceljet.net/functions/subtotal-function)
 for the full list). The key feature of SUBTOTAL is that it will ignore rows that have been "filtered out" of an [Excel Table](https://exceljet.net/things-to-know-about-excel-tables)
, and, optionally, rows that have been manually hidden. In the screen below, SUBTOTAL is used to count and sum only the 7 visible rows in the table:

![SUBTOTAL function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/subtotal%20function.png?itok=pyoSIjLi "SUBTOTAL function example")

    =SUBTOTAL(3,B5:B14) // returns 7
    =SUBTOTAL(9,F5:F14) // returns 9.54

Copy

### AGGREGATE

Like SUBTOTAL, the [AGGREGATE function](https://exceljet.net/functions/aggregate-function)
 can also run a number of aggregate operations on a set of data and can optionally ignore hidden rows. The key differences are that AGGREGATE can run more operations (19 total) and can also ignore errors.

In the screen below, AGGREGATE is used to perform MIN, MAX, LARGE and SMALL operations while ignoring errors. Normally, the error in cell B9 would prevent these functions from returning a result. [See this page](https://exceljet.net/functions/aggregate-function)
 for a full list of operations AGGREGATE can perform.

![AGGREGATE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/aggregate%20function.png?itok=8Ro9eCkh "AGGREGATE function example")

    =AGGREGATE(4,6,values) // MAX ignore errors, returns 100
    =AGGREGATE(5,6,values) // MIN ignore errors, returns 75

Copy

TEXT Functions
--------------

### LEFT, RIGHT, MID

To extract characters from the left, right, or middle of text, use [LEFT](https://exceljet.net/functions/left-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, and [MID functions](https://exceljet.net/functions/mid-function)
:

![LEFT, RIGHT, MID function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/left%20right%20mid%20functions.png?itok=wmU2omON "LEFT, RIGHT, MID function examples")

    =LEFT("ABC-1234-RED",3) // returns "ABC"
    =MID("ABC-1234-RED",5,4) // returns "1234"
    =RIGHT("ABC-1234-RED",3) // returns "RED"

Copy

### LEN

The [LEN function](https://exceljet.net/functions/len-function)
 will return the length of a text string. LEN shows up in a lot of formulas that count words or [characters](https://exceljet.net/formulas/count-specific-characters-in-text-string)
.

![LEN function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/len%20function.png?itok=ICT2OnwW "LEN function example")

### FIND, SEARCH

To look for specific text in a cell, use the [FIND function](https://exceljet.net/functions/find-function)
 or [SEARCH function](https://exceljet.net/functions/search-function)
. These functions return the numeric position of matching text, but SEARCH allows wildcards and FIND is case-sensitive. Both functions will throw an error when text is not found, so wrap in the [ISNUMBER](https://exceljet.net/functions/isnumber-function)
 function to return TRUE or FALSE ([example here](https://exceljet.net/formulas/cell-contains-specific-text)
).

![FIND and SEARCH function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/find%20and%20search%20functions.png?itok=yAMJsyQK "FIND and SEARCH function examples")

    =FIND("Better the devil you know","devil") // returns 12
    =SEARCH("This is not my beautiful wife","bea*") // returns 12

Copy

### REPLACE, SUBSTITUTE

To replace text by position, use the [REPLACE function](https://exceljet.net/functions/replace-function)
. To replace text by matching, use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the first example, REPLACE removes the two asterisks (\*\*) by replacing the first two characters with an empty string (""). In the second example, SUBSTITUTE removes all hash characters (#) by replacing "#" with "".

![REPLACE and SUBSTITUTE function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/replace%20and%20substitute.png?itok=SDkaIZpm "REPLACE and SUBSTITUTE function examples")

    =REPLACE("**Red",1,2,"") // returns "Red"
    =SUBSTITUTE("##Red##","#","") // returns "Red"

Copy

### CODE, CHAR

To figure out the numeric code for a character, use the [CODE function](https://exceljet.net/functions/code-function)
. To translate the numeric code back to a character, use the [CHAR function](https://exceljet.net/functions/char-function)
. In the example below, CODE translates each character in column B to its corresponding code. In column F, CHAR translates the code back to a character.

![CODE and CHAR function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/code%20and%20char%20functions.png?itok=e8M1AC1q "CODE and CHAR function examples")

    =CODE("a") // returns 97
    =CHAR(97) // returns "a"

Copy

Video: [How to use the CODE and CHAR functions](https://exceljet.net/videos/how-to-use-char-and-code-functions)

### TRIM, CLEAN

To get rid of extra space in text, use the [TRIM function](https://exceljet.net/functions/trim-function)
. To remove line breaks and other non-printing characters, use [CLEAN](https://exceljet.net/functions/clean-function)
.

![TRIM and CLEAN function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/trim%20and%20clean.png?itok=bs589ATE "TRIM and CLEAN function examples")

    =TRIM(A1) // remove extra space
    =CLEAN(A1) // remove line breaks

Copy

Video: [How to clean text with TRIM and CLEAN](https://exceljet.net/videos/how-to-clean-text-with-clean-and-trim)

### CONCAT, TEXTJOIN, CONCATENATE

New in Excel  via Office 365 are CONCAT and TEXTJOIN. The [CONCAT function](https://exceljet.net/functions/concat-function)
 lets you concatenate (join) multiple values, including a range of values without a delimiter. The [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 does the same thing, but allows you to specify a delimiter and can also ignore empty values.

![CONCAT and TEXTJOIN function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/concat%20and%20textjoin.png?itok=hxoWK5o4 "CONCAT and TEXTJOIN function examples")

    =TEXTJOIN(",",TRUE,B4:H4) // returns "red,blue,green,pink,black"
    =CONCAT(B7:H7) // returns "8675309"

Copy

Excel also provides the [CONCATENATE function](https://exceljet.net/functions/concatenate-function)
, but it doesn't offer special features. I wouldn't bother with it and would instead [concatenate](https://exceljet.net/glossary/concatenation)
 directly with the ampersand (&) character in a formula.

### EXACT

The [EXACT function](https://exceljet.net/functions/exact-function)
 allows you to compare two text strings in a case-sensitive manner.

![EXACT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/exact%20function.png?itok=hyr69kZp "EXACT function example")

### UPPER, LOWER, PROPER

To change the case of text, use the [UPPER](https://exceljet.net/functions/upper-function)
, [LOWER](https://exceljet.net/functions/lower-function)
, and [PROPER function](https://exceljet.net/functions/proper-function)

![UPPER, LOWER, PROPER function examples](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/upper%20lower%20proper%20functions.png?itok=ljb152Yf "UPPER, LOWER, PROPER function examples")

    =UPPER("Sue BROWN") // returns "SUE BROWN"
    =LOWER("Sue BROWN") // returns "sue brown"
    =PROPER("Sue BROWN") // returns "Sue Brown"

Copy

Video: [How to change case with formulas](https://exceljet.net/videos/how-to-change-case-with-upper-lower-and-proper)

### TEXT

Last but definitely not least is the [TEXT function](https://exceljet.net/functions/text-function)
. The text function lets you apply number formatting to numbers (including dates, times, etc.) as text. This is especially useful when you need to embed a formatted number in a message, like "Sale ends on \[date\]".

![TEXT function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/text%20function.png?itok=d65WuOLc "TEXT function example")

    =TEXT(B5,"$#,##0.00")
    =TEXT(B6,"000000")
    ="Save "&TEXT(B7,"0%")
    ="Sale ends "&TEXT(B8,"mmm d")

Copy

More: [Detailed examples of custom number formatting](https://exceljet.net/articles/custom-number-formats)
.

Dynamic Array functions
-----------------------

[Dynamic arrays](https://exceljet.net/glossary/dynamic-array)
 are new in [Excel 365](https://exceljet.net/glossary/excel-365)
, and are a _major_ upgrade to Excel's formula engine. As part of the dynamic array update, Excel includes new functions which directly leverage dynamic arrays to solve problems that are traditionally hard to solve with conventional formulas. If you are using Excel 365, make sure you are aware of these new functions:

| Function | Purpose |
| --- | --- |
| [FILTER](https://exceljet.net/functions/filter-function) | Filter data and return matching records |
| [RANDARRAY](https://exceljet.net/functions/randarray-function) | Generate array of random numbers |
| [SEQUENCE](https://exceljet.net/functions/sequence-function) | Generate array of sequential numbers |
| [SORT](https://exceljet.net/functions/sort-function) | Sort range by column |
| [SORTBY](https://exceljet.net/functions/sortby-function) | Sort range by another range or array |
| [UNIQUE](https://exceljet.net/functions/unique-function) | Extract unique values from a list or range |
| [XLOOKUP](https://exceljet.net/functions/xlookup-function) | Modern replacement for VLOOKUP |
| [XMATCH](https://exceljet.net/functions/xmatch-function) | Modern replacement for the MATCH function |

Video: [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
 (about 3 minutes).

### Quick navigation

[ABS](https://exceljet.net/articles/101-excel-functions#abs)
, [AGGREGATE](https://exceljet.net/articles/101-excel-functions#aggregate)
, [AND](https://exceljet.net/articles/101-excel-functions#and_or_not)
, [AVERAGE](https://exceljet.net/articles/101-excel-functions#average_averageif_averageifs)
, [AVERAGEIF](https://exceljet.net/articles/101-excel-functions#average_averageif_averageifs)
, [AVERAGEIFS](https://exceljet.net/articles/101-excel-functions#average_averageif_averageifs)
, [CEILING](https://exceljet.net/articles/101-excel-functions#mround_ceiling_floor)
, [CHAR](https://exceljet.net/articles/101-excel-functions#code_char)
, [CHOOSE](https://exceljet.net/articles/101-excel-functions#choose)
, [CLEAN](https://exceljet.net/articles/101-excel-functions#trim_clean)
, [CODE](https://exceljet.net/articles/101-excel-functions#code_char)
, [COLUMN](https://exceljet.net/articles/101-excel-functions#row_column)
, [COLUMNS](https://exceljet.net/articles/101-excel-functions#rows_columns)
, [CONCAT](https://exceljet.net/articles/101-excel-functions#concat_textjoin)
, [CONCATENATE](https://exceljet.net/articles/101-excel-functions#concat_textjoin)
, [CONVERT](https://exceljet.net/articles/101-excel-functions#convert)
, [COUNT](https://exceljet.net/articles/101-excel-functions#count_counta)
, [COUNTA](https://exceljet.net/articles/101-excel-functions#count_counta)
, [COUNTBLANK](https://exceljet.net/articles/101-excel-functions#countif_countifs)
, [COUNTIF](https://exceljet.net/articles/101-excel-functions#countif_countifs)
, [COUNTIFS](https://exceljet.net/articles/101-excel-functions#countif_countifs)
, [DATE](https://exceljet.net/articles/101-excel-functions#day_month_year_date)
, [DATEDIF](https://exceljet.net/articles/101-excel-functions#datedif_yearfrac)
, [DAY](https://exceljet.net/articles/101-excel-functions#day_month_year_date)
, [EDATE](https://exceljet.net/articles/101-excel-functions#edate_eomonth)
, [EOMONTH](https://exceljet.net/articles/101-excel-functions#edate_eomonth)
, [EXACT](https://exceljet.net/articles/101-excel-functions#exact)
, [FIND](https://exceljet.net/articles/101-excel-functions#find_search)
, [FLOOR](https://exceljet.net/articles/101-excel-functions#mround_ceiling_floor)
, [GETPIVOTDATA](https://exceljet.net/articles/101-excel-functions#getpivotdata)
, [HLOOKUP](https://exceljet.net/articles/101-excel-functions#vlookup_hlookup)
, [HOUR](https://exceljet.net/articles/101-excel-functions#hour_minute_second_time)
, [HYPERLINK](https://exceljet.net/articles/101-excel-functions#hyperlink)
, [IF](https://exceljet.net/articles/101-excel-functions#if_ifs)
, [IFERROR](https://exceljet.net/articles/101-excel-functions#iferror_ifna)
, [IFNA](https://exceljet.net/articles/101-excel-functions#iferror_ifna)
, [IFS](https://exceljet.net/articles/101-excel-functions#if_ifs)
, [INDEX](https://exceljet.net/articles/101-excel-functions#index_match)
, [INDIRECT](https://exceljet.net/articles/101-excel-functions#indirect)
, [INT](https://exceljet.net/articles/101-excel-functions#round_roundup_rounddown_int)
, [ISBLANK](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISERROR](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISEVEN](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISFORMULA](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISLOGICAL](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISNUMBER](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISODD](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [ISTEXT](https://exceljet.net/articles/101-excel-functions#isblank_iserror_isnumber_isformula)
, [LARGE](https://exceljet.net/articles/101-excel-functions#min_max_large_small)
, [LEFT](https://exceljet.net/articles/101-excel-functions#left_right_mid)
, [LEN](https://exceljet.net/articles/101-excel-functions#len)
, [LOOKUP](https://exceljet.net/articles/101-excel-functions#lookup)
, [LOWER](https://exceljet.net/articles/101-excel-functions#upper_lower_proper)
, [MATCH](https://exceljet.net/articles/101-excel-functions#index_match)
, [MAX](https://exceljet.net/articles/101-excel-functions#min_max_large_small)
, [MAXIFS](https://exceljet.net/articles/101-excel-functions#minifs_maxifs)
, [MID](https://exceljet.net/articles/101-excel-functions#left_right_mid)
, [MIN](https://exceljet.net/articles/101-excel-functions#min_max_large_small)
, [MINIFS](https://exceljet.net/articles/101-excel-functions#minifs_maxifs)
, [MINUTE](https://exceljet.net/articles/101-excel-functions#hour_minute_second_time)
, [MOD](https://exceljet.net/articles/101-excel-functions#mod)
, [MODE](https://exceljet.net/articles/101-excel-functions#mode)
, [MONTH](https://exceljet.net/articles/101-excel-functions#day_month_year_date)
, [MROUND](https://exceljet.net/articles/101-excel-functions#mround_ceiling_floor)
, [NETWORKDAYS](https://exceljet.net/articles/101-excel-functions#workday_networkdays)
, [NOT](https://exceljet.net/articles/101-excel-functions#and_or_not)
, [NOW](https://exceljet.net/articles/101-excel-functions#now_today)
, [OFFSET](https://exceljet.net/articles/101-excel-functions#offset)
, [OR](https://exceljet.net/articles/101-excel-functions#and_or_not)
, [PROPER](https://exceljet.net/articles/101-excel-functions#upper_lower_proper)
, [RAND](https://exceljet.net/articles/101-excel-functions#rand_randbetween)
, [RANDBETWEEN](https://exceljet.net/articles/101-excel-functions#rand_randbetween)
, [RANK](https://exceljet.net/articles/101-excel-functions#rank)
, [REPLACE](https://exceljet.net/articles/101-excel-functions#replace_substitute)
, [RIGHT](https://exceljet.net/articles/101-excel-functions#left_right_mid)
, [ROUND](https://exceljet.net/articles/101-excel-functions#round_roundup_rounddown_int)
, [ROUNDDOWN](https://exceljet.net/articles/101-excel-functions#round_roundup_rounddown_int)
, [ROUNDUP](https://exceljet.net/articles/101-excel-functions#round_roundup_rounddown_int)
, [ROW](https://exceljet.net/articles/101-excel-functions#row_column)
, [ROWS](https://exceljet.net/articles/101-excel-functions#rows_columns)
, [SEARCH](https://exceljet.net/articles/101-excel-functions#find_search)
, [SECOND](https://exceljet.net/articles/101-excel-functions#hour_minute_second_time)
, [SMALL](https://exceljet.net/articles/101-excel-functions#min_max_large_small)
, [SUBSTITUTE](https://exceljet.net/articles/101-excel-functions#replace_substitute)
, [SUBTOTAL](https://exceljet.net/articles/101-excel-functions#subtotal)
, [SUM](https://exceljet.net/articles/101-excel-functions#sum_sumif_sumifs)
, [SUMIF](https://exceljet.net/articles/101-excel-functions#sum_sumif_sumifs)
, [SUMIFS](https://exceljet.net/articles/101-excel-functions#sum_sumif_sumifs)
, [SUMPRODUCT](https://exceljet.net/articles/101-excel-functions#sumproduct)
, [TEXT](https://exceljet.net/articles/101-excel-functions#text)
, [TEXTJOIN](https://exceljet.net/articles/101-excel-functions#concat_textjoin)
, [TIME](https://exceljet.net/articles/101-excel-functions#hour_minute_second_time)
, [TODAY](https://exceljet.net/articles/101-excel-functions#now_today)
, [TRANSPOSE](https://exceljet.net/articles/101-excel-functions#transpose)
, [TRIM](https://exceljet.net/articles/101-excel-functions#trim_clean)
, [UPPER](https://exceljet.net/articles/101-excel-functions#upper_lower_proper)
, [VLOOKUP](https://exceljet.net/articles/101-excel-functions#vlookup_hlookup)
, [WEEKDAY](https://exceljet.net/articles/101-excel-functions#weekday_weeknum)
, [WEEKNUM](https://exceljet.net/articles/101-excel-functions#weekday_weeknum)
, [WORKDAY](https://exceljet.net/articles/101-excel-functions#workday_networkdays)
, [YEAR](https://exceljet.net/articles/101-excel-functions#day_month_year_date)
, [YEARFRAC](https://exceljet.net/articles/101-excel-functions#datedif_yearfrac)
 

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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