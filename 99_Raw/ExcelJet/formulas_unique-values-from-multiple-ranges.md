# Unique values from multiple ranges  - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/unique-values-from-multiple-ranges

---

[Skip to main content](https://exceljet.net/formulas/unique-values-from-multiple-ranges#main-content)

[](https://exceljet.net/formulas/unique-values-from-multiple-ranges#)

*   [Previous](https://exceljet.net/formulas/unique-values-case-sensitive)
    
*   [Next](https://exceljet.net/formulas/unique-values-ignore-blanks)
    

[Dynamic array](https://exceljet.net/formulas#Dynamic-array)

Unique values from multiple ranges
==================================

by Dave Bruns · Updated 13 Aug 2024

Related functions 
------------------

[UNIQUE](https://exceljet.net/functions/unique-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/7426/download?token=vZXmEX_J)
 (14.54 KB)

![Excel formula: Unique values from multiple ranges ](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/unique%20values%20from%20multiple%20ranges.png "Excel formula: Unique values from multiple ranges ")

Summary
-------

To extract unique values from more than one range at the same time, you can use the [UNIQUE function](https://exceljet.net/functions/unique-function)
 with the [VSTACK function](https://exceljet.net/functions/vstack-function)
. In the example shown, the formula in cell H5 is:

    =UNIQUE(VSTACK(range1,range2,range3))
    

Where **range1** (C5:C16), **range2** (D5:D15), and **range3** (F5:F13) are [named ranges](https://exceljet.net/glossary/named-range)
.

Generic formula
---------------

    =UNIQUE(VSTACK(range1,range2,range3))

Explanation 
------------

In this example, the goal is to extract unique values from three separate ranges at the same time: **range1** (C5:C16), **range2** (D5:D15), and **range3** (F5:F13). At one time, this was a difficult problem, since UNIQUE is programmed to accept only one array and there is no obvious way to provide another range.  However, with the introduction of the [VSTACK function](https://exceljet.net/functions/vstack-function)
, the solution is straightforward. 

### UNIQUE function

The [UNIQUE function](https://exceljet.net/functions/unique-function)
 makes it very easy to extract unique values from a range. Just give UNIQUE a range, and it will give you back the unique values:

    =UNIQUE(range) // extract unique
    

Like other [dynamic array formulas](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, the results from UNIQUE will [spill](https://exceljet.net/glossary/spill)
 onto the worksheet into multiple cells.

The challenge in this example is to provide more than one range to UNIQUE at the same time. The solution is to use the VSTACK function to combine ranges first, before invoking UNIQUE. This is done with the VSTACK function.

### VSTACK function

The [VSTACK function](https://exceljet.net/functions/vstack-function)
 combines arrays or ranges _vertically_ into a single [array](https://exceljet.net/glossary/array)
. For example, the formula below joins range1 and range2:

    =VSTACK(range1,range2) // combines ranges
    

Each additional array is appended to the _bottom_ of the previous array. The result from VSTACK is a single array with **range1** at the top. To combine more arrays, simply provide more arrays to VSTACK.

_Note: VSTACK is currently a Beta function available only through the Beta channel of Office Insiders. The [Office Insiders program](https://insider.office.com/)
 is free to join in Excel 365. Without VSTACK, it is still possible to combine ranges in a formula, but it is a [more complicated formula](https://exceljet.net/formulas/combine-ranges)
._

### UNIQUE with VSTACK

To solve the problem in this example, we simply need to [nest](https://exceljet.net/glossary/nesting)
 the VSTACK function inside the UNIQUE function like this:

    =UNIQUE(VSTACK(range1,range2,range3))
    

Working from the inside out, the VSTACK function combines all three ranges vertically into a single range:

    VSTACK(range1,range2,range3) // combine ranges into one
    

The combined [array](https://exceljet.net/glossary/array)
 has  **range1** on top, **range2** in the middle, and **range3** at the bottom:

    range1
    range2
    range3
    

This array is then delivered to the UNIQUE function, which returns the unique values in the combined range. The result is a list of unique values in all three ranges taken together.

### Empty cells

If any of the ranges to be combined contain empty cells, a zero (0) will appear as a unique value in the final result. To prevent empty cells from being evaluated by UNIQUE, you can use the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    =LET(
        data,VSTACK(range1,range2,range3),
        UNIQUE(FILTER(data,data<>""))
    )
    

In this formula, the [LET function](https://exceljet.net/functions/let-function)
 is used to store the result from VSTACK in the variable **data** so that it can be used twice inside the FILTER function without another call to VSTACK. For more details on the operation of FILTER with UNIQUE, [see this example](https://exceljet.net/formulas/unique-values-ignore-blanks)
.

### Legacy Excel

In [Legacy Excel](https://exceljet.net/glossary/legacy-excel)
, there is no UNIQUE function or VSTACK function, so the formula on this page is not possible. In simple scenarios, you can use a [formula based on INDEX and MATCH](https://exceljet.net/formulas/extract-unique-items-from-a-list)
 to extract unique values. See [Alternatives to Dynamic Array Functions](https://exceljet.net/articles/alternatives-to-dynamic-array-functions)
 for a more general discussion.

If you open the attached workbook in an older version of Excel without UNIQUE and/or VSTACK. You will see an [xlfn prefix](https://exceljet.net/glossary/xlfn)
 before the function name. The original result will still be displayed, but the formula will not update if source data changes.

Related formulas
----------------

[![Excel formula: Unique values](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values.png "Excel formula: Unique values")](https://exceljet.net/formulas/unique-values)

### [Unique values](https://exceljet.net/formulas/unique-values)

This example uses the UNIQUE function, which is fully automatic. When UNIQUE is provided with the range B5:B16, which contains 12 values, it returns the 7 unique values seen in D5:D11. UNIQUE is a dynamic function. If any data in B5:B16 changes, the output from UNIQUE will update immediately...

[![Excel formula: Unique values ignore blanks](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/unique%20values%20ignore%20blanks.png "Excel formula: Unique values ignore blanks")](https://exceljet.net/formulas/unique-values-ignore-blanks)

### [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)

This example uses the UNIQUE function together with the FILTER function. Working from the inside out, the FILTER function is first used to remove any blank values from the data: FILTER(B5:B16,B5:B16<>"") The <> symbol is a logical operator that means "does not equal". For more examples...

Related functions
-----------------

[![Excel UNIQUE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_unique_function.png "Excel UNIQUE function")](https://exceljet.net/functions/unique-function)

### [UNIQUE Function](https://exceljet.net/functions/unique-function)

The Excel UNIQUE function extracts unique values from a range or array. The result is a dynamic array that automatically updates when source data changes. UNIQUE is _not_ case-sensitive and works with text, numbers, dates, and other data types.

[![Excel VSTACK function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20vstack%20function.png "Excel VSTACK function")](https://exceljet.net/functions/vstack-function)

### [VSTACK Function](https://exceljet.net/functions/vstack-function)

The Excel VSTACK function combines arrays vertically into a single array. Each subsequent array is appended to the bottom of the previous array....

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Unique values](https://exceljet.net/formulas/unique-values)
    
*   [Unique values ignore blanks](https://exceljet.net/formulas/unique-values-ignore-blanks)
    

### Functions

*   [UNIQUE Function](https://exceljet.net/functions/unique-function)
    
*   [VSTACK Function](https://exceljet.net/functions/vstack-function)
    

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