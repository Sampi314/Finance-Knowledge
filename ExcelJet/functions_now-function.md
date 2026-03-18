# Excel NOW function | Exceljet

**Source:** https://exceljet.net/functions/now-function

---

[Skip to main content](https://exceljet.net/functions/now-function#main-content)

[](https://exceljet.net/functions/now-function#)

*   [Previous](https://exceljet.net/functions/networkdays.intl-function)
    
*   [Next](https://exceljet.net/functions/second-function)
    

Excel 2003

[Date and time](https://exceljet.net/functions#Date-and-time)

NOW Function
============

by Dave Bruns · Updated 22 Jun 2024

Related functions 
------------------

[TODAY](https://exceljet.net/functions/today-function)

[TEXT](https://exceljet.net/functions/text-function)

![Excel NOW function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20now%20function.png "Excel NOW function")

Summary
-------

The Excel NOW function returns the current date and time, updated continuously when a worksheet is changed or opened. The NOW function takes no arguments. You can format the value returned by NOW as a date, or as a date with time by applying a [number format](https://exceljet.net/glossary/number-format)
.

Purpose 
--------

Get the current date and time

Return value 
-------------

A number representing the current date and time in Excel.

Syntax
------

    =NOW()

Using the NOW function 
-----------------------

NOW takes no parameters but requires empty parentheses. The value returned by NOW will continually update each time the worksheet is updated, for example, each time a value is entered or changed. Use F9 to force the worksheet to recalculate and update the value.

The value returned by the NOW function is a standard [Excel date](https://exceljet.net/glossary/excel-date)
, including a [fractional value for time](https://exceljet.net/glossary/excel-time)
. To display the result as a date, apply a date [number format](https://exceljet.net/glossary/number-format)
. Optionally, [customize the number format](https://exceljet.net/articles/custom-number-formats)
 to include the time. If you want the current date without a time value, use the [TODAY function](https://exceljet.net/functions/today-function)
.

### The NOW function explained

The NOW function returns the current date and time according to the settings on your computer. As I write this, the date is June 22, 2024, and it's just after 10 AM in the morning. When I enter the formula below in cell A1, it returns the decimal number shown below:

    =NOW() // returns 45465.42441
    

_To see the number returned by NOW, apply the General number format (Control + ~)._

The integer part of the number (45465) is the date (June 22, 2024), and the decimal part of the number (0.42441) is the time (about 10:11 AM). Note that you will need to apply a [number format](https://exceljet.net/glossary/number-format)
 to display the date and/or time as required. After working for a few minutes in Excel, NOW returns a new result:

    =NOW() // returns 45465.42721
    
    

Notice the number has increased slightly. The date (45465) is the same (June 22, 2024), but the time (0.42721) is now about 10:15 AM. The NOW function will continue to update this value each time the worksheet is changed, saved, or opened. To display the number returned by NOW as a date and/or time, you will need to [apply a suitable number format](https://exceljet.net/videos/how-to-create-a-custom-date-format)
. Here are three examples:

    "d-mmm-yyyy" // a date like "22-Jun-2024"
    "h:mm" // a time like "10:15"
    "m/d/yyyy h:mm" // a date and time like "6/22/2024 10:15"

_Note: the NOW function returns the current date and time. The similar [TODAY function](https://exceljet.net/functions/today-function)
 returns just the current date._

### Example - basic usage

The examples below show how the NOW function can be used in various ways:

    =NOW()  // current date and time
    =NOW()-7  // last week same time
    =NOW()+7  // next week same time
    =NOW()+90  // 90 days from now
    =MROUND(NOW()+90,"1:00")  // 90 days from now to nearest hour
    =EDATE(NOW(),3)  // 3 months from now, time removed
    =EDATE(NOW(),12)  // 12 months from now, time removed
    =EOMONTH(NOW(),-1)+1  // first day of current month
    =EDATE(NOW(),6)+MOD(NOW(),6)  // 6 months from now, time preserved
    

### Current time without a date

The NOW function returns the current date and time. However, in some cases, you may want to return only the current time. You can do this by adding the [MOD function](https://exceljet.net/functions/mod-function)
 as shown below:

    =MOD(NOW(),1)

The MOD function returns the remainder after division. The first argument is the number, and the second is the divisor. By using a divisor of 1, the remainder will be the decimal part of the number since every whole number can be evenly divided by itself.

### Hours and minutes before a specific time

Why would you want to remove the date? One example is the problem of displaying the hours and minutes that remain before a specific time of the day. For example, the formula below will display the time that remains before 6:00 PM:

    ="18:00"-MOD(NOW(),1)

Without removing the date, the value from NOW would always be larger than the time "18:00" which would create a negative number. Excel does not support negative time values and will instead display a string of hash characters like "######". Of course, the result from the formula above will turn negative when the current time has passed 6:00 PM. To force negative values to zero, you can add the [MAX function](https://exceljet.net/functions/max-function)
 like this:

    =MAX("18:00"-MOD(NOW(),1),0)

Here, the MAX function is a clever way to avoid an IF statement. If the time remaining is positive, MAX will return that value. If the time that remains is negative, MAX will return zero. To see hours and minutes, format the result with the number format like "h:mm".

### Static date and time

If you need a static date and time that won't change,  you can use the following shortcuts:

*   [Insert current date](https://exceljet.net/shortcuts/insert-current-date)
     - Control + ;
*   [Insert current time](https://exceljet.net/shortcuts/insert-current-time)
     - Control + Shift + :

To enter both values in a single cell, enter the date, a space, and then the time.

### Formatting results

The result of NOW is a serial number representing an [Excel date](https://exceljet.net/glossary/excel-date)
 and [time](https://exceljet.net/glossary/excel-time)
. You can format the value returned by TODAY using any standard date [format](https://exceljet.net/glossary/number-format)
. You can use the [TEXT function](https://exceljet.net/functions/text-function)
 to build a text message that includes the current date:

    ="The date is "&TEXT(NOW(),"mmm d")&" and the time is "&TEXT(NOW(),"h:mm AM/PM")
    

To return a text string like "The date is May 31 and the time is 6:10 PM".

NOW function examples
---------------------

[![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")](https://exceljet.net/formulas/list-sheet-names-with-formula)

### [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach: Define a name called "sheetnames" with an old macro command and the...

[![Excel formula: Display the current date and time](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/display%20current%20date%20and%20time.png "Excel formula: Display the current date and time")](https://exceljet.net/formulas/display-the-current-date-and-time)

### [Display the current date and time](https://exceljet.net/formulas/display-the-current-date-and-time)

The NOW function takes no arguments; it is entered with empty parentheses. When you enter the NOW function in a cell, it will display the current date and time. Each time the worksheet is recalculated or opened, the date and time will be updated. To display only the time component, format the cell...

NOW function videos
-------------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20display%20current%20date%20and%20time-thumb.png)](https://exceljet.net/videos/how-to-display-current-date-and-time)

### [How to display current date and time](https://exceljet.net/videos/how-to-display-current-date-and-time)

In this video we look at several ways to handle current dates and times. You may often want to enter a current date and time into a worksheet. A simple way to do this is to enter a time or date stamp. You can do this using keyboard shortcuts. Control semicolon enters the current date. Control-Shift...

Related functions
-----------------

[![Excel TODAY function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20today%20function.png "Excel TODAY function")](https://exceljet.net/functions/today-function)

### [TODAY Function](https://exceljet.net/functions/today-function)

The Excel TODAY function returns the current date, updated continuously when a worksheet is changed or opened. The TODAY function takes no arguments. You can format the value returned by TODAY with a date [number format](https://exceljet.net/glossary/number-format)
. If you need current date and time, use...

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

*   [Display the current date and time](https://exceljet.net/formulas/display-the-current-date-and-time)
    
*   [List sheet names with formula](https://exceljet.net/formulas/list-sheet-names-with-formula)
    

### Videos

*   [How to display current date and time](https://exceljet.net/videos/how-to-display-current-date-and-time)
    

### Functions

*   [TODAY Function](https://exceljet.net/functions/today-function)
    
*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Links

*   [Microsoft NOW function documentation](https://support.office.com/en-us/article/now-function-3337fd29-145a-4347-b2e6-20c904739c46)
    

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