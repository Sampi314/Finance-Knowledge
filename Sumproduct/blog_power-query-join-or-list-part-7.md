# Power Query: Join or List – Part 7

**Source:** https://sumproduct.com/blog/power-query-join-or-list-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Join or List – Part 7

*   January 10, 2023

Power Query: Join or List – Part 7
==================================

Power Query: Join or List – Part 7
==================================

11 January 2023

_Welcome to our Power Query blog. This week, I continue comparing alternative approaches to extracting data from another table with approximate matching using **List()** functions._

I know you have missed them: my imaginary salespeople are back! They are going to help me compare alternative approaches to pulling in data from one query to another, namely merging and using list functions. There are two examples that I am going to use in this series. I have covered the first example, which used exact matching.

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
 and [Part 2](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I looked at these two tables. The first is a list of item types that my salespeople have been putting under ‘personal’ on expenses. The second is a list indicating which are allowed and which are not, and any that require further information.

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-join-or-list-part-1/)
, I merged the queries to get the result:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-join-or-list-part-2/)
, I used **List** functions to achieve the same result.

![](<Base64-Image-Removed>)

In [Part 3](https://sumproduct.com/blog/power-query-join-or-list-part-3/)
, I moved onto the second example, which requires an approximate match. I have two more tables:

![](<Base64-Image-Removed>)

The plan is to encourage my salespeople to work harder, by linking their commission to each transaction. I extracted my data to Power Query and set about merging my queries:

![](<Base64-Image-Removed>)

Having transformed the resulting data, it seemed like I had a long way to go!

![](<Base64-Image-Removed>)

In [Part 4](https://sumproduct.com/blog/power-query-join-or-list-part-4/)
, I transformed this data to get to the desired result.

![](<Base64-Image-Removed>)

In [Part 5](https://sumproduct.com/blog/power-query-join-or-list-part-5/)
, I created a reference of **Sales**, which I called **Sales (list)**.

![](<Base64-Image-Removed>)

I added a new column **Commission Rate** to **Sales (list)**, which comprised of a list of all the **Amount** values from **Commissions** which were less than or equal to the **Amount** on **Sales (list)**.

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-join-or-list-part-6/)
, I used **List.Max()** and the method from Part 2 to get my result, but this time I will use another method. I begin by creating a Duplicate copy of **Sales (list)**:

![](<Base64-Image-Removed>)

I select the ‘Added Custom 3’ step and choose to ‘Delete Until End’.

![](<Base64-Image-Removed>)

I continue at the warning by pressing Delete:

![](<Base64-Image-Removed>)

Now I create a new Custom Column **Commission**. This method involves counting the number of list items returned to give the position of the rate associated with the highest band:

![](<Base64-Image-Removed>)

The **M** code is:

**\= Commissions\[Commission Rate\]{List.Count(\[Commission Rate\])-1 }**

This counts the number of items in the list and subtracts one \[1\] to get the index position in **Commissions** (since the index always starts from zero \[0\] by default). The associated **Commission Rate** then populates the **Commission** column.

![](<Base64-Image-Removed>)

This achieves the result in less steps than last time. As I did [last week](https://sumproduct.com/blog/power-query-join-or-list-part-6/)
, I can replace the errors with zero \[0\] and proceed with the calculation.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-join-or-list-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-join-or-list-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-join-or-list-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-join-or-list-part-7/#0)

[](https://sumproduct.com/blog/power-query-join-or-list-part-7/#0 "close")

top