# Power Query: Join or List – Part 1

**Source:** https://sumproduct.com/blog/power-query-join-or-list-part-1/

---

[Home](https://sumproduct.com/)

\> Power Query: Join or List – Part 1

*   November 29, 2022

Power Query: Join or List – Part 1
==================================

Power Query: Join or List – Part 1
==================================

30 November 2022

_Welcome to our Power Query blog. This week, I begin a series of blogs comparing alternative approaches to extracting data from another table._

I know you’ve missed them: my imaginary salespeople are back! They are going to help me compare alternative approaches to pulling in data from one query to another, namely merging and using list functions. There are two examples that I am going to use in this series. The first example, and the simplest, is **exact** matching. Later in the series I will also look at **approximate** matching.

I have two tables. The first is a list of item types that my salespeople have been putting under ‘Personal’ on expenses. The second is a list indicating which are allowed and which are not, and any that require further information.

![](https://sumproduct.com/wp-content/uploads/2025/05/d48da24ae75f3624c93bc0617b5385e0.jpg)

I extract both sets of data into Power Query by using the ‘From Table/Range’ option in the ‘Get & Transform’ section of the Data tab, one set at a time:

![](https://sumproduct.com/wp-content/uploads/2025/05/a18ab09e988d9ea824705772901efcc9.jpg)

To begin with, I choose to ‘Close & Load To’ from the Home tab in the Power Query editor to trigger the ‘Import Data’ dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/0701772cbf13580a685f9f0528aadcd5.jpg)

I choose to ‘Only Create Connection’, and load the other set of data:

![](https://sumproduct.com/wp-content/uploads/2025/05/a44f5f29958e2d2d699a6a9b3873f93d.jpg)

This gives me two queries, which I rename to **Expenses** and **Permissions**.

![](https://sumproduct.com/wp-content/uploads/2025/05/5323fa1c6a93578c6f6748f6cdfa7745.jpg)

The first method I am going to use is to merge the tables to find out who has expenses that are not allowed or that require more information. I start in **Expenses**, and I choose ‘Merge Queries’ from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/ece63b31c2e42a9f4bec185d86846c87.jpg)

This enables the ‘Merge Queries’ dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/dcb0ff83902dac5c17294ad02fb7e915.jpg)

I match the data (using a ‘Left Outer’ join) and I click OK.

![](https://sumproduct.com/wp-content/uploads/2025/05/10af531d62c784d933ec09891ee4948e.jpg)

I use the icon in the **Permissions** column to extract the data from the tables:

![](<Base64-Image-Removed>)

I only need the information in **Column2.**

![](<Base64-Image-Removed>)

I have the data I need, and I rename the column **Allowed to Claim?**

Next time, I will use **List** functions to achieve the same result.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-join-or-list-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-join-or-list-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-join-or-list-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-join-or-list-part-1/#0)

[](https://sumproduct.com/blog/power-query-join-or-list-part-1/#0 "close")

top