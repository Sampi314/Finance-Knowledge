# Power BI Blog: Dating Part 5

**Source:** https://sumproduct.com/blog/power-bi-blog-dating-part-5/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dating Part 5

*   February 2, 2022

Power BI Blog: Dating Part 5
============================

Power BI Blog: Dating Part 5
============================

3 February 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we create a month name column and add it to the hierarchy for **Calendar1**._

In [Power BI Blog: Dating Part 2](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-2)
, we generated a simple Date Table using the **DAX CALENDAR()** function, which we called **Calendar1**. We used **Calendar1** to link the other tables in our simple Data Model.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-71.jpg)

This enabled us to display the data from **Costs** and **Sales** correctly in a Matrix visualisation:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-97.jpg)

We completed **Calendar 1** by marking it as a Date Table and adding more columns in [Power BI Blog: Dating Part 3](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-3)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-74.jpg)

We created the **Year Hierarchy** in [Power BI Blog: Dating Part 4](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-4)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-68.jpg)

This allowed us to drill down and up in the Matrix visualisation:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-56.jpg)

We need to refine the **Calendar1** columns to make them easier to interpret. Month numbers aren’t very user friendly in a Matrix: it would be easier to interpret the data if we use the month name instead. We can do this by adding a new column to **Calendar1** in the Data view:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-48.jpg)

The new column will be called ‘**Month Name**‘:

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-45.jpg)

The **DAX** code we have used is:

**Month Name =** **Format****(****\[Date\]****,****“MMM”****)**

This extracts the month from the date in the format ‘MMM’. This format is ideal for the Matrix, as each column will be roughly the same width.

In the Model View, we need to amend the **Year Hierarchy** so that it includes **Month Name** instead of **Month Number**. We start by dragging **Month Name** into **Year Hierarchy** in the Fields pane:

![](<Base64-Image-Removed>)

We select **Year Hierarchy**, and in the Properties pane, we can delete **Month Number** using the cross next to the field. Note that no changes will be made to **Year Hierarch**y until we ‘Apply Level Changes’.

![](<Base64-Image-Removed>)

There is a feature when making changes here, which we could call a bug! We can click and drag the fields to reorder them within **Year Hierarchy**, but at this point these changes will not be saved, as the level deletion is performed first.

![](<Base64-Image-Removed>)

We can now choose to ‘Apply Level Changes’. Power BI prompts us to confirm the deletion:

![](<Base64-Image-Removed>)

We click OK, and the deletion occurs, but the change to the order of the hierarchy levels has not been saved:

![](<Base64-Image-Removed>)

We click and drag again:

![](<Base64-Image-Removed>)

This time when we ‘Apply Level Changes’, the order is changed:

![](<Base64-Image-Removed>)

When we go back to the Report View, we may expect to see the **Month Name** in the Matrix:

![](<Base64-Image-Removed>)

Clearly, we have more work to do! Next time, we will work on the Matrix to resolve the issues…

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dating-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dating-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dating-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dating-part-5/#0)

[](https://sumproduct.com/blog/power-bi-blog-dating-part-5/#0 "close")

top