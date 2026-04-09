# A to Z of Excel Functions: The ROWS Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The ROWS Function

*   February 9, 2025

A to Z of Excel Functions: The ROWS Function
============================================

A to Z of Excel Functions: The ROWS Function
============================================

10 February 2025

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **ROWS** function._

**The ROWS function**

![](<Base64-Image-Removed>)

The **ROWS** function returns the row number of a reference:

**ROWS(array)**

The **ROWS** function has the following argument:

*   **array**: this argument is required and represents an array, an array formula or a reference to a range of cells for which you want to know the number of rows.

Please see my examples below:

![](<Base64-Image-Removed>)

**ROWS** is sometimes associated with the **[HLOOKUP](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-hlookup-function)
**function. **HLOOKUP** always looks for the **lookup\_value** in the first row of a table (the **table\_array**) and then returns a corresponding value so many rows below, determined by the **row\_index\_number**, _e.g._

![](<Base64-Image-Removed>)

In this above example, the formula in cell **G25** seeks the value 2 in the first row of the table **G12:M18** and returns the corresponding value from the seventh row of the table (returning 96).

Pretty easy to understand; so far so good. So what goes wrong? Well, what happens if you add or remove a row from the table range? Adding (inserting) a row gives us the wrong value:

![](<Base64-Image-Removed>)

With a row inserted, the formula contains hard code (7) and therefore, the seventh row (row 18, not row 19) is still referenced, giving rise to the wrong value. Deleting a row instead is even worse:

![](<Base64-Image-Removed>)

Now there are only six rows so the formula returns _#REF!_ Oops.

It is possible to make the row index number dynamic using the **ROWS** function (that’s right, every **ROWS** has its **HLOOKUP** function):

![](<Base64-Image-Removed>)

**ROWS(reference)** counts the number of rows in the **reference**. Using the range **F12:F18**, this formula will now keep track of how many rows there are between the lookup row (12) and the result row (18). This will prevent the problems illustrated above.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-rows-function/#0 "close")

top