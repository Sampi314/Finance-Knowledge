# Print format codes

**Source:** https://www.andypope.info/tips/tip017.htm

---

[![AJP Excel Information](https://www.andypope.info/Site_Images/excel_white.png)](https://www.andypope.info/index.htm)
 AJP Excel Information

[![](https://www.andypope.info/Site_Images/nav_pagereturn.png)](https://www.andypope.info/tips.htm "Go up a section")
 ![](https://www.andypope.info/Site_Images/nav_pageback.png "Go Back to previous page")

### Formatting and VBA Codes for Headers and Footers

The following special formatting and Visual Basic for Applications (VBA) codes can be included as a part of the header and footer properties (LeftHeader, CenterHeader, RightHeader, LeftFooter, CenterFooter, and RightFooter).

|     |     |
| --- | --- |
| **Format code** | **Description** |
| &L  | Left aligns the characters that follow. |
| &C  | Centers the characters that follow. |
| &R  | Right aligns the characters that follow. |
| &E  | Turns double-underline printing on or off. |
| &X  | Turns superscript printing on or off. |
| &Y  | Turns subscript printing on or off. |
| &B  | Turns bold printing on or off. |
| &I  | Turns italic printing on or off. |
| &U  | Turns underline printing on or off. |
| &S  | Turns strikethrough printing on or off. |
| &"fontname" | Prints the characters that follow in the specified font. Be sure to include the double quotation marks. |
| &nn | Prints the characters that follow in the specified font size. Use a two-digit number to specify a size in points. |
| &H&Kcolor | Prints the characters in the specified color. User supplies a hexidecimal color value. |
| &"+" | Prints the characters that follow in the Heading font of the current theme. Be sure to include the double quotation marks. |
| &"-" | Prints the characters that follow in the Body font of the current theme. Be sure to include the double quotation marks. |
| &Kxx.Syyy | Prints the characters that follow in the specified color from the current theme. xx is a two-digit number from 1 to 12 that specifies the theme color to use. Snnn specifies the shade (tint) of that theme color. Specify S as + to produce a lighter shade; specify S as - to produce a darker shade. nnn is a three-digit whole number that specifies a percentage from 0 to 100. If the values that specify the theme color or shade are not within the described limits, Excel will use the nearest valid value. |
| &D  | Prints the current date. |
| &T  | Prints the current time. |
| &F  | Prints the name of the document. |
| &A  | Prints the name of the workbook tab. |
| &P  | Prints the page number. |
| &P+number | Prints the page number plus the specified number. |
| &P-number | Prints the page number minus the specified number. |
| &&  | Prints a single ampersand. |
| &N  | Prints the total number of pages in the document. |
| &Z  | Prints the file path. |
| &G  | Inserts an image. |

Created 29th December 2013

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
 [![Top of page](https://www.andypope.info/Site_Images/nav_top.png)](https://www.andypope.info/tips/tip017.htm#Top "Return to top of page")

  
  
Microsoft® and Microsoft® Excel are registered trademarks of the Microsoft Corporation.  
andypope.info is not associated with Microsoft. Copyright ©2007-2016 Andy Pope