# Replace one delimiter with another - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/replace-one-delimiter-with-another

---

[Skip to main content](https://exceljet.net/formulas/replace-one-delimiter-with-another#main-content)

[](https://exceljet.net/formulas/replace-one-delimiter-with-another#)

*   [Previous](https://exceljet.net/formulas/replace-one-character-with-another)
    
*   [Next](https://exceljet.net/formulas/reverse-text-string)
    

[Text](https://exceljet.net/formulas#Text)

Replace one delimiter with another
==================================

by Dave Bruns · Updated 3 May 2025

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

[CHAR](https://exceljet.net/functions/char-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7719/download?token=IWs-T6nv)
 (14.89 KB)

![Excel formula: Replace one delimiter with another](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/replace_one_delimiter_with_another.png "Excel formula: Replace one delimiter with another")

Summary
-------

To replace one delimiter with another in a text string, you can use a formula based on the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 and the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
. In the example shown, we are replacing commas with line breaks. The formula in cell D5 is:

    =TEXTJOIN(CHAR(10),TRUE,TRIM(TEXTSPLIT(B5, ", ")))

As the formula is copied down, the commas in column B become the line breaks seen in column D.

_Notes: (1) In older versions of Excel without TEXTJOIN or TEXTSPLIT, you can use a more primitive formula based on the_ [_SUBSTITUTE function_](https://exceljet.net/functions/substitute-function)
_. Both approaches are explained below. (2) This example is focused on replacing commas with line breaks, but you can use the same approach to replace other delimiters._

Generic formula
---------------

    =TEXTJOIN(new_delim,TRUE,TRIM(TEXTSPLIT(A1,old_delim)))

Explanation 
------------

In this example, the goal is to replace the comma-separated values in column B with the line break-separated values seen in column D. In a problem like this, the first step is to identify the _delimiter_, which is the character (or characters) that separate each value we want to process. In this case, the values in column B are separated by commas, so a comma (",") is the delimiter. Note that a space sometimes appears with the comma, but it is not consistent. This means we also need to handle this variation.

_Note: This example focuses on replacing commas with line breaks, but you can use the same approach to replace other delimiters._

### Approaches

There are three basic approaches to solving this problem:

1.  Use [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
     and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
     as shown ([Excel 365](https://exceljet.net/glossary/excel-365)
    )
2.  Use the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
     (Legacy Excel)
3.  Use Excel's [Text-to-Columns](https://exceljet.net/glossary/text-to-columns)
     feature (any version)

### CHAR function

Both formula options below depend on the CHAR function to insert a line break. The [CHAR function](https://exceljet.net/functions/char-function)
 returns a character when given a valid [ASCII code page number](https://exceljet.net/glossary/ascii)
. For example:

    =CHAR(65) // returns "A"
    =CHAR(97) // returns "a"
    

CHAR can be helpful when you want to insert characters in formulas or functions that are awkward or impossible to type directly. For example, you can use CHAR(10) to insert a line break in a formula like this:

    ="text"&CHAR(10)&"text" // add line break
    

_Note:_ [_Text wrap_](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)
 _must be enabled to see the line break take effect._ 

### TEXTSPLIT with TEXTJOIN

If you are using the current version of Excel, the easiest solution is to use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 with the [TEXTJOIN function](https://exceljet.net/functions/textjoin-function)
 as shown in the worksheet above:

    =TEXTJOIN(CHAR(10),TRUE,TRIM(TEXTSPLIT(B5,",")))

Working from the inside out, the first step is to parse the source data by the old delimiter, which is a comma. This is done with the TEXTSPLIT function and the [TRIM function](https://exceljet.net/functions/trim-function)
 like this:

    TRIM(TEXTSPLIT(B5,","))

Although TEXTSPLIT can accept up to six [arguments](https://exceljet.net/glossary/function-argument)
, we only need to provide the first two arguments, _text_ and _col\_delimiter_. _Text_ is provided as cell B5, and _col\_delimiter_ is a comma (","):

    =TEXTSPLIT(B5,",")

The result from TEXTSPLIT is returned to TRIM, which removes any leading or trailing spaces:

    TRIM({"Red"," Blue","Green"}) // remove extra space

The result from TRIM is returned directly to the TEXTJOIN function:

    =TEXTJOIN(CHAR(10),TRUE,{"Red","Blue","Green"})

Inside TEXTJOIN, _delimiter_ is set to CHAR(10), which is the line break character in Excel. _Ignore\_empty_ is set to TRUE in case any values in the original source text are empty (i.e. two commas appear together without a value in between), and _text1_ is delivered by the TRIM function in the previous step. TEXTJOIN then joins the values in the array with line breaks and returns the result to cell D5.

Note that the cells in the range D5:D8 must have text wrap enabled for the line breaks to behave correctly. You can enable Text wrap on the Home tab of the ribbon in the Alignment group. Or, you can display Format cells with the shortcut [Control + 1,](https://exceljet.net/shortcuts/format-almost-anything)
 then enable text wrap on the Alignment tab.

Video: [How to wrap text in cells in Excel](https://exceljet.net/videos/how-to-wrap-text-in-cells-in-excel)

### Sort option

Because we are working with the TEXTSPLIT function, we can easily sort the values before they are written out with the new delimiter. This is because TEXTSPLIT returns an _array of values_. The trick is to place the [SORT function](https://exceljet.net/functions/sort-function)
 outside the TRIM function and configure TEXTSPLIT to split text into _rows_ instead of columns:

    =TEXTJOIN(CHAR(10),TRUE,SORT(TRIM(TEXTSPLIT(B5,,","))))

We split text into rows because by default, SORT will sort by rows, not columns. Another option would be to change the configuration of SORT to sort by columns instead of changing TEXTSPLIT:

    =TEXTJOIN(CHAR(10),TRUE,SORT(TRIM(TEXTSPLIT(B5,",")),,,TRUE))

Both approaches achieve the same result.

### Legacy Excel

In older versions of Excel that do not offer the TEXTJOIN or TEXTSPLIT functions, you can use a more primitive formula based on the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
. If the comma-separated text is consistent, you can use a single call to SUBSTITUTE like this:

    =SUBSTITUTE(B5,",",CHAR(10))

Here, the source text in cell B5 is provided as the _text_ argument. The _old\_text_ argument is a comma without space (","), and _new\_text_ is provided by the [CHAR function](https://exceljet.net/functions/char-function)
, which returns Excel's line break character:

    CHAR(10) // line break

The CHAR function is a way to insert characters via [ASCII code numbers](https://exceljet.net/glossary/ascii)
. To summarize, SUBSTITUTE replaces all commas with Excel's line break character. This works, but it will leave leading spaces where commas appear with a space (", "). One way to handle this problem is to nest an additional SUBSTITUTE function inside the original formula as the _text_ argument:

    =SUBSTITUTE(SUBSTITUTE(B5,", ",","),",",CHAR(10))

Here, the inner SUBSTITUTE is configured to replace all instances of commas + space (", ") with a comma without space (","). This effectively normalizes the delimiters before the outer SUBSTITUTE runs. This formula will handle values separated by a single comma followed by a space (", ") and values separated by only a comma (",").

It is important to note that the SUBSTITUTE version of the formula is really just a hack. Unlike TEXTSPLIT, which actually parses the text values in the cell into an array that can be manipulated as needed, SUBSTITUTE has no concept of values separated by delimiters. It simply replaces text values in a text string. As a result, it's not possible to sort the values with this option, like we do with the TEXTSPLIT formula above.

### Text-to-columns

Formulas work great when you need a solution that is dynamic, because they will update automatically if data changes. However, if you only need a one-off manual process, you can also use Excel's [Text-to-Columns](https://exceljet.net/glossary/text-to-columns)
 feature to split values into separate cells, then [concatenate](https://exceljet.net/articles/how-to-concatenate-in-excel)
 the values in another formula using CHAR(10) to insert line breaks where needed.

Related formulas
----------------

[![Excel formula: Add a line break with a formula](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add_a_line_break_with_a_formula.png "Excel formula: Add a line break with a formula")](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

### [Add a line break with a formula](https://exceljet.net/formulas/add-a-line-break-with-a-formula)

In this example, the goal is to join together three text values separated by line breaks. In Excel, you can use the keyboard shortcut Alt + Enter to add a line break in a cell that contains text, but the same approach won't work in a formula. The trick is to use the CHAR function with the ASCII...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Get first word](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_get_first_word_1.png "Excel formula: Get first word")](https://exceljet.net/formulas/get-first-word)

### [Get first word](https://exceljet.net/formulas/get-first-word)

FIND returns the position (as a number) of the first occurrence of a space character in the text. This position, minus one, is fed into the LEFT function as num\_chars . The LEFT function then extracts characters starting at the left side of the text, up to (position - 1). Handling one word If a...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

[![Excel CHAR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20char%20function.png "Excel CHAR function")](https://exceljet.net/functions/char-function)

### [CHAR Function](https://exceljet.net/functions/char-function)

The Excel CHAR function returns a character when given a valid character code. CHAR can insert characters that are hard to enter into a formula. For example, CHAR(10) returns a line break and can be used to add a line break to text in a formula.

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
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Get first word](https://exceljet.net/formulas/get-first-word)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    
*   [CHAR Function](https://exceljet.net/functions/char-function)
    

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