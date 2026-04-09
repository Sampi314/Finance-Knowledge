# Get workbook path only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-workbook-path-only

---

[Skip to main content](https://exceljet.net/formulas/get-workbook-path-only#main-content)

[](https://exceljet.net/formulas/get-workbook-path-only#)

*   [Previous](https://exceljet.net/formulas/get-workbook-name-only)
    
*   [Next](https://exceljet.net/formulas/indirect-named-range-different-sheet)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Get workbook path only
======================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[CELL](https://exceljet.net/functions/cell-function)

[LEFT](https://exceljet.net/functions/left-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get workbook path only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get_workbook_path_only.png "Excel formula: Get workbook path only")

Summary
-------

To get the path to the current workbook _without_ the workbook name, you can use a formula based on the [CELL function](https://exceljet.net/functions/cell-function)
 and the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)
. In the example shown, the formula in E5 is:

    =TEXTBEFORE(CELL("filename",A1),"[")\
    \
\
The result is a path _without_ the filename like this: "C:\\path\\".\
\
_Note: TEXTAFTER is only available in Excel 2021 and later. See below for a formula that works in earlier versions of Excel._\
\
Generic formula\
---------------\
\
    =TEXTBEFORE(CELL("filename",A1),"[")\
\
Explanation \
------------\
\
In this example, the goal is to get the workbook path _without the workbook name_. For example, given a workbook called fruits.xlsx saved to:\
\
    C:\examples\fruits.xlsx\
\
We want the path only like this:\
\
    C:\examples\\
\
### TEXTBEFORE solution\
\
In a modern version of Excel (Excel 2021 or later) the simplest way to solve this problem is to use the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)\
 like this:\
\
    =TEXTBEFORE(CELL("filename",A1),"[")\
\
TEXTBEFORE is designed to return all text before a given delimiter. Working from the inside out, the [CELL function](https://exceljet.net/functions/cell-function)\
 runs first and returns a full path to the workbook and worksheet:\
\
    =CELL("filename",A1)\
    ="C:\examples\[fruits.xlsx]Sheet1"\
\
The result is returned to the TEXTBEFORE function which is configured to return all text before the opening square bracket "\[":\
\
    =TEXTBEFORE("C:\examples\[fruits.xlsx]Sheet1","[")\
    ="C:\examples\"\
\
The final result is the text string "C:\\examples\\".\
\
### Older versions of Excel\
\
In older versions of Excel without the TEXTBEFORE function, we need to use a more complicated formula based on the [LEFT function](https://exceljet.net/functions/left-function)\
 and [FIND function](https://exceljet.net/functions/find-function)\
:\
\
    =LEFT(CELL("filename",A1),FIND("[",CELL("filename",A1))-1)\
    \
\
At a high level, this formula works in 3 steps:\
\
1.  Get the full path and filename with CELL\
2.  Locate the opening square bracket ("\[")\
3.  Extract all text up to the opening square bracket ("\[")\
\
### Get the path and filename\
\
To get the path and file name, we use the [CELL function](https://exceljet.net/functions/cell-function)\
 like this:\
\
    CELL("filename",A1) // get path and filename\
    \
\
The _info\_type_ argument is "filename" and _reference_ is A1. The cell reference is arbitrary and can be any cell in the worksheet. The result is a full path like this as text:\
\
    C:\examples\[workbook.xlsx]Sheet1\
\
Note the sheet name (Sheet1) appears at the end, and the workbook name is enclosed in square brackets, \[workbook.xlsx\].\
\
### Locate the opening square bracket\
\
The location of the opening square bracket ("\[") is calculated with FIND like this\
\
    FIND("]",CELL("filename",A1))-1 // returns 12\
    \
\
The [FIND function](https://exceljet.net/functions/find-function)\
 returns the location of "\[" (13) from which 1 is subtracted to get 12. We subtract 1 because we want to remove all text _starting with_ the "\[" that precedes the workbook name. Or, to put it the other way, we want to _extract_ all text up to the "\[".\
\
### Extract path\
\
In the previous step, we located the "\]" at character 27, then stepped back to 12. This number is returned directly to the [LEFT function](https://exceljet.net/functions/left-function)\
 as the _num\_chars_ argument. The _text_ argument is again provided by the [CELL function](https://exceljet.net/functions/cell-function)\
 as described above:\
\
    =LEFT(CELL("filename",A1),12)\
    =LEFT("C:\examples\[workbook.xlsx]Sheet1",12)\
    \
\
The [LEFT function](https://exceljet.net/functions/left-function)\
 returns the first 12 characters of _text_ as the final result:\
\
    C:\examples\\
    \
\
The final result is the text string "C:\\examples\\".\
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
[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)\
\
### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)\
\
In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...\
\
[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)\
\
### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)\
\
In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...\
\
[![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")](https://exceljet.net/formulas/get-sheet-name-only)\
\
### [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)\
\
In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the TEXTAFTER function . In older versions of Excel, you can use an alternative formula based on the...\
\
[![Excel formula: Dynamic worksheet reference](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/formula%20with%20dynamic%20sheet%20name.png "Excel formula: Dynamic worksheet reference")](https://exceljet.net/formulas/dynamic-worksheet-reference)\
\
### [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)\
\
The INDIRECT function tries to evaluate text as a worksheet reference. This makes it possible to build formulas that assemble a reference as text using concatenation , and use the resulting text as a valid reference. In this example, we have Sheet names in column B, so we join the sheet name to the...\
\
Related functions\
-----------------\
\
[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)\
\
### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)\
\
The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.\
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
*   [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)\
    \
*   [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)\
    \
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)\
    \
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)\
    \
\
### Functions\
\
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)\
    \
*   [CELL Function](https://exceljet.net/functions/cell-function)\
    \
*   [LEFT Function](https://exceljet.net/functions/left-function)\
    \
*   [FIND Function](https://exceljet.net/functions/find-function)\
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