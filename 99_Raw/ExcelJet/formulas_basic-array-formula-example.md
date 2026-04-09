# Basic array formula example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/basic-array-formula-example

---

[Skip to main content](https://exceljet.net/formulas/basic-array-formula-example#main-content)

[](https://exceljet.net/formulas/basic-array-formula-example#)

*   [Previous](https://exceljet.net/formulas/all-dates-in-chronological-order)
    
*   [Next](https://exceljet.net/formulas/basic-attendance-tracking-formula)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Basic array formula example
===========================

by Dave Bruns · Updated 12 May 2024

Related functions 
------------------

[MAX](https://exceljet.net/functions/max-function)

[MIN](https://exceljet.net/functions/min-function)

![Excel formula: Basic array formula example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/basic%20array%20formula%20example.png "Excel formula: Basic array formula example")

Summary
-------

To calculate the max or min change in a set of data as shown, without using a helper column, you can use an array formula. In the example, the formula in G6 is:

    {=MAX(C5:C12-D5:D12)}
    

_Note: this is an [array formula](https://exceljet.net/glossary/array-formula)
 and must be entered with control + shift + enter in Excel 2019 and earlier. In Excel 2021 or later, [array formulas just work](https://exceljet.net/articles/dynamic-array-formulas-in-excel)
._

Generic formula
---------------

    {=MAX(rng1-rng2)}

Explanation 
------------

The example on this page shows a simple array formula. Working from the inside out, the expression:

    C5:C12-D5:D12
    

Results in an array containing seven values:

    {17;19;32;25;12;26;29;22}
    

Each number in the array is the result of subtracting the "low" from the "high" in each of the seven rows of data. This array is returned to the MAX function:

    =MAX({17;19;32;25;12;26;29;22})
    

And MAX returns the maximum value in the array, which is 32.

### MIN change

To return the minimum change in the data, you can substitute the MIN function for the MAX function:

    {=MIN(C5:C12-D5:D12)}
    

As before, this is an array formula and must be entered with control + shift + enter.

### More on array formulas

To understand array formulas, you must learn to investigate the results of various operations inside a formula as it is being evaluated by Excel. In particular, you need to know how to use the F9 key to debug a formula and how to use the Evaluate Feature in Excel. See the video links below for a quick demo.

Related formulas
----------------

[![Excel formula: Count total characters in a range](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/exceljet_count_characters_in_cell.png "Excel formula: Count total characters in a range")](https://exceljet.net/formulas/count-total-characters-in-a-range)

### [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)

SUMPRODUCT accepts the range B3:B6 as an array of four cells. For each cell in the array, LEN calculates the length of the text as a number. The result is an array that contains 4 numbers. SUMPRODUCT then sums the items in this array and returns the total.

Related functions
-----------------

[![Excel MAX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20max%20function.png "Excel MAX function")](https://exceljet.net/functions/max-function)

### [MAX Function](https://exceljet.net/functions/max-function)

The Excel MAX function returns the largest numeric value in the data provided. MAX ignores empty cells, the logical values TRUE and FALSE, and text values.

[![Excel MIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20min%20function.png "Excel MIN function")](https://exceljet.net/functions/min-function)

### [MIN Function](https://exceljet.net/functions/min-function)

The Excel MIN function returns the smallest numeric value in the data provided. The MIN function ignores empty cells, the logical values TRUE and FALSE, and text values.

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20check%20and%20debug%20a%20formula%20with%20F9.png)](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

### [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)

One thing you'll frequently do in Excel is check or debug formulas. In this video, we'll look at how to use the F9 key to quickly break a formula down into pieces that you can understand. Here we have a simple list of names. In addition to names, we have a column for birthdate, a column for age,...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20step%20through%20complex%20formulas%20using%20evaluate-thumb.png)](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

### [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)

Excel has a handy feature called Evaluate Formula, which solves a formula one step at a time. Each time you click the Evaluate button, Excel will solve the underlined part of the formula and show you the result. Here's the same worksheet we looked at in a previous video when we talked about...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20is%20an%20array%20formula%3F-play.png)](https://exceljet.net/videos/what-is-an-array-formula)

### [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)

In this video, we'll answer the question: What is an array formula? In the world of Excel formulas, the term "array formula" is probably responsible for more confusion than just about any other concept. This is because the definition of an array formula has become mixed up with the requirement to...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/What%20are%20dynamic%20array%20formulas-Play.png)](https://exceljet.net/videos/what-are-dynamic-array-formulas)

### [What are Dynamic Array formulas?](https://exceljet.net/videos/what-are-dynamic-array-formulas)

In this video, I'll explain the basic idea of dynamic array formulas. Dynamic Array formulas are the biggest change to the Excel formula engine in years. Maybe the biggest change ever. This is because Dynamic Arrays make it easy to work with many values at the same time. For many users, this will...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [Count total characters in a range](https://exceljet.net/formulas/count-total-characters-in-a-range)
    

### Functions

*   [MAX Function](https://exceljet.net/functions/max-function)
    
*   [MIN Function](https://exceljet.net/functions/min-function)
    

### Videos

*   [How to check and debug a formula with F9](https://exceljet.net/videos/how-to-check-and-debug-a-formula-with-f9)
    
*   [How to step through complex formulas using Evaluate](https://exceljet.net/videos/how-to-step-through-complex-formulas-using-evaluate)
    
*   [What is an array formula?](https://exceljet.net/videos/what-is-an-array-formula)
    
*   [What are Dynamic Array formulas?](https://exceljet.net/videos/what-are-dynamic-array-formulas)
    

### Articles

*   [How to use formula criteria (50 examples)](https://exceljet.net/articles/how-to-use-formula-criteria)
    

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