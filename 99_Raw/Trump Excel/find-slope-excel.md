# How to Find Slope in Excel? Using Formula and Chart

**Source:** https://trumpexcel.com/find-slope-excel

---

[Skip to content](https://trumpexcel.com/find-slope-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-slope-excel/#below-title)

The _slope_ of the regression line is a measure of the steepness of the line.

It’s a numeric value that tells us how two variables are correlated. It tells us how much the dependent variable will change in case there is a change in the independent variable.

There are three ways to find the slope of the regression line for a given set of variables in Excel:

*   Using the SLOPE Function
*   Using an Excel Scatter chart

In this tutorial, I show you how to calculate slope using each of the above three methods.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/find-slope-excel/#)

What is Slope? An Overview
--------------------------

A Slope is a value that tells us how two values (usually called the x and y values) are related to each other.

To give you a simple example, if you have the data about the height and yearly income of some people and you calculate the slope for this data, it will tell you whether there is a positive or negative correlation between these data points.

![Slope for Height and Income data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20511'%3E%3C/svg%3E)

The slope value can be positive or negative.

In our example, if the slope value is 138, which means that there is a positive correlation between height and the income of people. So if the height increases by 1 centimeter, the income is likely to increase by USD 138.

Apart from the slope, another thing you need to know about is the Intercept.

Let me explain it with the equation:

Y = Slope\*X + Intercept

In this equation, we have already calculated the slope, but to truly know what would be the Y value for a given X value, you also need to know the intercept.

Thankfully, Excel has a formula for that as well, and I will cover how to calculate intercept in all the methods.

Method 1: Using the Excel SLOPE Function
----------------------------------------

The easiest way to calculate slope in Excel is to use the in-built **SLOPE function**.

It finds the slope value of a given set of _x-y_ coordinates in one step.

While calculating slope manually could be hard, with the SLOPE function, you just need to give it the x and y values and it does all the heavy lifting in the backend.

### SLOPE Function Syntax in Excel

The syntax for the slope function is:

\=SLOPE(y\_vals, x\_vals)

Here, _y\_vals_ and _x\_vals_ each consist of an array or range of cells containing numeric dependent data values.

Remember that you need to give the **Y values as the first argument and X values as the second argument**. If you do it the other way round, you will still get the result but it would be incorrect.

Suppose you have the below dataset as shown below where I have the height (in cm) as X values and average annual income (in USD) as the Y values.

![Dataset to calculate slope and interceot](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20528'%3E%3C/svg%3E)

Below is the formula to calculate slope using this dataset:

\=SLOPE(B2:B11,A2:A11)

![SLOPE formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20580'%3E%3C/svg%3E)

The above result tells me that from this dataset, I can assume that in case the height increases by 1 cm, the income would increase by USD 138.58.

Another common statistical value that people often calculate when working with slope is to calculate the **Intercept value**.

Just to refresh, the slope equation is something as shown below:

  Y = Slope\*X + Intercept

While we know the slope, we would also need to know the intercept value to make sure we can calculate Y values for any X value.

This can easily be done using the below formula:

\=INTERCEPT(B2:B11,A2:A11) 

![INTERCEPT formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20578'%3E%3C/svg%3E)

With this, our equation for this dataset becomes:

Y = 138.56\*X + 65803.2

So now, if I ask you what would be the income of anyone whose height is 165 cm, you can calculate the value easily.

Y = 138.56\*165 + 65803.2

Both slope and intercept values can be positive or negative

### Points to Remember when Using the SLOPE Function in Excel

Here are a few points to remember when finding the slope of a regression line using the SLOPE function:

*   Arguments of the SLOPE function have to be numerical (DATE values are also accepted). In case any of the cells are blank or contains a text string, these would be ignored
    *   In case there is ‘0’ in any cell/cells, it would be used in the calculation
*   There should be an equal number of _x_ and _y_ values, when used as input for the SLOPE function. In case you give it unequal-sized ranges, you will get a [#N/A error](https://trumpexcel.com/iferror-vlookup/)
    .
*   There should be more than one set of points, otherwise, the SLOPE function returns a #DIV! error

Also read: [Calculate Interquartile Range (IQR) in Excel](https://trumpexcel.com/interquartile-range-iqr-excel/)

Method 2 – **Using a Scatter Chart to get the Slope Value**
-----------------------------------------------------------

If you prefer to visualize your data and the regression line, you can plot the data in a [scatter chart](https://trumpexcel.com/scatter-plot-excel/)
 and use it to find the slope and the intercept for the [trend line (also called the line of best fit)](https://trumpexcel.com/trendline/)
.

Suppose you have the dataset as shown below and you want to find out the slope and intercept for this data:

![Dataset to calculate slope and intercept using scatter plot](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20422'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select both X and Y data points (in our example, it would be the height and income column)
2.  Click on the ‘Insert’ tab in the ribbon

![Click the Insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20223'%3E%3C/svg%3E)

3.  Click on the ‘Insert scatter’ dropdown (under the Charts group)
4.  From the dropdown that appears, select the ‘Scatter chart’ option

![Click on the Insert Scatter chart icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20491%20498'%3E%3C/svg%3E)

5.  This will insert a scatter chart into your worksheet, displaying your x-y values as scatter points (as shown below)

![Scatter chart inserted in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20360'%3E%3C/svg%3E)

6.  Right-click on one of the scatter points, and select ‘Add Trendline’ from the context menu that appears. This will insert the trendline and also open the ‘Format Trendline’ pane in the right

![Click on Add Trendline](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20421'%3E%3C/svg%3E)

7.  In the Format Trendline pane, within the ‘Trendline Options’, select the ‘Display Equation on chart’ checkbox

![Select display equation on the chart option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20726'%3E%3C/svg%3E)

8.  Close th Format Trendline pane

The above steps would insert a scatter chart that has a trendline, and the trendline also has the slope and intercept equation.

![Slope and Intercept equation in the chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20423'%3E%3C/svg%3E)

In our example, we get the below equation:

y = 138.56x + 65803

Here:

*   138.56 is the slope of the regression line
*   65803 is the intercept of the regression line

You can compare this with the values we got from the SLOPE and INTERCEPT functions (it’s the same value).

If the slope value is positive, you’ll see the trend line going up, and if the slope value is negative, then you will see the trend line going down. The steepness of the slope would be dependent on its slope value

While the formula method to calculate slope and intercept is easy, the benefit of using the scatter chart method is that you can visually see the distribution of the data points as well as the slope of the regression line.

And in case you are anyway creating a scatter chart for your data, getting the slope value by adding a trendline would actually be faster than using the formulas.

So these are two really simple ways that you can use to calculate the slope and the intercept value of a data set in Excel.

I hope you found this tutorial useful.

**Other excel tutorials you may also like:**

*   [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    
*   [Calculate the Coefficient of Variation (CV) in Excel](https://trumpexcel.com/calculate-coefficient-of-variation-excel/)
    
*   [How to Add Error Bars in Excel (Horizontal/Vertical/Custom)](https://trumpexcel.com/error-bars-excel/)
    
*   [How to Calculate Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [How to Calculate Correlation Coefficient in Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [Calculate Area Under Curve in an Excel](https://trumpexcel.com/calculate-area-under-curve-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-slope-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK