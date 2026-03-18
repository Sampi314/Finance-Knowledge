# Power Query: Revision Time – Part 12

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-12/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 12

*   June 25, 2024

Power Query: Revision Time – Part 12
====================================

Power Query: Revision Time – Part 12
====================================

26 June 2024

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

In [Part 8](https://sumproduct.com/blog/power-query-revision-time-part-8/)
, I appended the slot number data to the rest of the **TimeTable** query.

![](<Base64-Image-Removed>)

In [Part 9](https://sumproduct.com/blog/power-query-revision-time-part-9/)
, I removed the duplicate values.

![](<Base64-Image-Removed>)

However, as I said in [Part 8](https://sumproduct.com/blog/power-query-revision-time-part-8/)
, I could have transformed the data in **TimeTable** by merging instead of appending, and I looked at that in [Part 10](https://sumproduct.com/blog/power-query-revision-time-part-10/)
:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-11/)
, I merged **TimeTable** with the **Random\_Subject** query, and transformed the result to get the final TimeTable query:

![](<Base64-Image-Removed>)

I choose ‘Close & Load To…’ from the ‘Close & Load’ dropdown in the Home tab. This is because I don’t want to load all the queries to the workbook.

![](<Base64-Image-Removed>)

This takes me back to the workbook and prompts me with a dialog. I choose ‘Only Create Connection’, as I will choose the query I wish to load individually:

![](<Base64-Image-Removed>)

I then right-click on **TimeTable** to access the dialog again:

![](<Base64-Image-Removed>)

I choose to load it to a new worksheet, so that I may print it out:

![](<Base64-Image-Removed>)

I can format my table using ‘Conditional Formatting’:

![](<Base64-Image-Removed>)

I have chosen a dark grey fill and no text to appear for those cells containing ‘x’:

![](<Base64-Image-Removed>)

I can refresh to change the random generation of subject slots, and when my daughter can revise during the day, I simply remove some of the ‘x’ values:

![](<Base64-Image-Removed>)

Then, I refresh the **TimeTable** Query:

![](<Base64-Image-Removed>)

The timetable is updated with more slots.

![](<Base64-Image-Removed>)

My timetable is working as required, and ready to be ignored!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-12/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-12/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-12/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-12/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-12/#0 "close")

top