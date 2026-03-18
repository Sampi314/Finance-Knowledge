# Show Trend Arrows in Excel Chart Data Labels

**Source:** https://trumpexcel.com/excel-chart-data-labels-trend-arrows

---

[Skip to content](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#below-title)

**Watch Video – Show Trend Arrows in Chart Data Labels**

Excel chart data labels are quite boring. While there is not much you can do with these, a bit of excel trickery can add some glamor to it. In this post, I will show you how to show trends in chart labels in a bar chart. Something as shown below:

![Excel Chart Data Labels - Show Trend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20235'%3E%3C/svg%3E)

##### Show Positive/Negative Trend Arrows in Excel Chart Data Labels

Suppose I have the data as shown below:

![Excel Chart Data Labels - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20229%20206'%3E%3C/svg%3E)

If I plot 2013 data only, it won’t tell us how much the sales of a product have increased/decreased over the last year. However, I can do this by changing the chart data label to show the YoY change. To do this, we first need to modify our data set a bit.

![Excel Chart Data Labels - Data Set with Arrows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20340'%3E%3C/svg%3E)

##### Changes made to the data set

1.  Added YoY change in Column D
2.  Added an upward arrow in B11 and downward arrow in C11
    *   To do this, go to Insert –> Symbol
    *   In the Symbol dialog box, select Arial font (or whatever you are using), and scroll down to find the arrow symbols
3.  In column E, use the following combination of [TEXT](https://trumpexcel.com/excel-text-function/)
     and [IF](https://trumpexcel.com/excel-if-function/)
     formula:

\=TEXT(D3,"0.0%")&IF(D3>0,$B$11,$C$11)

When you have the data set in place, create a bar chart using 2013 values. You will get a chart as shown below:

![Excel Chart Data Labels with Regular Chart Labels](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20223'%3E%3C/svg%3E)

Now to show the YoY change instead of 2013 values in chart labels, follow the steps below:

###### **For Excel 2013**

1.  Click on any of the data labels
2.  Right-click and select Format Data Labels
3.  In Label Option, check Value from Cells, click on Select Range and select the cells the new labels (E3:E9 in this case)  
    ![Excel Chart Data Labels - Format Data Labels Excel 2013](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20281%20368'%3E%3C/svg%3E)

###### **For Excel 2010**

1.  Select the first data label (click on it twice)
2.  Click on the formula bar and type \=
3.  Select E3
4.  This will change the first data label to display the value in E3 (along with the arrow). Now you can do this for all the data labels (a bit of manual labor – but a straight forward method)

That’s it!! You would have your chart ready.

![Excel Chart Data Labels with Trends in Chart Labels](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20224'%3E%3C/svg%3E)

_**Try it yourself.. Download the file**_  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Excel-Chart-with-Trend-in-Data-Labels.xlsx)

**You May Also Like the Following Excel Tutorials:**

*   [Color Negative Chart Data Labels in Red with a downward arrow](https://trumpexcel.com/chart-data-labels-in-red-with-arrows/)
    .
*   [Creating Pareto Chart in Excel (Simple + Interactive)](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Insert Arrows in Excel](https://trumpexcel.com/excel-insert-symbols/arrows/)
    
*   [How to Spot Data Point in Excel Scatter Chart](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/)
    .
*   [Format Numbers in Millions in Excel Charts](https://trumpexcel.com/millions-format-excel/)
    
*   [How to Type Degree Symbol in Excel.](https://trumpexcel.com/degree-symbol-in-excel/)
    
*   [How to Apply Superscript and Subscript Format in Excel.](https://trumpexcel.com/superscript-subscript-format-excel/)
    
*   [How to Insert Bullets in Excel.](https://trumpexcel.com/bullet-points/)
    
*   [Adding Trendlines in Excel Charts](https://trumpexcel.com/trendline/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “Show Trend Arrows in Excel Chart Data Labels”
------------------------------------------------------------

1.  I have the same problem as Chris Macro  
    I can’t figure out how to insert the arrow symbols into Excel 2016 as Insert > Symbol only gives me 255 Arial characters, none of which are the arrows.  
    \=CODE(B11) returns 63, which is the Arial Question Mark.  
    However, if I copy the arrows from your example file into 2016 it works perfectly!
    
    [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-11873)
    
2.  Hi Sumit, Thanks for the amazing video. I just had a confusion, can you help me in adding the colored up and down arrow in the chart, currently it only black in color.
    
    [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-3531)
    
3.  Can you insert the arrow symbol in Excel 2007? I can’t figure out how to insert the arrow symbols (see dialog in attached picture) but if I copy the arrows from your example file into 2007 it works perfectly!
    
    [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-1383)
    
    *   Hi Chris.. This is weird.. I don’t have 2007 (have 2010 and 2013). Let me get hold of a machine with 2007 and check this out. But if these arrows are not in 2007, the one at the bottom left of this picture should work the same I guess 🙂
        
        [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-1384)
        
        *   thanks alot for the tip. i have a bubble chart and would like to add trend up / down arrows against the bubbles to denote if there is a increase or decrease in the value.
            
            [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-2227)
            
4.  This is a cool trick! I’ve used it several times. However, it is very tedious to go over each data label to change it. Do you have some VBA code to change the labels automatically?
    
    There’s an add-in that you can use for scatterplots (X-Y plots) but I’m not aware of any add-ins for column charts.
    
    [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-1374)
    
    *   Hi Orlando.. There is a non-VBA way you can use to do this in Excel 2010. Have a look at this link (I have mentioned how to do this below the chart in this file). Hope this is what you are looking for
        
        [https://www.dropbox.com/s/qm9qxp2r5ykj4rr/Excel%20Chart%20with%20Trend%20in%20Data%20Labels%20for%202010.xlsx](https://www.dropbox.com/s/qm9qxp2r5ykj4rr/Excel%20Chart%20with%20Trend%20in%20Data%20Labels%20for%202010.xlsx)
        
        [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-1375)
        
5.  This is a very clever trick. Excel never stops to amaze me.
    
    [Reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#comment-1362)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/#respond)

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