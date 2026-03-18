# Highlight Data Points in Excel with a Click of a Button

**Source:** https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel

---

[Skip to content](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#below-title)

**Watch Video – Highlight Data Points in Excel with a Click of a Button**

A chart gets difficult to read if it has a lot of data plotted on it. While it is a good practice to plot only the relevant data, there are situations where you need to show a lot of data points on a single chart.

If you are stuck in such a situation, it is a good idea to have a dynamic chart that highlights the selected series so that it is easier to read and compare. Something as shown below:

![Highlight Data Points in Excel - Dynamic Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20336'%3E%3C/svg%3E)

In the above chart, when you click on the button, the selected year’s series gets highlighted with red marker outline and the data labels.

**Follow Along.. Download the Chart**  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/vjq0xtpr2ff0s3m/Highlight-Data-Points-in-Excel-Dynamic-Chart.xlsm?dl=1)

Highlight Data Points in Excel Line Chart
-----------------------------------------

Here is how you can create this type of charts:

1.  Get the data in place. For this chart, I have Revenue Growth numbers for each quarter during 2012-15.  
    ![Highlight Data Points in Excel - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20148'%3E%3C/svg%3E)
2.  Select the entire data, go to Insert –> Charts –> Line with Markers. This would insert a line chart with three different lines for each year.  
    ![Highlight Data Points in Excel - Insert Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20300'%3E%3C/svg%3E)
3.  Go to Insert –> Illustrations –> Shapes –> Rounded Rectangle. Click anywhere on the worksheet and it will insert a Rounded Rectangle in the worksheet.  
    ![Highlight Data Points in Excel - Insert Shapes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20211'%3E%3C/svg%3E)
4.  Insert 2 more Rounded Rectangles and place it over the chart. Enter the Series Name (years) in the shapes as shown below:  
    ![Highlight Data Points in Excel - Shapes Aligned with Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20336'%3E%3C/svg%3E)
5.  Select the rectangle for 2013, go to [Name Box](https://trumpexcel.com/name-box-excel/)
     and enter 2013. Similarly, do the same for 2014 and 2015 boxes as well _(Name Box is at the left of formula bar)._  
    ![Highlight Data Points in Excel - Name Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%2043'%3E%3C/svg%3E)
6.  In cell F2, enter 2013 (you can enter any year from the data).
7.  In cell F3, enter the following combination of [INDEX](https://trumpexcel.com/excel-index-function/)
    , [ROWS](https://trumpexcel.com/excel-rows-function/)
     and [MATCH](https://trumpexcel.com/excel-match-function/)
     functions (and drag it for cells F3:F6)
    
    \=INDEX($B$3:$D$6,ROWS($E$3:E3),MATCH($F$2,$B$2:$D$2,0))
    
8.  Select cells F3:F6 and copy it (press Control + C), select the chart and paste (control + v). This would create two lines for the same year (while copying, notice that the line color of the selected year changes).
9.  Select the line for the year (for which you copied the data), right click and select Format Series Data. In the Format Data Series:
    *   Change Line Color to No Line  
        ![Highlight Data Points in Excel - No Line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20230'%3E%3C/svg%3E)
    *   In Marker Options, make the following changes
        *   Built-in Type: Round shape
        *   Built-in Size: 15
    *   Change the Marker Fill to No Fill  
        ![Highlight Data Points in Excel - Marker Fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20272%20376'%3E%3C/svg%3E)
    *   Change Marker Border Color (I have used red color), width and dash type  
        ![Highlight Data Points in Excel - Marker Border](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20442'%3E%3C/svg%3E)
    *   Right click on any of the round markers and select Add Data Labels. [Format it to show percentages](https://trumpexcel.com/calculate-percentages-excel/)
        

If you have followed all the above steps, you would have something as shown below:  
![Highlight Data Points in Excel - Chart without vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20344'%3E%3C/svg%3E)

Now to make the buttons functional, we will use a simple VBA code.

### The VBA code

We will use VBA code to do 2 things:

*   Change the year value in cell F3 when the shape is clicked, and
*   Change the color of the selected shape

Simply copy the following code in the VB Editor.

Sub SelectYear2013()
Range("F2").Value = 2013
ActiveSheet.Shapes("2013").Fill.ForeColor.RGB = RGB(176, 196, 222)
ActiveSheet.Shapes("2014").Fill.ForeColor.RGB = RGB(255, 255, 255)
ActiveSheet.Shapes("2015").Fill.ForeColor.RGB = RGB(255, 255, 255)
End Sub

Sub SelectYear2014()
Range("F2").Value = 2014
ActiveSheet.Shapes("2013").Fill.ForeColor.RGB = RGB(255, 255, 255)
ActiveSheet.Shapes("2014").Fill.ForeColor.RGB = RGB(176, 196, 222)
ActiveSheet.Shapes("2015").Fill.ForeColor.RGB = RGB(255, 255, 255)
End Sub
Sub SelectYear2015()
Range("F2").Value = 2015
ActiveSheet.Shapes("2013").Fill.ForeColor.RGB = RGB(255, 255, 255)
ActiveSheet.Shapes("2014").Fill.ForeColor.RGB = RGB(255, 255, 255)
ActiveSheet.Shapes("2015").Fill.ForeColor.RGB = RGB(176, 196, 222)
End Sub

To copy this code:

*   Press Alt + F11. It will open the VBE Editor.
*   Go to Insert and click on Module. This will insert a module.
*   Double click on module icon, and paste the code on the code area on the right.

#### Assign Macros to Buttons

Once you have the VBA code in place, you need to [assign macros to the buttons](https://trumpexcel.com/assign-macro-to-button-in-excel/)
/shapes. To do this:

*   Right-click on the shape and select Assign Macro.
*   In the Assign Macro dialog box, select the macro and click OK.  
    ![Highlight Data Points in Excel - Assign Macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20369%20284'%3E%3C/svg%3E)

_Note: Since this workbook contains a macro, save it as a .xlsm or .xls format file._

Now your dynamic chart is ready. With a single click, you can now highlight data points for the selected series.

**Download the file**  
[![Download File Pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20142%2042'%3E%3C/svg%3E)](https://www.dropbox.com/s/vjq0xtpr2ff0s3m/Highlight-Data-Points-in-Excel-Dynamic-Chart.xlsm?dl=1)

**More on Dynamic Excel Charting Tutorials:**

*   [Dynamic Pareto Chart in Excel](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    .
*   [Dynamic Target Line in Excel Bar Charts](https://trumpexcel.com/dynamic-target-line-in-excel/)
    .
*   [Spot the Data Point in Excel Scatter Chart](https://trumpexcel.com/spot-data-point-in-excel-scatter-chart/)
    .
*   [Dynamic Chart with Series Selection Check Box](https://trumpexcel.com/dynamic-excel-chart-check-box/)
    .
*   [How to Create Dynamic Chart Titles in Excel](https://trumpexcel.com/dynamic-chart-titles-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “Dynamic Charting – Highlight Data Points in Excel with a Click of a Button”
------------------------------------------------------------------------------------------

1.  Hello Sumit,  
    I have market data for various brands for 2013, 2014, 2015 and it contains varying data types (i.e. Numbers, %ages and floats etc). How can I use charts to show these values with dynamic Y-Axis values according to the particular column header.
    
    Note: My data is like:- Brands in rows and various parameters in column headings. Above column headings I have year for particular set of headings. I need something like you showed here in this article. Please help.
    
    [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2333)
    
2.  Great..wonderful..I can impress my boss with this one! thanks Sumit!
    
    [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2240)
    
    *   That’s what we all want 😉 Glad you liked it
        
        [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2241)
        
3.  Sumit,  
    I like your concept for highlighting the data points in the chart.  
    I will typically create a dummy pivot table based on a list of the years so that I can use slicers to select the year to highlight the data points instead of shapes. This eliminates the need for the VBA code and adding named ranges in setting up the chart.
    
    [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2235)
    
    *   Thanks for sharing. It is a good alternate approach for this 🙂
        
        [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2238)
        
4.  This is awesome. Now I can see hundreds of situations where I could have used it. Thanks for sharing this..
    
    [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2233)
    
    *   Thanks for commenting Glen. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#comment-2234)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-charting-highlight-data-points-in-excel/#respond)

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