# Count cells between dates - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/count-cells-between-dates

---

[Skip to main content](https://exceljet.net/formulas/count-cells-between-dates#main-content)

[](https://exceljet.net/formulas/count-cells-between-dates#)

*   [Previous](https://exceljet.net/formulas/count-birthdays-by-year)
    
*   [Next](https://exceljet.net/formulas/count-cells-between-two-numbers)
    

[Count](https://exceljet.net/formulas#Count)

Count cells between dates
=========================

by Dave Bruns · Updated 11 May 2022

Related functions 
------------------

[COUNTIFS](https://exceljet.net/functions/countifs-function)

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Count cells between dates](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/Count%20cells%20between%20dates_0.png "Excel formula: Count cells between dates")

Summary
-------

To count the number of cells that contain dates between two dates, you can use the [COUNTIFS function](https://exceljet.net/functions/countifs-function)
. In the example shown, G6 contains this formula:

    =COUNTIFS(date,">="&G4,date,"<="&G5)
    

where **date** is the [named range](https://exceljet.net/glossary/named-range)
 D5:D16. The result is the number of dates in D5:D16 that are between June 1, 2022 and June 15, 2022, inclusive.

Generic formula
---------------

    =COUNTIFS(range,">="&date1,range,"<="&date2)

Explanation 
------------

In this example, the goal is to count the number of cells in column D that contain dates that are between two variable dates in G4 and G5. This problem can be solved with the COUNTIFS function or the SUMPRODUCT function, as explained below. For convenience, the worksheet contains two [named ranges](https://exceljet.net/glossary/named-range)
: **date** (D5:D16) and **amount** (C5:C16). The named range **amount** is not used to count dates, but can be used to sum amounts between the same dates, as seen below.

_Note: [Excel dates are large serial numbers](https://exceljet.net/glossary/excel-date)
 so, at the core, this problem is about counting numbers that fall into a specific range. In other words, SUMIFS and SUMPRODUCT don't care about the dates, they only care about the numbers underneath the dates. If you like, you can see the numbers underneath by temporarily formatting the dates with the General [number format](https://exceljet.net/glossary/number-format)
._

### COUNTIFS function

The [COUNTIFS function](https://exceljet.net/functions/countifs-function)
 is designed to count cells that meet multiple conditions. In this case, we need to provide two conditions: (1) the date is greater than or equal to G4 and (2) the date is less than or equal to G5. COUNTIFS accepts conditions as range/criteria pairs, so the conditions are entered like this:

    date,">="&G4 // greater than or equal to G4
    date,"<="&G5 // less than or equal to G5
    

The final formula looks like this:

    =COUNTIFS(date,">="&G4,date,"<="&G5)
    

Note that the logical [operators](https://exceljet.net/glossary/logical-operators)
 ">=" and "<=" must be entered as text and surrounded by double quotes. This means we must use [concatenation](https://exceljet.net/glossary/concatenation)
 with the ampersand [operator](https://exceljet.net/glossary/math-operators)
 (&) to join the operators to the dates in cell G4 and cell G5. This syntax is specific to [a group of eight functions in Excel](https://exceljet.net/articles/excels-racon-functions)
.

### SUMPRODUCT function

This problem can also be solved with the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 which allows a cleaner syntax:

    =SUMPRODUCT((date>=G4)*(date<=G5))
    

This is an example of using [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 in Excel. Because the named range **date** contains 12 dates, each expression inside SUMPRODUCT returns an [array](https://exceljet.net/glossary/array)
 with 12 TRUE or FALSE values. When these two arrays are multiplied together, they return an array of 1s and 0s. After multiplication, we have:

    =SUMPRODUCT({0;0;1;1;1;1;0;0;0;0;0;0})
    

SUMPRODUCT then returns the sum of the elements in the array, which is 4.

### Sum amounts between dates

To sum the amounts on dates between G4 and G5 in this worksheet, you can use the [SUMIFS function](https://exceljet.net/functions/sumifs-function)
 like this:

    =SUMIFS(amount,date,">="&G4,date,"<="&G5)
    

The conditions in SUMIFS are the same as in COUNTIFS, but SUMIFS also accepts the range to sum as the first [argument](https://exceljet.net/glossary/function-argument)
. The result is $630. 

To sum the amounts for dates between G4 and G5, you can use SUMPRODUCT like this:

    =SUMPRODUCT((date>=G4)*(date<=G5)*amount)
    

Here again, the conditions are the same as the original SUMPRODUCT formula above, but we have extended the formula to multiply by **amount**. This formula simplifies to:

    =SUMPRODUCT({0;0;1;1;1;1;0;0;0;0;0;0}*{180;120;105;100;220;205;225;140;180;200;240;235})
    

The zeros in the first array effectively cancel out the amounts for dates that don't meet criteria:

    =SUMPRODUCT({0;0;105;100;220;205;0;0;0;0;0;0})
    

and SUMPRODUCT returns $630 as a final result.

Related formulas
----------------

[![Excel formula: Count between dates by age range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/count%20between%20dates%20by%20age%20range.png "Excel formula: Count between dates by age range")](https://exceljet.net/formulas/count-between-dates-by-age-range)

### [Count between dates by age range](https://exceljet.net/formulas/count-between-dates-by-age-range)

The goal of this example is to count rows in the data where the date joined falls between start and end dates (inclusive) and the age also falls into the age ranges seen in column G. The formula is complicated somewhat by the fact that the age range labels are actually text, so we need to extract a...

[![Excel formula: Count cells between two numbers](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Count%20cells%20between%20two%20numbers_0.png "Excel formula: Count cells between two numbers")](https://exceljet.net/formulas/count-cells-between-two-numbers)

### [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)

In this example, the goal is to count numbers that fall within specific ranges. The lower value comes from the "Start" column, and the upper value comes from the "End" column. For each range, we want to include both the lower value and the upper value. For convenience, the numbers being counted are...

[![Excel formula: Highlight values between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20values%20between.png "Excel formula: Highlight values between")](https://exceljet.net/formulas/highlight-values-between)

### [Highlight values between](https://exceljet.net/formulas/highlight-values-between)

When you use a formula to apply conditional formatting, the formula is evaluated for each cell in the range, relative to the active cell in the selection at the time the rule is created. So, in this case, if you apply the rule to B4:G11, with B4 as the active cell, the rule is evaluated for each of...

[![Excel formula: Highlight dates between](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/Highlight%20dates%20between.png "Excel formula: Highlight dates between")](https://exceljet.net/formulas/highlight-dates-between)

### [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)

The AND function takes multiple arguments and returns TRUE only when all arguments return TRUE. The DATE function creates a proper Excel date with given year, month, and day values. Because the reference to B4 is fully relative, it will update as the rule is applied to each cell in the range, and...

[![Excel formula: Summary count by month with COUNTIFS](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/summary%20count%20by%20month%20with%20COUNTIFS_0.png "Excel formula: Summary count by month with COUNTIFS")](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

### [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)

In this example, we have a list of 100 issues in Columns B to D. Each issue has a date and priority. We are also using the named range dates for C5:C104 and priorities for D5:D105. Starting in column F, we have a summary table that shows a total count per month, followed by a total count per month...

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

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20use%20the%20COUNTIFS%20function-thumb.png)](https://exceljet.net/videos/how-to-use-the-countifs-function)

### [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)

In this video, we'll look at how to use the COUNTIFS function to count cells that meet multiple criteria. Let's take a look. In this first set of tables, we have two named ranges , "number" and "color." In column G, I'll enter a formula that satisfies the conditions in column E. The COUNTIFS...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count between dates by age range](https://exceljet.net/formulas/count-between-dates-by-age-range)
    
*   [Count cells between two numbers](https://exceljet.net/formulas/count-cells-between-two-numbers)
    
*   [Highlight values between](https://exceljet.net/formulas/highlight-values-between)
    
*   [Highlight dates between](https://exceljet.net/formulas/highlight-dates-between)
    
*   [Summary count by month with COUNTIFS](https://exceljet.net/formulas/summary-count-by-month-with-countifs)
    

### Functions

*   [COUNTIFS Function](https://exceljet.net/functions/countifs-function)
    
*   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)
    

### Videos

*   [How to use the COUNTIFS function](https://exceljet.net/videos/how-to-use-the-countifs-function)
    

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