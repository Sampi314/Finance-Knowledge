# Power Query: Revision Time – Part 5

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 5

*   May 7, 2024

Power Query: Revision Time – Part 5
===================================

Power Query: Revision Time – Part 5
===================================

8 May 2024

_Welcome to our Power Query blog. Today, I continue to create a refreshable revision timetable by creating a list of all the subject slots I need for the timetable._

As my salespeople take a well-earned break, many students here in the UK are preparing for exams in the summer. To help my own offspring get organised, I volunteered to create a refreshable printable revision timetable. This is the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/4b984f1c27c30cebe6872ece4248b2b8-1.jpg)

I needed a list of topics, and to begin with, I created extra entries for topics that required more timeslots:

![](https://sumproduct.com/wp-content/uploads/2025/05/d87c7f26a0cbab5fc7bd571f31c2f037-1.jpg)

We agreed on half-hourly slots, and I created a grid so that my daughter could indicate the slots that she wouldn’t be able to revise.

![](https://sumproduct.com/wp-content/uploads/2025/05/7514979fece2a591a31180d385deed73-1.jpg)

When I first designed the solution, I included some Excel functions, but since this is a Power Query blog, I will ensure that I only use Power Query functions (apart from some formatting at the end!).

In [Part 1](https://sumproduct.com/blog/power-query-revision-time-part-1/)
, I converted my data into two \[2\] Tables: **Subjects** and **Availability**. I extracted **Subjects** to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/7c83bafe0789c24de076f6ee8688127d-1.jpg)

I created the **Availability** query by taking a copy of **Subjects**, and amending it:

![](https://sumproduct.com/wp-content/uploads/2025/05/7d8d8c053d9a8c0867ef10196375f829-1.jpg)

In [Part 2](https://sumproduct.com/blog/power-query-revision-time-part-2/)
, and [Part 3](https://sumproduct.com/blog/power-query-revision-time-part-3/)
, I calculated the number of subjects and the number of slots on **Availability** respectively.

This gave me both totals:

![](https://sumproduct.com/wp-content/uploads/2025/05/edbd574a4f5648cbe2d31340714c17c3-1.jpg)

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-4/)
, I calculated how many times each subject will appear in a new query, remembering to round up to whole slots.

![](https://sumproduct.com/wp-content/uploads/2025/05/49f95f862f88e473dba78b6964400189-1.jpg)

This tells me the number of slots that each subject should have for my example is three \[3\]:

![](https://sumproduct.com/wp-content/uploads/2025/05/142582a38e247514d4dd41c4fa66f0c1-1.jpg)

I am ready to allocate the slots. My goal is to create a table with each subject appearing three times. I will then allocate a random number to each subject slot so that I may put it into the timetable. I could approach this in different ways. I have decided to create a table based on the number of slots for each subject which I will then merge with the **Subjects** query.

I start with a new blank query by right-clicking in the Queries pane and choosing the appropriate menu path:

![](<Base64-Image-Removed>)

I call the new query **Random\_Subject**. I am going to use list functionality to create a simple list from one \[1\] to **Subject\_Slots**:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= {1..Subject\_Slots}**

This gives me a list, which I need to convert to a Table so that I may merge it:

![](<Base64-Image-Removed>)

I take the defaults to create the Table. To allow me to merge with the **Subjects** query, I need something to link to. I create a Custom Column from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

This very simple column, which I have called ‘**Link**‘, has a value of zero \[0\] for every row.

![](<Base64-Image-Removed>)

Before I go to the **Subjects** query to add a similar column, I select both columns and change the data type to ‘Whole Number’:

![](<Base64-Image-Removed>)

Now, I add a ‘Link’ column to **Subjects**:

![](<Base64-Image-Removed>)

Back in **Random\_Subject**, I choose to ‘Merge Queries’ from the Home tab:

![](<Base64-Image-Removed>)

I use the column **Link** to merge **Random\_Subject** and **Subjects**. I take the default ‘Left Outer’ join, since that will link each row in **Random\_Subject** to matching rows in **Subjects**, which will be all of them. In this example, because the rows all have the same value for the **Link** columns, any joins other than ‘Left Anti’ and ‘Right Anti’ will give me the data that I need.

![](<Base64-Image-Removed>)

I choose to expand the **Subjects** column, choosing only the column **Subject**:

![](<Base64-Image-Removed>)

I Click OK, and then select the new column **Subject**, and right-click to ‘Remove Other Columns’:

![](<Base64-Image-Removed>)

I have a list of all the slots I need for the timetable, but I need to find a way to randomly insert them into the timetable. This is where I will continue next week…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-5/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-5/#0 "close")

top