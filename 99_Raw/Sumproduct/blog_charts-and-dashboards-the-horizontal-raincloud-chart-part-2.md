# Charts and Dashboards: The Horizontal Raincloud Chart – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: The Horizontal Raincloud Chart – Part 2

*   November 9, 2023

Charts and Dashboards: The Horizontal Raincloud Chart – Part 2
==============================================================

Charts and Dashboards: The Horizontal Raincloud Chart – Part 2
==============================================================

10 November 2023

_Welcome back to our Charts and Dashboards blog series. This week, we continue to show you how to make a bespoke Horizontal Raincloud chart, by creating a Stacked Column chart to show the percentile analysis._

_**The Horizontal Raincloud chart**_

Are you looking for a new way to present your data? This week, we continue looking at the Horizontal Raincloud chart. If you are unfamiliar with this concept, the Horizontal Raincloud chart might look like the following image:

![](<Base64-Image-Removed>)

You can download the starting Excel file [here](https://www.sumproduct.com/assets/blog-pictures/2022/cd/154/sp-horizontal-raincloud-chart---initial.xlsm)
 to build this chart with us.

Our Excel file contains two \[2\] workings sheets, one named ‘Horizontal Raincloud – 1 Cloud’ and the other ‘Horizontal Raincloud – 3 Clouds’. We will illustrate our example in the ‘Horizontal Raincloud – 1 Cloud’ sheet.

Let’s break down the charts we used here to make this design:

*   a Scatter chart for our data point distribution
*   a Stacked bar chart for percentile analysis
*   a Scatter chart for our error bar.

We will illustrate how to construct each of these charts and later merge them together to create the Horizontal Raincloud chart.

[Last week](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-1/)
, we created a Scatter chart for our data point distribution:

![](<Base64-Image-Removed>)

This week, we create a Stacked Column chart to show the percentile analysis. To create this chart, we will use the following two \[2\] tables:

![](<Base64-Image-Removed>)

The top table is called **Percentile**\_**Table** and the bottom table is called **Stacked\_Bar**. In the **Percentile**\_**Table**, we will enter the following formula in the ‘**Percentile:****Cloud 1**‘ column to return the percentiles of the data:

**\=PERCENTILE(Cloud\[Cloud 1\], \[@Percentile\])**

This will return the percentile values for 0%, 10%, 25%, 50%, 75%, 90% and 100% of our data in Cloud 1. Next, we will be using this table to calculate the **Stacked\_Bar** table:

*   for the ‘Base 25th‘ row, it will be equal to the 25th percentile of **Percentile\_Table**
*   for the ‘Bottom 25-50’ row, it will be equal to the 50th percentile less the 25th percentile from the **Percentile\_Table**
*   for the ‘Top 50-75’ row, it will be equal to the 75th percentile less the 50th percentile from the **Percentile\_Table**.

We will have the following table after we have finished our calculations:

![](<Base64-Image-Removed>)

Before plotting this, we will add two \[2\] dummy columns in the **Stacked\_Bar** table. This will help our ‘Scatter chart for our data point distribution’ components by having more space for the plot. Another reason why we add dummy columns is that the Stacked Bar graph and Scatter graph do not share the primary axis like the Stacked Column graph and Scatter graph. Hence, scaling the axis to make every component fall into the correct position will be a nightmare without the help of the dummy column. Thus, we will have the following table for the **Stacked\_Bar:**

![](<Base64-Image-Removed>)

We select whole **Stacked\_Bar** table and we go to the **Insert -> Charts -> 2-D Column -> Stacked Bar**.

![](<Base64-Image-Removed>)

After selecting that we will have the following visual:

![](<Base64-Image-Removed>)

This is where this week’s instalment ends, next time we will create a Scatter chart (of sorts) for our error bar.

_That’s it for this week, come back next week for more Charts and Dashboards tips._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-the-horizontal-raincloud-chart-part-2/#0 "close")

top