# Power Query: Merging Muddles

**Source:** https://sumproduct.com/blog/power-query-merging-muddles/

---

[Home](https://sumproduct.com/)

\> Power Query: Merging Muddles

*   February 23, 2021

Power Query: Merging Muddles
============================

Power Query: Merging Muddles
============================

24 February 2021

_Welcome to our Power Query blog. This week, I look at how to merge data when there is not a clear link between the tables._

I have some sales contact data for my imaginary business. Unfortunately, I have some complaints and I want to allocate them to the correct salesperson. I have the date of the complaint and the date the salesperson took over as the primary, as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-246.jpg)

I start by extracting my data and importing it into Power Query. I have two tables. I click somewhere in my first table and I choose ‘From Table/Range’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-310.jpg)

I accept the defaults (as usual!) and click OK.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-252.jpg)

I ‘Close & Load’ my first table and repeat this process for the other table.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-237.jpg)

I now have two tables, which I have called **Key Salesperson** and **Complaints**.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-200.jpg)

I am going to merge my tables, so I choose ‘Merge Queries’, then ‘Merge Queries as New’, from the Combine section on the Home tab. I choose to create a new table because I am going to join my tables in another way next time…

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-177.jpg)

In the join options, I can see that the dates are not going to help me join my tables: I need to use a full outer join.

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-162.jpg)

When I choose this, I can see there is more work to do to get the data into the format I require.

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-136.jpg)

I start by expanding the **Complaints** table, using the icon next to the column heading.

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-122.jpg)

I don’t need to use the prefix option as my columns have unique names.

![](https://sumproduct.com/wp-content/uploads/2025/05/daf8c4f0259ce428269c0d3d4badd32b-107.jpg)

I create a new date column which will hold whichever date is populated.

![](<Base64-Image-Removed>)

I click OK to create **Incident Date**.

![](<Base64-Image-Removed>)

I remove the other date fields and sort on **Incident Date**.

![](<Base64-Image-Removed>)

I fill down the salesperson name by selecting **Primary Salesperson**, right-clicking and selecting Fill and then ‘Fill Down’.

![](<Base64-Image-Removed>)

Finally, I select out rows where **Complaint Description** is _null_.

![](<Base64-Image-Removed>)

This gives me the data in the required format:

![](<Base64-Image-Removed>)

Next time, I’ll look at a much quicker way to achieve this result…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-merging-muddles/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-merging-muddles/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-merging-muddles/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-merging-muddles/#0)

[](https://sumproduct.com/blog/power-query-merging-muddles/#0 "close")

top