# Search and Highlight Data in Excel (with Conditional Formatting)

**Source:** https://trumpexcel.com/search-highlight-using-conditional-formatting

---

[Skip to content](https://trumpexcel.com/search-highlight-using-conditional-formatting/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/search-highlight-using-conditional-formatting/#below-title)

**Watch Video – Search and Highlight Data Using Conditional Formatting**

If you work with large datasets, there can be a need to create a search functionality that allows you to quickly highlight cells/rows for the searched term.

While there is no direct way to do this in Excel, you can create search functionality using [Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

For example, suppose you have a dataset as shown below (in the image). It has columns for Product Name, Sales Rep, and Country.

Now you can use conditional formatting to search for a keyword (by entering it in cell C2) and highlight all the cells that have that keyword.

Something as shown below (where I enter the item name in cell B2 and press Enter, the entire row gets highlighted):

![Search and Highlight Data in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20496'%3E%3C/svg%3E)

In this tutorial, I will show you how to create this search and highlight functionality in Excel.

Later in the tutorial, we will go a bit advanced and see how to make it dynamic (so that it highlights while you’re typing in the search box).

[**Click here to download the example file**](https://www.dropbox.com/s/g9ffg6bmbye0tul/Search%20And%20Highlight.xlsx?dl=0)
 and follow along.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/search-highlight-using-conditional-formatting/#)

Search and Highlight Matching Cells
-----------------------------------

In this section. I will show you how to search and highlight only the matching cells in a dataset.

Something as shown below:

![Search and Highlight Matching cells only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20482'%3E%3C/svg%3E)

Here are the steps to search and highlight all the cells that have the matching text:

1.  Select the dataset on which you want to apply Conditional Formatting (A4:F19 in this example).
2.  Click the Home tab.![Home Tab in the Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20316%20192'%3E%3C/svg%3E)
3.  In the Styles group, click on Conditional Formatting.
4.  In the drop-down options, click on New Rule._  
    ![Search and Highlight Data Using Conditional Formatting - New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20455%20404'%3E%3C/svg%3E)_
5.  In the ‘New Formatting Rule’ dialog box, click on the option ‘Use a formula to determine which cells to format’.![New Formatting Rule dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
6.  Enter the following formula: **\=A4=$B$1![Search and Highlight Matching cells - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click on ‘Format..’ button.![Format to highlight the searched cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
8.  Specify the formatting (to highlight cells that match the searched keyword).![Specifying the Color to Highlight searched cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20480'%3E%3C/svg%3E)
9.  Click OK.

Now type anything in cell B1 and press enter. It will highlight the matching cells in the dataset that contain the keyword in B1.

![Search and Highlight Matching cells only](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20482'%3E%3C/svg%3E)

**How does this work?**

Conditional Formatting gets applied whenever the formula specified in it returns TRUE.

In the above example, we check each cell using the formula **\=A4=$B$1**

Conditional Formatting checks each cell and verifies it the content in the cell is the same as that in cell B1. If it’s the same, the formula returns TRUE and the cell gets highlighted. If it isn’t the same, the formula returns FALSE and nothing happens.

[**Click here to download the example file**](https://www.dropbox.com/s/g9ffg6bmbye0tul/Search%20And%20Highlight.xlsx?dl=0)
 and follow along.

Search and Highlight Rows with Matching Data
--------------------------------------------

If you want to highlight the entire row instead of just the matching cells, you can do that by tweaking the formula a little.

Below is an example where the entire row gets highlighted if the product type matches the one in cell B1.

![Search and Highlight entire row - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20484'%3E%3C/svg%3E)

Here are the steps to search and highlight the entire row:

1.  Select the dataset on which you want to apply Conditional Formatting (A4:F19 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  In the drop-down options, click on New Rule.
5.  In the ‘New Formatting Rule’ dialog box, click on the option ‘Use a formula to determine which cells to format’.
6.  Enter the following formula: **\=$B4=$B$1![Search and Highlight entire row - formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click on ‘Format..’ button.
8.  Specify the formatting (to highlight cells that match the searched keyword).
9.  Click OK.

The above steps would search for the specified item in the dataset, and if it finds the matching item, it will highlight the entire row.

Note that this will only check for the item column. If you enter a Sales Rep name here, it will not work. If you want it to work for Sales Rep name, you need to change the formula to **\=$C4=$B$1**

Note: The reason it highlights the entire row and not just the matching cell is that we have used a $ sign before the column reference ($B4). Now when conditional formatting analyzes cells in a row, it checks whether the value in column B of that row is equal to the value in cell B1. So even when it’s analyzing A4 or B4 or C4 and so on, it’s checking for B4 value only (as we have locked column B by using the dollar sign).

You can read more about [absolute, relative and mixed references here](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
.

Search and Highlight Rows (based on Partial Match)
--------------------------------------------------

In some cases, you may want to highlight rows based on a partial match.

For example, if you have items such as White Board, Green Board, and Gray Board, and you want to highlight all these based on the word Board, then you can do this using the [SEARCH function](https://trumpexcel.com/excel-search-function/)
.

Something as shown below:

![Search and Highlight partial data - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20485'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the dataset on which you want to apply Conditional Formatting (A4:F19 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  In the drop-down options, click on New Rule.
5.  In the ‘New Formatting Rule’ dialog box, click on the option ‘Use a formula to determine which cells to format’.
6.  Enter the following formula: **\=AND($B$1<>””,ISNUMBER(SEARCH($B$1,$B4)))![Formula to search for partial matches](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click on ‘Format..’ button.
8.  Specify the formatting (to highlight cells that match the searched keyword).
9.  Click OK.

**How does this work?**

*   [SEARCH](https://trumpexcel.com/excel-search-function/)
     function looks for the search string/keyword in all the cells in a row. It returns an error if the search keyword is not found, and returns a number if it finds a match.
*   [ISNUMBER](https://trumpexcel.com/excel-is-function/)
     function converts the error into FALSE and the numeric values into TRUE.
*   [AND](https://trumpexcel.com/excel-and-function/)
     function checks for an additional condition – that cell C2 should not be empty.

So now, whenever you type a keyword in cell B1 and press Enter, it highlights all the rows that have the cells that contain that keyword.

**Bonus Tip:** If you want to make the search case sensitive, use the [FIND Function](https://trumpexcel.com/excel-find-function/)
 instead of SEARCH.

[**Click here to download the example file**](https://www.dropbox.com/s/g9ffg6bmbye0tul/Search%20And%20Highlight.xlsx?dl=0)
 and follow along.

Dynamic Search and Highlight Functionality (Highlights as you type)
-------------------------------------------------------------------

Using the same Conditional Formatting tricks covered above, you can also take it a step further and make it dynamic.

For example, you can create a search bar where the matching data gets highlighted as you’re typing in the search bar.

Something as shown below:

![Dynamic Search and Highlight in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20496'%3E%3C/svg%3E)

This can be done using ActiveX controls and can be a good functionality to use when [creating reports or dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

Below is a video where I show how to create this:

Did you find this tutorial useful? Let me know your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Dynamic Excel Filter – Extracts Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Create a drop-down list with search suggestion](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Creating a Heat Map in Excel](https://trumpexcel.com/heat-map-excel/)
    .
*   [Highlight Rows Based on a Cell Value in Excel](https://trumpexcel.com/highlight-rows-based-on-cell-value/)
    .
*   [Highlight the Active Row and Column in a Data Range in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    .
*   [How to Highlight Blank Cells in Excel.](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

21 thoughts on “Search and Highlight Data Using Conditional Formatting”
-----------------------------------------------------------------------

1.  I am trying to do this exact thing but with one added step and I have no idea how. I want to scan into the search box and have the corresponding cell’s column highlighted and remain highlighted until I have completed all scans. After that I want to simply clear the highlight formats and have the original spreadsheet remaining to do it all over again. I am making a really really low key inventory tracking and reordering system that anyone can use. Is this even possible??
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-14888)
    
2.  Sheet1 column A:A some cells have numbers(suppose 100 numbers).  
    Sheet2 column A, B C & D having a few numbers (suppose 50 numbers) those exactly match/equal with sheet1numbers.  
    Now want to highlight cells or rows of sheet1 on the basis of numbers of sheet2.  
    Tnx to all ecperts in advance.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-14451)
    
3.  Wrong explanation.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-14361)
    
4.  good lesson
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-13259)
    
5.  hi! i need help for excel
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-12238)
    
6.  This formula  
    \=AND($B$1″”,ISNUMBER(SEARCH($B$1,$B4)))  
    from Search and Highlight Rows (based on Partial Match)  
    is wrong…  
    There is a problem with this formular, is all excel have to say about this
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-12183)
    
    *   Nevermind, replaced , through ; and is now working
        
        [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-12184)
        
        *   I cant get this formula to work. What did you replace=AND($B$1″”,ISNUMBER(SEARCH($B$1,$B4)))
            
            [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-13186)
            
7.  Is there a way to have the highlighted data from search filter to top of dataset? I have a large spreadsheet and have to scroll all the way down to see highlighted rows.  
    Thanks
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-11728)
    
8.  HI  
    I cant get the formula to work. Excel wont recognize it.  
    I translated to danish.
    
    problem seems to be “”,ELLER
    
    any solution?
    
    \=OG($C$2″”,ELLER(ER.TAL(SØG($c$2,$A7:H7,1))))
    
    would apreciate it very much
    
    Nitram
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-11395)
    
9.  Sorry men. I do not why, in my case, it does not work. In the bets of the scenarios, it highlight like two cells that they do not have anything to do.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-10391)
    
10.  Thank you Sumit.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-9393)
    
11.  Hello, Why don’t =AND($C$2″”, OR(ISNUMBER(SEARCH($C$2, $B5)))) works?Coz I tried that formula so that even if I just input a string or a keyword, it will highlight that particular word, not the entire row. That formula works but if only I try to input the product, but if i try to input the name and geography it wont work.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-9276)
    
12.  Hi Sumit,  
    I find Search and Highlight Cells using Conditional Formatting very useful however I tried every other possibility to but doesn’t highlight any data. Same applies with Gantt chart as well I could not format the date schedule. I am using Microsoft office 2007. Hope you can help me out.
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-2516)
    
    *   Hi , I can’t see the necessity here for OR either, i used =SEARCH(input;$B16&$C16&$D16&$E16&$F16) , where $B16 &…. your range for row to be highlited and “input” the name of the cell that searches, also make sure you select the area you want with Shift+Ctrl before you go to Conditional formating, hope it works for you.
        
        [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-4031)
        
13.  I didn’t understand why we have used OR functions here –
    
    \=AND($C$2″”,OR($C$2=$B5:$D5))
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1685)
    
    *   OR formula would highlight the entire row. The first formula showcases how you can highlight matching cells only (in the countries column). I have used the OR formula in the second tab (in the download file), where the intent is to highlight the entire row.
        
        [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1686)
        
        *   I understand OR is to highlight the entire row but I did not understand the logic. I mean without OR why it is not working ? -> =AND($C$2″”,$C$2=$B5:$D5)
            
            [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1687)
            
            *   It doesn’t work without OR as $C$2=$B5:$D5 does not return a single TRUE or FALSE. Rather it returns an array of True/False. If you do not use OR, there would always be FALSE in the array, and hence AND would always return FALSE.
                
                [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1688)
                
14.  I have a doubt, why C2 is not equal to D5, I mean –> =AND($C$2″”,$C$2=D5) but instead you used =AND($C$2″”,$C$2=B5) which works here.
    
    Can you please explain ?
    
    [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1681)
    
    *   Hello Deepak.. when we select the entire range (B5:D22) in this case, the formula is applied keeping the active cell in mind. And conditional formatting evaluates each cell based on it. For example, when it is evaluating cell B5, it used the formula =AND($C$2″”,$C$2=B5). When it moves to cell C5, it evaluates it with the formula =AND($C$2″”,$C$2=C5)
        
        [Reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#comment-1684)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/search-highlight-using-conditional-formatting/#respond)

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