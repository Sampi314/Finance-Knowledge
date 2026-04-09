# Zodiac sign lookup - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/zodiac-sign-lookup

---

[Skip to main content](https://exceljet.net/formulas/zodiac-sign-lookup#main-content)

[](https://exceljet.net/formulas/zodiac-sign-lookup#)

*   [Previous](https://exceljet.net/formulas/xmatch-with-multiple-criteria)
    
*   [Next](https://exceljet.net/formulas/calculate-sales-commission-with-if)
    

[Lookup](https://exceljet.net/formulas#Lookup)

Zodiac sign lookup
==================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

[TEXT](https://exceljet.net/functions/text-function)

[DATEVALUE](https://exceljet.net/functions/datevalue-function)

[IFNA](https://exceljet.net/functions/ifna-function)

[YEAR](https://exceljet.net/functions/year-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6579/download?token=_f4t6ZtC)
 (16.02 KB)

![Excel formula: Zodiac sign lookup](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/zodiac%20sign%20lookup_0.png "Excel formula: Zodiac sign lookup")

Summary
-------

To look up one of the 12 Western Zodiac signs based on a birthdate, you can use a formula based on [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
. The formula in H7 is:

    =INDEX(sign,IFNA(MATCH(1,(dob>=DATEVALUE(start&", "&YEAR(dob)))*(dob<=DATEVALUE(end&", "&YEAR(dob))),0),10))
    

where **dob** (H5), **sign** (B5:B16), **symbol** (D5:D16), **start** (E5:E15), and **end** (F5:F16) are [named ranges](https://exceljet.net/glossary/named-range)
. Using the lookup table as shown is somewhat challenging. See below for an alternative self-contained formula.

Explanation 
------------

The goal of this example is to look up the correct astrological or zodiac sign for a given birthdate, using the table shown in B5:F15. These are based on the [Western zodiac signs described here](https://en.wikipedia.org/wiki/Astrological_sign)
. Zodiac signs are used in horoscopes, which are a kind of forecast of a person's future, based on the relative positions of the stars and planets at the time of birth.

Using the lookup table as shown is somewhat challenging. This article describes two ways to solve the problem. The [first way uses INDEX and MATCH](https://exceljet.net/formulas/zodiac-sign-lookup#index_match_formula)
 with the table as shown. The [second way is a VLOOKUP formula](https://exceljet.net/formulas/zodiac-sign-lookup#alt_formula)
 with a hard-coded array constant.

### Preface

For this example, I was determined to use a formula to look up a zodiac sign in an existing table (as shown) that lists each zodiac sign along with a symbol, start, and end dates. This is a challenging problem for a couple of reasons. First, the start and end dates are not actual dates, but are instead "date fragments." Second, because the zodiac signs start in March and cross over a year boundary, they are not listed in chronological order. If they were real dates in chronological order, we could use a standard [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
 formula set up for an approximate match on the start date only. Instead, we need to configure MATCH with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 to look and locate dates that fall _between_ two dates. In addition, we need to assemble the date fragments into actual dates, using the year from the given birthdate.

This approach works for all zodiac signs except one, Capricorn, which crosses the "new year" boundary, and means that the "between" logic will fail and never return TRUE. We could easily solve this problem by splitting the Capricorn entry into two rows with separate date ranges – one from December 22 to December 31; one for January 1 to January 19. But I didn't want to do that, since it would mess up the clean, "human-readable" lookup table. 

I tried a number of tricky options to work around this problem, including shifting all dates back three months so that they fit into one year. But the complexity of these approaches bothered me (and made the formula more opaque), so in the end, I cheated by catching the #N/A error returned by MATCH in the Capricorn date range, and returning row 10, hardcoded. In other words, if a date throws an error, it must be Capricorn.

This should work fine when a _valid_ birthdate is provided. But it also means that any invalid date will also return Capricorn – if your birthday is "apple," you are Capricorn :) Further down, I explain [a sane alternative that doesn't use the table](https://exceljet.net/formulas/zodiac-sign-lookup#alt_formula)
 as shown.

### The hard way - INDEX and MATCH with table as shown

The goal is to look up the correct zodiac sign for a given birthdate using the existing table as shown (B5:B16). The worksheet includes several [named ranges](https://exceljet.net/glossary/named-range)
 for convenience: **dob** (H5), **sign** (B5:B16), **symbol** (D5:D16), **start** (E5:E15), and **end** (F5:F16). The formula in H7 is:

    =INDEX(sign,IFNA(MATCH(1,(dob>=DATEVALUE(start&", "&YEAR(dob)))*(dob<=DATEVALUE(end&", "&YEAR(dob))),0),10))
    

At the core, this is a pretty standard [INDEX and MATCH formula](https://exceljet.net/articles/index-and-match)
, where the [MATCH function](https://exceljet.net/functions/match-function)
 is configured to look for a "1" and the array is constructed with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Taking out that logic, we have:

    =INDEX(sign,IFNA(MATCH(1,array,0),10))
    

The tricky part is in constructing the _array_, which is done with this expression:

    (dob>=DATEVALUE(start&", "&YEAR(dob)))*(dob<=DATEVALUE(end&", "&YEAR(dob)))
    

On the left, we check for a **dob** (date of birth) greater than or equal to the start:

    (dob>=DATEVALUE(start&", "&YEAR(dob))) // check start
    

On the right, we check for a **dob** less than or equal to end:

    (dob<=DATEVALUE(end&", "&YEAR(dob)) // check end
    

The two expressions are joined with the multiplication [operator](https://exceljet.net/glossary/math-operators)
 (\*), since [multiplication corresponds with AND logic in Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
.

Inside each expression, we [concatenate](https://exceljet.net/glossary/concatenation)
 a date fragment from the table with the year from the birthdate, extracted with the [YEAR function](https://exceljet.net/functions/year-function)
. Then we pass the result into the [DATEVALUE function](https://exceljet.net/functions/datevalue-function)
 to get a [valid Excel date](https://exceljet.net/glossary/excel-date)
. Because the named ranges "start" and "end" contain multiple values, the expressions above generate multiple results. With April 26, 1971 as the date of birth in H5, we get:

    (dob>={26013;26043;26074;26105;26137;26168;26199;26229;26259;26289;25953;25983})*(dob<={26042;26073;26104;26136;26167;26198;26228;26258;26288;25952;25982;26012})
    

Then:

    ({TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;TRUE;TRUE})*({FALSE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE})
    

Then:

    {0;1;0;0;0;0;0;0;0;0;0;0}
    

We can now simplify the original formula to:

    =INDEX(sign,IFNA(MATCH(1,{0;1;0;0;0;0;0;0;0;0;0;0},0),10))
    

The [MATCH function](https://exceljet.net/functions/match-function)
 then returns "2" and, since "2" is not an error, we have:

    =INDEX(sign,2) // returns Taurus
    

And the [INDEX function](https://exceljet.net/functions/index-function)
 returns the second item in **sign**: "Taurus" as a final result. In the event that the birthdate falls between December 22 and January 19, the "between two dates" logic will fail and MATCH will throw a #N/A error. The [IFNA function](https://exceljet.net/functions/ifna-function)
 will catch this error and return "10," and INDEX will return "Capricorn," the tenth item in **sign** (B5:B16).

As an alternative, the IFNA function or [IFERROR function](https://exceljet.net/functions/iferror-function)
 could be used at the _outer_ level of the formula as well. However, I wanted the two formulas (see symbol lookup below) to be identical, except for the lookup array passed into INDEX, and I also wanted to retrieve the actual values in the table for Capricorn.

### Retrieving the symbol

The formula in H8 to retrieve the symbol from the named range **symbol** (D5:D16), is almost identical to the original formula. The only difference is the array provided to INDEX, which is **symbol** instead of **sign**:

    =INDEX(symbol,IFNA(MATCH(1,(dob>=DATEVALUE(start&", "&YEAR(dob)))*(dob<=DATEVALUE(end&", "&YEAR(dob))),0),10))
    

The symbols in the table are created with the [UNICHAR function](https://exceljet.net/functions/unichar-function)
, introduced in Excel 2013. They start at 9800, and end at 9811:

    =UNICHAR(9800) // Aries
    =UNICHAR(9811) // Pisces
    

In [Excel 365](https://exceljet.net/glossary/excel-365)
, you can generate all symbols at once using the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
 like this:

    =UNICHAR(SEQUENCE(12,1,9800)) // all 12 symbols
    

### An easier way - VLOOKUP with an embedded table

The INDEX and MATCH formula above is based on a requirement to use the lookup table in B5:B16 as shown. If you don't need or want to show the lookup table, and if you don't mind a lookup table with two entries for Capricorn, you can use a formula based on the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
:

    =VLOOKUP(--TEXT(dob,"m.dd"),{1.01,"Capricorn";1.2,"Aquarius";2.19,"Pisces";3.21,"Aries";4.2,"Taurus";5.21,"Gemini";6.21,"Cancer";7.23,"Leo";8.23,"Virgo";9.23,"Libra";10.23,"Scorpio";11.22,"Sagittarius";12.22,"Capricorn"},2,1)
    

At the core, this is a straightforward VLOOKUP formula:

    =VLOOKUP(--TEXT(dob,"m.dd"),table_array,2,1)
    

where the _table\_array_ argument is supplied as a [hard-coded](https://exceljet.net/formulas/self-contained-vlookup)
 [array constant](https://exceljet.net/glossary/array-constant)
. If we put these values into cells, we have a table like this:

![Zodiac array constant](https://exceljet.net/sites/default/files/images/formulas/inline/zodiac%20array%20constant.png "Zodiac array constant")

Note that the values in the first column are actual decimal numbers. Also note that Capricorn appears _twice_, and entries are in _ascending_ order.

To look up a birthdate, we need a similar number, and for that, we use the [TEXT function](https://exceljet.net/functions/text-function)
 like this:

    --TEXT(dob,"m.dd") // returns 4.26
    

Text pulls the "month" number and "day" number out of the date as text. The [double negative](https://exceljet.net/glossary/double-unary)
 (--) then coerces the text to a number in the same format as the lookup table above. The result for April 26, 1971 is 4.26.

_Note: I ran into this approach in [a post on the MrExcel board, by the always amazing Aladin Akyurek](https://www.mrexcel.com/board/threads/formula-to-determine-the-zodiac-sign.55815/post-259604)
._

Related formulas
----------------

[![Excel formula: Self-contained VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/self-contained%20VLOOKUP%20formula2.png "Excel formula: Self-contained VLOOKUP")](https://exceljet.net/formulas/self-contained-vlookup)

### [Self-contained VLOOKUP](https://exceljet.net/formulas/self-contained-vlookup)

The goal in this example is to create a self-contained lookup formula to assign a grade to the score in cell E7, based on the table in B6:C10. However, instead of providing B6:B10 as a reference for the table\_array argument, the table is provided as a constant . Normally, the second argument for...

[![Excel formula: INDEX and MATCH with multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX%20and%20MATCH%20with%20multiple%20criteria.png "Excel formula: INDEX and MATCH with multiple criteria")](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

### [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)

This is a more advanced formula. For basics, see How to use INDEX and MATCH . Normally, an INDEX MATCH formula is configured with MATCH set to look through a one-column range and provide a match based on given criteria. Without concatenating values in a helper column , or in the formula itself,...

[![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

### [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people...

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel DATEVALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20datevalue.png "Excel DATEVALUE function")](https://exceljet.net/functions/datevalue-function)

### [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)

The Excel DATEVALUE function converts a date represented as a [text string](https://exceljet.net/glossary/text-value)
 into a [valid Excel date](https://exceljet.net/glossary/excel-date)
. For example, the formula =DATEVALUE("3/10/1975") returns a serial number (27463) in the Excel date system that represents March...

[![Excel IFNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")](https://exceljet.net/functions/ifna-function)

### [IFNA Function](https://exceljet.net/functions/ifna-function)

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result....

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Self-contained VLOOKUP](https://exceljet.net/formulas/self-contained-vlookup)
    
*   [INDEX and MATCH with multiple criteria](https://exceljet.net/formulas/index-and-match-with-multiple-criteria)
    
*   [Sort birthdays by month and day](https://exceljet.net/formulas/sort-birthdays-by-month-and-day)
    
*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [DATEVALUE Function](https://exceljet.net/functions/datevalue-function)
    
*   [IFNA Function](https://exceljet.net/functions/ifna-function)
    
*   [YEAR Function](https://exceljet.net/functions/year-function)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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