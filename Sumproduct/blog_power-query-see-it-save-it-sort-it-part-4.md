# Power Query: See it, Save it, Sort it – Part 4

**Source:** https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: See it, Save it, Sort it – Part 4

*   June 7, 2022

Power Query: See it, Save it, Sort it – Part 4
==============================================

Power Query: See it, Save it, Sort it – Part 4
==============================================

8 June 2022

_Welcome to our Power Query blog. This week, I reorganise the data from my appended queries._

In [Power Query: See it, Save it, Sort it – Part 1](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-1/)
, I started with some data for my imaginary salespeople:

![](<Base64-Image-Removed>)

and extracted it into Power Query, in order to perform some transformations.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-3/)
, I appended **Full\_Dates** to **Sales\_Transactions** to give me a row for every consecutive date in **Sales\_Transactions**:

![](<Base64-Image-Removed>)

This time, I will organise the data in **Sales\_Transactions**. Currently, the appended **Full\_Dates** rows are under the original **Sales\_Transactions** data:

![](<Base64-Image-Removed>)

I start by sorting by **Date**. I can do this using the arrow dropdown on the right of the **Date** heading.

![](<Base64-Image-Removed>)

I choose to ‘Sort Ascending’:

![](<Base64-Image-Removed>)

The **Full\_Dates** query had no **Amount**, **ID** or **Name** columns, so these have been left as _null_ values. I only need these rows if there are no transactions from the original data on that date, so now I need a way of removing the extra _null_ lines.

There are several ways I can achieve this, and the first is by using a merge. I can check the data against the original **Sales\_Transactions** data.

I start by generating the **M** code I will need. On the Home tab, I choose ‘Merge Queries’ from the Merge Queries’ dropdown:

![](<Base64-Image-Removed>)

In the dialog, I choose to merge the table with itself on **Date**, and choose a ‘Full Outer’ join:

![](<Base64-Image-Removed>)

This gives me a column of tables.

![](<Base64-Image-Removed>)

I continue by using the expand icon next to the heading on the **Sorted Rows** column:

![](<Base64-Image-Removed>)

I have only selected **Date**, and I have chosen not to ‘Use original column name as prefix’, therefore my new column will be called **Date.1**:

![](<Base64-Image-Removed>)

Next time, I will show how I am going to use this to filter my data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/#0)

[](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-4/#0 "close")

top