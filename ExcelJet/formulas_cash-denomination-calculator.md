# Cash denomination calculator - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/cash-denomination-calculator

---

[Skip to main content](https://exceljet.net/formulas/cash-denomination-calculator#main-content)

[](https://exceljet.net/formulas/cash-denomination-calculator#)

*   [Previous](https://exceljet.net/formulas/carry-on-baggage-inches-to-centimeters)
    
*   [Next](https://exceljet.net/formulas/celsius-to-fahrenheit-conversion)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Cash denomination calculator
============================

by Dave Bruns · Updated 4 Mar 2025

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[INT](https://exceljet.net/functions/int-function)

[LET](https://exceljet.net/functions/let-function)

[SCAN](https://exceljet.net/functions/scan-function)

[MOD](https://exceljet.net/functions/mod-function)

[DROP](https://exceljet.net/functions/drop-function)

[HSTACK](https://exceljet.net/functions/hstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8927/download?token=RcZ3HKz1)
 (33.65 KB)

![Excel formula: Cash denomination calculator](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/cash_denomination_calculator.png "Excel formula: Cash denomination calculator")

Summary
-------

To calculate how many bills and coins of different denominations are needed to achieve a certain cash value, you can build a currency calculation table and use the [INT function](https://exceljet.net/functions/int-function)
 with the [SUM function](https://exceljet.net/functions/sum-function)
 to calculate a count for each denomination. In the example shown, the formula in D5 (copied across) is:

    =INT(($B5-SUM($C$4:C$4*$C5:C5))/D$4)
    

As the formula is copied across and down, it calculates the correct count for each denomination shown in D4:I4. The formula in column K checks that the denomination counts add up to the original amount. The denominations in row 4 can be customized as needed to account for different currencies.

> _Note: The worksheet shown shows a traditional approach involving carefully constructed cell references. You can also solve this problem with a more modern dynamic array formula option, which is explained below._

Generic formula
---------------

    =INT((amount-SUM(denoms,counts))/currentdenom)

Explanation 
------------

In this example, the goal is to build a "cash denomination calculator." A cash denomination calculator is a tool for counting and verifying cash amounts. It can calculate the denominations needed to achieve a certain cash value. It can also perform the reverse calculation and determine the cash value of a group of bills and coins of different denominations. Since we are building this tool in Excel, we also want to make it easy to customize the denominations to account for different currencies.

This article explores two ways to solve this problem. First, we look at a traditional approach using SUM, INT, and carefully constructed cell references. Next, we look at a modern [dynamic array formula](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 based on the SCAN function. Both approaches are designed to calculate all denominations for a given amount with the same basic formula. This is more difficult, but one smart reusable formula is much better than separate formulas to calculate each denomination.

### The worksheet layout

In the worksheet shown, the denominations appear in the range D4:I4, and the range B5:B16 contains sample inputs. The calculations occur in the range D5:I16. Column K contains a formula to check that the calculated denominations in D5:I16 add up to the original amount in column B. For example, for $32, the result should be 1 x $20, 1 x $10, and 2 x $1, which add up to $32.

> Note: the denomination amounts can be changed to handle different currencies. You can also add columns to handle coins. For example, in the US, you could insert columns for $0.25, $0.10, $0.05, and $0.01 to handle quarters, dimes, nickels, and pennies. 

The calculation for each denomination is quite easy and can be done with the [INT function](https://exceljet.net/functions/int-function)
 like this:

    =INT(amount/denomination)

After dividing the amount by a denomination, the INT function returns only the integer portion of the result. For a given denomination, this gives us the number of whole denominations that fit into the amount. However, for this problem, the main challenge is to account for the denominations _already counted_ before we count the next smallest denomination. In other words, as we move from left to right across the table, we must reduce the amount by the value of all denominations _already counted_.

### Method 1: SUM and INT

A classic and traditional way to solve this problem is with the [SUM function](https://exceljet.net/functions/sum-function)
 and [INT function](https://exceljet.net/functions/int-function)
, and carefully configured cell references. This is the approach seen in the worksheet above, where the formula in cell D5 looks like this:

    =INT(($B5-SUM($C$4:C$4*$C5:C5))/D$4)

_Note: this is an array formula in Excel 2019 and older and must be entered with control + shift + enter. In Excel 2021+, the formula will work without special handling._

At the core, this formula uses the =INT(amount/denomination) formula explained above to work out denomination counts. The challenge is that we also need to account for any denominations _already_ counted, so the references are carefully constructed so that certain ranges expand as the formula is copied to the right. Notice the following:

*   $B5 - is a [mixed reference](https://exceljet.net/glossary/mixed-reference)
     to lock the column.
*   $C$4:C$4 - is a mixed and [expanding reference](https://exceljet.net/glossary/expanding-reference)
    .
*   $C5:C5 - is an expanding reference.
*   Column C is blank, yet we include it in the formula.

Working from the inside out, we begin with the original amount in column B, then subtract the value of the denominations already counted:

    =$B5-SUM($C$4:C$4*$C5:C5)

The tricky part is the [expanding ranges](https://exceljet.net/glossary/expanding-reference)
 inside SUM. The first, $C$4:C$4, refers to the denominations in row 4. The second, $C5:C5, refers to previously counted denominations. Inside SUM, we multiply the denominations by their counts to calculate the _value_ of previous denominations. The SUM function calculates a total, which is subtracted from the original amount in B5. As the formula is copied to the right, these ranges will expand to accommodate more previous counts. 

> Why we are starting with column C, which is empty? We start with column C because we want to avoid having to use a different formula in the first column, which has no previous denominations. Because of the way the formula is set up, the sum of "previous" denominations in column C is zero, which means the full amount in B5 will be used in the first column. Once the formula is entered in D5, it can be copied right to column I, then down to row 16 without any modifications.

After the above calculations, we have the remaining amount. Next, we divide the remaining amount by the denomination in row 4 and feed the result into the INT function, which returns the whole number after division:

    =INT(($B5-SUM($C$4:C$4*$C5:C5))/D$4)

When the denomination does not fit into the amount, the result from INT is zero. When the denomination does fit, INT returns a count as a whole number. As the formula is copied to the right, the expanding references expand to account for the value of previously counted denominations, and the same calculation is repeated in each column. When the formulas are copied down, the correct denominations are calculated for each amount in column B.

> Note: I would normally use the SUMPRODUCT function in the formula above to avoid array formula syntax, which requires special handling in Excel 2019 and older. However, SUMPRODUCT will return #VALUE for the first calculation (empty column B) for reasons I don't fully understand. Using SUM avoids this problem but means you must enter with control + shift + enter in older versions of Excel. No special handling is needed in Excel 2021 or later.

### Reverse Calculation: Checking the result

The "reverse" calculation determines the value of a specific set of denominations and counts. In this worksheet, we use a formula like this in column K to check the results of our other formulas. The formula in K5, copied down, looks like this:

    =SUMPRODUCT($D$4:$I$4,D5:I5)

In each row, [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 multiplies the counts calculated in D5:I16 by the denominations in row 4 and returns a sum that should always equal the original amount in column B.

### Method 2: Dynamic array formula option

This seems like exactly the kind of problem that could be solved neatly with a modern dynamic array formula and, in particular, a formula that uses the [SCAN function](https://exceljet.net/functions/scan-function)
. I had a crack at this and came up with the following formula:

    =LET(
    amount,B5,
    denoms,$D$4:$I$4,
    remainders,SCAN(amount,denoms,LAMBDA(a,v,MOD(a,v))),
    available_amounts,DROP(HSTACK(amount,remainders),,-1),
    INT(available_amounts/denoms)
    )

We use the LET function to assign variable names and improve readability. At a high level, the formula works like this:

*   To calculate counts correctly, we need to divide the amount by each denomination in sequence. Before we divide, we need to subtract the value of the denominations already counted.
*   We use the SCAN function with the MOD function to calculate remainders. While SCAN gives us the correct remainders going forward, they are not aligned correctly with denominations.
*   We construct an array of "available amounts". This is the remaining amount available for each denomination as we move across the table. Because there is no "previous remainder" for the first column, we do some fancy footwork with DROP and HSTACK to insert the original amount first, then drop the last remainder, which we don't need. Essentially, we are aligning the correct amounts with each denomination.
*   Finally, in the last step, we use INT to calculate a whole number after dividing the available amounts by each denomination. You can see the result below:

![A dynamic array formula to calculate all denominations at once](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/cash_denomination_calculator_dynamic_array_version.png "A dynamic array formula to calculate all denominations at once")

Even though this formula is longer than the original option, it has several nice advantages:

*   Each row requires one formula only instead of six.
*   We don't have to work with a tangle of mixed and expanding references.
*   The variable names make it easier to understand the flow of the formula.
*   We don't need to use an empty column in the calculation.

As always, there are many ways to solve a problem with [Excel's latest dynamic array functions](https://exceljet.net/new-excel-functions)
, and I'm certain there is a better way to do this. Let me know if you have a more elegant solution!

### Extending the formulas to handle coins

Both solutions above can easily be extended to handle coins (i.e., quarters, dimes, nickels, and pennies). The main task is to insert the needed columns, add the denominations in row 4, and then adjust the formula ranges. However, there is one additional task, which is to add the ROUND function to prevent possible floating point errors. The traditional formula then becomes:

    =INT(ROUND(($B5-SUM($C$4:C$4*$C5:C5)),10)/D$4)

The dynamic array formula becomes:

    =LET(
    amount,B5,
    denoms,$D$4:$M$4,
    remainders,SCAN(amount,denoms,LAMBDA(a,v,ROUND(MOD(a,v),10))),
    available_amounts,DROP(HSTACK(amount,remainders),,-1),
    INT(available_amounts/denoms)
    )

The screen below shows the traditional approach extended to handle quarters, dimes, nickels, and pennies.

![Traditional formula extended to handle coins](https://exceljet.net/sites/default/files/images/formulas/inline/cash_denomination_calculator_with_coins.png "Traditional formula extended to handle coins")

See below for details about why rounding is important when working with fractional values like (some) coins.

### About floating point errors and rounding

When you deal with fractional values like coins, you can run into floating point problems. For example, with a starting amount of 15.37, things work fine until we get to pennies ($0.01). At that point, we've accounted for 15.35, so the formula should return 2 for pennies. However, the formula instead returns 1 instead of 2.

This happens because `15.37 - 15.35` evaluates to `0.0199999999999996` instead of `0.02` due to how Excel handles floating-point arithmetic. Computers store numbers in a binary format. In this system, only fractions that can be expressed as sums of powers of 2 (like 1/2, 1/4, 1/8, etc.) can be represented exactly. Decimal fractions like 15.35 and 15.37 cannot be represented exactly in binary. Instead, they are approximated by the closest representable binary numbers. Most of the time, you won't notice this because Excel will display a number like `0.0199999999999996` as `0.02` by default. However, when you are dividing a number that contains a fractional value, you can run into this problem.

The solution above uses the ROUND function to round off the intermediate results, eliminating most floating-point problems. Rounding to 10 decimal places limits the number of decimal places to a manageable precision, but it doesn't compromise the underlying precision of typical financial or currency-related calculations.

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel INT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20int%20function.png "Excel INT function")](https://exceljet.net/functions/int-function)

### [INT Function](https://exceljet.net/functions/int-function)

The Excel INT function returns the integer part of a decimal number by rounding down to the integer. Note that negative numbers become _more negative_. For example, while INT(10.8) returns 10, INT(-10.8) returns -11.

[![Excel LET function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_let.png "Excel LET function")](https://exceljet.net/functions/let-function)

### [LET Function](https://exceljet.net/functions/let-function)

The Excel LET function lets you define named variables in a formula. There are two primary reasons you might want to do this: (1) to improve performance by eliminating redundant calculations and (2) to make more complex formulas easier to read and write....

[![Excel SCAN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20scan%20function.png "Excel SCAN function")](https://exceljet.net/functions/scan-function)

### [SCAN Function](https://exceljet.net/functions/scan-function)

The SCAN function applies a custom calculation to each element in a given array or range and returns an [array](https://exceljet.net/glossary/array)
 that contains the intermediate values created during the scan. SCAN can be used to generate running totals, running counts, and other...

[![Excel MOD function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20mod%20function.png "Excel MOD function")](https://exceljet.net/functions/mod-function)

### [MOD Function](https://exceljet.net/functions/mod-function)

The Excel MOD function returns the remainder of two numbers after division.  For example, MOD(10,3) = 1. The result of MOD carries the same sign as the divisor.

[![Excel DROP function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20drop%20function.png "Excel DROP function")](https://exceljet.net/functions/drop-function)

### [DROP Function](https://exceljet.net/functions/drop-function)

The Excel DROP function returns a subset of a given array by "dropping" rows and columns. The number of rows and columns to remove is provided by separate _rows_ and _columns_ arguments. Rows and columns can be dropped from the start or end of the given array....

[![Excel HSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20hstack%20function.png "Excel HSTACK function")](https://exceljet.net/functions/hstack-function)

### [HSTACK Function](https://exceljet.net/functions/hstack-function)

The Excel HSTACK function combines arrays horizontally into a single array. Each subsequent array is appended to the right of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [INT Function](https://exceljet.net/functions/int-function)
    
*   [LET Function](https://exceljet.net/functions/let-function)
    
*   [SCAN Function](https://exceljet.net/functions/scan-function)
    
*   [MOD Function](https://exceljet.net/functions/mod-function)
    
*   [DROP Function](https://exceljet.net/functions/drop-function)
    
*   [HSTACK Function](https://exceljet.net/functions/hstack-function)
    

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