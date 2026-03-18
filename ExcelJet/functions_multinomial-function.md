# Excel MULTINOMIAL function | Exceljet

**Source:** https://exceljet.net/functions/multinomial-function

---

[Skip to main content](https://exceljet.net/functions/multinomial-function#main-content)

[](https://exceljet.net/functions/multinomial-function#)

*   [Previous](https://exceljet.net/functions/mround-function)
    
*   [Next](https://exceljet.net/functions/munit-function)
    

Excel 2003

[Math](https://exceljet.net/functions#Math)

MULTINOMIAL Function
====================

by Kurt Bruns · Updated 1 Jul 2025

Related functions 
------------------

[FACT](https://exceljet.net/functions/fact-function)

[COMBIN](https://exceljet.net/functions/combin-function)

[PERMUT](https://exceljet.net/functions/permut-function)

[COMBINA](https://exceljet.net/functions/combina-function)

![Excel MULTINOMIAL function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_multinomial_function_main_screenshot_cropped.png "Excel MULTINOMIAL function")

Summary
-------

The Excel MULTINOMIAL function calculates the multinomial coefficient, which is used to determine the number of ways to assign groups of items into specified sizes.

Purpose 
--------

Calculate the multinomial coefficient for a list of numbers

Return value 
-------------

The multinomial coefficient, which is a positive integer

Syntax
------

    =MULTINOMIAL(number1,[number2],...)

*   _number1_ - The first value.
*   _number2_ - \[optional\] Additional values.

Using the MULTINOMIAL function 
-------------------------------

The Excel MULTINOMIAL function calculates the multinomial coefficient, which is used to determine the number of ways to assign groups of items into specified sizes. This is especially useful in combinatorics and probability, where you need to count the distinct ways to distribute items into multiple groups, regardless of the order within each group.

### Key features

*   Returns the multinomial coefficient for a set of numbers
*   Accepts 1 to 255 arguments
*   All arguments must be non-negative numbers
*   Returns #VALUE! if any argument is non-numeric
*   Returns #NUM! if any argument is negative

### Table of contents

*   [Key features](https://exceljet.net/functions/multinomial-function#key-features)
    
*   [Example #1 - Basic usage](https://exceljet.net/functions/multinomial-function#example-1---basic-usage)
    
*   [Example #2 - Drawing marbles from a bag](https://exceljet.net/functions/multinomial-function#example-2---drawing-marbles-from-a-bag)
    
*   [Example #3 - Count possible combinations](https://exceljet.net/functions/multinomial-function#example-3---count-possible-combinations)
    
*   [Example #4 - Calculate probability](https://exceljet.net/functions/multinomial-function#example-4---calculate-probability)
    
*   [Example #5 - Errors](https://exceljet.net/functions/multinomial-function#example-5---errors)
    
*   [When to use](https://exceljet.net/functions/multinomial-function#when-to-use)
    
*   [Formula](https://exceljet.net/functions/multinomial-function#formula)
    

### Example #1 - Basic usage

The formula below calculates the multinomial coefficient for the numbers 3, 6, and 1:

    =MULTINOMIAL(3, 6, 1) // returns 840
    

This is equivalent to:

    =FACT(3+6+1)/(FACT(3)*FACT(6)*FACT(1))
    

### Example #2 - Drawing marbles from a bag

Suppose you have a bag containing 2 red marbles and 2 blue marbles. You draw all 4 marbles one by one and place them in order. We can use the MULTINOMIAL function to count the number of different sequences of colors that could be drawn.

    =MULTINOMIAL(2, 2) // returns 6
    

This counts the number of different color sequences possible when drawing 2 red and 2 blue marbles. The 6 possible sequences are:

*   Red, Red, Blue, Blue
*   Red, Blue, Red, Blue
*   Red, Blue, Blue, Red
*   Blue, Red, Red, Blue
*   Blue, Red, Blue, Red
*   Blue, Blue, Red, Red

### Example #3 - Count possible combinations

The MULTINOMIAL function is useful when you have more than two groups and want to count the number of distinct ways to distribute items into groups of specific sizes.

For example, suppose you survey 9 people about their favorite ice cream flavor, and the choices are either chocolate, vanilla, or strawberry. "How many different ways could 2 people pick chocolate, 3 pick vanilla, and 4 pick strawberry?"

We can use the MULTINOMIAL function to count the number of distinct ways to distribute the 9 people into groups of 2, 3, and 4. The formula is:

    =MULTINOMIAL(2, 3, 4) // returns 1260
    

### Example #4 - Calculate probability

The MULTINOMIAL function can also be used to calculate probabilities in multinomial distributions. Excel does not provide a dedicated function for the multinomial distribution, so we need to construct the formula manually.

Continuing from the previous example, suppose the probability that a person chooses chocolate is 0.5, vanilla is 0.35, and strawberry is 0.15. Suppose you want to know: "If you survey 9 people, what is the probability that 2 choose chocolate, 3 choose vanilla, and 4 choose strawberry?"

To start, let's calculate the probability of just one specific way to assign people to flavors: for example, the first two people pick chocolate, the next three pick vanilla, and the last four pick strawberry:

    =(0.5^2) * (0.35^3) * (0.15^4) // 7.75195E-06
    

This value is quite small, because it only accounts for one possible way the outcome could occur. In reality, there are 1260 different ways to assign 2, 3, and 4 people to the three flavors, and each assignment is equally likely. We need to count all possible assignments using the MULTINOMIAL function, and then multiply by the probability of each outcome.

    =MULTINOMIAL(2,3,4) * (0.5^2) * (0.35^3) * (0.15^4) // 0.006837223
    

This gives us the probability that, for our survey of 9 people, 2 choose chocolate, 3 choose vanilla, and 4 choose strawberry.

### Example #5 - Errors

All arguments for the MULTINOMIAL function must be numeric and non-negative. If any argument is negative, the function returns #NUM! error.

    =MULTINOMIAL(-3, 6, 1) // returns #NUM!
    

If any argument is non-numeric, the function returns #VALUE! error.

    =MULTINOMIAL(3, "a", 1) // returns #VALUE!
    

### When to use

Excel offers several functions for combinatorics and probability. For example, COMBIN and PERMUT can be used for specific types of counting problems involving two groups.

*   [COMBIN](https://exceljet.net/functions/combin-function)
     is used for counting combinations of items where order does not matter.
*   [PERMUT](https://exceljet.net/functions/permut-function)
     is used for counting permutations of items where order does matter.

The MULTINOMIAL function is more general and is used when you have more than two groups and want to count the number of distinct ways to distribute items into groups of specific sizes, when the order within each group does not matter.

The multinomial coefficient is closely related to the multinomial distribution, which describes the probabilities of counts for more than two possible outcomes (generalizing the binomial distribution). However, Excel does not provide a dedicated function for the multinomial distribution. If you need to calculate multinomial probabilities, you will need to construct the formula manually using the MULTINOMIAL function together with probability terms.

### Formula

The MULTINOMIAL function calculates the multinomial coefficient, which is the ratio of the factorial of the sum of the arguments to the product of the factorials of each argument. The formula is:

![Excel multinomial function formula](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/MultinomialFunctionFormula.png "Excel multinomial function formula")

Related functions
-----------------

[![Excel FACT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_fact.png "Excel FACT function")](https://exceljet.net/functions/fact-function)

### [FACT Function](https://exceljet.net/functions/fact-function)

The Excel FACT function returns the factorial of a given number. For example, =FACT(3) returns 6, equivalent to 3 x 2 x 1.

[![Excel COMBIN function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20combin.png "Excel COMBIN function")](https://exceljet.net/functions/combin-function)

### [COMBIN Function](https://exceljet.net/functions/combin-function)

The Excel COMBIN function returns the number of combinations for a given number of items. The COMBIN function _does not_ allow repetitions. To count combinations that _allow_ repetitions, use the [COMBINA function](https://exceljet.net/functions/combina-function)
.

[![Excel PERMUT function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20permut.png "Excel PERMUT function")](https://exceljet.net/functions/permut-function)

### [PERMUT Function](https://exceljet.net/functions/permut-function)

The Excel PERMUT function returns the number of permutations (combinations where order is significant) for a given number of items. The PERMUT function _does not_ allow repetitions. To allow permutations with repetitions, use the [PERMUTATIONA](https://exceljet.net/functions/permutationa-function)
...

[![Excel COMBINA function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20combina.png "Excel COMBINA function")](https://exceljet.net/functions/combina-function)

### [COMBINA Function](https://exceljet.net/functions/combina-function)

The Excel COMBINA function returns the number of combinations with repetitions _allowed_. To count combinations that _do not_ allow repetitions, use the [COMBIN function](https://exceljet.net/functions/combin-function)
.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [FACT Function](https://exceljet.net/functions/fact-function)
    
*   [COMBIN Function](https://exceljet.net/functions/combin-function)
    
*   [PERMUT Function](https://exceljet.net/functions/permut-function)
    
*   [COMBINA Function](https://exceljet.net/functions/combina-function)
    

### Links

*   [Microsoft MULTINOMIAL function documentation](https://support.office.com/en-us/article/multinomial-function-6fa6373c-6533-41a2-a45e-a56db1db1bf6)
    
*   [Multinomial distribution (Wikipedia)](https://en.wikipedia.org/wiki/Multinomial_distribution)
    

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