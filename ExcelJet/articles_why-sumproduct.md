# Why SUMPRODUCT? | Exceljet

**Source:** https://exceljet.net/articles/why-sumproduct

---

[Skip to main content](https://exceljet.net/articles/why-sumproduct#main-content)

[](https://exceljet.net/articles/why-sumproduct#)

*   [Previous](https://exceljet.net/articles/xlookup-vs-vlookup)
    
*   [Next](https://exceljet.net/articles/how-to-concatenate-in-excel)
    

Why SUMPRODUCT?
===============

by Dave Bruns · Updated 7 Jan 2023

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/7338/download?token=NZ21_xon)
 (17.67 KB)

![Why does SUMPRODUCT show up in so many formulas?](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/why_sumproduct.jpeg "Why does SUMPRODUCT show up in so many formulas?")

Summary
-------

In this article, I attempt to explain why you see SUMPRODUCT so often in formulas, and when you can use the SUM function instead. The short version: SUMPRODUCT supports [array operations](https://exceljet.net/glossary/array-operation)
 natively, which makes it very useful for solving seemingly unrelated Excel problems. In the current version of Excel, you can use the SUM function instead, but SUMPRODUCT is better for backwards compatibility.

If you spend much time working with Excel formulas, you'll start to run into the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 a lot. SUMPRODUCT seems to be the catch-all, do-all, go-to solution for many seemingly unrelated Excel problems. Why is SUMPRODUCT in so many Excel formulas? 

The main reason SUMPRODUCT appears so often in Excel formulas is that it supports [array operations](https://exceljet.net/glossary/array-operation)
 natively, and array operations combined with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 are a very good way to solve many problems in Excel. In the past (Excel 2019 and older) Excel's formula engine did not handle most array operations without special handling. As a result, SUMPRODUCT has always been a simple way to create an array formula that "just works". In the current version of Excel, [these limitations are gone](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, so it is possible to use the [SUM function](https://exceljet.net/functions/sum-function)
 instead.

Note: as mentioned above, the technique of using SUMPRODUCT to solve general problems in Excel often involves some kind of [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. If this concept is new to you, [this video provides a basic overview](https://exceljet.net/videos/boolean-operations-in-array-formulas)
. The video was created in [Excel 365](https://exceljet.net/glossary/excel-365)
, so I am using the SUM function, but SUMPRODUCT would work just as well.

### The SUMPRODUCT function

The purpose of SUMPRODUCT is to calculate the sum of products. The worksheet below shows a classic example: SUMPRODUCT is used to calculate the sum of Price \* Qty:

![Basic SUMPRODUCT example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/Basic%20SUMPRODUCT%20example.png?itok=ex6c3BDq "Basic SUMPRODUCT example")

In this worksheet, there is no [helper column](https://exceljet.net/glossary/helper-column)
 that calculates the "Extended price" for each item. Instead, SUMPRODUCT calculates the intermediate values by multiplying the two ranges together and returns a sum in one step. Notice we are providing C5:C9 as _array1_ and D5:D9 as _array2_. So far, so good. SUMPRODUCT performs a useful calculation, but there seems to be nothing special about it.

### SUMPRODUCT and array operations

In the formula above, we are using two separate [arguments](https://exceljet.net/glossary/function-argument)
, _array1_ and _array2_:

    =SUMPRODUCT(C5:C9,D5:D9)
    

Things get more interesting if we alter the structure of this formula and _combine_ the two arguments into _one_ argument like this:

    =SUMPRODUCT(C5:C9*D5:D9)
    

![SUMPRODUCT with array operation](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUMPRODUCT%20with%20array%20operation.png?itok=Ujbkmd0k "SUMPRODUCT with array operation.png ")

In this formula, we multiply the two ranges together inside _array1,_ using what is called an "[array operation](https://exceljet.net/glossary/array-operation)
". The formula evaluates like this:

    =SUMPRODUCT(C5:C9*D5:D9)
    =SUMPRODUCT({10.5;8;11.75;7.74;9}*{5;6;10;4;8})
    =SUMPRODUCT({52.5;48;117.5;30.96;72})
    

After multiplication, there is just one array given to SUMPRODUCT as _array1_. The final result is exactly the same as the original formula.

You will see this pattern frequently in SUMPRODUCT — various math operations combined in _array1 —_ because it provides more control over the logic used to manage data. When separate arguments are used, SUMPRODUCT _multiplies_ arguments, which [works like AND logic in Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. Using one argument means you can use addition (+) for OR logic, or other math operations as needed. As a bonus, any math operation [will automatically convert TRUE and FALSE values to 1s and 0s](https://exceljet.net/videos/how-to-convert-booleans-to-numbers)
, which are frequently needed to tally up results. Finally, this flexibility means SUMPRODUCT can solve all kinds of [tricky problems](https://exceljet.net/formulas/count-if-row-meets-multiple-criteria)
 _without_ Control + Shift + Enter, which is why it's the go-to function in so many formulas.

A further reason SUMPRODUCT is used so often is that it can handle conditional counts and sums in ways that [COUNTIFS](https://exceljet.net/functions/countifs-function)
 and [SUMIFS](https://exceljet.net/functions/sumifs-function)
 simply can't. This is because [these functions require ranges](https://exceljet.net/articles/excels-racon-functions)
 and can't use arrays directly. Examples: [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)
, [Sum by year](https://exceljet.net/formulas/sum-by-year)
.

### The SUM function

In the formula above, notice that we have just a single array after multiplication. When SUMPRODUCT is given one array, it simply returns a sum. In that case, you might wonder if we can replace the SUMPRODUCT function with the [SUM function](https://exceljet.net/functions/sum-function)
 like this:

    =SUM(C5:C9*D5:D9)
    

The answer is: it depends. In modern versions of Excel that include the new [dynamic array engine](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, you can indeed use SUM instead of SUMPRODUCT. However, in older versions of Excel, the SUM version of the formula must be entered as an [array formula](https://exceljet.net/glossary/array-formula)
 with Control + Shift + Enter. If not, the formula returns an incorrect result:

![SUM function with array operation - Excel 2010 incorrect result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUM%20function%20with%20array%20operation%20Excel%202010%20incorrect.png?itok=BuYI8sTZ "SUM function with array operation - Excel 2010 incorrect result")

In older versions of Excel (2010, 2016, 2019), the SUM version of the formula returns an incorrect result when the formula is entered normally. In Excel 365, the formula works just fine:

![SUM function with array operation Excel 365](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUM%20function%20with%20array%20operation%20Excel%20365.png?itok=oLohZ3Om "SUM function with array operation Excel 365")

Why does the formula work in SUMPRODUCT but not SUM? Recall that multiplying the two ranges together is an "[array operation](https://exceljet.net/glossary/array-operation)
". It turns out that SUMPRODUCT is in a [small group of functions](https://exceljet.net/glossary/array-operation)
 that can handle most array operations natively. The SUM function is _not_ in this group and must be entered with Control + Shift + Enter when arguments include array operations.

_Note: in the example above, we are using just one [argument](https://exceljet.net/glossary/function-argument)
. When only one argument is provided, both SUM and SUMPRODUCT return a sum. With more than one argument, SUM and SUMPRODUCT have different behaviors. SUM returns a sum, while SUMPRODUCT returns the sum of products._

### The past

The main reason SUMPRODUCT appears so often in Excel formulas is that it supports [array operations](https://exceljet.net/glossary/array-operation)
 natively, and array operations combined with [Boolean logic](https://exceljet.net/glossary/boolean-logic)
 turn out to be a very good way to solve many problems in Excel. In the past (Excel 2019 and older) Excel's formula engine did not handle most array operations without special handling. As a result, SUMPRODUCT has always been a simple way to create an array formula that "just works".

In the past, you _could_ use the SUM function instead of SUMPRODUCT in formulas that use array operations, but SUM required Control + Shift + Enter. This means if someone forgets to use [CSE](https://exceljet.net/glossary/cse)
 when checking or adjusting a formula, the result might change, even if the formula did not change. SUMPRODUCT avoids this problem. It also avoids the need to explain Control + Shift + Enter, which is a complicated topic.

### The present

Since dynamic array formulas were [introduced in Excel 365](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the need for SUMPRODUCT has started to diminish, because array formulas are natively supported. This means you can replace the SUMPRODUCT function with the SUM function in formulas that use an array operation and get the same behavior. To illustrate with another example, the worksheet below uses the [LEN function](https://exceljet.net/functions/len-function)
 to count the total number of characters in the range B5:B9.

    =SUMPRODUCT(LEN(B5:B9))
    

Because the range contains five cells, the LEN function returns an [array](https://exceljet.net/glossary/array)
 with five counts:

    LEN(B5:B9) // returns {5;5;4;6;4}
    

This is another kind of array operation called [lifting](https://exceljet.net/glossary/lifting)
. The array from LEN is returned to SUMPRODUCT as _array1_:

    =SUMPRODUCT({5;5;4;6;4}) // returns 24
    

And SUMPRODUCT returns 24 as a final result. This formula needs no special handling; it will work in any version of Excel.

![SUMPRODUCT with the LEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUMPRODUCT%20with%20the%20LEN%20function.png?itok=D-wK_5DF "SUMPRODUCT with the LEN function")

In "modern" versions of Excel, the SUM version of the formula works exactly the same way:

    =SUM(LEN(B5:B9))
    

![SUM function with the LEN function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUM%20function%20with%20the%20LEN%20function.png?itok=vNQ2wCMs "SUM function with the LEN function")

However, in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
 the SUM version fails. The screen below shows the same formula in Excel 2010:

    =SUM(LEN(B5:B9))
    

![SUM function in Excel 2010 incorrect result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUM%20function%20in%20Excel%202010%20incorrect%20result.png?itok=b3XsaNPx "SUM function in Excel 2010 incorrect result")

Note that curly braces are _not_ visible in the formula bar. This confirms the formula was _not_ entered with [CSE](https://exceljet.net/glossary/cse)
. Below is the same formula, this time entered with Control + Shift + Enter:

    {=SUM(LEN(B5:B9))}
    

![SUM function in Excel 2010 correct result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/SUM%20function%20in%20Excel%202010%20correct%20result.png?itok=cGZ8nCAy "SUM function in Excel 2010 correct result")

Now the formula returns a correct result. The curly braces in the formula bar confirm the formula was entered with Control + Shift + Enter.

_Note: the curly braces are added by Excel automatically when a formula is entered as an array formula with Control + Shift + Enter. Do not add curly braces manually or the formula will not work._

### Automatic array formula conversion

To prevent formulas from breaking in older versions of Excel, Excel will automatically convert array formulas to use the array syntax\*. This means you will see curly braces in the formula bar even when a formula was never entered with Control + Shift + Enter. For example, the SUM formula above will appear like this if opened in Excel 2016:

    {=SUM(LEN(B5:B9))}
    

Note this is automatic behavior to prevent the formula from returning a different result in older versions of Excel. If the formula is re-entered _without_ Control + Shift + Enter in an older version of Excel, the formula _will_ return an incorrect result.

_\* Excel is quite conservative in how it evaluates array formulas and you will sometimes see curly braces added to formulas that work just fine without them. For example, you will see the curly braces added to a SUMPRODUCT formula that uses array operations, even when they are not needed. The only way to be sure if the array syntax is needed is to re-enter the formula normally and check the result._

### Summary

SUMPRODUCT is in a small group of functions that can handle array operations natively, without Control + Shift + Enter. By placing various operations into a single argument, you can extract data with other functions, and use [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
 to create AND and OR logic in many different ways. This has made SUMPRODUCT the go-to solution for tricky problems over the years.

In [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021 the formula engine [handles arrays natively](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
. This means you can often use the SUM function in place of SUMPRODUCT with the same result and no need to enter the formula in a special way. However, if the same formula is opened in an earlier version of Excel, it will require Control + Shift + Enter.

If you need compatibility with older versions of Excel, SUMPRODUCT is a safer and more robust option, since it "just works" in almost all cases. If you will only be using a worksheet in modern versions of Excel (with the [new dynamic array engine](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
), the SUM function can be used instead of SUMPRODUCT and will work just fine. If you are not sure what version of Excel a worksheet will be used with, SUMPRODUCT is probably the better option, since it avoids complexity.

### More Examples

The formulas below use SUMPRODUCT for compatibility with older versions of Excel, but you can use the SUM function instead in modern Excel.

*   [Count if row meets internal criteria](https://exceljet.net/formulas/count-if-row-meets-internal-criteria)
    
*   [Count birthdays by year](https://exceljet.net/formulas/count-birthdays-by-year)
    
*   [Count cells equal to case sensitive](https://exceljet.net/formulas/count-cells-equal-to-case-sensitive)
    
*   [Count cells that begin with](https://exceljet.net/formulas/count-cells-that-begin-with)
    

### Workbook note

The attached workbook below contains the examples used in the article above. Keep in mind that if you open this workbook in older versions of Excel, you will see that the formulas with array operations have already been converted to array formulas. Look for the curly braces in the formula bar, and notice they disappear if you edit the formula. To see the formula fail without this special handling, re-enter the formula normally (i.e. don't use Control + Shift + Enter).

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