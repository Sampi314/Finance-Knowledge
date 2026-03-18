# How to fix a circular reference error - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/how-to-fix-a-circular-reference-error

---

[Skip to main content](https://exceljet.net/formulas/how-to-fix-a-circular-reference-error#main-content)

[](https://exceljet.net/formulas/how-to-fix-a-circular-reference-error#)

*   [Previous](https://exceljet.net/formulas/two-way-summary-with-sumifs)
    
*   [Next](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)
    

[Errors](https://exceljet.net/formulas#Errors)

How to fix a circular reference error
=====================================

by Dave Bruns · Updated 30 Mar 2024

![Excel formula: How to fix a circular reference error](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/How%20to%20fix%20a%20circular%20reference%20error.png "Excel formula: How to fix a circular reference error")

Summary
-------

Circular reference errors occur when a formula refers back to its own cell. For example, in the example shown, the formula in F7 is:

    =F5+F6+F7
    

To resolve circular references, you'll need to find the cell(s) with incorrect cell references and adjust as needed. The article below provides more information and steps to resolve.

Explanation 
------------

A circular reference occurs when a formula refers directly to its own cell, or refers to another cell that depends on the original cell. This creates an infinite loop that cannot be resolved. For example, if cell A1 contains a formula that refers to B1, and B1 contains a formula that refers to A1, this creates a circular reference. Circular reference errors are not like other errors in Excel in that they don't display on the worksheet and don't have a numeric error code. To find circular references, navigate to Formulas > Error checking > Circular references. 

### Example

In the worksheet shown, the formula in F7 is:

    =F5+F6+F7
    

This creates a circular reference because the formula, entered in cell F7, refers to F7. This in turn throws off other formula results in D7, C11, and D11:

    =F7 // formula in C7
    =SUM(B7:C7) // formula in D7
    =SUM(C5:C9) // formula in C11
    =SUM(D5:D9) // formula in D11
    

Circular references can cause many problems (and a lot of confusion) because they may cause other formulas to return zero, or a different incorrect result.

### The circular reference error message

When a circular reference occurs in a spreadsheet, you'll see a warning like this:

_"There are one or more circular references where a formula refers to its own cell either directly or indirectly. This might cause them to calculate incorrectly. Try removing or changing these references, or moving the formulas to different cells."_

![Circular reference error message dialog](https://exceljet.net/sites/default/files/images/formulas/inline/circular%20error%20pop%20up%20message.png "Circular reference error message dialog")

This warning will appear sporadically while editing, or when a worksheet is opened.

### Finding and fixing circular references

To resolve circular references, you'll need to find the cell(s) with incorrect cell references and adjust as needed. However, unlike other errors (#N/A, #VALUE!, etc.) circular references don't appear directly in the cell. To find the source of a circular reference error, use the Error Checking menu on the Formulas tab of the ribbon.

![Error checking menu on Formulas tab of ribbon](https://exceljet.net/sites/default/files/images/formulas/inline/error%20checking%20menu%20on%20ribbon.png "Error checking menu on Formulas tab of ribbon")

Select the Circular References item to see the source of circular references:

![Show circular references in error checking menu](https://exceljet.net/sites/default/files/images/formulas/inline/show%20circular%20references%20in%20error%20checking%20menu.png "Show circular references in error checking menu")

Below, the circular reference has been fixed and other formulas now return the correct results:

![Circular reference fixed, formulas show correct results again](https://exceljet.net/sites/default/files/images/formulas/inline/circular%20references%20fixed.png "Circular reference fixed, formulas show correct results again")

Related formulas
----------------

[![Excel formula: How to fix the #N/A error ](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20NA%20error.png "Excel formula: How to fix the #N/A error ")](https://exceljet.net/formulas/how-to-fix-the-na-error)

### [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)

About the #N/A error The #N/A error appears when something can't be found or identified. It is often a useful error, because it tells you something important is missing – a product not yet available, an employee name misspelled, a color option that doesn't exist, etc. However, #N/A errors can also...

[![Excel formula: How to fix the #DIV/0! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20DIV%20error.png "Excel formula: How to fix the #DIV/0! error")](https://exceljet.net/formulas/how-to-fix-the-div0-error)

### [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)

About the #DIV/0! error The #DIV/0! error appears when a formula attempts to divide by zero, or a value equivalent to zero. Like other errors, the #DIV/0! is useful, because it tells you there is something missing or unexpected in a spreadsheet. You may see #DIV/0! errors when data is being entered...

[![Excel formula: How to fix the #REF! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20REF%20error.png "Excel formula: How to fix the #REF! error")](https://exceljet.net/formulas/how-to-fix-the-ref-error)

### [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)

About the #REF! error The #REF! error occurs when a reference is invalid. In many cases, this is because sheets, rows, or columns have been removed, or because a formula with relative references has been copied to a new location where references are invalid. In the example shown, the formula in C10...

[![Excel formula: How to fix the #NAME? error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NAME%20error.png "Excel formula: How to fix the #NAME? error")](https://exceljet.net/formulas/how-to-fix-the-name-error)

### [How to fix the #NAME? error](https://exceljet.net/formulas/how-to-fix-the-name-error)

The #NAME? error occurs when Excel can't recognize something. Frequently, the #NAME? occurs when a function name is misspelled, but there are other causes, as explained below. Fixing a #NAME? error is usually just a matter of correcting spelling or a syntax problem. The examples below show...

[![Excel formula: How to fix the #VALUE! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20VALUE%20error.png "Excel formula: How to fix the #VALUE! error")](https://exceljet.net/formulas/how-to-fix-the-value-error)

### [How to fix the #VALUE! error](https://exceljet.net/formulas/how-to-fix-the-value-error)

The #VALUE! error appears when a value is not the expected type. This can occur when cells are left blank, when a function expecting a number receives text value, or when dates are evaluated as text by Excel. Fixing a #VALUE! error is usually just a matter of entering the right kind of value. The #...

[![Excel formula: How to fix the #NUM! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NUM%20error.png "Excel formula: How to fix the #NUM! error")](https://exceljet.net/formulas/how-to-fix-the-num-error)

### [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)

The #NUM! error occurs in Excel formulas when a calculation can't be performed. For example, if you try to calculate the square root of a negative number, you'll see the #NUM! error. The examples below show formulas that return the #NUM error. In general, the fixing the #NUM! error is a matter of...

[![Excel formula: How to fix the #NULL! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20NULL%20error.png "Excel formula: How to fix the #NULL! error")](https://exceljet.net/formulas/how-to-fix-the-null-error)

### [How to fix the #NULL! error](https://exceljet.net/formulas/how-to-fix-the-null-error)

The #NULL! error is quite rare in Excel, and is usually the result of a typo where a space character is used instead of a comma (,) or colon (:) between two cell references. Technically, the space character is the "range intersect" operator and the #NULL! error is reporting that the two ranges do...

[![Excel formula: How to fix the #### (hashtag) error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/How%20to%20fix%20the%20%23%23%23%20error.png "Excel formula: How to fix the #### (hashtag) error")](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)

### [How to fix the #### (hashtag) error](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)

The "hashtag" error, a string of hash or pound characters like ####### is not technically an error, but it looks like one. In most cases, it indicates the column width is too narrow to display the value as formatted. You might run into this odd looking result in several situations: You apply number...

[![Excel formula: How to fix the #SPILL! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20SPILL%20error.png "Excel formula: How to fix the #SPILL! error")](https://exceljet.net/formulas/how-to-fix-the-spill-error)

### [How to fix the #SPILL! error](https://exceljet.net/formulas/how-to-fix-the-spill-error)

About spilling and the #SPILL! error With the introduction of Dynamic Arrays in Excel , formulas that return multiple values " spill " these values directly onto the worksheet. The rectangle that encloses the values is called the " spill range ". When data changes, the spill range will expand or...

[![Excel formula: How to fix the #CALC! error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/how%20to%20fix%20the%20calc%20error.png "Excel formula: How to fix the #CALC! error")](https://exceljet.net/formulas/how-to-fix-the-calc-error)

### [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)

With the introduction of Dynamic Arrays in Excel formulas , there is more emphasis on arrays . The #CALC! error occurs when a formula runs into a calculation error with an array. The #CALC! error is a "new" error in Excel, introduced with dynamic arrays. It will not appear in older versions of...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Excel%20formula%20error%20codes-thumb.png)](https://exceljet.net/videos/excel-formula-error-codes)

### [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)

In this video, we'll take a look at the error codes that Excel generates when there's something wrong with a formula. There are 8 error codes that you're likely to run into at some point as you work with Excel's formulas. First, we have the divide by zero error. You'll see this when a formula tries...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trace%20a%20formula%20error-thumb.png)](https://exceljet.net/videos/how-to-trace-a-formula-error)

### [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)

In this video we'll look at how to trace a formula error. Here we have a simple sales summary for a team of salespeople over a period of 4 months. You can see that we have monthly totals in the bottom row and totals for each salesperson in the last column. Below the table, we have a sales target...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20trace%20formula%20relationships-thumb.png)](https://exceljet.net/videos/how-to-trace-formula-relationships)

### [How to trace formula relationships](https://exceljet.net/videos/how-to-trace-formula-relationships)

In this video, we'll look at how to quickly find formulas and trace how they are related to one another using the concept of precedents and dependents. Here we have a simple model that shows the expense of making coffee at home vs. buying coffee in a coffee shop. Let's take a look through the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [How to fix the #N/A error](https://exceljet.net/formulas/how-to-fix-the-na-error)
    
*   [How to fix the #DIV/0! error](https://exceljet.net/formulas/how-to-fix-the-div0-error)
    
*   [How to fix the #REF! error](https://exceljet.net/formulas/how-to-fix-the-ref-error)
    
*   [How to fix the #NAME? error](https://exceljet.net/formulas/how-to-fix-the-name-error)
    
*   [How to fix the #VALUE! error](https://exceljet.net/formulas/how-to-fix-the-value-error)
    
*   [How to fix the #NUM! error](https://exceljet.net/formulas/how-to-fix-the-num-error)
    
*   [How to fix the #NULL! error](https://exceljet.net/formulas/how-to-fix-the-null-error)
    
*   [How to fix the #### (hashtag) error](https://exceljet.net/formulas/how-to-fix-the-hashtag-error)
    
*   [How to fix the #SPILL! error](https://exceljet.net/formulas/how-to-fix-the-spill-error)
    
*   [How to fix the #CALC! error](https://exceljet.net/formulas/how-to-fix-the-calc-error)
    

### Videos

*   [Excel formula error codes](https://exceljet.net/videos/excel-formula-error-codes)
    
*   [How to trace a formula error](https://exceljet.net/videos/how-to-trace-a-formula-error)
    
*   [How to trace formula relationships](https://exceljet.net/videos/how-to-trace-formula-relationships)
    

### Articles

*   [Excel Formula Errors](https://exceljet.net/articles/excel-formula-errors)
    
*   [Excel formulas and functions](https://exceljet.net/articles/excel-formulas-and-functions)
    
*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    
*   [29 ways to save time with Excel formulas](https://exceljet.net/articles/29-ways-to-save-time-with-excel-formulas)
    

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