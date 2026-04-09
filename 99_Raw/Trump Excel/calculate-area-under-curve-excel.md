# Calculate Area Under Curve in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/calculate-area-under-curve-excel

---

[Skip to content](https://trumpexcel.com/calculate-area-under-curve-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-area-under-curve-excel/#below-title)

Area Under Curve (AUC) is a widely used concept in data sciences in multiple fields.

While the concept of Area Under Curve is quite simple – which is to calculate the total area covered between the curve/line and the axis – there is no direct way to calculate this in Excel.

But it isn’t too difficult as well!

In this short tutorial, I will show you two ways you can use to **calculate Area Under Curve in Excel**.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-area-under-curve-excel/#)

Formula to Calculate Area Under Curve in Excel
----------------------------------------------

As I mentioned, there is no direct formula to calculate AUC, but we can calculate it using a helper column and a simple formula.

Below I have a dataset and I have created a line chart using this data.

![Dataset and line chart for area under curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20325'%3E%3C/svg%3E)

While I can not calculate the area under the curve for this whole chart, I can break it down into small trapezoids (as shown below), and then calculate the area of each trapezoid.

![Area Under Curve Chart Logic explained](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20301'%3E%3C/svg%3E)

In the above chart image, I have broken each interval into a separate section (indicated with a different color), and each of these sections resembles a trapezoid.

While I can not calculate the area under the line curve directly, I can calculate the area of these individual trapezoids.

Once I have the area for all of these trapezoids, I can just add them all. This will give me a very close value of the total area under the chart.

Below is the formula to calculate the area of a trapezoid

A = (a+b)/2 \* h

where:

*   a is the base lengh of one side
*   b is the base length of the other side
*   h is the height

![Trapezoid Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20310%20274'%3E%3C/svg%3E)

Below is the formula that I can use (in the adjacent column) to calculate the area of a trapezoid in the chart for my dataset:

\=((B2+B3)/2)\*(A3-A2)

![Formula to get trapezoid area for each value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20384'%3E%3C/svg%3E)

Apply the above formula for all the cells in the column (except the last one).

Now that I have the trapezoid value (which is also the area under the curve value) for the x-axis intervals in the chart, I can now add all these to get the overall area under the chart.

I can use a simple SUM formula to do this.

![SUM formula to get the total area under curve](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20410%20418'%3E%3C/svg%3E)

So this is how I can calculate the total area under the curve for a simple line chart.

Note that the result of this method would be very close to the actual area under curve value, it could be slightly off. This is because the area between the line and axis is not a perfect trapezoid, but close to it.

Using the Trend line Equation for Area Under Curve
--------------------------------------------------

Let me show you another method to calculate the Area Under Curve (AUC) for a chart in Excel.

This method uses [adding a trendline in the Excel chart](https://trumpexcel.com/trendline/)
 and then utilizing the equation that the Excel chart automatically creates for the trendline.

Below is a dataset for which I have created the line chart, and now I want to calculate the area under the curve for this chart.

![Dataset and line chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20337'%3E%3C/svg%3E)

Below are the steps to get the Trendline equation for our dataset:

1.  Select the chart
2.  In the Chart Design tab, click on the Add Chart Element option

![Click on plus icon add chart element icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20447'%3E%3C/svg%3E)

3.  Hover the Cursor over the Trendline option, and in the options that show up, click on ‘More Trendline Options’. This will open the Format Trendline pane

![Click on More Options in Trendline](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20693%20475'%3E%3C/svg%3E)

4.  In the ‘Trendline Options’, select Polynomial

![Select the Polynomial option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20614%20470'%3E%3C/svg%3E)

5.  Check the ‘Display Equation on chart’ option. This will show a polynomial equation of the trendline in the chart

![Check the display equation on chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20591%20359'%3E%3C/svg%3E)

Now that we have the polynomial equation, we can use this to calculate the area for this line chart.

But before doing that, there is one more step that you need to do. You need to get the definite integral for the polynomial equation.

In my case, the equation is

y = 1.0038x2 + 2.1826x - 1.85

So the definite integral of this equation would be

y = (1.0038/3)\*x3 + (2.1826/2)\*x2 - 1.85x + c

While I am not an expert in calculus, based on my limited understanding, you can convert an equation to a definite integral by increasing the power of x by 1, and diving it by that same value power. For example, x2 will become x3/3 and x will become x2/2 and any constant (such as 1.85) will become 1.85x

Now that I have the equation, I can calculate the area under the curve by finding the value of f(10)-f(1)

In our example, I have the equation – f(x) = (1.0038/3)\*x3 + (2.1826/2)\*x2 – 1.85x + c

So F(1) can be calculated using the below formula:

\=(1.0038/3)\*(1^3) + (2.1826/2)\*(1^2) - 1.85\*1 

and f(10) can be calculated using the below formula:

  =(1.0038/3)\*(10^3) + (2.1826/2)\*(10^2) - 1.85\*10  

To get the area under the curve, we need to find the difference between these two values \[f(10) – f(1)\]

![Formula to calculate the area under curve in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20430'%3E%3C/svg%3E)

You will notice that the value is very close to the one we got from our previous method (by using the trapezoid formula).

While both these methods work fine, remember these are still a very close approximation of the area under the curve and are not accurate.

So while Microsoft Excel does not have a direct way to calculate the area under the curve, you can use any of these two methods to do it.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like**:

*   [How to Create an Area Chart in Excel (explained with Examples)](https://trumpexcel.com/area-chart/)
    
*   [How to Find Slope in Excel? Using Formula and Chart](https://trumpexcel.com/find-slope-excel/)
    
*   [How to Make a Scatter Plot in Excel (XY Chart)](https://trumpexcel.com/scatter-plot-excel/)
    
*   [How to Add a Secondary Axis in Excel Charts (Easy Guide)](https://trumpexcel.com/add-secondary-axis-charts/)
    
*   [How to Make a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Calculate Area Under Curve in Excel (2 Easy Ways)”
-----------------------------------------------------------------

1.  Excellent information for a person like me. Thank you.
    
    [Reply](https://trumpexcel.com/calculate-area-under-curve-excel/#comment-37670)
    
2.  Yes, good job – especially with the polynomial. Maybe a method of getting the exact area would be to average up each pair of Y axis values (1st pair would be the average of 0 and 3) and average those averages, then multiply with the x axis length (10 in this case). The exact area for this set is 428.
    
    [Reply](https://trumpexcel.com/calculate-area-under-curve-excel/#comment-36016)
    
    *   Would the next pair then be the average of 3 and 5 or the average of 5 and 12?
        
        [Reply](https://trumpexcel.com/calculate-area-under-curve-excel/#comment-42395)
        
3.  Good job. clear methods. Both correspond to integrating the curve graphical and analytical. Just a note: for the first ,method if you have negative values you need to use absolute values
    
    [Reply](https://trumpexcel.com/calculate-area-under-curve-excel/#comment-31859)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-area-under-curve-excel/#respond)

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