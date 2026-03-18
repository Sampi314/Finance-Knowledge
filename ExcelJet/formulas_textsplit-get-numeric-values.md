# TEXTSPLIT get numeric values - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/textsplit-get-numeric-values

---

[Skip to main content](https://exceljet.net/formulas/textsplit-get-numeric-values#main-content)

[](https://exceljet.net/formulas/textsplit-get-numeric-values#)

*   [Previous](https://exceljet.net/formulas/sum-numbers-with-text)
    
*   [Next](https://exceljet.net/formulas/tiered-discounts-based-on-quantity)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

TEXTSPLIT get numeric values
============================

by Dave Bruns · Updated 8 Feb 2024

Related functions 
------------------

[TEXTSPLIT](https://exceljet.net/functions/textsplit-function)

[VALUE](https://exceljet.net/functions/value-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[LET](https://exceljet.net/functions/let-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8194/download?token=xBFLsy3X)
 (14.93 KB)

![Excel formula: TEXTSPLIT get numeric values](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/TEXTSPLIT_get_numbers.png "Excel formula: TEXTSPLIT get numeric values")

Summary
-------

To get numeric values with TEXTSPLIT, you can use the IFERROR function with the VALUE function. In the worksheet shown, the formula in cell D5 is:

    =IFERROR(VALUE(TEXTSPLIT(B5,",")),TEXTSPLIT(B5,","))

The VALUE function converts numbers as text to numeric values. When this operation fails, IFERROR traps the error and returns the original text value. As the formula is copied down, the numbers are converted to numeric values, and the text values in column D are preserved. See below for a full explanation.

Generic formula
---------------

    =IFERROR(VALUE(TEXTSPLIT(A1,",")),TEXTSPLIT(A1,","))

Explanation 
------------

In this example, we have comma-separated text in column B. The goal is to split the text in column B into columns D through G while at the same time converting the numbers to true numeric values. The challenge is that TEXTSPLIT always returns text, so we need a way to convert the numbers while leaving the text values alone. 

To watch a video, see [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)

### The problem with TEXTSPLIT

To split the text in column B into separate columns, we can use the TEXTSPLIT function with a simple formula like this:

    TEXTSPLIT(B5,",")

This seems to work great. But the problem is that the numbers in columns E, F, and G aren't really _numeric values_. Instead, they are _text values,_ as you can see by the way Excel aligns them to the left:

![The problem with TEXTSPLIT and numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/TEXTSPLIT_get_numbers_basic_problem.png "The problem with TEXTSPLIT and numbers")

If you use a function like SUM to sum these numbers up, the result will be _zero_. How can convert these numbers as text to actual numeric values? Well, one option is to use the VALUE function.

### Adding the VALUE function

The [VALUE function](https://exceljet.net/functions/value-function)
 is designed to convert text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. If we wrap the VALUE function around the TEXTSPLIT function, this is the result:

![The VALUE function with the TEXTSPLIT function](https://exceljet.net/sites/default/files/images/formulas/inline/TEXTSPLIT_get_numbers_with_value_function.png "The VALUE function with the TEXTSPLIT function")

Notice the numbers in columns E, F, and G are now actually numeric values, as we can see by the way Excel right-aligns them. However, we now have a new problem — the VALUE function has corrupted the text values in column D. This happens because when VALUE tries to convert the text to a number, the operation fails with a #VALUE! error. What we need is a way to _selectively_ convert the "numbers as text" to numbers while leaving the text values alone. We can do that with the IFERROR function.

### Adding the IFERROR function

The [IFERROR function](https://exceljet.net/functions/iferror-function)
 returns a custom result when a formula generates an error, and a standard result when no error is detected. The syntax for IFERROR looks like this:

    =IFERROR(value,value_if_error)

To illustrate how this works, we can start by adding IFERROR like this:

    =IFERROR(VALUE(TEXTSPLIT(B5,",")),"x")

Notice we have simply embedded the original formula above into IFERROR as the value argument, then provided the value "x" for value\_if\_error. The result looks like this:

![Adding IFERROR to VALUE and TEXTSPLIT](https://exceljet.net/sites/default/files/images/formulas/inline/TEXTSPLIT_get_numbers_with_value_and_iferror.png "Adding IFERROR to VALUE and TEXTSPLIT")

The "x" in column D tells us that IFERROR has encountered an error in this column, which is created when VALUE tries to convert the text values into numbers. The final step is to replace the "x" with the original text value. We can do that by simply repeating the original TEXTSPLIT formula. The final formula looks like this:

    =IFERROR(VALUE(TEXTSPLIT(B5,",")),TEXTSPLIT(B5,","))

The result in the worksheet looks like this:

![Final formula - numbers are converted and text is unaffected](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/TEXTSPLIT_get_numbers_final_formula.png "Final formula - numbers are converted and text is unaffected")

### Optimizing with the LET function

The formula above works fine, but it would be inefficient with a large amount of data because we are running the same TEXTSPLIT operation twice. One way to improve performance is to use the [LET function](https://exceljet.net/functions/let-function)
 like this:

    =LET(array,TEXTSPLIT(B5,","),IFERROR(VALUE(array),array))

In this formula, the result from TEXTSPLIT is assigned to a variable named "array". We then use _array_ inside the IFERROR and VALUE functions as above. The key difference is that TEXTSPLIT runs _just one time_.

Related formulas
----------------

[![Excel formula: Split comma-separated values to multiple columns](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/split-comma-separated-values.png "Excel formula: Split comma-separated values to multiple columns")](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

### [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)

In this example, the goal is to split comma-separated values (CSV) in column B into multiple columns, as seen in the worksheet shown. Each text string in column B contains 5 fields separated by commas, so we expect to get 5 columns of data as a result. The header row in column D is manually entered...

Related functions
-----------------

[![Excel TEXTSPLIT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20textsplit%20function.png "Excel TEXTSPLIT function")](https://exceljet.net/functions/textsplit-function)

### [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)

The Excel TEXTSPLIT function splits text by a given delimiter to an array that spills into multiple cells. TEXTSPLIT can split text into rows or columns.

[![Excel VALUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20value%20function.png "Excel VALUE function")](https://exceljet.net/functions/value-function)

### [VALUE Function](https://exceljet.net/functions/value-function)

The Excel VALUE function converts text that appears in a recognized format (i.e. a number, date, or time format) into a numeric value. Normally, the VALUE function is not needed in Excel, because Excel automatically converts text to numeric values.

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

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

*   [Split comma-separated values to multiple columns](https://exceljet.net/formulas/split-comma-separated-values-to-multiple-columns)
    

### Functions

*   [TEXTSPLIT Function](https://exceljet.net/functions/textsplit-function)
    
*   [VALUE Function](https://exceljet.net/functions/value-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    

### Videos

*   [TEXTSPLIT with numbers](https://exceljet.net/videos/textsplit-with-numbers)
    

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