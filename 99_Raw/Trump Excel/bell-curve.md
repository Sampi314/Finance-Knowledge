# How to Make a Bell Curve in Excel (Step-by-step Guide)

**Source:** https://trumpexcel.com/bell-curve

---

[Skip to content](https://trumpexcel.com/bell-curve/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/bell-curve/#below-title)

A bell curve (also known as normal distribution curve) is a way to plot and analyze data that looks like a bell curve.

In the bell curve, the highest point is the one that has the highest probability of occurring, and the probability of occurrences goes down on either side of the curve.

It is often used during employee performance appraisals or during evaluation in exams (_ever heard – “You will be graded on the curve?”_).

Now before I jump in on how to create a bell curve in Excel, let’s get a better understanding of the concept by taking an example.

Understanding the Bell Curve
----------------------------

Suppose you work in a team of 100 members and your manager tells you that your performance will be relative to others and will be evaluated on the bell curve.

This means that even if your team is the best team ever and you’re all superheroes, only a handful of you would get the top rating, most of the people in your team would get an average rating, and a handful will get the lowest rating.

![Bell Curve in Excel (distribution curve) - Understanding the Concept](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20351'%3E%3C/svg%3E)

_Image Source: [EmpxTrack](https://empxtrack.com/blog/bell-curve-for-performance-appraisal)
_

But why do we need the bell curve?

Fair question!

Suppose you have a class of 100 students that appear for an exam. According to your grading system, anyone who gets above 80 out of 100 gets an A grade. But since you set a really easy paper, everyone scored above 80 and got the A grade.

Now there is nothing wrong in this kind of grading system. However, using it, you can not differentiate between someone who got 81 and someone who got 95 (as both would get the A grade).

To keep the comparison fair and keep the competitive spirit alive, a bell curve is often used to evaluate performances (at least that’s how it was when I was in college).

Using the bell curve approach, the marks of students are converted into [percentiles](https://trumpexcel.com/percentile-excel/)
 that are then compared with each other.

Students getting higher marks are on the right side of the curve and students getting low marks are on the left of the curve (with most of the students being in the middle around mean score).

Now to understand bell curve, you need to know about two metrics:

*   **Mean** – the average value of all the data points
*   **Standard Deviation** – it shows how much the dataset deviates from the mean of the dataset. For example, suppose you have a group of 50 people, and you are recording their weight (in kgs). In this dataset, the average weight is 60 kg, and the standard deviation is 4 kg. It means that 68% of the people’s weight is within 1 standard deviation from the mean – which would be 56-64 kg. Similarly, 95% of the people are within 2 standard deviation – which would be 52-68 Kgs.

When you have a dataset that is normally distributed, your bell curve will follow the below rules:

*    The center of the bell curve is the mean of the data point (also the highest point in the bell curve).
*   68.2% of the total data points lie in the range (Mean – Standard Deviation to Mean + Standard Deviation).
*   95.5% of the total data points lie in the range (Mean – 2\*Standard Deviation to Mean + 2\*Standard Deviation)
*   99.7% of the total data points lie in the range (Mean – 3\*Standard Deviation to Mean + 3\*Standard Deviation)

![Bell Curve Example Graph (distribution curve)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20308'%3E%3C/svg%3E)Image Source: [MIT News](http://news.mit.edu/2012/explained-sigma-0209)

Now let’s see how to create a bell curve in Excel.

Creating a Bell Curve in Excel
------------------------------

Let’s take an example of a class of students that have been scored in an exam.

The mean score of the class is **65** and the standard deviation is **10**. (You can calculate the mean using the [AVERAGE function](https://trumpexcel.com/excel-average-function/)
 in Excel and [Standard Deviation using the STDEV.P function](https://trumpexcel.com/standard-deviation/)
).

Here are the steps to create a bell curve for this dataset:

*   In cell A1 enter 35. This value can be calculated using **Mean – 3\* Standard Deviation** (65-3\*10).
*   In the cell below it enter 36 and create a series from 35 to 95 (where 95 is  Mean + 3\* Standard Deviation). You can do this quickly by using the [autofill option](https://trumpexcel.com/fill-numbers-in-cells-without-dragging/)
    , or use the [fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
     and drag it down to fill the cells.![Bell Curve in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20232%20407'%3E%3C/svg%3E)
*   In the cell adjacent to 35, enter the formula: \=NORM.DIST(A1,65,10,FALSE)
    *   Note that here I have hardcoded the value of mean and standard deviation. You can also have these in cells and use the cell references in the formula.![Creating a bell Curve in Excel - Normal Distribution formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20356'%3E%3C/svg%3E)
*   Again use the fill handle to quickly copy and paste the formula for all the cells.
*   Select the data set and go to Insert tab.![Making a Bell Curve Chart in Excel - Insert Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20168'%3E%3C/svg%3E)
*   Insert the ‘Scatter with Smooth Lines’ chart.![Scatter chart to create a bell curve in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20254'%3E%3C/svg%3E)

This will give you a bell curve in Excel.

![Bell Curve when created in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20559%20338'%3E%3C/svg%3E)

Now you can change the chart title and adjust the axis if you need.

Note that when you have a low standard deviation, you get a packed slim bell curve, and when you have a high standard deviation, the bell curve is wide and covers more area on the chart.

This kind of bell curve can be used to identify where a data point lies in the chart. For example, in case a team is full of high performers, when evaluated on a curve, despite being a high performer, someone can get an average rating as he/she was in the middle of the curve.

_Note: In this blog post, I have discussed the concept of a bell curve and how to create it in Excel. A statistician would be better suited to talk about the efficacy of the bell curve and limitations associated with it. I am more of an Excel guy and my involvement with Bell curve has been limited to the calculations I did when I worked as a Financial Analyst._

Hope you found this tutorial useful!

Let me know your thoughts in the comments section.

**You May Also like the following Excel Tutorials:**

*   [How to Make a Histogram in Excel.](https://trumpexcel.com/histogram-in-excel/)
    
*   [How to Calculate Compound Interest in Excel + FREE Calculator](https://trumpexcel.com/compound-interest-calculator/)
    .
*   [How to Create a Heat Map in Excel.](https://trumpexcel.com/heat-map-excel/)
    
*   [Step Chart in Excel.](https://trumpexcel.com/step-chart-in-excel/)
    
*   [How to Create a Timeline / Milestone Chart in Excel.](https://trumpexcel.com/milestone-chart-in-excel/)
    
*   [Creating a Pareto Chart in Excel.](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [Calculate P-value in Excel](https://trumpexcel.com/p-value-excel/)
    
*   [Creating a Pie Chart in Excel](https://trumpexcel.com/pie-chart/)
    
*   [Advanced Excel Charts](https://trumpexcel.com/advanced-charts/)
    
*   [How to Find Slope in Excel? Using Formula and Chart](https://trumpexcel.com/find-slope-excel/)
    
*   [Calculate Area Under Curve in an Excel](https://trumpexcel.com/calculate-area-under-curve-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

28 thoughts on “How to Make a Bell Curve in Excel (Step-by-step Guide)”
-----------------------------------------------------------------------

1.  It’s 2023 and you’re still helping students!
    
    THANK YOU!
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-15527)
    
2.  very useful.  
    Thank you.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-14829)
    
3.  This was the easiest step-by-step guide for bell curves I’ve come across, many thanks!
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13692)
    
4.  is there any excel chart to create a rough predictive estimate of a pandemic based on previous known data applying present know data to project an estimate . now that would be very popular right now. A bell Gaussian distributions curve I think its called.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13610)
    
5.  Thanks…very helpful
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13580)
    
6.  Hi. The standard deviation of the calculated weights is 17.7 and not 10. So, this bell curve does not comply with the created data.  
    Am I right (or I’m not)?
    
    Best regards  
    ALSH
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13542)
    
    *   this is what I get too.
        
        [Reply](https://trumpexcel.com/bell-curve/#comment-31675)
        
7.  Many thanks
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13470)
    
8.  Thank you, life saver!
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13123)
    
9.  It is valuable
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-13119)
    
10.  Useful. Thank you.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12987)
    
11.  Thank very much you explain clarify good luck
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12982)
    
12.  Helped me a lot set up an activity for my class, than you!
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12945)
    
13.  Thank you so much for your step by step instructions, it was really usefull.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12768)
    
14.  how can shade the curve which the area that i want to find
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12751)
    
15.  Could you please explain from where you got (mean value 65 AND STD deviation 10)  
    also from where do we got this role ( mean-3\*STD Deviation )
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12357)
    
    *   For the mean, you can use the AVERAGE function, and for the deviation you can use the STDEV.P function. Both using your results as the range.
        
        [Reply](https://trumpexcel.com/bell-curve/#comment-12946)
        
16.  Thank you very much. Very nice and clear presentation. Just one question please: In which area of financial analysis did you meet the normal distribution? Aren’t the distributions of returns almost always leptokurtic?
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-12058)
    
17.  QUITE USEFUL. THANK YOU
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11847)
    
18.  this doesnt work, you are idiot
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11603)
    
    *   it works perfectly
        
        [Reply](https://trumpexcel.com/bell-curve/#comment-11911)
        
    *   instead of saying (Thank you) you’re saying that, by the way the above example working with all the people
        
        [Reply](https://trumpexcel.com/bell-curve/#comment-12358)
        
19.  Very useful and helpful post. Thank you so much
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11583)
    
20.  This is really good tutorial but I was thinking if our data increases on daily basis so how we can maintain automatically this curve?
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11582)
    
21.  GREAT!!!!!  
    You have done a wonderful job.
    
    Keep it up.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11491)
    
22.  Good, very good. Thank you so much for this man, people like you who spread knowledge like this and make the lives of others easier for free are amazing. God bless you brother.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11396)
    
23.  I wanted to know how to shade in all three standard deviations i.e. 68.2%, 95%, and 99.7%. I can create the curve. I just cannot figure out how to get the shading.
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-11263)
    
24.  one thing which is not clear for me. When you said “In cell A1 enter 35. This value can be calculated using Mean – 3\* Standard Deviation (65-3\*10)”. Now what is the idea of writing 35, 36 and 37 and so on in the cells… may be there is no student in the class who got 35 marks.  
    So how can you transfer the actual student marks into the excel sheet.. We are like using the lowest value as 3 SD from the mean, is n’t it?
    
    [Reply](https://trumpexcel.com/bell-curve/#comment-10884)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/bell-curve/#respond)

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