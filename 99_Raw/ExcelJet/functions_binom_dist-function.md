# Excel BINOM.DIST function | Exceljet

**Source:** https://exceljet.net/functions/binom.dist-function

---

[Skip to main content](https://exceljet.net/functions/binom.dist-function#main-content)

[](https://exceljet.net/functions/binom.dist-function#)

*   [Previous](https://exceljet.net/functions/averageifs-function)
    
*   [Next](https://exceljet.net/functions/binomdist-function)
    

Excel 2010

[Statistical](https://exceljet.net/functions#Statistical)

BINOM.DIST Function
===================

by Dave Bruns · Updated 22 Sep 2021

Related functions 
------------------

[BINOM.DIST](https://exceljet.net/functions/binom.dist-function)

![Excel BINOM.DIST function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet%20binom.dist%20function.png "Excel BINOM.DIST function")

Summary
-------

The Excel BINOM.DIST function returns the individual term binomial distribution probability. You can use BINOM.DIST to calculate probabilities that an event will occur a certain number of times in a given number of trials.

Purpose 
--------

Get binomial distribution probability

Return value 
-------------

Calculated probability

Syntax
------

    =BINOM.DIST(number_s,trials,probability_s,cumulative)

*   _number\_s_ - The number of successes.
*   _trials_ - The number of independent trials.
*   _probability\_s_ - The probability of success on each trial.
*   _cumulative_ - TRUE = cumulative distribution function, FALSE=probability mass function.

Using the BINOM.DIST function 
------------------------------

The BINOM.DIST function returns the individual term binomial distribution probability. You can use BINOM.DIST to calculate probabilities that an event will occur a certain number of times in a given number of trials. BINOM.DIST returns probability as a decimal number between 0 and 1.

Binary data occurs when an observation can be placed into only two categories. For example, when tossing a coin, the result can only be heads or tails. Or, when rolling a die, the result can either be 6 or not 6.

### Example

In the example shown, the BINOM.DIST function is used to calculate the probability of rolling a 6 with a die. Since a die has six sides, the probability of rolling a 6 is 1/6, or 0.1667. Column B holds the number of trials, and the formula in C5, copied down, is:

    =BINOM.DIST(B5,10,0.1667,TRUE) // returns 0.1614
    

which returns the probability of rolling zero 6s in 10 trials, about 16%. The probability of rolling one 6 in 10 trials is about 32%.

The formula in D5 is the same, except the _cumulative_ argument has been set to TRUE. This causes BINOM.DIST to calculate the probability that there are "at most" X successes in a given number of trials. The formula in D5, copied down, is:

    =BINOM.DIST(B5,10,0.1667,TRUE) // returns 0.1614
    

In cell D5, the result is the same as C5 because the probability of rolling at most zero 6s is the same as the probability of rolling zero 6s. In cell D8, the result is 0.9302, which means the probability of rolling at most three 6s in 10 rolls is about 93%.

### Notes

*   BINOM.DIST returns probability as a decimal number between 0 and 1.
*   _Number\_s_ should be an integer, and will be truncated to an integer if not.
*   _Trials_ should be an integer, and will be truncated to an integer if not.
*   If _number\_s, trials, or probability\_s_ are not numbers, BINOM.DIST returns a #VALUE! error.
*   If _number\_s_ < 0 or _number\_s_ \> _trials_, BINOM.DIST returns a #NUM! error.
*   If _probability\_s_ < 0 or _probability\_s_ > 1, BINOM.DIST returns a #NUM! error value.

Related functions
-----------------

[![Excel BINOM.DIST function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet%20binom.dist%20function.png "Excel BINOM.DIST function")](https://exceljet.net/functions/binom.dist-function)

### [BINOM.DIST Function](https://exceljet.net/functions/binom.dist-function)

The Excel BINOM.DIST function returns the individual term binomial distribution probability. You can use BINOM.DIST to calculate probabilities that an event will occur a certain number of times in a given number of trials.

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [BINOM.DIST Function](https://exceljet.net/functions/binom.dist-function)
    

### Links

*   [Microsoft BINOM.DIST function documentation](https://support.office.com/en-us/article/binom-dist-function-c5ae37b6-f39c-4be2-94c2-509a1480770c)
    

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