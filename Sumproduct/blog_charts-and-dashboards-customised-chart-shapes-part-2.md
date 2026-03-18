# Charts and Dashboards: Customised Chart Shapes – Part 2

**Source:** https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/

---

[Home](https://sumproduct.com/)

\> Charts and Dashboards: Customised Chart Shapes – Part 2

*   January 21, 2021

Charts and Dashboards: Customised Chart Shapes – Part 2
=======================================================

Charts and Dashboards: Customised Chart Shapes – Part 2
=======================================================

22 January 2021

_Welcome back to this week’s Charts and Dashboards blog series. This week, we continue to talk about customising chart shapes._

[Last week](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-1/)
, we created a column chart with a customised chart shape like the one below. Currently, the shapes do not look nice. The higher the sales, the more the shape stretches and the pointier the roof is. This week, we will continue editing this chart to give it a better look.

![](<Base64-Image-Removed>)

To do this, we need to separate the column into two parts, say **Roof** and **Floor**, in which the **Roof** parts are all equal to prevent the above stretch.

![](<Base64-Image-Removed>)

The **Roof** part should be formula-driven rather than a fix number. In this case, we will get the minimum sales of twelve months and divided it by two (2) since we have two parts (otherwise, the house will only have a roof without a floor!). The formula in cell **C2** is

**\=MIN($B$2:$B$13)/2**

and the **Floor** part, cell **D2**, equals **B2-C2**.

Now that we have the data, we will create a stacked column chart based on the two separated parts, we will have an initial chart like the one below.

![](<Base64-Image-Removed>)

We will copy the roof shape to the **Roof** series similarly to how we did [last week](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-1/)
.

![](<Base64-Image-Removed>)

Next, we will paint the **Floor** series the same colour as the **Roof**, reduce the Gap width between the columns and get the [dynamic chart title](https://sumproduct.com/blog/charts-and-dashboards-dynamic-chart-titles/)
 pointing to cell **B1**. The chart looks better now.

![](<Base64-Image-Removed>)

That’s it for this week. Check back next week for more Charts and Dashboards tips.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/#0)

[](https://sumproduct.com/blog/charts-and-dashboards-customised-chart-shapes-part-2/#0 "close")

top