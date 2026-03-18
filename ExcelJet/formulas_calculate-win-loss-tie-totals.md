# Calculate win loss tie totals - Excel formula | Exceljet

**Source:** https://exceljet.net/formulas/calculate-win-loss-tie-totals

---

[Skip to main content](https://exceljet.net/formulas/calculate-win-loss-tie-totals#main-content)

[](https://exceljet.net/formulas/calculate-win-loss-tie-totals#)

*   [Previous](https://exceljet.net/formulas/calculate-a-ratio-from-two-numbers)
    
*   [Next](https://exceljet.net/formulas/cap-percentage-at-100)
    

[Miscellaneous](https://exceljet.net/formulas#Miscellaneous)

Calculate win loss tie totals
=============================

by Dave Bruns · Updated 14 Sep 2022

Related functions 
------------------

[SUMPRODUCT](https://exceljet.net/functions/sumproduct-function)

![Excel formula: Calculate win loss tie totals](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/formulas/calculate%20win%20loss%20tie%20totals.png "Excel formula: Calculate win loss tie totals")

Summary
-------

To calculate win, loss, and tie totals for a team using game data that includes a score for both teams, you can use a formula based on the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
. In the example shown, the formula in H5, copied down, is:

    =SUMPRODUCT(((team1=$G5)*(score1>score2))+((team2=$G5)*(score2>score1)))
    

This formula returns total wins for the "Red" team based on the data shown, and uses these [named ranges](https://exceljet.net/glossary/named-range)
: **team1** (B5:B14), **team2** (C5:C14), **score1** (D5:D14), and **score2** (E5:E14).

Explanation 
------------

The goal in this example is to calculate total wins, losses, and ties for each team listed in column G. The problem is complicated somewhat by the fact that a team can appear in _either_ column B or C, so we need to take this into account when calculating wins and losses. For convenience and readability only, the formula uses the following [named ranges](https://exceljet.net/glossary/named-range)
: **team1** (B5:B14), **team2** (C5:C14), **score1** (D5:D14), and **score2** (E5:E14).

In solving this problem, you might think of using the [COUNTIF](https://exceljet.net/functions/countif-function)
 or [COUNTIFS function](https://exceljet.net/functions/countifs-function)
, but these functions are [limited to working with existing ranges for criteria](https://exceljet.net/articles/excels-racon-functions)
. Instead, the formula in the example uses the [SUMPRODUCT function](https://exceljet.net/functions/sumproduct-function)
 to sum the result of an array expression based on [Boolean logic](https://exceljet.net/glossary/boolean-logic)
. Inside SUMPRODUCT on the left we have an expression to count wins when a team appears in column B:

    ((team1=$G5)*(score1>score2))
    

If we replace the [mixed reference](https://exceljet.net/glossary/mixed-reference)
 $G5 with the value in G5, we have:

    ((team1="Red")*(score1>score2))
    

This expression is actually formed from two expressions, joined by [multiplication (\*) to create AND logic](https://exceljet.net/videos/array-formulas-with-and-and-or-logic)
. The expression on the left checks if **team1** is "Red":

    (team1="Red") // check team is "Red"
    

The expression on the right checks if **score1** is greater than **score2**:

    (score1>score2) // check score1 greater than score2
    

Because both expressions involve ranges with multiple values, they each return [arrays](https://exceljet.net/glossary/array)
 that contain multiple results. Rewriting the formula with the arrays returned, we have:

    ({TRUE;TRUE;TRUE;TRUE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE} *
    {FALSE;FALSE;TRUE;FALSE;FALSE;TRUE;FALSE;TRUE;TRUE;FALSE})
    

The math operation of multiplication (\*) works like AND in [Boolean algebra](https://exceljet.net/glossary/boolean-logic)
 and also coerces the TRUE and FALSE values into 1s and 0s. When corresponding values are both TRUE, the result is 1. In any other case, the result is 0. The result is a single array like this:

    {0;0;1;0;0;0;0;0;0;0}
    

Note the third value is 1, which corresponds to game 3, where Red beats Black 3-2. At this point, we have collected an array that represents all Red victories when Red is **Team1**. This covers the left side of the logic inside SUMPRODUCT.

On the right side, we have similar logic that checks for Red wins when Read is **Team2**:

    ((team2=$G5)*(score2>score1))
    

This logic evaluates in the same way as the left logic. Summarized, we have:

    ((team2="Red")*(score2>score1))
    

Then:

    ({FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE;FALSE})*({FALSE;TRUE;FALSE;TRUE;TRUE;FALSE;TRUE;FALSE;FALSE;TRUE})
    

Then:

    ({0;0;0;0;0;0;0;0;0;0})
    

Since Red doesn't actually appear as **Team2** in any game, all results are zero.

With both the left and right sides evaluated, we can now rewrite the original formula like this:

    =SUMPRODUCT(({0;0;1;0;0;0;0;0;0;0})+({0;0;0;0;0;0;0;0;0;0}))
    

At this point notice the math operator between the two arrays is addition (+), which [corresponds to OR logic](https://exceljet.net/videos/boolean-algebra-in-excel)
. We do this because we are counting Red wins as **Team1** OR **Team2**. The result is a single array inside SUMPRODUCT:

    =SUMPRODUCT({0;0;1;0;0;0;0;0;0;0})
    

With just one array to process, SUMPRODUCT sums the items in the array and returns a final result, 1.

For comparison, if we solve for the Green team in cell H7, we get 4:

    =SUMPRODUCT(((team1=$G7)*(score1>score2))+((team2=$G7)*(score2>score1)))
    

Then:

    =SUMPRODUCT(({0;0;0;0;0;0;0;1;1;0})+({0;1;0;0;1;0;0;0;0;0}))
    

Then:

    =SUMPRODUCT({0;1;0;0;1;0;0;1;1;0}) // returns 4
    

### Counting losses

The formula in I5 to count losses is very similar:

    =SUMPRODUCT(((team1=$G5)*(score1<score2))+((team2=$G5)*(score2

`   The only difference is the "reversed" logic in checking scores.  ### Counting ties  The formula to count follows the same pattern, the only difference is we check for equal scores:      =SUMPRODUCT(((team1=$G5)*(score1=score2))+((team2=$G5)*(score2=score1)))       One problem with this formula is that games without scores are counted as ties. This happens because Excel evaluates empty cells as zero, so when **score1** and **score2** are empty, they appear to the formula as zero, which counts like a 0-0 tie. To work around this problem, you can add a second array to SUMPRODUCT to check for ties with logic based on the [LEN function](https://exceljet.net/functions/len-function) :      (LEN(score1)>0)*(LEN(score2)>0) // check for no score       When both **score1** and **score2** have values, the result is 1. When either score is empty, the result is zero, and this zero "cancels out" the false tie that occurs when both cells are empty. The complete formula is:      =SUMPRODUCT(     ((team1=$G5)*(score1=score2))+     ((team2=$G5)*(score2=score1)),     (LEN(score1)>0)*(LEN(score2)>0)     )       The LEN function is checking for any characters. When LEN returns zero, it means a cell is empty.   `

`   Related formulas ----------------  [![Excel formula: Longest winning streak](https://exceljet.net/sites/default/files/styles/card/public/images/formulas/longest_winning_streak.png "Excel formula: Longest winning streak")](https://exceljet.net/formulas/longest-winning-streak)  ### [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)  In this example, the goal is to calculate a count for the longest winning streak in a set of data. In the worksheet shown, wins ("W") and losses ("L") are recorded in column C, so this means we want to count the longest consecutive series of W's. Although we are specifically counting the longest...  Related functions -----------------  [![Excel SUMPRODUCT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20sumproduct%20function.png "Excel SUMPRODUCT function")](https://exceljet.net/functions/sumproduct-function)  ### [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)  The Excel SUMPRODUCT function multiplies [ranges](https://exceljet.net/glossary/range)  or [arrays](https://exceljet.net/glossary/array)  together and returns the sum of products. This sounds boring, but SUMPRODUCT is an incredibly versatile function that can be used to count and sum like COUNTIFS or SUMIFS,...                 `

`   Was this page helpful? Yes No Report a problem  Cancel Submit  ![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)  Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)  ### Dave Bruns  Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.  Related Information -------------------  ### Formulas  *   [Longest winning streak](https://exceljet.net/formulas/longest-winning-streak)       ### Functions  *   [SUMPRODUCT Function](https://exceljet.net/functions/sumproduct-function)                  `

`   Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!  Thierry  [More Testimonials](https://exceljet.net/feedback)  Get [Training](https://exceljet.net/training)  ----------------------------------------------  ### Quick, clean, and to the point training  Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.  [View Paid Training & Bundles](https://exceljet.net/training)  [![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)  [![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)  [![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)  [![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)  [![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)  [![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)                  `