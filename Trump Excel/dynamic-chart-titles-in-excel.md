# How to Create Dynamic Chart Titles in Excel

**Source:** https://trumpexcel.com/dynamic-chart-titles-in-excel

---

[Skip to content](https://trumpexcel.com/dynamic-chart-titles-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-chart-titles-in-excel/#below-title)

Do you suffer from Forgot-to-change-chart-titles syndrome? I do.

Worry not. Today’s prescription includes an article and a video on how to create dynamic chart titles in excel.

Linking a Cell Value to the Chart Title
---------------------------------------

Suppose you have the data as shown below and you have created a chart using it.

![Dynamic Chart Titles in Excel - Data for linking cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20280'%3E%3C/svg%3E)

If you want to change the chart title, you need to manually change it by typing the text in the box. Since the chart title is static, you would have to change it again and again whenever your data is refreshed/updated.

Here is how you can make it dynamic (i.e., make it refer to a cell in the workbook):

*   Click on the Chart Title box
*   Go to [Formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
     and type =
*   Select the cell that you want to show as the chart title
*   Hit Enter

![Dynamic Chart Titles in Excel - Data for linking cell Gif](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20688%20468'%3E%3C/svg%3E)

This technique could be wonderfully helpful if you get the data in a fixed format, and you update charts by simply copy pasting the new data. It would ensure that your Chart Titles get updated automatically.

Creating Dynamic Chart Titles in Excel by Combining Cell Link and Text
----------------------------------------------------------------------

Continuing with the above example, suppose I want to add some additional text to the chart title (let’s say I want to add (YoY) to the title). To do this, I will have to create a formula and get the result in a separate cell. Then I can link that cell to the Chart Title.

Here is how you can do this:

*   In a new cell, type the following formula
    
    \=A1&" (YoY)"
    
*   Click on the chart title box
*   Go to Formula bar and type =
*   Select the cell where you have the new chart title
*   Hit Enter

![Dynamic Chart Titles in Excel - Data for linking cell and Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20484'%3E%3C/svg%3E)

This simple trick can save you a lot of time, and it ensures you don’t have to worry about the Forgot-to-change-chart-titles syndrome.

**You May Also Like the Following Excel Tutorials:**

*   [Dynamic Charting – Highlight Data Point with a click of a button](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/)
    .
*   [Dynamic Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Spice up Chart Data Labels – Show Positive/Negative Trend Arrows](https://trumpexcel.com/excel-chart-data-labels-trend-arrows/)
    .
*   [Create Dynamic Target Line in Excel Bar Charts](https://trumpexcel.com/dynamic-target-line-in-excel/)
    .
*   [How to Create a Dynamic Chart Range in Excel](https://trumpexcel.com/dynamic-chart-range/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “How to Create Dynamic Chart Titles in Excel”
-----------------------------------------------------------

1.  Is there any way to make this formula automatically adjust when copying and changing the chart (plus reference cells) across a sheet?
    
    [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-11059)
    
2.  Hi. Thank you very mich for this tip. Is there a possibility to link the Text to a chosen filter? I’m working with Pivot Charts and the user has the possibility to choose between the machines in our company. In german, the functionality i use is called “Datenschnitt”.
    
    [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-10761)
    
3.  In Excel 2016 I need to add the sheet name, something like Sheet1!A1. And adding a label-text with & “added text” does not work at all. Any hints or workarounds? thanks
    
    [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-10139)
    
    *   I agree Kurt. I can’t seem to get it to work with the process listed above for a dynamic link.
        
        [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-13983)
        
    *   You will have to concatenate in another cell, then reference that cell in your chart title.
        
        [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-38045)
        
4.  Super great tip! Wish I had known about this years ago!
    
    [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-2336)
    
    *   Thanks for commenting Shana.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-2369)
        
5.  Wow – this is nice! Thanks
    
    [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-2244)
    
    *   Thanks for commenting Zoli.. Glad you like it 🙂
        
        [Reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#comment-2254)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-chart-titles-in-excel/#respond)

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