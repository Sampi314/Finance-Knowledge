# Power Query: Check the Filters – Part 2

**Source:** https://sumproduct.com/blog/power-query-check-the-filters-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Check the Filters – Part 2

*   August 30, 2022

Power Query: Check the Filters – Part 2
=======================================

Power Query: Check the Filters – Part 2
=======================================

31 August 2022

_Welcome to our Power Query blog. This week, I look at how the options on the Transform tab can filter a query, saving both time and steps._

[Last time](https://sumproduct.com/blog/power-query-check-the-filters-part-1/)
, I looked at an example where I was creating a Date Table, where I started by finding the start and end date of the data. I showed how I could save time and steps by filtering the **Date** column to find the rows with the earliest date.

![](<Base64-Image-Removed>)

There are other ways I could have filtered my **Date** column. I start by taking a duplicate copy of the **Start Date** query:

![](<Base64-Image-Removed>)

This time, I am only going to keep the ‘Source’ step.

![](<Base64-Image-Removed>)

On the Transform tab, if I have **Date** selected, there is an option in the Date dropdown to transform the ‘Earliest’ date:

![](<Base64-Image-Removed>)

This transforms my query into the earliest date:

![](<Base64-Image-Removed>)

If I could use dates to create lists, I could stop here, but unfortunately Power Query is not able to do this (yet!). Instead, I delete the ‘Calculated Earliest’ step and change the data type on **Date** to ‘Whole Number’:

![](<Base64-Image-Removed>)

There is another useful option on the Transform tab, this time in the Statistics dropdown:

![](<Base64-Image-Removed>)

I transform to the Minimum:

![](<Base64-Image-Removed>)

I have achieved my goal in only three \[3\] steps. I rename the query **Start Date in 3**, and create a duplicate query which I call **End Date in 3**:

![](<Base64-Image-Removed>)

I delete the ‘Calculated Minimum’ step and go back to the Statistics dropdown in the Transform tab:

![](<Base64-Image-Removed>)

This time I transform the query to the Maximum value in **Date**:

![](<Base64-Image-Removed>)

I have my start and end date values expressed as numbers ready to create a list of dates to create my **Date Table**:

![](<Base64-Image-Removed>)

Since I started off with two queries that had six \[6\] steps each:

![](<Base64-Image-Removed>)

I have reduced the work needed by half by using the options available to filter a single column.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-check-the-filters-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-check-the-filters-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-check-the-filters-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-check-the-filters-part-2/#0)

[](https://sumproduct.com/blog/power-query-check-the-filters-part-2/#0 "close")

top