# A to Z of Excel Functions: The HLOOKUP Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The HLOOKUP Function

*   April 12, 2020

A to Z of Excel Functions: The HLOOKUP Function
===============================================

A to Z of Excel Functions: The HLOOKUP Function
===============================================

13 April 2020

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **HLOOKUP** function._

**The HLOOKUP function**

Often we need to look up data in a table or list – and one such function many are familiar with is **HLOOKUP**. But do you realise it’s very easy to make a mistake with this function.

**HLOOKUP** has the following syntax:

**HLOOKUP(lookup\_value, table\_array, row\_index\_number, \[range\_lookup\])**

*   **lookup\_value:** what value do you want to look up?
*   **table\_array:** where is the lookup table?
*   **row\_index\_number:** which row has the value you want returned?
*   **\[range\_lookup\]:** do you want an exact or an approximate match? This is optional and to begin with, I am going to ignore this argument exists.

**VLOOKUP** is similar, but works on a column, rather than a row, basis.

**_Example_**

**HLOOKUP** always looks for the **lookup\_value** in the first row of a table (the **table\_array**) and then returns a corresponding value so many rows below, determined by the **row\_index\_number**.

![](<Base64-Image-Removed>)

In this above example, the formula in cell **G25** seeks the value 2 in the first row of the table **G12:M18** and returns the corresponding value from the seventh row of the table (returning 96). You can follow all of these examples in the attached Excel file.

Pretty easy to understand; so far so good. So what goes wrong? Well, what happens if you add or remove a row from the table range?

Adding (inserting) a row gives us the wrong value:

![](<Base64-Image-Removed>)

With a row inserted, the formula contains hard code (8) and therefore, the seventh row (row 18, not row 19) is still referenced, giving rise to the wrong value. Deleting a row instead is even worse:

![](<Base64-Image-Removed>)

Now there are only six rows so the formula returns _#REF!_ Oops.

It is possible to make the row index number dynamic using the **ROWS** function (that’s right, every **ROWS** has its **HLOOKUP** function):

![](<Base64-Image-Removed>)

**ROWS(reference)** counts the number of rows in the **reference**. Using the range **F12:F18**, this formula will now keep track of how many rows there are between the lookup row (12) and the result row (18). This will prevent the problems illustrated above.

But there are more issues. Consider duplicate values in the lookup row. With one duplicate, the following happens:

![](<Base64-Image-Removed>)

Here, the second value is returned, which might not be what is wanted. With two duplicates:

![](<Base64-Image-Removed>)

Ah, it looks like it might take the last occurrence. Testing this hypothesis with three duplicates:

![](<Base64-Image-Removed>)

Yes, there seems to be a pattern: **HLOOKUP** takes the last occurrence. Better make sure:

![](<Base64-Image-Removed>)

Rats. In this example, the value returned is the fifth of six. The problem is, there’s no consistent logic and the formula and its result cannot be relied upon. It gets worse if we exclude duplicates but mix up the lookup row a little:

![](<Base64-Image-Removed>)

In this instance, **HLOOKUP** cannot even find the value 2!

So what’s going on? The problem – and common modelling mistake – is that the fourth argument has been ignored:

**HLOOKUP(lookup\_value, table\_array, row\_index\_number, \[range\_lookup\])**

**\[range\_lookup\]** appears in square brackets, which means it is optional. It has two values:

*   **TRUE**: this is the default setting if the argument is not specified. Here, **HLOOKUP** will seek an approximate match, looking for the largest value less than or equal to the value sought. There is a price to be paid though: the values in the first row must be in strict ascending order – this means that each value must be larger than the value before, so no duplicates.
    
    This is useful when looking up postage rates for example where prices are given in categories of pounds and you have 2.7lb to post (say). It’s worth noting though that this isn’t the most common lookup when modelling.
    
*   **FALSE**: this has to be specified. In this case, data can be any which way – including duplicates – and the result will be based upon the first occurrence of the value sought. If an exact match cannot be found, **HLOOKUP** will return the value _#N/A_.

And this is the problem highlighted by the above examples. The final argument was never specified so the lookup row data has to be in strict ascending order – and this premiss was continually breached.

The robust formula needs both **ROWS** and a fourth argument of **FALSE** to work as expected:

![](<Base64-Image-Removed>)

This is a very common mistake in modelling. Using a fourth argument of **FALSE**, **HLOOKUP** will return the corresponding result for the first occurrence of the **lookup\_value**, regardless of number of duplicates, errors or series order. If an approximate match is required, the data must be in strict ascending order.

**HLOOKUP** is not the simple, easy to use functions people think it is. In fact, it can never be used to return data for rows above.

**_Word to the Wise_**

**VLOOKUP** works like **HLOOKUP** but hunts out a value in the first column of a table and returns a value so many columns to the right of this reference. However, it has the same limitations and should be used just as carefully.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-hlookup-function/#0 "close")

top