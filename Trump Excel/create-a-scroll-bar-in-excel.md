# How to Create a Scroll Bar in Excel - Step by Step Tutorial

**Source:** https://trumpexcel.com/create-a-scroll-bar-in-excel

---

[Skip to content](https://trumpexcel.com/create-a-scroll-bar-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/create-a-scroll-bar-in-excel/#below-title)

**Watch Video – Creating a Scroll Bar in Excel**

A Scroll Bar in Excel is what you need when you have a huge dataset and you don’t want it to hijack your entire screen’s real estate.

It’s a great tool to use in an [Excel Dashboard](https://trumpexcel.com/creating-excel-dashboard/)
 where you have to show a lot of data in a limited space.

In this step-by-step tutorial, I will show you how to create a scroll bar in excel.  You will also learn how to link a dataset to this dynamic scroll bar, such that when a user changes the scroll bar, the data accordingly changes.

Creating a Scroll Bar in Excel
------------------------------

For the purpose of this tutorial, I have taken the data for 28 states in India, along with each state’s area and population ([census 2001](http://www.censusindia.gov.in/2011census/population_enumeration.html)
).

Now, I want to create a data set that displays only 10 states at a time, and when the user changes the scroll bar, the data dynamically changes.

Something like this shown below:

![Scroll Bar in Excel - Scrollable List](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20867%20583'%3E%3C/svg%3E)

**[Click here to download the example file](https://trumpexcel.com/wp-content/uploads/2016/10/Creating-a-Scrollable-List.xls)
**

### Steps to Create a Scroll Bar in Excel

1.  The first step is to get your data in place. For the purpose of this post, I have used census 2001 data of 28 Indian States with its Area and Population.
2.  Go to Developer Tab –> Insert –> Scroll Bar (Form Control).![Scroll Bar in Excel- Scroll Bar pic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20398%20274'%3E%3C/svg%3E)_If you can’t find the developer tab in the ribbon, it is because it has not been enabled. By default, it’s hidden in Excel. You first need to [add the developer tab](https://trumpexcel.com/excel-developer-tab/)
     in the ribbon._
3.  Click on Scroll Bar (Form Control) button and click anywhere on your worksheet. This will insert a Scroll Bar in the excel worksheet.
4.  Right-click on the Scroll Bar and click on ‘Format Control’. This will open a Format Control dialog box.
5.  In the Format Control dialogue box go to the ‘Control’ tab, and make the following changes:
    *   Current Value: 1
    *   Minimum Value: 1
    *   Maximum Value: 19 _(it is 19 here as we display 10 rows at a time. So when the user makes the scroll bar value 19, it displays rows 19-28)_
    *   Incremental Change: 1
    *   Page Change: 5
    *   Cell Link: $L$3![Scroll Bar in Excel- format control dialogue box settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20425'%3E%3C/svg%3E)  
        _$L$3 is the cell that is linked to the scroll bar in Excel. Its value varies from 1 to 19. This is the cell value that we use to make the scrollable list. Don’t worry if it doesn’t make sense as of now. Just keep reading and it will become clear!!_
6.  Resize the Scroll Bar so that it fits the length of the 10 columns (this is just to give it a good look, as shown in the pic below).![Scroll Bar in Excel - empty 10 cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20266'%3E%3C/svg%3E)
7.  Now enter the following formula in the first cell (H4) and then copy it to fill all the other cells:  
    \=OFFSET(C3,$L$3,0)

Note that this [OFFSET formula](https://trumpexcel.com/excel-offset-function/)
 is dependent on cell L3, which is linked to the scroll bar.

Now you are all set with a Scroll Bar in Excel.

**How does this work?**

The OFFSET formula uses cell C3 as the reference cell and offsets it by the values specified by cell L3. Since L3 is linked to scroll bar value, when the scrollbar value becomes 1, the formula refers to the first state name. When it becomes 2, it refers to the second state.

Also, since C3 cell has not been locked, in the second row, the formula becomes \=OFFSET(C4,$L$3,0) and works the same way.

**Try it yourself.. Download the file  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Creating-a-Scrollable-List.xls)
**

**You May Also Like the Following Excel Tutorials:**

*   [Create Dynamic Labels in Scroll Bar in Excel](https://trumpexcel.com/dynamic-labels-in-excel-scroll-bar/)
    .
*   [How to Turn OFF Scroll Lock in Excel?](https://trumpexcel.com/turn-off-scroll-lock-excel/)
    
*   [How to Freeze Multiple Columns in Excel?](https://trumpexcel.com/freeze-multiple-columns-excel/)
    
*   [Adjust Scroll Bar Maximum Value based on a Cell Value in Excel](https://trumpexcel.com/adjust-scroll-bar-maximum-value/)
    .
*   [How to Insert and Use a CheckBox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [How to Insert and Use Checkmark and Crossmark symbols in Excel](https://trumpexcel.com/check-mark/)
    .
*   [How to Insert & Use a Radio Button in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .
*   [Creating Dynamic Filter in Excel](https://trumpexcel.com/dynamic-excel-filter/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

29 thoughts on “How to Create a Scroll Bar in Excel – Step by Step Tutorial”
----------------------------------------------------------------------------

1.  Very useful and helpful. Thank you for sharing. Very much appreciated.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-13783)
    
2.  Excellent video, thank you! Very helpful.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-13223)
    
3.  How can I also scroll down if the reference has images?
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-12976)
    
4.  Thanks a lot for your easy and beautiful clarification.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-12687)
    
5.  Thanks a lot
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-12085)
    
6.  A little mixed up as I already had my table done and just needed to insert the scroll bar.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-11624)
    
7.  Is there a way to do this where your scrolling table has data validation list drop downs in each of the fields? I have a table that consist of two column headers with 300 rows of empty cells where a user will select from a list. I would like to only have 10 to 20 rows visible as to not have to potentially scroll the entire worksheet down to row 300. is this possible? Your method above will not work since my table is more of a data entry vs. displaying data already available.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-11581)
    
8.  I don’t understand the Linking L3. It’s not shown in the example.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-10877)
    
9.  Awesome, Sumit..
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-9722)
    
10.  Mine worked – Thank you! How do you incorporate hyperlinks? I can attach the link, but the link will attach to the cell and whatever is in that one cell only… Any help would massively appreciated
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-9392)
    
11.  Great tutorial!  
    Question: in my original table I have a lot of functions, dates and even drop down menus. We use this online calendar so we see who in our team will be doing what on a day. This table counts for a year (long table) and with this scroll function I’d like to keep it above in the excel so we can keep the rest of the sheet in mind.  
    Is it possible the new scroll table takes over all functions from the original list?  
    thank you!  
    [https://uploads.disquscdn.com/images/f6f1003082489f35f25ba0f36b53f71a21de10d0ef89a34f0b9ea49f316daa6d.jpg](https://uploads.disquscdn.com/images/f6f1003082489f35f25ba0f36b53f71a21de10d0ef89a34f0b9ea49f316daa6d.jpg)
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8738)
    
12.  Hey Sumit. I came across the leave tracker which you had uploaded a couple of years back.. trust me it was just awesome. I am trying to create a similar tracker on google sheet. would you be able to help me with some tips?
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8488)
    
    *   Hello Ashutosh.. I don’t have a similar tracker for Google Sheets but I am working on creating one. Will soon share it with you.
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8491)
        
        *   Thank you.
            
            [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8543)
            
13.  I was unable to download the census data. Pls help me out I want to practise the work.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-3888)
    
    *   You can download the file I have provided and you will find the census data in it
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-7989)
        
        *   Dear sir,
            
            I am very much pleased to see your work in excel vba. I have worked a lot on my worksheet but at a particular stage…I have a problem that I have a list of Months from March to February…that I want to scroll down from button ………So would you help me to set a such a button and vba code to that button that should work as I want and would you send me to [bhaiswarpravin@gmail.com](mailto:bhaiswarpravin@gmail.com)
             Please sir……..
            
            [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8880)
            
14.  Thank you, Sumit. This is a big help in my reports!
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-3575)
    
    *   Thanks for commenting Jiah! Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-7990)
        
