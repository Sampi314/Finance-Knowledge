# Split dimensions into three parts - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/split-dimensions-into-three-parts

---

[Skip to main content](https://exceljet.net/formulas/split-dimensions-into-three-parts#main-content)

[](https://exceljet.net/formulas/split-dimensions-into-three-parts#)

*   [Previous](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    
*   [Next](https://exceljet.net/formulas/split-dimensions-into-two-parts)
    

[Text](https://exceljet.net/formulas#Text)

Split dimensions into three parts
=================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[LEFT](https://exceljet.net/functions/left-function)

[RIGHT](https://exceljet.net/functions/right-function)

[MID](https://exceljet.net/functions/mid-function)

[LEN](https://exceljet.net/functions/len-function)

[SUBSTITUTE](https://exceljet.net/functions/substitute-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7539/download?token=g8vWh3eD)
 (15.77 KB)

![Excel formula: Split dimensions into three parts](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/split_dimensions_into_three_parts.png "Excel formula: Split dimensions into three parts")

Summary
-------

To split dimensions like "100x50x25" into three separate parts, you can use a formula based on the TEXTSPLIT function. In the example shown, the formula in cell D5 is:

    =TEXTSPLIT(B5,"x")+0

The formula returns all three dimensions to cell D5, and the results [spill](https://exceljet.net/glossary/spill)
 into the range D5:F5.

_Note: in older versions of Excel without TEXTSPLIT, you can use more complicated formulas based on several functions. Both approaches are explained below. Also, if you don't want or need to use a formula, you can use Excel's [Text-to-Columns](https://exceljet.net/glossary/text-to-columns)
 feature._

Generic formula
---------------

    =TEXTSPLIT(A1,"x")+0

Explanation 
------------

In this example, the goal is to split the [text strings](https://exceljet.net/glossary/text-value)
 in column B, which contain three dimensions in the form "L x W x H", into 3 separate dimensions. One problem with dimensions entered as text is that they can't be used for any kind of calculation. So, in addition, we want our final dimensions to be _numeric_. In a problem like this, we need to identify the delimiter, which is the character (or characters), that separate each thing we want to extract. In this case, the delimiter is the "x" character. Note that the "x" has a space (" ") on either side, something we'll also need to handle. Also notice that the "x" appears in different locations, so we can't extract dimensions by position. 

There are two basic approaches to solving this problem. If you are using [Excel 365](https://exceljet.net/glossary/excel-365)
, the easiest solution is to use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
 as shown in the worksheet above. If you are using an older version of Excel without TEXTSPLIT, you can use more complicated formulas based on several functions, including  [LEFT](https://exceljet.net/functions/left-function)
, [RIGHT](https://exceljet.net/functions/right-function)
, [LEN](https://exceljet.net/functions/len-function)
, [SUBSTITUTE](https://exceljet.net/functions/substitute-function)
, and [FIND](https://exceljet.net/functions/find-function)
. Both approaches are explained below.

### TEXTSPLIT function

The TEXTSPLIT function is a great way to solve this problem, because it is so simple to use. To split dimensions into three parts, using the "x" as a delimiter, the formula in D5, copied down, is:

    =TEXTSPLIT(B5,"x")+0

The formula works in two steps. First, TEXTSPLIT splits the text in B5 using the "x". The result is a horizontal array that contains three elements, one for each dimension:

    ={"10 "," 5 "," 7"}+0

Notice the numbers are still surrounded by space. Our goal is to get actual numeric values, so in the second step, we simply add zero. This is a simple way of getting Excel's formula engine to coerce a text value to an actual number. The result is an array like this:

    ={10,5,7} // true numbers

Notice the double quotes ("") are gone, because the math operation of addition (+) changes the text values to actual numbers. The formula returns this result to cell D5, and the three dimensions [spill](https://exceljet.net/glossary/spill)
 into the range D5:F5.

_Note: one nice thing about the "add zero" trick, is that it doesn't matter if the number is surrounded by space characters or not. The numbers can be separated with " x " or  "x" in the original text string with the same result. However, if you are splitting values that are not meant to be numbers, you will want to remove the +0, otherwise the formula will return a #VALUE! error._

### Legacy Excel

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, we need to use more complicated formulas to accomplish the same thing. To get the first dimension (L), we can use a formula like this in D5:

    =LEFT(B5,FIND("x",B5)-1)+0
    

At a high level, this works by extracting text starting from the _left_ side. The number of characters to extract is calculated by locating the first "x" in the text using the FIND function, then subtracting 1:

    =LEFT(B5,FIND("x",B5)-1)+0
    =LEFT(B5,4-1)+0
    =LEFT(B5,3)+0
    ="10 "+0
    =10

To get the second dimension, we can use a formula like this in cell E5:

    =MID(B5,FIND("x",B5)+1,FIND("~",SUBSTITUTE(B5,"x","~",2))-FIND("x",B5)-1)+0
    

At a high level, this formula extracts the width (W) with the [MID function](https://exceljet.net/functions/mid-function)
, which returns a given number of characters starting at a given position in the next. The starting position is calculated with the [FIND function](https://exceljet.net/functions/find-function)
 like this:

    FIND("x",B5)+1
    

FIND simply locates the first "x" and returns the location (4) as a number. Then we add one to start at the first character _after_ "x":

    =FIND("x",B5)+1
    =4+1
    =5

The number of characters to extract, which is provided as _num\_chars_ to the MID function, is the most complicated part of the formula:

    FIND("~",SUBSTITUTE(B5,"x","~",2))-FIND("x",B5)-1
    

Working from the inside out, we use SUBSTITUTE with FIND to locate the position of the 2nd "x", [as described here](https://exceljet.net/formulas/position-of-2nd-3rd-etc-instance-of-character)
. We then subtract from that the location of the first "x" + 1.

    =FIND("~",SUBSTITUTE(B5,"x","~",2))-FIND("x",B5)-1
    =FIND("~","10 x 5 ~ 7")-FIND("x",B5)-1
    =8-FIND("x",B5)-1
    =8-4-1
    =3

The main trick here is that we are using the seldom seen _instance\_num_ argument in the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 to replace only the second instance of the "x" with a tilde (~), so that we can target the second instance of "x" with the FIND function in the next step.

Now that we've calculated the _start\_num_ and _num\_chars_, we can simplify the original MID formula to this:

    =MID(B5,5,3)+0
    =MID("10 x 5 x 7",5,3)+0
    =" 5 "+0
    =5

Note we are using the trick of adding zero again to force Excel to coerce the next to a number. Finally, to get the third dimension, we can use a formula like this in cell F5:

    =RIGHT(B5,LEN(B5)-FIND("~",SUBSTITUTE(B5,"x","~",2)))+0
    

This formula works a lot like the formula to get the second dimension above. At a high level, we are using the [RIGHT function](https://exceljet.net/functions/right-function)
 to extract text from the right. The main challenge is to calculate how many characters to extract, _num\_chars_, which is done again with FIND and SUBSTITUTE like this:

    LEN(B5)-FIND("~",SUBSTITUTE(B5,"x","~",2))

As above, we use 2 for _instance\_num_ argument in the [SUBSTITUTE function](https://exceljet.net/functions/substitute-function)
 to replace only the _second_ instance of the "x" with a tilde (~), so that we can target this instance of "x" with the FIND function in the next step:

    =LEN(B5)-FIND("~",SUBSTITUTE(B5,"x","~",2))
    =RIGHT(B5,10-8)+0
    =RIGHT(B5,2)+0
    =" 7"+0
    =7

The LEN function returns the total characters in the text string (10) and FIND returns 8 as the location of the second "x", so _num\_chars_ becomes 2 in the end. RIGHT returns the 2 characters from the right side of the text string (which includes a space) we add zero to the result to force Excel to change the next to a number.

Related formulas
----------------

[![Excel formula: Split dimensions into two parts](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split%20dimensions%20into%20two%20parts%20-%20left.png "Excel formula: Split dimensions into two parts")](https://exceljet.net/formulas/split-dimensions-into-two-parts)

### [Split dimensions into two parts](https://exceljet.net/formulas/split-dimensions-into-two-parts)

Background A common annoyance with data is that it may be represented as text instead of numbers. This is especially common with dimensions, which may appear in one text string that includes units, for example: 50 ft x 200 ft 153 ft x 324 ft Etc. In a spreadsheet, it's a lot more convenient to have...

[![Excel formula: Get first name from name](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_0.png "Excel formula: Get first name from name")](https://exceljet.net/formulas/get-first-name-from-name)

### [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)

In this example, the goal is to extract the first name from names that appear in <first> <middle> <last> format, where the middle name is optional. The easiest way to do this is with the newer TEXTBEFORE function. In older versions of Excel, you can use an alternative formula...

[![Excel formula: Get first name from name with comma](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/get_first_name_from_name_with_comma.png "Excel formula: Get first name from name with comma")](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

### [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)

In this example, the goal is to extract the first name from a list of names in "Last, First" format as seen in column B. There are several ways to approach this problem. In the current version of Excel, the easiest solution is to use the TEXTAFTER function. In older versions of Excel, it can be...

[![Excel formula: Split text string at specific character](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split_text_string_at_specific_character.png "Excel formula: Split text string at specific character")](https://exceljet.net/formulas/split-text-string-at-specific-character)

### [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)

In this example, the goal is to split a text string at the underscore("\_") character with a formula. Notice the location of the underscore is different in each row. This means the formula needs to locate the position of the underscore character first before any text is extracted. There are two...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel LEFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20left.png "Excel LEFT function")](https://exceljet.net/functions/left-function)

### [LEFT Function](https://exceljet.net/functions/left-function)

The Excel LEFT function extracts a given number of characters from the left side of a supplied text string. For example, =LEFT("apple",3) returns "app".

[![Excel RIGHT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_right_function.png "Excel RIGHT function")](https://exceljet.net/functions/right-function)

### [RIGHT Function](https://exceljet.net/functions/right-function)

The Excel RIGHT function extracts a given number of characters from the _right_ side of a supplied text string. For example, =RIGHT("apple",3) returns "ple".

[![Excel MID function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_mid_function.png "Excel MID function")](https://exceljet.net/functions/mid-function)

### [MID Function](https://exceljet.net/functions/mid-function)

The Excel MID function extracts a given number of characters from the middle of a supplied text string based on the provided starting location. For example, =MID("apple",2,3) returns "ppl".

[![Excel LEN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20len%20function.png "Excel LEN function")](https://exceljet.net/functions/len-function)

### [LEN Function](https://exceljet.net/functions/len-function)

The Excel LEN function returns the length of a given text string as the number of characters. LEN will also count characters in numbers, but number formatting is not included.

[![Excel SUBSTITUTE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_substitute.png "Excel SUBSTITUTE function")](https://exceljet.net/functions/substitute-function)

### [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)

The Excel SUBSTITUTE function replaces text in a given string by matching. You can use SUBSTITUTE to replace or completely remove matched text. SUBSTITUTE is case-sensitive and does not support wildcards....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_numbers_Play.png)](https://exceljet.net/videos/textsplit-with-numbers)

### [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

In this video, we'll take a look at how to handle numbers with the TEXTSPLIT function. One result of using the TEXTSPLIT function is that all output is text, and this can cause problems if you need numeric values. Let me illustrate with an example. In this worksheet, we have some comma-separated...

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
    
*   [Get first name from name](https://exceljet.net/formulas/get-first-name-from-name)
    
*   [Get first name from name with comma](https://exceljet.net/formulas/get-first-name-from-name-with-comma)
    
*   [Split text string at specific character](https://exceljet.net/formulas/split-text-string-at-specific-character)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [LEFT Function](https://exceljet.net/functions/left-function)
    
*   [RIGHT Function](https://exceljet.net/functions/right-function)
    
*   [MID Function](https://exceljet.net/functions/mid-function)
    
*   [LEN Function](https://exceljet.net/functions/len-function)
    
*   [SUBSTITUTE Function](https://exceljet.net/functions/substitute-function)
    

### Videos

*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    

### Training

*   [Dynamic Array Formulas](https://exceljet.net/training/dynamic-array-formulas)
    
*   [Core Formula](https://exceljet.net/training/core-formula)
    

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