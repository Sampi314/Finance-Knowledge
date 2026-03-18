# How to Create a Dynamic Chart Range in Excel

**Source:** https://trumpexcel.com/dynamic-chart-range

---

[Skip to content](https://trumpexcel.com/dynamic-chart-range/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/dynamic-chart-range/#below-title)

When you create a chart in Excel and the source data changes, you need to update the chart’s data source to make sure it reflects the new data.

In case you work with charts that are frequently updated, it’s better to create a dynamic chart range.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/dynamic-chart-range/#)

What is a Dynamic Chart Range?
------------------------------

A dynamic chart range is a data range that updates automatically when you change the data source.

This dynamic range is then used as the source data in a chart. As the data changes, the dynamic range updates instantly which leads to an update in the chart.

Below is an example of a chart that uses a dynamic chart range.

![Dynamic Chart Range in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20692%20320'%3E%3C/svg%3E)

Note that the chart updates with the new data points for May and June as soon as the data in entered.

How to Create a Dynamic Chart Range in Excel?
---------------------------------------------

There are two ways to create a dynamic chart range in Excel:

*   Using Excel Table
*   Using Formulas

In most of the cases, using [Excel Table](https://trumpexcel.com/excel-table/)
 is the best way to create dynamic ranges in Excel.

Let’s see how each of these methods work.

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2017/08/Dynamic-Chart-Ranges-Excel.xlsx)
**.

### Using Excel Table

Using Excel Table is the best way to create dynamic ranges as it updates automatically when a new data point is added to it.

Excel Table feature was introduced in Excel 2007 version of Windows and if you’re versions prior to it, you won’t be able to use it (see the next section on creating dynamic chart range using formulas).

**Pro Tip:** To convert a range of cells to an Excel Table, select the cells and use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 – Control + T (hold the Control key and press the T key).

In the example below, you can see that as soon as I add new data, the Excel Table expands to include this data as a part of the table (note that the border and formatting expand to include it in the table).

![Creating a Dynamic Chart Range in Excel using Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20220%20240'%3E%3C/svg%3E)

Now, we need to use this Excel table while creating the charts.

Here are the exact steps to create a dynamic line chart using the Excel table:

*   Select the entire Excel table.![Select the Excel table with which to create dynamic chart range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20262%20199'%3E%3C/svg%3E)
*   Go to the Insert tab.![Click on insert tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20135'%3E%3C/svg%3E)
*   In the Charts Group, select ‘Line with Markers’ chart.![Click on Line Chart with markers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20449'%3E%3C/svg%3E)

That’s it!

The above steps would insert a line chart which would automatically update when you add more data to the Excel table.

Note that while adding new data automatically updates the chart, deleting data would not completely remove the data points. For example, if you remove 2 data points, the chart will show some empty space on the right. To correct this, drag the blue mark at the bottom right of the Excel table to remove the deleted data points from the table (as shown below).

![Deleting Data from Excel Table](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20332'%3E%3C/svg%3E)

While I have taken the example of a line chart, you can also create other chart types such as column/bar charts using this technique.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2017/08/Dynamic-Chart-Ranges-Excel.xlsx)

### Using Excel Formulas

As I mentioned, using Excel table is the best way to create dynamic chart ranges.

However, if you can’t use Excel table for some reason (possibly if you are using Excel 2003), there is another (slightly complicated) way to create dynamic chart ranges using [Excel formulas](https://trumpexcel.com/excel-functions/)
 and [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
.

Suppose you have the data set as shown below:

![Data for creating dynamic named range in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20213%20210'%3E%3C/svg%3E)

To create a dynamic chart range from this data, we need to:

1.  Create two dynamic named ranges using the OFFSET formula (one each for ‘Values’ and ‘Months’ column). Adding/deleting a data point would automatically update these named ranges.
2.  Insert a chart that uses the named ranges as a data source.

Let me explain each step in detail now.

#### Step 1 – Creating Dynamic Named Ranges

Below are the steps to create dynamic named ranges:

*   Go to the ‘Formulas’ Tab.![Formulas tab in Excel for creating dynamic charts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20130'%3E%3C/svg%3E)
*   Click on ‘Name Manager’.![Name Manager in Formulas Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20465%20129'%3E%3C/svg%3E)
*   In the Name Manager dialog box, specify the name as **ChartValues** and enter the following formula in Refers to part: \=OFFSET(Formula!$B$2,,,COUNTIF(Formula!$B$2:$B$100,”<>”))![ChartValues Named Range Dialog Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20232'%3E%3C/svg%3E)
*   Click OK.
*   In the Name Manager dialog box, click on New.
*   In the Name Manager dialog box, specify the name as **ChartMonths** and enter the following formula in Refers to part: \=OFFSET(Formula!$A$2,,,COUNTIF(Formula!$A$2:$A$100,”<>”))![Creating Named Range for Months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20232'%3E%3C/svg%3E)
*   Click Ok.
*   Click Close.

The above steps have created two named ranges in the Workbook – ChartValue and ChartMonth (these refer to the values and months range in the data set respectively).

If you go and update the value column by adding one more data point, the ChartValue named range would now automatically update to show the additional data point in it.

The magic is done by the [OFFSET function](https://trumpexcel.com/excel-offset-function/)
 here.

In the ‘ChartValue’ named range formula, we have specified B2 as the reference point. OFFSET formula starts there and extends to cover all the filled cells in the column.

The Same logic works in the ChartMonth named range formula as well.

#### Step 2 – Create a Chart Using these Named Ranges

Now all you need to do is insert a chart that will use the named ranges as the data source.

Here are the steps to insert a chart and use dynamic chart ranges:

*   Go to the Insert tab.![Insert Chart from Ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20376%20127'%3E%3C/svg%3E)
*   Click on ‘Insert Line or Area Chart’ and insert the ‘Line with markers’ chart. This will insert the chart in the worksheet.![Click on Line Chart with markers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20449'%3E%3C/svg%3E)
*   With the chart selected, go to the Design tab.![Design tab - Contextual tab that appears when a chart is selected](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20174'%3E%3C/svg%3E)
*   Click on Select Data.![Select Data in the Design tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20542%20162'%3E%3C/svg%3E)
*   In the ‘Select Data Source’ dialog box, click on the Add button in ‘Legend Entries (Series)’.![Add Series Data for the Excel Dynamic Chart Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20304'%3E%3C/svg%3E)
*   In the Series value field, enter \=Formula!ChartValues (note that you need to specify the worksheet name before the named range for this to work).![Edit Series for Chart with Sheet name along with named range ChartValues](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20311%20158'%3E%3C/svg%3E)
*   Click OK.
*   Click on the Edit button in the ‘Horizontal (Category) Axis Labels’.![Horizontal Axis Values for months in Excel chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20584%20304'%3E%3C/svg%3E)
*   In the ‘Axis Labels’ dialog box, enter \=Formula!ChartMonths![Axis Namrd Range for Months in Excel Chart](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20306%20109'%3E%3C/svg%3E)
*   Click Ok.

That’s it! Now your chart is using a dynamic range and will update when you add/delete data points in the chart.

[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2017/08/Dynamic-Chart-Ranges-Excel.xlsx)

A few important things to know when using named ranges with charts:

*   There should not be any blank cells in the chart data. If there is a blank, named range would not refer to the correct dataset (as the total count would lead to it referring to less number of cells).
*   You need to follow the naming convention when using the sheet name in chart source. For example, if the sheet name is a single word, such as Formula, then you can use =Formula!ChartValue. But if there is more than one word, such as Formula Chart, then you need to use =’Formula Chart’!ChartValue.

**You May Also Like the Following Excel Tutorials:**

*   [How to Create a Thermometer Chart in Excel](https://trumpexcel.com/thermometer-chart/)
    .
*   [How to Make a Bell Curve in Excel.](https://trumpexcel.com/bell-curve/)
    
*   [Creating a Step Chart in Excel.](https://trumpexcel.com/step-chart-in-excel/)
    
*   [Creating a Pareto Chart in Excel.](https://trumpexcel.com/dynamic-pareto-chart-in-excel/)
    
*   [How to Make a Histogram in Excel](https://trumpexcel.com/histogram-in-excel/)
    
*   [How to Add Error Bars in Excel (Horizontal/Vertical/Custom)](https://trumpexcel.com/error-bars-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

17 thoughts on “How to Create a Dynamic Chart Range in Excel”
-------------------------------------------------------------

1.  Thanks for a great tip!
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-14627)
    
2.  I haven’t tried this yet but superbly explained. I am keeping my fingers crossed it will work out as I hope it should. Keep up your good work and comprehensive explanations and “how-to” details.
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-14439)
    
3.  Are you aware that the latest version of Excel throws an error message?  
    “Excel found a problem with one or more formula references in this worksheet”
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-14136)
    
4.  This is amazing! It is exactly the solution I needed to deal with this aggravating pivot table disappearing custom chart formatting issue. Thank you!
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-13268)
    
5.  When I have to do ‘something’ myself anyway to get rid of excess chart space like in the first example – it is not really dynamic in my mind. My hope was to have a completely self adjusting chart in every sense.
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-12868)
    
6.  • I want to make a chart which doesn’t include the all the data of the table and its data range include the data from middle to end of the table. I have found that the dynamic feature of charts using table data doesn’t hold in this case. Is there a way to correct this problem?
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-11688)
    
7.  When you said “In the Series value field, enter =Formula!ChartValues (note that you need to specify the worksheet name before the named range for this to work).” What would the syntax be to specify the worksheet name.
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-11590)
    
    *   Hi Dan,  
        The author forgot to mention that his Sheet name is called “Formula” so you need to change “Formula” in to you you Sheet name. If your Sheet name is called “Sheet1” the correct named range for ChartMonths would be “=OFFSET(Sheet1!$A$2,,,COUNTIF(Sheet1!$A$2:$A$100,””))” and referencing this Named Range in graph would be “=Sheet1!ChartMonths”
        
        [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-43158)
        
8.  Hi,  
    Do you know if Excel functionalities changed since you made those “offset” formula.  
    I have copied exactly what you’ve done and it does not work…  
    I have no clue why.  
    Thanks
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-11256)
    
    *   Hi Gregory,  
        The author forgot to mention that his Sheet name is called “Formula” so you need to change “Formula” in to you you Sheet name. If your Sheet name is called “Sheet1” the correct named range for ChartMonths would be “=OFFSET(Sheet1!$A$2,,,COUNTIF(Sheet1!$A$2:$A$100,””))” and referencing this Named Range in graph would be “=Sheet1!ChartMonths”
        
        [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-43159)
        
9.  In Step 1 – Creating Dynamic Named Ranges, shouldn’t your formulas used in the ‘Refers to’ field of the dynamic range names, viz;  
    \=OFFSET(Formula!$B$2,,,COUNTIF(Formula!$B$2:$B$100,””))  
    include some value after the “”?  
    For example, to count the number values in column B to determine the number of rows in the range, shouldn’t the formula be:  
    \=OFFSET(Formula!$B$2,,,COUNTIF(Formula!$B$2:$B$100,”” & 0))
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-10826)
    
10.  Hello,
    
    I have a table with two columns, One Date(For Example Jan 2015…….. Dec 2017),  
    The Second (For Example Monthly Temporature for each month)
    
    I created a 2 dropdown menu lists (Start Date and End Date).  
    and I put Error Message Box for Start Date should be Prior to End Date.
    
    I want to create ( a Dynamic Graph (Chart) link to two dropdown menu which  
    when you change Start Date and End Date of dropdown Menu’s, the chart Automatically Update the graph based on
    
    new dropdown menu.
    
    I would like to know, Is it possible with VBA or not? or It’s asking too much from VBA 😉
    
    Thanks,  
    Amir
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-10373)
    
11.  Dear sumit sir from last 2 days i didnt get any mail. I hope and pray you are good and fine.
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-9706)
    
12.  Thank you very much for this awesome tutorial, I am impressed that this can be achieved in Excel, great!! What’s the meaning of ”” in COUNTIF formula?
    
    [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-9696)
    
    *   Thanks for commenting Juan.. is an operator that meas ‘not equal to’. In the COUNTIF function, it is used in double quotes with a blank (“”). This means that COUNTIF will count all the cells that are not empty.
        
        [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-9698)
        
        *   Sumit: i don´t see the blank in four formula: is it there?
            
            [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-9700)
            
        *   Thank you very much for the great explanation Sumit
            
            [Reply](https://trumpexcel.com/dynamic-chart-range/#comment-9702)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/dynamic-chart-range/#respond)

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