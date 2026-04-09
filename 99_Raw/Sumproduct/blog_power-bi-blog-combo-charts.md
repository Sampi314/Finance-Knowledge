# Power BI Blog: Combo Charts

**Source:** https://sumproduct.com/blog/power-bi-blog-combo-charts/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Combo Charts

*   January 8, 2020

Power BI Blog: Combo Charts
===========================

Power BI Blog: Combo Charts
===========================

9 January 2020

_Welcome back to this week’s Power BI blog series. This week, we are going to look at how to create combo charts (Line and Clustered Column charts)._

Again, we are going to use the data set we have now used for several blogs (image is incomplete):

![](<Base64-Image-Removed>)

We previously created measures to calculate the **Total Cost**, **Total Sales** and **Profit**. What if we want to now create a new measure to calculate the Profit Margin and have it displayed on a Line and Clustered Column chart?

As mentioned before, in our [previous blog](https://sumproduct.com/blog/power-bi-blog-presenting-several-measures-on-a-single-visualisation/)
, we created the **Total Costs**, **Total Sales** and **Profit** measures. We may use two of these measures to help us create the **Profit Margin** measure, _viz._

Profit Margin = \[**Profit**\]/**\[Total Sales**\]

Remember to format the measure as a percentage with the appropriate number of decimals:

![](<Base64-Image-Removed>)

The next step is to create the ‘Line and Stacked bar’ chart:

![](<Base64-Image-Removed>)

Drag the **Total Sales** measure into the ‘Column values’ area, and the **Date** from the Calendar table to the ‘Shared axis’ area:

![](<Base64-Image-Removed>)

Drill down through the visualisation using the dual arrows pointing down icon in the top right corner of the visualisation:

![](<Base64-Image-Removed>)

Now add the **Profit Margin** measure into the ‘Line values’ area:

![](<Base64-Image-Removed>)

Notice that the Y-Axis scale for the percentage’s ranges from 62.5% to 64.5%? Power BI defaulted to that range to best illustrate the changes between each period although it may be a little misleading. If we wanted to change the Y-Axis scale, it can be adjusted in the Format tab:

![](<Base64-Image-Removed>)

The trick here is to keep scrolling down until we can see the options to adjust the Y-Axis (Line). We can then change the starting and ending values of the axis to suit our needs:

![](<Base64-Image-Removed>)

We’ve elected to set the range of the Y-Axis to start at 0% and end at 100%.

![](<Base64-Image-Removed>)

Next up is to fix up the chart title:

![](<Base64-Image-Removed>)

We can also add other fields into the Column values area such as the **Total Costs**:

![](<Base64-Image-Removed>)

We can see that data headers are ‘on’ for the **Total Costs** measure. We can change this by going to the **Format tab -> Data labels**, scroll down and toggle the ‘Customize series’ option to ‘on’:

![](<Base64-Image-Removed>)

Then, toggle not to show the Data labels for the **Total Costs** measure:

![](<Base64-Image-Removed>)

There we have it, how to create a simple Line and clustered column chart.

That’s it for this week, come back next week for more Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-combo-charts/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-combo-charts/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-combo-charts/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-combo-charts/#0)

[](https://sumproduct.com/blog/power-bi-blog-combo-charts/#0 "close")

top