# Power Pivot Principles: Introducing the FILTERS Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the FILTERS Function

*   July 20, 2020

Power Pivot Principles: Introducing the FILTERS Function
========================================================

Power Pivot Principles: Introducing the FILTERS Function
========================================================

21 July 2020

_Welcome back to the Power Pivot Principles blog. This week, we will talk about the **FILTERS** function in DAX._

The **FILTERS** function returns the values that are directly applied as filters to the **columnName**. This function has the following syntax:

**FILTERS(columnName)**

For example, consider that we have **Sales** data already loaded into the Power Pivot Data Model:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-178-scaled-1.jpg)

We want to know the number of direct filters on the columns ‘**Store Key**‘, ‘**Product’** and ‘**Customer Key**‘ have been applied to the context where the expression is being evaluated.

In Power Pivot, we create the following measures:

*   ‘**Filters Store Key**‘:

**\=COUNTROWS(FILTERS(Sales\[Store Key\]))**

*   ‘**Filters Product**‘:

**\=COUNTROWS(FILTERS(Sales\[Product\]))**

*   ‘**Filters Customer Key’**:

**\=COUNTROWS(FILTERS(Sales\[Customer Key\]))**

They will give us results as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-166-scaled-1.jpg)

It may sound similar to the [**DISTINCT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-function)
 and the [**DISTINCTCOUNT**](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-function-distinctcount)
 functions we mentioned previously, so we’d want to compare between them, by creating measures using these functions. There is a slight difference between these two functions as we discussed [here](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-distinct-vs-distinctcount)
.

*   ‘**Distinct Store Key**‘:

**\=COUNTROWS(DISTINCT(Sales\[Store Key\]))**

*   ‘**Distinct Product**‘:

**\=COUNTROWS(DISTINCT(Sales\[Product\]))**

*   ‘**Distinctcount Customer Key**‘:

**\=DISTINCTCOUNT(Sales\[Customer Key\])**

They just give us exactly the same results:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-160-scaled-1.jpg)

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-filters-function/#0 "close")

top