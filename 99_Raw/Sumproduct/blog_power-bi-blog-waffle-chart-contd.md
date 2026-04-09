# Power BI Blog: Waffle Chart (cont’d)

**Source:** https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Waffle Chart (cont’d)

*   July 3, 2019

Power BI Blog: Waffle Chart (cont’d)
====================================

Power BI Blog: Waffle Chart (cont’d)
====================================

4 July 2019

_Welcome back to this week’s Power BI blog series! This week, we’ll continue to have more fun playing with amazing visual effects of Waffle Chart._

Last week, I introduced a cool Power Bi’s custom visual: [Waffle Chart](https://sumproduct.com/blog/power-bi-blog-waffle-chart/)
. Waffle Chart presents proportional data in a 10×10 dimension, which allows easier visualisation and comparison of small percentages. I also created a beautiful chart of my Course Registration in March 2019:

![](https://sumproduct.com/wp-content/uploads/2025/05/22c6daeb82d7d69ac88f878227e04b28-89-1.jpg)

Aren’t the dots too boring? Knowing that, the developer also allows more visual effects to Waffle Chart by applying SVG Path for various colours and shapes.

I’ve found an easy way: I use [https://thenounproject.com/](https://thenounproject.com/)
 to search for an icon depending on my topic of presentation, next I save the icon as SVG file, and then I go to [https://kiewic.com/paths/](https://kiewic.com/paths/)
 to convert the SVG icon file into a usable path.

Here after getting the path for icons related to my courses, I put them in another column called “Avatar” in my Excel’s KPI table for each course, and I load it back to Power BI.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-401.jpg)

Then in Report view, I drag “Avatar” to the **Paths** field, and I choose colours for the corresponding courses in **Visual\_DataPoint**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-414.jpg)

And now each of the courses all has different icons and colours, which makes the visual more interesting.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-389.jpg)

But wait, I need one more step since I wish to put the course registration performance in a proper order. I mouse over the chart, then I click the three-dotted icon at the top left-hand side and choose ‘Sort descending’ and ‘Sort by’ – “Count of Registration”.

It’s worth noting here that the course KPIs are not equal, and the visuals are sorted by the number of registrations, not the KPI percentage. So, while Excel’s performance compared to KPI is only 53%, which is less than Power Pivot’s 70%, because there are more registrations in the Excel course than in the Power Pivot course, Excel is being reported in front of Power Pivot in the visualisation.

![](<Base64-Image-Removed>)

To make the chart and figures more transparent, I add a few tables to the dashboard and rescale the Waffle Chart area.

Finally, it’s neat!

![](<Base64-Image-Removed>)

That’s it for Waffle Chart, have fun drawing your chart.

Stay tuned for the next blog in the Power BI series. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/#0)

[](https://sumproduct.com/blog/power-bi-blog-waffle-chart-contd/#0 "close")

top