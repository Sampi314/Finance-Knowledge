# Get sheet name only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/get-sheet-name-only

---

[Skip to main content](https://exceljet.net/formulas/get-sheet-name-only#main-content)

[](https://exceljet.net/formulas/get-sheet-name-only#)

*   [Previous](https://exceljet.net/formulas/get-full-workbook-name-and-path)
    
*   [Next](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    

[Workbook](https://exceljet.net/formulas#Workbook)

Get sheet name only
===================

by Dave Bruns · Updated 15 Apr 2024

Related functions 
------------------

[CELL](https://exceljet.net/functions/cell-function)

[TEXTAFTER](https://exceljet.net/functions/textafter-function)

[MID](https://exceljet.net/functions/mid-function)

[FIND](https://exceljet.net/functions/find-function)

![Excel formula: Get sheet name only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/get%20worksheet%20name%20only.png "Excel formula: Get sheet name only")

Summary
-------

To get the name of the current worksheet (i.e. current tab) you can use a formula based on the [CELL function](https://exceljet.net/functions/cell-function)
 together with the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In the example shown, the formula in E5 is:

    =TEXTAFTER(CELL("filename",A1),"]")

The result is "September" the name of the current worksheet in the workbook shown. In older versions of Excel which do not provide the TEXTAFTER function, you can use an alternate formula based on the [MID](https://exceljet.net/functions/mid-function)
 and [FIND](https://exceljet.net/functions/find-function)
 function. Both approaches are explained below.

Generic formula
---------------

    =TEXTAFTER(CELL("filename",A1),"]")

Explanation 
------------

In this example, the goal is to return the name of the current worksheet (i.e. tab) in the current workbook with a formula. This is a simple problem in the latest version of Excel, which provides the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
. In older versions of Excel, you can use an alternative formula based on the [MID](https://exceljet.net/functions/mid-function)
 and [FIND](https://exceljet.net/functions/find-function)
 functions. Both formula options rely on the [CELL function](https://exceljet.net/functions/cell-function)
 to get a full path to the current workbook. Read below for a full explanation.

> You must save your workbook before the formulas presented here will work since they depend on the CELL function to return a full path to the workbook.

### Workbook path

The first step in this problem is to get the workbook path, which includes the workbook and worksheet name. This can be done with the [CELL function](https://exceljet.net/functions/cell-function)
 like this:

    CELL("filename",A1)
    

With the _info\_type_ [argument](https://exceljet.net/glossary/function-argument)
 set to "filename", and _reference_ set to cell A1 in the current worksheet, the result from CELL is a full path as a text string like this:

    "C:\path\to\folder\[workbook.xlsx]sheetname"
    

Notice the sheet name begins _after_ the closing square bracket ("\]"). The problem now becomes how to extract the sheet name from the path. The best way to do this depends on your Excel version. Use the TEXTAFTER function if available. Otherwise, use the MID and FIND functions as explained below.

### TEXTAFTER function

In [Excel 365](https://exceljet.net/glossary/excel-365)
, the easiest option is to use the [TEXTAFTER function](https://exceljet.net/functions/textafter-function)
 with the CELL function like this:

    =TEXTAFTER(CELL("filename",A1),"]")

The CELL function returns the full path to the current workbook as explained above, and this text string is delivered to TEXTAFTER as the _text_ argument. _Delimiter_ is set to "\]" in order to retrieve only text that occurs _after_ the closing square bracket ("\]"). In the example shown, the final result is "September" the name of the current worksheet in the workbook shown. 

### MID + FIND function

In older versions of Excel that do not offer the TEXTAFTER function, you can use the [MID function](https://exceljet.net/functions/mid-function)
 with the [FIND function](https://exceljet.net/functions/find-function)
 to extract the sheet name:

    =MID(CELL("filename",A1),FIND("]",CELL("filename",A1))+1,255)

The core of this formula is the MID function, which is used to extract text starting at a specific position in a text string. Working from the inside out, the first CELL function returns the full path to the current workbook to the MID function as the _text_ argument:

    CELL("filename",A1) // get full path

We then need to tell MID where to start extracting text. To do this, we use the FIND function with a second call to the CELL function to locate the "\]" character. We want MID to start extracting text _after_ the "\]" character, so we use the FIND function to get the position, then add 1:

    FIND("]",CELL("filename",A1))+1 // get start number
    

The result from the above snippet is returned to the MID function as _start\_num_. For the _num\_chars_ argument, we hard-code the number 255\*. The MID function doesn't care if the number of characters requested is larger than the length of the remaining text, it simply extracts _all_ remaining text. The final result is "September" the name of the current worksheet in the workbook shown.

_\*Note: In Excel user interface, you can't name a worksheet longer than 31 characters, but the file format itself permits worksheet names up to 255 characters, so this ensures the entire name is retrieved._

Related formulas
----------------

[![Excel formula: Get full workbook name and path](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get%20workbook%20name%20and%20path_0.png "Excel formula: Get full workbook name and path")](https://exceljet.net/formulas/get-full-workbook-name-and-path)

### [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)

The CELL function can return various information about a worksheet. CELL can get things like address and filename, as well as information about the formatting used in the cell. The type of information to be returned is specified by the info\_type argument . In this example, we want the path, name,...

[![Excel formula: Get workbook name and path without sheet](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_workbook_name_and_path_without_sheet.png "Excel formula: Get workbook name and path without sheet")](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

### [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)

In this example, the goal is to get a normal path to the current workbook, without a sheet name, and without the square brackets ("\[ \]") that normally enclose the workbook name. This is a pretty simple problem in the latest version of Excel, which provides the TEXTBEFORE function . In older...

[![Excel formula: Get workbook name only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Get_workbook_name_only.png "Excel formula: Get workbook name only")](https://exceljet.net/formulas/get-workbook-name-only)

### [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)

In this example, the goal is to return the name of the current workbook with a formula. This is a fairly simple problem in the latest version of Excel, which provides the TEXTAFTER function and the TEXTBEFORE function . In older versions of Excel, you can use a more complicated formula based on the...

[![Excel formula: Worksheet name exists](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/worksheet%20name%20exists.png "Excel formula: Worksheet name exists")](https://exceljet.net/formulas/worksheet-name-exists)

### [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)

The ISREF function returns TRUE for a valid worksheet reference and FALSE is not. In this case, we want to find out of a particular sheet exists in a workbook, so we construct a full reference by concatenating the sheet names in column B with an exclamation mark and "A1": B5...

Related functions
-----------------

[![Excel CELL function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20cell%20function.png "Excel CELL function")](https://exceljet.net/functions/cell-function)

### [CELL Function](https://exceljet.net/functions/cell-function)

The Excel CELL function returns information about a cell in a worksheet. The type of information to be returned is specified as _info\_type_. CELL can get things like address and filename, as well as detailed info about the formatting used in the cell. See below for a full list of...

[![Excel TEXTAFTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textafter%20function.png "Excel TEXTAFTER function")](https://exceljet.net/functions/textafter-function)

### [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)

The Excel TEXTAFTER function returns the text that occurs after a given substring or delimiter. In cases where multiple delimiters appear in the text, TEXTAFTER can return text after the nth occurrence of a delimiter....

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel FIND function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20find.png "Excel FIND function")](https://exceljet.net/functions/find-function)

### [FIND Function](https://exceljet.net/functions/find-function)

The Excel FIND function returns the position (as a number) of one text string inside another. When the text is not found, FIND returns a #VALUE error.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Get full workbook name and path](https://exceljet.net/formulas/get-full-workbook-name-and-path)
    
*   [Get workbook name and path without sheet](https://exceljet.net/formulas/get-workbook-name-and-path-without-sheet)
    
*   [Get workbook name only](https://exceljet.net/formulas/get-workbook-name-only)
    
*   [Worksheet name exists](https://exceljet.net/formulas/worksheet-name-exists)
    

### Functions

*   [CELL Function](https://exceljet.net/functions/cell-function)
    
*   [TEXTAFTER Function](https://exceljet.net/functions/textafter-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [FIND Function](https://exceljet.net/functions/find-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    
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