# Power Query: Revision Time – Part 3

**Source:** https://sumproduct.com/blog/power-query-revision-time-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Revision Time – Part 3

*   April 23, 2024

Power Query: Revision Time – Part 3
===================================

Power Query: Revision Time – Part 3
===================================

24 April 2024

_Welcome to our Power Query blog. Today, I continue to create a refreshable revision timetable by calculating the number of slots available._

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

[Last time](https://sumproduct.com/blog/power-query-revision-time-part-2/)
, I calculated the number of subjects by referencing the **Subjects** query and grouping the results. This gave me the **Subjects\_Total** query, consisting of a number:

![](<Base64-Image-Removed>)

Calculating the number of slots on **Availability** will require a difference approach, since I need to consider the values in multiple columns:

![](<Base64-Image-Removed>)

I will start by creating a reference query from **Availability** in the same way that I did for **Subjects**. I will call it **Slot\_Total**:

![](<Base64-Image-Removed>)

To get all the slots available in one column that I may group, I could unpivot the day columns. However, at the moment, the available slots contain the value _null_:

![](<Base64-Image-Removed>)

If I were to select **Time Slot** and right-click to ‘Unpivot other columns’:

![](<Base64-Image-Removed>)

I might think I have all the slots in one column. However, if I look at the filter options, I only have the slots with value ‘x’: the _null_ values have been removed during the unpivot process.

![](<Base64-Image-Removed>)

To rectify this, I need to replace the _null_ values with an empty space. I will insert a step after the Source step. I select all columns by selecting any column heading and using **CTRL** + **A.** I access the right-click menu:

![](<Base64-Image-Removed>)

I receive a warning telling me I am inserting a step, and I choose to Insert:

![](<Base64-Image-Removed>)

In the dialog that appears, I choose to replace any _null_ value with an empty cell:

![](<Base64-Image-Removed>)

I click OK and go to the last step:

![](<Base64-Image-Removed>)

The blank values have been included, and I may uncheck the ‘x’ value:

![](<Base64-Image-Removed>)

This gives me all the available rows, and I may group them and drill down into the total cell using the same method I used [last week](https://sumproduct.com/blog/power-query-revision-time-part-2/)
:

![](<Base64-Image-Removed>)

Now I have the number of subjects and the number of slots, I can calculate how many times each subject will appear. This is where I will continue next time.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-revision-time-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-revision-time-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-revision-time-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-revision-time-part-3/#0)

[](https://sumproduct.com/blog/power-query-revision-time-part-3/#0 "close")

top