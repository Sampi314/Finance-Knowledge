# Add leading zeros to numbers - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/add-leading-zeros-to-numbers

---

[Skip to main content](https://exceljet.net/formulas/add-leading-zeros-to-numbers#main-content)

[](https://exceljet.net/formulas/add-leading-zeros-to-numbers#)

*   [Previous](https://exceljet.net/formulas/abbreviate-state-names)
    
*   [Next](https://exceljet.net/formulas/all-dates-in-chronological-order)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Add leading zeros to numbers
============================

by Dave Bruns · Updated 6 Dec 2021

Related functions 
------------------

[TEXT](https://exceljet.net/functions/text-function)

![Excel formula: Add leading zeros to numbers](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/add%20leading%20zeros%20to%20numbers.png "Excel formula: Add leading zeros to numbers")

Summary
-------

To add leading zeros to a number, you can take one of two basic approaches: (1) convert the number to a [text value](https://exceljet.net/glossary/text-value)
 with leading zeros (2) apply a [number format](https://exceljet.net/glossary/number-format)
 to display the number with leading zeros. Both approaches are described below. In the example shown, the formula in D5 uses Option 1 to convert B5 to text:

    =TEXT(B5,"00000")
    

The result in column D is text – the number is embedded in a text string with the correct number of zeros. Read below for details and the steps needed to apply Option 2.

Generic formula
---------------

    =TEXT(A1,"00000")

Explanation 
------------

In this example, the goal is to add leading zeros to a given number so that the total number of characters displayed is 5. Sometimes this is referred to as "padding" a number with zeros, because the number of zeros needed is variable. If the original number contains 2 digits, 3 zeros are added. If the original number contains 3 digits, 2 zeros are added, and so on.

There are two basic ways to solve this problem: (1) convert the number to text with leading zeros (2) apply a custom number format to display the number with leading zeros. The best approach depends on your needs. If numbers really should be text values, use Option 1. If numbers need to remain numeric values, use Option 2. Both options are easy to implement, but Option 1 is more flexible.

### Option 1 - convert to text

A simple way to add leading zeros to a number is to use the [TEXT function](https://exceljet.net/functions/text-function)
. The TEXT function returns a number formatted as text, using the [number format](https://exceljet.net/glossary/number-format)
 provided. In this case, we want the final result to have five characters total, so the number format includes five zeros: "00000". This number format is used directly in the TEXT function as the _format\_text_ argument:

    =TEXT(B5,"00000") // returns "00127"
    

The result is the [text string](https://exceljet.net/glossary/text-value)
 "00127". Note that Excel will _automatically_ align text values to the left, but you can manually set alignment as desired. To replace the original numbers with the converted text values: first copy the converted values, then select the original numbers and use [Paste Special](https://exceljet.net/shortcuts/display-the-paste-special-dialog-box)
 > Values to overwrite the original numbers.

Related video: [How to do in place changes with Paste Special](https://exceljet.net/videos/how-to-do-in-place-changes-with-paste-special)

### Option 2 - apply number format

Another way to add leading zeros to a number is to apply a [custom number format](https://exceljet.net/articles/custom-number-formats)
 to display the numbers with leading zeros. The key thing to understand with this option is that the numeric values underneath are _not affected_. Applying a number format only changes the way the numbers are _displayed in Excel_.

To apply a number format to display leading zeros, select the values in F5:F16 and use the shortcut [Control + 1](https://exceljet.net/shortcuts/format-almost-anything)
 to display the Format Cells window:

![Format Cells dialog box](https://exceljet.net/sites/default/files/images/formulas/inline/add%20leading%20zeros%20to%20numbers%20format%20cells%201.png "Format Cells dialog box")

Then navigate to the Number tab, select "Custom" and enter 00000 in the "Type" input area:

![Select Number > Custom](https://exceljet.net/sites/default/files/images/formulas/inline/add%20leading%20zeros%20to%20numbers%20format%20cells%202.png "Select Number > Custom")

Note the Sample area will show an example of the format applied to the first cell in the selection. When you click "OK" the number format is applied and numbers are displayed with leading zeros. Note the formula bar will continue to show the numeric value in its original form:

![Numeric values unchanged by number format](https://exceljet.net/sites/default/files/images/formulas/inline/numeric%20values%20unchanged%20by%20numbe%20format.png "Numeric values unchanged by number format")

### Summary

Both options above work well for adding leading zeros to a number. The key difference is that Option 1 results in _text_, while Option 2 preserves the _number_. Be aware that you may need to cater to this difference in other formulas. For example, if you are performing a lookup operation with [VLOOKUP](https://exceljet.net/functions/vlookup-function)
 or [INDEX and MATCH](https://exceljet.net/articles/index-and-match)
, you must match the lookup value to the data. The formulas below show how this difference affects a VLOOKUP formula:

    =VLOOKUP("00127",range,column,FALSE) // look up text
    =VLOOKUP(127,range,column,FALSE) // look up number
    

[More on VLOOKUP here](https://exceljet.net/functions/vlookup-function)
.

Related formulas
----------------

[![Excel formula: Pad week numbers with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20week%20numbers%20with%20zeros.png "Excel formula: Pad week numbers with zeros")](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

### [Pad week numbers with zeros](https://exceljet.net/formulas/pad-week-numbers-with-zeros)

The TEXT function can apply number formats of any kind, including currency, date, percentage, etc. By applying a number format like "00", "000", "0000", you can "pad" numbers with as many zeros as you like. Zeros will only be added where needed. Number format only The TEXT function converts numbers...

[![Excel formula: Pad a number with zeros](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/pad%20number%20with%20zeros.png "Excel formula: Pad a number with zeros")](https://exceljet.net/formulas/pad-a-number-with-zeros)

### [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)

In this example, the goal is to pad a number with zeros. To illustrate how Excel functions can be combined, the number of zeros to use is variable and comes from column C. The formula used to solve this problem combines the TEXT function and the REPT function . Fixed number The TEXT function...

Related functions
-----------------

[![Excel TEXT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_text_function.png "Excel TEXT function")](https://exceljet.net/functions/text-function)

### [TEXT Function](https://exceljet.net/functions/text-function)

The Excel TEXT function returns a number formatted as text. This makes it easy to embed a formatted number (e.g., dates, times, currencies, percentages, fractions, etc.) in a text string with the number format of your choice.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20combine%20functions%20in%20a%20formula-thumb.png)](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

### [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)

In this video I'm going to show you how you can use multiple Excel functions to split, manipulate, and rejoin values inside a single formula. Here we have some sample data and, in column B, we have text values with a number at the end. What we want to do is increment these numbers using the value...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Paste%20special%20Shortcuts-thumb.png)](https://exceljet.net/videos/shortcuts-for-paste-special)

### [Shortcuts for paste special](https://exceljet.net/videos/shortcuts-for-paste-special)

In this video, we'll review shortcuts and commands for Paste Special. As you might already know, Paste special is a gateway to many powerful operations in Excel. To use Paste Special, just copy normally, then use the shortcut Ctrl + Alt + V in Windows, Ctrl + Command + V on the Mac. Using this...

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
    
*   [Pad a number with zeros](https://exceljet.net/formulas/pad-a-number-with-zeros)
    

### Functions

*   [TEXT Function](https://exceljet.net/functions/text-function)
    

### Videos

*   [How to combine functions in a formula](https://exceljet.net/videos/how-to-combine-functions-in-a-formula)
    
*   [Shortcuts for paste special](https://exceljet.net/videos/shortcuts-for-paste-special)
    

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