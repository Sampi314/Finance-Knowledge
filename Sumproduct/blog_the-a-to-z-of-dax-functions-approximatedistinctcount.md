# The A to Z of DAX Functions – APPROXIMATEDISTINCTCOUNT

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – APPROXIMATEDISTINCTCOUNT

*   March 22, 2022

The A to Z of DAX Functions – APPROXIMATEDISTINCTCOUNT
======================================================

Power Pivot Principles: The A to Z of DAX Functions – APPROXIMATEDISTINCTCOUNT
==============================================================================

22 March 2022

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week, we look at **APPROXIMATEDISTINCTCOUNT**._

**_The APPROXIMATEDISTINCTCOUNT function_**

![](<Base64-Image-Removed>)

The DAX function [**DISTINCTCOUNT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
 counts the number of distinct (unique) values in a column. It has the following syntax to operates:

**DISTINCTCOUNT**(**column**)

where:

*   **column** is the **column** that contains the values to be counted.

In the image above, **DISTINCTCOUNT(Country)** would return a value of two \[2\].

**APPROXIMATEDISTINCTCOUNT** returns the _approximate_ number of rows that contain distinct values in a column of data. This function can query large amounts of data with potentially better performance than **DISTINCTCOUNT**, with a possible slight deviation from the exact result.

It has the following syntax:

**APPROXIMATEDISTINCTCOUNT**(**column**)

where:

*   **column** is the **column** that contains the values to be counted. This may not be an expression.

This function returns the number of distinct values in **column**. The only argument allowed in this function is a **column**. We can use columns containing any type of data. When the function finds no rows to count, it returns **BLANK**; otherwise, it returns the count of distinct values.

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ [_here_](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
_._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-approximatedistinctcount/#0 "close")

top