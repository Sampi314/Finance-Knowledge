# Format Numbers as Text in Drop down List in Excel

**Source:** https://trumpexcel.com/format-numbers-as-text-excel

---

[Skip to content](https://trumpexcel.com/format-numbers-as-text-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/format-numbers-as-text-excel/#below-title)

A few days ago, I was working on [creating an Excel dashboard](https://trumpexcel.com/creating-excel-dashboard/)
.

I had to create a number of drop downs with the options ranging from 1 to 5. To make it more user-friendly, I also wanted to give an option of ‘Not Selected’, when a user does not want to make a selection in the [drop down list in excel](https://trumpexcel.com/excel-drop-down-list/)
.

Something as shown below in the pic:

![Format Numbers as Text - Drop Down List in Excel - Not Selected](https://trumpexcel.com/wp-content/uploads/2013/09/Not-Selected-in-Formula-Bar.gif)

The problem here is that when I  choose ‘Not Selected’ from the drop down, it returns the text _Not Selected_ (see in the formula bar in the pic above). Since I have to use this selection in some formulas, I want this to return a 0.

Now there are 2 ways to format numbers as text using Number Custom Formatting. 

Method 1: Format Numbers as Text in Drop Down List in Excel
-----------------------------------------------------------

You can format numbers as text in the drop down list in Excel in such a way, that it shows text in the drop down, but when selected, gets stored as a number in the cell.

Here are the steps to do this:

1.  In a cell type 0 (this is the cell that you want to be displayed as ‘Not Selected’).
2.  With the cell selected, press Control + 1 (this opens the Format Cells dialogue box).
3.  Select the Number tab and go to Custom option.
4.  In Custom, type “Not Selected” as shown in the pic.

![Format Numbers as Text Drop Down List in Excel - Custom Format Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20488%20434'%3E%3C/svg%3E)

1.  That’s it!! Now you will have a cell that has **_Not Selected_** in it, but in the formula bar displays a **0**. When I use this in creating a drop down list, a user can select the option ‘Not Selected’ and this would return 0 (as shown below in the pic).

![Format Numbers as Text Drop Down List in Excel - Not Selected Returns Zero](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20294%20233'%3E%3C/svg%3E)

Also read: [Convert Text to Number in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)

Method 2 – Format Number as Text in the Cell in Excel
-----------------------------------------------------

While the above trick works fine, in terms of creating dashboards, it makes more sense to display ‘Not Selected’ in the drop down menu as well as in the cell (when it is selected), instead of a 0 (as shown in the pic below; notice the value in formula bar). This makes it easier for someone else to pick-up the spreadsheet and works on it.

![Format Numbers as Text Drop Down List in Excel - Not Selected Returns Text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20326%20255'%3E%3C/svg%3E)

Again, this can be done very easily using custom formats.

Here are 2 quick ways to do this:

1.  Select the cell that has the drop down validation list and press **Control + 1** (This opens the Format Cells dialogue box).
2.  Select the Number tab and go to Custom option.
3.  Type \[\=0\]”Not Selected” OR Type 0;0;”Not Selected”.
4.  Click OK.

**How it works**

Custom Number Formatting has for components (separated by semi-colon):

<_Positive Numbers> ; <Negative Numbers> ; <Zero> ; <Text>_

These four parts can be formatted separately to give the desired format.

For example, in the case above, we wanted to display 0 as Not Selected. In the number formatting sequence, 0 is the third part of the format, so we changed the sequence to 0;0;”Not Selected”.

This means that positive and negative numbers are displayed as it is, and whenever there is a zero, it is displayed as _**Not Selected.**_

The other way is to give a condition to number format  \[=0\]”Not Selected”. This display _**Not Selected**_ whenever the value in a cell is 0, else it will use the General formatting settings.

Here are a couple of good sources to learn more about Custom Number Formatting:

*   _[Office Help](http://office.microsoft.com/en-001/excel-help/create-a-custom-number-format-HP010342372.aspx)
    _
*   _[Ozgrid](http://www.ozgrid.com/Excel/excel-custom-number-formats.htm)
    _
*   [Six Things Custom Number Formatting can do for you](https://trumpexcel.com/excel-custom-number-formatting/)
    .

**Related Tutorials:**

*   [Creating a Dependent Drop Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    .
*   [Creating a Drop Down List with Search Suggestion Functionality](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [Creating Multiple Drop Down List without Repetition](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    .
*   [Format Numbers in Millions in Excel](https://trumpexcel.com/millions-format-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Format Numbers as Text in a Drop Down List in Excel”
------------------------------------------------------------------

1.  What if I want my drop down to show only text, but represent numbers, for example: (drop down shows) always, sometimes, never. Numeric value is 3, 2, 1 (respectively). But I would like it to display always, sometimes, never….but I want to quantify it with an average score at the end. Is there a way to do that using your awesome simple method?
    
    [Reply](https://trumpexcel.com/format-numbers-as-text-excel/#comment-2475)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/format-numbers-as-text-excel/#respond)

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