# Charts and Dashboards: Moving Chart Labels – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Moving Chart Labels – Part 2

*   May 6, 2021

Charts and Dashboards: Moving Chart Labels – Part 2
===================================================

Charts and Dashboards: Moving Chart Labels – Part 2
===================================================

7 May 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we will continue to discuss about the moving chart labels._

In [Part 1](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-1/)
, we took actual and budget sales data in a financial year,

![](<Base64-Image-Removed>)

to create a line chart. We then added the data labels to the end points of each chart series, _viz._

![](<Base64-Image-Removed>)

However, when we added more data to the chart, the labels were not moving and were overwritten by their respective series lines, because we had been adding data labels for a single point in each series. In summary, the data labels were not dynamic _yet_.

![](<Base64-Image-Removed>)

Guess what we are going to do this week!

To fix this, we will need a helper series which plots only the last actual data point. In cells **I13:I24**, we will add a series call ‘Actual’ – which will be used as the label later – and use the formula as shown below to get only the last actual data point. We will also need to rename the existing ‘Actual’ series to ‘Actual Data’ to distinguish with the new series. All other data point with _#N/A_ errors will be hidden. The _#N/A_ errors are deliberate, as they prevent the points being plotted on a line chart. You can read more about hiding chart data [here](https://sumproduct.com/blog/charts-and-dashboards-hiding-data-part-1/)
 and [here](https://sumproduct.com/blog/charts-and-dashboards-hiding-data-part-2/)
. We have used the formula

**\=IF(MATCH(F13,$F$13:$F$24,0)=COUNTA($G$13:$G$24),G13,NA())**

![](<Base64-Image-Removed>)

Next, let’s remove the ‘Actual’ data label, and then right-click on the chart area and choose ‘Select Data…’:

![](<Base64-Image-Removed>)

In the ‘Select Data Source’ dialog, under ‘Legend Entries (Series)’, click Add.

![](<Base64-Image-Removed>)

Select cell **I12** to be the Series name and cells **I13:I24** to be the Series values and click OK.

![](<Base64-Image-Removed>)

The chart now looks like the one below. A new ‘Actual’ series is added, with only one data point overlapped by the ‘Actual Data’ series (making it difficult, if not impossible, to see).

![](<Base64-Image-Removed>)

To format the Actual series only, right-click on the chart and select ‘Format Data Series’. In the ‘Format Data Series’ panel, under ‘Series Options’, choose ‘Series “Actual”‘.

![](<Base64-Image-Removed>)

The data point is highlighted, right-click on it and choose ‘Add Data Label’.

![](<Base64-Image-Removed>)

Again, right-click on the label, select ‘Format Data Label’ and tick ‘Series Name’.

![](<Base64-Image-Removed>)

We won’t need the legend, hence, click on it and hit Delete. We may also need to resize the plot area. The chart now looks like this:

![](<Base64-Image-Removed>)

Now, if we add more actual data, the chart title changes and the label moves along with the series!

![](<Base64-Image-Removed>)

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-moving-chart-labels-part-2/#0 "close")

top