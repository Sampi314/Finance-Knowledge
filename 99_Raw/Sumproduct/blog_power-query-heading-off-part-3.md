# Power Query: Heading Off – Part 3

**Source:** https://sumproduct.com/blog/power-query-heading-off-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Heading Off – Part 3

*   February 27, 2024

Power Query: Heading Off – Part 3
=================================

Power Query: Heading Off – Part 3
=================================

28 February 2024

_Welcome to our Power Query blog. Today, I continue looking at an issue that occurs when I load to a Table with no headers._

I plan to show a particular issue with Power Query and Tables without headers. However, first I need to create the scenario, and I will show a few methods and tips along the way. I have two Tables of data:

1.  contains my salespeople’s expenses (**Expenses**)
2.  determines the expenses that will be covered by each supplier (**Supplier\_Limit**).

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-heading-off-part-1/)
, I created two \[2\] queries, and grouped **Expenses**.

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-heading-off-part-2/)
, I merged **Expenses** with the **Supplier\_Limit** query to see if any limits have been breached. To achieve this, I created a new conditional column **Flag**:

![](<Base64-Image-Removed>)

I may now remove the **Flag** Column. From the Home tab, I choose to ‘Close & Load To…’:

![](<Base64-Image-Removed>)

I need to be able to control which queries are loaded to the workbook. In the workbook, I choose ‘Only Create Connection’:

![](<Base64-Image-Removed>)

This will create all the queries as connections, and I can decide which to load:

![](<Base64-Image-Removed>)

Since I only need to load **Limit\_Exceeded** to the workbook, I can right-click on that query and find the ‘Load To…’ option.

![](<Base64-Image-Removed>)

This brings up the same ‘Import Data’ dialog that I saw earlier:

![](<Base64-Image-Removed>)

I change the settings and check ‘Table’ and ‘New worksheet’:

![](<Base64-Image-Removed>)

I click OK, and a new worksheet ‘Limit\_Exceeded’ is created.

![](<Base64-Image-Removed>)

This data is going to be transferred to another system, which means the headings must be removed. I click anywhere in the Table to reveal the ‘Table Design’ tab:

![](<Base64-Image-Removed>)

In the ‘Table Style Options’, I uncheck the ‘Header Row’:

![](<Base64-Image-Removed>)

So far so good. I change some values in the **Expenses**Table, and refresh the query:

![](<Base64-Image-Removed>)

Everything looks fine, but next time, I will see what happens when the requirements change and I run the query for a single salesperson.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-heading-off-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-heading-off-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-heading-off-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-heading-off-part-3/#0)

[](https://sumproduct.com/blog/power-query-heading-off-part-3/#0 "close")

top