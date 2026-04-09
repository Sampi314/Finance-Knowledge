# Dynamic array formulas in Excel | Exceljet

**Source:** https://exceljet.net/articles/dynamic-array-formulas-in-excel

---

[Skip to main content](https://exceljet.net/articles/dynamic-array-formulas-in-excel#main-content)

[](https://exceljet.net/articles/dynamic-array-formulas-in-excel#)

*   [Previous](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
    
*   [Next](https://exceljet.net/articles/excel-pivot-tables)
    

Dynamic array formulas in Excel
===============================

by Dave Bruns · Updated 3 Jul 2025

![The biggest change to Excel formulas in years](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/field/image/Dynamic%20array%20formulas%20in%20Excel.png "The biggest change to Excel formulas in years")

Summary
-------

Dynamic Arrays are the biggest change to Excel formulas in years. Maybe the biggest change ever. This is because Dynamic Arrays let you easily work with multiple values at the same time in a formula. This article provides an overview with many links and examples.

The key benefit of Dynamic Arrays is the ability to work with multiple values at the same time in a formula. This is a big upgrade and a welcome change. Dynamic Arrays solve some really hard problems in Excel, and will fundamentally change the way worksheets are designed. Once you see how they work, you'll never want to go back.

### Availability

Dynamic arrays and the new functions below are only available [Excel 365](https://exceljet.net/glossary/excel-365)
 and Excel 2021. Excel 2019 and earlier do not offer dynamic array formulas. For convenience, I'll use "[Dynamic Excel](https://exceljet.net/glossary/dynamic-excel)
" (Excel 365) and "[Legacy Excel](https://exceljet.net/glossary/legacy-excel)
" (2019 or earlier) to differentiate the Excel versions below.

> New: [Dynamic Array Formula video training](https://exceljet.net/training/dynamic-array-formulas)

### New functions

As part of the dynamic array update, Excel now includes 8 new functions that directly leverage dynamic arrays to solve problems that are traditionally hard to solve with conventional formulas. Click the links below for details and examples for each function:

| Function | Purpose |
| --- | --- |
| [FILTER](https://exceljet.net/functions/filter-function) | Filter data and return matching records |
| [RANDARRAY](https://exceljet.net/functions/randarray-function) | Generate an array of random numbers |
| [SEQUENCE](https://exceljet.net/functions/sequence-function) | Generate an array of sequential numbers |
| [SORT](https://exceljet.net/functions/sort-function) | Sort range by column |
| [SORTBY](https://exceljet.net/functions/sortby-function) | Sort range by another range or array |
| [UNIQUE](https://exceljet.net/functions/unique-function) | Extract unique values from a list or range |
| [XLOOKUP](https://exceljet.net/functions/xlookup-function) | Modern replacement for VLOOKUP |
| [XMATCH](https://exceljet.net/functions/xmatch-function) | Modern replacement for the MATCH function |

Video: [New dynamic array functions in Excel](https://exceljet.net/videos/new-dynamic-array-functions-in-excel)
 (about 3 minutes).

> As of September 2024, almost [50 new functions](https://exceljet.net/new-excel-functions)
>  have been added to Excel!

### Example

Before we get into the details, let's look at a simple example. Below we are using the new [UNIQUE function](https://exceljet.net/functions/unique-function)
 to extract unique values from the range B5:B15, with a _single_ formula entered in E5:

    =UNIQUE(B5:B15) // return unique values in B5:B15
    

![UNIQUE function example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/unique%20function%20example.png?itok=zi6fPU7T "UNIQUE function example")

The result is a list of the five unique city names, which appear in E5:E9.

Like all formulas, UNIQUE will update automatically when data changes. Below, Vancouver has replaced Portland on row 11. The result from UNIQUE now includes Vancouver:

![UNIQUE function example after change](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/unique%20function%20example%202.png?itok=G1cZZNCU "UNIQUE function example after change")

### Spilling - one formula, many values

In Dynamic Excel, formulas that return multiple values will "[spill](https://exceljet.net/glossary/spill)
" these values directly onto the worksheet. This will immediately be more logical to formula users. It is also a fully dynamic behavior – when source data changes, spilled results will immediately update.

The rectangle that encloses the values is called the "[spill range](https://exceljet.net/glossary/spill-range)
". You will notice that the spill range has special highlighting. In the UNIQUE example above, the spill range is E5:E10.

When data changes, the spill range will expand or contract as needed. You might see new values added, or existing values disappear. In this way, a spill range is a new kind of dynamic range.

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, by contrast, you can see multiple results returned by an array formula in the formula bar if you [use F9 to inspect the formula](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
. However, unless the formula is entered as a [multi-cell array formula](https://exceljet.net/glossary/multi-cell-array-formula)
, only _one value_ will be displayed on the worksheet. This behavior has always made array formulas difficult to understand. Spilling makes array formulas more intuitive. 

_Note: when spilling is blocked by other data, you'll see a #SPILL error. Once you make room for the spill range, the formula will automatically spill._

Video: [Spilling and the spill range](https://exceljet.net/videos/spilling-and-the-spill-range)

### Spill range reference

To refer to a spill range, use a hash symbol (#) after the first cell in the range. For example, to reference the results from the UNIQUE function above use:

    =E5# // reference UNIQUE results
    

This is the same as referencing the entire spill range, and you'll see this syntax when you write a formula that refers to a complete spill range.

You can feed a spill range reference into other formulas directly. For example, to count the number of cities returned by UNIQUE, you can use:

    =COUNTA(E5#) // count unique cities
    

![Example of dynamic array spill range reference](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20array%20spill%20range%20reference%20example.png?itok=JPMsh0Ay "Example of dynamic array spill range reference")

When the spill range changes, the formula will reflect the latest data.

### Massive simplification

The addition of new dynamic array formulas means certain formulas can be drastically simplified. Here are a few examples:

*   Extract and list unique values ([before](https://exceljet.net/formulas/extract-unique-items-from-a-list)
     | [after](https://exceljet.net/functions/unique-function)
    )
*   Count unique values ([before](https://exceljet.net/formulas/count-unique-text-values-in-a-range)
     | [after](https://exceljet.net/formulas/count-unique-values)
    )
*   Filter and extract records ([before](https://exceljet.net/formulas/get-nth-match-with-index-match)
     | [after](https://exceljet.net/formulas/basic-filter-example)
    )
*   Extract partial matches ([before](https://exceljet.net/formulas/index-and-match-all-partial-matches)
     | [after](https://exceljet.net/formulas/filter-text-contains)
    )

### The power of one

One of the most powerful benefits of the "one formula, many values" approach is less reliance on [absolute](https://exceljet.net/glossary/absolute-reference)
 or [mixed](https://exceljet.net/glossary/mixed-reference)
 references. As a dynamic array formula spills results onto the worksheet, references remain unchanged, but the formula generates correct results.

For example, below we use the FILTER function to extract records in group "A". In cell F5, a single formula is entered:

    =FILTER(B5:D11,B5:B11="a") // references are relative
    

![Dynamic array one formula only example](https://exceljet.net/sites/default/files/images/articles/inline/dynamic%20array%20one%20formula%20only.png "Dynamic array one formula only example")

Notice both ranges are unlocked relative references, but the formula works perfectly.

This is a huge benefit for many users because it makes the process of writing formulas so much simpler. For another good example, see the multiplication table below.

### Chaining functions

Things get really interesting when you chain together more than one dynamic array function. Perhaps you want to sort the results returned by UNIQUE? Easy. Just wrap the [SORT function](https://exceljet.net/functions/sort-function)
 around the UNIQUE function like this:

![Example of UNIQUE and SORT together](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/unique%20function%20example%203.png?itok=1cQ2Camw "Example of UNIQUE and SORT together")

As before, when source data changes, new unique results automatically appear, nicely sorted.

### Native behavior

It's important to understand that dynamic array behavior is [_native and deeply integrated_](https://exceljet.net/videos/dynamic-arrays-are-native)
_._ When _any_ formula returns multiple results, these results will spill into multiple cells on the worksheet. This includes older functions not originally designed to work with dynamic arrays.

For example, in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, if we give the [LEN function](https://exceljet.net/functions/len-function)
 a _range_ of text values, we'll see a _single_ result. In Dynamic Excel, if we give the LEN function a range of values, we'll see _multiple_ results. This screen below shows the old behavior on the left and the new behavior on the right:

![The LEN function with arrays - old and new](https://exceljet.net/sites/default/files/images/articles/inline/LEN%20function%20dynamic%20array%20example.png "The LEN function with arrays - old and new")

This is a huge change that can affect all kinds of formulas. For instance, the [VLOOKUP function](https://exceljet.net/functions/vlookup-function)
 is designed to fetch a single value from a table, using a column index. However, in Dynamic Excel, if we give VLOOKUP more than one column index using an [array constant](https://exceljet.net/glossary/array-constant)
 like this:

    =VLOOKUP("jose",F7:H10,{1,2,3},0)
    

VLOOKUP will return multiple columns:

![Multiple results with VLOOKUP and dynamic arrays](https://exceljet.net/sites/default/files/images/articles/inline/VLOOKUP%20dynamic%20array%20multiple%20results.png "Multiple results with VLOOKUP and dynamic arrays")

In other words, even though VLOOKUP was never designed to return multiple values, it can now do so, thanks to the new formula engine in Dynamic Excel.

### All formulas

Finally, note that dynamic arrays work with _all formulas_ not just [functions](https://exceljet.net/functions)
. In the example below cell C5 contains a single formula:

    =B5:B14*C4:L4
    

The result spills into a 10 by 10 range that includes 100 cells:

![Dynamic array multiplication table](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/dynamic%20array%20multiplication%20table.png?itok=zpjuUT2R "Dynamic array multiplication table")

If the numbers in the ranges B5:B14 and C4:L4 where are themselves dynamic arrays (i.e. created with the [SEQUENCE function](https://exceljet.net/functions/sequence-function)
), the spill reference operator can be used like this:

    =B5#*C4# // returns same 10 x 10 array
    

### Arrays go mainstream

With the rollout of dynamic arrays, the word "[array](https://exceljet.net/glossary/array)
" is going to pop up much more often. In fact, you may see "array" and "range" used almost interchangeably. You'll see arrays in Excel enclosed in curly braces like this:

    {1,2,3} // horizontal array
    {1;2;3} // vertical array
    

Array is a programming term that refers to a list of items that appear in a particular order. The reason arrays come up so often in Excel formulas is that arrays can [perfectly express the values in a range of cells](https://exceljet.net/glossary/array)
.

Video: [What is an array?](https://exceljet.net/videos/what-is-an-array)

### Array operations become important

Because Dynamic Excel formulas can easily work with multiple values, array operations will become more important. The term "array operation" refers to an expression that runs a logical test or math operation on an array. For example, the expression below tests if values in B5:B9 are equal to "ca"

    =B5:B9="ca" // state = "ca"
    

![Array operation example test a](https://exceljet.net/sites/default/files/images/articles/inline/array%20operation%20example%20test%20a.png "Array operation example test a")

because there are 5 cells in B5:B9, the result is 5 TRUE/FALSE values in an array:

    {FALSE;TRUE;FALSE;TRUE;TRUE}
    

The array operation below checks for amounts greater than 100:

    =C5:C9>100 // amounts > 100
    

![Array operation example test b](https://exceljet.net/sites/default/files/images/articles/inline/array%20operation%20example%20test%20b.png "Array operation example test b")

The final array operation combines test A and test B in a single expression:

    =(B5:B9="ca")*(C5:C9>100) // state = "ca" and amount > 100
    

![Array operation example test a and b](https://exceljet.net/sites/default/files/images/articles/inline/array%20operation%20example%20test%20a%20and%20b.png "Array operation example test a and b")

Note: Excel automatically coerces the TRUE and FALSE values to 1 and 0 during the math operation.

To bring this back to dynamic array formulas in Excel, the example below demonstrates how we can use exactly the same array operation inside the FILTER function as the _include_ argument:

![Array operation with FILTER function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/articles/inline/array%20operation%20with%20FILTER%20function.png?itok=jJ2m5peR "Array operation with FILTER function")

FILTER returns the two records where state = "ca" and amount > 100.

For a demonstration, see: [How to filter with two criteria](https://exceljet.net/videos/filter-function-with-two-criteria)
 (video).

### New and old array formulas

In Dynamic Excel, there is no need to enter array formulas with control + shift + enter. When a formula is created, Excel checks if the formula might return multiple values. If so, it will automatically be saved as a dynamic array formula, but you will not see curly braces. The example below shows a typical array formula entered in Dynamic Excel:

![Basic array formula in Legacy Excel](https://exceljet.net/sites/default/files/images/articles/inline/basic%20array%20formula%20-%20dynamic%20excel.png "Basic array formula in Legacy Excel")

If you open the same formula in [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, you'll see curly braces:

![Basic array formula in dynamic Excel](https://exceljet.net/sites/default/files/images/articles/inline/basic%20array%20formula%20-%20traditional%20excel.png "Basic array formula in dynamic Excel")

Going the other direction, when a "traditional" array formula is opened in Dynamic Excel, you will see the curly braces in the formula bar.  For example, the screen below shows a simple array formula in Legacy Excel:

![Simple array formula with curly braces visible](https://exceljet.net/sites/default/files/images/articles/inline/simple%20array%201%20braces%20visible.png "Simple array formula with curly braces visible")

However, if you re-enter the formula with no changes, the curly braces are removed, and the formula returns the same result:

![Simple array formula with curly braces not visible](https://exceljet.net/sites/default/files/images/articles/inline/simple%20array%202%20braces%20gone.png "Simple array formula with curly braces not visible")

The bottom line is that array formulas entered with control + shift + enter (CSE) still work to maintain compatibility, but you shouldn't need to enter array formulas with CSE in Dynamic Excel.

### Spilling limitations and the plus (+) operator

The term "lifting" refers to an _array calculation behavior_ in Excel formulas. When you give a range or array to a function not programmed to accept arrays natively (i.e. an older function), Excel will "lift" the function and call it multiple times, one time for each value in the array. The result is an array with the same dimensions as the input array. Lifting is a built-in behavior that happens automatically.

In Dynamic Excel, some older functions like EOMONTH "resist" spilling when provided a range. So, for example, EOMONTH(A1:A5,1) will return #VALUE even with valid dates in A1:A5. This limitation comes from certain functions expecting a single value instead of a range. The #VALUE! error is essentially reporting the range as an unexpected value. However, adding an operator in front of the reference will often fix the problem. For example, EOMONTH(+A1:A5,1) will work and spill properly. This is because adding the + in front of A1:A5 forces Excel to evaluate the expression first, before the function runs. The result of +A1:A5 is an array containing 5 values, which are then passed into EOMONTH as the start date. EOMONTH returns 5 results through the normal process of lifting, which is not function-specific. Other functions that have this same limitation include EDATE, ISEVEN, ISODD, YEARFRAC, WORKDAY, and WORKDAY.INTL.

> For more details and a list of functions that have this problem, see: [Why some functions won't spill](https://exceljet.net/articles/why-some-excel-functions-wont-spill)
> .

### The @ character

With the introduction of dynamic arrays, you're going to see the @ character appear more often in formulas. The @ character enables a behavior known as "[implicit intersection](https://exceljet.net/glossary/implicit-intersection)
". Implicit intersection is a logical process where many values are reduced to one value. 

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, implicit intersection is a silent behavior used (when necessary) to reduce multiple values to a single result in one cell. In Dynamic Excel, it is not typically needed, since multiple results can spill onto the worksheet. When it is needed, implicit intersection is invoked manually with the @ character.

When opening spreadsheets created in an older version of Excel, you may see the @ character added automatically to existing formulas that have the _potential_ to return many values. In Legacy Excel, a formula that returns multiple values won't spill on the worksheet. The @ character forces this same behavior in Dynamic Excel so that the formula behaves the same way and returns the same result as it did in the original Excel version.

In other words, the @ is added to prevent an older formula from spilling multiple results onto the worksheet. Depending on the formula, you may be able to remove the @ character and the behavior of the formula will not change. 

### Summary

*   Dynamic Arrays will make certain formulas much easier to write.
*   You can now filter matching data, sort, and extract unique values easily with formulas.
*   Dynamic Array formulas can be chained (nested) to do things like filter and sort.
*   Formulas that return more than one value will automatically spill.
*   It is not necessary to use Ctrl+Shift+Enter to enter an array formula.
*   Dynamic array formulas are only available in Excel 365. 

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