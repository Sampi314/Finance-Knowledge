# Pad a number with zeros - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/pad-a-number-with-zeros

---

[Skip to main content](https://exceljet.net/formulas/pad-a-number-with-zeros#main-content)

[](https://exceljet.net/formulas/pad-a-number-with-zeros#)

*   [Previous](https://exceljet.net/formulas/one-or-the-other-not-both)
    
*   [Next](https://exceljet.net/formulas/parse-xml-with-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Pad a number with zeros
=======================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

[REPT](https://exceljet.net/functions/rept-function)

![Excel formula: Pad a number with zeros](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/pad%20number%20with%20zeros.png "Excel formula: Pad a number with zeros")

Summary
-------

To pad a number with a variable number of zeros, you can use a formula based on the [TEXT function](https://exceljet.net/functions/rept-function)
 and the [REPT function](https://exceljet.net/functions/rept-function)
. In the example shown, the formula in D5 is:

    =TEXT(B5,REPT("0",C5))
    

As the formula is copied down, the numbers in column B are padded with a progressively larger number of zeros based on the number in column C. Note that the result is a [text value](https://exceljet.net/glossary/text-value)
.

Generic formula
---------------

    =TEXT(A1,REPT("0",n))

Explanation 
------------

In this example, the goal is to pad a number with zeros. To illustrate how Excel functions can be combined, the number of zeros to use is variable and comes from column C. The formula used to solve this problem combines the [TEXT function](https://exceljet.net/functions/rept-function)
 and the [REPT function](https://exceljet.net/functions/rept-function)
.

### Fixed number

The TEXT function returns a number formatted as text, using the [number format](https://exceljet.net/glossary/number-format)
 provided. The TEXT function can apply number formats of any kind to numbers. It is most often used when you want to maintain number formatting for a number when concatenating that number with other text. For example to use the TEXT function to pad a number 3, 4, and 5 zeros:

    =TEXT(17,"000") // returns "017"
    =TEXT(17,"0000") // returns "0017"
    =TEXT(17,"00000") // returns "00017"
    

Notice the [number format](https://exceljet.net/articles/custom-number-formats)
 works by adding zeros to the left as needed to reach the total number of zeros supplied.

### Variable number

To allow a variable number of zeros based on a number in another cell, we can add the REPT function into the mix. The REPT function simply repeats a text string a given number of times:

    =REPT("a",2) // returns "aa"
    =REPT("a",3) // returns "aaa"
    =REPT("a",4) // returns "aaaa"
    

So to pad a number with 5 zeros, we can use REPT to assemble the five zeros into  the text"00000":

    =TEXT(17,REPT("0",5)) // returns "00017"
    

The formula used in the example shown is simply a variation of the above formula. The formula in E9 evaluates like this:

    =TEXT(B9,REPT("0",C9))
    =TEXT(29,REPT("0",5))
    =TEXT(29,"00000")
    ="00029"
    

### Other characters

You can adapt this formula to use any character you like:

    =TEXT(29,REPT("*",5)) // returns "***29"
    =TEXT(29,REPT("-",5)) // returns "---29"
    

### Pad for display only

Padding a number with zeros with the TEXT function changes the number into text, which may not suit your needs. To simply _display_ a number with padding, you can use a regular [number format](https://exceljet.net/glossary/number-format)
. For example, to pad a number with 5 zeros for display only, select the cells and use the shortcut [Control + 1 to open the Format Cells](https://exceljet.net/shortcuts/format-almost-anything)
 window.  Then:

Format cells > Number > Custom > "00000"

With this approach, the number is not converted to text but remains a true number. [More details here](https://exceljet.net/formulas/add-leading-zeros-to-numbers)
.

Related formulas
----------------

[![Excel formula: Pad week numbers with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20week%20numbers%20with%20zeros.png "Excel formula: Pad week numbers with zeros")](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

### [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

The TEXT function can apply number formats of any kind, including currency, date, percentage, etc. By applying a number format like "00", "000", "0000", you can "pad" numbers with as many zeros as you like. Zeros will only be added where needed. Number format only The TEXT function converts numbers...

[![Excel formula: Add leading zeros to numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/add%20leading%20zeros%20to%20numbers.png "Excel formula: Add leading zeros to numbers")](https://exceljet.net/formulas/add-leading-zeros-to-numbers)

### [Add leading zeros to numbers](https://exceljet.net/formulas/add-leading-zeros-to-numbers)

In this example, the goal is to add leading zeros to a given number so that the total number of characters displayed is 5. Sometimes this is referred to as "padding" a number with zeros, because the number of zeros needed is variable. If the original number contains 2 digits, 3 zeros are added. If...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

[![Excel REPT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20rept%20function.png "Excel REPT function")](https://exceljet.net/functions/rept-function)

### [REPT Function](https://exceljet.net/functions/rept-function)

The Excel REPT function repeats characters a given number of times. For example, =REPT("x",5) returns "xxxxx".

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)
    
*   [Add leading zeros to numbers](https://exceljet.net/formulas/add-leading-zeros-to-numbers)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    
*   [REPT Function](https://exceljet.net/functions/rept-function)
    

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