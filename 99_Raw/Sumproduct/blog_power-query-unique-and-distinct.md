# Power Query: Unique and Distinct

**Source:** https://sumproduct.com/blog/power-query-unique-and-distinct/

---

[Home](https://sumproduct.com/)

\> Power Query: Unique and Distinct

*   March 24, 2020

Power Query: Unique and Distinct
================================

Power Query: Unique and Distinct
================================

25 March 2020

_Welcome to our Power Query blog. This week, I look at how to find the unique or distinct values in a list of data._

I have a list of data, and I want to find the values that occur once only.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-249-1.jpg)

My first step is to extract my data to Power Query using the ‘From Table’ option in the ‘Get & Transform section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-247-1.jpg)

I begin by using the ‘Group By’ feature on the Transform tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-233-1.jpg)

I can accept the defaults:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-210-1.jpg)

This will count the number of times each **Data** value appears.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-181-1.jpg)

I only want to see the **Data** values that appear once. I can do this by filtering **Count****.**

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-161-1.jpg)

I click OK to see my unique data:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-137-1.jpg)

I can also find the distinct values from my original data. I start from the original data again.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-111-1.jpg)

This time, I can right click on my column to find the distinct values.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-91-1.jpg)

I remove the duplicates:

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-65-1.jpg)

I can see that I now have 99 distinct values out of the original 500 rows.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-unique-and-distinct/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-unique-and-distinct/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-unique-and-distinct/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-unique-and-distinct/#0)

[](https://sumproduct.com/blog/power-query-unique-and-distinct/#0 "close")

top