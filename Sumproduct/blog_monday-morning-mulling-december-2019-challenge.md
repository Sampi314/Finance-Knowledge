# Monday Morning Mulling: December 2019 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: December 2019 Challenge

*   December 29, 2019

Monday Morning Mulling: December 2019 Challenge
===============================================

Monday Morning Mulling: December 2019 Challenge
===============================================

30 December 2019

_On the final Friday of each month, we set an Excel problem for you to puzzle over the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

To recap, the problem presented [last Friday](https://www.sumproduct.com/)
 was to create a single chart in Excel that would display the target amounts and have the actual amounts flow through like a bullet chart for each time period.

The challenge was to create a “Bullet Time Series chart” that looks something like this:

![](<Base64-Image-Removed>)

**  
Suggested Solution**

The first step is to format our data properly in a way that we can plot it on a chart in Excel. We will be using the following dataset in the current format:

![](<Base64-Image-Removed>)

With the data in hand, we can create the chart. As part of this solution we will be using the Custom Combination chart in Excel (we need to use this type of chart to generate a secondary axis):

![](<Base64-Image-Removed>)

Toggle all of the chart types to be “Clustered Columns”.

![](<Base64-Image-Removed>)

Then right-click on the chart and choose “Select Data…”, in the ‘Select Data Source’ dialog box, where we can switch the row / column.

![](<Base64-Image-Removed>)

The chart should look something like this now:

![](<Base64-Image-Removed>)

Notice that the **x**\-axis is labelled as 1, 2, 3, 4 and 5 when we want it to be 2014, 2015, 2016, and so on… Therefore, return to the ‘Select Data Source’ dialog and edit the horizontal ‘Axis Labels’:

![](<Base64-Image-Removed>)

Great; now we have our years in order.

![](<Base64-Image-Removed>)

The next step is to organise the columns into primary and secondary axes. Click on the chart, then click on the Design tab on the Ribbon, and then the ‘Change Chart Type’ option. This brings up the ‘Change Chart Type’ dialog, where we can assign different data series onto a secondary axis. In this case we will assign all of the Actual series to the secondary axis (this is because the secondary axis is displayed on top):

![](<Base64-Image-Removed>)

Remove the Year series from the chart. Then, we change adjust the format of the data series to make it appear like a bullet chart. We do this by changing the Series Overlap and Gap Width values in the Format Data Series panel. We adjust the ‘Gap Width’ of the budgeted series to 0%.

![](<Base64-Image-Removed>)

To format the primary axis data series, we set the ‘Series Overlap’ to -100% and ‘Gap Width’ to 100% (of course you can vary these settings to create a slightly different chart):

![](<Base64-Image-Removed>)

Our chart is starting to come together, at this point we have two things to deal with:

1.  The axes have different maximum amounts – this will cause confusion as our budget amounts are being compared to our actual amounts that are on different axes
2.  We do not have clear spacing between the years. This may make it difficult for end users to read the chart.

To deal with these two issues we can include new data series that will ‘control’ the maximum amount in the axis. We do this by using the **MAX** formula to retrieve the maximum amount from out data:

![](<Base64-Image-Removed>)

This will insert a new data series into the chart that will always have the maximum value from the dataset:

![](<Base64-Image-Removed>)

The two axes are now set to the same maximum amounts.

Format the two new data series with ‘No fill’, which essentially renders them invisible:

![](<Base64-Image-Removed>)

Two birds one bar… wait, was it stone? That would conclude it for our chart, if we did not care for colour. We should apply a different colour palette:

![](<Base64-Image-Removed>)

Of course, you do not have to pick these exact colours, but we’ve tried to pick a pallet that looks somewhat desirable. The final adjustments to the chart are:

1.  Delete the ‘Max Budget’ and ‘Max Actuals’ series from the legend
2.  Hide the secondary axis
3.  Give the chart a name.

![](<Base64-Image-Removed>)

Lastly, notice that the **x**\-axis years are slightly misaligned? There is one trick we can use to fix this. It involves creating a cell with several spaces ” “:

![](<Base64-Image-Removed>)

Now we adjust the cells containing our **x**\-axis values to:

![](<Base64-Image-Removed>)

This way we can adjust the total number of spaces we want to include to centre our year axis. Now the chart looks like this:

![](<Base64-Image-Removed>)

There we have it, did you come up with a better solution? Let us know at [contact@sumproduct.com](mailto:contact@sumproduct.com)
. In the meantime, here is the completed [file](https://sumproduct.com/assets/blog-pictures/2019/challenges-fff-mmm/dec-2019-mmm/final-friday-fix-dec-2019-solution.xlsm)
 for your reference.

_The Final Friday Fix will return on Friday 31st January 2020 with a new challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-december-2019-challenge/#0 "close")

top