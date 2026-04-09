# Power Pivot Principles: Summarising a Budget

**Source:** https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Summarising a Budget

*   February 1, 2021

Power Pivot Principles: Summarising a Budget
============================================

Power Pivot Principles: Summarising a Budget
============================================

2 February 2021

_Welcome back to the Power Pivot Principles blog. This week, we’ll examine an example of how to summarise a company’s budget in Power Pivot._

Let’s assume a company XYZ has a **Budget** table they wish to summarise. Their budget consists of three worksheets. The first is the **Budget** table, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-256.jpg)

The second is the **Transaction** table:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-321.jpg)

The final worksheet comprises the **Charts of Accounts** (**COA**) table:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-262.jpg)

To begin, we must add all three worksheets to the Data Model in Power Pivot by clicking on ‘Add to Data Model’ on the ‘Power Pivot’ tab of the Ribbon.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-248.jpg)

To facilitate the summarising of the Budget table, it important to define relationships between these tables. These relationships will allow us to us the **[RELATED](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-related-vs-lookupvalue)
**function to extract values from different columns of another worksheet. We can also [add a Calendar Table](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
, which will later be used in a PivotTable too.

By switching to the ‘Diagram View’ in the Home tab, we can drag the ‘**Account Number**‘ field to connect the **COA** and **Budget** tables, as well as link ‘**EOM\_Date**‘ to **‘Date’,** to connect the **Calendar** and **Budget** tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-210.jpg)

Switching back to ‘Data View’, we may add new calculated columns to identify ‘**Account\_Name**‘ using the follow code:

**\=RELATED(COA\[Account Name\])**

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-186.jpg)

The next step in the process is to transform the table into a Pivot Table, by selecting the option from the **Home** tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-168.jpg)

In the ‘**PivotTable Fields**‘, drop the ‘**Month**‘ from ‘**Date Hierarchy**‘ in Calendar table to ‘Columns’, ‘**Account\_Name**‘ from **Budget** table to ‘Rows’ and ‘**Amount**‘ from **Budget** table to ‘Values’.

![](<Base64-Image-Removed>)

Click on the drop down menu next to ‘Sum of Amount’ to select ‘Value Field Settings’:

![](<Base64-Image-Removed>)

Click on ‘**Number Format**‘:

![](<Base64-Image-Removed>)

Finally, select ‘**Currency**‘, reducing the figures displayed to two decimal places and hit OK.

![](<Base64-Image-Removed>)

You will now have a summary of the budget, _viz._

![](<Base64-Image-Removed>)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/#0)

[](https://sumproduct.com/blog/power-pivot-principles-summarising-a-budget/#0 "close")

top