# Power BI Blog: Maximum and Minimum Points on Power BI Line Charts

**Source:** https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Maximum and Minimum Points on Power BI Line Charts

*   December 25, 2025

Power BI Blog: Maximum and Minimum Points on Power BI Line Charts
=================================================================

__Welcome back to this week’s edition of the Power BI blog series.  This week, we look at maximum and minimum points on Power BI Line charts.__

Currently, Power BI does not have an integrated function to highlight maximum and minimum points on a Line chart.  Using the method detailed below, you will be able to add that extra piece of detail!  Here is an example:

![](https://sumproduct.com/wp-content/uploads/2025/12/image.png)

For this example, data detailing the sales **Month** and **Sales** are used:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-1.png)

As you create the data, you should have the following columns and a **Sales Amount** measure:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-2.png)

Also, for one of the steps (_i.e_. the visual calculation step), you will need to make sure visual calculations are enabled.  To do this, click on **File -> Options and settings -> Options -> Preview features** and tick the **Visual calculations** box, v_iz._

![](https://sumproduct.com/wp-content/uploads/2025/12/image-3.png)

Once this has been done, then go to ‘Report View’ and select the Line chart option under the Build section.  For the **x**\-axis, drag in the **Month** column, and for **y**\-axis select the **Sales Amount** measure.  This is all standard practice for Power BI:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-4.png)

Then, press the **+Add data** button under the Y-axis, and click the **New visual calculation** icon:

![](https://sumproduct.com/wp-content/uploads/2025/12/image-5.png)

In the formula bar that pops up below the graph, type in this formula and press **ENTER**:

**Data Labels =  
VAR MaxPoint = MAXX(ROWS, \[Sales Amount\])  
VAR MinPoint = MINX(ROWS, \[Sales Amount\])  
RETURN  
IF(\[Sales Amount\] IN {MaxPoint, MinPoint}, \[Sales Amount\], BLANK())**

![](<Base64-Image-Removed>)

This formula works by assessing each month’s sales amount for whether it is a maximum or minimum value in relation to the other months.  **ROWS** represents all rows in the table, and **Sales Amount** is the name of the column being assessed.  **RETURN** outputs these values based on the proceeding [**IF()**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-if/)
 statement which returns the corresponding sales amount if, and only if, that row’s sales amount is a maximum or a minimum value.  If it is not, it uses [**BLANK()**](https://sumproduct.com/blog/the-a-to-z-of-dax-functions-blank/)
 to return a blank value.  This visual calculation will then produce a line between the two max/min points:

![](<Base64-Image-Removed>)

Now, the labels for the maximum and minimum points need to be added and the newly created line needs to be removed (without removing the labels).

To include the labels, open the Format tab, and click the ‘Data labels’ switch from ‘off’ to ‘on’:

![](<Base64-Image-Removed>)

Then, open the ‘Data labels’ dropdown, change the ‘Apply settings to’ dropdown to **Sales Amount,** and turn the ‘Show for this series’ switch off:

![](<Base64-Image-Removed>)

This will hide all data labels of the main **Sales Amount** curve but keep the labels for the maximum and minimum points.

As an aside, if your maximum and minimum data labels are not visible because they overlap the **Sales Amount** curve, you can adjust their position under **Data labels -> Options -> Minimum offset**.

Also, if you’d like to add markers, go to **Format -> Markers -> Apply settings to** and choose **Data Labels.**  Then turn the ‘Show for this series’ switch on:

![](<Base64-Image-Removed>)

Now, to remove the line.  Scroll back up the Format tab and find the Lines dropdown.  Open it and use the corresponding ‘Apply settings to’ dropdown to select ‘Data Labels’ (_i.e_. the name of the maximum / minimum line we created).  Then, change the width of the line to zero \[0\] pixels:

![](<Base64-Image-Removed>)

That will produce the final result (with a bit of a silly title but I will not bore you with how to change that!):

![](<Base64-Image-Removed>)

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/public-courses/)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
. 

*   [Log in](https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/#0)
    
*   [Register](https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/#0)

[](https://sumproduct.com/uncategorized/power-bi-blog-maximum-and-minimum-points-on-power-bi-line-charts/#0 "close")

top