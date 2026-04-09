# Sum if one of many things - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/sum-if-one-of-many-things

---

[Skip to main content](https://exceljet.net/formulas/sum-if-one-of-many-things#main-content)

[](https://exceljet.net/formulas/sum-if-one-of-many-things#)

*   [Previous](https://exceljet.net/formulas/sum-if-not-blank)
    
*   [Next](https://exceljet.net/formulas/sum-if-with-multiple-ranges)
    

[Sum](https://exceljet.net/formulas#Sum)

Sum if one of many things
=========================

by Dave Bruns · Updated 21 Dec 2022

Related functions 
------------------

[SUMIFS](https://exceljet.net/functions/sumifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNUMBER](https://exceljet.net/functions/isnumber-function)

[MATCH](https://exceljet.net/functions/match-function)

[FILTER](https://exceljet.net/functions/filter-function)

![Excel formula: Sum if one of many things](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/sum_if_one_of_many_things.png "Excel formula: Sum if one of many things")

Summary
-------

To sum values when cells are equal to _one of many things_, you can use a formula based on the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 and the [SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)
 function. In the example shown, the formula in I5 is:

    =SUMPRODUCT(SUMIFS(E5:E16,B5:B16,things))
    

where **things** is the [named range](https://exceljet.net/glossary/named-range)
 G5:G7. The result is $19.50, the sum of Price where Item is "Apples", "Pears", or "Kiwis".

Generic formula
---------------

    =SUMPRODUCT(SUMIFS(values,range,things))

Explanation 
------------

In this example, the goal is to sum the numbers in column E when the item in column B appears in the range G5:G7. The named range **things** is not required. It is used only for convenience and can be expanded as needed to include additional criteria. The article below explains several ways to solve this problem.

### SUMIFS with SUMPRODUCT

One way to accomplish this is to give the SUMIFS function all three values in the [named range](https://exceljet.net/glossary/named-range)
 **things** (G5:G7) as criteria, then use the SUMPRODUCT function to calculate a total. This is the approach in the worksheet shown, where the formula in I5 is:

    =SUMPRODUCT(SUMIFS(E5:E16,B5:B16,things))
    

Working from the inside out, the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 takes three arguments: _sum\_range_, _range_, and _criteria._

*   _Sum\_range is_ E5:E16 and contains the values we want to sum.
*   _Range is_ B5:B15 and contains the values we are testing.
*   _Criteria_ is the named range **things** (G5:G7), which contains 3 values.

When Excel evaluates this formula, it retrieves the values in **things** as an [array](https://exceljet.net/glossary/array)
 like this:

    =SUMPRODUCT(SUMIFS(E5:E16,B5:B16,{"apples";"pears";"kiwis"}))

Because SUMIFS receives 3 separate values for _criteria_, it returns 3 results in an array like this:

    {3.75;11.25;4.5}

The first number is a sum for "apples", the second number is a sum for "Pears", and the last number is a sum for "Kiwis". These results are returned directly to the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 like this:

    =SUMPRODUCT({3.75;11.25;4.5})

With just one array to process, SUMPRODUCT sums the array and returns a final result of $19.50.

_Note: in the latest version of Excel, you can use the SUM function instead of SUMPRODUCT in this formula. Read more about this topic here: [Why SUMPRODUCT?](https://exceljet.net/articles/why-sumproduct)
_

### ISNUMBER and MATCH

The above formula works fine, but has some limitations due to the [nature of SUMIF](https://exceljet.net/articles/excels-racon-functions)
. As an alternative, you can use the formula below, which uses the [ISNUMBER function](https://exceljet.net/functions/isnumber-function)
 with the [MATCH function](https://exceljet.net/functions/match-function)
 to achieve the same result:

    =SUMPRODUCT(--ISNUMBER(MATCH(B5:B16,things,0)),E5:E16)
    

This is a more flexible formula in cases where logical conditions become more complex. [This formula shows one example](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
.

### FILTER function

This problem can also be solved in a more literal way with the [FILTER function](https://exceljet.net/functions/filter-function)
 like this:

    =SUM(FILTER(E5:E16,ISNUMBER(MATCH(B5:B16,things,0)),0))

In this formula, FILTER is configured to use ISNUMBER + MATCH to extract the Price of Items that appear in the named range _things_. The result is delivered to the [SUM function](https://exceljet.net/functions/sum-function)
 which returns a final result. See [this example](https://exceljet.net/formulas/filter-contains-one-of-many)
 for more details.

Related formulas
----------------

[![Excel formula: Sum if multiple criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/sum_if_multiple_criteria.png "Excel formula: Sum if multiple criteria")](https://exceljet.net/formulas/sum-if-multiple-criteria)

### [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)

In this example, the goal is to sum the values in F5:F16 when the Color in C5:C16 is "Red" and the State in D5:D16 is "TX". This is an example of a conditional sum with multiple criteria and the SUMIFS function is the easiest way to solve this problem. SUMIFS function The SUMIFS function sums cells...

[![Excel formula: If cell contains one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/If%20cell%20contains%20one%20of%20many%20things.png "Excel formula: If cell contains one of many things")](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

### [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)

This formula uses two named ranges : things , and results . If you are porting this formula directly, be sure to use named ranges with the same names (defined based on your data). If you don't want to use named ranges, use absolute references instead. The core of this formula is this snippet:...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

[![Excel formula: Count cells equal to one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20one%20of%20many%20things.png "Excel formula: Count cells equal to one of many things")](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

### [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

In this example, the goal is to count the values in column B listed in the range E5:E7. One way to do this is to give the COUNTIF function all three values in the named range things (E5:E7) as criteria, then use the SUMPRODUCT function to get a total. The formula in G4 is: =SUMPRODUCT(COUNTIF(B5:...

[![Excel formula: Categorize text with keywords](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/categorize_text_with_keywords.png "Excel formula: Categorize text with keywords")](https://exceljet.net/formulas/categorize-text-with-keywords)

### [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)

In this example, the goal is to categorize various expenses using the categories shown in column F and the keywords shown in column E. This is a case where it seems like we should perform a lookup operation of some kind, but the problem is that the keywords appear embedded in the text and the...

Related functions
-----------------

[![Excel SUMIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumifs%20function.png "Excel SUMIFS function")](https://exceljet.net/functions/sumifs-function)

### [SUMIFS Function](https://exceljet.net/functions/sumifs-function)

The Excel SUMIFS function returns the sum of cells that meet multiple conditions, referred to as criteria. To define criteria, SUMIFS supports logical operators (>,<,<>,=) and wildcards (\*,?,~), and can be used with cells that contain dates, numbers, and text.

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

[![Excel ISNUMBER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isnumber%20function.png "Excel ISNUMBER function")](https://exceljet.net/functions/isnumber-function)

### [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)

The Excel ISNUMBER function returns TRUE when a cell contains a number, and FALSE if not. You can use ISNUMBER to check that a cell contains a numeric value, or that the result of another function is a number.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel FILTER function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_filter_function.png "Excel FILTER function")](https://exceljet.net/functions/filter-function)

### [FILTER Function](https://exceljet.net/functions/filter-function)

The Excel FILTER function is used to extract matching values from data based on one or more conditions. The output from FILTER is dynamic. If source data or criteria change, FILTER will return a new set of results. This makes FILTER a flexible way to isolate and inspect data without...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20SUMIFs%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-sumifs-function)

### [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)

In this video, we'll look at how to use the SUMIFS function to sum cells that meet multiple criteria. Let's take a look. SUMIFS has three required arguments: sum\_range, criteria\_range1, and criteria1 . After that, you can enter additional range and criteria pairs to add additional conditions. In...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Sum if multiple criteria](https://exceljet.net/formulas/sum-if-multiple-criteria)
    
*   [If cell contains one of many things](https://exceljet.net/formulas/if-cell-contains-one-of-many-things)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    
*   [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    
*   [Categorize text with keywords](https://exceljet.net/formulas/categorize-text-with-keywords)
    

### Functions

*   [SUMIFS Function](https://exceljet.net/functions/sumifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNUMBER Function](https://exceljet.net/functions/isnumber-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [FILTER Function](https://exceljet.net/functions/filter-function)
    

### Videos

*   [How to use the SUMIFS function](https://exceljet.net/videos/how-to-use-the-sumifs-function)
    

### Training

*   [Core Formula](https://exceljet.net/training/core-formula)
    

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