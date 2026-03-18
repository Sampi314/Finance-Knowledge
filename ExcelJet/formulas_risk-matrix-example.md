# Risk Matrix Example - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/risk-matrix-example

---

[Skip to main content](https://exceljet.net/formulas/risk-matrix-example#main-content)

[](https://exceljet.net/formulas/risk-matrix-example#)

*   [Previous](https://exceljet.net/formulas/reverse-a-list-or-range)
    
*   [Next](https://exceljet.net/formulas/score-quiz-answers-with-key)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Risk Matrix Example
===================

by Dave Bruns · Updated 27 Nov 2020

Related functions 
------------------

[INDEX](https://exceljet.net/functions/index-function)

[MATCH](https://exceljet.net/functions/match-function)

![Excel formula: Risk Matrix Example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/risk%20matrix%20example.png "Excel formula: Risk Matrix Example")

Summary
-------

To set up a simple risk matrix, you can use a formula based on INDEX and MATCH. In the example shown, the formula in J7 is:

    =INDEX(C5:G9,MATCH(impact,B5:B9,0),MATCH(certainty,C4:G4,0))
    

Where "impact" is the named range J6, and "certainty" is the named range J5

### Context

A risk matrix is used for risk assessment. One axis is used to assign the probability of a particular risk and the other axis is used to assign consequence or severity. A risk matrix can a useful to rank the potential impact of a particular event, decision, or risk.

In the example shown, the values inside the matrix are the result of multiplying certainty by impact, on a 5-point scale. This is a purely arbitrary calculation to give each cell in the table a unique value.

Generic formula
---------------

    =INDEX(matrix,MATCH(impact,range1,0),MATCH(certainty,range2,0))

Explanation 
------------

At the core, we are using the INDEX function to retrieve the value at a given row or column number like this:

    =INDEX(C5:G9,row,column)
    

The range C5:C9 defines the matrix values. What's left is to figure out the correct row and column numbers, and for that we use the MATCH function. To get a row number for INDEX (the impact), we use:

    MATCH(impact,B5:B9,0)
    

To get a column number for INDEX (the impact), we use:

    MATCH(certainty,C4:G4,0)
    

In both cases, MATCH is set up to perform an exact match. When certainty is "possible" and impact is "major" MATCH calculates row and column numbers as follows:

    =INDEX(C5:G9,4,3)
    

The INDEX function then returns the value at the fourth row and third column, 12.

For a more detailed explanation of how to use INDEX and MATCH, see [this article](https://exceljet.net/articles/index-and-match)
.

Related formulas
----------------

[![Excel formula: INDEX and MATCH exact match](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/INDEX_and_MATCH_exact_match.png "Excel formula: INDEX and MATCH exact match")](https://exceljet.net/formulas/index-and-match-exact-match)

### [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)

In this example, the goal is to look up various information about a random group of popular movies from the 1990s. The information to retrieve includes the year released, the rank against the other movies in the list, and worldwide gross sales. To retrieve this information, we are using an INDEX...

[![Excel formula: Two-way lookup with INDEX and MATCH](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/two-way%20lookup%20with%20INDEX%20and%20MATCH.png "Excel formula: Two-way lookup with INDEX and MATCH")](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

### [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)

In this example, the goal is to perform a two-way lookup, sometimes called a matrix lookup . This means we need to create a match on both rows and columns and return the value at the intersection of this two-way match The core of this formula is INDEX, which is simply retrieving a value from C6:G10...

Related functions
-----------------

[![Excel INDEX function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20index%20function.png "Excel INDEX function")](https://exceljet.net/functions/index-function)

### [INDEX Function](https://exceljet.net/functions/index-function)

The Excel INDEX function returns the value at a given location in a range or array. You can use INDEX to retrieve individual values, or entire rows and columns. The MATCH function is often used together with INDEX to provide row and column numbers....

[![Excel MATCH function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_match.png "Excel MATCH function")](https://exceljet.net/functions/match-function)

### [MATCH Function](https://exceljet.net/functions/match-function)

MATCH is an Excel function used to locate the position of a lookup value in a row, column, or table. MATCH supports approximate and exact matching, and [wildcards](https://exceljet.net/glossary/wildcard)
 (\* ?) for partial matches. Often, MATCH is combined with the...

Related videos
--------------

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20look%20things%20up%20with%20INDEX-thumb.png)](https://exceljet.net/videos/how-to-look-things-up-with-index)

### [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)

What does the INDEX function do? Unlike the MATCH function , which gets the position of an item in a list or a table, INDEX assumes you already know the position, and it gets the value of the item at that position. Let's take a look. INDEX is a powerful and flexible function that can be used for...

[![](https://exceljet.net/sites/default/files/styles/card/public/images/lesson/How%20to%20do%20a%20two-way%20lookup%20with%20INDEX%20and%20MATCH-thumb.png)](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

### [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)

In this video we'll look at how to set up a classic two-way lookup using INDEX and MATCH . Here we have a list of salespeople with monthly sales figures. What we want to do is add a formula in Q6 that looks up and retrieves a sales number based on the name and month above. To do this, we'll use the...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Formulas

*   [INDEX and MATCH exact match](https://exceljet.net/formulas/index-and-match-exact-match)
    
*   [Two-way lookup with INDEX and MATCH](https://exceljet.net/formulas/two-way-lookup-with-index-and-match)
    

### Functions

*   [INDEX Function](https://exceljet.net/functions/index-function)
    
*   [MATCH Function](https://exceljet.net/functions/match-function)
    

### Videos

*   [How to look things up with INDEX](https://exceljet.net/videos/how-to-look-things-up-with-index)
    
*   [How to do a two-way lookup with INDEX and MATCH](https://exceljet.net/videos/how-to-do-a-two-way-lookup-with-index-and-match)
    

### Articles

*   [How to use INDEX and MATCH](https://exceljet.net/articles/index-and-match)
    

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