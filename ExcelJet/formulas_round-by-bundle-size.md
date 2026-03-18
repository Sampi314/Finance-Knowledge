# Round by bundle size - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/round-by-bundle-size

---

[Skip to main content](https://exceljet.net/formulas/round-by-bundle-size#main-content)

[](https://exceljet.net/formulas/round-by-bundle-size#)

*   [Previous](https://exceljet.net/formulas/round-a-price-to-end-in-99)
    
*   [Next](https://exceljet.net/formulas/round-number-to-n-significant-figures)
    

[Round](https://exceljet.net/formulas#Round)

Round by bundle size
====================

by Dave Bruns · Updated 15 May 2024

Related functions 
------------------

[CEILING](https://exceljet.net/functions/ceiling-function)

![Excel formula: Round by bundle size](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/round_by_bundle_size_0.png "Excel formula: Round by bundle size")

Summary
-------

To round up to the next bundle size, you can use the [CEILING function](https://exceljet.net/functions/ceiling-function)
 which automatically rounds up to a given multiple. In the worksheet shown, the formula in cell D5 is:

    =CEILING(B5,C5)/C5
    

As the formula is copied down, it returns the total number of bundles needed, given the items needed in column B and the bundle size in column C.

Generic formula
---------------

    =CEILING(items_needed/bundle_size,1)

Explanation 
------------

In this example, the context is that a certain number of items are needed and the items are only available in bundles of a set size. The goal is to calculate the number of bundles needed based on the items in each bundle, and the number of items needed. For example:

*   If you need 6 items, and the bundle size is 2, you'll need 3 bundles and have zero extra items.
*   If you need 7 items, and the bundle size is 6, you'll need 2 bundles and you'll have 5 extra items.
*   If you need 13 items, and the bundle size is 3, you'll need 5 bundles and have 2 extra items.

Column B lists the number of items needed, and Column C specifies the bundle size. The worksheet calculates the number of bundles needed in Column D and the extra items in Column E. 

### The CEILING function

In the worksheet shown, the solution is based on the [CEILING function](https://exceljet.net/functions/ceiling-function)
 which is designed to round a number up to a given multiple. If the number is already an exact multiple, no rounding occurs and the original number is returned. Here are a few examples of how CEILING works using 5 as the multiple to round to:

    =CEILING(3,5) // returns 5
    =CEILING(5,5) // returns 5
    =CEILING(7,5) // returns 10
    =CEILING(11,5) // returns 15
    

CEILING can also be used with decimal values up to the next whole number by providing 1 as the significance argument:

    =CEILING(1.1,1) // returns 2
    =CEILING(2.4,1) // returns 3
    =CEILING(3,1) // returns 3
    =CEILING(4.6,1) // returns 5
    

Notice that CEILING _always rounds up_, even when the decimal portion of the number is small.

### Calculating bundles needed

To calculate the number of bundles needed, the formula in cell D5 is:

    =CEILING(B5/C5,1)

This formula calculates the exact number of bundles needed and then uses CEILING to round up to the next whole number to get the number. First, we divide the items needed by the bundle size:

    =B5/C5 // returns 3

Since the bundle items needed is 6 and the bundle size is 2, the result is 3. Then we use the CEILING function to round up the result:

    =CEILING(3,1) // returns 3

Since 3 is already a whole number, CEILING returns 3. In the next row, 7 items are needed and the bundle size is 6. The formula calculates 2 bundles needed like this:

    =CEILING(B6/C6,1)
    =CEILING(1.16666666666667,1)
    =2

### Alternative formula

Of course, in Excel, there is always another way to solve the problem :) Since CEILING can round up to any multiple, you can also calculate the bundles needed with a formula like this:

    =CEILING(B5,C5)/C5

This formula first rounds up the number of items needed to the nearest bundle size. Then it divides the result by the bundle size to get the number of bundles needed. First, we use the CEILING function to round up the number of items needed (B5) to the nearest multiple of the bundle size (C5):

    =CEILING(B5,C5) // returns 6
    

With 6 items needed and 2 items per bundle, the result is 6. Next, we divide the result from CEILING by the bundle size (C5) to get the number of bundles needed. Since there are 2 items per bundle, the final result is 3:

    =CEILING(B5,C5)/C5
    =6/2
    =3

Both formulas return the same result by using CEILING in different ways. The first formula is simpler and more direct, but the second formula might be more intuitive to some people and works just as well.

### Calculating extra items

Since the items needed will not always be an even multiple of the bundle size, there will be extra items in some cases. To calculate how many extra items are needed, you can use a formula like this in cell E5:

    =(D5*C5)-B5

This formula works by calculating the total number of items in the needed bundles (D5 \* C5) and subtracting the actual number of items needed (B5). The result is the number of extra items in the last bundle. Notice that the result is sometimes zero because the items needed are an even multiple of the bundle size.

Related formulas
----------------

[![Excel formula: Round a number up to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20up%20to%20nearest%20multiple.png "Excel formula: Round a number up to nearest multiple")](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

### [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)

The Excel CEILING function rounds a number up to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. CEILING works like the MROUND function , but unlike MROUND, which rounds to the...

[![Excel formula: Round a number down to nearest multiple](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/round%20a%20number%20down%20to%20nearest%20multiple.png "Excel formula: Round a number down to nearest multiple")](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

### [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)

The Excel FLOOR function rounds a number down to a given multiple. The multiple to use for rounding is given as the second argument ( significance ). If the number is already an exact multiple, no rounding occurs. FLOOR works like the MROUND function , but unlike MROUND, which rounds to the nearest...

Related functions
-----------------

[![Excel CEILING function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20ceiling%20function.png "Excel CEILING function")](https://exceljet.net/functions/ceiling-function)

### [CEILING Function](https://exceljet.net/functions/ceiling-function)

The Excel CEILING function rounds a given number _up_ to the nearest specified multiple. CEILING works like the [MROUND function](https://exceljet.net/functions/mround-function)
, but CEILING _always rounds up_.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Round a number up to nearest multiple](https://exceljet.net/formulas/round-a-number-up-to-nearest-multiple)
    
*   [Round a number down to nearest multiple](https://exceljet.net/formulas/round-a-number-down-to-nearest-multiple)
    

### Functions

*   [CEILING Function](https://exceljet.net/functions/ceiling-function)
    

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