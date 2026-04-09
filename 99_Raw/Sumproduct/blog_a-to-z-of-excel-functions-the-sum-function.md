# A to Z of Excel Functions: The SUM Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SUM Function

*   March 9, 2026

A to Z of Excel Functions: The SUM Function
===========================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **SUM** function._

**The SUM function**

![](<Base64-Image-Removed>)

Is there really anyone out there that hasn’t encountered the **SUM** function?  Is there anything new for me to tell you about **SUM**..?

Well, let me try.

**SUM** adds things up:  you can add individual values, cell reference, a range or any combination thereof.  It may include cells, numbers or ranges.  In the context of financial modelling, summations are usually of numbers either directly above or to the left of the cell in question:

![](<Base64-Image-Removed>)

There is a great keyboard shortcut available on most PC’s _(PC = proper computer)_.  If you select the cell to the right or directly below the values to be aggregated and then use the shortcut **ALT + =** you will see that the range is summed automatically.  If you find this doesn’t work for you, make sure you keep the **ALT** button held down on your keyboard.

It’s a fast shortcut, it ensures you don’t miss cells within the range, it requires the range to be contiguous and you can’t leave blank cells.  This shortcut actually forces you to build in a manner that will reduce the number of errors you might make. 

Be careful with **SUM**.  Consider the following example:

![](<Base64-Image-Removed>)

In this example, we have totalled the values in cells **E3:E7** in two distinct ways: the first uses the aforementioned **SUM** function with **ALT + =**, the other has added each cell individually using the ‘+’ operator.  Are you thinking you’d be mad to use the alternative (second) approach – especially if there were many more rows?

Well, take another look:

In this example, cell **E5** has been modified.  It has been stored as text, even though it looks like the number 3.  **SUM** treats this as having zero value whereas the more convoluted addition carries on regardless. 

In an example like the one above, this may be easy to spot, but would you stake your life that the sum

![](<Base64-Image-Removed>)

is correct?

There is a simple way to check using the **COUNT** function.  **COUNT** counts the number of numbers in a range, so we can use it to spot numbers that aren’t numbers:

![](<Base64-Image-Removed>)

Here, the formula in column **I** highlights when a number is not a number.  Note how it reports by exception: if the cell in question contains a number, then **COUNT(cell\_reference)** equals 1 and **\=1-COUNT(cell\_reference)** equals zero \[0\].  Only non-numbers will be highlighted – it’s better to know we have two errors rather than 14,367 values working correctly.

If you don’t think this applies to you, have you ever worked with PivotTables?  This article isn’t about PivotTables, but as an aside, for those of you who have ever worked with this Excel feature, have you ever been frustrated when the following has happened?

![](<Base64-Image-Removed>)

You want your aggregation of values to default to **SUM** but instead they display as **COUNT**.  This could be highlighting that some of your data is non-numerical and / or blank. 

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sum-function/#0 "close")

top