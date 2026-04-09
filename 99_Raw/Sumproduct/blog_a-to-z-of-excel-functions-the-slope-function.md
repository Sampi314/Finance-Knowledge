# A to Z of Excel Functions: The SLOPE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The SLOPE Function

*   September 8, 2025

A to Z of Excel Functions: The SLOPE Function
=============================================

_Welcome back to our regular A to Z of Excel Functions blog.  Today we look at the **SLOPE** function._

**The SLOPE function**

Sometimes, you wish to forecast what comes next in a sequence, _i.e._ make a forecast.  There are various approaches you could use:

*   **Naïve method:** this really does live up to its billing – you simply use the last number in the sequence, _e.g._ the continuation of the series 8, 17, 13, 15, 19, 14, … would be 14, 14, 14, 14, …  Hmm, great  
      
    
*   **Simple average:** only a slightly better idea: here, you use the average of the historical series, _e.g._ for the continuation of the series 8, 17, 13, 15, 19, 14, … would be 14.3, 14.3, 14.3, 14.3, …   
      
    
*   **Moving average:** now we start to look at smoothing out the trends by taking the average of the last **n** items.  For example, if n were 3, then the sequence continuation of 8, 17, 13, 15, 19, 14, … would be 16, 16.3, 15.4, 15.9, 15.9, …  
      
    
*   **Weighted moving average:** the criticism of the moving average is that older periods carry as much weighting as more recent periods, which is often not the case.  Therefore, a weighted moving average is a moving average where within the sliding window values are given different weights, typically so that more recent points matter more.  For example, instead of selecting a window size, it requires a list of weights (which should add up to 1).  As an illustration, if we picked four periods and \[0.1, 0.2, 0.3, 0.4\] as weights, we would be giving 10%, 20%, 30% and 40% to the last 4 points respectively which would add up to 1 (which is what it would need to do to compute the average).  
      
    Therefore the continuation of the series 8, 17, 13, 15, 19, 14, … would be 15.6, 15.7, 15.7, 15.5, 15.6, …  
      
    

All of these approaches are simplistic and have obvious flaws.  We are using historical data to attempt to predict the next point.  If we go beyond this, we are then using forecast data to predict further forecast data.  That doesn’t sound right.  We should stick to the next point.  Since we are looking at a single point and we can weight the historical data by adding exponents to the calculation, this is sometimes referred to as **Exponential Single Smoothing**.

A slightly more sophisticated method is called **regression analysis**: well, that takes me back!  This is a technique where you plot an independent variable on the **x** (horizontal axis) against a dependent variable on the **y** (vertical) axis.  “Independent” means a variable you may select (_e.g._ “June”, “Product A”) and dependent means the result of that choice or selection.

For example, if you plotted your observable data on a chart, it might look something like this:

![](https://sumproduct.com/wp-content/uploads/2025/09/image1.png)

Do you see?  You can draw a straight line through the data points.  There is a statistical technique where you may actually draw the “best straight line” through the data using an approach such as Ordinary Least Squares, but rather than attempt to explain that, I thought I would try and keep you awake.  There are tools and functions that can work it out for you.  This is predicting a trend, not a point, so is a representative technique for **Exponential Double Smoothing** (since you need just two points to define a linear trend).

Once you have worked it out, you can calculate the gradient (**m**) and where the line cuts the **y** axis (the **y** intercept, **c**).  This gives you the equation of a straight line:

> **y = mx + c**

Therefore, for any independent value **x**, the dependent value **y** may be calculated – and we can use this formula for forecasting.

Of course, this technique looks for a straight line and is known as **linear** regression.  You may think you have a more complex relationship (and you may well be right), but consider the following:

*   Always split your forecast variables to logical classifications.  For example, sales may be difficult to predict as the mix of products may vary period to period, for each product, there may be readily recognizable trends
*   If the relationship does not appear to be linear, try plotting **log x** against **log y**.  If this has a gradient of two then **y** is correlated with **x2**; if the gradient is three, then **y** is correlated with **x3** _etc_.

One way of defining this is with the **INTERCEPT** (_i.e_. where the trendline cuts the **y**\-axis, or the value when **x** is zero \[0\]) and **SLOPE** (_i.e._ the gradient) functions.

The **SLOPE** function returns the slope of the linear regression line through data points in **known\_y’s** and **known\_x’s**.  The slope is the vertical distance divided by the horizontal distance between any two points on the line, which is the rate of change along the regression line.

The **SLOPE** function employs the following syntax to operate:

> **SLOPE(known\_y’s, known\_x’s)**.

The **SLOPE** function has the following arguments:

*   **known\_y’s:** this is required and represents the dependent set of observations or data
*   **known\_x’s:** this is also required and denotes the independent set of observations or data.

It should be noted that:

*   the arguments should be either numbers or names, arrays or references that contain numbers  
      
    
*   if an array or reference argument contains text, logical values or empty cells, those values are ignored; however, cells with the value zero are included  
      
    
*   if **known\_y’s** and **known\_x’s** contain a different number of data points or contain no data points, **SLOPE** returns the _#N/A_ error value  
      
    
*   The equation for the intercept of the regression line, **a**, is:

![](<Base64-Image-Removed>)

where the slope, **b**, is calculated as:

![](<Base64-Image-Removed>)

and where **x** and **y** are the sample means **AVERAGE(known\_x’s)** and **AVERAGE(known\_y’s)  
  
**

*   the underlying algorithm used in the **SLOPE** and **INTERCEPT** functions is different than the underlying algorithm used in the **LINEST** function.  The difference between these algorithms can lead to different results when data is undetermined and collinear.  For example, if the data points of the **known\_y’s** argument are zero (0) and the data points of the **known\_x’s** argument are one (1):  
      
    
    *   **SLOPE** and **INTERCEPT** return an _#DIV/0!_ error.  The **SLOPE** and **INTERCEPT** algorithm is designed to look for one and only one answer, and in this case there can be more than one answer  
          
        
    
    *   **LINEST** returns a value of zero (0).  The **LINEST** algorithm is designed to return reasonable results for collinear data, and in this case at least one answer can be found.

Please see my example below:

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon.  Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found [here](https://sumproduct.com/thought/a-to-z-of-excel-functions)
._

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-slope-function/#0 "close")

top