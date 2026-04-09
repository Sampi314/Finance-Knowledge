# Power BI Blog: More on Visual Calculations Part 2

**Source:** https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: More on Visual Calculations Part 2

*   April 10, 2024

Power BI Blog: More on Visual Calculations Part 2
=================================================

Power BI Blog: More on Visual Calculations Part 2
=================================================

11 April 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we take a deeper look at some more of the visual calculations available in this exciting new preview feature._

[Recently](https://www.sumproduct.com/blog/article/power-bi-tips/visual-calculations-in-preview)
, we introduced to you the Preview feature: visual calculations. [Last time](https://www.sumproduct.com/blog/article/power-bi-tips/more-on-visual-calculations-part-1)
, we demonstrated how **RUNNINGSUM** could help us, and went on the look at some of the advantages and disadvantages when using visual calculations.

We left you with a list of the visual calculations available at the time of writing:

*   **COLLAPSE**: calculation is evaluated at a higher level of the axis
*   **COLLAPSEALL**: calculation is evaluated at the total level of the axis
*   **EXPAND**: calculation is evaluated at a lower level of the axis
*   **EXPANDALL**: calculation is evaluated at the leaf level of the axis
*   **FIRST**: refers to the first row of an axis
*   **ISATLEVEL**: reports whether a specified column is present at the current level
*   **LAST**: refers to the last row of an axis
*   **MOVINGAVERAGE**: adds a moving average on an axis
*   **NEXT**: refers to a next row of an axis
*   **PREVIOUS**: refers to a previous row of an axis
*   **RANGE**: refers to a slice of rows of an axis
*   **RUNNINGSUM**: adds a running sum on an axis.

Some functions, for example **MOVINGAVERAGE** or **PREVIOUS** simply provide the functionality suggested by their names. However, visual calculations provide more level-flexibility by using the functions **COLLAPSE** / **COLLAPSEALL** and **EXPAND** / **EXPANDALL**, so let’s take a closer look at these.

The function **COLLAPSE** evaluates a calculation at a higher level of the axis and the function **COLLAPSEALL** evaluates a calculation at the total level of the axis. The function **EXPAND** evaluates a calculation at a lower level of the axis and the function **EXPANDALL** evaluates a calculation at the leaf level of the axis.

In the following example built on Power BI’s default ‘Financial Samples’ dataset, we created a matrix with the field **Profit** listed over months:

![](<Base64-Image-Removed>)

If we apply the **COLLAPSE** function on **Profit** we will evaluate it at a higher level – in this case, the yearly subtotals.

![](<Base64-Image-Removed>)

Let’s consider another example on distinct counts of product types with the same dataset.

![](<Base64-Image-Removed>)

There are six \[6\] types of products in the dataset, and the subtotals and the overall total show that the distinct counts are always six \[6\] either within each year or over the whole dataset. However, if we apply the **EXPAND** function

**\=  
EXPAND(SUM(\[Count of Product\]), ROWS)**

we will observe something interesting:

![](<Base64-Image-Removed>)

Here, the subtotal rows evaluate the distinct counts at a lower level each month and then sums for the years. For example, each month in the year 2014 has six \[6\] types of products, and the 2014 subtotal sums up 12 months to have (6 x 12) 72 types. However, the overall total only evaluates one \[1\] level lower, to each year, and obtains six \[6\] distinct types for each year and a sum of 12 in total.

If we instead apply the **EXPANDALL** function, the overall total will evaluate down to the lowest level, to each month

**\=  
EXPANDALL(SUM(\[Count of Product\]), ROWS)**

and show us a sum over all 16 months:

![](<Base64-Image-Removed>)

Model relationships are generally not available in visual calculations except using the specific functions. For example, for the earlier example on **Profit**, we are not allowed to apply filters in calculations like this:

**\=  
CALCULATE(\[Profit\], \[Year\] = 2013)**

However, we do find exceptions to that. For example, the function **LOOKUP** can still be used with filters in visual calculations, and we are allowed to do something like this

**\=  
LOOKUP(\[Profit\], \[Year\] = 2013)**

to build on which, we can even calculate year-on-year growth:

![](<Base64-Image-Removed>)

The divide-by-zero errors can be cleaned by **IF** functions, but you get the idea.

Visual calculations is still a Preview feature for Power BI, as Microsoft continues to improve and update the feature. For example, there are small glitches like this:

![](<Base64-Image-Removed>)

When a field used in the calculation is renamed, it will not be updated simultaneously in the visual calculations Formula bar, but shows red underline instead. Here we are changing ‘Sum of Profit’ to ‘Profit’ for demonstration purposes. It is only refreshed when the Edit mode screen is closed and re-opened.

![](<Base64-Image-Removed>)

It is worthwhile trying it out yourself, and we believe this can become a much more powerful feature as it matures.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/#0)

[](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-2/#0 "close")

top