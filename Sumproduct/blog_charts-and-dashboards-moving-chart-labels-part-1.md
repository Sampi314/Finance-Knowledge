# Charts and Dashboards: Moving Chart Labels – Part 1

**Source:** https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Moving Chart Labels – Part 1

*   April 22, 2021

Charts and Dashboards: Moving Chart Labels – Part 1
===================================================

Charts and Dashboards: Moving Chart Labels – Part 1
===================================================

23 April 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we will talk about creating a chart label that can move._

Chart labelling is an interesting topic. We have previously talked about the [Dynamic Chart Labels](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/)
 and played around with the [Dynamic Chart Labels for Stacked Column Charts](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/)
. Over the next two blogs, we want to discuss more tips concerning creating a chart label that can move along with its associated data series.

For example, imagine we have data for actual and budget sales for a given financial year. Actual data will be filled in at the close of each month, _e.g._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-212.jpg)

We want to create a line chart to illustrate the sales performance against the budget data. We will not need the legend for the chart, as we wish to place the labels next to the end point of each series, which move depending upon the data we input, as illustrated below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-272.jpg)

First, to create a chart, select the range **F12:H24** and navigate to the Insert tab on the Ribbon, and then select a line chart. The initial line chart will look like the one below:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-216.jpg)

We will undertake some formatting at this point. First, we will extract the [dynamic chart title](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-titles/)
 by pointing it to cell **D10**. Then, we will remove the gridlines from the chart area and emphasise the border line for the two axes. You can read more about formatting the line chart [here](https://sumproduct.com/blog/charts-and-dashboards-line-charts/)
. The chart now appears like below:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-203.jpg)

To get the series chart label for only the end point of a series, click on the series, then click once again on the data point we want to add the label on, right-click and choose ‘Add Data Label’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-172.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-151.jpg)

As the label stays too close to the chart border, we will resize the plot area.

![](<Base64-Image-Removed>)

To change the chart label to the series name instead of the data value, right-click on the data point (**not** the label) and select ‘Format Data Label’. In the ‘Format Data Label’ pane, under ‘Label Options’, tick ‘Series Name’.

![](<Base64-Image-Removed>)

The chart will now look like the one below:

![](<Base64-Image-Removed>)

If we change the budget data, the label is moving with the chart series.

![](<Base64-Image-Removed>)

We will repeat the same process to get the label for the Actual series.

![](<Base64-Image-Removed>)

However, when we add more data to the chart, the label is not moving and is overwritten by the series line.

![](<Base64-Image-Removed>)

This is because we are adding data label for a single point in the series, so the data label is not dynamic yet. Of course, we can find a way to fix this, but that’s for next time…

That’s it for this week. Come back in a fortnight for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/#0 "close")

top