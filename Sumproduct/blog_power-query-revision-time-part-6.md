# Power Query: Revision Time – Part 6

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 6

*   May 14, 2024

Power Query: Revision Time – Part 6
===================================

Power Query: Revision Time – Part 6
===================================

15 May 2024

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

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-5/)
, I created a table where each subject appeared three times (_i.e_. the number of times given by **Subject\_Slots**).

![](<Base64-Image-Removed>)

I now have a list of slots to insert in the timetable. I need a unique identifier for each slot, but I need them to be in a random order. I add a new custom column from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

I have used the **M** code:

**\= Number.RandomBetween(1,Slot\_Total)**

Which gives me a number in the range one \[1\] to **Slot\_Total**. I could have used any number as the top limit, but to avoid more hard-coding, **Slot\_Total** is a suitable number here.

Now I have some random numbers, I am going to sort the data in ascending order.

![](<Base64-Image-Removed>)

The data type of this column is not important as I will be deleting it shortly. Having ordered my data, I create an Index column beginning at one \[1\] from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

Now I have my data in a random order, I delete **Slot Number**.

![](<Base64-Image-Removed>)

Next time, I will prepare the data from the **Availability** so that I can add in the slot data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-6/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-6/#0 "close")

top