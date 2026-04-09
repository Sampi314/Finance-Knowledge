# Power Query: Heading Off – Part 4

**Source:** https://sumproduct.com/blog/power-query-heading-off-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Heading Off – Part 4

*   March 5, 2024

Power Query: Heading Off – Part 4
=================================

Power Query: Heading Off – Part 4
=================================

6 March 2024

_Welcome to our Power Query blog. Today, I continue to consider an issue that occurs when I load to a Table with no headers._

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

[Last time](https://sumproduct.com/blog/power-query-heading-off-part-3/)
, I loaded **Limit\_Exceeded** to a new worksheet.

![](<Base64-Image-Removed>)

I removed the header row and changed some of the data in **Expenses**.

![](<Base64-Image-Removed>)

This time, I will see what happens when the requirements change, and I run the query for a single salesperson. On the ‘Expenses’ sheet, cell **N2** contains the salesperson value I want to use. This cell may be identified by the name **P\_Salesperson:**

![](<Base64-Image-Removed>)

If I right-click on cell **N2**, I have the option to ‘Get Data from Table/Range’.

![](<Base64-Image-Removed>)

This creates a new query called **P\_Salesperson**:

![](<Base64-Image-Removed>)

Note that Power Query has decided to promote headers, leaving an empty table! The ‘Changed Type’ step is also ineffective since there is no data to work with. I only need the Source step, so I delete the other steps:

![](<Base64-Image-Removed>)

I click in the cell and right-click to ‘Drill down’:

![](<Base64-Image-Removed>)

This gives me the parameter I need.

![](<Base64-Image-Removed>)

Since I will be reducing the data, I should apply the parameter as close to the source as possible (ignoring the option of doing this in Excel as this is a Power Query blog!). In the **Expenses** query, I go to the Source step:

![](<Base64-Image-Removed>)

I may add a filter on **Salesperson**:

![](<Base64-Image-Removed>)

I choose ‘Mary’ as my placeholder value. I will change this to **P\_Salesperson** later. When I click OK, I received a warning:

![](<Base64-Image-Removed>)

I may ignore the warning and click Insert, as I am happy to insert a step.

![](<Base64-Image-Removed>)

The **M** code for the ‘Filtered Rows’ step is:

**\= Table.SelectRows(Source, each (\[Salesperson\] =  
“Mary”))**

To use the parameter, I change this to:

**\= Table.SelectRows(Source, each (\[Salesperson\] =  
P\_Salesperson))**

This gives me the same results:

![](<Base64-Image-Removed>)

My final query now looks like this:

![](<Base64-Image-Removed>)

Now I have reduced the data in **Expenses**, I check the **Limit\_Exceeded** query.

![](<Base64-Image-Removed>)

I now only have one \[1\] row. I ‘Close & Load To…’ as I did [last week](https://sumproduct.com/blog/power-query-heading-off-part-3/)
, so that my parameter query can be set to ‘Connection Only’:

![](<Base64-Image-Removed>)

I refresh **Limit\_Exceeded** and look at the results:

![](<Base64-Image-Removed>)

The results correctly show one row of data and no headings. However, things change when I select a different Salesperson:

![](<Base64-Image-Removed>)

More on this next time!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-heading-off-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-heading-off-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-heading-off-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-heading-off-part-4/#0)

[](https://sumproduct.com/blog/power-query-heading-off-part-4/#0 "close")

top