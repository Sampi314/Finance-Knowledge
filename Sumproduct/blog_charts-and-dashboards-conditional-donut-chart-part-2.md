# Charts and Dashboards: Conditional Donut Chart – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Conditional Donut Chart – Part 2

*   March 18, 2021

Charts and Dashboards: Conditional Donut Chart – Part 2
=======================================================

Charts and Dashboards: Conditional Donut Chart – Part 2
=======================================================

19 March 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we will continue to build the “conditional donut chart”._

[Last week](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-1/)
, from the group rating data and the transformed chart data table (as shown below),

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-232.jpg)

we created an initial donut chart:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-294.jpg)

We deliberately included 15 series in the chart, although there will be only three \[3\] series that are visible. We will need to format the series so that each of the series indicating the same rating will be displayed with the same colour, _e.g._ the three series Group 1-1, Group 2-1 and Group 3-1 have a rating 1 and should share the same colour scheme.

To make it clear, we have an example chart like the one below, where we have different items with different values plotted with different colours on the chart.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-237.jpg)

If we get all items with the same value, only the size of their portions on the donut chart changes, not the colour.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-224.jpg)

However, what we are aiming to do here is that if all items share the same value, they will be plotted with the same colour on the chart and the colour depends on their value, _e.g._ green for value of five \[5\]

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-187.jpg)

and orange for value of one \[1\]

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-166.jpg)

or a mixture of values as shown below.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-151.jpg)

The process of getting the colours for the above chart is manual. Let’s make things automatic.

To do this, first, we replace the **Chart Data** series with the **Rating** number:

![](<Base64-Image-Removed>)

The donut chart will now look like the one below, which makes it easier to tell between the series.

![](<Base64-Image-Removed>)

Now, click twice on the series (not double-click) to select the series we need to format, then right-click and choose the colour to our liking from the Fill drop-down. Otherwise, we can select ‘Format Data Point…’ for detailed formatting options. Here, we defined the lowest rating as red shade and highest rating as green shade.

![](<Base64-Image-Removed>)

When we are finished with the colour formatting, the chart should resemble something similar to the one below:

![](<Base64-Image-Removed>)

By reverting the **Chart Data** series to the initial formula

**\=IF(SUMIFS(Group\_Point\[Rating\],Group\_Point\[Group\],\[@Group\])=\[@Rating\],\[@Rating\],0)**

we will get the donut chart with the conditional colouring.

![](<Base64-Image-Removed>)

If we change the group rating as two, two and five for Group 1, 2 and 3 respectively, our donut chart will show the same colour for the rating as two points for Group 1 and 2.

![](<Base64-Image-Removed>)

As we already removed the legend (we do not need fifteen!), we will need another legend or data label for our chart, which we will save for the next part.

That’s it for this week. Come back next week for more charts and dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-conditional-donut-chart-part-2/#0 "close")

top