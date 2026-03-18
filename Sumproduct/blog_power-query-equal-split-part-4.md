# Power Query: Equal Split Part 4

**Source:** https://sumproduct.com/blog/power-query-equal-split-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Equal Split Part 4

*   January 30, 2024

Power Query: Equal Split Part 4
===============================

Power Query: Equal Split Part 4
===============================

31 January 2024

_Welcome to our Power Query blog. Today, I modify the solution to divide amounts over rows by using a parameter._

In this mini-series of blogs, I have been looking at an issue that Mary, my top imaginary salesperson had. She had some accounting data, which she needed to split equally for two suppliers:

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-equal-split/)
, I created two queries:

![](<Base64-Image-Removed>)

I looked at a simple way to achieve the result I want, which assumes that I always have two \[2\] suppliers.

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-equal-split-part-2/)
, I refined this solution to make it more flexible, by using a parameter for the number of suppliers:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-equal-split-part-3/)
, I looked at a slightly difference scenario. I had the same accounting data, but this time, there were no suppliers to link to:

![](<Base64-Image-Removed>)

I needed to split the rows into two \[2\] equal parts.

![](<Base64-Image-Removed>)

However, it is often useful to make the solution more flexible. This time, I will use a parameter to decide how many ways I need to split the amounts.

![](<Base64-Image-Removed>)

I have given cell **G1**, containing the number to split by, a defined name, **Split\_By**. I click on cell **G1**, and choose to extract my data to Power Query by right-clicking and choosing to ‘Get Data from Table/Range’:

![](<Base64-Image-Removed>)

This automatically creates a new query called **Split\_By**.

![](<Base64-Image-Removed>)

I click in the cell, and right-click to ‘Drill Down’:

![](<Base64-Image-Removed>)

I now have a parameter to use:

![](<Base64-Image-Removed>)

I take a reference copy of the query I created in [Part 1](https://sumproduct.com/blog/power-query-equal-split/)
, **Accounts**, as I wish to keep the original steps:

![](<Base64-Image-Removed>)

I call my new query **AccountsNS\_Split**. I need to divide the data in a different way, since I can’t just use duplicate columns as I did last week. I am going to create a helper query.

![](<Base64-Image-Removed>)

I call the new blank query **Helper\_Split**:

![](<Base64-Image-Removed>)

The **M** code I have used to create the list is:

**\= {1..Split\_By}**

This creates a list, where the number of rows is the number in **Split\_By**. Using the ‘List Tools’ Transform tab, I convert the list into a table, as I wish to add a column:

![](<Base64-Image-Removed>)

I take the defaults and add a new ‘Custom Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I create a new column **Link**, which is always one \[1\]. This is similar to the approach I used in [Part 1](https://sumproduct.com/blog/power-query-equal-split/)
.

![](<Base64-Image-Removed>)

Next time, I will tidy up my helper query and complete the solution.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-equal-split-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-equal-split-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-equal-split-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-equal-split-part-4/#0)

[](https://sumproduct.com/blog/power-query-equal-split-part-4/#0 "close")

top