# Hilite axis labels

**Source:** https://www.andypope.info/charts/hiliteaxislabels.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/charts.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Conditionally highlight axis labels

  

![](https://www.andypope.info/charts/hla.gif) 
----------------------------------------------

##### The above chart high lights the X axis category labels when the monthly data drops below 25.  
  
This effect is achieved by using the data labels of 2 extra data series, plotted as lines.

  

##### Here is the data and formula used to build the chart. The actual data for the column chart is in the range C3:C14.  
The formula in columns D and E test the Data value and either output a zero or #N/A depending on whether a red or blue label should be displayed. 

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|     | B   | C   | D   | E   |
| 2   |     | Data | Red Labels | Blue Labels |
| 3   | Jan | 82  | \=IF(C3<25,0,NA()) | \=IF(C3>=25,0,NA()) |
| 4   | Feb | 99  | \=IF(C4<25,0,NA()) | \=IF(C4>=25,0,NA()) |
| 5   | Mar | 81  | \=IF(C5<25,0,NA()) | \=IF(C5>=25,0,NA()) |
| 6   | Apr | 20  | \=IF(C6<25,0,NA()) | \=IF(C6>=25,0,NA()) |
| 7   | May | 4   | \=IF(C7<25,0,NA()) | \=IF(C7>=25,0,NA()) |
| 8   | Jun | 35  | \=IF(C8<25,0,NA()) | \=IF(C8>=25,0,NA()) |
| 9   | Jul | 76  | \=IF(C9<25,0,NA()) | \=IF(C9>=25,0,NA()) |
| 10  | Aug | 67  | \=IF(C10<25,0,NA()) | \=IF(C10>=25,0,NA()) |
| 11  | Sep | 15  | \=IF(C11<25,0,NA()) | \=IF(C11>=25,0,NA()) |
| 12  | Oct | 18  | \=IF(C12<25,0,NA()) | \=IF(C12>=25,0,NA()) |
| 13  | Nov | 63  | \=IF(C13<25,0,NA()) | \=IF(C13>=25,0,NA()) |
| 14  | Dec | 16  | \=IF(C14<25,0,NA()) | \=IF(C14>=25,0,NA()) |

  ![](https://www.andypope.info/charts/hla_1.gif)

##### Select the range B2:E14 and use the chart wizard to build a standard Clustered Column chart.

   ![](https://www.andypope.info/charts/hla_2.gif)

##### Select the 'Red Label' line and right mouse click. From the popup menu choose Chart Type. Select the Line chart.

##### Repeat for the 'Blue Label' series

   ![](https://www.andypope.info/charts/hla_3.gif)

##### Double click the 'Red Labels' series and on the Data Labels tab of the Format Data Series dialog check the Category name option.

   ![](https://www.andypope.info/charts/hla_4.gif)

##### Repeat the application of data labels for the 'Blue Labels' series 

   ![](https://www.andypope.info/charts/hla_5.gif)

##### Double click the 'Red Labels' data labels and on the Alignment tab of the Format Data Labels dialog set the Label Position to Below. 

   ![](https://www.andypope.info/charts/hla_6.gif)

##### Repeat data label label position for the 'Blue Labels' series. 

  ![](https://www.andypope.info/charts/hla_7.gif)

##### Double click the X axis and on the Patterns tab of the Format Axis dialog set the Tick Mark Labels to none.

##### This will clear the built-in axis labels. 

  ![](https://www.andypope.info/charts/hla_8.gif)    ![](https://www.andypope.info/charts/hla_10.gif)

##### Double click the 'Red Labels' data labels and on the Font tab of the Format Data Labels dialog set the Font Colour to Red.

   ![](https://www.andypope.info/charts/hla_11.gif)

##### Repeat for the 'Blue Labels' data labels. Setting the Font Colour to Blue.

 

 ![](https://www.andypope.info/charts/hla_12.gif)

##### Double click the 'Red Labels' data series and on the Patterns tab of the Format Data Series set the Line and Marker to None.

   ![](https://www.andypope.info/charts/hla_13.gif)

##### Repeat for the 'Blue Labels' series. 

  

##### For a explanation of how to remove the extra series from the legend see, [Delete a single entry from the legend](http://www.andypope.info/charts/deletelegendentry.htm)
.

     

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/charts/hiliteaxislabels.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope