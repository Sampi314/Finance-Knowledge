# Power BI Blog: More on Visual Calculations Part 1

**Source:** https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: More on Visual Calculations Part 1

*   April 3, 2024

Power BI Blog: More on Visual Calculations Part 1
=================================================

Power BI Blog: More on Visual Calculations Part 1
=================================================

4 April 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we take a deeper look at the new Preview feature, visual calculations._

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/visual-calculations-in-preview)
, we introduced to you the Preview feature: visual calculations. Now, we plan to consider how to create a visual calculation and demonstrate a visual calculations specific function: **RUNNINGSUM**.

![](https://sumproduct.com/wp-content/uploads/2025/05/f9cdf4710331d988425fc268e6e958d6-1.jpg)

The **RUNNINGSUM** function is both useful and convenient. In one of our earlier blogs on [labelling growth](https://www.sumproduct.com/blog/article/power-bi-tips/labelling-growth-on-a-line-chart-part-1)
 on a Line chart, we created a cumulative measure for the profit data and used that to build visuals. The **DAX** formula we used was:

**Cum  
Profit = CALCULATE(SUM(Financials\[Profit\]), ‘Calendar'\[Date\] <=  
MAX(Financials\[Date\]))**

Now using **RUNNINGSUM**, we can replace that with simply:

**Cum  
Profit = RUNNINGSUM(\[Sum of Profit\])**

Much simpler! We can also build other visual calculations based on the visual calculation **Cum Profit** – in our [blog](https://www.sumproduct.com/blog/article/power-bi-tips/labelling-growth-on-a-line-chart-part-1)
 example, the subsequent chart measures could be built using visual calculations.

It is generally not easy to model running sums (cumulative totals) or moving averages in **DAX** – or even just to calculate the previous item of a field. Now, with visual calculation specific functions like **RUNNINGSUM**, **MOVINGAVERAGE**, **PREVIOUS** or **FIRST**, it is easier to achieve that within visuals. It is exciting to see how this feature will evolve for broader use than just confined in visuals. Watch this space!

Before listing all the visual calculation specific functions, let’s look at some features, advantages and disadvantages of visual calculations:

*   Visual calculations aren’t stored in the model but within the visual, which means anything in the model must be added to the visual before the visual calculation can refer to it
*   Compared to measures, visual calculations operate on aggregated data instead of the detailed level, often leading to performance benefits
*   Power BI now displays a visual matrix for building visual calculations which makes the process very intuitive (in fact, we used to build similar matrices alongside when assembling similar visuals)

![](<Base64-Image-Removed>)

*   Most of the existing **DAX** functions are available for building visual calculations, but since visual calculations work within the confines of the visual matrix, functions that rely on model relationships such as **USERELATIONSHIP**, **RELATED** or **RELATEDTABLE** cannot be used
*   Templates are also provided to inspire visual calculation ideas

![](<Base64-Image-Removed>)

*   Microsoft has tested and found the following visual types do not work with visual calculations:
    *   ArcGIS Maps
    *   Azure Map
    *   Decomposition Tree
    *   Key Influencers
    *   Line and Stacked Column chart
    *   Map
    *   Metrics
    *   Paginated Report
    *   Power Automate
    *   Power Maps
    *   Python visual
    *   Q&A
    *   R visual
    *   Shape Map
    *   Slicer
    *   Small Multiples
    *   Smart Narrative
    *   Treemap
*   Visual calculations may be added and edited using Power BI Desktop; reports containing visual calculations can be published to the Power BI Service, but visual calculations cannot be edited in the Power BI Service
*   A visual calculation can’t refer to itself on the same or different detail level
*   Power BI Embedded isn’t supported for reports that use visual calculations
*   The _see records_drill-through functionality cannot be used on visuals containing visual calculations
*   Users cannot set built-in or custom format strings or conditional formatting on visual calculations
*   Users cannot set data categories or change aggregations on visual calculations
*   Users cannot change the sort order for visual calculations
*   Users cannot use field parameters with visual calculations.

Visual calculations offer great simplicity by calculating within the filter context of a visual and many of the visual calculations specific functions exploit that advantage. Let’s take a look at the available functions as at the time of writing:

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

We’ve touched on the **RUNNINGSUM** function, and some other functions like **MOVINGAVERAGE** or **PREVIOUS** work quite straightforwardly as their names suggest. Next time, we’ll take a look at some of the more interesting functions.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/#0)

[](https://sumproduct.com/blog/power-bi-blog-more-on-visual-calculations-part-1/#0 "close")

top