# How to Create Dynamic Hyperlinks in Excel

**Source:** https://trumpexcel.com/create-dynamic-hyperlinks-in-excel

---

[Skip to content](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#below-title)

Hyperlinks are Excel’s shortcut way to jump to the required data point in the same workbook, a different workbook, or an external URL.

While [hyperlinks](https://trumpexcel.com/hyperlinks/)
 are mostly static links, here is the way you can use to create dynamic hyperlinks.

By Dynamic Hyperlinks, I mean links that change based on the selection (or any other user action)

Suppose I have the data set as shown below:

![Dynamic Hyperlinks in Excel Data Set](https://trumpexcel.com/wp-content/uploads/2014/03/Dynamic-Hyperlink-Excel-Data-Set.png)

This is the back-end data, and I have a summary sheet where I have drop-downs where the person can select the Month. The idea is to update the hyperlink with the selections so that it takes the user to the right cell when the hyperlink is clicked.

Something as shown below

![Dynamic Hyperlinks in Excel Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20480'%3E%3C/svg%3E)

Here to Create Dynamic Hyperlinks in Excel
------------------------------------------

1.  Create a data validation drop-down in Cell B3, with the source as the name of all months in the Data tab [_\[Learn how to create a drop down list in Excel\]_](https://trumpexcel.com/excel-drop-down-list/ "Learn all about Data Validation in Excel")
    
2.  Use the following formula in cell C3

\=HYPERLINK("#"&"Data!B"&(MATCH(B3,Data!$B$3:$B$26,0)+2),"Click Here to See Data")

1.  That’s it!! Your Dynamic Hyperlink is Ready

**How this works**

*   **#** tells the formula to refer to the same workbook
*   Data!B is the reference of [sheet name](https://trumpexcel.com/get-sheet-name-excel/)
     and column name
*   [MATCH](https://trumpexcel.com/excel-match-function/)
    (B3,Data!$B$3:$B$26,0) gives the position of the matching month in the list. 2 is added to it as there are 2 data beginning from the third row. For example, in the case of January 2012, the Match formula returns 1, and adding two returns 3. Hence it refers to B3

This is an amazing trick that can come very handy in creating [Excel dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

_**Try it Yourself.. Download the file from here  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/10/Dynamic-Hyperlink-in-Excel.xlsx)
  
**_

**You May Also Like the Following Excel Tutorials:**

*   [How to Quickly Find Hyperlinks in Excel (using Find and Replace)](https://trumpexcel.com/find-hyperlinks-in-excel/)
    .
*   [How to Quickly Remove Hyperlinks from a Worksheet in Excel](https://trumpexcel.com/remove-hyperlinks/)
    .
*   [Quickly Create Summary Worksheet with Hyperlinks in Excel](https://trumpexcel.com/create-summary-worksheet-in-excel/)
    .
*   [Excel INDIRECT Function](https://trumpexcel.com/excel-indirect-function/)
    
*   [Extract URL from Hyperlinks in Excel](https://trumpexcel.com/extract-url-from-hyperlinks-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Create Dynamic Hyperlinks in Excel”
--------------------------------------------------

1.  I have a unique need for a dynamic hyperlink but not related to text that you can match. I want to be able to enter R1C1 Coordinates in a cell and hyperlink to that cell within the same worksheet. I don’t believe it can be done with the standard hyperlink because the coordinates will vary, I think this needs to be created as a macro and assigned a button or some other form. Can you assist?
    
    [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-14056)
    
2.  If we have excel in one folder with all linked files how we can move the folder to another place? When I do it I lost all links
    
    [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-13315)
    
3.  Wow thanks, I didn’t know the HYPERLINK formula existed. The way it is used is almost exactly like an INDIRECT formula. I have now used it to link multiple different sheets with a formula rather than tediously linking to each sheet:
    
    \=HYPERLINK(“#'”&$A4&”‘!A1″,”→”)
    
    Gives an arrow that when clicked takes you to cell A1 of the sheet named in A4… brilliant!
    
    [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-11385)
    
    *   Hi David, this is so close to what i search for. I want to do this. In a cell i use some functions and the result i got is “A22” . I need to build a Hyperlink to get me to Cell A22 in another sheet…
        
        [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-13691)
        
4.  Thank you for this excellent tutorial! Your explanation made it easy for me to modify your formula for a very similar task.
    
    [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-11184)
    
5.  I have removed the “#” in the formula and it did not work.  
    Also, you said <> , If we want to refer some other workbook ?
    
    Can you explain it in detail ?
    
    [Reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#comment-2113)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/#respond)

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