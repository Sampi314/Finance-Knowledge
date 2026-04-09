# Dynamic Excel Chart with Series Selection Check-box

**Source:** https://trumpexcel.com/dynamic-excel-chart-check-box

---

[Skip to content](https://trumpexcel.com/dynamic-excel-chart-check-box/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-excel-chart-check-box/#below-title)

Apart from being super cool, Excel dynamic charts are really helpful in presenting a comparative analysis from the data.

Suppose you have the financial data for a company ABC Ltd, and you want to see how the revenue has grown over the quarters. At the same time, you also want to compare the growth with previous years. [Dynamic excel chart](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
 can give you something as shown below:

![Dynamic Excel Chart with Series Selection Check-box](https://trumpexcel.com/wp-content/uploads/2014/01/Dynamic-Chart-with-Series-Selection-Checkbox.gif)A single click instantly shows you the performance of 2013 as compared to 2011 or 2012.

##### Dynamic Excel Chart with Series Selection Check-box

1.  Arrange the data as shown below:

![Dynamic Excel Chart with Series Selection Check-box - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20130'%3E%3C/svg%3E)

1.  Go to Developer tab –> Insert –> Form Controls –> Check Box (Form Control)

![Dynamic Excel Chart with Series Selection Check-box - Insert Check Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20181%20204'%3E%3C/svg%3E)

1.  Click anywhere in the worksheet to [insert the check box](https://trumpexcel.com/insert-checkbox-in-excel/)
    . Change the name of the Checkbox from Check Box 1 to 2011.
2.  Right click on the check box and select Format Control, specify a cell link (in this case I have used C7).
    *   Cell C7 would return TRUE when the check box is checked, and FALSE when unchecked.
3.  Repeat Steps 2 to 4 to insert another check box for 2012, and use a different cell link (I have used C8 here).
4.  Copy the original chart data from B2:F5 and paste it in some other location. I have used B10:F13.

![Dynamic Excel Chart with Series Selection Check-box - Final Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20374%20289'%3E%3C/svg%3E)

1.  Delete the data for 2011 and 2012, and use the following formula:
    
    *   In C11: \=IF($C$7,C3,NA()) _\[Drag this to fill the row from D11 to F11\]_
    *   In C12: \=IF($C$8,C4,NA()) _\[Drag this to fill the row from D12 to F12\]_
    
    *   _This formula returns the value from original data if the check box for that year is checked, and #N/A if it is unchecked._
2.  With both the checkboxes checked, select the entire data and go to Insert –> Charts–> Column–> Clustered Column. This will insert a column chart with three column [bars for each Quarter](https://trumpexcel.com/calculate-quarter-from-date-excel/)
    .

![Dynamic Excel Chart with Series Selection Check-box - Insert Column Chart Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201123%20355'%3E%3C/svg%3E)

1.  Click on any data bar for 2011 (this will select all the data bars for 2011) and right click. From the menu select Change Series Chart Type. This will change the chart type from a bar chart to a line chart.

![Dynamic Excel Chart with Series Selection Check-box - Change Chart Type Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201134%20324'%3E%3C/svg%3E)

1.  Repeat the same process for 2012 bar to convert it into a line chart. Format the chart as you wish.

![Dynamic Excel Chart with Series Selection Check-box - final chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%20247'%3E%3C/svg%3E)

1.  That’s it. You have a dynamic chart ready. Now when you uncheck the checkbox for a year, its data would disappear from the chart, and when checked, it would reappear.

_**Try it Yourself.. Download the file  
**_[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dynamic-Chart-in-Excel-with-Series-Selection-Check-box.xls)

**You May Also Like the Following Excel Tutorials:**

*   [Creating Dynamic Chart Titles in Excel](https://trumpexcel.com/dynamic-chart-titles-in-excel/)
    .
*   [Dynamic Pareto Chart – The 80/20 Rule.](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [Dynamic Target Line in Excel Bar Charts.](https://trumpexcel.com/dynamic-target-line-in-excel/)
    
*   [How to Create a Dynamic Chart Range in Excel](https://trumpexcel.com/dynamic-chart-range/)
    .
*   [Creating Combination Charts in Excel](https://trumpexcel.com/combination-charts-in-excel/)
    .
*   [Inserting a checkmark in Excel](https://trumpexcel.com/check-mark/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “Dynamic Excel Chart with Series Selection Check-box”
-------------------------------------------------------------------

1.  Hi Sumit,  
    I got the formulas all to work. How do I get the check boxes on the chart itself?
    
    [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-12377)
    
2.  Hi Sumit, All works well until I get to changing the 2011 bar to line. It changes the whole chart to line. I follow the instructions exactly, “Click on any data bar for 2011 (this will select all the data bars for 2011) and right click. From the menu select Change Series Chart Type. This will change the chart type from a bar chart to a line chart” but the whole chart changes. Help?
    
    [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-10878)
    
3.  great job. It’s very impressive and clear, thanks you.
    
    [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-2094)
    
4.  Very good this article
    
    [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-2086)
    
    *   Thanks for commenting Pablo.. Glad you like it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-2088)
        
5.  good
    
    [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-1472)
    
    *   Thanks for stopping by and commenting 🙂
        
        [Reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#comment-2089)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-excel-chart-check-box/#respond)

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