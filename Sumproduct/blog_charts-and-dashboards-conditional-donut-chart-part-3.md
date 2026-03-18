# Charts and Dashboards: Conditional Donut Chart – Part 3

**Source:** https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Conditional Donut Chart – Part 3

*   April 1, 2021

Charts and Dashboards: Conditional Donut Chart – Part 3
=======================================================

Charts and Dashboards: Conditional Donut Chart – Part 3
=======================================================

2 April 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we will get the data label in the “conditional donut chart”._

To recap, in [Part 1](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-1/)
 of this series, from the group rating data and the transformed chart data table (as shown below),

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-224.jpg)

we created an initial donut chart:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-285.jpg)

Then, in [Part 2](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/)
, we constructed some conditional formatting in the colour of the series so that each of the series indicating the same rating will be displayed with the same colour, _e.g._ the three series Group 1-1, Group 2-1 and Group 3-1 have a rating 1 and should therefore share the same colour scheme.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-228.jpg)

There is not much information that can be drawn from the chart, as we could not distinguish between the groups and their ratings. Hence, it’s a good idea to add data labels to the chart by getting the ‘Data Labels’ from the ‘Chart Elements’ list, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-215.jpg)

We only have three groups and their ratings, but we get more than three data labels; furthermore, the names of the group do not seem right. To fix this, we need to go back to the **Chart Data** table. First, we need to change the formula in the Chart Data column _i.e._ **H21:H35**, from

**\=IF(SUMIFS(Group\_Point\[Rating\],Group\_Point\[Group\],\[@Group\])=\[@Rating\],\[@Rating\],0)**

to

**\=IF(SUMIFS(Group\_Point\[Rating\],Group\_Point\[Group\],\[@Group\])=\[@Rating\],\[@Rating\],NA())**

Originally, the series with the zero \[0\] value will still be plotted in the chart (we just cannot see it because it is zero), hence, our chart has fifteen series in it. Meanwhile, the series with **_#N/A_** will not be plotted. Thus, our chart will only show three series. You can read more [here](https://sumproduct.com/blog/charts-and-dashboards-hiding-data-part-1/)
 and [here](https://sumproduct.com/blog/charts-and-dashboards-hiding-data-part-2/)
 for tips on how to hide data on chart.

Next, we change the **Series Name** column to be equal to the **Group** column. We can also use the **Group** column to draw a chart. However, the current chart is using the **Series Name** column (and I am lazy).

![](<Base64-Image-Removed>)

Then, right-click on the data labels and choose ‘Format Data Labels’. In the ‘Format Data Labels’ panel, under ‘Label Options’, tick ‘Value’ and choose ‘(New Line)’ as a Separator from the drop-down list.

![](<Base64-Image-Removed>)

We now have a donut chart which looks like the one below.

![](<Base64-Image-Removed>)

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-3/#0 "close")

top