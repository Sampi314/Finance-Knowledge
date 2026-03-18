# Power BI Blog: Draw a Line

**Source:** https://sumproduct.com/blog/power-bi-blog-draw-a-line/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Draw a Line

*   July 14, 2021

Power BI Blog: Draw a Line
==========================

Power BI Blog: Draw a Line
==========================

15 July 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we will look at how to create a line in a matrix visualisation._

This has been one of our more popular queries regarding Power BI – unbelievably!

I have a simple table of accounting data, and I want to create a Matrix visualisation:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-164.jpg)

I can choose to create a Matrix in the Visualisations pane:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-215.jpg)

I drag the **Months** field into the Columns area.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-174.jpg)

I then drag the **Sales** and **Costs** into the Values area.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-169.jpg)

I toggle on the ‘Show on rows’ option in the Formatting tab in the Visualizations (values) section.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-141.jpg)

I am going to create a simple measure to calculate profit:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-124.jpg)

**Profit = CALCULATE(SUM(Accounts\[Sales\]) – SUM(Accounts\[Costs\])**

This is a simple calculation to get **Profit**, which I can add to the Values area.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-116.jpg)

I’d like to make it clear that **Profit** has been calculated from **Sales** and **Costs**. Therefore, I’d like to put a line before **Profit**. To do this, I can create a new measure:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-97.jpg)

**\*  = ” “**

The name of the measure (which I will refer to as the asterisk measure) is an asterisk, and the value is a space. The reasons for this will become clearer when I plot this measure on the Matrix.

![](<Base64-Image-Removed>)

The name of the asterisk measure doesn’t appear as it’s a _special character_. Next, I need to format the measure so that it appears as a line. On the Formatting tab, there is a section for ‘Field formatting’, and I can choose my asterisk measure.

![](<Base64-Image-Removed>)

Changing the background colour to black has made my asterisk measure appear as a black line. The thickness of this line is linked to the padding on the Grid section of the Formatting tab. I have this set to 1:

![](<Base64-Image-Removed>)

It’s now clear that **Profit** has been calculated from **Sales** and **Costs**.

![](<Base64-Image-Removed>)

Next time, I’ll look at how to leave a blank line in a Matrix when I have multiple calculations.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-draw-a-line/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-draw-a-line/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-draw-a-line/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-draw-a-line/#0)

[](https://sumproduct.com/blog/power-bi-blog-draw-a-line/#0 "close")

top