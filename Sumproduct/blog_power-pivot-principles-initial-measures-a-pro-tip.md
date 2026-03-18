# Power Pivot Principles: Initial Measures – a Pro Tip

**Source:** https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Initial Measures – a Pro Tip

*   May 31, 2021

Power Pivot Principles: Initial Measures – a Pro Tip
====================================================

Power Pivot Principles: Initial Measures – a Pro Tip
====================================================

1 June 2021

_Welcome back to the Power Pivot Principles blog. This week, we explain the advantages of creating measures from fields. Who’d have thought..?_

I can’t believe it’s taken 176 blogs to come up with this tip that we take for granted when building models in Power Pivot and Power BI. It’s deceptively simple but can avoid a lot of problems later.

Consider the following dataset:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-187.jpg)

This Excel Table, **Example**, contains just two fields, **Sales** and **Costs**. Let’s imagine we have imported this Table into Power Pivot in a usual way (_e.g._ from the ‘Power Pivot’, click on ‘Add to Data Model’) and we want to create a **Gross Profit** measure.

We could simply create the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-245.jpg)

**\=SUM(Example\[Sales\])-SUM(Example\[Costs\])**

(Don’t forget you need to aggregate fields, using **DAX** functions such as **SUM**, **AVERAGE**, **MAX** or **MIN** otherwise this measure will not resolve.)

This will work and we often see people build **DAX** formulae this way. But we don’t. In this example, we might create the following two measures first, where we make a measure out of each field we reference:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-196.jpg)

_i.e._ a measure called **Total Sales**,

**\=SUM(Example\[Sales\])**

and another called **Total Costs**:

![](<Base64-Image-Removed>)

**\=SUM(Example\[Costs\])**

Then, and only then, do we create our **Gross Profit** measure:

![](<Base64-Image-Removed>)

**\=\[Total Sales\]-\[Total Costs\]**

There are two advantages in creating these interim measures out of the reference fields:

1.  Dependent formulae are easier to read
2.  Should the field names in the source change you only need to change the definition of the original measure, created from the field. You do not need to propagate this change throughout all measures that reference the field _because they don’t_. This creates much less work (you have control over all measure names) and leaves a better audit trail too.

The simplest ideas are often the best.

That’s it for this week!

Come back next week to see how we use the disconnected table for performing a sensitivity analysis by staying tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/#0)

[](https://sumproduct.com/blog/power-pivot-principles-initial-measures-a-pro-tip/#0 "close")

top