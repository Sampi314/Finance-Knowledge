# Excel Formula List - Which formulas you must learn - 100+ examples

**Source:** https://chandoo.org/wp/excel-formula-list

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

100+ Excel Formula Examples + List
==================================

*   Last updated on June 28, 2018

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**The first step of getting awesome in Excel is to understand that** _**you can ask Excel do things for you.**_ This is done by speaking a special language called as “Excel Formulas”. When you write a formula or function, you are asking Excel to figure out something from the values you have. Say you want to add up a bunch of values in a range A1:A10, you can ask Excel to do this for you by writing =SUM(A1:A10) and bingo, you get the result immediately. The best part is, if your numbers change, the answer changes too.

If you are a beginner, Excel formula list can feel overwhelming. Why not? There are hundreds of different formulas in Excel. _**So which formulas should you learn?**_

![Excel Formula list, examples and how-to - Free Guide](https://chandoo.org/wp/wp-content/uploads/2018/06/excel-formula-how-to.jpg)

This guide gives you the answer. Here is a 100+ Excel formula list for every occasion. Each box describes a problem statement, an example, result, some notes and link to learn more. Use this guide to learn formulas quickly.

### Data for Excel formula list in this guide

Most formula examples shown here are self-explanatory. In some places I have used a table of data, called **_staff._** Here is a snapshot of the Staff table. When looking a formula example, refer to this image to understand how the calculation works.

![data for Excel Formula examples](https://chandoo.org/wp/wp-content/uploads/2018/06/sample-data-for-formula-how-to.png)

If you have never used tables before, check out [**Excel Tables – What are they and how to use them?**](https://chandoo.org/wp/data-tables/)
 to learn more.

Excel Formula List by topic
---------------------------

This page is rather long. So I have broken it in to sections. Click on below links to navigate or use CTRL+F on your browser to search for a function / formula how-to.

*   [Numbers, values, summaries and statistics](https://chandoo.org/wp/excel-formula-list/#numbers)
    
*   [Check things, apply business rules and logic control](https://chandoo.org/wp/excel-formula-list/#logical)
    
*   [Lookup items](https://chandoo.org/wp/excel-formula-list/#lookup)
    
*   [Convert data](https://chandoo.org/wp/excel-formula-list/#convert)
    
*   [Text values, strings, words and phrases](https://chandoo.org/wp/excel-formula-list/#text)
    
*   [Date, time and calendar](https://chandoo.org/wp/excel-formula-list/#date-time)
    
*   [Operations on numbers](https://chandoo.org/wp/excel-formula-list/#operations)
    
*   [Check and prevent errors](https://chandoo.org/wp/excel-formula-list/#errors)
    
*   [Generate randomized data](https://chandoo.org/wp/excel-formula-list/#random)
    

Formulas related to numbers, values, summaries and statistics
-------------------------------------------------------------

Excel offers many functions when it comes to working with numeric values. Use below example formulas and functions to work efficiently with numbers. Learn how to calculate count, sum, average and other statistical summaries from your data. Apart from the functions discussed here, you can also use operators like + (to add things), -(to subtract), \*(to multiply), /(to divide), %(to convert a value to percentage), ^(to raise the power), ~(to negate a Boolean value) and brackets to create expressions.

|     |     |
| --- | --- | 
| ### Add some values |     |
|     |     |
| Example | \=SUM(5,6,9) |
| Result | 20  |

|     |     |
| --- | --- | 
| ### Add values from a range of cells |     |
|     |     |
| Example | \=SUM(A1:A5) |
| Result | 125 |

|     |     |
| --- | --- | 
| ### Sum up values from a table reference |     |
|     |     |
| Example | \=SUM(staff\[Salary\]) |
| Result | $ 945,000 |

|     |     |
| --- | --- | 
| ### Sum of numbers that meet conditions |     |
|     |     |
| Example | \=SUMIFS(staff\[Salary\], staff\[Department\],"Sales") |
| Result | $ 279,000 |
| Learn more about this formula: [SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/) |     |

|     |     |
| --- | --- | 
| ### Sum of numbers greater than (less than etc.) something |     |
|     |     |
| Example | \=SUMIFS(A1:A6, A1:A6,">25") |
| Result | 100 |
| Learn more about this formula: [SUMIFS formula](https://chandoo.org/wp/introduction-to-excel-sumifs-formula/) |     |

|     |     |
| --- | --- | 
| ### Sum of numbers that are currently filtered |     |
|     |     |
| Example | \=SUBTOTAL(109,staff\[Salary\]) |
| Result | $ 945,000 |
| Learn more about this formula: [SUBTOTAL function](https://chandoo.org/wp/subtotal-formula-excel/) |     |

|     |     |
| --- | --- | 
| ### Count of numbers that are currently filtered |     |
|     |     |
| Example | \=SUBTOTAL(103,staff\[Name\]) |
| Result | 13  |
| Learn more about this formula: [SUBTOTAL function](https://chandoo.org/wp/subtotal-formula-excel/) |     |

|     |     |
| --- | --- | 
| ### Running total in a column, adjacent to original data |     |
| _Type this formula in first cell and drag down to get running total._ |     |
| Example | \=SUM($A$1:A1) |
| Result | 10  |

|     |     |
| --- | --- | 
| ### Count of numbers in a range |     |
|     |     |
| Example | \=COUNT(A1:A6) |
| Result | 6   |

|     |     |
| --- | --- | 
| ### Count of all values (including text) |     |
|     |     |
| Example | \=COUNTA(staff\[Name\]) |
| Result | 13  |

|     |     |
| --- | --- | 
| ### Count of blank values in the input (range or table column) |     |
|     |     |
| Example | \=COUNTBLANK(A1:A20) |
| Result | 14  |

|     |     |
| --- | --- | 
| ### Count number of non-blank values |     |
| _ROWS formula tells how rows are there in a range. You can also use COLUMNS_ |     |
| Example | \=ROWS(A1:A20)-COUNTBLANK(A1:A20) |
| Result | 6   |

|     |     |
| --- | --- | 
| ### Count how many items have met given conditions |     |
|     |     |
| Example | \=COUNTIFS(staff\[Department\],"IT") |
| Result | 3   |

|     |     |
| --- | --- | 
| ### Count how many items begin with given text |     |
| _\* is a wild card. You can use it to match any number of letters. If you want to match a single letter, use ?_ |     |
| Example | \=COUNTIFS(staff\[Name\],"J\*") |
| Result | 13  |

|     |     |
| --- | --- | 
| ### Count how many items end with given pattern |     |
|     |     |
| Example | \=COUNTIFS(staff\[Name\],"\*n") |
| Result | 4   |

|     |     |
| --- | --- | 
| ### Count how many items contain given word |     |
|     |     |
| Example | \=COUNTIFS(staff\[Name\],"\*an\*") |
| Result | 3   |

|     |     |
| --- | --- | 
| ### Average of given numbers |     |
|     |     |
| Example | \=AVERAGE(staff\[Salary\]) |
| Result | $ 72,692 |
| Learn more about this formula: [More about Averages in your analysis](https://chandoo.org/wp/cp009-averages-are-mean-part1/) |     |

|     |     |
| --- | --- | 
| ### Average of given numbers satisfying conditions |     |
|     |     |
| Example | \=AVERAGEIFS(staff\[Salary\],staff\[Department\], "HR") |
| Result | $ 77,333 |

|     |     |
| --- | --- | 
| ### Average of positive numbers |     |
|     |     |
| Example | \=AVERAGEIFS(A1:A10,A1:A10,">0") |
| Result | 25.83 |

|     |     |
| --- | --- | 
| ### Average of numbers excluding top & bottom 10% values |     |
|     |     |
| Example | \=TRIMMEAN(staff\[Salary\],10%) |
| Result | $ 72,692 |

|     |     |
| --- | --- | 
| ### 7 day moving average from daily data |     |
| _Type this formula in first cell and drag down to get moving average._ |     |
| Example | \=AVERAGE(A1:A7) |
| Result | 25.83 |
| Learn more about this formula: [Moving Average in Excel](https://chandoo.org/wp/calculate-moving-average/) |     |

|     |     |
| --- | --- | 
| ### Weighted average of numbers |     |
| _A1:A6 contain values and B1:B6 contain weights_ |     |
| Example | \=SUMPRODUCT(A1:A6,B1:B6) |
| Result | 2,550 |
| Learn more about this formula: [Weighted Average Formula](https://chandoo.org/wp/weighted-average-excel/) |     |

|     |     |
| --- | --- | 
| ### Median of a range of values |     |
|     |     |
| Example | \=MEDIAN(staff\[Salary\]) |
| Result | $ 76,000 |

|     |     |
| --- | --- | 
| ### Most frequent number in a range (MODE) |     |
| _If your list has multiple MODEs, use MODE.MULT to return all of them as a new list._ |     |
| Example | \=MODE.SNGL(1,2,3,3,2,1,1,5,6,7,3,4,8,9) |
| Result | 1   |

|     |     |
| --- | --- | 
| ### Statistical quartiles of given values |     |
| _Use 1 for first quartile, 2 for median, 3 for third quartile. EXC means 0 & 1 are excluded when calculating quartiles._ |     |
| Example | \=QUARTILE.EXC(staff\[Salary\],1) |
| Result | $ 59,500 |

|     |     |
| --- | --- | 
| ### 90th (or any other) percentile of given values |     |
|     |     |
| Example | \=PERCENTILE.EXC(staff\[Salary\],0.9) |
| Result | $ 89,000 |

|     |     |
| --- | --- | 
| ### Minimum value among a list of numbers |     |
|     |     |
| Example | \=MIN(A1:A6) |
| Result | 10  |

|     |     |
| --- | --- | 
| ### 3rd smallest (or any other) among a list |     |
|     |     |
| Example | \=SMALL(staff\[Salary\],3) |
| Result | $ 59,000 |

|     |     |
| --- | --- | 
| ### Rank of a number in a list of values |     |
| _If two numbers share a rank, then the rank will be averaged. Use RANK.EQ to return same rank for both numbers_ |     |
| Example | \=RANK.AVG(76000, staff\[Salary\]) |
| Result | 7   |

|     |     |
| --- | --- | 
| ### Maximum value from a list of values |     |
|     |     |
| Example | \=MAX(staff\[Salary\]) |
| Result | $ 89,000 |

|     |     |
| --- | --- | 
| ### 2nd largest value in a spreadsheet range |     |
|     |     |
| Example | \=LARGE(A2:A7,2) |
| Result | 30  |

Formulas to do operations on numbers
------------------------------------

Whenever you have some numbers in a worksheet, you may want to run some operations like rounding them or extracting integer portion etc. on them. In this section, see some of the frequently used number operations.

|     |     |
| --- | --- | 
| ### Remainder after dividing two numbers |     |
|     |     |
| Example | \=MOD(31,7) |
| Result | 3   |

|     |     |
| --- | --- | 
| ### Round a number to nearest whole number or fraction |     |
|     |     |
| Example | \=ROUND(PI(),4) |
| Result | 3.1416 |

|     |     |
| --- | --- | 
| ### Round a number to nearest multiple of x |     |
|     |     |
| Example | \=MROUND(27,4) |
| Result | 28  |

|     |     |
| --- | --- | 
| ### Integer portion of a number |     |
|     |     |
| Example | \=INT(19/7) |
| Result | 2   |

|     |     |
| --- | --- | 
| ### Percentage change (variance) from one value to another |     |
| _H4 is 35000, H5 is 38000_ |     |
| Example | \=H5/H4-1 |
| Result | 8.57% |

|     |     |
| --- | --- | 
| ### Decimal portion of a number |     |
|     |     |
| Example | \=MOD(PI(),1) |
| Result | 0.141592654 |

|     |     |
| --- | --- | 
| ### Absolute value of a number |     |
|     |     |
| Example | \=ABS(30-43) |
| Result | 13  |

|     |     |
| --- | --- | 
| ### Calculate power of one number to another |     |
|     |     |
| Example | \=7^3 |
| Result | 343 |

Formulas related to check things, apply business rules and logic control
------------------------------------------------------------------------

Microsoft Excel has several powerful functions to check things and set up control or business logic in your workbooks. You can use IF function to write simple logic expressions or nest multiple IF functions for more complex scenarios. You can also use newly introduced IFS function to write long multi-step if function. This only works in Office 365 or Excel online. See below examples to learn more about formulas and functions to check things and apply business rules.

|     |     |
| --- | --- | 
| ### Check a condition and output one of the two possible values |     |
|     |     |
| Example | \=IF(A9>20,"Too high", "Too low") |
| Result | Too low |
| Learn more about this formula: [Writing logical rules in Excel](https://chandoo.org/wp/cp028-how-to-tell-business-logic-rules-to-excel/) |     |

|     |     |
| --- | --- | 
| ### Check if multiple conditions are true (AND) |     |
|     |     |
| Example | \=AND(A9>5,B9<20) |
| Result | FALSE |

|     |     |
| --- | --- | 
| ### Check if any condition is true (OR) |     |
|     |     |
| Example | \=OR(E10="Sales", F10>90000, D10=A9) |
| Result | FALSE |

|     |     |
| --- | --- | 
| ### Logical NOT check |     |
|     |     |
| Example | \=NOT("Sam"="Samuel") |
| Result | TRUE |

|     |     |
| --- | --- | 
| ### Check if either this or that (Exclusive OR) |     |
| _Will be TRUE only if either A1>10 or B1>10 but not both or neither._ |     |
| Example | \=XOR(A9>10, B9>10) |
| Result | FALSE |
| Learn more about this formula: [More on XOR](https://chandoo.org/wp/bitwise-operations-in-excel/) |     |

|     |     |
| --- | --- | 
| ### Select one among multiple values |     |
| _Picks a value from a list of values, in this case, picks A2 as it is the 3rd value._ |     |
| Example | \=CHOOSE(3,A9,B10,A10,B11) |
| Result | 0   |
| Learn more about this formula: [CHOOSE Function](https://chandoo.org/wp/introduction-to-choose-function/) |     |

|     |     |
| --- | --- | 
| ### Multiple IF conditions as IFS |     |
| _A9 has 7. Works only in Office 365, Office online (and may be in Excel 2019)_ |     |
| Example | \=ifs(A9>10, "This is too high", A9>5, "This is ok", A9>2,"Almost low", A9<=2,"Really low") |
| Result | This is ok |

|     |     |
| --- | --- | 
| ### Check if a value is present in a list |     |
|     |     |
| Example | \=IF(COUNTIFS(staff\[Name\],"Jan")>0,"Yes, Jan is in there","No, no such person") |
| Result | Yes, Jan is in there |

|     |     |
| --- | --- | 
| ### Check multiple conditions as nested IF |     |
|     |     |
| Example | \=IF(A9>10, "This is too high",IF( A9>5, "This is ok", IF(A9>2,"Almost low", "Really low"))) |
| Result | Really low |

|     |     |
| --- | --- | 
| ### Check if a value is between two other values |     |
|     |     |
| Example | \=IF(AND(A9>=10,A9<=20),"Between 10 and  20","Nope, not between 10 and 20") |
| Result | Nope, not between 10 and 20 |
| Learn more about this formula: [Between Formula](https://chandoo.org/wp/between-formula-excel/) |     |

|     |     |
| --- | --- | 
| ### Is a cell blank? |     |
|     |     |
| Example | \=ISBLANK(A18) |
| Result | TRUE |

|     |     |
| --- | --- | 
| ### Is a value even? |     |
|     |     |
| Example | \=ISEVEN(7) |
| Result | FALSE |

|     |     |
| --- | --- | 
| ### Is a value odd? |     |
|     |     |
| Example | \=ISODD(7) |
| Result | TRUE |

|     |     |
| --- | --- | 
| ### Is a cell contains number? |     |
|     |     |
| Example | \=ISNUMBER(A9) |
| Result | FALSE |

|     |     |
| --- | --- | 
| ### Is a cell contains formula? |     |
|     |     |
| Example | \=ISFORMULA(A9) |
| Result | FALSE |

|     |     |
| --- | --- | 
| ### Is a cell (or formula) ends up in error? |     |
|     |     |
| Example | \=ISERROR(7/0) |
| Result | TRUE |

Formulas to work with text values, strings, words and phrases
-------------------------------------------------------------

While Excel is predominantly a number driven tool, we still have lots of text values in spreadsheets. Excel has many powerful and elegant text processing functions to help you extract, analyze or understand your text / string values. You can use the special operator & to combine text values or even work with newly introduced TEXTJOIN() function to combine a range of values to one. Keep in mind, this TEXTJOIN only works in Office 365 or Excel Online at the moment. In the below examples, know how to work with string / text values in your workbooks using formulas.

|     |     |
| --- | --- | 
| ### Convert text to lower case |     |
|     |     |
| Example | \=LOWER("hello") |
| Result | hello |

|     |     |
| --- | --- | 
| ### Convert text to upper case |     |
|     |     |
| Example | \=UPPER(D3) |
| Result | JAMES |

|     |     |
| --- | --- | 
| ### Convert text to proper case (each word's first letter capitalized) |     |
|     |     |
| Example | \=PROPER("this is a long sentence") |
| Result | This Is A Long Sentence |

|     |     |
| --- | --- | 
| ### Combine different text values to one text |     |
|     |     |
| Example | \=CONCATENATE(A3, " and ", A4) |
| Result | 30 and 25 |

|     |     |
| --- | --- | 
| ### Combine different text values to one text |     |
|     |     |
| Example | \=A3&" and "&A4 |
| Result | 30 and 25 |

|     |     |
| --- | --- | 
| ### Extract first few letters from a text |     |
|     |     |
| Example | \=LEFT("India",3) |
| Result | Ind |

|     |     |
| --- | --- | 
| ### Extract last few letters from a text |     |
|     |     |
| Example | \=RIGHT("New Zealand",4) |
| Result | land |

|     |     |
| --- | --- | 
| ### Extract middle portion from given text |     |
|     |     |
| Example | \=MID("United States",4,5) |
| Result | ted S |

|     |     |
| --- | --- | 
| ### What is the length of given text value |     |
|     |     |
| Example | \=LEN("Chandoo.org") |
| Result | 11  |

|     |     |
| --- | --- | 
| ### Substitute one word with another |     |
|     |     |
| Example | \=SUBSTITUTE("Microsoft Excel","cel","cellent") |
| Result | Microsoft Excellent |

|     |     |
| --- | --- | 
| ### Replace some letters with other |     |
|     |     |
| Example | \=REPLACE("abc@email.com",5,1,"g") |
| Result | abc@gmail.com |

|     |     |
| --- | --- | 
| ### Find if a text has another text |     |
|     |     |
| Example | \=FIND("soft","Microsoft Excel") |
| Result | 6   |

|     |     |
| --- | --- | 
| ### Extract initials from a name |     |
| _H1 contains Bill Jelen_ |     |
| Example | \=LEFT(H1,1)&MID(H1,FIND(" ",H1)+1,1) |
| Result | BJ  |

|     |     |
| --- | --- | 
| ### Find out how many words are in a sentence |     |
| _H2 contains "This is a very long sentence with lots of words"_ |     |
| Example | \=LEN(H2)-LEN(SUBSTITUTE(H2," ",""))+1 |
| Result | 10  |

|     |     |
| --- | --- | 
| ### Remove unnecessary spaces from a cell |     |
|     |     |
| Example | \=TRIM("  chandoo.  org   ") |
| Result | chandoo. org |

|     |     |
| --- | --- | 
| ### Remove anything after a symbol or word |     |
| _H3 contains someone@something.com_ |     |
| Example | \=LEFT(H3,FIND("@",H3)-1) |
| Result | someone |

Formulas to work with date, time and calendar
---------------------------------------------

Date and time values are very important when working with business data. That is why, Excel has many functions in this space. You can use TODAY() to figure out what is the current date or use DATE() to generate a date that you want. In the below examples, learn how to calculate some of the most common date and time related stuff using Excel.

|     |     |
| --- | --- | 
| ### What is today's date? |     |
|     |     |
| Example | \=TODAY() |
| Result | 6/27/2018 |

|     |     |
| --- | --- | 
| ### What is the current date & time? |     |
|     |     |
| Example | \=NOW() |
| Result | 6/27/2018 12:00 |

|     |     |
| --- | --- | 
| ### Create a date value from year, month and day |     |
|     |     |
| Example | \=DATE(2018,10,20) |
| Result | 10/20/2018 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Create a time value from hour, minute and second |     |
|     |     |
| Example | \=TIME(9,45,21) |
| Result | 9:45 AM |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Get day of month from given date |     |
|     |     |
| Example | \=DAY(TODAY()) |
| Result | 27  |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### What month is a given date on? |     |
|     |     |
| Example | \=MONTH(DATEVALUE("12-July-1999")) |
| Result | 7   |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Extract year from a date |     |
|     |     |
| Example | \=YEAR(TODAY()) |
| Result | 2018 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Find out day of week (number) from a date |     |
|     |     |
| Example | \=WEEKDAY(TODAY()) |
| Result | 4   |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Find out day of week (name of the day) from a date |     |
| _Use DDD to see short form of day name, such as SUN, MON etc._ |     |
| Example | \=TEXT(TODAY(), "DDDD") |
| Result | Wednesday |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### What is the name of a month from a date? |     |
| _Use MMM to see short form of month name, such as Jan, Feb etc._ |     |
| Example | \=TEXT(TODAY(), "MMMM") |
| Result | June |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Hour from time |     |
|     |     |
| Example | \=HOUR(NOW()) |
| Result | 12  |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Minute from time |     |
|     |     |
| Example | \=MINUTE(NOW()) |
| Result | 0   |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Second from time |     |
|     |     |
| Example | \=SECOND(NOW()) |
| Result | 2   |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### What is the date after / before x months |     |
|     |     |
| Example | \=EDATE(TODAY(),3) |
| Result | 9/27/2018 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### What is the last date of a month? |     |
|     |     |
| Example | \=EOMONTH(DATE(2018,8,1),0) |
| Result | 8/31/2018 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Calculate number of days between two dates |     |
|     |     |
| Example | \=DATE(2018,12,1)-DATEVALUE("1-july-2018") |
| Result | 153 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Calculate number of years between two dates |     |
| _You can also use (date1-date2)/365 to calculate number of years between 2 dates_ |     |
| Example | \=YEARFRAC(DATE(2009,9,24),TODAY(),1) |
| Result | 8.76 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### Number of weeks between two dates |     |
|     |     |
| Example | \=INT((DATE(2018,12,1)-DATEVALUE("1-july-2018"))/7) |
| Result | 21  |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### What is the date after / before x working days (excluding weekends etc.) |     |
| _This assumes Saturday & Sunday are weekends. If you have some other workweek pattern, use the 3rd parameter of WORKDAY.INTL to specify that. Likewise, you can also specify a list of special holidays (New Years Day, Diwali, Ramadan or Christmas etc.) to exclude them too_ |     |
| Example | \=WORKDAY.INTL(TODAY(),12) |
| Result | 7/13/2018 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

|     |     |
| --- | --- | 
| ### How many working days are between two dates? |     |
| _This assumes Saturday & Sunday are weekends. If you have some other workweek pattern, use the 3rd parameter of NETWORKDAYS.INTL to specify that. Likewise, you can also specify a list of special holidays (New Years Day, Diwali, Ramadan or Christmas etc.) to exclude them too_ |     |
| Example | \=NETWORKDAYS.INTL(TODAY(),DATE(2018,12,31)) |
| Result | 134 |
| Learn more about this formula: [Working with date & time values in Excel](https://chandoo.org/wp/date-time-tips-ms-excel/) |     |

Formulas to lookup items
------------------------

Lookup functions help us answer specific questions from business data, like which customer placed the order number PQ1234? You can use them to ask simple questions or combine lookup functions with other formulas in Excel to find more complex things. In these examples, learn how to write some of the most common lookup functions in Excel.

|     |     |
| --- | --- | 
| ### Lookup a value in a table and find corresponding items (example, salary of an employee) |     |
| _Finds John in the staff table's first column and returns value from 3rd column (salary)_ |     |
| Example | \=VLOOKUP("John", staff, 3, FALSE) |
| Result | $ 77,000 |
| Learn more about this formula: [All you want to know about VLOOKUP](https://chandoo.org/wp/comprehensive-guide-excel-vlookup/) |     |

|     |     |
| --- | --- | 
| ### Lookup a pattern in a table and find corresponding items (example, salary of an employee) |     |
|     |     |
| Example | \=VLOOKUP("Jon\*", staff,2,FALSE) |
| Result | Production |
| Learn more about this formula: [VLOOKUP with wild cards](https://chandoo.org/wp/using-wildcards-with-vlookup/) |     |

|     |     |
| --- | --- | 
| ### What is the position of a value in a list? |     |
|     |     |
| Example | \=MATCH(76000,staff\[Salary\],0) |
| Result | 10  |
| Learn more about this formula: [Using MATCH formula](https://chandoo.org/wp/how-to-lookup-values-to-left/) |     |

Formulas to convert one data to another type of data
----------------------------------------------------

Often, we end up having data that is not in the right format to do our job. You can use conversion formulas to change data from one type to another.

|     |     |
| --- | --- | 
| ### Convert a cell to number |     |
| _Here . Is the thousand's separator and , is decimal point (i.e. European notation)_ |     |
| Example | \=NUMBERVALUE("123.456,78",",",".") |
| Result | 123,456.78 |

|     |     |
| --- | --- | 
| ### Convert a value to date |     |
|     |     |
| Example | \=DATEVALUE("1-jul-2018") |
| Result | 7/1/2018 |

|     |     |
| --- | --- | 
| ### Convert a cell to number (another technique) |     |
| _You can also +0 to a text value to convert it to number._ |     |
| Example | \="12456.78"\*1 |
| Result | 12,456.78 |

Formulas to check and prevent errors
------------------------------------

We can't escape bad coffee, occasionally annoying bosses and errors. Of course, Excel can't help you with first two, but it does a fine job of handling errors for us. Learn how to use the important error handling and checking functions in Excel.

|     |     |
| --- | --- | 
| ### Show a different value if a formula has an error |     |
|     |     |
| Example | \=IFERROR(VLOOKUP("Sam",staff,3,FALSE),"Employee not found") |
| Result | Employee not found |
| Learn more about this formula: [IFERROR](https://chandoo.org/wp/iferror-formula/) |     |

|     |     |
| --- | --- | 
| ### Show a different value if a formula has an NA error |     |
|     |     |
| Example | \=IFNA(7/0,"This will appear if the error is #N/A") |
| Result | #DIV/0! |

|     |     |
| --- | --- | 
| ### Is a cell (or formula) ends up in error? |     |
|     |     |
| Example | \=ISERROR(7/0) |
| Result | TRUE |

|     |     |
| --- | --- | 
| ### Safely divide one number with another |     |
|     |     |
| Example | \=IF(A2=0,"",A1/A2) |
| Result | 0.5 |

Formulas to generate randomized data
------------------------------------

Once in a while you need to generate or create random data in Excel. You can use either RAND() or RANDBETWEEN() to complete the job. In these examples, learn how to create most common types of random data using Excel.

|     |     |
| --- | --- | 
| ### Generate a random number |     |
| _The output changes every time you make a change in your spreadsheet._ |     |
| Example | \=RAND() |
| Result | 0.948708709 |

|     |     |
| --- | --- | 
| ### Generate a random phone number |     |
| _The output changes every time you make a change in your spreadsheet._ |     |
| Example | \=RANDBETWEEN(1000000000,9999999999) |
| Result | (535) 050-1262 |

|     |     |
| --- | --- | 
| ### Generate a random letter from alphabet |     |
| _The output changes every time you make a change in your spreadsheet._ |     |
| Example | \=CHAR(RANDBETWEEN(CODE("A"),CODE("Z"))) |
| Result | Z   |

|     |     |
| --- | --- | 
| ### Create a random option from a list of values |     |
| _The output changes every time you make a change in your spreadsheet._ |     |
| Example | \=INDEX(staff\[Name\], RANDBETWEEN(1,COUNTA(staff\[Name\]))) |
| Result | June |

Want some other example? Post a comment
---------------------------------------

Are you looking for some other example? Please post a comment explaining what you are looking for so our community can help you.

And of course, if you love this guide, **please share** it with your friends using the buttons below.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [69 Comments](https://chandoo.org/wp/excel-formula-list/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-formula-list/#respond)
    
*   Tagged under [Excel 101](https://chandoo.org/wp/tag/excel-101/)
    , [excel basics](https://chandoo.org/wp/tag/excel-basics/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousHow to undo in Power Query \[Quick Tip\]](https://chandoo.org/wp/how-to-undo-in-power-query/)

[NextPlay spreadsheet soccer with Excel Penalty Game \[VBA\]Next](https://chandoo.org/wp/excel-penalty-game/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/excel-formula-list/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-formula-list/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-formula-list/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