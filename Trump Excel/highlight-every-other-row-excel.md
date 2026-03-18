# Highlight EVERY Other ROW in Excel (using Conditional Formatting)

**Source:** https://trumpexcel.com/highlight-every-other-row-excel

---

[Skip to content](https://trumpexcel.com/highlight-every-other-row-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-every-other-row-excel/#below-title)

**Watch Video – How to Highlight Alternate (Every Other Row) in Excel**

Below is the complete written tutorial, in case you prefer reading over watching a video.

[Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 in Excel can be a great ally in while working with spreadsheets.

A trick as simple as the one to highlight every other row in Excel could immensely increase the readability of your data set.

And it is as EASY as PIE.

Suppose you have a dataset as shown below:![Highlight Every Other Row in Excel using Conditional Formatting - Select Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20389%20290'%3E%3C/svg%3E)

Let’s say you want to highlight every second month (i.e., February, April and so on) in this data set.

This can easily be achieved using conditional formatting.

Highlight Every Other Row in Excel
----------------------------------

Here are the steps to highlight every alternate row in Excel:

1.  Select the data set (B4:D15 in this case).![Highlight Every Other Row in Excel using Conditional Formatting - Seelct Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20389%20290'%3E%3C/svg%3E)
2.  Open the Conditional Formatting dialogue box (Home–> Conditional Formatting–> New Rule) \[_Keyboard Shortcut – Alt + O + D_\].![Highlight Every other Row in Excel using Conditional Formatting - New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20578%20280'%3E%3C/svg%3E)
3.  In the dialogue box, click on “_Use a Formula to determine which cells to format_” option.![Highlight Every other Row in Excel using Conditional Formatting - Use a fromula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20370'%3E%3C/svg%3E)
4.  In Edit the Rule Description section, enter the following formula in the field:  
    \=[MOD](https://trumpexcel.com/excel-mod-function/)
    ([ROW](https://trumpexcel.com/excel-row-function/)
    (),2)=1![Highlight Every other Row in Excel using Conditional Formatting - MOD Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20372'%3E%3C/svg%3E)

1.  Click on the Format button to set the formatting.![Highlight Every Nth Row in Excel using Conditional Formatting - Set Format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20683%20341'%3E%3C/svg%3E)
2.  Click OK.![Highlight Every other Row in Excel using Conditional Formatting - Click OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20372'%3E%3C/svg%3E)

That’s it!! You have the alternate rows highlighted.![Highlight Every other Row in Excel using Conditional Formatting - highlighted data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20290'%3E%3C/svg%3E)

**How does it Work?**

Now let’s take a step back and understand how this thing works.

The entire magic is in the formula \=MOD(ROW(),2)=1. _\[MOD formula returns the remainder when the ROW number is divided by 2\]._

This evaluates each cell and checks if it meets the criteria. So it first checks B4. Since the ROW function in B4 would return 4, =MOD(4,2) returns 0, which does not meet our specified criteria.

So it moves on to the other cell in next row.

Here Row number of cell B5 is 5 and =MOD(5,1) returns 1, which meets the condition. Hence, it highlights this entire row (since all the cells in this row have the same row number).

You can change the formula according to your requirements. Here are a few examples:

*   _Highlight every 2nd row starting from the first row \=MOD(ROW(),2)=0_
*   _Highlight every 3rd Row \=MOD([ROW](https://trumpexcel.com/excel-row-function/)
    (),3)=1_
*   Highlight every 2nd column \=_MOD([COLUMN](https://trumpexcel.com/excel-column-function/)
    (),2)=0_

These banded rows are also called zebra lines and are quite helpful in increasing the readability of the data set.

If you plan to print this, make sure you use a light shade to highlight the rows so that it is readable.

**Bonus Tip:** Another quick way to highlight alternate rows in Excel is to convert the data range into an [Excel Table](https://trumpexcel.com/excel-table/)
. As a part of the Excl Table formatting, you can easily highlight alternate rows in Excel (all you need is to use the check the Banded Rows option as shown below):

![Highlight Altenate Rows in Excel - Banded Rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20369%20145'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [Creating a Heat Map in Excel](https://trumpexcel.com/heat-map-excel/)
    .
*   [How to Apply Conditional Formatting in a Pivot Table in Excel](https://trumpexcel.com/apply-conditional-formatting-pivot-table-excel/)
    .
*   [Conditional Formatting to Create 100% Stacked Bar Chart in Excel](https://trumpexcel.com/stacked-bar-chart-in-excel/)
    .
*   [How to Insert Multiple Rows in Excel](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    .
*   [How to Count Colored Cells in Excel.](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [How to Highlight Blank Cells in Excel.](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [7 Quick & Easy Ways to Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
    .
*   [How to Compare Two Columns in Excel.](https://trumpexcel.com/compare-two-columns/)
    
*   [Insert a Blank Row after Every Row in Excel (or Every Nth Row)](https://trumpexcel.com/insert-blank-row-after-every-row/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    
*   [Select Every Other Row in Excel](https://trumpexcel.com/select-every-other-row-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

32 thoughts on “Highlight EVERY Other ROW in Excel (using Conditional Formatting)”
----------------------------------------------------------------------------------

1.  You just saved me days of work in a matter of seconds, THANK YOU SO MUCH
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-16020)
    
2.  Hi there, thank you your site is very helpful. I work with spreadsheets daily and I like to make my data to be easier on the eyes. Is there a modified formula to =MOD(ROW(),2)=0 so that the 1st row is blank and the shading begins on the 2nd row? Please let me know. THANKS!!!
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-13701)
    
3.  Sir, 19th March,2020.  
    I appreciate your efforts to explain deeply each and every lesson.  
    Generally,what I observed tell you, no one cares to go deeply.  
    I hope,like me others may have also impressed while reading those articles.  
    Once again thanking you and hope to receive more and more articles from you in future too.  
    Kanahaiyalal Newaskar.
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-13545)
    
4.  If I understand correctly, this is a typo: “Here Row number of cell B5 is 5 and =MOD(5,1) returns 1”; Should this not be “… =MOD(5,2) returns 1”?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-12079)
    
5.  Thank you for the site. It is one of the best site I found which caters to a novice to expert Excel user with simple and detailed step by step instructions with examples.  
    I will definitely recommend it to colleagues and friends.
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-11755)
    
6.  How do i find % differences between numbers in two columbs?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-11443)
    
7.  Sir can you suggest / create any a default function in excel which will highlight row & column for every excel workbook by default without any application.
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-10579)
    
8.  This was really helpful. Thank you for sharing.
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-3886)
    
9.  this is what I used to do it years ago…
    
    …but then I discovered Tables  
    and have never done this again
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-3614)
    
10.  HOW TO HIGHLIGHT THE CELL IF IT HOLD A SPECIFIC CHARACTER
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-3606)
    
11.  HOW TO HIGHLIGHT THE CELL OF Nth CAHARACTER
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-3605)
    
12.  Very Helpful. Thank you for sharing and answering all the questions. This really helped me.
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2574)
    
13.  How would you highlight every 10th row, starting from 2?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2474)
    
14.  is there a formula for 4 rows highlighted, 4 rows not highlighted, and so on?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2298)
    
    *   Try this formula:
        
        \=ISODD(ROUNDUP(ROW()/4,0))
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2300)
        
        *   Awesome thank you! I was just looking for this too 🙂
            
            [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2501)
            
15.  Hi there, how do I highlight/shade/flag every 5th cell along a single row, and only the cells that contain a ‘1’. I have only found formulas highlighting every nth row down a column, and no examples for along a row. Can you help me?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2297)
    
    *   Try this formula:
        
        \=AND((A$1=1),MOD(COLUMN(A$1),5)=0)
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2299)
        
16.  How would I do this to highlight every 24th cell -1 (because I don’t want the header accounted for)
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2236)
    
    *   Hello Debra.. Do you want to highlight every 23rd row? If yes, you can use this formula =MOD(ROW(),23)=0
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-2237)
        
17.  Very helpful, thank you so much!
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1990)
    
    *   Thanks for commenting. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1993)
        
18.  Awesome. Thanks!
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1947)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1992)
        
19.  how do you highlight every 15th cell in column H for the SUM mathematical function
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1938)
    
    *   Thanks for commenting.. To highlight every 15th cell in column H, select the entire column and use the following formula in conditional formatting
        
        \=Mod(row($H1),15)=0
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1939)
        
        *   thank you. i forgot to add the range from 712-4430
            
            [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1940)
            
            *   when i paste the formula it tell me it is false
                
                [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1941)
                
                *   I guess you are pasting the formula in the worksheet. Instead, you need to paste the formula in the conditional formatting box as shown in the article.
                    
                *   oh ok. thank you. and the range 712-4430
                    
20.  How do I get this to only highlight cells every fourth row that are great than 1 but less than 99999?
    
    [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1936)
    
    *   Hello Brandy.. Thanks for commenting. To do this select all the cells and use the following formula in conditional formatting
        
        \=AND(MOD(ROW(A1),4)=0,A1>0,A1<9999)
        
        [Reply](https://trumpexcel.com/highlight-every-other-row-excel/#comment-1937)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-every-other-row-excel/#respond)

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