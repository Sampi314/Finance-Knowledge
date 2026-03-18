# Power Query: Revision Time – Part 9

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-9/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 9

*   June 4, 2024

Power Query: Revision Time – Part 9
===================================

Power Query: Revision Time – Part 9
===================================

5 June 2024

_Welcome to our Power Query blog. Today, I continue to create a refreshable revision timetable by randomising the subject slots I need for the timetable._

As my salespeople take a well-earned break, many students here in the UK are preparing for exams in the summer. To help my own offspring get organised, I volunteered to create a refreshable printable revision timetable. This is the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/9fa4928e14c7422c8be9c83417b61922-1.jpg)

I needed a list of topics, and to begin with, I created extra entries for topics that required more timeslots:

![](https://sumproduct.com/wp-content/uploads/2025/05/2734faf8bb0c4e8f3c8cb772fe0d7ba3-1.jpg)

We agreed on half-hourly slots, and I created a grid so that my daughter could indicate the slots that she wouldn’t be able to revise.

![](https://sumproduct.com/wp-content/uploads/2025/05/bbef9530a5dd6e6f91072736ed0f9cc7-1.jpg)

When I first designed the solution, I included some Excel functions, but since this is a Power Query blog, I will ensure that I only use Power Query functions (apart from some formatting at the end!).

In [Part 1](https://sumproduct.com/blog/power-query-revision-time-part-1/)
, I converted my data into two \[2\] Tables: **Subjects** and **Availability**. I extracted **Subjects** to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/413d7ef9314ea3ca270945c0b5f5b027-1.jpg)

I created the **Availability** query by taking a copy of **Subjects**, and amending it:

![](https://sumproduct.com/wp-content/uploads/2025/05/c10f40de073ab43a9f508ece457af593-1.jpg)

In [Part 2](https://sumproduct.com/blog/power-query-revision-time-part-2/)
, and [Part 3](https://sumproduct.com/blog/power-query-revision-time-part-3/)
, I calculated the number of subjects and the number of slots on **Availability.**

This gave me both totals:

![](https://sumproduct.com/wp-content/uploads/2025/05/2cfbc9eb1a21686e35d2beb4789969e5-1.jpg)

In [Part 4](https://sumproduct.com/blog/power-query-revision-time-part-4/)
, I calculated how many times each subject will appear in a new query, remembering to round up to whole slots.

This told me the number of slots that each subject should have for my example is three \[3\]:

![](https://sumproduct.com/wp-content/uploads/2025/05/d917c7c59d5b66cf2219a2c9f1650088-1.jpg)

In [Part 5](https://sumproduct.com/blog/power-query-revision-time-part-5/)
, I created a table where each subject appeared three times (_i.e_. the number of times given by **Subject\_Slots**).

![](<Base64-Image-Removed>)

In [Part 6](https://sumproduct.com/blog/power-query-revision-time-part-6/)
, I randomised the order of the slots ready to add to the timetable:

![](<Base64-Image-Removed>)

In [Part 7](https://sumproduct.com/blog/power-query-revision-time-part-7/)
, I took a reference copy of the query **Availability** which I called **TimeTable** and began to transform it so that it is ready to receive the slot data.

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-8/)
, I appended the slot number data to the rest of the **TimeTable** query.

![](<Base64-Image-Removed>)

This means I have duplicate rows for my slot data, one with data in **Slot Number**, and one without. I can’t get rid of the rows without data in **Slot Number** as I need to retain the rows with ‘x’ in the **Value** column. However, I start with a simple filter to get the basic **M** code:

![](<Base64-Image-Removed>)

The step generated is:

![](<Base64-Image-Removed>)

The **M** code is:

**\= Table.SelectRows(#”Appended Query”, each (\[Slot  \
Number\] <> null))**

I need to add some logic to this:

**\= Table.SelectRows(#”Appended Query”, each (\[Slot  \
Number\] <> null or \[Value\] = “x”))**

This retains all the rows I need:

![](<Base64-Image-Removed>)

I may now sort the data into ascending **Index** order:

![](<Base64-Image-Removed>)

This data is now ready to merge with the **Random\_Subject** query. Next time, I will look at how I would have approached preparing **TimeTable** by merging instead of appending.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-9/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-9/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-9/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-9/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-9/#0 "close")

top