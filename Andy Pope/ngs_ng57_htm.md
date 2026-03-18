# AJP Excel Information

**Source:** https://www.andypope.info/ngs/ng57.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/newsgroups.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

 

|     |     |
| --- | --- |
|     | Re: Data labels linked to filtered data<br>--------------------------------------- |
|     | ##### ![](https://www.andypope.info/ngs/ng57a.gif)<br><br>##### When data labels are linked to cells that are not those used for the Category or Series text and the data is filtered the displayed text if incorrect. This is because the actual points displayed are always sequential.<br><br>##### So **if points 1, 2 and 3 are showing and you then filter out point 2 what is displayed is 1 and 2 rather than 1 and 3. Obviously the actual values used are correct but the linked labels become incorrect.**<br><br>##### To avoid this problem you can use some helper columns that automatically revise the order of the linked labels.  <br>  <br>The following is an example data set including helper columns. The actual chart is based on first 2 columns.<br><br>![](https://www.andypope.info/ngs/ng57b.gif)<br><br>##### And here are the formula used to create the Indexed text.<br><br>![](https://www.andypope.info/ngs/ng57c.gif)<br><br>##### And this is what the chart looks like unfiltered. The first series has it data labels linked to the Labels column. The second series is linked to the Indexed text column.<br><br>![](https://www.andypope.info/ngs/ng57d.gif)<br><br>##### When the data is filtered on Data = 1 you can see the normally linked data labels are incorrect but the Indexed labels work.  <br>This is because the SUBTOTAL formula returns different values if the row is hidden. For visible rows the actual row number is returned otherwise a value greater than the last row, I used 999, is returned.  <br>The Ordered column then uses this value to create a row index value used in the INDEX formula. Because the formula is also in the rows that are filtered you can not see the complete set of labels.  <br>  <br>Here is the data filtered on Data =1<br><br>![](https://www.andypope.info/ngs/ng57e.gif)<br><br>##### You can see the second data series in the chart displays the labels of the filtered rows.<br><br>![](https://www.andypope.info/ngs/ng57a.gif)<br><br>##### Here is an [Example file](https://www.andypope.info/ngs/ng57.zip)<br><br>For information on [linking data labels](https://www.andypope.info/tips/tip001.htm)<br> to cells.  <br>  <br>Free add-in<br><br>##### [Rob Bovey's XY Chart labeler](http://www.appspro.com/Utilities/ChartLabeler.htm) |
|     |
|     |
|     |

  

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/ngs/ng57.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope