# Formula with locked absolute reference - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/formula-with-locked-absolute-reference

---

[Skip to main content](https://exceljet.net/formulas/formula-with-locked-absolute-reference#main-content)

[](https://exceljet.net/formulas/formula-with-locked-absolute-reference#)

*   [Previous](https://exceljet.net/formulas/forecast-vs-actual-variance)
    
*   [Next](https://exceljet.net/formulas/get-date-associated-with-last-entry)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Formula with locked absolute reference
======================================

by Dave Bruns · Updated 30 Nov 2021

Related functions 
------------------

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Formula with locked absolute reference](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/formula%20with%20locked%20absolute%20reference.png "Excel formula: Formula with locked absolute reference")

Summary
-------

To create a formula with a "locked" absolute reference – a reference that won't be changed during copy or paste, or when rows and columns are inserted or deleted in a worksheet – you can use the [INDIRECT function](https://exceljet.net/functions/indirect-function)
. In the example shown, the formula in E5 is:

    =INDIRECT("B5")
    

This approach can be useful when a worksheet is routinely edited in a way that would break traditional cell references. This reference to cell B5 won't change during copy/paste/cut operations, or when columns or rows are inserted/deleted in a worksheet.

Generic formula
---------------

    =INDIRECT("A1")

Explanation 
------------

In this example, the goal is to create an "locked" reference that won't change when columns or rows are added or deleted in a worksheet, or during a copy / paste / cut operation.

The INDIRECT function accepts text, and evaluates that text as a reference. As a result, the text is not susceptible to changes, like a normal cell reference. It will continue to evaluate to the same location regardless of changes to the worksheet. For example, this formula:

    =INDIRECT("A1")
    

will continue to return a reference to cell A1 even if row 1, or column A, are deleted.

### Examples

A reference created with INDIRECT can be used just like a regular cell reference in other formulas. In the worksheet shown above, the formulas in E5:E9 use INDIRECT to create a locked reference that won't change:

    =INDIRECT("B5")
    =SUM(INDIRECT("B5:B16"))
    =MIN(INDIRECT("B5:B16"))
    =MAX(INDIRECT("B5:B16"))
    =COUNT(INDIRECT("B5:B16"))
    

This approach can be useful when a worksheet is routinely edited in a way that would break traditional cell references.

### Sheet names

Formulas with sheet names must follow standard rules. Sheets names without spaces or punctuation need no extra handling:

    =INDIRECT("Sheet1!A1")
    

Sheet names with space or punctuation need to be enclosed in single quotes ('):

    =INDIRECT("'Sheet 1'!A1") // note single quotes
    

_Note: if you \*rename\* a sheet name used in INDIRECT, the reference will break. This happens because the reference is entered as text and therefore is not automatically updated like a normal reference._

### Different from absolute and relative references

Using INDIRECT is different from standard [absolute, relative, and mixed references](https://exceljet.net/shortcuts/toggle-absolute-and-relative-references)
. The $ syntax is designed to allow "intelligent" copying and pasting of formulas, so that references that need to change _will change_, while references that shouldn't change, _will not change_. Using INDIRECT with text references stops _all changes_ to the reference, even when columns/rows are inserted or deleted, or when a sheet is renamed.

_Note: INDIRECT is a "[volatile function](https://exceljet.net/glossary/volatile-function)
" function, and can cause slow performance in large or complicated workbooks._

Related formulas
----------------

[![Excel formula: VLOOKUP with variable table array](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP%20with%20variable%20table%20array.png "Excel formula: VLOOKUP with variable table array")](https://exceljet.net/formulas/vlookup-with-variable-table-array)

### [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)

In this example, the goal is to set up VLOOKUP to retrieve costs based on a variable vendor name. In other words, we want a formula that allows us to switch tables dynamically based on a user-supplied value. There are two cost tables in the worksheet, one for Vendor A and one for Vendor B. Both...

[![Excel formula: Sum top n values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_top_n_values.png "Excel formula: Sum top n values")](https://exceljet.net/formulas/sum-top-n-values)

### [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)

In this example, the goal is to sum the largest n values in a set of data, where n is a variable that can be easily changed. For convenience, the range B5:B16 is named data . At a high level, the solution breaks down into two steps: (1) extract the n largest values from the data set and (2) sum the...

[![Excel formula: Lookup with variable sheet name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/lookup_with_variable_sheet_name.png "Excel formula: Lookup with variable sheet name")](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

### [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)

In this example, the goal is to create a lookup formula with a variable sheet name. In other words, a formula that uses a sheet name typed into a cell to construct a reference to a range on that sheet. If the sheet name is changed, the reference should update automatically. The key to the solution...

[![Excel formula: Create array of numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/create%20array%20of%20numbers.png "Excel formula: Create array of numbers")](https://exceljet.net/formulas/create-array-of-numbers)

### [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)

Note: In Excel 365 , the new SEQUENCE function is a better and easier way to create an array of numbers. The method explained below will work in previous versions. The core of this formula is a string that represents rows. For example, to create an array with 10 numbers, you can hard-code a string...

Related functions
-----------------

[![Excel INDIRECT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20indirect%20function_0.png "Excel INDIRECT function")](https://exceljet.net/functions/indirect-function)

### [INDIRECT Function](https://exceljet.net/functions/indirect-function)

The Excel INDIRECT function returns a valid cell reference from a given text string. INDIRECT is useful when you want to assemble a text value that can be used as a valid reference.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP with variable table array](https://exceljet.net/formulas/vlookup-with-variable-table-array)
    
*   [Sum top n values](https://exceljet.net/formulas/sum-top-n-values)
    
*   [Lookup with variable sheet name](https://exceljet.net/formulas/lookup-with-variable-sheet-name)
    
*   [Create array of numbers](https://exceljet.net/formulas/create-array-of-numbers)
    

### Functions

*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

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