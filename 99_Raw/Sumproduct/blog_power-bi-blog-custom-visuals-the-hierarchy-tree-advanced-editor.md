# Power BI Blog: Custom Visuals – the Hierarchy Tree Advanced Editor

**Source:** https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Custom Visuals – the Hierarchy Tree Advanced Editor

*   February 26, 2020

Power BI Blog: Custom Visuals – the Hierarchy Tree Advanced Editor
==================================================================

Power BI Blog: Custom Visuals – the Hierarchy Tree Advanced Editor
==================================================================

27 February 2020

_Welcome back to this week’s Power BI blog series. This week, we take an even deeper look at the Hierarchy Tree visualisation._

This week we will cover some other features in the Hierarchy Tree visualisation.

As a quick recap, this is the resulting visual we produced by the end of [last week’s blog](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-continued/)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-265.jpg)

We set some conditional formatting rules so that the progress bars, on top of each node, display how much the actual amounts vary compared to the budgeted amounts.

Throughout this short series, you may have noticed the yellow button on the top right-hand corner of the visualisation.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-266-1.jpg)

This button opens the ‘Advanced Editor’, which allows us to apply another level of conditional formatting to the nodes. This level of conditional formatting will apply to the background or font colour of the nodes.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-251-1.jpg)

For this example, we will use the background colour option.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-225-1.jpg)

To create a conditional formatting rule, we simply add a conditional formatting rule from the left pane.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-194-1.jpg)

I have elected to use the following settings to further highlight if a node is under budget:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-172-1.jpg)

Now we have to specify the condition rules, so I will click on the ‘Condition 1’ option:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-147-1.jpg)

I have elected to base this conditional formatting rule on the stock amounts. The drop-down option here allows me to pick from all of the fields in the current dataset. I have then selected the less than or equal to option. The next step is to pick the ‘Comparison Type’:

![](<Base64-Image-Removed>)

There are various types:

*   the **Number** option will allow me to compare every node stock value to a set number that is manually entered
*   the **Value** option allows me to compare the node stock values to another field in my dataset
*   the **Calculation** option allows me to compare the node stock values to a simple calculation (simple calculation example pictured below):

![](<Base64-Image-Removed>)

For this example, we will just compare the Stock values to the Budget values, _viz_.

![](<Base64-Image-Removed>)

As a side note, we can add more conditions to this rule with the ‘+’ option at the bottom.

Next, I press Save and the resulting changes should look like this:

![](<Base64-Image-Removed>)

With multiple rules we can enable and disable rules with the ‘off and on’ toggles on the right of each rule:

![](<Base64-Image-Removed>)

That’s it for this week, check back next week for the next week for more Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/#0)

[](https://sumproduct.com/blog/power-bi-blog-custom-visuals-the-hierarchy-tree-advanced-editor/#0 "close")

top