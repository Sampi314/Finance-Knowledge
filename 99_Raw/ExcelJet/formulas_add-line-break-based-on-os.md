# Add line break based on OS - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-line-break-based-on-os

---

[Skip to main content](https://exceljet.net/formulas/add-line-break-based-on-os#main-content)

[](https://exceljet.net/formulas/add-line-break-based-on-os#)

*   [Previous](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    
*   [Next](https://exceljet.net/formulas/capitalize-first-letter-in-a-text-string)
    

[Text](https://exceljet.net/formulas#Text)

Add line break based on OS
==========================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[INFO](https://exceljet.net/functions/info-function)

[CHAR](https://exceljet.net/functions/char-function)

![Excel formula: Add line break based on OS](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add%20line%20break%20based%20on%20OS.png "Excel formula: Add line break based on OS")

Summary
-------

To add a line break taking into account the current OS (Mac or Windows), you can use the [INFO function](https://exceljet.net/functions/info-function)
 to test the system and then return the correct break character — [ASCII](https://exceljet.net/glossary/ascii)
 10 for Windows and ASCII 13 on a Mac. In the worksheet shown, the formula in cell C3 is:

    =IF(INFO("system")="mac",CHAR(13),CHAR(10))
    

Notice that cell C3 has been [named](https://exceljet.net/articles/named-ranges)
 "break" as you can see in the [name box](https://exceljet.net/glossary/name-box)
. The result is that the name **break** can be used like a variable in other formulas.

> This formula will not work correctly and is not needed in current versions of Mac Excel. Starting with Excel 2016, the Mac version of Excel began to use ASCII 10 as a line break character, the same as the Windows version. The example on this page is therefore historical to illustrate how the INFO function can be used to switch a value depending on the platform Excel is running on. See: [How to insert a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
>  for a standard formula solution in current versions of Excel.

Generic formula
---------------

    =IF(INFO("system")="mac",CHAR(13),CHAR(10))

Explanation 
------------

In older versions of Excel (before Excel 2016?), the character used for line breaks is different depending on whether Excel is running on a Mac or Windows computer: On Windows Excel, the line break character is ASCII 10. In older versions of Excel on a Mac, the line break character is ASCII 13. These are invisible characters and therefore difficult to enter directly into a formula. The standard way to insert them in a formula is to use the [CHAR function](https://exceljet.net/functions/char-function)
 like this:

    CHAR(10) // line break in Win Excel
    CHAR(13) // line break in Mac Excel

Because the line break varies by platform in older versions of Excel, it is tricky to write a single formula that will work as expected on both platforms. One solution is to use the [INFO function](https://exceljet.net/functions/info-function)
 to test the current environment and then set a value for a line break that is conditional on the platform. In the worksheet shown, we do this by first [naming](https://exceljet.net/articles/named-ranges)
 cell C3 "break". Then, in the same cell, we enter the following formula:

    =IF(INFO("system")="mac",CHAR(13),CHAR(10))
    

Now we can use the word **break** like a variable in a formula. If Excel is running on a Mac, **break** will equal CHAR(13), if not, **break** will equal CHAR(10). In column E, we can then [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the address information that appears in B, C, and D with a formula like this:

    =B6&break&C6&break&D6
    

The result of the concatenation is text with line breaks:

Traci Brown¬  
1301 Robinson Court¬  
Saginaw, MI 48607

_Note: to see the line break take effect, you will need to [enable text wrap](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
._

Related formulas
----------------

[![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

### [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut Alt + Enter to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the CHAR function with the ASCII...

[![Excel formula: Count line breaks in cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20line%20breaks%20in%20cell.png "Excel formula: Count line breaks in cell")](https://exceljet.net/formulas/count-line-breaks-in-cell)

### [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)

First, the LEN function counts total characters in the cell B5. Next SUBSTITUTE removes all "line returns" from the text in B5 by looking for CHAR(10) which is the character code for the return character in Windows. LEN returns the result inside of a second LEN, which counts characters without...

Related functions
-----------------

[![Excel INFO function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20info%20function.png "Excel INFO function")](https://exceljet.net/functions/info-function)

### [INFO Function](https://exceljet.net/functions/info-function)

The Excel INFO function returns information about the current environment, including platform, Excel version, number of worksheets in a workbook, and so on. To use the INFO function, supply the type of information you want as text. There are seven types of information available, summarized in...

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20concatenate%20with%20line%20breaks-thumb.png)](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

### [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)

In the real world, you often need to concatenate values in a way that includes line breaks and other punctuation. In this video we'll look at a clever way to make this task easier and less error-prone. A common example of a situation that requires concatenation is assembling a mailing address from...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How_to_wrap_text_in_cells-thumb.png)](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)

### [How to wrap text in cells in Excel](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)

Before we look at alignment, we need to look at text wrapping. Wrapping text in cells is a key feature in Excel. Wrapping text allows you to fit multiple lines of text in a single cell. Let's take a look. You've probably noticed that longer text will extend right through the cell border into...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)
    
*   [Count line breaks in cell](https://exceljet.net/formulas/count-line-breaks-in-cell)
    

### Functions

*   [INFO Function](https://exceljet.net/functions/info-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

### Videos

*   [How to concatenate with line breaks](https://exceljet.net/videos/how-to-concatenate-with-line-breaks)
    
*   [How to wrap text in cells in Excel](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
    

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