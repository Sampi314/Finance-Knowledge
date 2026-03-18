# Power BI Blog: Different Coloured Columns in a Stacked Column Chart

**Source:** https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Different Coloured Columns in a Stacked Column Chart

*   March 3, 2021

Power BI Blog: Different Coloured Columns in a Stacked Column Chart
===================================================================

Power BI Blog: Different Coloured Columns in a Stacked Column Chart
===================================================================

4 March 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we will expand on the last week’s blog, this time with different coloured stacked column charts._

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-different-coloured-columns-in-a-chart)
 we created the following chart, whereby the current year’s data is coloured differently to the historical data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-240.jpg)

This works fine for that particular case. However, what if we also wanted to see the product category breakdown, say, in a stacked column chart?

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-304.jpg)

As it stands, we are unable to include the **Product Category** field in the Legend if we have more than one field in the Values area. The solution here would be to create a new **Product Category** field that will not only distinguish between the products, but also between the years.

There is one hurdle. The **Sales** table, where the **SalesAmount**field is located, does not have the **Product Category** in it. The **Product Category** field is located in the **ProductList** table. Fortunately, we can create a relationship between the two tables using the **ProductKey** as the common key. You can read more about creating relationships [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-relationships)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-247.jpg)

With that borne in mind, we can create some related columns in the **Sales** table. Navigating to the Data view of the report, we can create a custom column called **Product Category** with the following code:

Product Category = RELATED(ProductList\[Product Category\])

![](<Base64-Image-Removed>)

I have used the **RELATED** function to create a column that populates each row with the corresponding product category, similar to **VLOOKUP**, or **INDEX** and **MATCH.** You can read more about the **RELATED** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-is-there-anything-related)
.

The next step is to create the conditional column that will consider the year. This is performed with the following code:

Product Category 2 = IF(YEAR(Sales\[OrderDate\]) = 2021, Sales\[Product Category\] & ” F”, Sales\[Product Category\])

![](<Base64-Image-Removed>)

Going back to the Report view, I can use **Product Category 2** as the legend:

![](<Base64-Image-Removed>)

We can make some adjustments in the colours in the ‘Data colors’ option in the Format tab:

![](<Base64-Image-Removed>)

That’s it for this week! A quick and simple way to colour different columns in your stacked columns charts in Power BI, while factoring in different product types. Join us next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/#0)

[](https://sumproduct.com/blog/power-bi-blog-different-coloured-columns-in-a-stacked-column-chart/#0 "close")

top