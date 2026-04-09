# Count not equal to multiple criteria - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-not-equal-to-multiple-criteria

---

[Skip to main content](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria#main-content)

[](https://exceljet.net/formulas/count-not-equal-to-multiple-criteria#)

*   [Previous](https://exceljet.net/formulas/count-non-blank-cells-by-category)
    
*   [Next](https://exceljet.net/formulas/count-numbers-by-nth-digit)
    

[Count](https://exceljet.net/formulas#Count)

Count not equal to multiple criteria
====================================

by Dave Bruns · Updated 13 May 2024

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

[ISNA](https://exceljet.net/functions/isna-function)

[MATCH](https://exceljet.net/functions/match-function)

[COUNTIFS](https://exceljet.net/functions/countifs-function)

![Excel formula: Count not equal to multiple criteria](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/count%20not%20equal%20to%20multiple%20criteria.png "Excel formula: Count not equal to multiple criteria")

Summary
-------

To count rows not equal to multiple criteria, you can use the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 together with the [MATCH](https://exceljet.net/functions/match-function)
 and [ISNA](https://exceljet.net/functions/isna-function)
 functions. In the example shown, the formula in G6 is:

    =SUMPRODUCT((data[Gender]="Male")*ISNA(MATCH(data[Group],{"A","B"},0)))
    

Where **data** is an [Excel Table](https://exceljet.net/glossary/excel-table)
 in the range B5:D15. The result is 2 since two males are not in Group A or B.

_Note: You can also solve this problem with the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, as explained below. The SUMPRODUCT formula is more advanced, but it scales better when there are many exclusions._

Generic formula
---------------

    =SUMPRODUCT((range=criteria)*ISNA(MATCH(range,criteria,0)))

Explanation 
------------

In this example, the goal is to count rows in a set of data using multiple criteria and "not equals to" logic. Specifically, we want to count males that are not in group A or B. All data is in an [Excel Table](https://exceljet.net/articles/excel-tables)
 named **data** in the range B5:D15. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function. Both approaches are explained below.

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 returns the count of cells that meet one or more criteria, and supports [logical operators](https://exceljet.net/glossary/logical-operators)
 (>,<,<>,=) and [wildcards](https://exceljet.net/glossary/wildcard)
 (\*,?) for partial matching. Conditions are supplied to COUNTIFS in the form of _range/criteria_ pairs — each pair contains one range and the associated criteria for that range:

    =COUNTIFS(range1,criteria1,range2,criteria2,etc)
    

In this case, the first condition is that Gender is Male:

    =COUNTIFS(data[Gender],"Male") // returns 6
    

The result is 6, since there are six Males in the table. Next, we need to exclude group "A":

    =COUNTIFS(data[Gender],"Male",data[Group],"<>A")
    

This formula returns 5. Notice we use the not equal to [operator](https://exceljet.net/glossary/logical-operators)
 (<>) enclosed in double quotes. Finally, we need to exclude group B with another _range/criteria_ pair:

    =COUNTIFS(data[Gender],"Male",data[Group],"<>A",data[Group],"<>B")
    

Notice the syntax to exclude group B is the same and both conditions use the same range. This formula returns 2. The COUNTIFS function joins all criteria with AND logic, so it works well to exclude A and B in this case. As more exclusions are added however, the syntax gets more cumbersome, because each new exclusion requires another _range/criteria_ pair. The SUMPRODUCT option below scales more easily.

### SUMPRODUCT function

Another way to solve this problem is with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 and [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. To start off, we can count males like this:

    =SUMPRODUCT(--(data[Gender]="Male")) // returns 6
    

Working from the inside out, this expression tests all values in the Gender column for "Male":

    data[Gender]="Male"
    

Since there are 11 cells in the column, the result is an [array](https://exceljet.net/glossary/array)
 with 11 TRUE and FALSE values:

    {TRUE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;TRUE;FALSE}
    

Each TRUE represents a "Male" in the Gender column. SUMPRODUCT will ignore TRUE and FALSE values by default, so we need to convert these TRUE and FALSE values to their numeric equivalents, 1 and 0. A simple way to do this is with a [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--):

    --(data[Gender]="Male")
    

The result from this snippet is an array like this:

    {1;0;1;0;1;1;0;1;0;1;0}
    

Notice the TRUE values are now 1s. This array is delivered to SUMPRODUCT, which returns 6:

    =SUMPRODUCT({1;0;1;0;1;1;0;1;0;1;0}) // returns 6
    

Next, we need to exclude groups "A" and "B". A good way to do this is with the [MATCH function](https://exceljet.net/functions/match-function)
 together with the [ISNA function](https://exceljet.net/functions/isna-function)
 like this:

    ISNA(MATCH(data[Group],{"A","B"},0))
    

Notice the configuration of MATCH is "reversed". The _lookup\_value_ is given as **data\[Group\]**, and the _lookup\_array_ is given as the [array constant](https://exceljet.net/glossary/array-constant)
 {"A","B"}. We do it this way to keep the rows in the output array consistent with the table. The result from MATCH is an array like this:

    {1;2;#N/A;1;2;#N/A;1;2;1;2;#N/A}
    

This [array](https://exceljet.net/glossary/array)
 has 11 rows, like the **data** table. The numbers indicated rows where group "A" or "B" were found. The #N/A errors indicate rows where group "A" or "B" were not found. To convert this array into something we can use, we use the ISNA function:

    ISNA(MATCH(data[Group],{"A","B"},0))
    

The result from ISNA is an array of TRUE and FALSE values like this:

    {FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;FALSE;FALSE;FALSE;TRUE}
    

ISNA returns TRUE only for the #N/A errors, so the TRUE values in this array indicate rows where the group was _not_ "A" or "B". If we wanted to use this expression in SUMPRODUCT by itself, we would use a formula like this:

    =SUMPRODUCT(--ISNA(MATCH(data[Group],{"A","B"},0)))
    

The [double negative](https://exceljet.net/articles/the-double-negative-in-excel-formulas)
 (--) again converts TRUE and FALSE values, and the result looks like this:

    =SUMPRODUCT({0;0;1;0;0;1;0;0;0;0;1}) // returns 3
    

The result is 3, since there are 3 records not in group A or B.

### Putting it all together

The next step is to put both tests above together inside SUMPRODUCT like this:

    =SUMPRODUCT((data[Gender]="Male")*ISNA(MATCH(data[Group],{"A","B"},0)))
    

Notice we use multiplication (\*) to join the two expressions. We do this because multiplication corresponds to AND logic in [Boolean algebra](https://exceljet.net/videos/boolean-algebra-in-excel)
. Also notice that we no longer need the double negative (--). This is because the math operation of multiplication automatically converts the TRUE and FALSE values to 1s and 0s. The formula evaluates like this:

    =SUMPRODUCT({1;0;1;0;1;1;0;1;0;1;0}*{0;0;1;0;0;1;0;0;0;0;1})
    =SUMPRODUCT({0;0;1;0;0;1;0;0;0;0;0})
    =2
    

The final result is 2 since two males are not in Group A or B.

_Note: In Excel 365 and Excel 2021 you can use the [SUM function](https://exceljet.net/functions/sum-function)
 instead of SUMPRODUCT if you prefer. [This article provides more detail](https://exceljet.net/articles/why-sumproduct)
._

Related formulas
----------------

[![Excel formula: Count cells not equal to many things](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20cells%20not%20equal%20to%20many.png "Excel formula: Count cells not equal to many things")](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

### [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)

First, a little context. Normally, if you have just a couple things you don't want to count, you can use COUNTIFS like this: =COUNTIFS(range,"<>apple",range,"<>orange") But this doesn't scale very well if you have a list of many things, because you'll have to add an additional range/...

[![Excel formula: COUNTIFS with multiple criteria and OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/COUNTIFS%20with%20multiple%20criteria%20and%20OR%20logic.png "Excel formula: COUNTIFS with multiple criteria and OR logic")](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

### [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)

In this example, the goal is to use the COUNTIFS function to count data with "OR logic". The challenge is the COUNTIFS function applies AND logic by default. COUNTIFS function The COUNTIFS function returns the count of cells that meet one or more criteria, and supports logical operators (>,...

[![Excel formula: Count rows with OR logic](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20rows%20with%20OR%20logic.png "Excel formula: Count rows with OR logic")](https://exceljet.net/formulas/count-rows-with-or-logic)

### [Count rows with OR logic](https://exceljet.net/formulas/count-rows-with-or-logic)

One of the trickier problems in Excel is to count rows in a set of data with "OR logic". There are two basic scenarios: (1) you want to count rows where a value in a column is "x" OR "y" (2) you want to count rows where a value, "x", exists in one column OR another. In this example, the goal is to...

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

[![Excel ISNA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20isna%20function.png "Excel ISNA function")](https://exceljet.net/functions/isna-function)

### [ISNA Function](https://exceljet.net/functions/isna-function)

The Excel ISNA function returns TRUE when a cell contains the #N/A error and FALSE for any other value, or any other error type. You can use the ISNA function with the IF function test for #N/A and display a friendly message if the error occurs.

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

[![Excel COUNTIFS function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_countifs_function.png "Excel COUNTIFS function")](https://exceljet.net/functions/countifs-function)

### [COUNTIFS Function](https://exceljet.net/functions/countifs-function)

The Excel COUNTIFS function returns the count of cells in a range that meet one or more conditions. Each condition is provided with a separate _range_ and _criteria_, and all conditions must be TRUE for a cell to be included in the count. COUNTIF can be used to count cells...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count cells not equal to many things](https://exceljet.net/formulas/count-cells-not-equal-to-many-things)
    
*   [COUNTIFS with multiple criteria and OR logic](https://exceljet.net/formulas/countifs-with-multiple-criteria-and-or-logic)
    
*   [Count rows with OR logic](https://exceljet.net/formulas/count-rows-with-or-logic)
    
*   [SUMPRODUCT count multiple OR criteria](https://exceljet.net/formulas/sumproduct-count-multiple-or-criteria)
    

### Functions

*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    
*   [ISNA Function](https://exceljet.net/functions/isna-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    
*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    

### Links

*   [Stackoverflow answer by Barry Houdini](http://stackoverflow.com/a/20859526/4071990)
    

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