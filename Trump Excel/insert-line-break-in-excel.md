# How to Insert Line Break in Excel (Quick and Easy)

**Source:** https://trumpexcel.com/insert-line-break-in-excel

---

[Skip to content](https://trumpexcel.com/insert-line-break-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/insert-line-break-in-excel/#below-title)

A line break in Excel can be used to end the current line and start a new line in the same cell (as shown below).

![Insert Line Break in Excel Formula](https://trumpexcel.com/wp-content/uploads/2014/02/Line-Break-in-Excel1.png)

Notice that in the pic above, Morning is in the second row in the same cell.

You may want to insert a line break in Excel when you have multiple parts of a text string that you want to show in separate lines. A good example of this could be when you have an address and you want to show each part of the address in a separate line (as shown below).

![Line break in address](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20269%20250'%3E%3C/svg%3E)

In this tutorial, I will show you a couple of ways to insert a line break in Excel (also called the **in-cell carriage return in Excel**)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/insert-line-break-in-excel/#)

Inserting a Line Break Using a Keyboard Shortcut
------------------------------------------------

If you only need to add a couple of line breaks, you can do this manually by using a keyboard shortcut.

Here is how to insert a line break using a keyboard shortcut:

*   Double-click on the cell in which you want to insert the line break (or press F2). This will get you into the [edit mode in the cell](https://trumpexcel.com/edit-cells-excel/)
    
*   Place the cursor where you want the line break.
*   Use the keyboard shortcut – ALT + ENTER (hold the ALT key and then press Enter).

The above steps would insert a line break right where you had placed the cursor. Now you can continue to write in the cell and whatever you type will be placed in the next line.

Note that you need the cell to be in the ‘Wrap text’ mode to see the content appear in the next line. In case it’s is not applied, you will see all the text in a single cell (even if you have the line break). ‘Wrap Text’ option is available in the Home tab in the ribbon.

The keyboard shortcut is a quick way to add a line break if you only have to do this for a few cells. But if you have to do this a lot of cells, you can use the other methods covered later in this tutorial.

Inserting Line Breaks Using Formulas
------------------------------------

You can add a line break as a part of the formula result.

This can be useful when you have different cells that you want to combine and add a line break so that each part is in a different line.

Below is an example where I have used a formula to combined different parts of an address and have added a line break in each part.

![Add Line break using a formula to combine address](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20745%20410'%3E%3C/svg%3E)

Below is the formula that adds a line break within the formula result:

\=A2&CHAR(10)&B2&(CHAR(10)&C2)

The above formula uses CHAR(10) to add the line break as a part of the result. CHAR(10) uses the ASCII code which returns a line feed. By placing the line feed where you want the line break, we are forcing the formula to break the line in the formula result.

You can also use the CONCAT formula instead of using the ampersand (&) symbol:

\=CONCAT(A2,CHAR(10),B2,CHAR(10),C2)

or the old CONCATENATE formula in case you’re using older versions of Excel and don’t have CONCAT

\=CONCATENATE(A2,CHAR(10),B2,CHAR(10),C2)

And in case you are using Excel 2016 or prior versions, you can use the below TEXTJOIN formula (which is a better way to join cells/ranges)

\=TEXTJOIN(CHAR(10),TRUE,A2:C2)

Note that in order to get the line break visible in the cell, you need to make sure that ‘Wrap Text’ is enabled. If the [Wrap Text](https://trumpexcel.com/wrap-text/)
 is NOT applied, adding Char(10) would make no changes in the formula result.

_Note: If you are using Mac, use Char(13) instead of Char(10)._

### Using Define Name Instead of Char(10)

If you need to use Char(10) or Char(13) often, a better way would be to assign a name to it by creating a defined name. This way, you can use a shortcode instead of typing the entire CHAR(10) in the formula.

Below are the steps to create a named range for CHAR(10)

*   Click the Formulas tab
*   Click on the ‘Define Name’ option.![Insert Line Break in Excel Formula - Defined Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20485%20141'%3E%3C/svg%3E)
*   In the New Name dialogue box, enter the following details:
    *   Name: LB (you can name it whatever you want – without spaces)
    *   Scope: Workbook
    *   Refers to: =CHAR10)![Insert Line Break in Excel Formula - Defined Name Details](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20309%20241'%3E%3C/svg%3E)
*   Click OK.

Now you can use LB instead of =CHAR(10).

So the formula to combine address can now be:

\=A2&LB&B2&LB&C2

_Also read: [Start New Line In Excel Cell](https://trumpexcel.com/start-a-new-line-in-excel-cell/)
_

Using Find and Replace (the CONTROL J Trick)
--------------------------------------------

This is a super cool trick!

Suppose you have a dataset as shown below and you want to get a line break wherever there is a comma in the address.

![Address where comma needs to be replaced by a line break](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20478%20197'%3E%3C/svg%3E)

If you want to insert a line break wherever there is a comma in the address, you can do that using the FIND and REPLACE dialog box.

Below are the steps to replace the comma with a line break:

1.  Select the cells in which you want to replace the comma with a line break
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20382%20199'%3E%3C/svg%3E)
3.  In the Editing group, click on Find and Select and then click on Replace (you can also use the keyboard shortcut Control + H). This will open the Find and Replace dialog box.![Click on Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20281%20436'%3E%3C/svg%3E)
4.  In the Find and Replace dialog box, enter comma (,) in the Find What field.![Enter comma in Find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
5.  Place the cursor in the Replace Field and then use the keyboard shortcut – CONTROL + J (hold the Control key and then press J). This will insert the line feed in the field. You may be able to see a blinking dot in the field after you use Control + J![Use Control J in the Replace with field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
6.  Click on Replace ALL.![Click on Replace all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20250'%3E%3C/svg%3E)
7.  Make sure Wrap text is enabled.

The above steps [remove the comma](https://trumpexcel.com/remove-comma-excel/)
 and replace it with the line feed.

Note that if you use the keyboard shortcut Control J twice, this will insert the line feed (carriage return) two times and you will have a gap of two lines in between sentences.

You can also use the same steps if you want to [remove all the line breaks](https://trumpexcel.com/remove-line-break-excel/)
 and replace it will a comma (or any other character). Just reverse the ‘Find What’ and ‘Replace with’ entries.

**You may also like the following Excel tutorials:**

*   [Insert a watermark in Excel](https://trumpexcel.com/insert-watermark-in-excel/)
    .
*   [Excel AUTOFIT: Make Rows/Columns Fit the Text Automatically](https://trumpexcel.com/autofit-excel/)
    
*   [Insert Picture in an Excel Cell](https://trumpexcel.com/insert-picture-into-excel-cell/)
    .
*   [Add Bullet Points In Excel](https://trumpexcel.com/bullet-points/)
    
*   [Insert a Check Mark Symbol in Excel](https://trumpexcel.com/check-mark/)
    
*   [200+ Excel Keyboard Shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
    .
*   [How to Create Named Ranges in Excel](https://trumpexcel.com/named-ranges-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

2 thoughts on “How to Insert Line Break in Excel (Quick and Easy)”
------------------------------------------------------------------

1.  In my spreadsheet, in A column there are 5 rows of data, a space in the 6th row& 7th row, again data starts from 8th row until 15th row, then space in 16th row, again data starts from 17th row. I want each of this to be transposed to columns, the first data line after the space, should be transposed to column. Please let me know how do I achieve this.
    
    [Reply](https://trumpexcel.com/insert-line-break-in-excel/#comment-14381)
    
2.  Thanks! Control + J option helped me.
    
    [Reply](https://trumpexcel.com/insert-line-break-in-excel/#comment-14015)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/insert-line-break-in-excel/#respond)

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