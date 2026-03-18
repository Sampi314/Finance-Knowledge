# Stacked total

**Source:** https://www.andypope.info/charts/stackcoltotal.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Display Total within a stacked column chart

  

![](https://www.andypope.info/charts/sct3.gif)  
 

 

##### Using a dummy data series on the secondary axis.

##### Here is our data set. The actual chart data is in the range A1:D5  
I have added formula to E2:E5 to store the cumulative total to be displayed.  

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
|     | ##### **A** | ##### **B** | ##### **C** | ##### **D** | ##### **E** |
| ##### **1** |     | ##### Data A | ##### Data B | ##### Data C | ##### Total |
| ##### **2** | ##### Qrt 1 | ##### 2 | ##### 4 | ##### 4 | ##### \=SUM(B2:D2) |
| ##### **3** | ##### Qrt 2 | ##### 2 | ##### 2 | ##### 3 | ##### \=SUM(B3:D3) |
| ##### **4** | ##### Qrt 3 | ##### 3 | ##### 1 | ##### 2 | ##### \=SUM(B4:D4) |
| ##### **5** | ##### Qrt 4 | ##### 4 | ##### 1 | ##### 1 | ##### \=SUM(B5:D5) |

##### Select the range A1:E5 and use the chart wizard to create a standard Stacked column chart.

##### ![](https://www.andypope.info/charts/sct1.gif)

##### Select the data series 'Total' and via the Format Data Series dialog (CTRL+1) change the Axis to Secondary axis.

##### ![](https://www.andypope.info/charts/sct8.gif)

##### This will make the 'Total' data series appear in front of the other data series.

##### ![](https://www.andypope.info/charts/sct2.gif)

##### To finish off format the 'Total' data series to have no border and no pattern. This will allow the other data series to be seen. Also apply Value data labels.

##### ![](https://www.andypope.info/charts/sct3.gif)

##### To remove the extra data series form the legend see "[Delete legend entry](https://www.andypope.info/charts/deletelegendentry.htm)
"

##### Using a dummy series on the same axis

##### This time our data set includes 2 helper columns. E2:E5 contains a constant value that will be used to display the data labels. F2:F5 contains formula for the cumulative total.

|     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
|     | ##### **A** | ##### **B** | ##### **C** | ##### **D** | ##### **E** | ##### **F** |
| ##### **1** |     | ##### Data A | ##### Data B | ##### Data C | ##### Dummy | ##### Total |
| ##### **2** | ##### Qrt 1 | ##### 2 | ##### 4 | ##### 4 | ##### 2 | ##### \=SUM(B2:D2) |
| ##### **3** | ##### Qrt 2 | ##### 2 | ##### 2 | ##### 3 | ##### 2 | ##### \=SUM(B3:D3) |
| ##### **4** | ##### Qrt 3 | ##### 3 | ##### 1 | ##### 2 | ##### 2 | ##### \=SUM(B4:D4) |
| ##### **5** | ##### Qrt 4 | ##### 4 | ##### 1 | ##### 1 | ##### 2 | ##### \=SUM(B5:D5) |

##### Format the 'Dummy' data series as before, setting the border and pattern to none.  
Apply the values data labels.

##### ![](https://www.andypope.info/charts/sct5.gif)

##### Format the 'Dummy' data series as before, setting the border and pattern to none.  
Apply the values data labels

##### ![](https://www.andypope.info/charts/sct5.gif)

##### In order to get the data labels to display there cumulative total instead of there true value we need to alter the text.

##### ![](https://www.andypope.info/charts/sct6.gif)

##### Static method:  
Select the data labels and then select an individual data label. Simply edit the text in the data label.

##### Dynamic link method:  
Select the data labels and then select an individual label. Go to the formula bar and enter '=' (_without quotes_) and then select the cell to be linked. This will enter the full cell address. If you want you can just type the address directly in the formula bar.

##### ![](https://www.andypope.info/charts/sct9.gif)

##### Here are 2 free add-ins to make the chore of linking data labels to cells easier.

##### Rob Bovey's [Chart Labeler](http://www.appspro.com/Utilities/ChartLabeler.htm)
John Walkenbach's [Chart Tools](http://j-walk.com/ss/excel/files/charttools.htm)

##### The use of a dummy series on the same axis is suitable for use with 3d stacked column charts

##### ![](https://www.andypope.info/charts/sct7.gif)

        

Created August 2004

Last updated 5th August 2014 

  
           [![Return to main page](https://www.andypope.info/Site_Images/nav_home.png)](https://www.andypope.info/index.htm "Return to home page")
 [![Chart Section](https://www.andypope.info/Site_Images/nav_charts.png)](https://www.andypope.info/charts.htm "Goto Charts Section")
 [![VBA section](https://www.andypope.info/Site_Images/nav_vba.png)](https://www.andypope.info/vba.htm "Goto VBA Section")
 [![Fun and games section](https://www.andypope.info/Site_Images/nav_fun.png)](https://www.andypope.info/fun.htm "Goto Fun & Games Section")
 [![Forum files](https://www.andypope.info/Site_Images/nav_forum.png)](https://www.andypope.info/newsgroups.htm "Goto Forum Section")
 [![Tips section](https://www.andypope.info/Site_Images/nav_tips.png)](https://www.andypope.info/tips.htm "Goto Tips & Tricks Section")
 [![Links section](https://www.andypope.info/Site_Images/nav_links.png)](https://www.andypope.info/links.htm "Goto Excel Resources Section")
 [![Book section](https://www.andypope.info/Site_Images/nav_books.png)](https://www.andypope.info/books.htm "Goto Books section")
 [![Site information](https://www.andypope.info/Site_Images/nav_info.png)](https://www.andypope.info/about.htm "Goto About Section")
 [![Site Search](https://www.andypope.info/Site_Images/nav_search.png)](https://www.andypope.info/search.htm "Goto Site Search")
[![RSS feed](https://www.andypope.info/Site_Images/nav_rss.png)](https://www.andypope.info/feed/feed.xml "RSS Feed")
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/stackcoltotal.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope