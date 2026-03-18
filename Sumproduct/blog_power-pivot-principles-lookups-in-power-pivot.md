# Power Pivot Principles: Lookups in Power Pivot

**Source:** https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Lookups in Power Pivot

*   December 17, 2018

Power Pivot Principles: Lookups in Power Pivot
==============================================

Power Pivot Principles: Lookups in Power Pivot
==============================================

18 December 2018

_Welcome back to our Power Pivot blog. Today, we discuss how to create lookups in Power Pivot._

The ability to create lookup columns in Excel is very useful, especially when we have a table that only contains an identifier of some sort but the data we need, such as the product name, is stored elsewhere.

For example, let’s assume that we have the following table that contains today’s (at the time of writing) shipment:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-517.jpg)

Yes, the table is useful however the table only contains the **Product ID** and **Customer ID**, making this particularly difficult to read for humans. The customer and product names are stored in other (related) tables, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/82793bd878118b7ac5e4390cbcbf0e0a.jpg)

We can use the **RELATED** function to create two custom columns in the shipment table that will display the **Product Name** and **Customer Name**. You should note that before creating the custom columns, ensure that the three tables have been loaded to the data model and have established relationships between them (you can read more about establishing relationships between tables [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-relationships)
).

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-462.jpg)

To create our custom columns, navigate to the Power Pivot window and create a custom column on our Shipping Table (you can read more about creating custom columns [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-calculated-columns)
):

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-381.jpg)

It’s simple:

**\=RELATED(‘Customer Table'\[CustomerName\])**.

We add another column for the **Product Name**:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-328.jpg)

**\=RELATED(‘Product Table'\[ProductName\])**.

There we have it, using the **RELATED** function we have created a much more readable table.

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/#0)

[](https://sumproduct.com/blog/power-pivot-principles-lookups-in-power-pivot/#0 "close")

top