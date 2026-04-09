# Mimic conditional formatting icons

**Source:** https://www.andypope.info/tips/tip011.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Mimic 2007 Conditional Formatting Icons

XL2007 has a extended conditional formatting to allow the display of icon sets. The following will demonstrate some ways in which you can create a similar appearance in previous versions of excel.  
  
Here is how XL2007 would display a small data table. The shift arrows are based on the difference between 2007 and 2006 Performance figures for each Widget.  
  
The 4 Rating columns are based on the comparison of the Sales of the Widgets.

![](https://www.andypope.info/tips/tip011a.gif)

Here is the same data table in xl2003

![](https://www.andypope.info/tips/tip011b.gif)

The arrows are the easiest to construct as this are based on characters from the Wingdings font.  
The cell D3 contains the following formula

\=MID("èéê",IF(C3-B3=0,1,IF(C3-B3>0,2,3)),1)

  
Lets break that formula down. The MID function returns a sub set of characters from a piece of text starting at a specific position and continuing for a specified number of characters. The piece of text is "èéê" which displayed using the wingdings font is èéê. The number of character we want displayed is always 1. The start position is determined by the compound IF function. The first test is for the 2 values being equal. If they are the number 1 if returned and used as the starting position. If not the second IF function is performed. If the difference between the 2007 and 2006 value is positive 2 is returned otherwise 3.  
The Shift Colour column contains the same formula in order to get the correct arrow displayed. The colour is provided by using normal conditional formatting.

![](https://www.andypope.info/tips/tip011c.gif)

The ratings icon requires some additional work to create the picture we will need in order to mask conditional formatting of cells.  
Start by creating 4 rectangular auto shapes increasing in size. Position these in front of a larger white rectangle with no border.  
Note: For the purposes of this page I have coloured the background shape so you can see it against a white background.

![](https://www.andypope.info/tips/tip011d.gif)

  
Select all five shapes and group them. Now whilst holding the SHIFT key click the Edit menu. You should see a new menu item **Copy Picture...**

![](https://www.andypope.info/tips/tip011e.gif)

You will then see a dialog that allows you copy the shape as a BMP picture.

![](https://www.andypope.info/tips/tip011f.gif)

Once you have copied the picture use paste to insert the new picture back into your workbook. If you select the picture you should see the Picture toolbar, if not right click the picture and pick Show Picture Toolbar...

![](https://www.andypope.info/tips/tip011g.gif)

You can now use the Set Transparent Color ![](https://www.andypope.info/tips/tip011h.gif) button to turn those Pink bars see-thru. Size and position the picture over the range G3:J3. The 4 columns are going to provide the colour for the bars but in order to get the correct number display we need a calculate how many to display and then apply conditional formatting on each column.  
Lets start with the formula to calculate whether to display 1, 2, 3 or 4 bars. Note that with the 4 rating bar 1 is always displayed so we can already set the fill colour of the cells in column G to Blue.  
This is the formula in G3  

\=VLOOKUP((F3-MIN($F$3:$F$6))/(MAX($F$3:$F$6)-MIN($F$3:$F$6)),{0,1;0.25,2;0.5,3;0.75,4},2,TRUE)

It calculates the percent value of the spread of a Sales figure in relations to all the Sales figures (I think!). The percentage is then used as the lookup value in the table with the following outcome  
4 bars when value is >= 75%  
3 bars when value is >=50% AND < 75%  
2 bars when value is >=25% AND < 50%  
1 bar when value is  <25%  
  
Now we need to apply conditional formatting to H3:H6

![](https://www.andypope.info/tips/tip011i.gif)

The conditional formatting for columns I and J is the same except the >1 part change to >2 and >3 respectively. You should now have cells displaying a blue pattern depending on the number in column G. The picture acts as a mask over those 4 columns. Here is the example workbook [CF\_Icons\_2003](https://www.andypope.info/tips/CF_Icons_2003.zip)

Created 10th October 2008

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip011.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope