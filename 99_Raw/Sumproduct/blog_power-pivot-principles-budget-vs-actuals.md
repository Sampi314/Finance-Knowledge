# Power Pivot Principles: Budget vs Actuals

**Source:** https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Budget vs Actuals

*   March 8, 2021

Power Pivot Principles: Budget vs Actuals
=========================================

Power Pivot Principles: Budget vs Actuals
=========================================

9 March 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll create a quarterly Budget vs Actuals table based on different Account aggregation._

To begin with, I have a **Transaction** table that contain “Actual” values for different accounts in the year 2020, _viz_.

![](https://sumproduct.com/wp-content/uploads/2025/05/dcb7919da6963fc52ac2a5a24ce02bf6-1.jpg)

Before I bring in this Actuals data, I must create a relationship between the **COA** (chart of accounts) table and the **Transaction** table based upon the **Account\_Number** column. Additionally, there should be another link between the **Calendar** table and **Transaction** table based upon the **Date** column. This is an addition to the relationships created earlier and would look as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-301.jpg)

Now that I have my relationships created, I can rename the **Amount** columns in the **Budget** and **Transaction** tables by prefixing them with their respective table names and then hit Refresh on the Data tab.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-245.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/0bad081ab840debeabbd91a9f4889845.jpg)

Further, to summarise the Budget vs Actual data, I select the following fields in the Pivot Table:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-194.jpg)

We have a quarterly Budget vs Actuals table prepared based upon different Account aggregations:

![](https://sumproduct.com/wp-content/uploads/2025/05/960352c722d688e42b540df8e2b8ded7.jpg)

While most of you are wondering why some of the aggregations have negative values for Budget data but positive values for Actuals data, that’s this week’s cliff-hanger. We will cover that next week!

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/#0)

[](https://sumproduct.com/blog/power-pivot-principles-budget-vs-actuals/#0 "close")

top