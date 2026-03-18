# Power BI Blog: Dating Part 4

**Source:** https://sumproduct.com/blog/power-bi-blog-dating-part-4/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dating Part 4

*   January 26, 2022

Power BI Blog: Dating Part 4
============================

Power BI Blog: Dating Part 4
============================

27 January 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we create a hierarchy for **Calendar1**._

Cast your mind back to [Power BI Blog: Dating Part 2](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-2)
, where we generated a simple Date Table using the DAX **CALENDAR()** function, which we called **Calendar1**. We used **Calendar1** to link the other tables in our simple Data Model.

![](<Base64-Image-Removed>)

This enabled us to display the data from **Costs** and **Sales** correctly in a matrix visualisation:

![](<Base64-Image-Removed>)

We completed **Calendar1** by marking it as a Date Table and adding more columns in [Power BI Blog: Dating Part 3](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-3)
.

![](<Base64-Image-Removed>)

Although we have the columns we need for a hierarchy, the ability to drill down is not available in the matrix visualisation:

![](<Base64-Image-Removed>)

The date hierarchy is not automatically available because we turned off auto Date/Time in [Power BI Blog: Dating Part 1](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-1)
. Therefore, we will need to create our own hierarchy. Users of older versions of Power BI may expect to be able to drag and drop **Qtr** in **Year** in the Fields pane, but this is no longer possible:

![](<Base64-Image-Removed>)

This feature was removed because users were accidentally creating hierarchies more often than they deliberately created them! Now, to create a hierarchy, we start by right-clicking on **Year.**

![](<Base64-Image-Removed>)

Choosing the option to ‘Create hierarchy’ we create **Year Hierarchy**, which contains **Year**:

![](<Base64-Image-Removed>)

We still can’t add to this on the Fields pane by clicking and dragging, but we can right-click on the next column in the hierarchy, which is **Qtr**.

![](<Base64-Image-Removed>)

We can select ‘Add to hierarchy’ and then ‘Year Hierarchy’ to add **Qtr.**

![](<Base64-Image-Removed>)

We can repeat this process for **Month Number** and **Day.**

![](<Base64-Image-Removed>)

Now we can drag **Year Hierarchy** to the matrix visualisation instead of **Date**:

![](<Base64-Image-Removed>)

Looking at the visualisation, we now have drill down options:

![](<Base64-Image-Removed>)

We can use these to view the data at different levels:

![](<Base64-Image-Removed>)

It’s getting better, but we need to refine the **Calendar1** columns to make them easier to interpret. We will address this next time…

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dating-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dating-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dating-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dating-part-4/#0)

[](https://sumproduct.com/blog/power-bi-blog-dating-part-4/#0 "close")

top