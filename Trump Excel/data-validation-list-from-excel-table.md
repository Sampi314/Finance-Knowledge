# Create Data Validation List from Excel Table as Source

**Source:** https://trumpexcel.com/data-validation-list-from-excel-table

---

[Skip to content](https://trumpexcel.com/data-validation-list-from-excel-table/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/data-validation-list-from-excel-table/#below-title)

A common complaint of many Excel users is that they can’t directly use Excel table’s structured references in data validation to [create drop-down lists](https://trumpexcel.com/excel-drop-down-list/)
.

If you try, Excel would give you an ugly pop-up and refuse to play along.

![](https://trumpexcel.com/wp-content/uploads/2025/03/Error-when-using-Excel-Table-as-source-for-Drop-Downs.png)

But what if you still want to (somehow) use Excel table as the source in data validation.

_There is a work around – actually three workarounds._

In this article, I will show you how to use Excel Table as a source in data validation and how to create a drop down using it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/data-validation-list-from-excel-table/#)

Using Excel Table as Source in Data Validation
----------------------------------------------

Below I have an [Excel table](https://trumpexcel.com/excel-table/)
 (named ‘Data’), and I want to create a drop-down list that shows the list of all the countries in the Regions column.

Normally, I can refer to these country names by using a structured reference as shown below:

\=Data\[Regions\]

where _Data_ in the name of the table and _Regions_ is the name of the column I am referring to.

But for some reason, Excel won’t allow me to use this structured reference in Data Validation.

So let’s see three ways to trick Excel and still use Excel Table structured reference in data validation.

Method 1: Using the INDIRECT Function
-------------------------------------

A quick and easy way to use Excel table in data validation is to put the structured reference within the INDRECT function

Here’s how you do it:

1.  Select a cell where you want the drop-down
2.  Go to the Data tab and click on the Data Validation icon

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20746%20168'%3E%3C/svg%3E)

3.  Select “List” from the Allow dropdown
4.  In the Source field, enter`:`

\=INDIRECT("Data\[Regions\]")

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

5.  Click OK

This will give you functioning drop down list in the cell you selected in step 1

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20695%20530'%3E%3C/svg%3E)

When you use [INDIRECT function](https://trumpexcel.com/excel-indirect-function/)
, instead of referring to the text “Data\[Regions\]”, it refers to what this name actually points to, which is your list of countries in the Region column.

And the best part? This is dynamic!

If you add or remove regions from your table, the drop-down list automatically updates.

This method also works across different sheets. So if your table is in one sheet and you want the drop-down in another sheet, no problem!

If you change the name of the table or the name of the column this method would break as the INDIRECT function would not know what to refer to. In case there is a possibility that you might change the name of the table or column it’s better to use the second method that uses Named Ranges

Method 2: Creating a Named Range with Structured Reference
----------------------------------------------------------

This is the most reliable method to use Excel table in data validation.

In this method we first [create a named range](https://trumpexcel.com/named-ranges-in-excel/)
 that would hold the reference to the table and then use this name range within the data validation dialog box.

Here’s is how it works:

1.  Go to the _Formulas_ tab and click on _Define Name_

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20830%20221'%3E%3C/svg%3E)

2.  In the _New Name_ dialog box, give your named range a name – let’s call it “RegionDD”
3.  In the Refers to field, just use the structured reference: =Data\[Regions\]

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

4.  Click OK

The above steps have created a Named Range that we can now use in data validation using the below steps:

1.  Go to the Data tab and click on the data validation icon
2.  Select _List_ from the _Allow_ dropdown
3.  In the Source field, enter: =RegionDD

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

4.  Click OK

This will give you a functioning drop down list that use Excel table column as the source.

Again, this method is dynamic. If you add anything to your regions list, the drop-down automatically expands. If you remove regions, the drop-down updates accordingly.

And even if you change the name of the table or the column this method would continue to work without any issues

Method 3: Direct Selection (Same Sheet Only)
--------------------------------------------

And here’s a third workaround, which probably the easiest, but it has one limitation – this would only work if your Excel Table and the drop down are in the same worksheet.

Here is how this works:

1.  Go to the Data tab and click on Data Validation icon
2.  Select _Lis_t from the _Allow_ dropdown
3.  Click in the Source field and simply select the cells in your table column

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20936%20531'%3E%3C/svg%3E)

4.  Click OK

This creates your drop-down list and it will automatically expand if you add new regions to your table.

_But there is a limitation as I mentioned?_

This only works if the Excel table and the drop-down list are in the same sheet. If they’re on different sheets, then this method won’t work as expected.

So there you have it – three ways to use table structured references in data validation drop-down lists.

I hope you found this useful! If you’re liking these Excel tips, make sure to keep an eye out for more tutorials like this one. Happy Excelling, and have a nice day!

**Other Excel articles you may also like:**

*   [Dependent Drop Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    
*   [Make a Yes/No Drop-Down in Excel](https://trumpexcel.com/make-yes-no-drop-down-excel/)
    
*   [Make Multiple Selections in a Drop Down List](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    
*   [Show Symbols in Drop Down Lists](https://trumpexcel.com/symbols-in-drop-down-lists-excel/)
    
*   [Enable Conditional Data Entry using Data Validation](https://trumpexcel.com/conditional-data-entry-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Create Data Validation List from Excel Table as Source”
----------------------------------------------------------------------

1.  Hi Sumit,
    
    I have watched quite a number of your videos and right now I am interested in adding QR codes to a spreadsheet.  
    One of your videos was one of the best and I am interested in VBA code that you mentioned in the video but I could not find the actual VBA code which was supposed to be in the description of the video.
    
    Could you provide me a way to find this VBA code as I don’t want to do a screen capture for the code?
    
    Best regards,  
    Hans Sitte
    
    [Reply](https://trumpexcel.com/data-validation-list-from-excel-table/#comment-42686)
    
    *   Hello Hans… You can get the VBA code for the QR code generator here – [https://trumpexcel.com/create-qr-codes-excel/#Using-VBA-Code-to-Generate-Custom-Function](https://trumpexcel.com/create-qr-codes-excel/#Using-VBA-Code-to-Generate-Custom-Function)
        
        [Reply](https://trumpexcel.com/data-validation-list-from-excel-table/#comment-42696)
        
2.  Thanks for your generosity in the field knowledge. I really enjoy your excel contents. Thank for educating us. God bless you.
    
    [Reply](https://trumpexcel.com/data-validation-list-from-excel-table/#comment-42683)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/data-validation-list-from-excel-table/#respond)

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