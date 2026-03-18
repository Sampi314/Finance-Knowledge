# Count cells not equal to x or y - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y

---

[Skip to main content](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y#main-content)

[](https://exceljet.net/formulas/count-cells-not-equal-to-x-or-y#)

*   [Previous](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Next](https://exceljet.net/formulas/count-cells-over-n-characters)
    

[Count](https://exceljet.net/formulas#Count)

Count cells not equal to x or y
===============================

by Dave Bruns · Updated 17 Aug 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells not equal to x or y](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20cells%20not%20equal%20to%20x%20or%20y_1.png "Excel formula: Count cells not equal to x or y")

Summary
-------

To count cells not equal to this or that, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 with multiple criteria. To count the number of cells that are _not equal_ to "red" or "blue", the formula in E5 is:

    =COUNTIFS(data,"<>red",data,"<>blue")
    

where **data** is the [named range](https://exceljet.net/glossary/named-range)
 B5:B15.

Generic formula
---------------

    =COUNTIFS(range,"<>x",range,"<>y")

Explanation 
------------

In this example, the goal is to count the number of cells in **data** (B5:B15) that are not equal to "red" or "blue". This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below.

### Not equal to

The not equal to [operator](https://exceljet.net/glossary/logical-operators)
 in Excel is <>. For example, with the number 10 in cell A1:

    =A1<>5 // returns TRUE
    =A1<>10 // returns FALSE
    

The first formula returns TRUE since A1 is indeed not equal to 5. The second formula returns FALSE since A1 is equal to 10.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 counts the number of cells in a range that meet one or more supplied criteria. All conditions must pass in order for a cell to be counted, so you can think of COUNTIFS as using AND logic to join conditions.

In the example shown, there is a list of colors in column B in the named range **data** (B5:B15). We want to count cells where the color is _not_ red or blue. To solve this problem, we need two separate conditions: (1) not equal to "red", and (2) not equal to "blue". The conditions given to COUNTIFS are supplied with range/criteria _pairs_, and can use [logical operators](https://exceljet.net/glossary/logical-operators)
. The key in this case is to use the "not equals" operator, which is <>. The conditions we need are:

    data,"<>red" // not equal to "red"
    data,"<>blue" // not equal to "blue"
    

When we place these conditions in COUNTIFS, the result is 4, since there are 4 cells that contain colors not equal to "red" or "blue":

    =COUNTIFS(data,"<>red",data,"<>blue") // returns 4
    

To exclude other colors, you can add additional range/criteria pairs.

### Alternative with SUMPRODUCT

The [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 can also count cells that meet multiple conditions. For the above example, the syntax for SUMPRODUCT is:

    =SUMPRODUCT((data<>"blue")*(data<>"green"))
    

This is an example of using [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 with [multiplication for OR logic](https://exceljet.net/videos/boolean-algebra-in-excel)
.

### Not equal to many things

The formulas above do scale well as you add more conditions. To count cells not equal to many things with a more streamlined formula, [see this example](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
.

Related formulas
----------------

[![Excel formula: Count cells not equal to](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to.png "Excel formula: Count cells not equal to")](https://exceljet.net/formulas/count-cells-not-equal-to)

### [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)

In this example, the goal is to count the number of cells in column D that are not equal to a given color. The simplest way to do this is with the COUNTIF function , as explained below. Not equal to In Excel, the operator for not equal to is "<>". For example: =A1<>10 // A1 is not equal...

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: Count cells equal to one of many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20equal%20to%20one%20of%20many%20things.png "Excel formula: Count cells equal to one of many things")](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

### [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)

In this example, the goal is to count the values in column B listed in the range E5:E7. One way to do this is to give the COUNTIF function all three values in the named range things (E5:E7) as criteria, then use the SUMPRODUCT function to get a total. The formula in G4 is: =SUMPRODUCT(COUNTIF(B5:...

Related functions
-----------------

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

[![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)

### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)

The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)
 or [arrays](https://exceljet.net/glossary/array)
 together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells not equal to](https://exceljet.net/formulas/count-cells-not-equal-to)
    
*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [Count cells equal to one of many things](https://exceljet.net/formulas/count-cells-equal-to-one-of-many-things)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Articles

*   [Excel's RACON functions](https://exceljet.net/articles/excels-racon-functions)
    

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