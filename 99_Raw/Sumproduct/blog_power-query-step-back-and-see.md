# Power Query: Step Back and See

**Source:** https://sumproduct.com/blog/power-query-step-back-and-see/

---

[Home](https://sumproduct.com/)

\> Power Query: Step Back and See

*   August 6, 2019

Power Query: Step Back and See
==============================

Power Query: Step Back and See
==============================

7 August 2019

_Welcome to our Power Query blog. Today, I build a function to add a column to a table._

My imaginary salesperson, Mary, has been busy, and I want to look at how her commission varies daily.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-384.jpg)

I upload my data into Power Query using ‘From Table’ on the ‘Get & Transform’ section of the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-394.jpg)

I am going to add an index column, in the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-373.jpg)

I choose to start from zero \[0\].

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-346.jpg)

The step is call ‘Added Index’, which I need to remember for later. I am going to add another index column, this time starting at one \[1\]:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-296.jpg)

I am going to merge ‘Added Index’ and’ Added Index.1′ by using some **M** code in a step. This will allow me to link each row to the previous row. The **M** function I am using is **Table.NestedJoin()**, which I used in [Power Query: Group Dynamics](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-group-dynamics)
 when I was calculating group share.

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-264.jpg)

The **M** code I have used is:

**\= Table.NestedJoin(#”Added Index”, {“Employee”,”Index”}, #”Added Index1″, {“Employee”,”Index.1″}, “Added Index”, JoinKind.LeftOuter)**

This takes my data with the index that begins at 0 and links it to the table with the index that begins at 1. Therefore, it links all the data to the previous row.

Next, I need to expand some data from my joined table.

![](<Base64-Image-Removed>)

In this case, I will ‘Use original column name as prefix’, so I can distinguish between my original and expanded data.

![](<Base64-Image-Removed>)

I can now remove the row with _null_ values. I choose to apply a filter.

![](<Base64-Image-Removed>)

Now, I create a custom column to calculate the daily difference in commission.

![](<Base64-Image-Removed>)

I click OK to see my new column:

![](<Base64-Image-Removed>)

I can track my salesperson’s progress in terms of commission, and set targets if I wish.

![](<Base64-Image-Removed>)

I can expand this method to include data from other salespeople.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-step-back-and-see/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-step-back-and-see/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-step-back-and-see/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-step-back-and-see/#0)

[](https://sumproduct.com/blog/power-query-step-back-and-see/#0 "close")

top