# Power Pivot Principles: Introducing the CLOSINGBALANCEMONTH Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the CLOSINGBALANCEMONTH Function

*   October 1, 2018

Power Pivot Principles: Introducing the CLOSINGBALANCEMONTH Function
====================================================================

Power Pivot Principles: Introducing the CLOSINGBALANCEMONTH Function
====================================================================

2 October 2018

_Welcome back to our Power Pivot blog. Today, we introduce the CLOSINGBALANCEMONTH function._

**CLOSINGBALANCEMONTH** is a time intelligence function similar to the **DATESYTD** (you can read about the **DATESYTD** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-datesytd-function)
). The **CLOSINGBALANCEMONTH** function, like all time series functions, requires contiguous dates to work properly.

The **CLOSINGBALANCEMONTH** has the following syntax:

**CLOSINGBALANCEMONTH(<expression>,<dates>\[,<filter>\])**

The **CLOSINGBALANCEMONTH** function can be used to generate balance sheet values, as we want to view the inventory balance at the _end_ of a period.

We have the following inventory table containing T-Shirt data from the months of January 2017 to June 2017. Do note, for simplicity’s sake our example table already contains contiguous dates.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-558.jpg)

After importing the table into Power Pivot let’s create a measure using the **CLOSINGBALANCEMONTH** function:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-580.jpg)

The next step is to create the following PivotTable:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-537.jpg)

The PivotTable now displays the inventory closing balance amount at the end of the month. From here we can use these values for our financial reports.

That’s all for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-closingbalancemonth-function/#0 "close")

top