# Power Query: Heading Off – Part 1

**Source:** https://sumproduct.com/blog/power-query-heading-off-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Heading Off – Part 1

*   February 13, 2024

Power Query: Heading Off – Part 1
=================================

Power Query: Heading Off – Part 1
=================================

14 February 2024

_Welcome to our Power Query blog. Today, I begin to look at an issue that occurs when I load to a Table with no headers._

I plan to show a particular issue with Power Query and Tables without headers. However, first I need to create the scenario, and I will show a few methods and tips along the way. I have two Tables of data:

1.  contains my salespeople’s expenses (**Expenses**)
2.  determines the expenses that will be covered by each supplier (**Supplier\_Limit**).

![](https://sumproduct.com/wp-content/uploads/2025/05/48a36ac320ae1fff50ecae0b3f3f1944.jpg)

I extract **Supplier\_Limit**, by clicking somewhere in the Table, and right-clicking to ‘Get Data from Table/Range’.

![](https://sumproduct.com/wp-content/uploads/2025/05/dafdb1d9b35e59b7667918d18041f30e.jpg)

This gives me a query called **Supplier\_Limit**:

![](https://sumproduct.com/wp-content/uploads/2025/05/32a1b7a8ef35d8a745d901546d9d620c.jpg)

I could load this query as a connection only and go back and get the other data in the same way, but there is another method I could use without leaving the Power Query editor. I make a duplicate copy of **Supplier\_Limit**:

![](https://sumproduct.com/wp-content/uploads/2025/05/df4e32d8338af0f316e2751b93b1402a.jpg)

I delete the ‘Changed Type’ step because it uses the column names, and look at the **M** code in the Source step:

![](https://sumproduct.com/wp-content/uploads/2025/05/6604accdf38e1a6011240c56ca0c04b9.jpg)

I may use the current **M** code:

**\=  
Excel.CurrentWorkbook(){\[Name=”Supplier\_Limit”\]}\[Content\]**

and change the Table name from **Supplier\_Limit** to **Expenses**:

**\= Excel.CurrentWorkbook(){\[Name=”Expenses”\]}\[Content\]**

This gives me the contents of the **Expenses** Table, and automatically recreates the ‘Changed Type’ step:

![](<Base64-Image-Removed>)

I rename this query **Expenses**.

Before I can compare this date to the limits, I need to group by **Supplier** and **Expense Type**. I can do this using the ‘Group By’ functionality on the Home tab:

![](<Base64-Image-Removed>)

Using Advanced mode, I have chosen **Supplier**, and then used ‘Add grouping’ to also group by Expense Type. I have chosen to aggregate **Amount**, by using the Sum Operation.

![](<Base64-Image-Removed>)

The data is now in a similar format to the **Supplier\_Limit** query.

Next time, I will merge **Expenses** with the **Supplier\_Limit** query to see if any limits have been breached.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-heading-off-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-heading-off-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-heading-off-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-heading-off-part-1/#0)

[](https://sumproduct.com/blog/power-query-heading-off-part-1/#0 "close")

top