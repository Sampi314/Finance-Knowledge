# Charts and Dashboards: Dynamic Chart Labels for Stacked Column Charts

**Source:** https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Dynamic Chart Labels for Stacked Column Charts

*   February 4, 2021

Charts and Dashboards: Dynamic Chart Labels for Stacked Column Charts
=====================================================================

Charts and Dashboards: Dynamic Chart Labels for Stacked Column Charts
=====================================================================

5 February 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we continue to talk about customising chart shapes._

In the past few weeks, we have talked about [customising chart shapes](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-1/)
 and [formatting tips](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/)
, where we created a chart for house sales with the house-shaped columns like the one below:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-253.jpg)

The chart is actually a stacked column chart and we left the vertical axis in place. Now, we want the data labels representing sales to be displayed on top of each column. However, when we remove the vertical axis and gridlines and add data labels to the chart, since it is a stacked column chart with two data series, we get two series of data labels.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-318.jpg)

Unlike the column chart options where we can add data labels at the outside end of the column, in the stacked column chart, we need a few tweaks to get this done:

*   we will need a helper data series to top the stack chart, say ‘Label series’, whose values are equal to the **Roof** series
*   right-click on the chart and choose ‘Select data’ and add this series to the chart
*   right-click on the top series and choose ‘Format Data Series’ in the ‘Series Options’
*   let the Fill be ‘No fill’ and Border be ‘No line’ to make this series invisible
*   to delete unnecessary series of data labels, just click on a label of the series and hit Delete.

Now we have brought the data labels to the top of the columns.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-259.jpg)

To get the data labels to point to the house sales instead of the helper stack data, we will use [dynamic chart labels](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels/)
. By clicking on one of the labels, on the ‘Format Data Labels’ panel, under the ‘Label Options’, uncheck ‘Value’ and check ‘Value From Cells’ instead.

![](<Base64-Image-Removed>)

In the ‘Data Label Range’ dialog that occurs, point the range to the house sales, which is the range **B2:B13**. The chart is now complete.

![](<Base64-Image-Removed>)

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-labels-for-stacked-column-charts/#0 "close")

top