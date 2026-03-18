# Charts and Dashboards: Pareto Power

**Source:** https://sumproduct.com/blog/charts-and-dashboards-pareto-power/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Pareto Power

*   August 19, 2021

Charts and Dashboards: Pareto Power
===================================

Charts and Dashboards: Pareto Power
===================================

20 August 2021

_Welcome back to our Charts and Dashboards blog series. This week, I make my manually created Pareto chart interactive_

In [Problem Solving with Pareto Charts](https://sumproduct.com/blog/charts-and-dashboards-problem-solving-with-pareto-charts/)
, I was analysing some complaint data for our Tent Hire business.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-144.jpg)

I wanted to create a Pareto chart, so that I could quickly identify which issues to look at in order to significantly reduce the **Number of Reports**. I did this by creating a combination of a Column Chart and a Line Chart, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-192.jpg)

I can improve this, to allow the user to specify a percentage of complaints to resolve, and then highlight the problems that need to be solved in order to reach that percentage.

In order to do this, I start with the data that I created for [Problem Solving with Pareto Charts](https://sumproduct.com/blog/charts-and-dashboards-problem-solving-with-pareto-charts/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-156.jpg)

I plan to use a Scroll Bar to allow the user to change the percentage of reports to be resolved. To insert a Scroll Bar, I go to the Developer tab and choose the ‘Scroll Bar’ icon from the ‘Form Controls’ part of the Insert section (beware the classic “gotcha” selecting the ActiveX control instead).

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-151.jpg)

Having placed the Scroll Bar where I want it, I can right click and choose ‘Format Control’.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-123.jpg)

I plan to link the Scroll Bar to a cell which I call **Scroll Value**. This will also link to another cell, styled as a percentage, which I call **Target Value**. In the ‘Format Control’ dialog, I take the default minimum, maximum and increments.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-108.jpg)

I also link the scroll bar to my **Scroll Value** cell. The formula I use for **Target Value** is:

**\= I11/100**

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-99.jpg)

I need one more value to highlight the correct bars: I need to know which value from the **Cumulative %** column will meet the required target. I create another cell which I give the title **Cumulative Value**.

![](<Base64-Image-Removed>)

The formula for **Cumulative Value** is:

**\=IFERROR(INDEX($C$2:$C$8,IFERROR(MATCH($I$11,$C$2:$C$8,1),0)+1),1)**

This will give me the bar that will solve enough complaints to meet or exceed the **Target Value**.

If **Target Value** is 21%, then I would just need to solve my ‘Late Delivery’ problems, which would resolve 35.71% of the reports.

Next, I create two new columns on my table to indicate which bars will be less than the target, and which will be more.

![](<Base64-Image-Removed>)

**Below Target** has the formula:

**\=IF($I$11>=C2,B2,NA())**

**Above Target** has the formula:

**\=IF($I$11<C2,B2,NA())**

Now I am ready to construct the chart. I select the data in my table, and on the Insert tab I choose to insert a Clustered column chart.

![](<Base64-Image-Removed>)

Having positioned the chart above the Scroll Bar, I can right click on any bar to ‘Change Series Chart Type’.

![](<Base64-Image-Removed>)

Choosing a Combo Chart, I change the **Cumulative %** to a Line on a Secondary Axis.

![](<Base64-Image-Removed>)

I don’t need to show the **Number of Reports**, so I right click and delete this data series. I also right click on the **Below Target** and **Above Target** bars and change their colour to red and grey respectively.

![](<Base64-Image-Removed>)

Now when I move the Scroll Bar left and right, the number of red bars increases and decreases to show me which problems must be solved to meet the **Target Value**.

That’s it for this week. Come back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-pareto-power/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-pareto-power/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-pareto-power/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-pareto-power/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-pareto-power/#0 "close")

top