# Power BI Blog: The COALESCE Function

**Source:** https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: The COALESCE Function

*   July 8, 2020

Power BI Blog: The COALESCE Function
====================================

Power BI Blog: The COALESCE Function
====================================

9 July 2020

_Welcome back to this week’s edition of the Power BI blog series. This week,_ _we look_ _at how to use the new COALESCE function._

After an update in March, Power BI has received a new function in its DAX arsenal: the **COALESCE** function. This function has the following syntax:

**COALESCE**( **expression**, **expression\[**, **expression …\])**

The **expression** parameter must return a scalar value.

The **COALESCE** function will evaluate the first **expression** and if it returns with a blank value it will return with the second **expression** in the formula. If there are more than two **expressions** the function will continue to cascade to the next **expression** if all of the previous **expression** arguments evaluate to blank.

Confusing? Let’s consider an example. We are going to use the following dataset:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-185-1.jpg)

After loading the data into Power BI, we create some simple measures to calculate the total sales for the BizSupplies division.

We may create a simple card visualisation that illustrates the total sales:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-174-1.jpg)

Let’s imagine we want to have a slicer so that the user may toggle the monthly breakdown of sales:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-170-1.jpg)

However, notice that when August is selected, the card returns with (Blank). Although it should return with zero (0) since no sales were made in that month. To avoid this, we may use the **IF** and **ISBLANK** functions to tell Power BI, if the measure evaluates to blank, we want it to return zero (0):

**Total Sales IF Blank = IF(ISBLANK(\[Total Sales\]),0,\[Total Sales\])**

![](<Base64-Image-Removed>)

Now Power BI will produce zero (0) if blank is returned. Can we simplify this code? We can try using the **COALESCE** function instead:

**Total Sales Coalesce = COALESCE(\[Total Sales\],0)**

The following screenshot will illustrate the results for the three measures:

![](<Base64-Image-Removed>)

As you can see, we have achieved the output of the **IF** and **ISBLANK** functions with a much simpler line of code! A shorter line of code means it is easier for users to understand and saves the creator time when writing DAX code. Furthermore, it is important to note that the structure of the **COALESCE** function allows the creator to avoid using nested **IF**s measures should there be multiple expressions that may be blank.

That’s it for this week, come back next week for more on Power BI.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/#0)

[](https://sumproduct.com/blog/power-bi-blog-the-coalesce-function/#0 "close")

top