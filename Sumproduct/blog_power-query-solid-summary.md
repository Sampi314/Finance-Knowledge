# Power Query: Solid Summary

**Source:** https://sumproduct.com/blog/power-query-solid-summary/

---

[Home](https://sumproduct.com/)

\> Power Query: Solid Summary

*   January 7, 2020

Power Query: Solid Summary
==========================

Power Query: Solid Summary
==========================

8 January 2020

_Welcome to our Power Query blog. This week, I look at a use for grouping._

I have some data for the rental income for my imaginary tent hire business. I want to see what seasonal variation I have.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-294.jpg)

I start by using ‘From Table’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-299-1.jpg)

I take the defaults as I want to use the headings.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-283.jpg)

I will use the ‘Group By’ functionality in the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-258.jpg)

I need to group by **_Department_** to get the totals for the year.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-221.jpg)

The Basic grouping is not detailed enough, as I want to create an **_Average Income_** column and a **_Rows_** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-194.jpg)

When I select OK, I get one row.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-165-1.jpg)

The **_Rows_** column contains a table, which I expand.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-135-1.jpg)

This will give me a table with my original information, and an **Average Income** column.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-111-1.jpg)

I add a ‘Custom Column’ from the ‘Add Column’ tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-82-1.jpg)

This gives me the **Deviation from Average**.

![](<Base64-Image-Removed>)

I can now filter on this column to see when I get a deviation of more than 20, whichever currency it may be in.

![](<Base64-Image-Removed>)

This gives me the dates when my income is maximised.

![](<Base64-Image-Removed>)

I make most money at Christmas, Easter and the New Year. Time to focus my salespeople on the lucrative summer market next!

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-solid-summary/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-solid-summary/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-solid-summary/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-solid-summary/#0)

[](https://sumproduct.com/blog/power-query-solid-summary/#0 "close")

top