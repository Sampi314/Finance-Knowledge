# Extract numbers from text - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/extract-numbers-from-text

---

[Skip to main content](https://exceljet.net/formulas/extract-numbers-from-text#main-content)

[](https://exceljet.net/formulas/extract-numbers-from-text#)

*   [Previous](https://exceljet.net/formulas/extract-common-values-from-two-lists)
    
*   [Next](https://exceljet.net/formulas/filter-and-exclude-columns)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Extract numbers from text
=========================

by Dave Bruns · Updated 24 May 2024

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[TOROW](https://exceljet.net/functions/torow-function)

[DROP](https://exceljet.net/functions/drop-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8328/download?token=__1BhrvU)
 (14.85 KB)

![Excel formula: Extract numbers from text](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/extract_numbers_from_text.png "Excel formula: Extract numbers from text")

Summary
-------

To extract numbers from a text string, you can use a clever formula based on the [TEXTSPLIT](https://exceljet.net/functions/textsplit-function)
 and [TOROW](https://exceljet.net/functions/torow-function)
 functions. In the worksheet shown, the formula in cell C5 is:

    =DROP(TOROW(TEXTSPLIT(B5," ")+0,2),,1)

As the formula is copied down, it extracts the beds, baths, size, and lot information for each property listing. The numeric portion of the address function is discarded.

Generic formula
---------------

    TOROW(TEXTSPLIT(A1," ")+0,2)

Explanation 
------------

In this example, the goal is to extract the numbers from a set of property listings which describe the number of bedrooms and bathrooms, the size of the house in sq. ft., and the size of the lot in acres. Traditionally, this kind of problem has been quite difficult in Excel because each number must be extracted with a separate, carefully configured formula ([example](https://exceljet.net/formulas/split-dimensions-into-three-parts)
). However, in the latest version of Excel, new functions like TEXTSPLIT, TOROW, and DROP make the process _much easier._

### The approach

The overall approach in the worksheet shown above is to split the text in column B into separate words, remove all non-numeric words with a clever hack, and remove the first number, which represents the street number. The formula in cell C5, copied down, looks like this:

    =DROP(TOROW(TEXTSPLIT(B5," ")+0,2),,1)

Working from the inside out, the first step is to split the text string into separate words.

### Splitting text into words

To split the text strings in column B into separate words, we use the [TEXTSPLIT function](https://exceljet.net/functions/textsplit-function)
. TEXTSPLIT is a flexible function that can be configured with up to six arguments, but in this case, we need just two: text and column delimiter:

    TEXTSPLIT(B5," ") // split text into words

For _text_, we provide cell B5. For _col\_delimiter,_ we provide a single space (" "). With these inputs, TEXTSPLIT splits the text at each space and returns an array like this:

    {"1025","Maple","St,","4","beds","3","baths,","3200","sq.","ft.","on",".35","acre"}

Note that all values at this point are text strings, which Excel encloses in double quotes ("").

### Removing the non-numeric values

The next step in the process is to remove the non-numeric values. At first glance, this is a puzzle, because _all the values_ in the array are text, _including_ the numbers. This is one of those cases where the easiest solution is a hack that depends on knowing how the Excel formula engine works. Briefly, Excel tries to convert a text string to a number when it is involved in a math operation. For example, if we add 1 to a true number and a number that is text, it works in both cases:

    =100+1 // returns 101
    ="100"+1 // returns 101

This happens because Excel silently converts the text "100" into the number 100 and then proceeds with the addition. However, if we try to add a number to a text string that can't be converted to a number, the operation fails with a #VALUE! error:

    ="apple"+1 // returns #VALUE!

It turns out that we can use this behavior in this problem to easily remove the non-numeric values. First, we add zero to the result from TEXTSPLIT:

    TEXTSPLIT(B5," ")+0

As explained above, Excel will try to convert the text values returned by TEXTSPLIT into numbers. The result is an array like this:

    {1025,#VALUE!,#VALUE!,4,#VALUE!,3,#VALUE!,3200,#VALUE!,#VALUE!,#VALUE!,0.35,#VALUE!}

Notice #VALUE! errors have replaced the non-numeric text values, while the numbers have survived the operation and are now true numeric values. In other words, we have forced all text values to errors and converted text to numbers at the same time. Next, we need to discard the errors. While we could use the [FILTER function](https://exceljet.net/functions/filter-function)
 for this job, a simpler option is to use the [TOROW function](https://exceljet.net/functions/torow-function)
 like this:

    TOROW(TEXTSPLIT(B5," ")+0,2)

The purpose of TOROW is to transform an array into a single row. In this case, we already have a row, so we only use the TOROW function to remove errors, by setting the _ignore_ argument to 2. The result from this operation is a much cleaner array like this:

    {1025,4,3,3200,0.35}

With _ignore_ set to 2, TOROW removes the errors and leaves the numbers. Pretty cool, huh?

### Removing the street number

The last step in this problem is to remove the first number from the final result, which is a street number, and a characteristic of the property itself. We can do this with the [DROP function](https://exceljet.net/functions/drop-function)
, which is designed to remove rows or columns from an array. In this case, since we have already split the text into separate columns, we want to remove the _first_ column. We can do that by providing the number 1 for the _columns_ argument:

    =DROP({1025,4,3,3200,0.35},,1)

Notice the _rows_ argument is left empty. The final result is an array with four numbers like this:

    {4,3,3200,0.35}

This array spills into the range C5:F5. As the formula is copied down, the formula extracts the same information from each property as shown. 

### With the FILTER function

Just for the record, here is what a formula based on FILTER would look like, instead of TOCOL:

    =DROP(FILTER(TEXTSPLIT(B5," ")+0,ISNUMBER(TEXTSPLIT(B5," ")+0),2),,1)

The basic mechanics are the same. TEXTSPLIT creates an array of values, and adding zero forces the text values to errors, leaving numbers. The FILTER function then removes the errors by testing for numbers with the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
. However, because of the structure of FILTER, we need to repeat the TEXTSPLIT operation twice. The TOCOL solution avoids this redundancy, resulting in a compact, elegant formula.

Related formulas
----------------

[![Excel formula: Strip non-numeric characters](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/strip_non-numeric_characters.png "Excel formula: Strip non-numeric characters")](https://exceljet.net/formulas/strip-non-numeric-characters)

### [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)

In this example, the goal is to strip (i.e., remove) non-numeric characters from a text string with a formula. Until 2024, this was a tricky problem in Excel, partly because Excel did not support regex (Regular Expressions), and partly because there wasn't a good way to convert a text string into...

[![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")](https://exceljet.net/formulas/textsplit-get-numeric-values)

### [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel TOROW function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20torow%20function.png "Excel TOROW function")](https://exceljet.net/functions/torow-function)

### [TOROW Function](https://exceljet.net/functions/torow-function)

The Excel TOROW function transforms an array into a single row. By default, TOROW will scan values by row, but TOROW can also scan values by column.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/TEXTSPLIT_with_numbers_Play.png)](https://exceljet.net/videos/textsplit-with-numbers)

### [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

In this video, we'll take a look at how to handle numbers with the TEXTSPLIT function. One result of using the TEXTSPLIT function is that all output is text, and this can cause problems if you need numeric values. Let me illustrate with an example. In this worksheet, we have some comma-separated...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel_TEXTSPLIT_function_play.png)](https://exceljet.net/videos/excel-textsplit-function)

### [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)

In this video, we'll take a look at the TEXTSPLIT function. TEXTSPLIT is an Excel function designed to split text into separate cells using a given delimiter. In this worksheet, we have a list of email addresses. The goal is to split each email into a separate name and domain. As I start to enter...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Strip non-numeric characters](https://exceljet.net/formulas/strip-non-numeric-characters)
    
*   [TEXTSPLIT get numeric values](https://exceljet.net/formulas/textsplit-get-numeric-values)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [TOROW Function](https://exceljet.net/functions/torow-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    

### Videos

*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    
*   [Excel TEXTSPLIT function](https://exceljet.net/videos/excel-textsplit-function)
    

### Training

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