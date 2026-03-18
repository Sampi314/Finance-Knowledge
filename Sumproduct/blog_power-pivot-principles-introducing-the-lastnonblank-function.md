# Power Pivot Principles: Introducing the LASTNONBLANK Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the LASTNONBLANK Function

*   June 24, 2019

Power Pivot Principles: Introducing the LASTNONBLANK Function
=============================================================

Power Pivot Principles: Introducing the LASTNONBLANK Function
=============================================================

25 June 2019

_Welcome back to our Power Pivot blog. Today, we will go over how to use the LASTNONBLANK function._

The **LASTNONBLANK** function returns the last value in the column, where the expression is not blank. This function requires the following syntax to operate:

**LASTNONBLANK**( <column>, <expression> )

The <column> parameter can be a:

*   Reference to a column
*   A table with a single column
*   A Boolean expression that defines an individual column.

The **<expression>** is evaluated on each row of the column for blanks.

In this example we will be using the following data table:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-406.jpg)

After we have loaded the Table into Power Pivot and created a PivotTable, we can populate it with some measures:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-420.jpg)

We first create a measure the sums the total sales:

\=SUM(

SalesAndCategory\[Sales\]

)

Now, we can create a measure that retrieves the category of the last sale:

\=LASTNONBLANK(

SalesAndCategory\[Category\],

\[Total Sales\]

)

![](<Base64-Image-Removed>)

We can see that the measure is in fact returning with category 4:

![](<Base64-Image-Removed>)

which is what we would expect.

Now, what if we want a measure that will retrieve the value of the last sale? Following the logic of the previous measure we can write:

\=LASTNONBLANK(

SalesAndCategory\[Sales\],

\[Sales\]

)

![](<Base64-Image-Removed>)

Placing the measure in our PivotTable yields:

![](<Base64-Image-Removed>)

That’s not quite right. This is because it has arranged the sales in descending order before retrieving the last non-blank value. In order to retrieve the last sale amount based on dates, ‘$ 146.00’, we have to use the **CALCULATE** function:

\=CALCULATE(

\[Sum of Sales\],

LASTNONBLANK(

SalesAndCategory\[Date\],

\[Sum of Sales\]

)

)

![](<Base64-Image-Removed>)

Looking back to our PivotTable:

![](<Base64-Image-Removed>)

It works as expected. These measures are also dynamic: we can insert slicers and have them change accordingly!

![](<Base64-Image-Removed>)

Note that if we do not use the **CALCULATE** function with the **LASTNONBLANK** function the measure will arrange the sales in decending order before retrieving the last non-blank value. Don’t be caught out!

That’s it for this week, come back next week for more Power Pivot. Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastnonblank-function/#0 "close")

top