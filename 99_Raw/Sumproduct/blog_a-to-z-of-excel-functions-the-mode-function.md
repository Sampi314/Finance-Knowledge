# A to Z of Excel Functions: The MODE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The MODE Function

*   July 17, 2022

A to Z of Excel Functions: The MODE Function
============================================

A to Z of Excel Functions: The MODE Function
============================================

18 July 2022

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **MODE** function._

**The MODE function**

The mode is the value that appears most often in a set of data values. If **X** is a discrete random variable, the mode is the value **x** (_i.e_. **X = x**) at which the probability mass function takes its maximum value; it is the value that is most likely to be sampled.

The mode is not necessarily unique to a given discrete distribution, since the probability mass function may take the same maximum value at several points **x1**, **x2**, _etc._ The most extreme case occurs in uniform distributions, where all values occur equally frequently.

In symmetrical unimodal (_i.e_. only one mode value) distributions, such as the normal distribution, the mean (if defined), median and mode all coincide. For samples, if it is known that they are drawn from a symmetrical unimodal distribution, the sample mean can be used as an estimate of the population mode.

The **MODE** function measures what is known as “central tendency”, which is the location of the centre of a group of numbers in a statistical distribution. There are three common measures of central tendency:

*   **Average:** the arithmetic mean, calculated by adding a group of numbers and then dividing by the count of those numbers. For example, the average of 2, 3, 3, 5, 7, and 10 is 30 divided by 6, which is 5
*   **Median:** the middle number of a group of numbers; that is, half the numbers have values that are greater than the median, and half the numbers have values that are less than the median. For example, the median of 2, 3, 3, 5, 7, and 10 is 4. If the number of values in the selection is an even number, the median is defined as the midpoint between the two central numbers
*   **Mode:** the most frequently occurring number in a group of numbers. For example, the mode of 2, 3, 3, 5, 7, and 10 is 3.

For a symmetrical distribution of a group of numbers, these three measures of central tendency are all the same. For a skewed distribution of a group of numbers, they can be different.

The **MODE** function employs the following syntax to operate:

**MODE(number1, \[number2\], …)**

The **MODE** function has the following arguments:

*   **number1**: this is required. The first number, cell reference, or range for which you want to calculate the mode
*   **number2**, …: this is optional. Additional numbers, cell references or ranges for which you want the mode, up to a maximum of 255 in total.

It should be further noted that:

*   arguments may either be numbers or names, ranges or cell references that contain numbers
*   logical values and text representations of numbers that you type directly into the list of arguments are counted
*   if a range or cell reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included
*   arguments that are error values or text that cannot be translated into numbers cause errors
*   if the data set contains no duplicate data points, **MODE** returns the _#N/A_ error
*   if there is more than one mode, **MODE** reports the first mode value that occurs.

This function has been replaced with two new functions (**MODE.MULT** and **MODE.SNGL**) that may provide improved accuracy and whose names better reflect their usage. Although this function is still available for backward compatibility, you should consider using the new functions from now on, because this function may not be available in future versions of Excel.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found__[here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-mode-function/#0 "close")

top