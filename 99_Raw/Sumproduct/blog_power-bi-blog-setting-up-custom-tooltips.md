# Power BI Blog: Setting Up Custom ToolTips

**Source:** https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Setting Up Custom ToolTips

*   December 9, 2020

Power BI Blog: Setting Up Custom ToolTips
=========================================

Power BI Blog: Setting Up Custom ToolTips
=========================================

10 December 2020

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at how to set up a custom ToolTip._

We have previously discussed ToolTips and their existence in a previous [blog](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-tooltip-reports)
. However, we did not go in depth on how to set them up. Let’s put that right today.

Consider our “complex” example report:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-92-1.jpg)

If we move the mouse over any of the columns, by default, we are presented with the following ToolTip:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-81-1.jpg)

Sure, it has the added benefit of telling us the precise number of **Total Sales**. However, what if we wanted to know the breakdown of sales in each country when we positioned the mouse over a column?

In this scenario, we are going to have to create a custom ToolTip. The first step in this process is to create a new report page (click on the plus icon on the bottom right-hand side of the pages in Power BI).

There are two things we have to do before creating the visualisations for our custom ToolTip page:

1.  Mark this page as a ToolTip page
2.  Change the ‘Page size’.

While on the new page, navigate to the ‘Page information’ drop down section on the Visualizations panel:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-72-1.jpg)

It is always good practice to give the page a name. We have elected to give it the appropriate name of ‘Tooltip1’ (yes 10/10 for being creative!). We also must toggle the Tooltip option to On.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-64-1.jpg)

With the Tooltip option toggled On, Power BI will recognise this page as a ToolTip page.

Moving on, we should also adjust the page size. Otherwise, you will end up with a ToolTip that looks like this:

![](<Base64-Image-Removed>)

Expand the ‘Page size’ option and select the Tooltip or Custom option from the drop-down list. The Custom option will give you a bit more flexibility in page size, allowing you to adjust how much information you want the ToolTip to portray. For this example, we have picked the Tooltip option.

We can finally create the visualisation that we wish to be displayed as the Tooltip. For this example, we have picked a Donut visualisation.

![](<Base64-Image-Removed>)

Navigate back to our ‘Global Overview’ page and select the visualisation you wish to add **Tooltip1** to. With the visualisation selected, we may go to the Format tab and expand the Tooltip section:

![](<Base64-Image-Removed>)

Change the Type to ‘Report Page’. This will reveal a second drop-down option (Page):

![](<Base64-Image-Removed>)

Here we select, you guessed it, **Tooltip1**. Now if a user places the mouse over a column in the visualisation, this happens:

![](<Base64-Image-Removed>)

There we have it, a step and step guide on how to create a custom ToolTip.

That’s it for this week! Join us next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/#0)

[](https://sumproduct.com/blog/power-bi-blog-setting-up-custom-tooltips/#0 "close")

top