# Data validation specific characters only - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/data-validation-specific-characters-only

---

[Skip to main content](https://exceljet.net/formulas/data-validation-specific-characters-only#main-content)

[](https://exceljet.net/formulas/data-validation-specific-characters-only#)

*   [Previous](https://exceljet.net/formulas/data-validation-require-unique-number)
    
*   [Next](https://exceljet.net/formulas/data-validation-unique-values-only)
    

[Data validation](https://exceljet.net/formulas#Data-validation)

Data validation specific characters only
========================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[MATCH](https://exceljet.net/functions/match-function)

[COUNT](https://exceljet.net/functions/count-function)

[LEN](https://exceljet.net/functions/len-function)

[MID](https://exceljet.net/functions/mid-function)

[INDIRECT](https://exceljet.net/functions/indirect-function)

![Excel formula: Data validation specific characters only](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Data%20validation%20specific%20characters%20only.png "Excel formula: Data validation specific characters only")

Summary
-------

To use data validation to allow a list of specific characters only, you can use a rather complicated array formula based on the [COUNT](https://exceljet.net/functions/count-function)
, [MATCH](https://exceljet.net/functions/match-function)
, and [LEN](https://exceljet.net/functions/len-function)
 functions. In the example shown, data validation is applied with this formula:

    =COUNT(MATCH(MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1),allowed&"",0))=LEN(B5)
    

where "allowed" is the [named range](https://exceljet.net/glossary/named-range)
 D5:D11.

Generic formula
---------------

    =COUNT(MATCH(MID(A1,ROW(INDIRECT("1:"&LEN(A1))),1),allowed&"",0))=LEN(A1)

Explanation 
------------

Working from the inside out, the MID function is used to generate an array from text entered in B5 with this snippet:

    MID(B5,ROW(INDIRECT("1:"&LEN(B5))),1)
    

[explained in detail here](https://exceljet.net/formulas/convert-string-to-array)
. The result is an array like this:

    {"A";"A";"A";"-";"1";"1";"1"}
    

which goes into MATCH as the lookup value. For the lookup array, we use the named range "allowed", concatenated to an [empty string](https://exceljet.net/glossary/empty-string)
 (""):

    allowed&""
    

The concatenation converts any numbers to strings so that we are matching apples-to-apples. The result is an array like this:

    {"A";"B";"C";"1";"2";"3";"-"}
    

The last argument in MATCH, match\_type is set to zero to force an exact match. Because we give MATCH multiple lookup values, we get back an array with multiple results:

    {1;1;1;7;4;4;4}
    

Each number in this array represents a match. In the event a match isn't found for a character, the array will contain a #N/A error.

Finally, the COUNT function is used to count the numbers in the result array, which is compared to a count of all characters in the cell calculated with the LEN function. When MATCH finds a match for all characters, the counts are equal, the formula returns TRUE, and data validation succeeds. If MATCH doesn't find a match any character, it returns #N/A instead of a number. In that case, the counts don't match and data validation fails.

_Note: this formula relies on brute force to get the job done. If you have a better approach, please leave a comment below._

> [Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
>  | [Data Validation Formulas](https://exceljet.net/data-validation-formulas)
>  | [Dependent Dropdown Lists](https://exceljet.net/articles/dependent-dropdown-lists)

Related formulas
----------------

[![Excel formula: Data validation no punctuation](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20no%20punctuation.png "Excel formula: Data validation no punctuation")](https://exceljet.net/formulas/data-validation-no-punctuation)

### [Data validation no punctuation](https://exceljet.net/formulas/data-validation-no-punctuation)

Data validation rules are triggered when a user adds or changes a cell value. When a custom formula returns TRUE, validation passes and the input is accepted. When a formula returns FALSE, validation fails and the input is rejected with a popup message. In this case, we have previously defined the...

[![Excel formula: Data validation allow numbers only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20number%20only.png "Excel formula: Data validation allow numbers only")](https://exceljet.net/formulas/data-validation-allow-numbers-only)

### [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)

Data validation rules are triggered when a user adds or changes a cell value. The ISNUMBER function returns TRUE when a value is numeric and FALSE if not. As a result, all numeric input will pass validation. Be aware that numeric input includes dates and times, whole numbers, and decimal values...

[![Excel formula: Data validation allow text only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20allow%20text%20only.png "Excel formula: Data validation allow text only")](https://exceljet.net/formulas/data-validation-allow-text-only)

### [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)

Data validation rules are triggered when a user adds or changes a cell value. Cell references in data validation formulas are relative to the upper left cell in the range selected when the validation rule is defined. The ISTEXT function returns TRUE when a value is text and FALSE if not. As a...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Data validation whole percentage only](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/data%20validation%20whole%20percentage%20only3.png "Excel formula: Data validation whole percentage only")](https://exceljet.net/formulas/data-validation-whole-percentage-only)

### [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)

The Excel TRUNC function does no rounding, it just returns a truncated number. It has an optional second argument (num\_digits) to specify precision. When num\_digits is not provided, it defaults to zero. In this formula for data validation, we use TRUNC to get the non-decimal part of a percentage,...

Related functions
-----------------

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel COUNT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20count%20function.png "Excel COUNT function")](https://exceljet.net/functions/count-function)

### [COUNT Function](https://exceljet.net/functions/count-function)

The Excel COUNT function returns a count of values that are numbers. Numbers include negative numbers, percentages, dates, times, fractions, and formulas that return numbers. Empty cells and text values are ignored....

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

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

*   [Data validation no punctuation](https://exceljet.net/formulas/data-validation-no-punctuation)
    
*   [Data validation allow numbers only](https://exceljet.net/formulas/data-validation-allow-numbers-only)
    
*   [Data validation allow text only](https://exceljet.net/formulas/data-validation-allow-text-only)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Data validation whole percentage only](https://exceljet.net/formulas/data-validation-whole-percentage-only)
    

### Functions

*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [COUNT Function](https://exceljet.net/functions/count-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [INDIRECT Function](https://exceljet.net/functions/indirect-function)
    

### Articles

*   [Excel Data Validation Guide](https://exceljet.net/articles/excel-data-validation-guide)
    

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