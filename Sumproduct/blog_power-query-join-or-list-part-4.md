# Power Query: Join or List – Part 4

**Source:** https://sumproduct.com/blog/power-query-join-or-list-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Join or List – Part 4

*   December 20, 2022

Power Query: Join or List – Part 4
==================================

Power Query: Join or List – Part 4
==================================

21 December 2022

_Welcome to our Power Query blog. This week, I continue comparing alternative approaches to extracting data from another table, this time with approximate matching._

I know you have missed them: my imaginary salespeople are back! They are going to help me compare alternative approaches to pulling in data from one query to another, namely merging and using list functions. There are two examples that I am going to use in this series. I have covered the first example, which used exact matching.

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
 and [Part 2](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I looked at these two tables. The first is a list of item types that my salespeople have been putting under ‘personal’ on expenses. The second is a list indicating which are allowed and which are not, and any that require further information.

![](https://sumproduct.com/wp-content/uploads/2025/05/1995a4ae4cc538069bf4fcf873d0b38f.jpg)

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
, I merged the queries to get the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/b7bf23a820ae5af91fd82b599499936f.jpg)

In [Part 2](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I used List functions to achieve the same result.

![](https://sumproduct.com/wp-content/uploads/2025/05/f460ec3115de729493bca018dee6650f.jpg)

[Last time](https://sumproduct.com/blog/power-query-join-or-list-part-3/)
, I moved onto the second example, which required an approximate match. To remind you, I have two more tables:

![](https://sumproduct.com/wp-content/uploads/2025/05/ba1e8b12e682e65ae2f2f804a0215fba.jpg)

The plan is to encourage my salespeople to work harder, by linking their commission to each transaction. Last time, I extracted my data to Power Query and set about merging my queries:

![](https://sumproduct.com/wp-content/uploads/2025/05/339eea492e327c1b9dfcb31bb1ea990b.jpg)

Having transformed the resulting data, it seemed like I had a long way to go!

![](https://sumproduct.com/wp-content/uploads/2025/05/6b5d07a09fb4214c13272f1847159260.jpg)

I had no exact matches, just a lot of _null_ values!

This time, I will transform this data to get to the desired result. I start by creating a ‘Conditional Column’ from the ‘Add Column’ tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/2ea8e099d76a61de0bb0ed82549d4654.jpg)

Note that I have selected a column for the ‘Output’ and ‘Else’ values, so that I can pick the value in **Commissions.Amount** if the value in **Amount** is _null_, otherwise I use the value in **Amount**.

This gives me a new column, and I set the data type to a decimal number:

![](<Base64-Image-Removed>)

Next, I ‘Sort Ascending’ on **Commission Band**. I access this option from the filter arrow dropdown:

![](<Base64-Image-Removed>)

Next, I Fill Down on **Commissions.Commission Rate**:

![](<Base64-Image-Removed>)

I no longer need the **Commissions.Commission Amount** or the **Commission Band** columns so I select them both, and right-click to ‘Remove Columns’.

![](<Base64-Image-Removed>)

I select the filter arrow dropdown next to the **Name** column, and choose to ‘Remove Empty’:

![](<Base64-Image-Removed>)

Then, I can tidy up my data types and view the commission rates for each transaction. I also rename **Commissions.Commission Rate** to **Commission**.

![](<Base64-Image-Removed>)

To calculate the amount of commission, I go to the ‘Add Column’ tab and used the ‘Standard’ dropdown to ‘Multiply’ them:

![](<Base64-Image-Removed>)

This gives me a new column called **Multiplication**. If I select this column and **Amount**, I can use another method to add a column using a standard function. I can right-click and choose Sum:

![](<Base64-Image-Removed>)

This gives me a new column called **Addition**:

![](<Base64-Image-Removed>)

I can now remove the **Amount**, **Commission** and **Multiplication** columns (this time I select them and use the **\[Delete\]** key) and rename **Addition** to **Amount**. I sort my data by **Date**, and rename the query **Amounts Inclusive of Commission**.

![](<Base64-Image-Removed>)

Next time, I’ll look at how I can achieve this with **List()** functions.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-join-or-list-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-join-or-list-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-join-or-list-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-join-or-list-part-4/#0)

[](https://sumproduct.com/blog/power-query-join-or-list-part-4/#0 "close")

top