# Power Pivot Principles: Counting Working Days

**Source:** https://sumproduct.com/blog/power-pivot-principles-counting-working-days/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Counting Working Days

*   January 13, 2020

Power Pivot Principles: Counting Working Days
=============================================

Power Pivot Principles: Counting Working Days
=============================================

14 January 2020

_Welcome back to the Power Pivot Principles blog. This week, we are going to learn a method to calculate the working days using PowerPivot._

DAX can compute the difference between two dates by subtracting one from the other (assuming the start date is not to be counted). This produces the number of days between the two dates – a simple task that can be done by a calculated column. However, in a real business case, we need to calculate the working days between two different dates. Let’s look at one such example.

Consider the data table (not displayed in full):

![](<Base64-Image-Removed>)

This data table contains the **Order Date** and **Delivery Date**. The **Delivery Days** is the difference between two dates, _i.e._ it excludes the **Order Date** from the calculation. The delivery days calculated here includes weekends. We also create another calendar table in PowerPivot by using the method introduced previously [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-creating-a-calendar-table)
. The two tables are linked as follows:

![](<Base64-Image-Removed>)

In order to get the working days between two dates, one solution to this scenario is to create a calculated column – **IsWorkingDay**, which indicates that if a particular day is a working day or not. We can write the following calculated column in the table **Calendar**:

![](<Base64-Image-Removed>)

We use the nested function **IF** with function **WEEKDAY** to determine if the **Date** is working day or not. **WEEKDAY** function returns a number from 1 to 7 identifying the day of the week of a date. By default, the day ranges from 1 (Sunday) to 7 (Saturday). In this case, we use return type 2 which indicates that week begins on Monday (1) and ends on Sunday (7). If the day number returned is not 6 or 7, it is a working day and the value 1 is returned (ignoring holidays).

Next, we build the calculated column **Delivery Days Exclude Weekend** in the **Delivery** Table.

![](<Base64-Image-Removed>)

We use **CALCULATE** to counts the rows in the **Calendar** table by filtering the selection criteria **IsWorkingDay = 1** and the days returned from **DATESBETWEEN** between **Order Date** and **Delivery Date**. The result would be:

![](<Base64-Image-Removed>)

The column **Delivery Days Exclude Weekend** correctly calculates the working days between **Order Date** and **Delivery Date**.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-counting-working-days/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-counting-working-days/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-counting-working-days/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-counting-working-days/#0)

[](https://sumproduct.com/blog/power-pivot-principles-counting-working-days/#0 "close")

top