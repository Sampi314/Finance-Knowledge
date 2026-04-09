# Excel HYPERLINK function | Exceljet

**Source:** https://exceljet.net/functions/hyperlink-function

---

[Skip to main content](https://exceljet.net/functions/hyperlink-function#main-content)

[](https://exceljet.net/functions/hyperlink-function#)

*   [Previous](https://exceljet.net/functions/hlookup-function)
    
*   [Next](https://exceljet.net/functions/index-function)
    

Excel 2003

[Lookup and reference](https://exceljet.net/functions#Lookup-and-reference)

HYPERLINK Function
==================

by Dave Bruns · Updated 19 Mar 2024

![Excel HYPERLINK function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20hyperlink%20function.png "Excel HYPERLINK function")

Summary
-------

The Excel HYPERLINK function returns a hyperlink to a given destination. You can use HYPERLINK to create a clickable hyperlink with a formula. The HYPERLINK function can build links to workbook locations, pages on the internet, or files on network servers.

Purpose 
--------

Create a clickable link.

Return value 
-------------

A clickable hyperlink

Syntax
------

    =HYPERLINK(link_location,[friendly_name])

*   _link\_location_ - The path to the file or page to be opened.
*   _friendly\_name_ - \[optional\] The link text to display in a cell.

Using the HYPERLINK function 
-----------------------------

The HYPERLINK function creates a hyperlink to a given destination with a "friendly name", which is simply the anchor text. You can use HYPERLINK to construct a clickable hyperlink with a formula. The HYPERLINK function can build links to other cells in a workbook, other sheets, named ranges, other workbooks, pages on the internet, or files on network servers. You can also use HYPERLINK to create email links.

The HYPERLINK function takes two [arguments](https://exceljet.net/glossary/function-argument)
: _link\_location_ and _friendly\_name_. _Link\_location_ is the destination or path the link should follow, entered as text. _Friendly\_name_ is the text that will be displayed with the link.

When a user clicks a cell that contains the HYPERLINK function, Excel will open the file or page specified by link\_location. _Link\_location_ can be a cell reference or named range, a path to a file stored on a local drive, a path a file on a server using Universal Naming Convention (UNC), or an internet path in Uniform Resource Locator (URL) format.

### Example #1 - link to cell

To link to another cell in the same worksheet, prefix the cell with "#":

    =HYPERLINK("#Z100","link to Z100") // cell in same sheet
    

### Example #2 - link to sheet

To link to another sheet in the same workbook, use "#" with the Sheet name like this

    =HYPERLINK("#Sheet2!A1","Sheet2") // sheet2 in same workbook
    

If the sheet name contains a space, you'll get an invalid reference error with the formula above. In that case, you'll need to enclose the sheet name in single quotes (') like this:

    =HYPERLINK("#'Sheet 2'!A1","Sheet 2") // sheet name with space
    

### Example #3 - external link

To link to [https://exceljet.net/](https://exceljet.net/)
 with the text "exceljet":

    =HYPERLINK("https://exceljet.net/","exceljet")
    

### Example #4 - email link

To link to a valid email address in A1, you can [concatenate](https://exceljet.net/glossary/concatenation)
 "mailto:" like this:

    =HYPERLINK("mailto:"&A1,"email") // link to email address in A1
    

With two email addresses in A1 and A2, you can create a link like this:

    =HYPERLINK("mailto:"&A1&","&B1,"email") // two emails
    

[This formula example](https://exceljet.net/formulas/send-email-with-formula)
 explains how to construct a more complete mailto email link with cc, subject, body, etc.

### Notes

*   _Link\_location_ should be supplied as a text string in quotation marks or a cell reference that contains the link path as text.
*   If _friendly\_name_ is not supplied, the HYPERLINK will display _link\_location_ as the _friendly\_name_.
*   To select a cell that contains HYPERLINK _without_ following the link, use arrow keys or right-click the cell.

HYPERLINK function examples
---------------------------

[![Excel formula: Send email with formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/send%20email%20with%20formula2.png "Excel formula: Send email with formula")](https://exceljet.net/formulas/send-email-with-formula)

### [Send email with formula](https://exceljet.net/formulas/send-email-with-formula)

In this example, the goal is to create a clickable link that will result in a ready-to-send email. The mailto link protocol The mailto link protocol allows five variables as shown in the table below: Variable Purpose mailto: The primary recipient(s) &cc= The CC recipient(s) &bcc= The BCC...

[![Excel formula: Hyperlink to first match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/hyperlink%20to%20first%20match.png "Excel formula: Hyperlink to first match")](https://exceljet.net/formulas/hyperlink-to-first-match)

### [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)

Working from the inside out, we use a standard INDEX and MATCH function to locate the first match of lookup values in column B: INDEX(data,MATCH(B5,data,0)) The MATCH function gets the position of the value in B5 inside the named range data, which for the lookup value "blue" is 3. This result goes...

[![Excel formula: Build hyperlink with VLOOKUP](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/build%20hyperlink%20with%20VLOOKUP.png "Excel formula: Build hyperlink with VLOOKUP")](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

### [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)

The hyperlink function allows you to create a working link with a formula. It takes two arguments: link\_location and, optionally, friendly\_name . Working from the inside out, VLOOKUP looks up and retrieves a link value from column 2 of the named range "link\_table" (B5:C8). The lookup value comes...

[![Excel formula: Hyperlink to first blank cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Hyperlink%20to%20first%20blank%20cell.png "Excel formula: Hyperlink to first blank cell")](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

### [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)

Working from the inside out, we use MATCH to locate the relative position of the last entry in column C: MATCH(9.99E+307,C5:C100) Basically, we are giving MATCH a "big number" it will never find in approximate match mode. In this mode, MATCH will "step back" to the last numeric value. Note: this...

[![Excel formula: Count errors in all sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count_errors_in_all_sheets.png "Excel formula: Count errors in all sheets")](https://exceljet.net/formulas/count-errors-in-all-sheets)

### [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)

In this example, the goal is to count errors in a workbook by sheet, where the sheet names have been previously entered in a column as shown. This is a tricky problem in Excel for a couple of reasons. First, there is no direct way to generate a list of sheets in a workbook with a formula. Second,...

[![Excel formula: Link to multiple sheets](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/link%20to%20multiple%20sheets.png "Excel formula: Link to multiple sheets")](https://exceljet.net/formulas/link-to-multiple-sheets)

### [Link to multiple sheets](https://exceljet.net/formulas/link-to-multiple-sheets)

This formula relies on concatenation to assemble a valid location for the HYPERLINK function. In cell D5, the link location argument is created like this: "#"...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Build hyperlink with VLOOKUP](https://exceljet.net/formulas/build-hyperlink-with-vlookup)
    
*   [Hyperlink to first blank cell](https://exceljet.net/formulas/hyperlink-to-first-blank-cell)
    
*   [Count errors in all sheets](https://exceljet.net/formulas/count-errors-in-all-sheets)
    
*   [Link to multiple sheets](https://exceljet.net/formulas/link-to-multiple-sheets)
    
*   [Send email with formula](https://exceljet.net/formulas/send-email-with-formula)
    
*   [Hyperlink to first match](https://exceljet.net/formulas/hyperlink-to-first-match)
    

### Links

*   [Microsoft HYPERLINK function documentation](https://support.office.com/en-us/article/hyperlink-function-333c7ce6-c5ae-4164-9c47-7de9b76f577f)
    

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