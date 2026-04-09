# Power BI Blog: Dynamic Visualisation Titles

**Source:** https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dynamic Visualisation Titles

*   January 1, 2020

Power BI Blog: Dynamic Visualisation Titles
===========================================

Power BI Blog: Dynamic Visualisation Titles
===========================================

2 January 2020

_Welcome back to this week’s Power BI blog series. This week, we are going to look at how to create dynamic visualisation titles – whatever they might be…_

[Last week](https://sumproduct.com/blog/power-bi-blog-presenting-several-measures-on-a-single-visualisation/)
, we looked at creating visualisations that can be toggled between two or more data sets using a slicer. This week, we are going to address the problem of static visualisation titles.

As a refresher, we’ve created a table that broke down the Profit, Total Costs and Total Sales by country and month:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-297.jpg)

This visualisation has been designed to display either **Profit**, **Total Costs** or **Total Sales**, depending upon the slicer selection. From a user friendliness perspective, we have no indication of what the visualisation is presenting other than what is selected on the slicer. We should give the table a title. To do this, we click on the visualisation, then click on the format tab and we give the visualisation a title:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-302-1.jpg)

We have decided on ‘Profit’. However, when we change the slicer selection the title remains as ‘Profit’ – obviously, as it has been typed in (it is “static”).

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-286.jpg)

In a previous blog, we discussed how to create dynamic card headings. Using this methodology, we can create the following measure:

Title = **IF**(

**ISFILTERED**(‘Filters'\[**Filter Items**\]),

“Selected Option: ” & **FIRSTNONBLANK**(‘Filters'\[Filter Items\],1),

“Sales”

)

We then place this measure on a Card visualisation on top of the Table:

![](<Base64-Image-Removed>)

The title card will now update to reflect the selection on the slicer:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-224.jpg)

However, this would mean that we need a title card on top of each visualisation. Thinking ahead, if we were to create a dashboard with multiple visualisations this could get quite confusing quite quickly.

Therefore, we click on the visualisation, then click on the Format tab, and finally, enable the title. Do you see that there are three dots next to ‘Title text’?

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-197.jpg)

We then click on Conditional formatting:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-166-1.jpg)

This brings up the ‘Title text’ dialog, where we can format the title based upon a field:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-136-1.jpg)

In this case, we select the **Title** measure:

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-112-1.jpg)

There we go: we have given the visualisation a dynamic title!

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-83-1.jpg)

Lets make some changes to the **Title** measure:

Title = **IF**(

**ISFILTERED**(‘Filters'\[Filter Items\]),

**FIRSTNONBLANK**(‘Filters'\[Filter Items\],1) & ” in ” & **FIRSTNONBLANK**(‘Calendar Table'\[Year\],1),

“Total Sales in ” & **FIRSTNONBLANK**(‘Calendar Table'\[Year\],1)

)

Just to make the title a little more descriptive:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

That’s it for this week, come back next week for more Power BI!

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/#0)

[](https://sumproduct.com/blog/power-bi-blog-dynamic-visualisation-titles/#0 "close")

top