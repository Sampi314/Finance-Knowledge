# Why some Excel functions won't spill | Exceljet

**Source:** https://exceljet.net/articles/why-some-excel-functions-wont-spill

---

[Skip to main content](https://exceljet.net/articles/why-some-excel-functions-wont-spill#main-content)

[](https://exceljet.net/articles/why-some-excel-functions-wont-spill#)

*   [Previous](https://exceljet.net/articles/native-checkboxes-in-excel)
    
*   [Next](https://exceljet.net/articles/floating-point-errors-in-excel)
    

Why some Excel functions won't spill
====================================

by Dave Bruns · Updated 4 Jul 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/9259/download?token=cBOWIacL)
 (26.04 KB)

![Some older Excel functions don't spill as expected. Why?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/functions_that_wont_spill_artwork.jpg "Some older Excel functions don't spill as expected. Why?")

Summary
-------

Ever wonder why some Excel functions stubbornly refuse to [spill](https://exceljet.net/glossary/spill)
 results into multiple cells, even when you give them a range of data? For example, if you give some functions like [EOMONTH](https://exceljet.net/functions/eomonth-function)
 or [EDATE](https://exceljet.net/functions/edate-function)
 a range of dates, you'll get back a #VALUE! error. This quirky behavior affects dozens of Excel functions, mostly legacy functions from the old Analysis ToolPak, that were developed decades before dynamic array formulas were introduced. The good news? There's an incredibly simple fix that most Excel users don't know about: just add a plus sign (+) before your range reference. That's it!  Read below for a full explanation, examples of how to fix the problem, and a list of functions that are affected.

Some older Excel functions don't spill when you give them a range as input. This article explains why this happens, which functions are affected, and how to fix it. 

### Table of Contents

*   [Dynamic Arrays and Spilling](https://exceljet.net/articles/why-some-excel-functions-wont-spill#dynamic-arrays-and-spilling)
    
*   [The spilling problem explained](https://exceljet.net/articles/why-some-excel-functions-wont-spill#the-spilling-problem-explained)
    
*   [The simple solution](https://exceljet.net/articles/why-some-excel-functions-wont-spill#the-simple-solution)
    
*   [List of affected functions](https://exceljet.net/articles/why-some-excel-functions-wont-spill#list-of-affected-functions)
    
*   [Why the plus sign?](https://exceljet.net/articles/why-some-excel-functions-wont-spill#why-the-plus-sign)
    

> There are other reasons why a formula might not spill. This article focuses on one specific case: a specific group of older functions that will not accept a range in place of a single value. 

### Dynamic Arrays and Spilling

In 2019, the Excel team began to introduce [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, a new way to work with data in Excel. In a nutshell, dynamic array formulas can process more than one value at the same time, then return multiple values to the worksheet in a behavior known as "[spilling](https://exceljet.net/glossary/spill)
". Many newer dynamic array functions spill multiple values natively. Good examples are functions like [FILTER](https://exceljet.net/functions/filter-function)
, [SORT](https://exceljet.net/functions/sort-function)
, [SEQUENCE](https://exceljet.net/functions/sequence-function)
, and [UNIQUE](https://exceljet.net/functions/unique-function)
. However, older Excel functions will also spill through a process called "[lifting](https://exceljet.net/glossary/lifting)
". When you give a range or [array](https://exceljet.net/glossary/array)
 to a function not programmed to accept arrays natively, Excel will "lift" the function and call it multiple times, once for each value in the array. For example, the [LEN function](https://exceljet.net/functions/len-function)
 is designed to return the number of characters in a text string. If we give LEN the text "apple", it will return 5:

    =LEN("apple") // returns 5
    

If we give LEN three text strings in an [array](https://exceljet.net/glossary/array)
, it returns an array with three counts, one for each text string:

    =LEN({"apple";"banana";"pear"}) // returns {5;6;4}
    

You can see an example of this in the following worksheet, where the formula in cell D8 looks like this:

    =LEN(B8:B10) // returns {5;6;4}
    

![A basic example of lifting and spilling with the LEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/basic-lifting-and-spilling-example.png "A basic example of lifting and spilling with the LEN function")

The main thing to understand is that lifting is a built-in behavior that happens automatically. When you give a function more than one value as an input, you will get back multiple results that spill onto the worksheet. It just works. Except when it doesn't 🙃

### The spilling problem explained

As it turns out, some functions don't spill when you give them a range instead of a single cell reference. A good example is the [EOMONTH function](https://exceljet.net/functions/eomonth-function)
, which returns the last day of the month for any given date. If we give EOMONTH the date 23-Apr-2025, with an offset of 0, it will return the last day of that month, which is 30-Apr-2025. You can see this in the following worksheet, where the formula in cell D5 looks like this:

    =EOMONTH(B5,0) // returns 30-Apr-2025
    

However, if we give EOMONTH a range of three dates, it refuses to spill and instead returns a #VALUE! error with a formula like this in cell D8:

    =EOMONTH(B8:B10,0) // returns #VALUE!
    

![An example of the spilling problem with the EOMONTH function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/eomonth-spill-problem-example.png "An example of the spilling problem with the EOMONTH function")

We can see exactly the same problem with the [EDATE function](https://exceljet.net/functions/edate-function)
, which returns the date a given number of months before or after a given date. If we give EDATE the date 23-Apr-2025, with an offset of 1, it will return the date 23-May-2025. You can see this in the following worksheet, where the formula in cell D5 looks like this:

    =EDATE(B5,1) // returns 23-May-2025
    

However, if we give EDATE a range of three dates, it refuses to spill and instead returns a #VALUE! error with a formula like this in cell D8:

    =EDATE(B8:B10,1) // #VALUE! error

![An example of the spilling problem with the EDATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/edate-spill-problem-example.png "An example of the spilling problem with the EDATE function")

What's going on here? The problem is that some older functions like EOMONTH "resist" spilling when provided a range. This limitation comes from these functions expecting a single cell value instead of a range. The #VALUE! error is essentially reporting the range as an unexpected value. Other common functions that have this same limitation include EDATE, [ISEVEN](https://exceljet.net/functions/iseven-function)
, [ISODD](https://exceljet.net/functions/isodd-function)
, [YEARFRAC](https://exceljet.net/functions/yearfrac-function)
, [WORKDAY](https://exceljet.net/functions/workday-function)
, and [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
. See [below](https://exceljet.net/articles/why-some-excel-functions-wont-spill#list-of-affected-functions)
 for a larger list of affected functions.

### The simple solution

Although this seems like a difficult technical problem, the solution is actually quite simple. The trick is to add a plus sign (+) before the range. This forces Excel to evaluate the range before the function runs. The result is an [array](https://exceljet.net/glossary/array)
 of values, which are then passed to the function so that [lifting](https://exceljet.net/glossary/lifting)
 and spilling occur as expected. You can see this fix in the following worksheet, where the formula in cell D8 looks like this:

    =EOMONTH(+B8:B10,0) // spills normally
    

![The EOMONTH formula spill problem fixed with a + sign before the range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/eomonth-spill-problem-fix.png "The EOMONTH formula spill problem fixed with a + sign before the range")

We can do exactly the same thing with the EDATE function, and it will spill normally:

    =EDATE(+B8:B10,1) // spills normally
    

![The EDATE formula spill problem fixed with a + sign before the range](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/edate-spill-problem-fix.png "The EDATE formula spill problem fixed with a + sign before the range")

> Note: In simple situations like those described above, diagnosing the spill problem and fixing it is fairly straightforward as long as you know about this issue and how to fix it. Where it gets more complicated is when you use a function that resists spilling with a range inside a larger formula. Then, function will return a #VALUE! error that blows up the entire formula, but it will not be so easy to understand what the problem is, since you aren't actually seeing a function fail to spill on a worksheet. 

### List of affected functions

The origins of this problem are murky, and it is difficult to find good documentation for Excel functions from the era in which most of these functions were introduced. However, based on conversations with other Excel MVPs, I believe that functions with this spilling limitation all originate from the same development effort: the Analysis ToolPak, which was initially included in Excel 97 as a separate add-in, and later rolled into the core application in Excel 2007. Here is a list of the functions that started life in the Analysis ToolPak:

| Category | Functions |
| --- | --- |
| **Financial** | [ACCRINT](https://exceljet.net/functions/accrint-function)<br>, [ACCRINTM](https://exceljet.net/functions/accrintm-function)<br>, [AMORDEGRC](https://exceljet.net/functions/amordegrc-function)<br>, [AMORLINC](https://exceljet.net/functions/amorlinc-function)<br>, [COUPDAYBS](https://exceljet.net/functions/coupdaybs-function)<br>, [COUPDAYS](https://exceljet.net/functions/coupdays-function)<br>, [COUPDAYSNC](https://exceljet.net/functions/coupdaysnc-function)<br>, [COUPNCD](https://exceljet.net/functions/coupncd-function)<br>, [COUPNUM](https://exceljet.net/functions/coupnum-function)<br>, [COUPPCD](https://exceljet.net/functions/couppcd-function)<br>, [CUMIPMT](https://exceljet.net/functions/cumipmt-function)<br>**\***, [CUMPRINC](https://exceljet.net/functions/cumprinc-function)<br>, [DISC](https://exceljet.net/functions/disc-function)<br>, [DOLLARDE](https://exceljet.net/functions/dollarde-function)<br>, [DOLLARFR](https://exceljet.net/functions/dollarfr-function)<br>, [DURATION](https://exceljet.net/functions/duration-function)<br>, [EFFECT](https://exceljet.net/functions/effect-function)<br>, [FVSCHEDULE](https://exceljet.net/functions/fvschedule-function)<br>, [INTRATE](https://exceljet.net/functions/intrate-function)<br>, [MDURATION](https://exceljet.net/functions/mduration-function)<br>, [NOMINAL](https://exceljet.net/functions/nominal-function)<br>, [ODDFPRICE](https://exceljet.net/functions/oddfprice-function)<br>, [ODDFYIELD](https://exceljet.net/functions/oddfyield-function)<br>, [ODDLPRICE](https://exceljet.net/functions/oddlprice-function)<br>, [ODDLYIELD](https://exceljet.net/functions/oddlyield-function)<br>, [PMT](https://exceljet.net/functions/pmt-function)<br>**\***, [PRICE](https://exceljet.net/functions/price-function)<br>, [PRICEDISC](https://exceljet.net/functions/pricedisc-function)<br>, [PRICEMAT](https://exceljet.net/functions/pricemat-function)<br>, [RECEIVED](https://exceljet.net/functions/received-function)<br>, [TBILLEQ](https://exceljet.net/functions/tbilleq-function)<br>, [TBILLPRICE](https://exceljet.net/functions/tbillprice-function)<br>, [TBILLYIELD](https://exceljet.net/functions/tbillyield-function)<br>, [XIRR](https://exceljet.net/functions/xirr-function)<br>**\***, [XNPV](https://exceljet.net/functions/xnpv-function)<br>, [YIELD](https://exceljet.net/functions/yield-function)<br>, [YIELDDISC](https://exceljet.net/functions/yielddisc-function)<br>, [YIELDMAT](https://exceljet.net/functions/yieldmat-function) |
| **Engineering** | BESSELI, BESSELJ, BESSELK, BESSELY, [BIN2DEC](https://exceljet.net/functions/bin2dec-function)<br>, [BIN2HEX](https://exceljet.net/functions/bin2hex-function)<br>, [BIN2OCT](https://exceljet.net/functions/bin2oct-function)<br>, [COMPLEX](https://exceljet.net/functions/complex-function)<br>, [CONVERT](https://exceljet.net/functions/convert-function)<br>, [DEC2BIN](https://exceljet.net/functions/dec2bin-function)<br>, [DEC2HEX](https://exceljet.net/functions/dec2hex-function)<br>, [DEC2OCT](https://exceljet.net/functions/dec2oct-function)<br>, [DELTA](https://exceljet.net/functions/delta-function)<br>, ERF, ERFC, GESTEP, [HEX2BIN](https://exceljet.net/functions/hex2bin-function)<br>, [HEX2DEC](https://exceljet.net/functions/hex2dec-function)<br>, [HEX2OCT](https://exceljet.net/functions/hex2oct-function)<br>, [IMABS](https://exceljet.net/functions/imabs-function)<br>, [IMAGINARY](https://exceljet.net/functions/imaginary-function)<br>, [IMARGUMENT](https://exceljet.net/functions/imargument-function)<br>, [IMCONJUGATE](https://exceljet.net/functions/imconjugate-function)<br>, [IMCOS](https://exceljet.net/functions/imcos-function)<br>, [IMDIV](https://exceljet.net/functions/imdiv-function)<br>, [IMEXP](https://exceljet.net/functions/imexp-function)<br>, [IMLN](https://exceljet.net/functions/imln-function)<br>, [IMLOG10](https://exceljet.net/functions/imlog10-function)<br>, [IMLOG2](https://exceljet.net/functions/imlog2-function)<br>, [IMPOWER](https://exceljet.net/functions/impower-function)<br>, [IMPRODUCT](https://exceljet.net/functions/improduct-function)<br>**\***, [IMREAL](https://exceljet.net/functions/imreal-function)<br>, [IMSIN](https://exceljet.net/functions/imsin-function)<br>, [IMSQRT](https://exceljet.net/functions/imsqrt-function)<br>, [IMSUB](https://exceljet.net/functions/imsub-function)<br>, [IMSUM](https://exceljet.net/functions/imsum-function)<br>**\***, [OCT2BIN](https://exceljet.net/functions/oct2bin-function)<br>, [OCT2DEC](https://exceljet.net/functions/oct2dec-function)<br>, [OCT2HEX](https://exceljet.net/functions/oct2hex-function) |
| **Math & Trig** | [FACTDOUBLE](https://exceljet.net/functions/factdouble-function)<br>, [GCD](https://exceljet.net/functions/gcd-function)<br>**\***, [LCM](https://exceljet.net/functions/lcm-function)<br>**\***, [MROUND](https://exceljet.net/functions/mround-function)<br>, [MULTINOMIAL](https://exceljet.net/functions/multinomial-function)<br>**\***, [QUOTIENT](https://exceljet.net/functions/quotient-function)<br>, [RANDBETWEEN](https://exceljet.net/functions/randbetween-function)<br>, SERIESSUM, [SQRTPI](https://exceljet.net/functions/sqrtpi-function) |
| **Date & Time** | [EDATE](https://exceljet.net/functions/edate-function)<br>, [EOMONTH](https://exceljet.net/functions/eomonth-function)<br>, [NETWORKDAYS](https://exceljet.net/functions/networkdays-function)<br>, [WEEKNUM](https://exceljet.net/functions/weeknum-function)<br>, [WORKDAY](https://exceljet.net/functions/workday-function)<br>, [YEARFRAC](https://exceljet.net/functions/yearfrac-function) |
| **Information** | [ISEVEN](https://exceljet.net/functions/iseven-function)<br>, [ISODD](https://exceljet.net/functions/isodd-function) |
| **Text** | ASC |

_Credit: I put together this list using_ [_this page on bettersolutions.com_](https://bettersolutions.com/excel/functions/updates-2003-functions.htm)
_._

I quickly tested all of the functions in the list above. Most of them have the spill problem, but there are a few exceptions, which I've marked with an asterisk (\*) above. Note also that there are a number of functions _derived_ from the ATP functions above that have the spill problem, including [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
, [NETWORKDAYS.INTL](https://exceljet.net/functions/networkdays.intl-function)
, ERF.PRECISE, and ERFC.PRECISE.

> When testing these functions, the basic approach is to provide a range in place of any argument that would normally be provided as a single cell reference. For the above functions, the result is usually a #VALUE! error, with exceptions as noted. When you add the plus (+) sign before the range, the formula should lift and spill, and you should get more than one result, depending on the size of the range provided. 

### Why the plus sign?

Way back in the 1980s, Lotus 1-2-3 was the dominate spreadsheet application, and it allowed you to start a formula with a plus sign (+) instead of an equal sign (=). When Excel added Lotus compatibility in the 1990s, it accepted that syntax, so users migrating to Excel often typed `+A1` or `+SUM(B2:B10)`, which Excel quietly converted to `=+A1` and `=+SUM(B2:B10)`. In Excel, the extra "+" is ignored; it's just an identity operator. In Excel, the + operator has no effect on a single value, but it _will_ coerce a range into an [array](https://exceljet.net/glossary/array)
, which sidesteps the legacy scalar (i.e., single value) restriction that creates the spilling problem described in this article.

> Researching this was interesting. It helped me understand why you occasionally see the + operator turn up in all kinds of simple formulas. I think the reason is that the people who wrote these formulas learned on Lotus 1-2-3. 🙂  I also think it is a matter of convenience for people who use a 10-key (the numeric keypad on a computer keyboard). I ran into many variations of this comment: When I'm typing on the 10 key, I don't have to move my hand to start a formula with = .. I just hit + with my pinky and start typing. Excel puts the = in on it's own. We don't actually type "=+".

### Summary

Excel's [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
 were introduced in Excel 365 starting in 2019.  A key feature of dynamic arrays is the ability to process multiple values and return multiple results through "[spilling](https://exceljet.net/glossary/spill)
." While newer functions like [FILTER](https://exceljet.net/functions/filter-function)
 and [SORT](https://exceljet.net/functions/sort-function)
 spill natively, older functions use a process called "[lifting,](https://exceljet.net/glossary/lifting)
" where Excel automatically calls the function multiple times for each value in an [array](https://exceljet.net/glossary/array)
.

However, certain older functions - primarily those originating from Excel's Analysis ToolPak - resist spilling when given a range as input. Functions like [EOMONTH](https://exceljet.net/functions/eomonth-function)
, [EDATE](https://exceljet.net/functions/edate-function)
, [ISEVEN](https://exceljet.net/functions/iseven-function)
, [ISODD](https://exceljet.net/functions/isodd-function)
, [YEARFRAC](https://exceljet.net/functions/yearfrac-function)
, [WORKDAY](https://exceljet.net/functions/workday-function)
, and [WORKDAY.INTL](https://exceljet.net/functions/workday.intl-function)
 will return a #VALUE! error instead of spilling results because they expect single values rather than ranges.

The solution is simple: add a plus sign (+) before the range reference. For example, `=EOMONTH(+A1:A5,1)` works where `=EOMONTH(A1:A5,1)` fails. The + operator forces Excel to evaluate the range first, converting it to an array of values that can then be processed through normal [lifting](https://exceljet.net/glossary/lifting)
 and [spilling](https://exceljet.net/glossary/spill)
 behavior.

This limitation affects dozens of functions across financial, engineering, math, date/time, and information categories - essentially all functions that were originally part of the Analysis ToolPak add-in.

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