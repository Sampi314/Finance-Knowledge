# List sheet names with formula - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/list-sheet-names-with-formula

---

[Skip to main content](https://exceljet.net/formulas/list-sheet-names-with-formula#main-content)

[](https://exceljet.net/formulas/list-sheet-names-with-formula#)

*   [Previous](https://exceljet.net/formulas/list-sheet-index-numbers)
    
*   [Next](https://exceljet.net/formulas/worksheet-name-exists)
    

[Workbook](https://exceljet.net/formulas#Workbook)

List sheet names with formula
=============================

by Dave Bruns · Updated 20 Mar 2024

Related functions 
------------------

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TRANSPOSE](https://exceljet.net/functions/transpose-function)

[INDEX](https://exceljet.net/functions/index-function)

[MID](https://exceljet.net/functions/mid-function)

[ROW](https://exceljet.net/functions/row-function)

[NOW](https://exceljet.net/functions/now-function)

[T](https://exceljet.net/functions/t-function)

![Excel formula: List sheet names with formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/List_sheet_names_with_formula_0.png "Excel formula: List sheet names with formula")

Summary
-------

To list worksheets in an Excel workbook with a formula, you can use a 2-step approach: (1) define a [named range](https://exceljet.net/glossary/named-range)
 called "sheetnames" with an old macro command and (2) use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 and the [TRANSPOSE function](https://exceljet.net/functions/transpose-function)
 to retrieve sheet names using the name. In the example shown, the formula in B5 is:

    =TRANSPOSE(TEXTAFTER(sheetnames,"]"))
    

_Notes: (1) In older versions of Excel without the TEXTAFTER function you can use a formula based on INDEX. See below for details (2) This article is about using Excel formulas to return a list of sheet names, but I've included a Power Query solution below as well._

Generic formula
---------------

    =GET.WORKBOOK(1)&T(NOW())

Explanation 
------------

In this example, the goal is to generate a list of the sheet names in an Excel workbook with a formula. Unfortunately, there is no simple way to do this with a formula in Excel. However, it can be done with a two-step approach:

1.  Define a name called "sheetnames" with an old macro command and the Name Manager.
2.  Use the defined name in a formula that extracts the names into the workbook

The article below explains how to follow these steps. It includes a newer dynamic array formula that will return all sheets at once and a more traditional formula that will work in older versions of Excel.

> _This article is about using a formula to return a list of sheet names, but I've included a [Power Query option below](https://exceljet.net/formulas/list-sheet-names-with-formula#power_query_option)
>  as well._

### Step 1: Define the name

The first step is to define a new name. Navigate to the "Formulas" tab and click the "Define Name" button. In the "Name" field, enter "sheetnames". For the "Refers to" field, enter the formula below:

    =GET.WORKBOOK(1)&T(NOW())

_GET.WORKBOOK is part of a set of commands referred to as "Excel 4.0 macros" or "XLM macros," which were introduced with Excel 4 in the early 1990s. These macros provided basic automation in Excel before the introduction of Visual Basic for Applications (VBA) in Excel 5. This is essentially a hack that still works in later versions of Excel. In Excel 365, you might need to enable Excel 4.0 macros in the Trust Center, as explained below._

In the first part of the formula, GET.WORKBOOK(1), retrieves an array of sheet names in the current workbook. In a generic workbook called "workbook.xlsx" with five sheets, the resulting array looks like this:

    {"[workbook.xlsx]Sheet1","[workbook.xlsx]Sheet2","[workbook.xlsx]Sheet3","[workbook.xlsx]Sheet4","[workbook.xlsx]Sheet5"}
    

Next, we [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 a strange expression to the result:

    &T(NOW())
    

_I ran into this approach formula many years ago on the MrExcel message board [in a post by T. Valko](http://www.mrexcel.com/forum/excel-questions/428957-list-worksheet-names-using-formula.html)
._

The purpose of this cryptic code is to trigger a recalculation when the worksheet changes. Since [NOW](https://exceljet.net/functions/now-function)
 is a [volatile function](https://exceljet.net/glossary/volatile-function)
, it will recalculate with each workbook change, like, for example, when a sheet is renamed. NOW returns a number indicating time in Excel, and the [T function](https://exceljet.net/functions/t-function)
 translates the number into an empty string (""). As a result, this part of the formula does not affect the output from GET.WORKBOOK; it is simply used to trigger recalculation.

_Notes: (1) Because this step relies on a macro command, you'll need to save the file as a macro-enabled workbook (.xlsm) to allow the formula to update sheet names after the file is closed and re-opened. If you save the file as a normal worksheet (.xlsx), the sheetname code will be removed. (2) In newer versions of Excel, you may encounter a #BLOCKED error even after taking these steps. [See below for a fix](https://exceljet.net/formulas/list-sheet-names-with-formula#clear_blocked_error)
._ 

### Step 2: enter a formula to retrieve sheet names

The second step in the process is to enter a formula that will retrieve the individual sheet names from the previously defined "sheetnames". In a modern version of Excel that provides [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 and offers the TEXTAFTER function, you can use a formula like this to retrieve all sheet names in one step:

    =TRANSPOSE(TEXTAFTER(sheetnames,"]"))

The TEXTAFTER function extracts just the sheet name from the full workbook path. The TRANSPOSE function converts the original _horizontal array_ into a _vertical array_. The individual sheet names land in cell B5 and [spill](https://exceljet.net/glossary/spill)
 onto the worksheet. Done.

If you are using an older version of Excel without TEXTAFTER, see the next section.

### Legacy formula

If you have an older version of Excel that does not support dynamic arrays, you will need to use a more traditional formula like this:

    =INDEX(MID(sheetnames,FIND("]",sheetnames)+1,31),ROWS($B$5:B5))
    

Working from the inside out, the MID function is configured to extract each sheet name from the array returned by GET.WORKBOOK like this:

    MID(sheetnames,FIND("]",sheetnames)+31)

The _text_ argument is provided as _sheetnames_, which is the defined name created above. The value in sheetnames is an array like this:

    {"[workbook.xlsx]Sheet1","[workbook.xlsx]Sheet2","[workbook.xlsx]Sheet3","[workbook.xlsx]Sheet4","[workbook.xlsx]Sheet5"}
    

The _start\_num_ argument is determined with the [FIND function](https://exceljet.net/functions/find-function)
 here:

    FIND("]",sheetnames)+1

The FIND function locates the closing square bracket "\]" in sheetnames, which appears right after the workbook name. The result is a number that indicates the position of this bracket. We add 1 because we want to start extracting the sheet name _after_ the closing bracket. The value for _num\_chars_ is hardcoded as 31 to keep things simple. When _num\_chars_ exceeds the length of the text following the start number, MID returns _all remaining text_. Since sheet names cannot be longer than 31 characters, this ensures that we get the entire sheet name. The result from MID is an array like this:

    {"Sheet1","Sheet2","Sheet3","Sheet4","Sheet5"}
    

At this point, we have the sheet names ready to go, we just need to get them onto the worksheet. We do this with the INDEX function. The array is delivered to INDEX as the _array_ argument. The value for _row\_num_ is provided by the ROW function like this:

    ROWS($B$5:B5)

The ROW function uses an [expanding reference](https://exceljet.net/glossary/expanding-reference)
 to generate an incrementing row number — as the formula is copied down, ROWS will return 1, then 2, then 3, etc. This allows INDEX to retrieve the next sheet name from the array at each new row. Copy the formula down until all sheet names are listed. When there are no more sheet names to output, the formula will return a #REF error. 

_Note: close observers will notice that we are asking INDEX for specific rows, even though the array is horizontal and has one row only. INDEX is clever this way_ — _it knows what you want :)_

### Clearing a #BLOCKED error

In newer versions of Excel, you may run into a #BLOCKED error even after saving the file in .xlsm format and enabling VBA Macros. The error looks like this:

![#BLOCKED error with XLM macros](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/List_sheet_names_with_formula_blocked_error.png "#BLOCKED error with XLM macros")

The problem occurs because a Trust Center setting called "Enable Excel 4.0 macros when VBA macros are enabled" in Excel 365 is _disabled by default:_

![Enable Excel 4.0 macros in Trust Center](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/List_sheet_names_with_formula_trust_center_settings.png "Enable Excel 4.0 macros in Trust Center")

To open the Trust Center, navigate to File > Options > Trust Center, then click the "Trust Center Settings" button. To clear the blocked error, you will need to enable this setting. Check the checkbox and reopen the file. This time, when you are prompted to enable VBA macros the #BLOCKED error should be cleared.

### List sheet names with Power Query

If you find the Macro-based solution above complex and underwhelming, there is another way to list sheet names in Excel: Power Query. Power Query is a heavy-duty data transformation tool, so this is a little like using a sledgehammer to crack a nut, but it works well. Below is a summary of the steps to list all Sheet names with Power Query. Don't be discouraged by the number of steps, you can do this in less than 2 minutes:

1.  Place your cursor in the cell where you want to list sheet names.
2.  Navigate to Data > Get Data > From File > From Excel Workbook.
3.  Select the current Excel workbook.
4.  Select any sheet name, then click the "Transform Data" button.
5.  Under Properties > Name, enter "List sheet names"
6.  Under Applied Steps, remove all steps except Source
7.  In the Kind column, filter to select "Sheet" only.
8.  Right-click the Name column and select "Remove other columns".
9.  Click "Close & Load" then select "Close & Load to"
10.  Select "Existing worksheet" and click "OK"

The sheet names will be delivered to the cell you selected in step #1 in an [Excel table](https://exceljet.net/articles/excel-tables)
.

One disadvantage to the Power Query solution is that you must _manually_ refresh the query if sheet names change — the list of sheet names won't automatically update. To refresh results, first save the workbook. Then Right-click the table and select "Refresh". One nice benefit of the Power Query approach is that you can easily exclude a sheet from the list. To exclude a specific sheet, click the filter button in the Name column after step #7 above then deselect the sheet(s) you want to exclude.

_Notes: Power Query is built-in to Excel 2016 and later on Windows and is available as a free add-in for Excel 2010 and 2013. On the Mac, Power Query is available in Excel 365 but the feature set is more limited. The example above does work in a current version of Excel 365 on a Mac._

Related formulas
----------------

[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)

### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)

In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...

[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)

### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...

[![Excel formula: Count errors in all sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_errors_in_all_sheets.png "Excel formula: Count errors in all sheets")](https://exceljet.net/formulas/count-errors-in-all-sheets)

### [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)

In this example, the goal is to count errors in a workbook by sheet, where the sheet names have been previously entered in a column as shown. This is a tricky problem in Excel for a couple of reasons. First, there is no direct way to generate a list of sheets in a workbook with a formula. Second,...

Related functions
-----------------

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel TRANSPOSE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_transpose.png "Excel TRANSPOSE function")](https://exceljet.net/functions/transpose-function)

### [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)

The Excel TRANSPOSE function "flips" the orientation of a given range or array: TRANSPOSE flips a vertical range to a horizontal range, and flips a horizontal range to a vertical range.

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel ROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20row%20function.png "Excel ROW function")](https://exceljet.net/functions/row-function)

### [ROW Function](https://exceljet.net/functions/row-function)

The Excel ROW function returns the row number for a reference. For example, ROW(C5) returns 5, since C5 is the fifth row in the spreadsheet. When no reference is provided, ROW returns the row number of the cell which contains the formula.

[![Excel NOW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20now%20function.png "Excel NOW function")](https://exceljet.net/functions/now-function)

### [NOW Function](https://exceljet.net/functions/now-function)

The Excel NOW function returns the current date and time, updated continuously when a worksheet is changed or opened. The NOW function takes no arguments. You can format the value returned by NOW as a date, or as a date with time by applying a [number format](https://exceljet.net/glossary/number-format)
...

[![Excel T function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20t%20function.png "Excel T function")](https://exceljet.net/functions/t-function)

### [T Function](https://exceljet.net/functions/t-function)

The Excel T function returns text when given a text value and an empty string ("") for numbers, dates, and the logical values TRUE and FALSE. You can use the T function to remove values that are not text.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)
    
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)
    

### Functions

*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [TRANSPOSE Function](https://exceljet.net/functions/transpose-function)
    
*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [ROW Function](https://exceljet.net/functions/row-function)
    
*   [NOW Function](https://exceljet.net/functions/now-function)
    
*   [T Function](https://exceljet.net/functions/t-function)
    

### Links

*   [Mr. Excel forum post by T. Valko](https://www.mrexcel.com/forum/excel-questions/428957-list-worksheet-names-using-formula.html)
    

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