15.  Good Day Sumit, is there way I can use the scroll bar to page down sets of data. I have 200 graphs on a spreadsheet, I would like to only view six at a time.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-2358)
    
    *   You can use the scroll bar to update chart based on the data that will change in the backend.
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-7992)
        
        *   Hi Sumit – I am trying to reach you for assistance in the dashboard that you released regarding call center stats. It is an AWESOME dashboard and I am trying to figure out how to use it. Could you e-mail me [lmacdonald@idle0095.com](mailto:lmacdonald@idle0095.com)
            
            [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8341)
            
            *   Hello Lisa.. You can email me your query at [sumitbansal@trumpexcel.com](mailto:sumitbansal@trumpexcel.com)
                
                [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-8511)
                
16.  Hi Sumit, is there a way that i can add more rows to my data and the scroll bar will be able to also take in the input?
    
    For example, now i have 18 sets of data and i only want my scroll bar to have a maximum of 18 data  
    but as i add on more data, is there a way that my scroll bar can detect it?
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-1954)
    
    *   Hello Cheryl.. You would need VBA to do this. Have a look at this – [http://trumpexcel.com/2014/01/vba-tip-5-adjust-scroll-bar-maximum-scroll-value-based-on-a-cell-value/](http://trumpexcel.com/2014/01/vba-tip-5-adjust-scroll-bar-maximum-scroll-value-based-on-a-cell-value/)
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-2314)
        
17.  Can you not have more than one scroll bar on one page? I’ve put two on one page and when you scroll one, the other one scrolls too.
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-1789)
    
    *   You can have two scroll bars and it should be linked to two different cells. When you do this, the two scroll bars would be independent of each other.
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-1791)
        
18.  This is really cool. Thanks
    
    [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-1411)
    
    *   Thanks for commenting.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#comment-1790)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/create-a-scroll-bar-in-excel/#respond)

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