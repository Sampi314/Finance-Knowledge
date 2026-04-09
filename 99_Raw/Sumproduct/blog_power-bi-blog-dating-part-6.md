# Power BI Blog: Dating Part 6

**Source:** https://sumproduct.com/blog/power-bi-blog-dating-part-6/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Dating Part 6

*   February 9, 2022

Power BI Blog: Dating Part 6
============================

Power BI Blog: Dating Part 6
============================

10 February 2022

_Welcome back to this week’s edition of the Power BI blog series. This week, we continue formatting the Matrix using the amended hierarchy for **Calendar1**._

In [Power BI Blog: Dating Part 2](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-2)
, we generated a simple Date Table using the **DAX CALENDAR()** function, which we called **Calendar1**. We used **Calendar1** to link the other tables in our simple Data Model.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-67.jpg)

This enabled us to display the data from **Costs** and **Sales** correctly in a Matrix visualisation:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-92.jpg)

We completed **Calendar 1** by marking it as a Date Table and adding more columns in [Power BI Blog: Dating Part 3](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-3)
.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-70.jpg)

We created the **Year Hierarchy** in [Power BI Blog: Dating Part 4](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-4)
:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-64.jpg)

In [Power BI Blog: Dating Part 5](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-dating-part-5)
, we created a new column **Month Name**, and we replaced **Month Number** in **Year Hierarchy** with **Month Name**. Unfortunately, this didn’t quite have the effect we were looking for on the Matrix:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-52.jpg)

To see what is wrong, we click on ‘See Details’:

![](https://sumproduct.com/wp-content/uploads/2025/05/23912d3b1671861e02bebcd5183f1607-44.jpg)

The Matrix is still expecting to use **Month Number** in **Year Hierarchy**. To fix this, we remove **Year Hierarchy** from ‘Columns’ in the Visualizations pane, which we can do by clicking on the cross next to the top **Year Hierarchy** (notice that instead of **Month Number**, we have an exclamation mark telling us that something is wrong with **Year Hierarchy**):

![](https://sumproduct.com/wp-content/uploads/2025/05/6f49c288a0d88a66b427eaf4ece923d6-41.jpg)

We can then drag the current **Year Hierarchy** back into ‘Columns’:

![](https://sumproduct.com/wp-content/uploads/2025/05/b9ee28d90e6b5bc92ea4aeafdad51628-31.jpg)

We can now view and drill down into the Matrix:

![](https://sumproduct.com/wp-content/uploads/2025/05/0485ccbc83bdeec1d741bad442a1ea5f-27.jpg)

We have month names, but they are no longer in the right order. To fix this we go back to the Data view:

![](<Base64-Image-Removed>)

We can use the ‘Sort by Column’ dropdown and sort **Month Name** by **Month Number**:

![](<Base64-Image-Removed>)

Having done this, we can return to the Report View:

![](<Base64-Image-Removed>)

The month information is now much clearer.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-dating-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-dating-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-dating-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-dating-part-6/#0)

[](https://sumproduct.com/blog/power-bi-blog-dating-part-6/#0 "close")

top