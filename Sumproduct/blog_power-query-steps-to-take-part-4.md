# Power Query: Steps to Take – Part 4

**Source:** https://sumproduct.com/blog/power-query-steps-to-take-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Steps to Take – Part 4

*   October 4, 2022

Power Query: Steps to Take – Part 4
===================================

Power Query: Steps to Take – Part 4
===================================

5 October 2022

_Welcome to our Power Query blog. This week, I continue with my worked example by unpivoting and combining my data._

The tent business has a new administrative assistant, who used to work in the United States. George has provided some information, but it’s not yet in a format I can use:

![](https://sumproduct.com/wp-content/uploads/2025/05/5b7a5b15019781243cdc6341ad8bec7b.jpg)

In [Part 1](https://sumproduct.com/blog/power-query-steps-to-take-part-1/)
, I extracted the data and created a **Base** query, and took a Reference copy which I transformed to only hold the quantity rows: **Quantities**:

![](https://sumproduct.com/wp-content/uploads/2025/05/a78462c841b95ff3abd371ec9006c1d1.jpg)

In [Part 2](https://sumproduct.com/blog/power-query-steps-to-take-part-2/)
, I created another query for the date information. This query is called **Dates:**

![](https://sumproduct.com/wp-content/uploads/2025/05/8c41e1ea96c96c035ebe8b954a091e9a.jpg)

[Last week](https://sumproduct.com/blog/power-query-steps-to-take-part-3/)
, I transformed the data so that the dates are in the correct format for my region.

![](https://sumproduct.com/wp-content/uploads/2025/05/4e3a9afbbba1171bafa287705cd938de.jpg)

Now it’s time to put **Quantities** and **Dates** back together to get a list of dates and quantities. I need to get the dates and quantities in columns rather than rows first. To do this, I need to use the ‘Unpivot columns’ function. In **Quantities**, I select the **Month** column and right-click.

![](https://sumproduct.com/wp-content/uploads/2025/05/367a555cc4f7341c4b4af06806d2aaf0.jpg)

I choose to ‘Unpivot Other Columns’:

![](https://sumproduct.com/wp-content/uploads/2025/05/4b009ab4b436ef6ffe8eaf5e7ee95660.jpg)

I need to perform the same unpivoting step in **Dates**:

![](https://sumproduct.com/wp-content/uploads/2025/05/5ff18572fc395a205a75a84786dd2c2a.jpg)

I can now merge the data, using the **Month** and **Attribute** columns:

![](https://sumproduct.com/wp-content/uploads/2025/05/fee0bef6af002a0541bc147c5955928a.jpg)

This brings my data back together:

![](https://sumproduct.com/wp-content/uploads/2025/05/cd408dbb245fbbc90ca9fe5700221cb2.jpg)

I expand **Dates** to just give me the **Value** column:

![](https://sumproduct.com/wp-content/uploads/2025/05/ce4c7880c547c25d26410204dc3aab19.jpg)

Now I just need to tidy up. I only need the **Value** and **Date.Value** columns, which I rename **Salespeople Available** and **Week Commencing**. I also change the data type of **Salespeople Available** to Whole Number, and rename the query to **Availability Q4**.

![](<Base64-Image-Removed>)

The data is ready to load.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-steps-to-take-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-steps-to-take-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-steps-to-take-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-steps-to-take-part-4/#0)

[](https://sumproduct.com/blog/power-query-steps-to-take-part-4/#0 "close")

top