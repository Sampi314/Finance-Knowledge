# Get workbook name and path without sheet - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet

---

[Skip to main content](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet#main-content)

[](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet#)

*   [Previous](https://exceljet.net/formulas/get-sheet-name-only)
    
*   [Next](https://exceljet.net/formulas/get-workbook-name-only)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Get workbook name and path without sheet
========================================

by Dave Bruns · Updated 16 Dec 2022

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[LET](https://exceljet.net/functions/let-function)

![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")

Summary
-------

To get a path to the current workbook, you can use a formula based on the [CELL function](https://exceljet.net/functions/cell-function)
, the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
, and the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. In the example shown, the formula in E5 is:

    =SUBSTITUTE(TEXTBEFORE(CELL("filename",A1),"]"),"[","")\
\
The result is a path and filename like this: "C:\\examples\\workbook.xlsx". The sheet name and the square brackets ("\[ \]") that normally enclose the file name have been removed.\
\
Generic formula\
---------------\
\
    =SUBSTITUTE(TEXTBEFORE(CELL("filename",A1),"]"),"[","")\
\
Explanation \
------------\
\
In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)\
. In older versions of Excel, you can use a more complicated formula based on the [LEFT](https://exceljet.net/functions/left-function)\
 and [FIND](https://exceljet.net/functions/find-function)\
 functions. Both options use the [CELL function](https://exceljet.net/functions/cell-function)\
 to get a full path to the current workbook. Read below for a full explanation.\
\
### Get workbook path\
\
The first step in this problem is to get the workbook path, which includes the workbook and worksheet name. This can be done with the [CELL function](https://exceljet.net/functions/cell-function)\
 like this:\
\
    CELL("filename",A1)\
    \
\
With the _info\_type_ [argument](https://exceljet.net/glossary/function-argument)\
 set to "filename", and _reference_ set to cell A1 in the current worksheet, the result from CELL will be a full path as a text string like this:\
\
    "C:\path\to\folder\[workbook.xlsx]sheetname"\
    \
\
Notice the workbook name is enclosed in square brackets ("\[name\]"). This is close to what we want, but there are still two tasks that remain:\
\
1.  Remove the sheet name\
2.  Remove the square brackets ("\[ \]")\
\
The best way to do this depends on what Excel version you have. If you have the latest version of Excel, you should use a formula based on the TEXTBEFORE function. Otherwise, you can use the LEFT and FIND functions as explained below.\
\
### TEXTBEFORE option\
\
In the worksheet shown above, the formula in E5 is:\
\
    =SUBSTITUTE(TEXTBEFORE(CELL("filename",A1),"]"),"[","")\
\
This is an example of [nesting](https://exceljet.net/glossary/nesting)\
. The CELL function is nested inside the TEXTBEFORE function, which is nested inside the SUBSTITUTE function. Working from the inside out:\
\
1.  The CELL function returns the full path as a text string, as explained above.\
2.  The TEXTBEFORE function returns all text _before_ the closing square bracket ("\]").
3.  The SUBSTITUTE function replaces the opening square bracket ("\[") with an empty string ("").\
\
The final result is a path to the workbook like this:\
\
    C:\path\to\folder\workbook.xlsx\
\
### Legacy Excel\
\
In older versions of Excel without the TEXTBEFORE function, you can use a formula based on LEFT, CELL, FIND, and SUBSTITUTE:\
\
    =SUBSTITUTE(LEFT(CELL("filename",A1),FIND("]",CELL("filename",A1))-1),"[","")\
    \
\
At a high level, this formula works in 4 steps:\
\
1.  Get the full path and filename\
2.  Locate the closing square bracket ("\]")
3.  Remove sheet name and "\]"
4.  Remove the opening square bracket ("\]")

_Note: the CELL function is called twice in the formula because we need the path twice, once for the FIND function to locate the "\]", and once for the SUBSTITUTE function to remove the "\]". CELL is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can cause performance problems in larger or more complicated worksheets._ 

### Get path and filename

To get the path and file name, we use the [CELL function](https://exceljet.net/functions/cell-function)
 like this:

    CELL("filename",A1) // get path and filename
    

The _info\_type_ argument is "filename" and _reference_ is A1. The cell reference is arbitrary and can be any cell in the worksheet. The result is a full path like this as text:

    C:\examples\[workbook.xlsx]Sheet1

Note the sheet name("Sheet1") appears at the end.

### Locate the closing square bracket

The location of the closing square bracket ("\]") is calculated like this

    FIND("]",CELL("filename",A1))-1 // returns 26
    

The [FIND function](https://exceljet.net/functions/find-function)
 returns the location of "\]" (27) from which 1 is subtracted to get 26. We subtract 1 because we want to remove text _starting with_ the "\]" that follows the filename. 

### Remove sheet name

In the previous step, we located the "\]" at character 27, then stepped back to 26. This number is returned directly to the [LEFT function](https://exceljet.net/functions/left-function)
 as the _num\_chars_ argument. The _text_ argument is again provided by the [CELL function](https://exceljet.net/functions/cell-function)
:

    LEFT("C:\examples\[workbook.xlsx]Sheet1",26)
    

The [LEFT function](https://exceljet.net/functions/left-function)
 returns the first 26 characters of _text_.

    C:\examples\[workbook.xlsx\
    \
\
At this point, LEFT has removed the sheet name, but notice the opening square bracket "\[" remains.\
\
### Remove opening square bracket\
\
The result from LEFT is returned to the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)\
 as the _text_ argument:\
\
    =SUBSTITUTE("C:\examples\[workbook.xlsx","[","")\
    \
\
SUBSTITUTE is configured to remove the opening square bracket by setting _old\_text_ to "\[" and _new\_text_ to an [empty string](https://exceljet.net/glossary/empty-string)\
 (""). The final result returned by SUBSTITUTE is:\
\
    C:\examples\workbook.xlsx\
    \
\
Related formulas\
----------------\
\
[![Excel formula: Get full workbook name and path](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workbook%20name%20and%20path_0.png "Excel formula: Get full workbook name and path")](https://exceljet.net/formulas/get-full-workbook-name-and-path)\
\
### [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)\
\
The CELL function can return various information about a worksheet. CELL can get things like address and filename, as well as information about the formatting used in the cell. The type of information to be returned is specified by the info\_type argument . In this example, we want the path, name,...\
\
Related functions\
-----------------\
\
[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)\
\
### [CELL Function](https://exceljet.net/functions/cell-function)\
\
The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...\
\
[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)\
\
### [LEFT Function](https://exceljet.net/functions/left-function)\
\
The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".\
\
[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)\
\
### [FIND Function](https://exceljet.net/functions/find-function)\
\
The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.\
\
[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)\
\
### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)\
\
The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....\
\
[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)\
\
### [LET Function](https://exceljet.net/functions/let-function)\
\
The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....\
\
Was this page helpful? Yes No Report a problem\
\
Cancel Submit\
\
![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)\
\
Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)\
\
### Dave Bruns\
\
Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.\
\
Related Information\
-------------------\
\
### Formulas\
\
*   [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)\
    \
\
### Functions\
\
*   [CELL Function](https://exceljet.net/functions/cell-function)\
    \
*   [LEFT Function](https://exceljet.net/functions/left-function)\
    \
*   [FIND Function](https://exceljet.net/functions/find-function)\
    \
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)\
    \
*   [LET Function](https://exceljet.net/functions/let-function)\
    \
\
### Links\
\
*   [Excel file and formula name formulas (Chip Pearson)](http://www.cpearson.com/excel/FileFolderNames.aspx)\
    \
\
### Training\
\
*   [Core Formula](https://exceljet.net/training/core-formula)\
    \
\
Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!\
\
Thierry\
\
[More Testimonials](https://exceljet.net/feedback)\
\
Get [Training](https://exceljet.net/training)\
\
----------------------------------------------\
\
### Quick, clean, and to the point training\
\
Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.\
\
[View Paid Training & Bundles](https://exceljet.net/training)\
\
[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)\
\
[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)\
\
[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)\
\
[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)\
\
[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)\
\
[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)