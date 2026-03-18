# Charts and Dashboards: Vertical Raincloud Chart Part 1

**Source:** https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Vertical Raincloud Chart Part 1

*   December 8, 2022

Charts and Dashboards: Vertical Raincloud Chart Part 1
======================================================

Charts and Dashboards: Vertical Raincloud Chart Part 1
======================================================

9 December 2022

_Welcome back to our Charts and Dashboards blog series. This week, we’re going to look at how to make a bespoke Vertical Raincloud chart by creating the first of three charts that we will need._

**The Vertical Raincloud chart**

Are you looking for a new way to present your data? Meet the Vertical Raincloud chart:

![](https://sumproduct.com/wp-content/uploads/2025/05/4e0286bfa67c9c45a5f1704b426e4fdb.jpg)

This chart shows three \[3\] clouds. We will start by showing how to create a chart for just one cloud.

We will need to combine three \[3\] charts:

*   a Scatter chart for our data point distribution
*   a Stacked Column chart for percentile analysis
*   a Scatter chart for our error bar.

We will illustrate how to construct each of these charts and later merge them together to create the Vertical Raincloud chart. This week, we look at the Scatter chart for our data point distribution.

**Scatter chart for our data point distribution**

Our aim here is to transform the single data column **Cloud 1** in the **Cloud** table into a chart showing the distribution of data points like this:

![](<Base64-Image-Removed>)

In order to do that we will add three \[3\] more columns to the **Cloud** table.

The first column that we add, will be called **Cloud 1: 1st Position**, this column will count the appearance of the data points accumulated from the top row to the bottom row. Hence, we will use this formula to get that result:

**\=COUNTIF($D$10:D10, D10)**

This formula will count the first appearance of the number in the column as one \[1\]. If the data appears a second time in the row below the row where it first appears, at that row the formula will return two \[2\] and so on. Since we are adding a column to an Excel Table, the other values in the column are either populated automatically or can be dragged down depending on the settings:

![](<Base64-Image-Removed>)

The cells **J9:K10** indicate the location of the data and the length of the data point.

![](<Base64-Image-Removed>)

We need to create a column to track the **x**position of the data points that we have which we call **Cloud 1: X-position**. In the first row of this column, we use the formula:

**\=IF(E10=1,$K$9,F9+$K$10)**

where:

*   **E10** is the first cell of column **Cloud 1: 1st Position**
*   **$K$9** isthe input cell for the location of data (in this example, we will set it as 1.5)
*   **F9** is the cell above the formula cell
*   **$K$10** is the input cell for the length of the data (in this example, we will set it as 0.1).

The last column we add is just a copy of the first column we have. The reason we must duplicate this column is that Scatter Plot is strict about the position of the column. If we simply just select the ‘**Cloud 1: Distribution**‘ column first and hold **CTRL** and select the **Cloud 1** column and insert the scatter graph, it will create the following visual:

![](<Base64-Image-Removed>)

This is not what we wanted for this chart as we need the data in the ‘**Cloud 1: X-position**‘ column on the **x**\-axis and the data in the ‘**Cloud 1**‘ column on the **y**\-axis.

Instead, we duplicate the ‘**Cloud 1**‘ column to the right of the ‘**Cloud 1: X-position**‘. We name this column ‘**Cloud 1: Distribution**‘. Then, we will select two \[2\] columns which are ‘**Cloud 1: X-position**‘ and ‘**Cloud 1: Distribution**‘ and select **Insert -> Charts -> Scatter -> Scatter**.

![](<Base64-Image-Removed>)

This will provide the Scatter chart that we need, resulting in the following visual:

![](<Base64-Image-Removed>)

That’s where we’ll leave it for this week, next week we’ll create the Stacked Column chart for percentile analysis.

_That’s it for this week, come back next week for more Charts and Dashboards tips._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-vertical-raincloud-chart-part-1/#0 "close")

top