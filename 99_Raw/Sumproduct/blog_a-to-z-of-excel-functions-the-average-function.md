# A to Z of Excel Functions: The AVERAGE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The AVERAGE Function

*   September 18, 2016

A to Z of Excel Functions: The AVERAGE Function
===============================================

A to Z of Excel Functions: The AVERAGE Function
===============================================

19 September 2016

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **AVERAGE** function._

**The AVERAGE function**

This is quite an ordinary function; indeed, it is distinctly average. Returns the average (arithmetic mean) of the arguments. For example, if the range **A1:A20** contains numbers, the formula **\=AVERAGE(A1:A20)** returns the arithmetic mean of those numbers, including counting zeros.

The **AVERAGE** function measures what is known as “central tendency”, which is the location of the centre of a group of numbers in a statistical distribution. There are three common measures of central tendency:

*   **Average:** the arithmetic mean, calculated by adding a group of numbers and then dividing by the count of those numbers. For example, the average of 2, 3, 3, 5, 7, and 10 is 30 divided by 6, which is 5
*   **Median:** the middle number of a group of numbers; that is, half the numbers have values that are greater than the median, and half the numbers have values that are less than the median. For example, the median of 2, 3, 3, 5, 7, and 10 is 4. If the number of values in the selection is an even number, the median is defined as the midpoint between the two central numbers
*   **Mode:** the most frequently occurring number in a group of numbers. For example, the mode of 2, 3, 3, 5, 7, and 10 is 3.

For a symmetrical distribution of a group of numbers, these three measures of central tendency are all the same. For a skewed distribution of a group of numbers, they can be different.

The **AVERAGE** function employs the following syntax to operate:

**AVERAGE(number1, \[number2\], …)**

The **AVERAGE** function has the following arguments:

*   **number1**: this is required. The first number, cell reference, or range for which you want the average
*   **number2**, …: this is optional. Additional numbers, cell references or ranges for which you want the average, up to a maximum of 255 in total.

It should be further noted that:

*   Arguments can either be numbers or names, ranges, or cell references that contain numbers
*   Logical values and text representations of numbers that you type directly into the list of arguments are counted
*   If a range or cell reference argument contains text, logical values, or empty cells, those values are ignored; however, cells with the value zero are included
*   Arguments that are error values or text that cannot be translated into numbers cause errors
*   If you want to include logical values and text representations of numbers in a reference as part of the calculation, use the **AVERAGEA** function
*   If you want to calculate the average of only the values that meet certain criteria, use the **AVERAGEIF** or **AVERAGEIFS** functions.

You should bear in mind that when you average cells, there is a difference between empty cells and those containing the value zero. If you have cleared the ‘Show a zero in cells that have a zero value’ check box in the Excel Options dialog box in Excel, you may not realise zeros are being included in calculating the average. To locate the ‘Show a zero in cells that have a zero value’ check box, go to **File -> Options -> Advanced** and look under ‘Display options for this worksheet’.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-average-function/#0 "close")

top