# Power BI Blog: Custom Visuals – the Hierarchy Tree Continued

**Source:** https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Custom Visuals – the Hierarchy Tree Continued

*   February 19, 2020

Power BI Blog: Custom Visuals – the Hierarchy Tree Continued
============================================================

Power BI Blog: Custom Visuals – the Hierarchy Tree Continued
============================================================

20 February 2020

_Welcome back to this week’s Power BI blog series. This week, we take a deeper look at the Hierarchical Variance Tree visualisation._

Last week, we looked at how to create a Hierarchy Tree with a custom visual. This week, we shall look at how to further customise the visual presentation and present more than one field in the value field.

As a quick recap, this is the resulting visual we produced by the end of [last week’s blog](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-269.jpg)

We had the total stock amounts separated into Australia and New Zealand nodes, then had the stock amounts broken down further into city nodes. This visualisation also allows us to compare two fields. Let’s update our original dataset to include budget amounts for our stock values so we may analyse items further:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-272-1.jpg)

Refreshing the query in the Power BI file will bring in our Budget numbers into our dataset. We can then add the Budget numbers into the Value area of the visualisation.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-256-1.jpg)

We will see that there are two new numbers below the Australia and New Zealand nodes. The percentage figure represents the percentage difference between the actuals and budget amounts. The second number is the raw number value difference between the stock and budgeted amounts. Both numbers will be displayed in brackets when negative.

We can expand the tree to view the breakdown per city by country:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-230-1.jpg)

Each of the city nodes now has the percentage and raw number difference between the budget and total stock in each city.

The blue bars ‘Progress Bars’ do not serve much purpose at the moment; we may change them so that the bar will reflect the difference between the stock amounts and the budgeted amounts. To do this, click on the visualisation and navigate to the Format tab, to scroll down to the ‘Conditional Formatting’ option and toggle it to On in the Visualization pane:

![](<Base64-Image-Removed>)

Currently, it is colour coded based on how far actual stock values are compared to the budget. We can further customise the ‘Progress Bar’ under the ‘Tree Options’ option. For this example, we have picked the ‘% Variance’ option:

![](<Base64-Image-Removed>)

The progress bar area has changed to show the budgeted amount represented by the black bar. The progress bars are displayed directionally in relation to the budget amount to give a visual representation of how the actual stock amounts differ from the budgeted amount. We can alter the conditional formatting threshold in the ‘Conditional Formatting’ option in the Format tab.

![](<Base64-Image-Removed>)

That’s it for this week, check back next week for the next week for more Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/#0)

[](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/#0 "close")

top