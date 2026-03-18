# Score quiz answers with key - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/score-quiz-answers-with-key

---

[Skip to main content](https://exceljet.net/formulas/score-quiz-answers-with-key#main-content)

[](https://exceljet.net/formulas/score-quiz-answers-with-key#)

*   [Previous](https://exceljet.net/formulas/risk-matrix-example)
    
*   [Next](https://exceljet.net/formulas/search-entire-worksheet-for-value)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Score quiz answers with key
===========================

by Dave Bruns · Updated 2 Aug 2022

Related functions 
------------------

[SUM](https://exceljet.net/functions/sum-function)

[COUNTA](https://exceljet.net/functions/counta-function)

![Excel formula: Score quiz answers with key](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/score%20quiz%20answers%20with%20key.png "Excel formula: Score quiz answers with key")

Summary
-------

To score a quiz and count correct and incorrect answers based on an answer key, you can use a basic array formula. In the example shown, the formula in I7, copied down, is:

    =SUM(--(C7:G7=key))
    

where **key** is the [named range](https://exceljet.net/glossary/named-range)
 C4:G4.

_Note: This is an [array formula](https://exceljet.net/glossary/array-formula)
. In Excel 365, enter normally. In older versions of Excel, you must enter with control + shift + enter._

Generic formula
---------------

    =SUM(--(answers=key))

Explanation 
------------

This formula uses the named range **key** (C4:G4) for convenience only. Without the named range, you'll want to use an absolute reference so the formula can be copied.

In cell I7, we have this formula:

    =SUM(--(C7:G7=key))
    

working from the inside-out, this expression is evaluated first:

    C7:G7=key // compare answers to key
    

The result is an [array](https://exceljet.net/glossary/array)
 of TRUE FALSE values like this:

    {TRUE,TRUE,TRUE,FALSE,TRUE}
    

TRUE values indicate a correct answer, FALSE values indicate an incorrect answer.

To coerce the TRUE and FALSE values to numbers, we use a [double negative](https://exceljet.net/glossary/double-unary)
:

    --({TRUE,TRUE,TRUE,FALSE,TRUE}) // get 1's and 0's
    

The is an array of 1's and 0's delivered directly to the SUM function:

    =SUM({1,1,1,0,1}) // sum correct
    

The SUM function then returns the final result, 4.

### Incorrect answers

The formula in J7 counts incorrect answers in almost the same way:

    =SUM(--(C7:G7<>key))
    

The only difference is that we are now using the not equal to (<>) logical operator:

    =SUM(--(C7:G7<>key))
    =SUM(--({FALSE,FALSE,FALSE,TRUE,FALSE}))
    =SUM({0,0,0,1,0})
    =1
    

### Percent correct

The formula in K7 calculates the percentage of correct answers like this:

    =I7/COUNTA(key) // divide correct by total
    

Cell I7 already contains the count of correct answers. This is divided by the total count of quiz answers, which is calculated with the COUNTA function:

    COUNTA(key) // count total
    

The result is formatted with the percentage [number format](https://exceljet.net/articles/custom-number-formats)
.

Related formulas
----------------

[![Excel formula: VLOOKUP calculate grades](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/VLOOKUP_calculate_grades.png "Excel formula: VLOOKUP calculate grades")](https://exceljet.net/formulas/vlookup-calculate-grades)

### [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)

In this example, the goal is to calculate the correct grade for each name in column B using the score in column C and the table in F5:G9 as a "key" to assign grades. For convenience only, the range F5:G9 has been named key . This is a classic "approximate-match" lookup problem because it is not...

[![Excel formula: Must pass 4 out of 6 subjects](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/must_pass_4_out_of_6_subjects.png "Excel formula: Must pass 4 out of 6 subjects")](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)

### [Must pass 4 out of 6 subjects](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)

In this example, the goal is to create a formula that will return "Pass" or "Fail" depending on whether a student has a passing score in at least 4 out of 6 subjects. This problem can be easily solved with a formula based on the COUNTIF function together with the IF function in a formula like this...

Related functions
-----------------

[![Excel SUM function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sum%20function.png "Excel SUM function")](https://exceljet.net/functions/sum-function)

### [SUM Function](https://exceljet.net/functions/sum-function)

The Excel SUM function returns the sum of values supplied. These values can be numbers, cell references, ranges, arrays, and constants, in any combination. SUM can handle up to 255 individual arguments.

[![Excel COUNTA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20counta%20function.png "Excel COUNTA function")](https://exceljet.net/functions/counta-function)

### [COUNTA Function](https://exceljet.net/functions/counta-function)

The Excel COUNTA function returns the count of cells that contain numbers, text, logical values, error values, and empty text (""). COUNTA does not count empty cells.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [VLOOKUP calculate grades](https://exceljet.net/formulas/vlookup-calculate-grades)
    
*   [Must pass 4 out of 6 subjects](https://exceljet.net/formulas/must-pass-4-out-of-6-subjects)
    

### Functions

*   [SUM Function](https://exceljet.net/functions/sum-function)
    
*   [COUNTA Function](https://exceljet.net/functions/counta-function)
    

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