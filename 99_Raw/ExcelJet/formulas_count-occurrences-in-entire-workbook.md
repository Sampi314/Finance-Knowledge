# Count occurrences in entire workbook - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-occurrences-in-entire-workbook

---

[Skip to main content](https://exceljet.net/formulas/count-occurrences-in-entire-workbook#main-content)

[](https://exceljet.net/formulas/count-occurrences-in-entire-workbook#)

*   [Previous](https://exceljet.net/formulas/count-numbers-with-leading-zeros)
    
*   [Next](https://exceljet.net/formulas/count-or-sum-variance)
    

[Count](https://exceljet.net/formulas#Count)

Count occurrences in entire workbook
====================================

by Dave Bruns · Updated 14 May 2024

Related functions 
------------------

[COUNTIF](https://exceljet.net/functions/countif-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[VSTACK](https://exceljet.net/functions/vstack-function)

![Excel formula: Count occurrences in entire workbook](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20occurrences%20in%20entire%20workbook.png "Excel formula: Count occurrences in entire workbook")

Summary
-------

To count total matches across an entire workbook, you can use a formula based on the [COUNTIF](https://exceljet.net/functions/countif-function)
 and [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 functions. In the example shown, the formula in D5 is:

    =SUMPRODUCT(COUNTIF(INDIRECT("'"&sheets&"'!"&B8),B5))
    

where **sheets** is the [named range](https://exceljet.net/glossary/named-range)
 B11:B13. The result is 16 since there are sixteen occurrences of "Steven" in Sheet1, Sheet2, and Sheet3.

_Note: In newer versions of Excel, you can also use the [VSTACK function](https://exceljet.net/functions/vstack-function)
 as explained below._

Generic formula
---------------

    =SUMPRODUCT(COUNTIF(INDIRECT("'"&sheets&"'!"&range),criteria))

Explanation 
------------

In this example, the goal is to count the value in cell B5 ("Steven") in the sheets listed in B11:B13. The workbook shown in the example has four worksheets in total. The first sheet is named "Master" and contains the search string, the range, and the sheets to include in the count, as seen in the screenshot above. The next three sheets, "Sheet1", "Sheet2", and "Sheet3" each contain 1000 random first names in the range B4:F203. The table in each sheet looks like this:

![Sample data - 1000 random names in each sheet](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/inline/count%20occurrences%20in%20entire%20workbook%20data.png?itok=59D7hjwO "Sample data - 1000 random names in each sheet")

Note that the range (B4:F203) must be adjusted to suit your data.

### COUNTIF function

The [COUNTIF function](https://exceljet.net/functions/countif-function)
 returns the count of cells that meet one or more criteria and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. One way to solve this problem is to use the COUNTIF function three times in a formula like this:

    =COUNTIF(Sheet1!B4:F203,B5)+COUNTIF(Sheet2!B4:F203,B5)+COUNTIF(Sheet3!B4:F203,B5)
    

With "Steven" in cell B5, this formula returns 16. This formula works but becomes cumbersome as the number of sheets increases. You might think you could use a [3D reference](https://exceljet.net/videos/how-to-create-3d-references)
 like this:

    =COUNTIF(Sheet1:Sheet3!B4:F203,B5)
    

However, COUNTIF is in a [group of eight functions that have some particular quirks](https://exceljet.net/articles/excels-racon-functions)
. One of these quirks is that you can't use a 3D reference for the _range_ argument. As a workaround, you can use the INDIRECT function to assemble an array constant, then feed that into COUNTIF. This approach helps streamline the formula as explained below.

### COUNTIF with INDIRECT

The [INDIRECT function](https://exceljet.net/functions/indirect-function)
 converts a given [text string](https://exceljet.net/glossary/text-value)
 into a proper Excel reference:

    =INDIRECT("A1") // returns A1
    

We can use INDIRECT in this example to create an array constant that contains all three range references as text. In the example shown, the formula in cell D5 is:

    =SUMPRODUCT(COUNTIF(INDIRECT("'"&sheets&"'!"&B8),B5))
    

Working from the inside out, the INDIRECT function is used to assemble a reference to all three ranges like this:

    INDIRECT("'"&sheets&"'!"&B8)
    

Because the named range **sheets** contains three cells, the code expands like this:

    INDIRECT({"'Sheet1'!B4:F203";"'Sheet2'!B4:F203";"'Sheet3'!B4:F203"})
    

The result in INDIRECT is an [array constant](https://exceljet.net/glossary/array-constant)
 that contains three text strings, each representing a range on each of the three sheets. INDIRECT will evaluate the text values and pass the references into COUNTIF as the _range_ argument. For reasons that are somewhat mysterious, COUNTIF will accept the result from INDIRECT without complaint. Because COUNTIF receives more than one range, it will return more than one result in an [array](https://exceljet.net/glossary/array)
 like this:

    COUNTIF(INDIRECT("'"&sheets&"'!"&B8) // returns {5;6;5}
    

The code above will return three counts in an array to the SUMPRODUCT function:

    =SUMPRODUCT({5;6;5})
    

With just one array to process, SUMPRODUCT sums the items in the array and returns 16 as a final result. Note that INDIRECT is a [volatile function](https://exceljet.net/glossary/volatile-function)
 and can impact workbook performance.

### VSTACK function

In the current version of Excel, you can use the [VSTACK function](https://exceljet.net/functions/vstack-function)
 with a [3D reference](https://exceljet.net/videos/how-to-create-3d-references)
 to achieve the same result with a more elegant formula:

    =SUMPRODUCT(--(VSTACK(Sheet1:Sheet3!B4:F203)=B5))
    

The VSTACK function combines the three ranges vertically into a single range and feeds the result into the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. Each cell in the combined range is compared to the value in cell B5 ("Steven") resulting in a large array containing only TRUE and FALSE values. We then use a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) to convert the TRUE and FALSE values into their numeric equivalents, 1 and 0. The numeric array is returned to SUMPRODUCT, which sums all items in the array and returns 16 as a final result. This is an example of using [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, a common way to solve more complicated problems in Excel.

_Note: In Excel 365 and Excel 2021 you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT if you prefer in both formulas above. [This article provides more detail](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Search entire worksheet for value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Search%20entire%20worksheet%20for%20value.png "Excel formula: Search entire worksheet for value")](https://exceljet.net/formulas/search-entire-worksheet-for-value)

### [Search entire worksheet for value](https://exceljet.net/formulas/search-entire-worksheet-for-value)

The second sheet in the workbook, Sheet2, contains 1000 first names in the range B4:F203. The COUNTIF function takes a range and a criteria. In this case, we give COUNTIF a range equal to all rows in Sheet2. Sheet2!1:1048576 Note: an easy way to enter this range is to use the Select All button ...

[![Excel formula: Search multiple worksheets for value](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/search%20multiple%20worksheets%20for%20value.png "Excel formula: Search multiple worksheets for value")](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

### [Search multiple worksheets for value](https://exceljet.net/formulas/search-multiple-worksheets-for-value)

The range B7:B9 contains the sheet names we want to include in the search. These are just text strings, and we need to do some work to get them to be recognized as valid sheet references. Working from the inside out, this expression is used to build a full sheet reference: "'"...

Related functions
-----------------

[![Excel COUNTIF function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countif_function.png "Excel COUNTIF function")](https://exceljet.net/functions/countif-function)

### [COUNTIF Function](https://exceljet.net/functions/countif-function)

The Excel COUNTIF function returns the count of cells in a range that meet a single condition. The generic syntax is COUNTIF(range, criteria), where "range" contains the cells to count, and "criteria" is a condition that must be true for a cell to be counted. COUNTIF can be used to count...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

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

*   [Search entire worksheet for value](https://exceljet.net/formulas/search-entire-worksheet-for-value)
    
*   [Search multiple worksheets for value](https://exceljet.net/formulas/search-multiple-worksheets-for-value)
    

### Functions

*   [COUNTIF Function](https://exceljet.net/functions/countif-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
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