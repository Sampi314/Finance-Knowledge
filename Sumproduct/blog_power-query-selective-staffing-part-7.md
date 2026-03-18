# Power Query: Selective Staffing Part 7

**Source:** https://sumproduct.com/blog/power-query-selective-staffing-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Selective Staffing Part 7

*   December 7, 2021

Power Query: Selective Staffing Part 7
======================================

Power Query: Selective Staffing Part 7
======================================

8 December 2021

_Welcome to our Power Query blog. This week I look at an example that considers values that can be marked as included or excluded._

[Last week](https://sumproduct.com/blog/power-query-selective-staffing-part-6/)
, I was looking at an example where I had a table of quote data for each of my salespeople, and a list of salespeople that I wished to view quote details for:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-97.jpg)

I used an Inner Join to merge the data to get the solution:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-133.jpg)

This time, I will look at how I can expand this to allow me to consider inclusion and exclusion in the same example. To begin with, I will consider the following situation:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-97.jpg)

I begin in exactly the same way as [last week](https://sumproduct.com/blog/power-query-selective-staffing-part-6/)
, by extracting the tables to Power Query using ‘From Table/Range’ in the ‘Get & Transform’ section of the Data tab.

The quote data is in table **Staff\_Quotes\_Join\_E:**

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-96.jpg)

The staff to be excluded are in table **Quote\_Selection\_Join\_E:**

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-80.jpg)

I can exclude these values by performing a join. I do this from ‘Merge Queries from the Home tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-69.jpg)

This time, I will use a Left Anti Join, which will show me the rows that are only in **Staff\_Quotes\_Join\_E** and NOT in **Quote\_Selection\_Join\_E**. I need to specify the columns to compare:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-65.jpg)

This sounds exactly like what I need, so I click OK.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-50.jpg)

I can delete the **Quote\_Selection\_Join\_E** column to get the data I need:

![](<Base64-Image-Removed>)

Now I will consider the situation where we have a list staff that are marked as included or excluded.

![](<Base64-Image-Removed>)

This time, I am linking to a table that includes all the salespeople, and they have a flag next to their name. I extract the new data into a table called **Quote\_Selection\_Both**:

![](<Base64-Image-Removed>)

I can still solve this with a merge, but I need an extra row in **Staff\_Quotes\_Join\_E**:

![](<Base64-Image-Removed>)

This highly complicated column always has the value “I” and will simply allow me to merge with **Quote\_Selection\_Both**.

![](<Base64-Image-Removed>)

I have used an Inner Join to keep the rows I need:

![](<Base64-Image-Removed>)

I can now delete **Include** and **Quote\_Selection\_Both** to get the data I need:

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-selective-staffing-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-selective-staffing-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-selective-staffing-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-selective-staffing-part-7/#0)

[](https://sumproduct.com/blog/power-query-selective-staffing-part-7/#0 "close")

top