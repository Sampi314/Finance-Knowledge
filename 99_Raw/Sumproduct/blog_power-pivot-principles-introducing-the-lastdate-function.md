# Power Pivot Principles: Introducing the LASTDATE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the LASTDATE Function

*   August 5, 2019

Power Pivot Principles: Introducing the LASTDATE Function
=========================================================

Power Pivot Principles: Introducing the LASTDATE Function
=========================================================

6 August 2019

_Welcome back to our Power Pivot blog. Today, we show you how the LASTDATE function work._

The **LASTDATE** function is a time intelligence function, just like the **DATESINPERIOD** function. We have covered the [**DATESINPERIOD**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-datesinperiod-function)
function last week.

The **LASTDATE** function uses the following syntax to operate:

**LASTEDATE**( **<date>**)

The **<date>** parameter must be a column with dates. The **<date>** parameter can also be a table expression that will return a single column of dates.

The **LASTDATE** function returns with a table containing a single row and column with the latest date value from the input column from the **<date>** parameter.

In last week’s blog, we used the **MIN** function to determine the earliest date in the column. So why would we use the **LASTDATE** function?

Well, we can use the **LASTDATE** function with other expressions that require a table input and not a scalar input.

The other reason is that we can use filter functions that return with a table as the **<date>** input. Let’s say that we wish to retrieve the last date from the following dataset:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-385.jpg)

We can use this measure:

\=LASTDATE(SaleDataJul1\[Date\])

![](<Base64-Image-Removed>)

Inserting this measure into a PivotTable:

![](<Base64-Image-Removed>)

It just returns with the respective row’s date, this is because the measure, as it stands, is subject to the row filters. If we remove the date column, we can see that the measure is returning with the last date in our data:

![](<Base64-Image-Removed>)

It seems that we will need to make some adjustments to our measure for it to return with the last date on each row:

\=LASTDATE(

            ALL(

                        SaleDataJul1\[Date\]

                        )

            )

![](<Base64-Image-Removed>)

Including this measure in our PivotTable yields:

![](<Base64-Image-Removed>)

We have included the **ALL** function, so that it forces the **LASTDATE** function to disregard the row filters on each row. We can now use this measure to create more complex calculations in DAX, but more on that in a future blog…

That’s it for this week, come back next week for more Power Pivot. Until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-lastdate-function/#0 "close")

top