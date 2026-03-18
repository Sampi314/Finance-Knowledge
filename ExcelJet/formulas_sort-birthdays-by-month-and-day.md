# Sort birthdays by month and day - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-birthdays-by-month-and-day

---

[Skip to main content](https://exceljet.net/formulas/sort-birthdays-by-month-and-day#main-content)

[](https://exceljet.net/formulas/sort-birthdays-by-month-and-day#)

*   [Previous](https://exceljet.net/formulas/remove-blank-rows)
    
*   [Next](https://exceljet.net/formulas/sort-by-custom-list)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Sort birthdays by month and day
===============================

by Dave Bruns · Updated 4 Oct 2023

Related functions 
------------------

[SORTBY](https://exceljet.net/functions/sortby-function)

[TEXT](https://exceljet.net/functions/text-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6562/download?token=BpZJGLyh)
 (14.97 KB)

![Excel formula: Sort birthdays by month and day](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Sort%20birthdays%20by%20month%20and%20day.png "Excel formula: Sort birthdays by month and day")

Summary
-------

To sort a list of birthdays that include the year of birth by month and day, you can use a formula based on the [SORTBY function](https://exceljet.net/functions/sortby-function)
 together with the [TEXT function](https://exceljet.net/functions/text-function)
. In the example shown, the formula in E5 is:

    =SORTBY(data,TEXT(birthdays,"mmdd"))
    

where **data** (B5:C16) and **birthdays** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
. The result is the list of birthdays sorted by month and day, ignoring year.

_Note: the SORTBY function is [new in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. Below, I explain how to use a helper column to sort birthdays by month and day._

Explanation 
------------

In this example, the goal is to sort a list of names and birthdays by month and year. The complication is that the birthdays also include a birth year, so if we try to sort the raw data by birthdays, we'll end up with a list of birthdays sorted first by year. We will actually see the oldest people in the list first, because [Excel dates are actually serial numbers](https://exceljet.net/glossary/excel-date)
 that increase over time.

To sort the data by month and then by day, ignoring year, we need to construct another [array](https://exceljet.net/glossary/array)
 in memory that we can use for sorting. This is done with the TEXT function, which we use to extract the month and day. In the example shown, the formula in E5 is:

    =SORTBY(data,TEXT(birthdays,"mmdd"))
    

where **data** (B5:C16) and **birthdays** (C5:C16) are [named ranges](https://exceljet.net/glossary/named-range)
.

The [SORTBY function](https://exceljet.net/functions/sortby-function)
 can sort by one or more arrays. One of the benefits the [SORTBY function](https://exceljet.net/functions/sortby-function)
 provides over the [SORT function](https://exceljet.net/functions/sort-function)
 is the ability to sort by an array that is _not part of the data_. For the _array_ argument, we provide the full set of **data** (B5:C16). For the _sort\_by_ argument, we use the TEXT function like this:

    TEXT(birthdays,"mmdd")
    

The [TEXT function](https://exceljet.net/functions/text-function)
 is a way to convert a numeric value to a text value using a specific [number format](https://exceljet.net/glossary/number-format)
. In this case, the number format is "mmdd", which translates to a 2-digit month, followed by a 2-digit day (i.e. "0727" for the date in cell C5).

Because we give the TEXT function the full list of **birthdays** (C5:C16), which contains 12 dates, we get back 12 results in an [array](https://exceljet.net/glossary/array)
 like this:

    {"0727";"1025";"0116";"0425";"1126";"0203";"0826";"0907";"0512";"0323";"0607";"1210"}
    

Notice these values are actually [text values](https://exceljet.net/glossary/text-value)
 (not numbers) but they work fine for the purpose of sorting in this case.

With this configuration, the SORTBY function returns all data sorted by the array returned by the TEXT function, and results [spill](https://exceljet.net/glossary/spill)
 into the range E5:F16, as seen in the example. Notice names and birthdays are now sorted by month, then by day. In other words, the birthdays are sorted in the order they will occur throughout the year.

### Numeric sort variation

The formula explained above is based on creating text values that can be used for sorting. For the purposes of this example, this works fine. However, there are times where you might [want or need a numeric sort option](https://exceljet.net/formulas/list-upcoming-birthdays)
. In that case, you can use a variation like this:

    =SORTBY(data,--TEXT(birthdays,"m.dd"))
    

The structure of this formula is the same as the formula above. However, the TEXT function is configured like this:

    --TEXT(birthdays,"m.dd")
    

The number format "m.dd" will return a value like "7.27" for July 27, and "7.04" for July 4. We then use a [double negative](https://exceljet.net/glossary/double-unary)
 (--) to coerce the text value into a true number, which the SORTBY function uses to sort the data with the same result.

### Older Excel versions

Because the SORTBY function is [new in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you won't find it in other Excel versions. In that case, the easiest way to solve this problem is to add a [helper column](https://exceljet.net/glossary/helper-column)
 to the original table with a formula like this, starting in cell D5:

    =TEXT(C5,"mmdd")
    

Copy the formula down the table and name the helper column "Helper" in cell D4. Now you can use the "Helper" column to sort the table manually by month and day. It is possible to sort with a formula as well, but it is [somewhat more complex](https://exceljet.net/formulas/basic-text-sort-formula)
. For more information on dynamic array alternatives, see: [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
.

Related formulas
----------------

[![Excel formula: List upcoming birthdays](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/list%20upcoming%20birthdays.png "Excel formula: List upcoming birthdays")](https://exceljet.net/formulas/list-upcoming-birthdays)

### [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)

In this example, the goal is to list the next n upcoming birthdays from a larger set of 25 birthdays based on the current date. The set of birthdays are in an Excel Table named data in the range B5:C29. In the example shown, we are using 7 for n , so the result will be the next 7 upcoming birthdays...

[![Excel formula: Sort by two columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20by%20two%20columns.png "Excel formula: Sort by two columns")](https://exceljet.net/formulas/sort-by-two-columns)

### [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)

In the example shown, we want to sort data in B5:D14 first by group in descending order. Here is the configuration needed: array = B5:D14 by\_array1 = D5:D14 sort\_order1 = 1 The formula below will sort data by group A-Z: =SORTBY(B5:D14,D5:D14,1) // sort by group only To extend the formula to sort...

[![Excel formula: Random sort](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/random_sort.png "Excel formula: Random sort")](https://exceljet.net/formulas/random-sort)

### [Random sort](https://exceljet.net/formulas/random-sort)

In this example, the goal is to perform a random sort of the data in B5:B16 with a formula. This can be done with the SORTBY function and the RANDARRAY function . SORTBY function The SORTBY function sorts provided values by one or more "sort by" arrays. The sort by arrays make it possible to sort...

[![Excel formula: Sort text by length](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sort%20text%20by%20length.png "Excel formula: Sort text by length")](https://exceljet.net/formulas/sort-text-by-length)

### [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)

The SORTBY function can sort values in a range with an array that doesn't exist on the worksheet. In this example, we want to sort the values in B5:B15 by the number of characters each string contains. Working from inside out, we use the LEN function to get the length of each value: LEN(B5:B15) //...

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

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [List upcoming birthdays](https://exceljet.net/formulas/list-upcoming-birthdays)
    
*   [Sort by two columns](https://exceljet.net/formulas/sort-by-two-columns)
    
*   [Random sort](https://exceljet.net/formulas/random-sort)
    
*   [Sort text by length](https://exceljet.net/formulas/sort-text-by-length)
    
*   [Sort by custom list](https://exceljet.net/formulas/sort-by-custom-list)
    
*   [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)
    

### Functions

*   [SORTBY Function](https://exceljet.net/functions/sortby-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

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