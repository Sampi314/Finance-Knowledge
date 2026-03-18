# Power Pivot Principles: Basic Use of Calendar Table

**Source:** https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Basic Use of Calendar Table

*   September 3, 2018

Power Pivot Principles: Basic Use of Calendar Table
===================================================

Power Pivot Principles: Basic Use of Calendar Table
===================================================

4 September 2018

_Welcome back to our Power Pivot blog. Today, we discuss the steps we should take when creating a Calendar Table._

In our previous blog (link to previous blog) we discussed on the steps we have to take to create a Calendar table. In this blog, we will discuss how to create future PivotTables once we have linked our Calendar table.

When creating new PivotTables from our Power Pivot Data we should always use date sources from the Calendar Table. In fact, if you always call your date field in the Calendar table ‘Date’, then any time series function in DAX requiring a date should cite **Calendar\[Date\]** – simple!

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-574.jpg)

Create a PivotTable with fields from any table in the data model, then use the date fields from the Calendar Table.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-595.jpg)

It is important to use the Calendar Table because all of the time intelligence for example the **DATESYTD** function, requires the contiguous dates to function properly.

We will cover the **DATESYTD** function next week.

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/#0)

[](https://sumproduct.com/blog/power-pivot-principles-basic-use-of-calendar-table/#0 "close")

top