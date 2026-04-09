# Split numbers from units of measure - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-numbers-from-units-of-measure

---

[Skip to main content](https://exceljet.net/formulas/split-numbers-from-units-of-measure#main-content)

[](https://exceljet.net/formulas/split-numbers-from-units-of-measure#)

*   [Previous](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Next](https://exceljet.net/formulas/split-text-and-numbers)
    

[Text](https://exceljet.net/formulas#Text)

Split numbers from units of measure
===================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[VALUE](https://exceljet.net/functions/value-function)

[MID](https://exceljet.net/functions/mid-function)

![Excel formula: Split numbers from units of measure](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Split%20numbers%20and%20units.png "Excel formula: Split numbers from units of measure")

Summary
-------

To split a number from a unit value, you can use a formula based on several functions: [MAX](https://exceljet.net/functions/max-function)
, [ISNUMBER](https://exceljet.net/functions/isnumber-function)
, [VALUE](https://exceljet.net/functions/value-function)
, and [MID](https://exceljet.net/functions/mid-function)
. In the example shown, the formula in C5 is:

    =MAX(ISNUMBER(VALUE(MID(B5,{1,2,3,4,5,6,7,8,9},1)))*{1,2,3,4,5,6,7,8,9})+1
    

_Note: this is an experimental formula that uses a hard-coded [array constant](https://exceljet.net/glossary/array-constant)
, set down here for reference and comment. Casually tested only, so take care if you use or adapt it._

Generic formula
---------------

    =MAX(ISNUMBER(VALUE(MID(A1,{1,2,3,4,5,6,7,8,9},1)))*{1,2,3,4,5,6,7,8,9})+1

Explanation 
------------

Sometimes you encounter data that mixes units directly with numbers (i.e. 8km, 12v, 7.5hrs). Unfortunately, Excel will treat the numbers in this format as text,  and you won't be able to perform math operations on such values.

To split a number from a unit value, you need to determine the position of the _last number_.  If you add 1 to that position, you have the start of the unit text. This formula uses this concept to figure out where the unit of measure begins.

In the example shown, the formula in C5 is:

    =MAX(ISNUMBER(VALUE(MID(B5,{1,2,3,4,5,6,7,8,9},1)))*{1,2,3,4,5,6,7,8,9})+1
    

This formula uses the [MID function](https://exceljet.net/functions/mid-function)
 to extract the first 9 values in B5, one character at a time:

    MID(B5,{1,2,3,4,5,6,7,8,9},1)

The array constant {1,2,3,4,5,6,7,8,9} is just a simple hack to extract up to 9 characters from a cell value into an [array](https://exceljet.net/glossary/array)
. The result looks like this:

    {"8","0","v","","","","","",""}
    

We then use the VALUE function to convert numbers in text format to actual numbers. The result is:

    {8,0,#VALUE!,#VALUE!,#VALUE!,#VALUE!,#VALUE!,#VALUE!,#VALUE!}
    

We run this array through ISNUMBER to get:

    {TRUE,TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE}
    

Then multiply that times another array with 9 numbers to get:

    {1,2,0,0,0,0,0,0,0}
    

We use MAX to get the largest value, which is the position of the "last number", then we add 1 to the position to get the "unit start" position. Finally, we use this position with standard LEFT and RIGHT functions to separate the numbers from the units:

    =VALUE(LEFT(B5,C5-1)) // number
    =TRIM(RIGHT(B5,LEN(B5)-C5+1)) // unit
    

Note that the hard-coded number array constant is a hack for convenience, and will only handle raw values up to 9 characters in length.

Related formulas
----------------

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Split text and numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20text%20and%20numbers.png "Excel formula: Split text and numbers")](https://exceljet.net/formulas/split-text-and-numbers)

### [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)

Overview The formula looks complex, but the mechanics are in fact quite simple. As with most formulas that split or extract text, the key is to locate the position of the thing you are looking for. Once you have the position, you can use other functions to extract what you need. In this case, we...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

[![Excel formula: Normalize size units to Gigabytes](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/normalize%20units%20to%20gigabytes.png "Excel formula: Normalize size units to Gigabytes")](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

### [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)

Important: This formula assumes that units are the last 2 characters of the text value that includes both a number and a unit of measure. This formula works because digital units have a "power of 10" relationship. At the core, this formula separates the number part of the size from the unit, then...

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    
*   [Split text and numbers](https://exceljet.net/formulas/split-text-and-numbers)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    
*   [Normalize size units to Gigabytes](https://exceljet.net/formulas/normalize-size-units-to-gigabytes)
    
*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    

### Links

*   [Inspiration from Rick Rothstein's formulas on MrExcel](http://www.mrexcel.com/forum/excel-questions/749876-separate-text-numbers.html)
    

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