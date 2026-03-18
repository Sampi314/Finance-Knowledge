# CONCAT & TEXTJOIN | Exceljet

**Source:** https://exceljet.net/articles/concat-textjoin

---

[Skip to main content](https://exceljet.net/articles/concat-textjoin#main-content)

[](https://exceljet.net/articles/concat-textjoin#)

*   [Previous](https://exceljet.net/articles/the-eomonth-function-formula-friday)
    
*   [Next](https://exceljet.net/articles/named-ranges)
    

CONCAT & TEXTJOIN
=================

by Dave Bruns · Updated 20 Oct 2022

![Fiddles with new CONCAT & TEXTJOIN functions](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/CONCAT%26TEXTJOIN.png "Fiddles with new CONCAT & TEXTJOIN functions")

Summary
-------

The CONCAT and TEXTJOIN functions make it possible to join values together in a range of cells. Since a range is just an array, this opens the door to some interesting new formulas that loop through values.

I've been playing around with the [TEXTJOIN](https://exceljet.net/functions/textjoin-function)
 and [CONCAT](https://exceljet.net/functions/concat-function)
 functions this week. These are both new functions in Excel 2016, introduced in the Office 365 subscription service.

Both of these functions let you join (concatenate) text in different cells together. TEXTJOIN lets you join values with a delimiter of your choice, and has an option to ignore empty values. CONCAT simply mashes all values together without options.

What's nice about both of these functions is that they can handle cell ranges.

That means you can do things like this:

![Concatenation with CONCAT and TEXTJOIN](https://exceljet.net/sites/default/files/images/articles/inline/concat%20and%20textjoin%20functions.png "Concatenation with CONCAT and TEXTJOIN")

    =TEXTJOIN(" ",TRUE,B4:H4) // J4
    =CONCAT(B7:H7) // J7
    

Maybe you're old enough to recognize [that number](https://www.youtube.com/watch?v=6WTdTwcmxyo)
? :)

The ability to handle ranges is cool, because it makes it trivial to concatenate a large collection of cells with a simple formula - something that required [annoying workarounds](https://exceljet.net/formulas/join-cells-with-comma)
 previously.

But I'm also intrigued about how this might be useful \*inside\* other formulas. In most programming languages, its common to split values into arrays, and join values back together again, after some kind of processing. For example, VBA has SPLIT and JOIN, and PHP has EXPLODE and IMPLODE, etc.

Inside an Excel formula, it's not too hard to split values into an array:

    =MID("apple",{1,2,3,4,5},1) // returns {"a","p","p","l","e"}
    

But once you have {"a","p","p","l","e"}, how you can you put it back together again?

Turns out, CONCAT and TEXTJOIN will let you do it, which solves a problem that's bugged me for a long time:

    =CONCAT({"a","p","p","l","e"}) // returns "apple"
    =TEXTJOIN("",TRUE,{"a","p","p","l","e"}) // returns "apple"
    

### Why does it matter?

To be honest, I'm not entirely how useful this is, since I've just started fiddling around with these functions. However, I think this might open the door to some interesting formulas that process values by looping through looping arrays. Here are a few ideas you might find interesting:

**1\. Uppercase text**

    =TEXTJOIN("",TRUE,(CHAR(CODE(MID(A1,{1,2,3,4,5},1))-32)))
    

The example above will uppercase "apple" > "APPLE" in A1. It's a silly example, since you can do the same thing more easily with the UPPER function. But I think it shows nicely how you can loop through each character, make changes, then bring it all back together again with TEXTJOIN.

**2\. Strip non-numeric characters**

![Stripping non-numeric characters with the TEXTJOIN function](https://exceljet.net/sites/default/files/images/articles/inline/textjoin_strip_non_numeric.png "Stripping non-numeric characters with the TEXTJOIN function")

    {=TEXTJOIN("",TRUE,IFERROR(MID(A1,ROW(INDIRECT("1:100")),1)+0,""))}
    

_Note: this is an array function - use control + shift + enter._

This example will strip all non-numeric characters in A1. So, for example, you can take a phone number like "(801)-654-4466" and turn it into "8016544466", which can then be formatted using a custom number format. You can do this same thing with the SUBSTITUTE function, but it's more work. If you're curious, here is a [detailed explanation](https://exceljet.net/formulas/strip-non-numeric-characters)
 of how this formula works.

More examples of [TEXTJOIN formulas](https://exceljet.net/functions/textjoin-function)
.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

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