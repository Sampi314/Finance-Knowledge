# The A to Z of DAX Functions – BLANK

**Source:** https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/

---

[Home](https://sumproduct.com/)

\> The A to Z of DAX Functions – BLANK

*   November 9, 2021

The A to Z of DAX Functions – BLANK
===================================

Power Pivot Principles: The A to Z of DAX Functions – BLANK
===========================================================

9 November 2021

_In our long-established Power Pivot Principles articles, we continue our series on the A to Z of Data Analysis eXpression (DAX) functions. This week our functions draw a **BLANK**…_

![](<Base64-Image-Removed>)

The **BLANK()** function takes no arguments and returns a blank.

**\=BLANK()**

That’s right. The above is truly a blank expression _(groan – Ed.)_.

It should be noted that:

*   blanks are not equivalent to nulls
*   DAX uses blanks for both database _null_ values and for blank cells in Excel
*   some DAX functions treat blank cells somewhat differently from Microsoft Excel. Blanks and empty strings (“”) are not always equivalent, but some operations may treat them as such. For example, if the original data source were a SQL Server database, _null_ values and empty strings are different kinds of data. However, when **BLANK()** is called, an implicit type cast is performed and DAX treats them as the same.

As an example, imagine you wanted to build a ‘**Profit Margin**’ measure:

![](<Base64-Image-Removed>)

Nothing seems to be wrong with this formula, even Power Pivot thinks so. But what if there were no sales in one period? We would get a division by zero error. To avoid the potential error, we can use the IF function to provide us with an error trap:

![](<Base64-Image-Removed>)

This will return a zero value when the sales are nil. But why report it anyway? We can use the **BLANK** function to further streamline this measure _viz._

![](<Base64-Image-Removed>)

Now the value will be suppressed in the Pivot Table if sales are blank, leading to clearer, more concise reports.

(It is acknowledged the **DIVIDE** function could have been used here, but we are trying to demonstrate an application of the **BLANK** function.)

_Come back next week for our next post on Power Pivot in the_ _[Blog](https://www.sumproduct.com/blog)
_ _section. In the meantime, please remember we have training in Power Pivot which you can find out more about_ [_here_](https://www.sumproduct.com/courses/)
_. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs_ _[here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
__._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/#0)
    
*   [Register](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/#0)

[](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/#0 "close")

top