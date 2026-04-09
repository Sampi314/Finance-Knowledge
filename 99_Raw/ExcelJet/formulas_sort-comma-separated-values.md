# Sort comma separated values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sort-comma-separated-values

---

[Skip to main content](https://exceljet.net/formulas/sort-comma-separated-values#main-content)

[](https://exceljet.net/formulas/sort-comma-separated-values#)

*   [Previous](https://exceljet.net/formulas/reverse-text-string)
    
*   [Next](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

[Text](https://exceljet.net/formulas#Text)

Sort comma separated values
===========================

by Dave Bruns · Updated 10 May 2024

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[SORT](https://exceljet.net/functions/sort-function)

[TEXTJOIN](https://exceljet.net/functions/textjoin-function)

[TRIM](https://exceljet.net/functions/trim-function)

[FILTERXML](https://exceljet.net/functions/filterxml-function)

![Excel formula: Sort comma separated values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sort_comma_separated_values.png "Excel formula: Sort comma separated values")

Summary
-------

To sort comma separated values in a cell, you can use a formula based on the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 together with the [SORT](https://exceljet.net/functions/sort-function)
 and [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 functions. In the example shown, the formula in cell D5, copied down, is:

    =TEXTJOIN(",",TRUE,SORT(TRIM(TEXTSPLIT(B5,,","))))
    

The result is the comma separated values from cell B5, sorted in alphabetical order.

Generic formula
---------------

    =TEXTJOIN(",",TRUE,SORT(TRIM(TEXTSPLIT(A1,,","))))

Explanation 
------------

In this example the goal is to sort the comma separated values in column B in alphabetical order. In the latest version of Excel, you can solve this problem with a formula based on TEXTSPLIT, SORT, and TEXTJOIN. In earlier versions of Excel the problem is more complicated. See below for a couple of alternatives.

### Current Excel

In the latest version of Excel, you can use a formula based on TEXTSPLIT, SORT, TEXTJOIN and (optionally) TRIM. In the example shown, the formula in cell D5, copied down, is:

    =TEXTJOIN(",",TRUE,SORT(TRIM(TEXTSPLIT(B5,,","))))
    

Working from the inside out, the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 is configured to split the comma separated values in B5 into rows like this:

    =TEXTSPLIT(B5,,",") // split into rows

Notice _col\_delimiter_ is left empty, and _row\_delimiter_ is provided as ",". We use _row\_delimiter_ instead of _col\_delimiter_ to save a little configuration with the SORT function coming up a bit later. The result from TEXTSPLIT is a [vertical array](https://exceljet.net/glossary/array)
 like this:

    {"C";"D";"A ";"F";"B";"E"}

This array is returned directly to the TRIM function:

    TRIM({"C";"D";"A ";"F";"B";"E"}) // remove extra space

The [TRIM function](https://exceljet.net/functions/trim-function)
 has just one job: remove extra space. This includes any leading or trailing spaces, as well as any extra space between values in normal text. In cell D5, TRIM strips the trailing space after "A" and returns the cleaned up array to the SORT function:

    SORT({"C";"D";"A";"F";"B";"E"})

The [SORT function](https://exceljet.net/functions/sort-function)
 then sorts the values in the array. By default, SORT will sort _rows_ in _ascending_ order. This is why we configured TEXTSPLIT to split values into rows: we can use this default behavior without any other configuration. Finally, the SORT function returns the sorted array directly to the TEXTJOIN function, which is configured to join values by with a comma:

    =TEXTJOIN(",",TRUE,{"A";"B";"C";"D";"E";"F"})

Note _delimiter_ is set to a comma (",") _ignore\_empty_ is set to TRUE, and _text1_ is delivered by the SORT function. TEXTJOIN joins each value in the array separated with a comma. The result is a single text string of comma separated values, sorted in alphabetical order.

### Legacy Excel

This is not an easy problem to solve in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
. One option is to use the [Text to columns](https://exceljet.net/glossary/text-to-columns)
 feature, then sort the values by column, and join them again with a formula that performs [concatenation](https://exceljet.net/articles/how-to-concatenate-in-excel)
. This is obviously quite manual, but it can be done.

If you happen to have a version of Excel _without_ TEXTSPLIT, but _with_ SORT and TEXTJOIN, you can use a more complicated formula based on the [FILTERXML function](https://exceljet.net/functions/filterxml-function)
:

    =TEXTJOIN(",",1,SORT(FILTERXML("<x><y>"&SUBSTITUTE(B5,",","</y><y>")&"</y></x>","//y")))

Basically, FILTERXML is performing the role of TEXTSPLIT in the formula above. In brief, we use SUBSTITUTE to convert the text values into a very simple XML format, then use FILTERXML to extract the values into an array. [See a more detailed explanation here](https://exceljet.net/formulas/text-split-to-array)
. After that SORT and TEXTJOIN work as explained above. When using FILTERXML, keep the following in mind:

1.  White space is ignored, a bit like using the [TRIM function](https://exceljet.net/functions/trim-function)
    . You can add space characters later with TEXTJOIN if needed.
2.  Numbers end up in General [number format](https://exceljet.net/glossary/number-format)
    . You could use the [TEXT function](https://exceljet.net/functions/text-function)
     to process the values after sorting to convert numeric values into a specific format.
3.  A double comma will throw a #VALUE error. You could catch this error with [IFERROR](https://exceljet.net/functions/iferror-function)
     and remap to a default value if needed.

> FILTERXML is only available in Excel for Windows, _not_ Excel for Mac, or Excel Online.

Related formulas
----------------

[![Excel formula: Split text with delimiter](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Split%20text%20with%20delimiter.png "Excel formula: Split text with delimiter")](https://exceljet.net/formulas/split-text-with-delimiter)

### [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)

The gist of this formula is to replace a given delimiter with a large number of spaces using SUBSTITUTE and REPT, then use the MID function to extract text related to the "nth occurrence" and the TRIM function to get rid of the extra space. In this snippet, the delimiter ( delim ) is replaced with...

[![Excel formula: Extract nth word from text string](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20nth%20word%20from%20text%20string.png "Excel formula: Extract nth word from text string")](https://exceljet.net/formulas/extract-nth-word-from-text-string)

### [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)

In this example, the goal is to extract the nth word from the text string given in column B. The article below explains two approaches. The first approach is based on the new TEXTSPLIT function , which makes it very easy to split text with a custom delimiter. The second approach is a more...

[![Excel formula: Extract multiple lines from a cell](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/extract%20multiple%20lines%20from%20a%20cell.png "Excel formula: Extract multiple lines from a cell")](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

### [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)

At the core, this formula looks for a line delimiter ("delim") and replaces it with a large number of spaces using the SUBSTITUTE and REPT functions. Note: In older versions of Excel on a Mac, use CHAR(13) instead of CHAR(10). The CHAR function returns a character based on it's numeric code. The...

[![Excel formula: Abbreviate names or words](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/abbreviate_with_capital_letters.png "Excel formula: Abbreviate names or words")](https://exceljet.net/formulas/abbreviate-names-or-words)

### [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)

In this example, the goal is to create initials or acronyms with a formula using the data in column B as the source text. The formula should parse the text in column B, build a list of capital letters used to start words and join the capital letters together in a single text string. The article...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel SORT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_sort_function_0.png "Excel SORT function")](https://exceljet.net/functions/sort-function)

### [SORT Function](https://exceljet.net/functions/sort-function)

The Excel SORT function sorts the contents of a range or array in ascending or descending order. Values can be sorted by one or more columns. SORT returns a dynamic array of results that automatically spills onto the worksheet.

[![Excel TEXTJOIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textjoin%20function.png "Excel TEXTJOIN function")](https://exceljet.net/functions/textjoin-function)

### [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)

The Excel TEXTJOIN function [concatenates](https://exceljet.net/glossary/concatenation)
 multiple values together with or without a delimiter. TEXTJOIN can concatenate values provided as cell references,  ranges, or constants, and can optionally ignore empty cells...

[![Excel TRIM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20trim%20function.png "Excel TRIM function")](https://exceljet.net/functions/trim-function)

### [TRIM Function](https://exceljet.net/functions/trim-function)

The Excel TRIM function strips extra spaces from text, leaving only a single space between words and no space characters at the start or end of the text.

[![Excel FILTERXML function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20filterxml.png "Excel FILTERXML function")](https://exceljet.net/functions/filterxml-function)

### [FILTERXML Function](https://exceljet.net/functions/filterxml-function)

The Excel FILTERXML function returns specific data from XML text using the specified XPath expression.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split text with delimiter](https://exceljet.net/formulas/split-text-with-delimiter)
    
*   [Extract nth word from text string](https://exceljet.net/formulas/extract-nth-word-from-text-string)
    
*   [Extract multiple lines from a cell](https://exceljet.net/formulas/extract-multiple-lines-from-a-cell)
    
*   [Abbreviate names or words](https://exceljet.net/formulas/abbreviate-names-or-words)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [SORT Function](https://exceljet.net/functions/sort-function)
    
*   [TEXTJOIN Function](https://exceljet.net/functions/textjoin-function)
    
*   [TRIM Function](https://exceljet.net/functions/trim-function)
    
*   [FILTERXML Function](https://exceljet.net/functions/filterxml-function)
    

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