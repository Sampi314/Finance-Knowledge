# Excel IFNA function | Exceljet

**Source:** https://exceljet.net/functions/ifna-function

---

[Skip to main content](https://exceljet.net/functions/ifna-function#main-content)

[](https://exceljet.net/functions/ifna-function#)

*   [Previous](https://exceljet.net/functions/iferror-function)
    
*   [Next](https://exceljet.net/functions/ifs-function)
    

Excel 2013

[Logical](https://exceljet.net/functions#Logical)

IFNA Function
=============

by Dave Bruns · Updated 6 Oct 2023

Related functions 
------------------

[ISERROR](https://exceljet.net/functions/iserror-function)

[IFERROR](https://exceljet.net/functions/iferror-function)

[ISNA](https://exceljet.net/functions/isna-function)

![Excel IFNA function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_ifna_function.png "Excel IFNA function")

Summary
-------

The Excel IFNA function is a simple way to handle #N/A errors specifically without catching other errors. The IFNA function allows you to specify a custom value or message to display instead of the #N/A error. If no error #N/A error occurs the formula returns a normal result.

Purpose 
--------

Trap and handle #N/A errors

Return value 
-------------

The value supplied for #N/A errors

Syntax
------

    =IFNA(value,value_if_na)

*   _value_ - The value, reference, or formula to check for an error.
*   _value\_if\_na_ - The value to return if #N/A error is found.

Using the IFNA function 
------------------------

The IFNA function is designed to manage #N/A errors and ignore other errors. When a function returns an #N/A, it typically indicates that a value is not available or not found. In many cases, an #N/A error is useful information because it tells you the formula is not able to find a value. However, the #N/A error can make users uncomfortable, because it might make it seem that there something is wrong with the worksheet. The IFNA function gives you a simple way to "catch" an #N/A error and provide another more user-friendly result. Unlike the more general IFERROR function, the IFNA function will only trap #N/A errors specifically; other errors will still be displayed. This is useful because it means the IFNA function won't accidentally hide another more serious error.

You can use the IFNA function to trap and handle #N/A errors that may occur in formulas that perform lookups, such as [VLOOKUP](https://exceljet.net/functions/vlookup-function)
, [MATCH](https://exceljet.net/functions/match-function)
, [HLOOKUP](https://exceljet.net/functions/hlookup-function)
, etc. The IFNA function returns a custom result when a formula generates the #N/A error, and a normal result when no error is detected. 

### Example

For example, in the worksheet shown, we are using VLOOKUP to find an item's price in the range B5:C16. The formula in F5, copied down, looks like this:

    =VLOOKUP(E5,$B$5:$C$16,2,FALSE)

Notice the formula works fine in the first three cells, correctly returning a price for Pear, Apple, and Orange. However, in cell F8 VLOOKUP returns #N/A because there is no entry for "Lime" in column B. The #N/A result essentially means "not found", but it is returned as an error on the worksheet. We can catch this error and return an alternative result with the IFNA function.

To use the IFNA function to trap #N/A errors, embed the original formula inside IFNA as the _first_ argument. In this case, we start off with the IFNA function:

    =IFNA(

Then we paste in the original formula like so:

    =IFNA(VLOOKUP(H5,$B$5:$C$16,2,FALSE),

Next, provide an alternative result as the _second_ argument. In the worksheet shown, we provide an empty string ("") so that the #N/A error is effectively hidden. The final formula in cell I5 looks like this:

    =IFNA(VLOOKUP(H5,$B$5:$C$16,2,FALSE),"")

Notice that the result in cells I5, I6, and I7 is unaffected; VLOOKUP returns the item price as before. However, in cell I8, we now see a blank cell. Inside IFNA, VLOOKUP returns #N/A as before. IFNA detects the #N/A error and returns an empty string ("") instead, which displays like an empty cell. If you would rather display a message like "Not found", simply modify the formula to include the message like this:

    =IFNA(VLOOKUP(H5,$B$5:$C$16,2,FALSE),"Not found")

Note that the message must be enclosed in double quotes. The screen below shows how this modified formula behaves on the worksheet:

![Example of IFNA with custom not found message](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_ifna_function_example.png "Example of IFNA with custom not found message")

### IFERROR vs IFNA

Like the IFNA function, the [IFERROR function](https://exceljet.net/functions/iferror-function)
 is designed to manage errors. In the worksheet shown, we can use IFERROR instead of IFNA like this:

    =IFERROR(VLOOKUP(H8,$B$5:$C$16,2,FALSE),"")

Notice the structure is exactly the same. The original formula appears as the first argument inside IFERROR and the custom result ("") is the second argument. However, unlike IFNA, IFERROR will catch any error. This makes IFERROR a more blunt instrument since it will trap many kinds of errors. For example, if a function name is misspelled, Excel will normally return the #NAME? error:

    =ZLOOKUP(H8,$B$5:$C$16,2,FALSE) // returns #NAME?

Above there is no function called "ZLOOKUP", so Excel returns #NAME?. IFERROR will catch this error as well, even though it has nothing to do with the operation of the formula:

    =IFERROR(ZLOOKUP(H8,$B$5:$C$16,2,FALSE),"") // returns ""

In other words, IFERROR may unintentionally hide other errors and obscure an important problem. As a result, it makes more sense to use the [IFNA function](https://exceljet.net/functions/ifna-function)
 if the intent is to manage #N/A errors only.

### Other error functions

Excel provides a number of error-related functions, each with a different behavior:

*   The [ISERR function](https://exceljet.net/functions/iserr-function)
     returns TRUE for any error type except the #N/A error.
*   The [ISERROR function](https://exceljet.net/functions/iserror-function)
     returns TRUE for any error.
*   The [ISNA function](https://exceljet.net/functions/isna-function)
     returns TRUE for #N/A errors only.
*   The [ERROR.TYPE function](https://exceljet.net/functions/errortype-function)
     returns the numeric code for a given error.
*   The [IFERROR function](https://exceljet.net/functions/iferror-function)
     traps errors and provides an alternative result.
*   The [IFNA function](https://exceljet.net/functions/ifna-function)
     traps #N/A errors and provides an alternative result.

### Notes

*   If _value_ is empty, it is evaluated as an empty string ("") and not an error.
*   If _value\_if\_na_ is supplied as an [empty string](https://exceljet.net/glossary/empty-string)
     (""), no message is displayed when an error is detected.

IFNA function examples
----------------------

[![Excel formula: XLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/XLOOKUP_without_NA_error.png "Excel formula: XLOOKUP without #N/A error")](https://exceljet.net/formulas/xlookup-without-na-error)

### [XLOOKUP without #N/A error](https://exceljet.net/formulas/xlookup-without-na-error)

In this example, we have a simple worksheet that uses the XLOOKUP function to lookup the name of a U.S. state when a valid two-letter code is provided as a lookup value. The goal is to remove the #N/A error that XLOOKUP returns when it can't find a result. Although you could use the IFNA or IFERROR...

[![Excel formula: Zodiac sign lookup](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/zodiac%20sign%20lookup_0.png "Excel formula: Zodiac sign lookup")](https://exceljet.net/formulas/zodiac-sign-lookup)

### [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)

The goal of this example is to look up the correct astrological or zodiac sign for a given birthdate, using the table shown in B5:F15. These are based on the Western zodiac signs described here . Zodiac signs are used in horoscopes, which are a kind of forecast of a person's future, based on the...

[![Excel formula: VLOOKUP without #N/A error](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_without_NA_error.png "Excel formula: VLOOKUP without #N/A error")](https://exceljet.net/formulas/vlookup-without-na-error)

### [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)

When VLOOKUP can't find a value in a lookup table, it returns the #N/A error. In this example, the goal is to remove the #N/A error that VLOOKUP returns when it can't find a lookup value. In general, the best way to do this is to use the IFNA function. However, the IFERROR function can also be used...

[![Excel formula: Make words plural](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/make%20words%20plural.png "Excel formula: Make words plural")](https://exceljet.net/formulas/make-words-plural)

### [Make words plural](https://exceljet.net/formulas/make-words-plural)

In this example, the goal is to make a noun plural when the number of items is greater than one. In many cases, a noun can be made plural by adding an "s". However, many nouns have an irregular plural form, and the main challenge is to handle these exceptions. Ingredients In the example shown, the...

[![Excel formula: Quantity based discount](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/quantity_based_discount.png "Excel formula: Quantity based discount")](https://exceljet.net/formulas/quantity-based-discount)

### [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)

The goal is to calculate discounts on a per-item and per-quantity basis using the discount table at the right in the workbook shown. The purpose of the discount table is to allow each item to have its own set of discounts. Notice that Donuts have a different discount for a quantity of 24. The...

Related functions
-----------------

[![Excel ISERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iserror%20function.png "Excel ISERROR function")](https://exceljet.net/functions/iserror-function)

### [ISERROR Function](https://exceljet.net/functions/iserror-function)

The Excel ISERROR function returns TRUE for any error type excel generates, including #N/A, #VALUE!, #REF!, #DIV/0!, #NUM!, #NAME?, or #NULL! You can use ISERROR together with the IF function to test for errors and display a custom message, or run a different calculation when an error occurs....

[![Excel IFERROR function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20iferror.png "Excel IFERROR function")](https://exceljet.net/functions/iferror-function)

### [IFERROR Function](https://exceljet.net/functions/iferror-function)

The Excel IFERROR function returns a custom result when a formula generates an error, and a standard result when no error is detected. IFERROR is an elegant way to trap and manage errors without using more complicated nested IF statements.

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP without #N/A error](https://exceljet.net/formulas/vlookup-without-na-error)
    
*   [Make words plural](https://exceljet.net/formulas/make-words-plural)
    
*   [Quantity based discount](https://exceljet.net/formulas/quantity-based-discount)
    
*   [XLOOKUP without #N/A error](https://exceljet.net/formulas/xlookup-without-na-error)
    
*   [Zodiac sign lookup](https://exceljet.net/formulas/zodiac-sign-lookup)
    

### Functions

*   [ISERROR Function](https://exceljet.net/functions/iserror-function)
    
*   [IFERROR Function](https://exceljet.net/functions/iferror-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    

### Links

*   [Microsoft IFNA function documentation](https://support.office.com/en-us/article/ifna-function-6626c961-a569-42fc-a49d-79b4951fd461)
    

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