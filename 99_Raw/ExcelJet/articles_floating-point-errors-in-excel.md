# Floating Point Errors in Excel | Exceljet

**Source:** https://exceljet.net/articles/floating-point-errors-in-excel

---

[Skip to main content](https://exceljet.net/articles/floating-point-errors-in-excel#main-content)

[](https://exceljet.net/articles/floating-point-errors-in-excel#)

*   [Previous](https://exceljet.net/articles/why-some-excel-functions-wont-spill)
    
*   [Next](https://exceljet.net/articles/regular-expressions-in-excel)
    

Floating Point Errors in Excel
==============================

by Dave Bruns · Updated 28 Apr 2025

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Attachment](https://exceljet.net/file/9106/download?token=-itNqz72)
 (27.7 KB)

![Floating Point Errors in Excel: Why Your Numbers Don’t Add Up](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/floating_point_errors_in_excel.jpg "Floating Point Errors in Excel: Why Your Numbers Don’t Add Up")

Summary
-------

Have you ever had Excel tell you two numbers are different when they look the same? This can be quite unsettling. You keep checking and re-checking numbers that look identical, and yet Excel insists they are different. Is Excel broken? Do you need glasses? Don't worry, it's not your fault. You may have run into a floating-point error. There are reasons why this can happen, and simple ways to fix the problem. 

If you've ever had a formula like =A1=B1 return FALSE—even though the values in A1 and B1 seem exactly the same—you've run into one of Excel’s most puzzling quirks: the floating-point error. These tiny differences are usually invisible, but they can cause formula checks and even conditional formatting rules to fail in unexpected ways. This article explains why these errors happen, how to spot them, and how to fix them with simple techniques like rounding.

### Table of Contents

*   [Why Your Numbers Don’t Add Up](https://exceljet.net/articles/floating-point-errors-in-excel#why-numbers-dont-add-up)
    
*   [What Is a Floating Point Error?](https://exceljet.net/articles/floating-point-errors-in-excel#what-is-floating-point-error)
    
*   [Example 1 - Typical rounding problem](https://exceljet.net/articles/floating-point-errors-in-excel#example-1)
    
*   [Example 2 - Floating point errors with subtraction](https://exceljet.net/articles/floating-point-errors-in-excel#example-2)
    
*   [Example 3 - Floating point errors with incremental addition](https://exceljet.net/articles/floating-point-errors-in-excel#example-3)
    
*   [Set precision as displayed (not recommended)](https://exceljet.net/articles/floating-point-errors-in-excel#set-precision)
    
*   [Other rounding functions in Excel](https://exceljet.net/articles/floating-point-errors-in-excel#other-rounding-functions)
    
*   [Takeaways](https://exceljet.net/articles/floating-point-errors-in-excel#takeaways)
    
*   [Floating point details](https://exceljet.net/articles/floating-point-errors-in-excel#floating-point-details)
    
*   [Useful Links](https://exceljet.net/articles/floating-point-errors-in-excel#useful-links)
    

### Why Your Numbers Don’t Add Up

When working with numbers in Excel, especially when adding or subtracting many values during reconciliation, you may run into small discrepancies that seem illogical, like two totals that should match but don’t. There are two basic reasons why you might run into this situation:

1.  A simple rounding problem.
2.  A floating-point error.

The first problem is more common and is often related to Excel's number formatting or sometimes to the column width. The second problem is less common and more difficult to understand. It happens because Excel uses binary floating-point numbers, which can’t represent some decimal values exactly. As a result, tiny rounding errors accumulate during calculations, creating results that are _extremely_ close but not exactly equal. These differences are often invisible on the worksheet but can cause equality checks or balance comparisons to fail unexpectedly:

*   A conditional formatting rule shows a calculated number in red when it should be green.
*   A formula that checks a calculation unexpectedly returns FALSE.
*   A final balance does not equal the expected result, although it appears to be correct.

> This problem is not limited to Excel. Other environments and computer languages have the same limitation.

### What Is a Floating Point Error?

Excel uses the decimal number system to display results. This is the base-10 system we use every day, with ten digits (0 through 9) to represent all numbers. In decimal, each digit's position in a number represents a power of 10, with values increasing from right to left. Computers, however, (including Excel) store numbers using a system called floating-point arithmetic, based on binary (base 2). In binary, only two digits (0 and 1) are used, and each position represents a power of 2. This system is efficient for computation, but it has an important limitation: many decimal values can’t be represented exactly in binary.

For example, numbers like 0.1 and 0.2 can't be represented perfectly in binary, so Excel stores values like 0.10000000000000001 and 0.20000000000000001 instead. Likewise, 1/3 doesn’t have an exact decimal representation (it becomes 0.3333333…). As a result, when Excel stores these values, it must approximate them. These tiny approximations—called floating-point errors—can cause surprising results when performing calculations or comparisons

Let's look at some examples, starting with a problem that is _not_ a floating-point error.

### Example 1 - Typical rounding problem

Before we get into specific examples of floating-point errors, let's look at a typical rounding problem. This is not a floating-point error, but rather a misunderstanding created by the way that Excel displays numbers when [number formatting](https://exceljet.net/glossary/number-format)
 is applied. In the worksheet below, we have a list of products in column B and corresponding prices in column C. In column D, we have calculated a 10% discount with a formula like this:

    =C5*10%

![Example 1 - formula to calculate a 10% discount](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/typical_rounding_problem1.png "Example 1 - formula to calculate a 10% discount") 

In column F, we have manually entered the same discount. In column G, we have a formula that checks the calculated discount in column C against the hardcoded discount in column F. The formula in G5 is:

    =D5=F5

![Example 1 - formula to compare discount and expected result](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/typical_rounding_problem2.png "Example 1 - formula to compare discount and expected result")

In all rows, it returns FALSE. What's going on?

The problem is that the calculated values in column D are not rounded, but they _look rounded_ because a [Number format](https://exceljet.net/glossary/number-format)
 with 2 decimal places has been applied to them. Number formats in Excel change the way a number is displayed, but they do not change the underlying number. If we change that number format to show four decimal places, you can see the problem clearly:

 ![Example 1 - the formula returns FALSE because the values are different](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/typical_rounding_problem3.png "Example 1 - the formula returns FALSE because the values are different")

> Tip: Another way to see more decimal places, temporarily apply the [General number format](https://exceljet.net/shortcuts/apply-general-format)
>  with the shortcut Ctrl + Shift + ~. Depending on the number, Excel will display up to 9 decimal places if the column is wide enough. Then Ctrl + Z to undo.

The discounts in column D are not rounded, but the number format with 2 decimal places causes them to look rounded. On the other hand, the numbers typed into column F are actually rounded to two decimal places. This is why none of the numbers match. If you need to compare these numbers apples-to-apples in a case like this, a good option is to modify the check formula in G5 like this

    =ROUND(D5,2)=F5

This formula uses the [ROUND function](https://exceljet.net/functions/round-function)
 to round the value in D5 to two decimal places before comparing it to the value in F5. The advantage of this approach is that it leaves the original values in column D unchanged, but still lets you compare to the expected results. With this change, you can see that now the check formula in column E returns TRUE in all rows:

![Example 1 - adjusting the check formula to round before comparing](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/typical_rounding_problem4.png "Example 1 - adjusting the check formula to round before comparing")

Another option is to round the values in column D right from the start using a formula like this in D5:

    =ROUND(C5*10%,2)

This option will actually round the discounts in column D to two decimal places, and they will match the hardcoded values in column F. Both options are valid, but I would generally avoid rounding the discounts unless you have a reason to do so.

To summarize, this is a rounding problem, not a floating-point error. [Number formats in Excel](https://exceljet.net/articles/custom-number-formats)
 can make it appear as though numbers are the same even when they aren't.

> Tip: Avoid rounding too early in your calculations, unless it is required. Early rounding can introduce cumulative errors. Instead, calculate precisely first, then apply rounding only at the final step. This method preserves accuracy. 

### Example 2 - Floating point errors with subtraction

Now let's look at an example of actual floating-point errors. In the worksheet below, we are subtracting numbers in column C from the numbers in column B. The formula in D5 looks like this:

    =B5-C5

![Example 2 - a floating point error with subtraction](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/floating_point_error_with_subtraction1.png "Example 2 - a floating point error with subtraction")

The values in columns B and C are ordinary numbers with exactly two decimal places, like dollars and cents. Column D contains the calculated result, and column E contains the expected result (hard-coded). If you look at the numbers in columns B and C, you can probably guess what the result should be. The formula in column F compares the actual result to the expected result, like this:

    =D5=E5

As you can see, most of the checks in column G are FALSE, even though we would expect all results to be TRUE. This is quite confusing. The calculation is simple, and the results look perfectly ordinary. What's going on here? This is a case where some of the numbers in column D can't be perfectly stored as binary numbers. They look normal, but if we look more carefully, we can find some tiny problems. 

The first thing to check is the raw numbers. To show more decimal places, use the [keyboard shortcut](https://exceljet.net/shortcuts/format-almost-anything)
 Ctrl + 1 to open the Format cells dialog box, then navigate to Number and set the decimal places to 16:

![Using Format Cells to show 16 decimal places](https://exceljet.net/sites/default/files/images/articles/inline/using_format_cells_to_set_16_decimal_places.png "Using Format Cells to show 16 decimal places")

Then adjust the column width to show the full value. Now we can see that some of these numbers are not what they appear to be:

![Example 2 - showing more decimal places to understand the problem](https://exceljet.net/sites/default/files/images/articles/inline/floating_point_error_with_subtraction2.png "Example 2 - showing more decimal places to understand the problem")

> Tip: Another way to increase decimal places is to punch the "increase decimal" button on the ribbon 16 times, but I like the Ctrl + 1 method because it's fast and you can quickly [undo with Ctrl+Z](https://exceljet.net/shortcuts/undo-last-action)
>  after checking the raw number. Note also if you want to check a static number typed or pasted into Excel, the formula bar will show the number in its raw form without number formatting.

Now that we know the problem, how should we fix it? One way to fix a floating-point error in Excel is to add rounding to the appropriate formulas. For example, in this worksheet, we can modify the Check formula to round the value in column D5 before testing. Since we're working with numbers that are accurate to two decimal places, we can use the ROUND function with _num\_digits_ set to 2. You can see this approach in the worksheet below, where the formula in G5 is now:

    =ROUND(D5,2)=F5

![Example 2 - all checks pass after rounding](https://exceljet.net/sites/default/files/images/articles/inline/floating_point_error_with_subtraction3.png "Example 2 - all checks pass after rounding")

Another good way to manage floating-point errors is to use a formula that ensures that calculated and expected results are within a specified tolerance. We can use the [ABS function](https://exceljet.net/functions/abs-function)
 to create a tolerance-based check like this:

    =ABS(D5-F5)<0.0000000001

We first subtract the expected result from the calculated result. Then we take the absolute value, and check the difference is less than 0.0000000001. This method allows you to bypass rounding entirely, by defining a threshold for how close is "close enough." You can see this formula in action below:

![Example 2 - another way to check for differences with the ABS function](https://exceljet.net/sites/default/files/images/articles/inline/floating_point_error_with_subtraction4.png "Example 2 - another way to check for differences with the ABS function")

> Note: The tolerance above is very small. In general, you should adjust the tolerance to suit the specific use case.

### Example 3 - Floating point errors with incremental addition

Floating-point errors can also appear when you add the same decimal value repeatedly. In the worksheet below, we are repeatedly adding 0.1 to a starting value of -1.9. All values in column B are generated with the SEQUENCE function with this formula in cell B5: 

    =SEQUENCE(F6,,F4,F5)

We would expect to reach 1 in row 14 after adding 0.1 nine times. However, for some reason, the value in cell B14 is not exactly 1. The values in column C are expected results. The yellow highlighting indicates rows where the calculated value does not equal the expected value. What is going on here?

![Example 3 - adding 0.1 incrementally causes unexpected results](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/floating_point_error_with_addition0.png "Example 3 - adding 0.1 incrementally causes unexpected results")

In the screen below, we have formatted values in column B to display 15 decimal places, then expanded the column as needed. Now we can see the source of the problem clearly:

![Example 3 - floating point errors created by incremental addition](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/floating_point_error_with_addition1.png "Example 3 - floating point errors created by incremental addition")

All values in the range B14:B24 are very slightly different from expected because of floating-point errors. These errors show up here because Excel internally can’t represent increments of 0.1 in binary exactly. As we incrementally add 0.1, the small errors accumulate, resulting in values like -0.999999999999999 instead of -1.0.

To eliminate this problem, we can simply round each result to a suitable number of decimal places. In this case, the intent is clearly to work at 1 decimal place precision. So we should use around to 1 decimal place. This is actually the formula used in column C to calculate expected values:

    =ROUND(SEQUENCE(F6,,F4,F5),1)

![Example 3 - rounding to eliminate floating point errors](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/floating_point_error_with_addition2.png "Example 3 - rounding to eliminate floating point errors")

The original SEQUENCE formula above is now nested inside the ROUND function as the number argument, with 1 for _num\_digits_. The results in column C are now cleanly incremented in steps of 0.1. To compare the original raw values with the rounded values, we use a [conditional formatting rule](https://exceljet.net/conditional-formatting-formulas)
 applied with this formula:

    =$C5<>$B5

This highlights the rows where the rounded values are different from the raw values. In other words, the yellow highlight shows where floating-point errors have created an unexpected result.

> Tip: Round to match your intended precision. For step sizes of 0.1, use 1 decimal place. For cents, use 2. Don’t round too early—round late in the process or at the point of comparison.

### Set precision as displayed (not recommended)

There is another way to fix problems related to floating-point errors, using an Excel setting called "Set Precision as Displayed." This is a dangerous setting that essentially truncates any part of a number that isn't visible on screen. In other words, "what you see is what you get." While this is a very fast way to change hundreds or thousands of numbers, it should be used with extreme caution. This option forces Excel to store numbers exactly as they are displayed on screen by permanently altering the stored precision of numbers, which can result in permanent data loss. Also, because the setting applies globally across the workbook, it can impact unrelated calculations on different worksheets. As a result, I do not recommend this approach unless you fully understand its implications and are certain it won’t negatively impact other data.

### Other rounding functions in Excel

Although the ROUND function is fine for the purposes shown above, Excel has a whole group of rounding functions you can use to fix floating-point problems and rounding problems in general:

*   [ROUND](https://exceljet.net/functions/round-function)
    : Round to a specific number of digits
*   [ROUNDUP](https://exceljet.net/functions/roundup-function)
    : Always rounds up, away from zero
*   [ROUNDDOWN](https://exceljet.net/functions/rounddown-function)
    : Always rounds down, toward zero
*   [MROUND](https://exceljet.net/functions/mround-function)
    : Rounds to the nearest multiple
*   [CEILING](https://exceljet.net/functions/ceiling-function)
    : Rounds up to the nearest multiple
*   [FLOOR](https://exceljet.net/functions/floor-function)
    : Rounds down to the nearest multiple
*   [INT](https://exceljet.net/functions/int-function)
    : Rounds down to the nearest integer
*   [TRUNC](https://exceljet.net/functions/trunc-function)
    : Removes the decimal part without rounding

### Key Takeaways

*   Floating-point errors in Excel are due to Excel’s internal representation of numbers using floating-point arithmetic. They can happen at any time, but they don't normally cause problems because they involve tiny values.
*   If you are comparing calculated results with expected results directly, you can run into floating-point errors in a way that is surprising and confusing. In general, values that seem identical will be flagged as different.
*   These issues can be easily managed by being aware of the possibility and understanding why they happen.
*   One way to fix the problem is to round strategically, typically late in your calculations or inside the formula that checks results.
*   Another good option is to switch to a formula that confirms numbers are within a given tolerance. This approach involves no rounding and maintains maximum precision.
*   A final option to resolve floating-point errors is to use Excel's "Set precision as displayed" feature to force Excel to store numbers as displayed. You shouldn't use this option unless you fully understand the implications.

### Floating point details

Excel performs floating-point math according to the IEEE 754 standard, which is the foundation for how decimal numbers are stored and calculated in nearly all modern software.

When you type a number or use the = operator in Excel, the value is limited to 15 significant digits—the maximum precision Excel stores. If the digits match, Excel considers the numbers equal, even if tiny differences exist beyond that point. For example, both 0.1 + 0.2 and a hardcoded 0.3 round to the same stored value, so =0.1 + 0.2 = 0.3 returns TRUE.

In theory, subtracting the same values like this: =(0.1 + 0.2) - 0.3 should expose a small error like 5.55E-17, because these decimal values can't be stored exactly in binary. But in current versions of Excel, the result is often 0.

This is because Excel appears to have a "feature" that "zeroes out" very small results in certain arithmetic operations. The exact behavior isn’t documented by Microsoft (as far as I know), but it helps avoid distracting floating-point glitches in many common cases.

Even with this safeguard, floating-point errors can still appear in other ways, especially with larger calculations, comparisons, or repeated operations. The best solution remains the same: use rounding when precision matters.

### Useful Links

*   [Floating-point arithmetic may give inaccurate results in Excel](https://learn.microsoft.com/en-us/office/troubleshoot/excel/floating-point-arithmetic-inaccurate-result)
     (Microsoft)
*   [Numeric precision in Microsoft Excel](https://en.wikipedia.org/wiki/Numeric_precision_in_Microsoft_Excel)
     (Wikipedia)
*   [Floating point explanation desired](https://www.reddit.com/r/excel/comments/1cb1ej9/excelfloating_point_explanation_desired/)
     (reddit)

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