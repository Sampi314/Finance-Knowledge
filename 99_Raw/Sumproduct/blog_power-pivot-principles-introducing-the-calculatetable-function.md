# Power Pivot Principles: Introducing the CALCULATETABLE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the CALCULATETABLE Function

*   February 25, 2019

Power Pivot Principles: Introducing the CALCULATETABLE Function
===============================================================

Power Pivot Principles: Introducing the CALCULATETABLE Function
===============================================================

26 February 2019

_Welcome back to our Power Pivot blog. Today, we discuss the **CALCULATETABLE** function._

The **CALCULATETABLE** function is somewhat similar to the **CALCULATE** function in Power Pivot, in that it applies filters to the data returned with a calculated value. The main difference between the two is that the **CALCULATETABLE** function returns with a table whereas the **CALCULATE** function returns with a scalar value.

The **CALCULATETABLE** requires the following syntax to operate:

**CALCULATETABLE**( **<expression>**, **<filter1>**, **<filter2>**, …)

The **<expression>** is the table to be evaluated, and the **<filter>** is a column that can be located in any table imported to Power Pivot. In order for the filters to work they have to be from tables that have proper connections established in the data model.

**_Example_**

Let’s create a measure that calculates the sales for division 3 in the year 2020:

\=CALCULATETABLE(

‘Sales Table’,’Calendar'\[Year\]=2020

)

Using the **CALCULATETABLE** formula alone will not work, as Power Pivot will return with the error:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-480.jpg)

As it stands above, the current **CALCULATETABLE** measure returns with a table looking like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-496.jpg)

Power Pivot can’t aggregate an entire table into a single cell. We have to specify which expression we want to be evaluated.

We have to use the **SUMX** function. To refresh your memory, the **SUMX** function ‘returns the sum of an expression evaluated for each row in a table’, it requires the following syntax to operate (you can read more on the **SUMX** function [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sumx-function)
):

\=**SUMX**( **<table>**, **<expression>**)

With that in mind we can adjust our previous measure:

\=SUMX(

CALCULATETABLE(‘Sales Table’,’Calendar'\[Year\]=2020)

, \[Division 3\]

)

![](<Base64-Image-Removed>)

The resulting PivotTable:

![](<Base64-Image-Removed>)

Of course, this result can be achieved using the **CALCULATE** function:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

As it stands the **CALCULATETABLE** and the **CALCULATE** functions are quite similar. The key difference is their outputs. We would use the **CALCULATETABLE** function when we need to use other functions that expect a table as an expression and **CALCULATE** when we use functions that expect a single value.

That’s it for this week, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-calculatetable-function/#0 "close")

top