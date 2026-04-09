# Power Pivot Principles: Introducing the DATESYTD Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the DATESYTD Function

*   September 10, 2018

Power Pivot Principles: Introducing the DATESYTD Function
=========================================================

Power Pivot Principles: Introducing the DATESYTD Function
=========================================================

11 September 2018

_Welcome back to our Power Pivot blog. Today, we introduce one our first time intelligence functions._

**DATESYTD** is a time intelligence function that, like all time series functions, requires contiguous dates in order to work properly (although some are becoming “forgiving”). The **DATESYTD** function returns values in a PivotTable that contain aggregated data for the year to date. The syntax of this function is:

**DATESYD(<dates>\[,year\_end\_date>\])**

It’s commonly used with our old friend, the **CALCULATE** function. To demonstrate, let’s create a measure using the **DATESYTD** function to show year to date sales:

![](<Base64-Image-Removed>)

The next step is to create our PivotTable report.

![](<Base64-Image-Removed>)

We can now see the total sales for the month and the total sales YTD (year to date) throughout the year. Notice that the year and month are both in the same column (column **B**) of the PivotTable. For many functions, this is necessary for the time series calculation to work correctly. If years were put in row 3 instead with months down column **B**, many formulae would not work as intended – hence the need for what is known as _contiguity_.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-datesytd-function/#0 "close")

top