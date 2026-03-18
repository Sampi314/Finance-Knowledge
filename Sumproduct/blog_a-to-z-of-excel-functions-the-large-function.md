# A to Z of Excel Functions: The LARGE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The LARGE Function

*   September 3, 2021

A to Z of Excel Functions: The LARGE Function
=============================================

A to Z of Excel Functions: The LARGE Function
=============================================

4 September 2021

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **LARGE** function._

**The LARGE function**

Are you living life **LARGE**? This function returns the **k**th largest value in a data set. You can use this function to select a value based on its relative standing. For example, you can use **LARGE** to return the highest, runner-up, or third-place score. Its syntax is as follows:

**\=LARGE(range, k)**

**LARGE** has the following arguments:

*   **array:** this is required and represents the array or range of data for which you want to determine the **k**th largest value
*   **k:** this is also required. This denotes the position (from the largest) in the array or cell range of data to return.

It should be noted that:

*   if **array** is empty**, LARGE** returns the _#NUM!_ error value
*   if **k** ≤ 0 or if **k** is greater than the number of data points, **LARGE** returns the _#NUM!_ error value
*   if **n** is the number of data points in a range, then **LARGE(array,1)** returns the largest value, and **LARGE(array,n)** returns the smallest value.

**k** must be a positive integer less than or equal to the number of non-blank items in the **range**. For example,

![](<Base64-Image-Removed>)

There are opportunities to create errors using this reasonably straightforward function:

![](<Base64-Image-Removed>)

Again, other than choosing an inappropriate **n** (_e.g_. choosing a negative value, too large a value or a non-integer), blank cells may again cause problems. Ensure you do not include blank cells in your given **range**.

**LARGE** may be used to rank numerical data in descending order using the **ROWS** function:

![](<Base64-Image-Removed>)

**LARGE** may also be used to derive statistical data from a range, sometimes requiring an array formula and sometimes not (this is often a case of trial and error for the inexperienced). For example, here’s two ways to calculate the sum of the top three (largest) values in the following range:

![](<Base64-Image-Removed>)

The formulae

**{=SUM(LARGE(F71:F85,H71:H73))}**_and_

**\=SUM(LARGE(F71:F85,{1,2,3}))**

will both sum the top three items in the list. You should note that an array formula is avoided in the second formula as **n** is specified as **{1,2,3}** – effectively creating an array of data without pressing **CTRL + SHIFT + ENTER**.

Similar formulae may be created for the sum of the bottom five, the average of the fourth, eighth and 12th largest items and so on. Try doing that with **MAX** or **MIN**!

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
.  
_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/#0 "close")

top