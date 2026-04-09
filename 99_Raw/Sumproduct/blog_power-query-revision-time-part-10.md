# Power Query: Revision Time – Part 10

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-10/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 10

*   June 11, 2024

Power Query: Revision Time – Part 10
====================================

Power Query: Revision Time – Part 10
====================================

12 June 2024

_Welcome to our Power Query blog. Today, I continue to create a refreshable revision timetable by randomising the subject slots I need for the timetable._

As my salespeople take a well-earned break, many students here in the UK are preparing for exams in the summer. To help my own offspring get organised, I volunteered to create a refreshable printable revision timetable. This is the result:

![](<Base64-Image-Removed>)

I needed a list of topics, and to begin with, I created extra entries for topics that required more timeslots:

![](<Base64-Image-Removed>)

We agreed on half-hourly slots, and I created a grid so that my daughter could indicate the slots that she wouldn’t be able to revise.

![](<Base64-Image-Removed>)

When I first designed the solution, I included some Excel functions, but since this is a Power Query blog, I will ensure that I only use Power Query functions (apart from some formatting at the end!).

In [Part 1](https://sumproduct.com/blog/power-query-revision-time-part-1/)
, I converted my data into two \[2\] Tables: **Subjects** and **Availability**. I extracted **Subjects** to Power Query.

![](<Base64-Image-Removed>)

I created the **Availability** query by taking a copy of **Subjects**, and amending it:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-revision-time-part-2/)
, and [Part 3](https://sumproduct.com/blog/power-query-revision-time-part-3/)
, I calculated the number of subjects and the number of slots on **Availability.**

This gave me both totals:

![](<Base64-Image-Removed>)

In [Part 4](https://sumproduct.com/blog/power-query-revision-time-part-4/)
, I calculated how many times each subject will appear in a new query, remembering to round up to whole slots.

This told me the number of slots that each subject should have for my example is three \[3\]:

![](<Base64-Image-Removed>)

In [Part 5](https://sumproduct.com/blog/power-query-revision-time-part-5/)
, I created a table where each subject appeared three times (_i.e_. the number of times given by **Subject\_Slots**).

![](<Base64-Image-Removed>)

In [Part 6](https://sumproduct.com/blog/power-query-revision-time-part-6/)
, I randomised the order of the slots ready to add to the timetable:

![](<Base64-Image-Removed>)

In [Part 7](https://sumproduct.com/blog/power-query-revision-time-part-7/)
, I took a reference copy of the query **Availability** which I called **TimeTable** and began to transform it so that it is ready to receive the slot data.

![](<Base64-Image-Removed>)

In [Part 8](https://sumproduct.com/blog/power-query-revision-time-part-8/)
, I appended the slot number data to the rest of the **TimeTable** query.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-revision-time-part-9/)
, I removed the duplicate values.

![](<Base64-Image-Removed>)

However, as I said in [Part 8](https://sumproduct.com/blog/power-query-revision-time-part-8/)
, I could have transformed the data in **TimeTable** by merging instead of appending. To make it easier to follow, I have created a copy of the earlier steps of **TimeTable**. This query has been created purely to show the merging technique:

![](<Base64-Image-Removed>)

I choose ‘Merge Queries’ from the Home tab, and merge **TimeTable (Merge Method)** with itself. I choose to merge on all columns apart from **Slot Number** and take the default ‘Left Outer’ join.

![](<Base64-Image-Removed>)

The results are not relevant at this point: I need to change the **M** code.

![](<Base64-Image-Removed>)

I change the **M** code from:

**\=  
Table.NestedJoin(#”Index Slots Only”, {“Time Slot”,  
“Attribute”, “Value”, “Index”}, #”Index  
Slots Only”, {“Time Slot”, “Attribute”,  
“Value”, “Index”}, “Index Slots Only”,  
JoinKind.LeftOuter)**

to

**\=  
Table.NestedJoin(#”Index Full Query”, {“Time Slot”,  
“Attribute”, “Value”, “Index”}, #”Index  
Slots Only”, {“Time Slot”, “Attribute”,  
“Value”, “Index”}, ” Index Slots Only”,  
JoinKind.LeftOuter)**

_i.e_. I am changing the first merge table to the ‘Index Full Query’ step:

![](<Base64-Image-Removed>)

I only need the **Slot Number** from the expanded Table:

![](<Base64-Image-Removed>)

When I click OK, I have the data, but the order is jumbled:

![](<Base64-Image-Removed>)

When I sort the data by ascending **Index**, I can compare it with the append method:

![](<Base64-Image-Removed>)

I have the same results in the same number of steps, so it only comes down to which method is easier for you!

Next time, I will continue to transform **TimeTable**.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-10/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-10/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-10/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-10/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-10/#0 "close")

top