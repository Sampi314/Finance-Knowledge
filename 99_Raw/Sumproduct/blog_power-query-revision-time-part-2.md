# Power Query: Revision Time – Part 2

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 2

*   April 16, 2024

Power Query: Revision Time – Part 2
===================================

Power Query: Revision Time – Part 2
===================================

17 April 2024

_Welcome to our Power Query blog. Today, I continue to create a refreshable revision timetable by calculating the number of subjects to be studied._

As my salespeople take a well-earned break, many students here in the UK are preparing for exams in the summer. To help my own offspring get organised, I volunteered to create a refreshable printable revision timetable. This is the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/42f1ea24b25c47ac542c597805873a9e-1.jpg)

I needed a list of topics, and to begin with, I created extra entries for topics that required more timeslots:

![](https://sumproduct.com/wp-content/uploads/2025/05/2c1f230e1f9e3f0bbf351cc97f3ee835-1.jpg)

We agreed on half-hourly slots, and I created a grid so that my daughter could indicate the slots that she wouldn’t be able to revise.

![](https://sumproduct.com/wp-content/uploads/2025/05/36ff5871a92ded76fd430f119d192511-1.jpg)

When I first designed the solution, I included some Excel functions, but since this is a Power Query blog, I will ensure that I only use Power Query functions (apart from some formatting at the end!).

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-1/)
, I converted my data into two \[2\] Tables: **Subjects** and **Availability**. I extracted **Subjects** to Power Query.

![](https://sumproduct.com/wp-content/uploads/2025/05/64146b75339467e7606f0ca450b4f59e-1.jpg)

I created the **Availability** query by taking a copy of **Subjects**, and amending it:

![](https://sumproduct.com/wp-content/uploads/2025/05/a26ac35c42115f9d8dd51dcf7c1662ef-1.jpg)

Now I have the subject and slot information, I need to perform some basic calculations. I could have performed this in Excel, but as this is a Power Query blog, I will be using **M** here.

The first number I need is the number of subjects. An easy way to calculate this begins with taking a reference copy of the **Subjects** query:

![](https://sumproduct.com/wp-content/uploads/2025/05/e68225ca21f8f3413089eb95c49fd586-1.jpg)

Using a reference copy means my new query will be updated if **Subjects** changes. I name my new query ‘Subjects\_Total’ and select the ‘Group By’ functionality from the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/b3cd032e3788eef0d387aa4e8b439191-1.jpg)

I have selected the Advanced options. Although the defaults in the aggregation section are correct in that I do wish to count rows, I do not want to group them by **Subject**. If I hover the cursor to the right of the grouping section, I have more options in Advanced mode:

![](<Base64-Image-Removed>)

In particular, I may delete the grouping:

![](<Base64-Image-Removed>)

I choose to do this, and then click OK:

![](<Base64-Image-Removed>)

To access the number in the cell, I click in the cell and right-click to ‘Drill down’:

![](<Base64-Image-Removed>)

This gives me a query consisting of a number:

![](<Base64-Image-Removed>)

Calculating the number of slots on **Availability** will require a difference approach, since I need to consider the values in multiple columns:

![](<Base64-Image-Removed>)

I will describe a method to achieve this next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-2/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-2/#0 "close")

top