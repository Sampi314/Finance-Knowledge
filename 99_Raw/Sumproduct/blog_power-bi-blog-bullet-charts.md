# Power BI Blog: Bullet Charts

**Source:** https://sumproduct.com/blog/power-bi-blog-bullet-charts/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Bullet Charts

*   January 15, 2020

Power BI Blog: Bullet Charts
============================

Power BI Blog: Bullet Charts
============================

16 January 2020

_Welcome back to this week’s Power BI blog series. This week, we are going to look at bullet charts._

Say that we’ve finally got the monthly budget sales targets for the previous years and we want to plot our performance on a bullet chart. Well, this week, we are going to look at a custom visual called Bullet Chart 2.0.1 (correct at the time of writing). It may be found on the Microsoft Marketplace and downloaded for free:

![](<Base64-Image-Removed>)

We can load the following monthly budget data into Power BI (this screenshot is not exhaustive):

![](<Base64-Image-Removed>)

After loading the data into Power BI, assuming that this is a new table, we have to create a relationship with the current dataset:

![](<Base64-Image-Removed>)

The next step is to create a measure that will summarise the budget amounts:

Budget = **Sum**(Projections\[Budget\])

We can now drag the **Budget** and **Actuals** measures into the visualisation:

![](<Base64-Image-Removed>)

We then turned Category off and we centrally align the title:

![](<Base64-Image-Removed>)

The next thing we can do is insert colour coded zones through the Data Values section in the Format tab:

![](<Base64-Image-Removed>)

We have elected to put the following percentages to colour code the visualisation:

![](<Base64-Image-Removed>)

You should note that to have additional space at the right end of the bullet chart, we can add a percentage **greater** than 100 in the Maximum % area.

If the colour palette doesn’t agree with your palate, we can change the colours in the Colors area too:

![](<Base64-Image-Removed>)

The bullet chart also responds to page slicers:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

There you have it: how to create a simple bullet chart in Power BI.

That’s it for this week, come back next week for more Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-bullet-charts/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-bullet-charts/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-bullet-charts/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-bullet-charts/#0)

[](https://sumproduct.com/blog/power-bi-blog-bullet-charts/#0 "close")

top