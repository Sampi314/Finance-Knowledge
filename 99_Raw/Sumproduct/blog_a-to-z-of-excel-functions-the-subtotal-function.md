# A to Z of Excel Functions: The SUBTOTAL Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SUBTOTAL Function

*   February 23, 2026

A to Z of Excel Functions: The SUBTOTAL Function
================================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **SUBTOTAL** function._

**The SUBTOTAL function**

![](https://sumproduct.com/wp-content/uploads/2026/02/image-76.png)

At first glance, **SUBTOTAL** seems like many other Excel functions:

> **\=SUBTOTAL(function\_number, ref1, ref2, …)**

The **function\_number** is an integer between one \[1\] and 11 inclusive or 101 and 111 inclusive as follows:

![](https://sumproduct.com/wp-content/uploads/2026/02/image-77.png)

For the **function\_number** constants from one \[1\] to 11, the **SUBTOTAL** function includes the values of rows hidden by the ‘Hide Rows’ command.  These constants should be used when you want to subtotal hidden and unhidden (visible) numbers in a list.  For the **function\_number** constants from 101 to 111, the **SUBTOTAL** function ignores values of rows hidden by the ‘Hide Rows’ command.  These constants should be used when you want to subtotal the visible numbers in a list only.

If there are other subtotals within **ref1, ref2, …** (or nested subtotals), these nested subtotals are ignored.  This is an important feature as it allows you to consider complete ranges without any risk of double-counting.

As an example:

![](https://sumproduct.com/wp-content/uploads/2026/02/image-78.png)

It is a useful function and once you understand how it works with hidden rows and filtering, it can prove to be quite flexible.  However, its full power and versatility is not truly realised until you start using the Subtotal functionality…

To illustrate the power of the Subtotal functionality, consider the following example:

![](<Base64-Image-Removed>)

Imagine you have data of sales for four customers and four products over a period of time, which you wish to summarise.  Highlighting the table (including the row containing the headers), the data can be sorted using Excel’s built-in **Sort** functionality (go to the ‘Data’ tab of the Ribbon and then in the ‘Sort & Filter’ section, click on Sort):

![](<Base64-Image-Removed>)

Alternatively, **ALT + D + S** or **ALT + A + SS** works here too – but don’t let the latter keyboard shortcut make an **ASS** out of you! 

This activates the Sort dialog box:

![](<Base64-Image-Removed>)

Ensure that the ‘My data has headers’ checkbox has been ticked and then sort as required using the ‘Add Level’ and ‘Delete Level’ buttons as necessary.  When finished, click on the ‘OK’ button.  The data will have then been sorted:

![](<Base64-Image-Removed>)

Now the data is in a suitable format for subtotalling.  Again, once the data (including the headers) has been highlighted, click on ‘Subtotal’ (located on the ‘Data’ tab of the Ribbon in the ‘Outline’ section):

![](<Base64-Image-Removed>)

Alternatively, **ALT + D + B** or **ALT + A + B** works for all versions of Excel, too.

This activates the Subtotal dialog box:

![](<Base64-Image-Removed>)

The dialog box is fairly self-explanatory.  The **SUBTOTAL** functions can be used as if you had chosen a **function\_number** between one \[1\] and 11.  In seconds, you have turned data into information:

![](<Base64-Image-Removed>)

Very useful!

### Word to the Wise

If you incorporate filtering in your list / database, the **SUBTOTAL** function ignores any rows that are not included in the result of a filter, no matter which **function\_number** value you use.

It should be noted that the **SUBTOTAL** function is designed for columns of data / vertical ranges.  It is not designed for rows of data / horizontal ranges.  For example, when you subtotal a horizontal range using a **function\_number** of 101 or greater, such as **SUBTOTAL(109,A1:A10)**, hiding a column does not affect the subtotal.  However, hiding a row in a subtotal of a vertical range will affect the subtotal.

**SUBTOTAL** is designed only to work on vector references (_i.e_. where **ref1, ref2, …** are ranges containing wither just one row or just one column).  If arrays (ranges of cells containing at least two rows and two columns), **SUBTOTAL** returns the _#VALUE!_ error value.

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-subtotal-function/#0 "close")

top