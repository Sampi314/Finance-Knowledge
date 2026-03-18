# Get year from date - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-year-from-date

---

[Skip to main content](https://exceljet.net/formulas/get-year-from-date#main-content)

[](https://exceljet.net/formulas/get-year-from-date#)

*   [Previous](https://exceljet.net/formulas/get-workdays-between-dates)
    
*   [Next](https://exceljet.net/formulas/happy-birthday-message)
    

[Date and Time](https://exceljet.net/formulas#Date-and-Time)

Get year from date
==================

by Dave Bruns · Updated 17 Jan 2026

Related functions 
------------------

[YEAR](https://exceljet.net/functions/year-function)

![Excel formula: Get year from date](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_year_from_date.png "Excel formula: Get year from date")

Summary
-------

To extract the year from a date, you can use the [YEAR function](https://exceljet.net/functions/year-function)
. In the generic form of the formula above, the date must be in a form that Excel recognizes as a valid date. In the worksheet shown, the formula in cell D5 is:

    =YEAR(B5)

As the formula is copied down, YEAR extracts a 4-digit year from each date in column B.

Generic formula
---------------

    =YEAR(date)

Explanation 
------------

In this example, the goal is to extract the year number from a list of dates in column B. This can be easily achieved with the [YEAR function](https://exceljet.net/functions/year-function)
. 

The YEAR function takes just one argument, the date from which you want to extract the year. For example, in the formula below, we pass the "12-Dec-1999" into the YEAR function, which returns 1999:

    =YEAR("12-Dec-1999") // returns 1999

In the worksheet shown, we use a cell reference instead of hard-coding the date. The formula in cell D5 is:

    =YEAR(B5)
    

The result in D5 is 1912 since the date in B5 is 4-Apr-1912. As the formula is copied down, it returns a four-digit year for each date listed in column B. 

### Dates as text

Note that you can use YEAR to extract the year from a day entered as text:

    =YEAR("1/5/2016") // returns 2016
    

However, using text for dates can cause unpredictable results on computers using different regional date settings. In general, a much better approach is to provide a cell reference that already contains a valid date. If YEAR returns a #VALUE error, it means Excel does not recognize the value as a date. For some ways to get Excel to recognize dates, see: [Convert text to date](https://exceljet.net/formulas/convert-text-to-date)
.

### Display year only

In some cases, you may want to enter a date and only display the year. You can accomplish this by applying a [custom number format](https://exceljet.net/articles/custom-number-formats)
 like "yyyy" or "yy" to one or more dates.

Related formulas
----------------

[![Excel formula: Get fiscal year from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20fiscal%20year%20from%20date.png "Excel formula: Get fiscal year from date")](https://exceljet.net/formulas/get-fiscal-year-from-date)

### [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)

In this example, the goal is to return the fiscal year for any given date, where a fiscal year starts in July as seen in the worksheet. By convention a fiscal year is denoted by the year in which it ends. So, if a fiscal year begins in July, then the date August 1, 2018 is in fiscal year 2019. The...

[![Excel formula: Get month from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_month_from_date.png "Excel formula: Get month from date")](https://exceljet.net/formulas/get-month-from-date)

### [Get month from date](https://exceljet.net/formulas/get-month-from-date)

The MONTH function takes just one argument, the date from which to extract the month. In the example shown, the formula is: =MONTH(B4) where B4 contains the date January 5, 2016. The MONTH function returns the number 1 representing the month( January) of the date. Note that you can use MONTH to...

[![Excel formula: Get day from date](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_day_from_date.png "Excel formula: Get day from date")](https://exceljet.net/formulas/get-day-from-date)

### [Get day from date](https://exceljet.net/formulas/get-day-from-date)

The DAY function takes just one argument, the date from which you want to extract the day. In the example, the formula is: =DAY(B5) B5 contains a date value for January 5, 2016. The DAY function returns the number 5 representing the day component of the date. Note that you can use DAY to extract...

Related functions
-----------------

[![Excel YEAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_year_function.png "Excel YEAR function")](https://exceljet.net/functions/year-function)

### [YEAR Function](https://exceljet.net/functions/year-function)

The Excel YEAR function returns the year of a date as a 4-digit number. You can use the YEAR function to extract the year from a date. You can also combine YEAR with other functions to manipulate dates in specific ways, and even to count and sum by year.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20enter%20dates%20in%20Excel-thumb.png)](https://exceljet.net/videos/how-to-enter-dates-in-excel)

### [How to enter dates in Excel](https://exceljet.net/videos/how-to-enter-dates-in-excel)

In this lesson, we'll look at how to enter dates in Excel . To enter a date in Excel, you need to type the date in a format that Excel can recognize. When checking for a date, Excel will look for a month, a day, and a year in a variety of formats. If you don't supply a year, Excel will use the...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_use_date_formatting-thumb.png)](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

### [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)

In this lesson we'll take a look at the Date format. The Date format is flexible and can display the same date in many different ways. Let's take a look. Here we have a set of dates in column B of our table. Let's start off by copying these dates to all columns. Let's look first at the Short Date...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get fiscal year from date](https://exceljet.net/formulas/get-fiscal-year-from-date)
    
*   [Get month from date](https://exceljet.net/formulas/get-month-from-date)
    
*   [Get day from date](https://exceljet.net/formulas/get-day-from-date)
    

### Functions

*   [YEAR Function](https://exceljet.net/functions/year-function)
    

### Videos

*   [How to enter dates in Excel](https://exceljet.net/videos/how-to-enter-dates-in-excel)
    
*   [How to use date formatting in Excel](https://exceljet.net/videos/how-to-use-date-formatting-in-excel)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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