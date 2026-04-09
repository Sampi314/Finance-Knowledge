# Power Query: Time for a List

**Source:** https://sumproduct.com/blog/power-query-time-for-a-list/

---

[Home](https://sumproduct.com/)

\> Power Query: Time for a List

*   November 19, 2019

Power Query: Time for a List
============================

Power Query: Time for a List
============================

20 November 2019

_There are three **M** functions in Power Query that will allow me to create a time dimension:_

*   **List.Dates(start** as date, **count** as number, **step** as duration**)** as list
    
    This returns a list of date values of size **count**, starting at **start**. The given increment, **step**, is a **duration** value that is added to every value
    
*   **List.Times(start** as time, **count** as number, **step** as duration**)** as list
    
    This returns a list of **time** values of size **count**, starting at **start****.** The given increment, **step**, is a **duration** value that is added to every value
    
*   **List.DateTimes(start** as datetime, **count** as number, **step** as duration**)** as list
    
    This returns a list of **datetime** values of size **count**, starting at **start**. The given increment, **step**, is a **duration** value that is added to every value.
    

I start with the **List.Dates()** function. I create a new blank query as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-323.jpg)

I create a new step.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-327.jpg)

The **M** code I am using is

**\= List.Dates(DateTime.Date(DateTime.LocalNow()), 7, #duration(-1, 0, 0, 0))**

which takes the current date and subtracts a day a total of seven (7) times.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-313.jpg)

This gives me the last seven days. I can convert my list to a table using ‘List Tools’, and I rename my new column **Date**.

To show how **List.Times()** works, I add a new ‘Custom Column’ from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= List.Times(#time(0, 0, 0), 96, #duration(0, 0, 15, 0))**

There are 96 quarter-hours in 24 hours, so this will divide each day into 15-minute segments.

![](<Base64-Image-Removed>)

I need to expand my list into rows.

![](<Base64-Image-Removed>)

I choose to ‘Expand to New Rows’:

![](<Base64-Image-Removed>)

I could combine these columns, if I wish, by creating a new custom column.

![](<Base64-Image-Removed>)

This will give me a new **DateTime** column.

![](<Base64-Image-Removed>)

**List.DateTimes()** allows me to create datetime entries at intervals starting from a particular point in time, for example, now. I can show this in a new blank query:

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= List.DateTimes(DateTime.LocalNow(),672, #duration(0, 0, 15, 0))**

which gives me 96 x 7 intervals of 15 minutes (i.e. the next seven days).

![](<Base64-Image-Removed>)

I can convert and rename as before.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-time-for-a-list/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-time-for-a-list/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-time-for-a-list/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-time-for-a-list/#0)

[](https://sumproduct.com/blog/power-query-time-for-a-list/#0 "close")

top