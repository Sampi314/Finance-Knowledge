# Sum numbers in single cell - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-numbers-in-single-cell

---

[Skip to main content](https://exceljet.net/formulas/sum-numbers-in-single-cell#main-content)

[](https://exceljet.net/formulas/sum-numbers-in-single-cell#)

*   [Previous](https://exceljet.net/formulas/sum-matching-columns-and-rows)
    
*   [Next](https://exceljet.net/formulas/sum-top-n-values)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum numbers in single cell
==========================

by Dave Bruns · Updated 11 May 2024

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[SUM](https://exceljet.net/functions/sum-function)

[FILTERXML](https://exceljet.net/functions/filterxml-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7875/download?token=NioBvyoX)
 (16.11 KB)

![Excel formula: Sum numbers in single cell](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_numbers_in_cell.png "Excel formula: Sum numbers in single cell")

Summary
-------

To sum numbers that appear inside a single cell, separated by a delimiter, you can use a formula based on the [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
 and [VALUE](https://exceljet.net/functions/value-function)
 functions. In the example shown, the formula in cell D5 is:

    =SUM(VALUE(TEXTSPLIT(B5,",")))

As the formula is copied down, it returns a sum for the comma-separated numbers in column B.

Generic formula
---------------

    ​=SUM(VALUE(TEXTSPLIT(A1,",")))
    

Explanation 
------------

The goal is to sum numbers that appear inside a single cell as seen in column B. Technically, the numbers in each cell are a single text string, and the numbers are separated by commas, which is referred to as a "delimiter". In the current version of Excel, the easiest way to solve this problem is with the TEXTSPLIT function. It is possible to sum numbers separated by other delimiters as well. See below for an example.

### Summary

In a nutshell, we use the TEXTSPLIT function to split the numbers up by delimiter, then use VALUE to convert the numbers to true numeric values, and then use the SUM function to get a final sum. In the worksheet shown, the formula in cell B5 is:

    =SUM(VALUE(TEXTSPLIT(B5,",")))

Working from the inside out, we start with the TEXTSPLIT function.

### TEXTSPLIT function

The [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 is designed to split a text string by a given delimiter into multiple values. The minimal generic syntax for TEXTSPLIT looks like this:

    =TEXTSPLIT(text,delimiter)

The result from TEXTSPLIT is an [array](https://exceljet.net/glossary/array)
 of separate values. For example, given the text string "A,B,C" with a comma (",") as a delimiter, TEXTSPLIT returns an array like {"A","B","C"}:

    =TEXTSPLIT("A,B,C",",") // returns {"A","B","C"}

Notice the delimiter is enclosed in double quotes (""). Moving back to the example, with the text "1,2,3" in cell B5, TEXTSPLIT splits the text at each comma and returns an array with 3 values:

    =TEXTSPLIT(B5,",") // returns {"1","2","3"}

This is close to what we need, but notice the result from TEXTSPLIT is _text_. If we try to SUM the output from TEXTSPLIT directly, the SUM function will ignore the text values and return zero:

    =SUM(TEXTSPLIT(B5,",")) // returns 0

We need to convert the text values to numeric values before a sum is calculated. To do this, we use the VALUE function.

### VALUE function

The [VALUE function](https://exceljet.net/functions/value-function)
 converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value.  For example, if we provide the text "100", VALUE returns the number 100:

    =VALUE("100") returns 100

We can use VALUE to solve this problem by nesting TEXTSPLIT inside VALUE like this:

    =VALUE(TEXTSPLIT(B5,","))
    =VALUE({"1","2","3"})
    ={1,2,3}

VALUE converts each text string to a number and returns the result in an array. As a bonus, VALUE will automatically ignore any space characters that appear in the text.

### SUM function

The final step in this problem is to sum the numbers returned by the VALUE function. The final formula in cell D5 is:

    =SUM(VALUE(TEXTSPLIT(B5,",")))

TEXTSPLIT splits the text string into separate text values, VALUE converts the text values to numbers, and the result from SUM is 6, the sum of 1+2+3.

### Other delimiters

To handle numbers in a cell separated by a different value, you can change the delimiter given to TEXTSPLIT. For example, the same numbers in the worksheet below are separated by the "+" symbol instead of a comma. The formula in cell D5 is:

    =SUM(VALUE(TEXTSPLIT(B5,"+")))

![Delimiter set to a plus symbol "+"](https://exceljet.net/sites/default/files/images/formulas/inline/sum_numbers_in_cell_plus_symbol_delimiter.png "Delimiter set to a plus symbol "+"")

When the formula is copied down, the results are the same as the original example above.

### Pro tip

There are other ways to convert text values to numbers in Excel. One common method is just to add zero like this:

    =SUM(TEXTSPLIT(B5,",")+0)

The result is the same, but we are not using the VALUE function.

### Handling text values and errors

If the text in a cell contains text values (i.e. 1,2,3,A) the formula above will return a #VALUE error. This happens because the VALUE function will return a #VALUE error if it can't convert a value to a number and, when this happens, the SUM function will also return a #VALUE error. One way to handle this problem is to wrap the [IFERROR function](https://exceljet.net/functions/iferror-function)
 around VALUE like this:

    =SUM(IFERROR(VALUE(TEXTSPLIT(B5,",")),0))

Essentially, we are using IFERROR to convert any errors returned by VALUE to zero. SUM can then sum the zeros along with other numbers without trouble.

### Legacy Excel

Older versions of Excel do not provide the TEXTSPLIT function, so there is no direct way to split text values into an array. However, in the Windows version of Excel, you can use a workaround based on the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
:

    =SUM(FILTERXML("<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>","//y"))

In a nutshell, this formula converts the text in B5 to XML by replacing the commas with markup, then it uses FILTERXML to parse the individual numbers into an array. The SUM function then sums the numbers normally. FILTERXML automatically converts the numbers to numeric values in the process, so the VALUE function is not needed. [Detailed explanation here](https://exceljet.net/formulas/text-split-to-array)
.

_Note: FILTERXML is only available in Windows Excel._

Related formulas
----------------

[![Excel formula: Sum Roman numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20roman%20numbers.png "Excel formula: Sum Roman numbers")](https://exceljet.net/formulas/sum-roman-numbers)

### [Sum Roman numbers](https://exceljet.net/formulas/sum-roman-numbers)

The goal in this example is to sum a range of Roman numbers. The challenge is that Roman numbers appear as text in Excel, not numeric values. If you try to use the SUM function to sum a range of Roman numbers directly, the result is zero (0). The solution is to use the ARABIC function to convert...

[![Excel formula: Sum numbers with text](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum%20numbers%20with%20text.png "Excel formula: Sum numbers with text")](https://exceljet.net/formulas/sum-numbers-with-text)

### [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)

In this example, one goal is to sum the numbers that appear in the range B5:B16. A second more challenging goal is to create the table of results seen in E7:F12. For convenience, data is the named range B5:B16. Total sum To sum all the numbers that appear in B5:B16, ignoring text, the formula in E5...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum Roman numbers](https://exceljet.net/formulas/sum-roman-numbers)
    
*   [Sum numbers with text](https://exceljet.net/formulas/sum-numbers-with-text)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

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