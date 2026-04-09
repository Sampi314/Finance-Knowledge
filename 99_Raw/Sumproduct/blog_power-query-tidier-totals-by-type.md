# Power Query: Tidier Totals by Type

**Source:** https://sumproduct.com/blog/power-query-tidier-totals-by-type/

---

[Home](https://sumproduct.com/)

\> Power Query: Tidier Totals by Type

*   July 20, 2021

Power Query: Tidier Totals by Type
==================================

Power Query: Tidier Totals by Type
==================================

21 July 2021

_Welcome to our Power Query blog. This week, I take another look at selective running totals._

[Last time,](https://sumproduct.com/blog/power-query-totals-by-type/)
 I extracted running totals by **Tent Type** for my tent data:

![](<Base64-Image-Removed>)

Although I got to my required output, I had to make an assumption that I had seven \[7\] rows for each **Tent Type** (since I had seven months of data).

![](<Base64-Image-Removed>)

I will start from the **Added Index** step that I used last time.

![](<Base64-Image-Removed>)

Since I am going to be reading the data in the table, I buffer it in step **Custom1**.

**\= Table.Buffer(#”Added Index”)**

The Custom Column I am going to create this time is a little more complicated, and is based upon **Table()** functionality instead of **List()** functionality. This allows me to enter conditions.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= (Other\_Table) =>Table.SelectRows(Custom1,**

**(Total\_Table) => Total\_Table\[Index\] <= Other\_Table\[Index\]**

**and Total\_Table\[Tent Type\] = Other\_Table\[Tent Type\])**

This looks complicated, but it can be broken down. **Custom1** is the table from the previous step. **Total\_Table** is the data that I am grouping. It’s essentially looking for all the rows where the **Tent Type** matches, and the **Index** is less than or equal to where we are now. **Other\_Table** is the current table. The result will be a mini table, with all the rows that should be included in the running total.

![](<Base64-Image-Removed>)

I have grouped the data by type into these mini tables. Now I can expand them to get at the amounts.

![](<Base64-Image-Removed>)

This gives me a subgroup for each occurrence of **Tent Type** containing the amounts I need to total for the running total.

![](<Base64-Image-Removed>)

I can group these by **Index**.

![](<Base64-Image-Removed>)

Since the values in **Month**, **Tent Type** and **Amount** are the same for all occurrences in the group, I use Max (I could also use Min).

![](<Base64-Image-Removed>)

The results are the same as last week, but this time I didn’t need to assume anything about my data, so this query would cope with additional months being added.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-tidier-totals-by-type/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-tidier-totals-by-type/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-tidier-totals-by-type/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-tidier-totals-by-type/#0)

[](https://sumproduct.com/blog/power-query-tidier-totals-by-type/#0 "close")

top