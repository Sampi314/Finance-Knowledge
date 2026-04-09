# Power BI Blog: Dynamic Headings for In-Between Variables

**Source:** https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dynamic Headings for In-Between Variables

*   February 17, 2021

Power BI Blog: Dynamic Headings for In-Between Variables
========================================================

Power BI Blog: Dynamic Headings for In-Between Variables
========================================================

18 February 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we’ll discuss another approach to dynamic headings, this time for variables between two periods using a time slicer selection._

Last week, we talked about [Dynamic Headings Based on Time Slicer](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-easier-dynamic-heading-based-on-time-slicer)
 for a stock variable from a **Year** slicer, in order to calculate current liabilities and current assets.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-249.jpg)

This week, we will build on last week’s blog and take it to the next level by creating a dynamic chart title with a start date and an end date. In the example below, I have already created a **Year** slicer that has been extracted from a [Calendar table](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-creating-a-dynamic-calendar-table)
, as well as a **Profitability Selection** slicer, leaving space at the top of the chart for a heading.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-313.jpg)

Now, to create a dynamic heading that shows the start and end date selected in the **Year** slicer, I need to create a measure.

**Profit selection title = “Profit for ” & MIN(‘Calendar'\[Year\]) & ” to ” & MAX(‘Calendar'\[Year\])**

I am using the **MIN** and **MAX** functions to define the values selected in the **Year** slicer. To get the heading on the dashboard, select the card and drag the measure created above to the Fields section, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-255.jpg)

The heading card will now look like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-239.jpg)

To get the card with only the heading, navigate to the Format panel and turn off Category.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-202.jpg)

Resize and realign the card to bring it on top of the visual. Now, select from 2021 to 2025 to ensure the dynamic heading works fine.

![](<Base64-Image-Removed>)

That’s it for this week! Join us next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/#0)

[](https://sumproduct.com/blog/power-bi-blog-dynamic-headings-for-in-between-variables/#0 "close")

top