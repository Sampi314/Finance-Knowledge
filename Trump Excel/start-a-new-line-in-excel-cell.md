# How to Start a NEW LINE in Excel Cell (Windows and Mac)

**Source:** https://trumpexcel.com/start-a-new-line-in-excel-cell

---

[Skip to content](https://trumpexcel.com/start-a-new-line-in-excel-cell/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/start-a-new-line-in-excel-cell/#below-title)

**Watch Video – Start a New Line in a Cell in Excel (Shortcut + Formula)**

In this Excel tutorial, I will show you how to start a new line in an Excel cell.

You can start a new line in the same cell in Excel by using:

*   A keyboard shortcut to manually force a line break.
*   A formula to automatically enter a line break and force part of the text to start a new line in the same cell.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/start-a-new-line-in-excel-cell/#)

Start a New Line in Excel Cell – Keyboard Shortcut
--------------------------------------------------

To start a new line in an Excel cell, you can use the following keyboard shortcut:

*   For Windows – ALT + Enter.
*   For Mac – Control + Option + Enter.

Here are the steps to start a new line in Excel Cell using the shortcut ALT + ENTER:

1.  Double click on the cell where you want to insert the line break (or press F2 key to get into the edit mode).
2.  Place the cursor where you want to insert the line break.
3.  Hold the ALT key and press the Enter key for Windows (for Mac – hold the Control and Option keys and hit the Enter key).

![Start a New Line in Excel Cell - Keyboard Shortcut Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20304%20136'%3E%3C/svg%3E)

**See Also:** [200+ Excel Keyboard Shortcuts](https://trumpexcel.com/excel-keyboard-shortcuts/)
.

Start a New Line in Excel Cell Using Formula
--------------------------------------------

While keyboard shortcut is fine when you are manually entering data and need a few line breaks.

But in case you need to combine cells and get a line break while combining these cells, you can use a formula to do this.

### Using TextJoin Formula

If you’re using Excel 2019 or Office 365 (Windows or Mac), you can use the TEXTJOIN function to combine cells and insert a line break in the resulting data.

For example, suppose we have a dataset as shown below and you want to combine these cells to get the name and the address in the same cell (with each part in a separate line):

![Address to Combine with a line break](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%20117'%3E%3C/svg%3E)

The following formula will do this:

\=TEXTJOIN(CHAR(10),TRUE,A2:E2)

At first, you may see the result as one single line that combines all the address parts (as shown below).

![TextJoin to Combine Address with line break](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20163'%3E%3C/svg%3E)

To make sure you have all the line breaks in between each part, make sure the wrap text feature is enabled.

To enable Wrap text, select the cells with the results, click on the Home tab, and within the alignment group, click on the ‘Wrap Text’ option.

![Click on Wrap Text in the Home tab in Excel ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20196'%3E%3C/svg%3E)

Once you click on the Wrap Text option, you will see the resulting data as shown below (with each address element in a new line):

![Resulting Data with Line Breaks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20408'%3E%3C/svg%3E)

Note: If you are using MAC, use CHAR(13) instead of CHAR(10).

### Using Concatenate Formula

If you’re using Excel 2016 or prior versions, you won’t have the TEXTJOIN formula available.

So you can use the good old [CONCATENATE function](https://trumpexcel.com/excel-concatenate-function/)
 (or the ampersand & character) to combine cells and get line break in between.

Again, considering you have the dataset as shown below that you want to combine and get a line break in between each cell:

For example, if I combine using the text in these cells using an ampersand (&), I would get something as shown below:

![Start a New Line in Excel Cell - Dataset Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20834%20130'%3E%3C/svg%3E)

While this combines the text, this is not really the format that I want. You can try using the text wrap, but that wouldn’t work either.

If I am creating a mailing address out of this, I need the text from each cell to be in a new line in the same cell.

To insert a line break in this formula result, we need to use CHAR(10) along with the above formula.

_CHAR(10) is a line feed in Windows, which means that it forces anything after it to go to a new line._

So to do this, use the below formula:

\=A2&CHAR(10)&B2&CHAR(10)&C2&CHAR(10)&D2&CHAR(10)&E2

This formula would enter a line break in the formula result and you would see something as shown below:

![Start a New Line in Excel Cell - Line break in formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20658%20302'%3E%3C/svg%3E)

**IMPORTANT****:** For this to work, you need to [wrap text in excel cells](https://trumpexcel.com/wrap-text/)
. To wrap text, go to Home –> Alignment –> Wrap Text. It is a toggle button.

![Start a New Line in Excel Cell - wrap text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20134'%3E%3C/svg%3E)

_Tip: If you are using MAC, use CHAR(13) instead of CHAR(10)._

**You may also like the following Excel Tutorial:**

*   [Insert Picture in an Excel Cell](https://trumpexcel.com/insert-picture-in-excel-comment/)
    .
*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [Combine Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    
*   [CONCATENATE Excel Range with and without a separator](https://trumpexcel.com/concatenate-excel-ranges/)
    
*   [MS Help – Start a New Line](https://support.office.com/en-GB/article/Start-a-new-line-of-text-inside-a-cell-33e41eab-8b5e-4193-93d6-9a06ecf812b3)
    .
*   [How to Switch Between Sheets in Excel? (7 Better Ways)](https://trumpexcel.com/switch-between-sheets-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “How to Start a New Line in Excel Cell (Keyboard Shortcut + Formula)”
-----------------------------------------------------------------------------------

1.  Shift + command for mac.
    
    There, short and concise.
    
    [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-13076)
    
2.  Sorry to come in so late.  
    I want to clear up something about the keyboard shortcut for the Mac in case anyone has seen this blog post, tried it, and then is wondering why it doesn’t work.
    
    On the Mac, the Enter key and the Return key are different keys. When I read this blog entry, I commented to someone with me that I will be surprised if it is the Enter key rather than the Return key. They are different keys on a standard Mac keyboard. The Return key is the more commonly used one. Then I added that I was saying all of that without trying it, so I could end up with egg on my face!
    
    Then I tried it. And I was correct. As you have written the shortcut, it doesn’t work.  
    Control+Option+Enter does nothing. (The Enter key on an Extended Mac keyboard is grouped with the numeric keypad.)
    
    Control+Option+Return does indeed start a new line.  
    And that’s what I came to find out, and now I know. Thank you for your post. 🙂
    
    [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-12652)
    
3.  Thanks Sumit Bansal, I usually use below format with Alt+Enter between cells in the formula. What do you think?
    
    \=+A2&”  
    “&B2&”  
    “&C2
    
    [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-2529)
    
    *   Thanks for sharing Cesar.. This works great as well.
        
        [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-2530)
        
    *   I was trying to find some formulae that work in Pages. I was finding it difficult to use CHAR formulae in Pages, but your trick helped me. Thanks César Cariboni.
        
        [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-10223)
        
    *   char(10) char(13) wrap text never worked for me, but this one worked! big thank you!!!
        
        [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-10313)
        
4.  Thanks for the video Sumit ! On the flip side, see how to use ‘Ctrl’ & ‘J’ with Text to Columns to split out text separated by line breaks (carriage returns) [https://youtu.be/ky-RdiwnHoM](https://youtu.be/ky-RdiwnHoM)
      
    This ‘Ctrl’ & ‘J’ trick was made popular by Bob Umlas
    
    [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-2495)
    
    *   Thanks for sharing Kevin.. I did an article on amazing things we can do using Find and Replace.. There I covered this Control + J technique.. it’s awesome
        
        [http://trumpexcel.com/2014/07/find-and-replace-in-excel/](http://trumpexcel.com/2014/07/find-and-replace-in-excel/)
        
        [Reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#comment-2496)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/start-a-new-line-in-excel-cell/#respond)

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