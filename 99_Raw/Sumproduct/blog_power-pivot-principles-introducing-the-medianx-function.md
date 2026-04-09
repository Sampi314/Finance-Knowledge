# Power Pivot Principles: Introducing the MEDIANX Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the MEDIANX Function

*   May 13, 2019

Power Pivot Principles: Introducing the MEDIANX Function
========================================================

Power Pivot Principles: Introducing the MEDIANX Function
========================================================

14 May 2019

_Welcome back to our Power Pivot blog. Today, we look at the MEDIANX function._

Last week we introduced the **MEDIAN** function, so this week we thought it would be appropriate to talk about the **MEDIANX** function. That’s right: this one is ‘X’ rated. We detailed what ‘median’ means and how to use the **MEDIAN** function in last week’s blog [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-median-function)
.

Just like the **MEDIAN** function, the **MEDIANX** function also returns the median value from a column of values in a data table. The ‘**X**‘ at the end of the function name highlights the fact that **MEDIANX** works on a record by record basis, rather than in aggregation (similar to [SUMX](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-sumx-function)
). Also, unlike the **MEDIAN** function, the **MEDIANX** function does not ignore blanks and it also has different inputs.

The **MEDIANX** function uses the following syntax:

**MEDIANX**( <table>, <expression> )

The **MEDIANX** requires a <table> input. This means that we can embed another function that returns a table, including the **FILTER** function, followed by an <expression> for the **MEDIANX** function to work.

Let’s take a look at an example. We have assigned Australian states to each value:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-432.jpg)

Let’s create four measures that will calculate the median value for each state. For example, for NSW the measure would be:

\=MEDIANX(

FILTER(

MedianX\_Example,\[Category\]=”NSW”

)

,MedianX\_Example\[Data Set\]

)

Looking at our PivotTable:

![](<Base64-Image-Removed>)

We can create measures for the rest of the states (these measures are similar, we just have to change the “NSW” text in the measure above to the new state), _viz._

![](<Base64-Image-Removed>)

As we can see, the **MEDIANX** also sorts the dataset into ascending order before calculating the median value, so it will ignore any sorting that we apply to the column.

Let’s see what happens when we add some blank values into our data set:

![](<Base64-Image-Removed>)

Refreshing the same PivotTable, the median for NSW has changed from 151 to 127, this is because the **MEDIANX** function **DOES****NOT** ignore blank values.

![](<Base64-Image-Removed>)

It is important to keep that in mind when using the **MEDIANX**. It does not ignore blank values in the dataset. Therefore, be sure to clear out blank values in the dataset before calculating the median value.

That’s it for this week, tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-medianx-function/#0 "close")

top