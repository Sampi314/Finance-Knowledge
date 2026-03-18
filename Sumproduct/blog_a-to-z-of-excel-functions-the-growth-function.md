# A to Z of Excel Functions: The GROWTH Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The GROWTH Function

*   March 8, 2020

A to Z of Excel Functions: The GROWTH Function
==============================================

A to Z of Excel Functions: The GROWTH Function
==============================================

9 March 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **GROWTH** function._

**The GROWTH function**

A window function (also known as an apodization or tapering function) is a mathematical function that has a zero value outside of a chosen interval. Uniform distributions and the bell curve are two such window functions commonly used in statistics.

Exponential smoothing is what’s known as a rule of thumb technique (_i.e._ not strictly accurate) for smoothing time series data using the exponential window function. The aim is to smooth out historical data to predict trends, _etc._

The aim is to develop a technique to identify what would be next in a series, _i.e._ forecast the future. There are various approaches used:

*   **Naïve method:** this really does live up to its billing – you simply use the last number in the sequence, _e.g._ the continuation of the series 8, 17, 13, 15, 19, 14, … would be 14, 14, 14, 14, … Hmm, great
*   **Simple average:** only a slightly better idea: here, you use the average of the historical series, _e.g._ for the continuation of the series 8, 17, 13, 15, 19, 14, … would be 14.3, 14.3, 14.3, 14.3, …
*   **Moving average:** now we start to look at smoothing out the trends by taking the average of the last **n** items. For example, if **n** were 3, then the sequence continuation of 8, 17, 13, 15, 19, 14, … would be 16, 16.3, 15.4, 15.9, 15.9, …
*   **Weighted moving average:** the criticism of the moving average is that older periods carry as much weighting as more recent periods, which is often not the case. Therefore, a weighted moving average is a moving average where within the sliding window values are given different weights, typically so that more recent points matter more. For example, instead of selecting a window size, it requires a list of weights (which should add up to 1). As an illustration, if we picked four periods and \[0.1, 0.2, 0.3, 0.4\] as weights, we would be giving 10%, 20%, 30% and 40% to the last 4 points respectively which would add up to 1 (which is what it would need to do to compute the average).
    
    Therefore the continuation of the series 8, 17, 13, 15, 19, 14, … would be 15.6, 15.7, 15.7, 15.5, 15.6, …
    

These only go so far. Sometimes, you want to spot non-linear, trends, _e.g._ sales are based on an exponential growth curve. The **GROWTH** function calculates the predicted exponential growth by using existing data. It returns the **y**\-values (dependent values) for a series of new **x**\-values (independent values) that you specify by using existing **x**\-values and **y**\-values. Therefore, you may use the **GROWTH** worksheet function to fit an exponential curve to existing **x**\-values and **y**\-values too.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-260-1.jpg)

The **GROWTH** function employs the following syntax to operate:

**GROWTH(known\_y’s, \[known\_x’s\], \[new\_x’s\], \[constant\])**

The **GROWTH** function has the following arguments:

*   **known\_y’s:** this is required and represents the set of **y**\-values you already know in the relationship **y = b\*m^x**
    *   if the array **known\_y’s** is in a single column, then each column of **known\_x’s** is interpreted as a separate variable
    *   if the array **known\_y’s** is in a single row, then each row of **known\_x’s** is interpreted as a separate variable
    *   if any of the numbers in **known\_y’s** is zero or negative, **GROWTH** returns the _#NUM!_ error value
*   **known\_x’s:** this argument is optional and denotes an optional set of **x**\-values that you may already know in the relationship **y = b\*m^x**
    *   the array **known\_x’s** can include one or more sets of variables. If only one variable is used, **known\_y’s** and **known\_x’s** can be ranges of any shape, as long as they have equal dimensions. If more than one variable is used, **known\_y’s** must be a vector (that is, a range with a height of one row or a width of one column)
    *   if **known\_x’s** is omitted, it is assumed to be the array {1,2,3,…} that is the same size as **known\_y’s**
*   **new\_x’s:** this is optional. These are new x-values for which you want **GROWTH** to return corresponding **y**\-values
    *   **new\_x’s** must include a column (or row) for each independent variable, just as **known\_x’s** does. Therefore, if **known\_y’s** is in a single column, **known\_x’s** and **new\_x’s** must have the same number of columns. If **known\_y’s** is in a single row, **known\_x’s** and **new\_x’s** must have the same number of rows
    *   if **new\_x’s** is omitted, it is assumed to be the same as **known\_x’s**
    *   if both **known\_x’s** and **new\_x’s** are omitted, they are assumed to be the array {1,2,3,…} that is the same size as **known\_y’s**
*   **constant:** this is also optional. This represents a logical value specifying whether to force the constant **b** to equal 1
    *   if **constant** is TRUE or omitted, **b** is calculated normally
    *   if **constan**t is FALSE, **b** is set equal to 1 and the **m**\-values are adjusted so that **y = m^x**.

Further, it should be noted:

*   formulae that return arrays must be entered as array formulae after selecting the correct number of cells
*   when entering an array constant for an argument such as **known\_x’s**, use commas to separate values in the same row and semicolons to separate rows.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-growth-function/#0 "close")

top