# Charts and Dashboards: The Risk Bubble Chart – Part 1

**Source:** https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: The Risk Bubble Chart – Part 1

*   January 12, 2023

Charts and Dashboards: The Risk Bubble Chart – Part 1
=====================================================

Charts and Dashboards: The Risk Bubble Chart – Part 1
=====================================================

13 January 2023

_Welcome back to our Charts and Dashboards blog series. This week, we’re going to look at how to make a Risk Bubble chart._

_**The Risk Bubble Chart**_

![](<Base64-Image-Removed>)

Have you ever wanted to organise your risks and consequences based on the likelihood of occurrence and the potential damage? Today, we will introduce you to a Risk Bubble chart which helps you to keep track of the likelihood of any given problem, the consequences of the problem, and the size of said problem.

Here, this chart categorises types of risk in two dimensions, _i.e._ both the impact of the risk and the likelihood of it occurring. The size of the bubble shows how many categories meet the same criteria, but this could be replaced by a monetary value impact, the number of customers affected, _etc._ And yes, I do appreciate that using bubbles (circles) may not be the best way to depict the number of risk types due to the area of a circle being proportional to the square of its radius! The aim of this article is not to defend such practice, but to show how to create such a chart given they are used for risk assessment / analysis.

A key element of this chart is the risk input table, which is automatically updated based upon your input(s) and the Risk Bubble chart. To assist us, there are a few key inputs we will be using here. The first table we have is a table we shall name **LU\_Matrix** (_i.e._ the “**L**ook**U**p **Matrix**“), viz.

![](<Base64-Image-Removed>)

In this table, we will name the row headings (in grey) **LU\_Likelihood** and the column / field headings (also in grey) **LU\_Consequences**. With these inputs, we can create a risk table that changes colour automatically.

The next input we will need is the risk category table which determines the likelihood and consequence of a risk:

![](<Base64-Image-Removed>)

We name this table **Risk\_Category**.

In this table, we can enter the **Risk Category**, **Likelihood**, and **Consequence**. These inputs will be used to make the Risk Bubble chart, but we will need to refine this data for it to be usable.

With these inputs available, the question now is: how do we make the Risk Bubble chart? Well, let’s get started with the risk table…

**Risk Table**

The first step is to construct the axis for this chart. For this task, we will need to employ the **COUNTA**, the **SEQUENCE**,and the **INDEX** functions. **COUNTA** as you guessed will “count” every cell that is not blank. Therefore, we will count the number of **Likelihood** categories:

**\=COUNTA(LU\_Likelihood)**

The output for this function will be five \[5\] as we have five \[5\] **Likelihood** categories in our example. As we generate a sequence of numbers, we will wrap up the **COUNTA** formula inside the **SEQUENCE** function**:**

**\=SEQUENCE(COUNTA(LU\_Likelihood))**

This will generate an array from one \[1\] to five \[5\]:

![](<Base64-Image-Removed>)

However, we want this array to generate in reverse order, _i.e._, five \[5\] to one \[1\]. This can be achieved by setting the third argument of the **SEQUENCE** function to our number of **Likelihood** categories and the fourth argument to negative one \[-1\]:

**\=SEQUENCE(COUNTA(LU\_Likelihood),,COUNTA(LU\_Likelihood),-1)**

The third argument of the **SEQUENCE** function will specify the starting value and the fourth argument will specify the increment for each subsequent value. This will give us the following:

![](<Base64-Image-Removed>)

(If dynamic arrays are not available, alternative formulae can generate the same desired result).

Finally, we apply our **INDEX** function here to make the **y**\-axis (vertical, or dependent, axis) of the chart:

**\=INDEX(LU\_Likelihood,SEQUENCE(COUNTA(LU\_Likelihood),,COUNTA(LU\_Likelihood),-1))**

The **INDEX** function will take the fifth item of the **LU\_Likelihood** and put it on the top row, the fourth item put on the second row, and we repeat this process until we have the first item in the fifth row:

![](<Base64-Image-Removed>)

Then, we will go one cell below and one cell to the right of the word “Rare” here to enter our second, much simpler, formula:

**\=LU\_Consequences**

After entering the formula in that cell (again, assuming you have [Dynamic Arrays](https://www.sumproduct.com/news/article/dynamic-arrays-gradually-rolling-out-on-monthly-channel)
 in your version of Excel), we will have the following visual:

![](<Base64-Image-Removed>)

Next, we apply some formatting:

![](<Base64-Image-Removed>)

We have formatted each of the **Likelihood** and **Consequence** values to make them look more like headings, whilst rotating the text in the **y**\-axis. We have also resized all cells within the graph area to dimensions of 100×100 pixels (a column width of 13.57 and a row height of 75).

Assuming the grid is positioned as in the graphic (_above_), in cell **L89**, we will enter the following formula, and then copy this throughout the entire table:

**\=INDEX(LU\_Matrix\[\[Minimal\]:\[Catastrophic\]\], MATCH($K89,LU\_Likelihood,0),  
MATCH(L$94,LU\_Consequences, 0))**

These **MATCH** functions will match the row position of the item on the left of the **LU\_Matrix** and the column position of the item on the bottom of the **LU\_Matrix**. Then the **INDEX** function will return the item in the exact row and column that we match on the **LU\_Matrix**. After entering the formula and populating the table we will have the following visual:

![](<Base64-Image-Removed>)

With the headings and shape of the chart in place, let’s take a break. Next week, we’ll look at making this a little more colourful.

_That’s it for this week, come back next week for more Charts and Dashboards tips._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-the-risk-bubble-chart-part-1/#0 "close")

top