# Power Pivot Principles: Introducing the DATESINPERIOD Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the DATESINPERIOD Function

*   July 29, 2019

Power Pivot Principles: Introducing the DATESINPERIOD Function
==============================================================

Power Pivot Principles: Introducing the DATESINPERIOD Function
==============================================================

30 July 2019

_Welcome back to our Power Pivot blog. Today, we show you how the DATESINPERIOD function works._

The **DATESINPERIOD** function is a time intelligence function, just like the **DATESYTD** and **DATEADD** functions. We have covered the **[DATESYTD](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-datesytd-function)
**and the **[DATEADD](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-dateadd-function)
** functions previously.

The **DATESINPERIOD** function uses the following syntax to operate:

**DATESINPERIOD( <dates>, <start\_date>, <number\_of\_intervals>, <interval> )**

This function returns with a table. This table will contain a column of dates that begins with the **<start\_date>** and continues on with the specified **<number\_of\_intervals>**.

The **<dates>** parameter has to be a column with dates.

The **<interval>** parameter has to be one of four predefined inputs by Power Pivot: year, quarter, month, day.

This function is commonly used together with the **CALCULATE** function. You can read more about the **CALCULATE** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-calculate)
.

Let’s take a look at a simple example. Imagine we had the following sales data:

![](<Base64-Image-Removed>)

In this example we want to create a rolling sum for every three days. We can use the following measure:

\=CALCULATE(

            SUM(SaleDataJul1\[Total Sales\]),

                        DATESINPERIOD(

                                    SaleDataJul1\[Date\],

                                    MIN(SaleDataJul1\[Date\]),

                                    3,

                                    DAY

                        )

            )

![](<Base64-Image-Removed>)

This would result in the following PivotTable:

![](<Base64-Image-Removed>)

Strangely, the rolling sum seems to be adding up the future dates. This is because we entered ‘3’ as the **<number\_of\_intervals>.** Therefore, it looks like positive intervals means that the measure will use future dates. Let’s try ‘-3’:

\=CALCULATE(

            SUM(SaleDataJul1\[Total Sales\]),

                        DATESINPERIOD(

                                    SaleDataJul1\[Date\],

                                    MIN(SaleDataJul1\[Date\]),

                                    -3,

                                    DAY

                        )

            )

![](<Base64-Image-Removed>)

Dragging the new measure into our PivotTable:

![](<Base64-Image-Removed>)

Now the measure is adding up sales from the previous dates rather than the future dates. This is all well and good, but having the rolling sum isn’t that useful. What if we changed the **SUM** function into an **AVERAGE** function instead?

\=CALCULATE(

            AVERAGE(SaleDataJul1\[Total Sales\]),

                        DATESINPERIOD(

                                    SaleDataJul1\[Date\],

                                    MIN(SaleDataJul1\[Date\]),

                                    -3,

                                    DAY

                        )

            )

![](<Base64-Image-Removed>)

Adding this measure into our PivotTable:

![](<Base64-Image-Removed>)

There we have it, a rolling average measure where we can change the number of days / periods we want to include in the average.

That’s it for this week, come back next week for more Power Pivot. Until then happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesinperiod-function/#0 "close")

top