# Power Query: Join or List – Part 3

**Source:** https://sumproduct.com/blog/power-query-join-or-list-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Join or List – Part 3

*   December 13, 2022

Power Query: Join or List – Part 3
==================================

Power Query: Join or List – Part 3
==================================

14 December 2022

_Welcome to our Power Query blog. This week, I continue comparing alternative approaches to extracting data from another table, this time, with approximate matching._

I know you have missed them: my imaginary salespeople are back! They are going to help me compare alternative approaches to pulling in data from one query to another, namely merging and using list functions. There are two examples that I am going to use in this series. I have covered the first example, which used exact matching.

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
 and [Part 2](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I looked at these two tables. The first is a list of item types that my salespeople have been putting under ‘personal’ on expenses. The second is a list indicating which are allowed and which are not, and any that require further information.

![](https://sumproduct.com/wp-content/uploads/2025/05/4437975347897e2227d10d6d5b5875b0.jpg)

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
, I merged the queries to get the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/86b9eafb6804543747afc79c80383d28.jpg)

[Last time](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I used **List** functions to achieve the same result.

![](https://sumproduct.com/wp-content/uploads/2025/05/892542be53d4eefc84250f2417a05f47.jpg)

This time, I’ll move onto the second example, which requires an approximate match. I have two more tables, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/5b948b2f44d674b512d1d42e15bf3d9f.jpg)

The plan is to encourage my salespeople to work harder by linking their commission to each transaction. I start by extracting the data from each table to Power Query, using ‘From Table/Range’ in the ‘Get & Transform’ section of the Data tab, which converts them to Excel Tables.

![](https://sumproduct.com/wp-content/uploads/2025/05/e70606dc6f9055ed4deea8d39d3f1c12.jpg)

Having done this for both sets of data, I can view my queries in the Power Query editor. I have named my new queries **Sales** and **Commissions** respectively.

![](https://sumproduct.com/wp-content/uploads/2025/05/4f4c566db80560225743411cdcf63220.jpg)

Starting in **Sales**, on the Home tab, I choose to ‘Merge Queries as New’ from the ‘Merge Queries’ option:

![](<Base64-Image-Removed>)

I choose to merge **Sales** and **Commissions**:

![](<Base64-Image-Removed>)

Clearly, just linking on **Amount** and taking the defaults isn’t going to give me any results. I need to change the join type to ‘Full Outer’. Trust me, this will lead to the correct result in the end!

![](<Base64-Image-Removed>)

I click OK to get a new query, which is a reference copy of **Sales**, plus a new column called **Commissions**:

![](<Base64-Image-Removed>)

I can expand **Commissions** by clicking on the double headed arrow icon:

![](<Base64-Image-Removed>)

Since I have two columns called **Amount**, I will leave the ‘Use original column name as prefix’ checked and click OK. The results don’t look too promising:

![](<Base64-Image-Removed>)

Since I have no exact matches, I have a lot of _null_ values. Next time, I will transform this data to get to the desired result…

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-join-or-list-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-join-or-list-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-join-or-list-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-join-or-list-part-3/#0)

[](https://sumproduct.com/blog/power-query-join-or-list-part-3/#0 "close")

top