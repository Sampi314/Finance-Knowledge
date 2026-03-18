# Charts and Dashboards: Tornado Charts – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Tornado Charts – Part 2

*   May 5, 2022

Charts and Dashboards: Tornado Charts – Part 2
==============================================

Charts and Dashboards: Tornado Charts – Part 2
==============================================

6 May 2022

_Welcome back to our Charts and Dashboards blog series._ _This week, we’ll begin to construct a Tornado chart._

[Last week](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-1/)
, we covered the basics of a Tornado chart and how it can be useful. This week, we’ll look at how to begin constructing said chart.

![](<Base64-Image-Removed>)

In this example, we have some data regarding how each variable affects a measured output in a **Low**, **Base**, and **High** scenario.

![](<Base64-Image-Removed>)

To give the Tornado chart its signature look, we must first rank these variables by the magnitude of the difference it caused. To do this, we begin by looking at the range of the output between the **Low** and **High** scenarios. This can be calculated by taking the [absolute](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-abs-function)
 value of the output in one case, less the output in the other case.

**\=ABS(J13-H13)**

![](<Base64-Image-Removed>)

The next step is to obtain the rank of each variable by the magnitude of the effect it has had on the output. This can be achieved by using the **RANK** formula on our new **Spread** column:

**\=RANK($L13,$L$13:$L$18)**

![](<Base64-Image-Removed>)

However, this approach could cause issues. If multiple variables have the same **Spread**, we will see the same **Rank** figure multiple times, which would become problematic down the line.

![](<Base64-Image-Removed>)

This problem can be avoided by making use of the **[COUNTIF](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countif-function)
** function to count how many occurrences of a value there have been prior to the one we’re ranking and then adding this to the rank.

**\=RANK($L13,$L$13:$L$18)+COUNTIF($L$12:$L12,$L13)**

![](<Base64-Image-Removed>)

The next step will be to reorder our variables into rank order. This can be achieved using the **[INDEX](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
** function in conjunction with the **[MATCH](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
** function to return the name of the variable where the **Rank** matches a simple ascending counter.

**\=INDEX(E$13:E$18,MATCH($D23,$N$13:$N$18,0))**

![](<Base64-Image-Removed>)

We can use a similar approach to pull down the relevant data for each variable.

![](<Base64-Image-Removed>)

Creating a bar chart of this data won’t quite give you the classic Tornado chart look, but we’re a lot closer now!

![](<Base64-Image-Removed>)

We will cover the final steps of creating and formatting the Tornado Chart next week, in part 3.

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-tornado-charts-part-2/#0 "close")

top