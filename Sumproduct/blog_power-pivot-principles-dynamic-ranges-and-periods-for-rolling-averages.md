# Power Pivot Principles: Dynamic Ranges and Periods for Rolling Averages

**Source:** https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Dynamic Ranges and Periods for Rolling Averages

*   August 19, 2019

Power Pivot Principles: Dynamic Ranges and Periods for Rolling Averages
=======================================================================

Power Pivot Principles: Dynamic Ranges and Periods for Rolling Averages
=======================================================================

20 August 2019

_Welcome back to our Power Pivot blog. Today, we expand on the rolling average concept, first introduced in a previous blog, and show you how to include a dynamic period selection range in a rolling average measure._

Heard of flogging a dead horse? We clearly haven’t…

Last week, we talked about creating a dynamic average range for a measure. As a recap, we used this measure to include a dynamic selection for the average range:

\=CALCULATE(

            AVERAGEX(SaleDataJul1, SaleDataJul1\[Sum of Total Sales\]),

                        DATESINPERIOD(

                                    SaleDataJul1\[Date\],

                        MIN(

                                    SaleDataJul1\[Date\]),

                                    -MAX(

                                                Days\_Average\[Days to Average\]),

                                    DAY

            )

)

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-376.jpg)

What if we also had to build in the ability to select the date range for our rolling average?

The first thing one would think of is to create a timeline slicer for our PivotTable

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-386.jpg)

to select different dates on the slicer filters our PivotTable. However, our measure ignores the date filter and returns with the same moving average values:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-365.jpg)

We want the measure to calculate the rolling average starting from the first date in our date selection. We use the **FILTER** and **ALLSELECTED** functions to create a new measure that will incorporate date selection ranges into the rolling average calculation as follows:

\=CALCULATE(

                AVERAGE(SaleDataJul1\[Total Sales\]),

                FILTER(

                                ALLSELECTED(SaleDataJul1),

                                                        SaleDataJul1\[Date\] > MAX(SaleDataJul1\[Date\]) – MAX(Days\_Average\[Days to Average\]) &&                                                                                                                                           SaleDataJul1\[Date\] <= MAX(SaleDataJul1\[Date\])                              

                                )

                )

![](<Base64-Image-Removed>)

In this measure we use the filter in the **CALCULATE** function, so we do not need to use the **AVERAGEX** function. The filter expression in this measure is a combination of two criteria combined with a double ampersand delimiter “&&” (the “and” operator). The first criterion

SaleDataJul1\[Date\] > MAX(SaleDataJul1\[Date\]) – MAX(Days\_Average\[Days to Average\])

considers the later range of dates to average, less the number of days to the average from our input. The second criterion

SaleDataJul1\[Date\] <= MAX(SaleDataJul1\[Date\])             

assesses the earlier range of dates to include in the average. With these two criteria combined the measure is able to take in the inputs of our date slicer and our Days to Average slicer to calculate our rolling average:

![](<Base64-Image-Removed>)

There we have it: a dynamic rolling average measure that can take inputs from both a date range to average and the number of days to average.

That’s it for this week, come back next week for more Power Pivot. Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/#0)

[](https://sumproduct.com/blog/power-pivot-principles-dynamic-ranges-and-periods-for-rolling-averages/#0 "close")

top