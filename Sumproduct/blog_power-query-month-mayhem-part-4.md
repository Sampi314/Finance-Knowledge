# Power Query: Month Mayhem – Part 4

**Source:** https://sumproduct.com/blog/power-query-month-mayhem-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Month Mayhem – Part 4

*   July 23, 2024

Power Query: Month Mayhem – Part 4
==================================

Power Query: Month Mayhem – Part 4
==================================

24 July 2024

_Welcome to our Power Query blog. Today, I use the **Source Summary**_ _query as a building block, as I continue transforming the data._

My salespeople are back from their break and I have more reports to construct. I have a report with a list of the clients they have been working with each month:

![](<Base64-Image-Removed>)

I would like to display the amount details in the salesperson sections but aligned to the relevant month at the top of the page:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-month-mayhem-part-3/)
, I created a **Months** query:

![](<Base64-Image-Removed>)

I also took a reference copy of this query, and transformed it to create **Months\_Unpivoted**:

![](<Base64-Image-Removed>)

This time, I will create the queries I need for the amount data. I start by taking a Reference copy of **Source Summary**:

![](<Base64-Image-Removed>)

I call the new query **Amounts**:

![](<Base64-Image-Removed>)

To remove the rows with heading data, I filter on **Column1** to remove nulls:

![](<Base64-Image-Removed>)

**Amounts** is now complete:

![](<Base64-Image-Removed>)

I take a reference copy of **Amounts**, which I call **Amounts\_Unpivoted**:

![](<Base64-Image-Removed>)

I select **Column1**, **Section Index** and **Index,** and right-click to ‘Unpivot Other Columns’:

![](<Base64-Image-Removed>)

I now have the two \[2\] queries I need for amounts; **Amounts** and **Amounts\_Unpivoted**.

![](<Base64-Image-Removed>)

Next time, I will consider how I am going to move the data by creating mapping queries.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-month-mayhem-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-month-mayhem-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-month-mayhem-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-month-mayhem-part-4/#0)

[](https://sumproduct.com/blog/power-query-month-mayhem-part-4/#0 "close")

top