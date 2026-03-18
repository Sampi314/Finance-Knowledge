# Power Query: Heading Off – Part 5

**Source:** https://sumproduct.com/blog/power-query-heading-off-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Heading Off – Part 5

*   March 12, 2024

Power Query: Heading Off – Part 5
=================================

Power Query: Heading Off – Part 5
=================================

13 March 2024

_Welcome to our Power Query blog. Today, I explore an issue that occurs when I load to a Table with no headers._

I plan to show a particular issue with Power Query and Tables without headers. However, first I need to create the scenario, and I will show a few methods and tips along the way. I have two Tables of data:

1.  contains my salespeople’s expenses (**Expenses**)
2.  determines the expenses that will be covered by each supplier (**Supplier\_Limit**).

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-heading-off-part-1/)
, I created two \[2\] queries, and grouped **Expenses**.

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-heading-off-part-2/)
, I merged **Expenses** with the **Supplier\_Limit** query to create **Limit\_Exceeded**, which tells me if any limits have been breached.

![](<Base64-Image-Removed>)

In [Part 3](https://sumproduct.com/blog/power-query-heading-off-part-3/)
, I loaded **Limit\_Exceeded** to a new worksheet.

![](<Base64-Image-Removed>)

I removed the header row and changed some of the data in **Expenses**.

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-heading-off-part-4/)
, I ran the query for a single salesperson.

![](<Base64-Image-Removed>)

I extracted this cell and created a parameter **P\_Salesperson**

![](<Base64-Image-Removed>)

I used this parameter to limit the data in **Expenses**:

![](<Base64-Image-Removed>)

When I refreshed **Limit\_Exceeded**, I checked the results:

![](<Base64-Image-Removed>)

The results correctly showed one row of data and no headings. However, things change when I select a different Salesperson:

![](<Base64-Image-Removed>)

When I refresh **Limit\_Exceeded**, it looks rather strange:

![](<Base64-Image-Removed>)

It shows a row of data where the header row would have been. Note that the **Limit\_Exceeded** query indicates that zero \[0\] rows have been loaded. If I look back at the data for Mary, I see that, instead of showing an empty table, Mary’s data has been pushed into the header row:

![](<Base64-Image-Removed>)

Whilst this could be described as a bug, I still need to fix it so that the output data is correct. I could assume that if I move the Table up a row, this problem might not happen. Let’s delete the top row:

![](<Base64-Image-Removed>)

So far so good. Now, I change the selected salesperson back to ‘Mary’ and refresh:

![](<Base64-Image-Removed>)

Finally, I change it back to ‘Newbie’. I can immediately see a problem:

![](<Base64-Image-Removed>)

I get a ‘Download failed’ message on **Limit\_Exceeded**. When I look at the query, the data looks strange:

![](<Base64-Image-Removed>)

That’s definitely not right: this query should be empty!

On the View tab, I tick the ‘Column distribution’ box.

![](<Base64-Image-Removed>)

It is empty and yet showing a row! If I ‘Refresh Preview,’ from the Home tab, it looks like this issue is fixed:

![](<Base64-Image-Removed>)

However, when I go back to the Excel worksheet and refresh, I still have a problem:

![](<Base64-Image-Removed>)

Clearly, I need to do more to solve this problem, which is where I will pick this up next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-heading-off-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-heading-off-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-heading-off-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-heading-off-part-5/#0)

[](https://sumproduct.com/blog/power-query-heading-off-part-5/#0 "close")

top