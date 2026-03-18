# Charts and Dashboards: Bullet Charts – Part 1

**Source:** https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Bullet Charts – Part 1

*   February 11, 2021

Charts and Dashboards: Bullet Charts – Part 1
=============================================

Charts and Dashboards: Bullet Charts – Part 1
=============================================

12 February 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we begin a review of Bullet Charts._

A few weeks ago, we talked about [how to create Multiple Bullet Charts](https://sumproduct.com/blog/charts-and-dashboards-multiple-bullet-charts-part-1/)
, and [how to format them](https://sumproduct.com/blog/charts-and-dashboards-multiple-bullet-charts-part-2/)
. Over the next few weeks, we will consider how to create and format a _single_ bullet chart.

Bullet charts (sometime known as Thermometer Charts) are very useful visualisations to show how a variable is on track with a target and accepted lower / upper bounds, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-250.jpg)

We can break down the bullet chart into four digestible elements:

1.  We need the bar that indicates the actual performance measure (indicated by the blue bar)
2.  We need two other bars that will indicate unsatisfactory, satisfactory and good performance(s) (indicated by the shaded areas)
3.  We need a target (indicated by the black bar at the 6,000 mark in this illustration)
4.  As an added bonus, we will be including conditional formatting into the bullet chart.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-315.jpg)

To aid in with the conditional formatting aspect, we need the following inputs for this build:

*   **MaxPoor**: the maximum ‘poor’ value
*   **MaxSat**: the maximum ‘satisfactory’ value
*   **Actual:** the actual amount
*   **Target:** the target value.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-256.jpg)

We will assign the following range names to the cells:

*   **H10** \= MaxPoor (Maximum poor performance threshold)
*   **H11** = MaxSat (Maximum satisfactory performance threshold)
*   **H12** \= Target
*   **H14** = Actual

The next two inputs we need are the target value again and the target category:

![](<Base64-Image-Removed>)

The ‘Target Value’ (cell **H18**) should refer to the ‘Target’ range name we set up earlier. Therefore, the formula in this cell should be:

**\=Target**

The Target Category should be an input, in this case 2, whereas the Target Value indicates the ‘X’ value of the target and the Target Category centres the bar.

There will be three rows to that will serve as the chart data, the repeated Graduations row is intentional:

1.  Graduations
2.  Actual
3.  Graduations

![](<Base64-Image-Removed>)

The formulae in the table are as follows:

**H24:J24 = 0**

**H25 = IF(Actual < MaxPoor, Actual, NA() )**

**H26:J26 = 0**

**I25 = IF(AND(Actual >= MaxPoor, Actual < MaxSat), Actual , NA() )**

**J25 = IF(Actual >= MaxSat, Actual, NA() )**

**K24 and K26 = MaxPoor**

**K25 = MAX(MaxPoor – MAX (0, Actual), 0)**

**L25 = MAX(MIN(MaxSat – MaxPoor, MaxSat – Actual), 0)**

**L24 & L26 = MAX(MaxSat – MaxPoor, 0)**

We will select our chart data from **H24:L26** (this will be one of the few times we allow for _#N/A_ errors, as they are needed for conditional bar colours):

![](<Base64-Image-Removed>)

Go to **Insert -> Charts -> Recommended Charts -> Stacked Bar Chart**:

![](<Base64-Image-Removed>)

If your initial chart looks like this:

![](<Base64-Image-Removed>)

This needs modifying, but more on that next time.

Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-bullet-charts-part-1/#0 "close")

top