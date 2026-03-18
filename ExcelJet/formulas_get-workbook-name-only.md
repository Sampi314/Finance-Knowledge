# Get workbook name only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-workbook-name-only

---

[Skip to main content](https://exceljet.net/formulas/get-workbook-name-only#main-content)

[](https://exceljet.net/formulas/get-workbook-name-only#)

*   [Previous](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    
*   [Next](https://exceljet.net/formulas/get-workbook-path-only)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Get workbook name only
======================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[TEXTBEFORE](https://exceljet.net/functions/textbefore-function)

[MID](https://exceljet.net/functions/mid-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")

Summary
-------

To get the workbook name only (i.e. the name of the Excel file) you can use a formula based on the [CELL function](https://exceljet.net/functions/cell-function)
 with the [TEXTAFTER](https://exceljet.net/functions/textafter-function)
 and [TEXTBEFORE](https://exceljet.net/functions/textbefore-function)
 functions. In the example shown, the formula in E5 is:

    =TEXTAFTER(TEXTBEFORE(CELL("filename",A1),"]"),"[")\
    \
\
The result is the name of the workbook only, "Test workbook name.xlsx" in the example shown.\
\
_Note: TEXTAFTER and TEXTBEFORE are only available in the latest version of Excel. In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)\
, you can use a more complicated formula based on the [MID](https://exceljet.net/functions/mid-function)\
 and [FIND](https://exceljet.net/functions/find-function)\
 functions. Read below for details._\
\
Generic formula\
---------------\
\
    =TEXTAFTER(TEXTBEFORE(CELL("filename",A1),"]"),"[")\
\
Explanation \
------------\
\
In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)\
 and the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)\
. In older versions of Excel, you can use a more complicated formula based on the [MID](https://exceljet.net/functions/mid-function)\
 and [FIND](https://exceljet.net/functions/find-function)\
 functions. Both options rely on the [CELL function](https://exceljet.net/functions/cell-function)\
 to get a full path to the current workbook. Read below for details.\
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
Notice the workbook name is enclosed in square brackets ("\[name\]"). The challenge then becomes how best to extract just the text between the square brackets from the path. The best way to do this depends on what Excel version you have. If you have the latest version of Excel, you should use TEXTAFTER and TEXTBEFORE functions. Otherwise, you can use the MID and FIND functions as explained below.\
\
### TEXTAFTER with TEXTBEFORE\
\
In [Excel 365](https://exceljet.net/glossary/excel-365)\
, the easiest option is to use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)\
 with the [TEXTBEFORE function](https://exceljet.net/functions/textbefore-function)\
 like this:\
\
    =TEXTAFTER(TEXTBEFORE(CELL("filename",A1),"]"),"[")\
\
This is an example of [nesting](https://exceljet.net/glossary/nesting)\
 — the TEXTBEFORE function is nested _inside_ of the TEXTAFTER function, and the CELL function is nested inside of TEXTBEFORE. Working from the inside out CELL returns the full path to the workbook as explained above, and the result is delivered to the TEXTBEFORE function, which extracts all text _before_ the closing square bracket ("\]"):

    TEXTBEFORE(CELL("filename",A1),"]")

_Delimiter_ is set to "\]" in order to retrieve only text that occurs _before_ the closing square bracket ("\]"). The result looks like this:

    "C:\path\to\folder\[workbook.xlsx"\
\
This value is then delivered to the TEXTAFTER function, which is configured to return text _after_ the opening square bracket ("\["):\
\
    =TEXTAFTER("C:\path\to\folder\[workbook.xlsx","[")\
\
The final result from TEXTAFTER is the workbook name only:\
\
    "workbook.xlsx"\
\
Assuming a path like "C:\\path\\to\\folder\\\[workbook.xlsx\]sheetname", the final result is "workbook.xlsx". \
\
### MID + FIND function\
\
In older versions of Excel you can get the workbook name with a more complicated formula based on the MID and FIND function:\
\
    =MID(CELL("filename",A1),FIND("[",CELL("filename",A1))+1,FIND("]", CELL("filename",A1))-FIND("[",CELL("filename",A1))-1)\
    \
\
This formula is annoyingly complex, mostly because older versions of Excel do not have good text parsing functions, and this means the formula needs to work in small, redundant steps. Notice the CELL function is called 4 times! \
\
To extract the workbook name, the formula works in 5 steps:\
\
1.  Get the full path and filename.\
2.  Locate the opening square bracket ("\[").\
3.  Locate the closing square bracket ("\]").\
4.  Calculate the length of the workbook name in characters.\
5.  Extract the text between square brackets with the MID function.\
\
### Get path and filename\
\
To get the path and file name, we use the [CELL function](https://exceljet.net/functions/cell-function)\
 like this:\
\
    CELL("filename",A1) // get path and filename\
    \
\
The _info\_type_ argument is "filename" and _reference_ is A1. The cell reference is arbitrary and can be any cell in the worksheet. The result is a full path like this as text:\
\
    "C:\path\to\folder\[workbook.xlsx]sheetname"\
    \
\
The path starts with the drive and includes both the workbook name and the Sheet name. Notice the workbook name appears enclosed in square brackets.\
\
### Locate the opening square bracket\
\
The location of the opening square bracket ("\[") is determined like this\
\
    FIND("[",CELL("filename",A1)) // returns 19\
    \
\
The [FIND function](https://exceljet.net/functions/find-function)\
 returns the location of "\[" (19) . We then add 1 because we want to extract text starting one character _after_ the "\[". We can now rewrite the formula like this:\
\
    =MID(CELL("filename",A1),20,FIND("]", CELL("filename",A1))-FIND("[",CELL("filename",A1))-1)\
    \
\
### Locate the closing square bracket\
\
Next, we locate the closing square bracket "\]" in the same way with the FIND function:\
\
    FIND("]", CELL("filename",A1)) // returns 33\
    \
\
The FIND function returns 33, from which we subtract 1, in order to extract text up through character 32.\
\
### Calculate the length of the workbook name\
\
The final step is to extract the text _between_ the square brackets, and this is done with the [MID function](https://exceljet.net/functions/mid-function)\
. We know where we want to start (20) and where to end (32). However, while the MID function takes _start\_num_ as the starting position, there is no equivalent _end\_num_. Instead, MID takes _num\_chars_, the number of characters to extract. Therefore, we need to calculate _num\_chars_ by subtracting the opening bracket "\[" location from closing bracket "\]" location. All of the code below simply calculates the number of characters to extract:\
\
    =FIND("]", CELL("filename",A1))-FIND("[",CELL("filename",A1))-1\
\
Using our test path above, the result is 13. This is the length of the workbook name in characters.\
\
### Extract the text between the brackets\
\
We can now rewrite the formula like this:\
\
    =MID(CELL("filename",A1),20,13)\
    =MID("C:\path\to\folder\[workbook.xlsx]sheetname",20,13)\
    ="workbook.xlsx"\
    \
\
The final result is "workbook.xlsx". \
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
[![Excel formula: Get workbook path only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_path_only.png "Excel formula: Get workbook path only")](https://exceljet.net/formulas/get-workbook-path-only)\
\
### [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)\
\
In this example, the goal is to get the workbook path without the workbook name . For example, given a workbook called fruits.xlsx saved to: C:\\examples\\fruits.xlsx We want the path only like this: C:\\examples\\ TEXTBEFORE solution In a modern version of Excel (Excel 2021 or later) the simplest way...\
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
[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)\
\
### [CELL Function](https://exceljet.net/functions/cell-function)\
\
The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...\
\
[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)\
\
### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)\
\
The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....\
\
[![Excel TEXTBEFORE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textbefore%20function.png "Excel TEXTBEFORE function")](https://exceljet.net/functions/textbefore-function)\
\
### [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)\
\
The Excel TEXTBEFORE function returns the text that occurs before a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTBEFORE can return text before the nth occurrence of the delimiter.\
\
[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)\
\
### [MID Function](https://exceljet.net/functions/mid-function)\
\
The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".\
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
*   [Get workbook path only](https://exceljet.net/formulas/get-workbook-path-only)\
    \
*   [Get sheet name only](https://exceljet.net/formulas/get-sheet-name-only)\
    \
*   [Dynamic worksheet reference](https://exceljet.net/formulas/dynamic-worksheet-reference)\
    \
\
### Functions\
\
*   [CELL Function](https://exceljet.net/functions/cell-function)\
    \
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)\
    \
*   [TEXTBEFORE Function](https://exceljet.net/functions/textbefore-function)\
    \
*   [MID Function](https://exceljet.net/functions/mid-function)\
    \
*   [FIND Function](https://exceljet.net/functions/find-function)\
    \
\
### Links\
\
*   [Excel file and folder names (Chip Pearson)](http://www.cpearson.com/excel/FileFolderNames.aspx)\
    \
\
### Training\
\
*   [Core Formula](https://exceljet.net/training/core-formula)\
    \
*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)\
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