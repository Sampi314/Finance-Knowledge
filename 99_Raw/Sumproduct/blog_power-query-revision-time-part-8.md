# Power Query: Revision Time – Part 8

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 8

*   May 28, 2024

Power Query: Revision Time – Part 8
===================================

Power Query: Revision Time – Part 8
===================================

29 May 2024

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

[Last week](https://sumproduct.com/blog/power-query-revision-time-part-7/)
, I took a reference copy of the query **Availability** which I called **TimeTable** and began to transform it so that it is ready to receive the slot data.

![](<Base64-Image-Removed>)

Before I can merge this query with **Random\_Subject**, I need to number the slots available.

As is often the case with Power Query, there are a number of ways I can do this, but I have chosen to filter the data I need to number and then re-merge it with the rest of the query. To make it easier to keep the order of my data, I will add an index column from the ‘Add Column’ tab before I start:

![](<Base64-Image-Removed>)

Next, I filter on **Value** to remove the rows containing ‘x’:

![](<Base64-Image-Removed>)

I may now add another index starting from one \[1\], which I name **Slot Number**:

![](<Base64-Image-Removed>)

I could merge or append my data to include the other rows that I will need for the timetable. Before I start, I will rename the steps ‘Added Index’ and ‘Renamed Columns 1’ which I plan to join, to make it easier to follow the process:

![](<Base64-Image-Removed>)

I will look at each option: this week I append the data. In the Home tab, I choose ‘Append Queries’, and choose to append to the current query:

![](<Base64-Image-Removed>)

This generates the **M** code I need.

![](<Base64-Image-Removed>)

I change the code from:

**\= Table.Combine({#”Index Slots Only”, #”Index  
Slots Only”})**

to

**\= Table.Combine({#”Index Slots Only”, #”Index Full  
Query”})**

This gives me some duplicates:

![](<Base64-Image-Removed>)

I will look at one way of dealing with these next week.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-8/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-8/#0 "close")

top