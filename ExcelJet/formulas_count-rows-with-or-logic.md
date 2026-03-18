# Count rows with OR logic - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-rows-with-or-logic

---

[Skip to main content](https://exceljet.net/formulas/count-rows-with-or-logic#main-content)

[](https://exceljet.net/formulas/count-rows-with-or-logic#)

*   [Previous](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Next](https://exceljet.net/formulas/count-sold-and-remaining)
    

[Count](https://exceljet.net/formulas#Count)

Count rows with OR logic
========================

by Dave Bruns · Updated 18 Jul 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/6304/download?token=69sNEW6L)
 (17.66 KB)

![Excel formula: Count rows with OR logic](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20rows%20with%20OR%20logic.png "Excel formula: Count rows with OR logic")

Summary
-------

To count rows with OR logic, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in G6 is:

    =SUMPRODUCT((group="a")*((color1="red")+(color2="red")>0))
    

where **group** (B5:B15), **color1** (C5:C15), and **color2** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

Explanation 
------------

One of the trickier problems in Excel is to count rows in a set of data with "OR logic". There are two basic scenarios: (1) you want to count rows where a value in a column is "x" OR "y" (2) you want to count rows where a value, "x", exists in one column OR another.

In this example, the goal is to count rows where group = "a" AND **Color1** OR **Color2** are "red". This means we are working with scenario 2 above.

### With COUNTIFS

You might at first reach for the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, which handles multiple criteria natively. However, the COUNTIFS function joins conditions with AND logic, so _all criteria must be TRUE_ to be included in the count:

    =COUNTIFS(group,"a",color1,"red",color2,"red") // returns 1
    

This makes COUNTIFS unworkable, _unless_ we use multiple instances of COUNTIFS:

    =COUNTIFS(group,"a",color1,"red")+COUNTIFS(group,"a",color2,"red")-COUNTIFS(group,"a",color1,"red",color2,"red")
    

_Translation: count rows where group is "a" and color1 is "red" + count rows where group is "a" and color2 is "red". Then subtract the count of rows where group is "a" and color1 is "red" and color2 is "red" (to avoid double counting)._

This works, but you can see this is a somewhat complicated and redundant formula.

### With Boolean logic

A better solution is to use [Boolean logic](https://exceljet.net/glossary/boolean-logic)
, and process the result with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. (If you need a primer on Boolean algebra, [this video provides an introduction](https://exceljet.net/videos/boolean-algebra-in-excel)
.)  In the example shown, the formula in G6 is:

    =SUMPRODUCT((group="a")*((color1="red")+(color2="red")>0))
    

where **group** (B5:B15), **color1** (C5:C15), and **color2** (D5:D15) are [named ranges](https://exceljet.net/glossary/named-range)
.

The first part of the problem is to test for group = "a" which we do like this:

    (group="a")
    

Because the range B5:B15 contains 11 cells, this expression returns an array of 11 TRUE and FALSE values like this:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

Each TRUE represents a row where the group is "A".

Next, we need to check for the value "red" in either **color1** or **color2.** We do this with two expressions joined by addition (+), since addition corresponds with OR logic in Boolean algebra:

    (color1="red")+(color2="red")
    

Excel automatically evaluates TRUE and FALSE values as 1s and 0s during any math operation, so the result from the above expression is an array like this:

    {2;0;0;1;1;0;1;0;0;0;1}
    

The first number in the array is 2, because both **Color1** and **Color2** are "red" in the first row. For reasons explained below, we need to guard against this situation by checking for values greater than zero:

    ({2;0;0;1;1;0;1;0;0;0;1})>0
    

Now we again have an array of TRUE and FALSE values:

    {TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

The table below summarizes how Excel evaluates the color logic explained above:

![How color logic is evaluated in this formula](https://exceljet.net/sites/default/files/images/formulas/inline/color%20logic%20table.png "How color logic is evaluated in this formula")

At this point, we have results from testing **Group** ="a" in one array:

    {TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE;FALSE;FALSE}
    

And results from testing "red" in **Color1** or **Color2** in another array:

    {TRUE;FALSE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;FALSE;TRUE}
    

The next step is to bring these two arrays together with "AND logic". To do this, we use multiplication (\*), since multiplication corresponds to AND logic in Boolean algebra.

After multiplying the two arrays together, we have a single array of 1s and 0s, which is delivered directly to the SUMPRODUCT function:

    =SUMPRODUCT({1;0;0;0;1;0;0;0;0;0;0})
    

The SUMPRODUCT function returns the sum of numbers, 2, as a final result. This is the count of rows where group = "a" AND **Color1** OR **Color2** are "red".

### To avoid double counting

We don't want to double count rows where both **Color1** and **Color2** are "red". This is why we check the results from (**color1**\="red")+(**color2**\="red") for values greater than zero in the code below:

    ((color1="red")+(color2="red"))>0
    

Without this check, the 2 from the first row in the data would show up in the final array, and cause the formula to incorrectly return 3 as the final count.

### FILTER option

One nice thing about Boolean logic is that it works perfectly with [Excel's newest functions](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, like [XLOOKUP](https://exceljet.net/functions/xlookup-function)
 and [FILTER](https://exceljet.net/functions/filter-function)
. For example, the FILTER function can use exactly the same logic explained above to extract matching rows:

    =FILTER(B5:D15,(group="a")*((color1="red")+(color2="red")>0))
    

The result from FILTER is the two rows that meet criteria, as seen below:

![FILTER rows with OR logic](https://exceljet.net/sites/default/files/images/formulas/inline/FILTER%20rows%20with%20or%20logic.png "FILTER rows with OR logic")

If you'd like to learn more about these new functions, we have an [overview](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
, and [video training](https://exceljet.net/training/dynamic-array-formulas)
.

Related formulas
----------------

[![Excel formula: Count rows with multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20multiple%20OR%20criteria.png "Excel formula: Count rows with multiple OR criteria")](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

### [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)

In this example, the goal is to count rows using OR logic based on the criteria shown in column F. For example, in cell G5 we want to count rows where Color is "Blue" OR Pet is "Dog". This can be done with Boolean logic and the SUMPRODUCT function , as explained below. Notes This formula uses an...

[![Excel formula: Count cells equal to this or that](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20this%20or%20that.png "Excel formula: Count cells equal to this or that")](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

### [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)

In this example, the goal is to count cells in the range D5:D15 that contain "red" or "blue". For convenience, the D5:D15 is named color . Counting cells equal to this OR that is more complicated than it first appears because there is no built-in function for counting with OR logic. The COUNTIFS...

[![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

### [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)

In this example, the goal is to count the number of cells in data (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. Not equal to The not equal to operator in Excel is <>. For example, with the...

[![Excel formula: Count cells that contain either x or y](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20that%20contain%20either%20x%20or%20y.png "Excel formula: Count cells that contain either x or y")](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

### [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)

In this example, the goal is to count cells in the range B5:B15 that contain either "x" or "y", where x and y are both text strings . When you count cells with "OR logic", you need to be careful not to double count. For example, if you are counting cells that contain "blue" or "green", you can't...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: SUMPRODUCT count multiple OR criteria](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/SUMPRODUCT%20count%20multiple%20OR%20criteria2.png "Excel formula: SUMPRODUCT count multiple OR criteria")](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

### [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)

In this example, the goal is to count rows where the value in column one is "A" or "B" and the value in column two is "X", "Y", or "Z". In the worksheet shown, we are using array constants to hold the values of interest, but the article also shows how to use cell references instead. In simple...

Related functions
-----------------

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/Boolean%20algebra%20in%20Excel-Play.png)](https://exceljet.net/videos/boolean-algebra-in-excel)

### [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)

In this video, we’ll look at how boolean algebra is used for AND and OR logic in formulas. In Boolean algebra, there are only two possible results for a math operation: 1 or 0, which, as we know, correspond to the logical values TRUE and FALSE. AND logic corresponds to multiplication . Anything...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count rows with multiple OR criteria](https://exceljet.net/formulas/count-rows-with-multiple-or-criteria)
    
*   [Count cells equal to this or that](https://exceljet.net/formulas/count-cells-equal-to-this-or-that)
    
*   [Count cells not equal to x or y](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y)
    
*   [Count cells that contain either x or y](https://exceljet.net/formulas/count-cells-that-contain-either-x-or-y)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [Boolean algebra in Excel](https://exceljet.net/videos/boolean-algebra-in-excel)
    

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