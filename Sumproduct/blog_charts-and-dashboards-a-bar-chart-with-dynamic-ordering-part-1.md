# Charts and Dashboards: A Bar Chart with Dynamic Ordering – Part 1

**Source:** https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: A Bar Chart with Dynamic Ordering – Part 1

*   May 20, 2021

Charts and Dashboards: A Bar Chart with Dynamic Ordering – Part 1
=================================================================

Charts and Dashboards: A Bar Chart with Dynamic Ordering – Part 1
=================================================================

21 May 2021

_Welcome back to this week’s Charts and Dashboards blog series. Over the next two weeks, we will discuss creating a bar chart with dynamic ordering._

[Bar Charts](https://sumproduct.com/blog/charts-and-dashboards-bar-charts/)
 are not only useful to illustrate the magnitude of values in one or more data series, but also a good alternative to the [Pie Chart](https://sumproduct.com/blog/charts-and-dashboards-pie-charts/)
, which compares the proportion of a series in a group of data.

For example, here is enrolment data for six sport courses from a youth centre.

![](<Base64-Image-Removed>)

From the above data, if we create a bar chart, it may appear as below:

![](<Base64-Image-Removed>)

We want the bar chart to illustrate the percentage of each course’s participants relative to the total and also sort the bars in order from largest to smallest.

One way to sort the bars is to turn the data in cells **F12:G18** to a table by highlighting the range and press **CTRL + T**, then sort the **Participants** column in the descending order. However, when we update the data in the table, we need to sort the data again so that the chart works in the way we want.

![](<Base64-Image-Removed>)

Let’s consider another way to get this working without using tables. In column **H**, we will get the order of the bar using the **RANK** function. The formula in cell **H13** is:

**\=RANK(G13,$G$13:$G$18,0)**

![](<Base64-Image-Removed>)

Next, we will create a **Chart Data** section to get the related data in order. We will **[INDEX MATCH](https://www.sumproduct.com/thought/index-match)
** against the **Rank** to get the **Course** and **Participants**. The formulae in cells **G26**, **H26** and **I26** are respectively:

**\=INDEX(F$13:F$18,MATCH($F26,$H$13:$H$18,0))**

**\=INDEX(G$13:G$18,MATCH($F26,$H$13:$H$18,0))**

**\=H26/$H$32**

![](<Base64-Image-Removed>)

There is one thing that is not quite right here. Suppose the data changes and the number of participants in the Swimming course and Yoga course are equal _e.g._ they are both 400. Their ranks will be equal first and the **Chart Data** will no longer be correct.

![](<Base64-Image-Removed>)

Hence, we will fix the formula in cell **H13** to get the **[unique rank](https://www.sumproduct.com/thought/unique-rank)
**:

**\=RANK(G13,$G$13:$G$18,0)+COUNTIF($G$13:G13,G13)-1**

![](<Base64-Image-Removed>)

If we revert to the original data and now that we have the **Chart Data** ready, we will select the **Course** and **%** columns to create an initial bar chart that looks like the one below.

![](<Base64-Image-Removed>)

We can do more to get the chart a nicer look, but that’s for next time…

That’s it for this week. Come back in a fortnight for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-a-bar-chart-with-dynamic-ordering-part-1/#0 "close")

top