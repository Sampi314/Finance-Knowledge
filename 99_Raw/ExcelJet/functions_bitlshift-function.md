# Excel BITLSHIFT function | Exceljet

**Source:** https://exceljet.net/functions/bitlshift-function

---

[Skip to main content](https://exceljet.net/functions/bitlshift-function#main-content)

[](https://exceljet.net/functions/bitlshift-function#)

*   [Previous](https://exceljet.net/functions/bitand-function)
    
*   [Next](https://exceljet.net/functions/bitor-function)
    

Excel 2013

[Engineering](https://exceljet.net/functions#Engineering)

BITLSHIFT Function
==================

by Kurt Bruns · Updated 17 Oct 2018

Related functions 
------------------

[BITRSHIFT](https://exceljet.net/functions/bitrshift-function)

![Excel BITLSHIFT function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_bitlshift.png "Excel BITLSHIFT function")

Summary
-------

The Excel BITLSHIFT function shifts a number by the specified number of bits, effectively doubling or halving the number a specified number of times.

Purpose 
--------

Returns a number shifted left by some number of bits

Return value 
-------------

Decimal Number

Syntax
------

    =BITLSHIFT(number,shift_amount)

*   _number_ - The number to be bit shifted.
*   _shift\_amount_ - The amount of bits to shift, if negative shifts bits to the right instead.

Using the BITLSHIFT function 
-----------------------------

For any bit shift that results in integer overflow, where the result is larger than 2^48 -1, the function returns the #NUM! error.

### How It Works

The shift\_amount can either be positive or negative. If a negative number is provided, the bits are shifted to the right instead.

![BITLSHIFT Internal Binary Representation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_bitlshift_internal_representation1.png?itok=q5mC2S-A "BITLSHIFT Internal Binary Representation")

Related functions
-----------------

[![Excel BITRSHIFT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_bitrshift1.png "Excel BITRSHIFT function")](https://exceljet.net/functions/bitrshift-function)

### [BITRSHIFT Function](https://exceljet.net/functions/bitrshift-function)

The Excel BITRSHIFT function shifts a number by the specified number of bits, effectively halving or doubling the number a specified number of times.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [BITRSHIFT Function](https://exceljet.net/functions/bitrshift-function)
    

### Links

*   [Microsoft BITLSHIFT function documentation](https://support.office.com/en-us/article/bitlshift-function-c55bb27e-cacd-4c7c-b258-d80861a03c9c)
    

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