# Using Find and Replace in Excel (4 Amazing Tips)

**Source:** https://trumpexcel.com/find-and-replace-in-excel

---

[Skip to content](https://trumpexcel.com/find-and-replace-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/find-and-replace-in-excel/#below-title)

**Watch Video – Useful Examples of Using Find & Replace in Excel**

Last month, one of my colleagues got a data set in Excel, and he was banging his head to [clean](https://trumpexcel.com/clean-data-in-excel/)
 it.

Since I was the only one in the office at that wee hour, he asked me if I could help.

I used a simple technique using Find and Replace in Excel, and his data was all clean and polished.

He thanked me, packed up, and left the office.

Excel Find and Replace feature is super powerful if you know how to use it best.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/find-and-replace-in-excel/#)

Using FIND and REPLACE in Excel (4 Examples)
--------------------------------------------

Find and Replace in Excel can save a lot of time, and that is what matters most these days.

In this blog, I will share four amazing tips that I have shared with hundreds of my colleagues in my office.

The response is always the same – _“I wish I knew this earlier. It could have saved me so much hard labor”._

### To Change Cell References Using Excel Find and Replace

Sometimes when you work with a lot of formulas, there is a need to change a cell reference in all the formulas.

It could take you a lot of time if you manually change it in every cell that has a formula.

Here is where Excel Find and Replace comes in handy. It can easily find a cell reference in all the formulas in the worksheet (or in the selected cells) and replace it with another cell reference.

For example, suppose you have a huge dataset with a formula in that uses $A$1 as one of the cell references (as shown below).

If you need to change $A$1 with $B$1, you can do that using Find and Replace in Excel.

![Find and Replace in Excel - Change Reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20179'%3E%3C/svg%3E)

**Here are the steps to do this:**

1.  Select the cells that have the formula in which you want to replace the reference. If you want to replace in the entire worksheet, select the entire worksheet.
2.  Go to Home –> Find and Select –> Replace _(Keyboard Shortcut – Control + H)_.
3.  In the Find and Replace dialogue box, use the following details:
    *   Find what: $A$1 (the cell reference you want to change).
    *   Replace with: $B$1 (the new cell reference).![Find and Replace in Excel - Change Reference](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20203'%3E%3C/svg%3E)
4.  Click on Replace All.![Find and Replace in Excel - Replace All](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20203'%3E%3C/svg%3E)

This would instantly update all the formulas with the new cell reference.

Note that this would change all the instances of that reference.

For example, if you have the reference $A$1 two times in a formula, both instances would be replaced by $B$1.

Also read: [Absolute, Relative, and Mixed Cell References in Excel](https://trumpexcel.com/absolute-relative-mixed-cell-references/)

### To Find and Replace Formatting in Excel

This is a cool feature when you want to replace existing formatting with some other formatting. For example, you may have cells with an orange background color and you want to change all these cell’s background color to red. Instead of manually doing this, use Find and Replace to do this all at once.

Here are the steps to do this:

1.  Select the cells for which you want to find and replace the formatting. If you want to find and replace a specific format in the entire worksheet, select the entire worksheet.
2.  Go to Home –> Find and Select –> Replace _(Keyboard Shortcut – Control + H)_.
3.  Click on the Options button. This will expand the dialogue box and show you more options.![Find and Replace in Excel - Click on Options Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20586%20251'%3E%3C/svg%3E)
4.  Click on the Find what Format button. It will show a drop-down with two options – Format and Choose Format from Cell.
    *   You can either manually specify the format that you want to find by clicking on the Format button, or you can select the format from a cell in the worksheet. To select a format from a cell, select the ‘Choose Format from Cell’ option and then click on the cell from which you want to pick the format.![Find and Replace in Excel - Choose format from cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20249'%3E%3C/svg%3E)
    *   Once you select a format from a cell or manually specify it from the format cells dialogue box, you will see that as the preview on the left of the format button.![Find and Replace in Excel - preview](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20462%20251'%3E%3C/svg%3E)
5.  Now you need to specify the format that you want instead of the one selected in the previous step. Click on the Replace with Format button. It will show a drop-down with two options – Format and Choose Format from Cell.
    *   You can either manually specify it by clicking on the Format button, or you can pick up an existing format in the worksheet by clicking on the cell that has it.![Find and Replace in Excel - Replace Choose format from cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20251'%3E%3C/svg%3E)
    *   Once you select a format from a cell or manually specify it from the format cells dialogue box, you will see that as the preview on the left of the format button.![Find and Replace in Excel - find and replace with formats](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20255'%3E%3C/svg%3E)
6.  Click on the Replace All button.

You can use this technique to replace a lot of things in formatting. It can pick up and replace formats such as background color, borders, font type/size/color, and even [merged cells](https://trumpexcel.com/find-merged-cells/)
.

### To Add or Remove Line Break

What do you do when you have to go to a new line in an Excel cell.

_You press Alt + Enter._

And what do you do when you want to revert this?

_You delete it manually.. isn’t it?_

Imagine you have hundreds of line breaks that you want to delete. [removing line breaks](https://trumpexcel.com/remove-line-break-excel/)
 manually can take a lot of time.

Here is the good news, you don’t need to do this manually. Excel Find and Replace has a cool trick up its sleeves that will make it happen in a snap.

Here are the steps to remove all the line breaks at once:

1.  Select the data from which you want to remove the line breaks.
2.  Go to Home –> Find and Select –> Replace _(Keyboard Shortcut – Control + H).![Find and Replace in Excel - Home Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20212%20222'%3E%3C/svg%3E)_
3.  In the Find and Replace Dialogue Box:
    *   Find What: Press **Control + J** (you may not see anything except for a blinking dot).
    *   Replace With: **Space bar character** (hit space bar once).![Find and Replace in Excel - Control J](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20463%20241'%3E%3C/svg%3E)
4.  Click on Replace All.

And Woosh! It would magically remove all the line breaks from your worksheet.

Also read: [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)

### To Remove Text Using Wildcard Characters

This one saved me hours. I got a list as shown below, and I had to remove the text between parenthesis.

![Find and Replace in Excel - Wildcard Character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20185'%3E%3C/svg%3E)

If you have a huge data-set, [removing the parentheses](https://trumpexcel.com/remove-parentheses-excel/)
 and the text between it can take you hours. But Find and Replace in Excel can do this in less than 10 seconds.

1.  Select the data
2.  Go to Home –> Find and Select –> Replace (Keyboard Shortcut – _Control + H_)
3.  In the Find and Replace Dialogue Box:
    *   Find What: **(\*)**  
        _Note I have used an asterisk, which is a [wildcard character](https://trumpexcel.com/excel-wildcard-characters/)
         that represents any number of characters._
    *   Replace With: **Leave this Blank.**![Find and Replace in Excel - Wildcard](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20203'%3E%3C/svg%3E)

I hope you find these tips helpful. If there are any other tricks that helped you save time, do share it with us!!

**You May Also Like the Following Excel Tips & Tutorials:**

*   [24 Excel Tricks to Make You Sail through Day-to-day work.](https://trumpexcel.com/24-excel-tricks/)
    
*   [10 Super Neat Ways to Clean Data in Excel Spreadsheets.](https://trumpexcel.com/clean-data-in-excel/)
    
*   [10 Excel Data Entry Tips You Can’t Afford to Miss.](https://trumpexcel.com/excel-data-entry-tips/)
    
*   [Suffering from Slow Excel Spreadsheets? Try these 10 Speed-up Tips.](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
    
*   [How to Filter Cells with Bold Font Formatting in Excel.](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Transpose Data in Excel](https://trumpexcel.com/transpose-data-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “Using Find and Replace in Excel”
------------------------------------------------

1.  Ok, let’s say that I need to exclude cells that have particular added values, while I need to find all the others that don’t have them. Example;  
    5 cells that contain the word “Bread” and 5 more that contain the words “White Bread”. Let’s say that I need the “Find” command to show me only the cells with the “Bread” value. If I hit CTRL + F and type “Bread” it will return all 10 cells. Is there a wildcard which will do the opposite of “\*”? So that if I place it in front and at the end of the letter/letters/word that I need excel to exclude from the search, it will comply? For example, let’s say thhat this wildcard is the “#” symbol. If I hit CTRL + F and type “#Wh#Bread” it will give me only the 5 cells with just the “Bread” value?  
    Also if you select multiple cells by holding down the CTRL key, is there a way to deselect a mistakenly selected cell, without having to repeat the whole process again from the beginning?  
    Thanks in advance.
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-13874)
    
2.  This post is a life saver. Thank you very much!
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-13419)
    
3.  #4 Explaining how to remove words just saved me at least a couple hours today! Thank you!!!!
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-11703)
    
4.  Sumit. This is a great blog indeed. I downloaded your super-useful ebook, then came here to explore more and more useful tips.  
    Thank you so much for taking the time to write, illustrate and share your valuable experience. This is noble indeed.  
    Much appreciated.
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-3619)
    
    *   Thanks for the kind words Amr.. Glad you find the tutorials and the ebook useful 🙂
        
        [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-3620)
        
5.  Sumit, you’re right this is a great post! Thanks!
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-2497)
    
    *   Thanks Kevin.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-2498)
        
6.  Great Tips Thank U sir!
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1525)
    
7.  Great stuff, I can still remember when I first discovered that I could use Find/Replace to modify formulas. Changed my life! I use Find/Replace the most when updating file paths for external links to other workbooks.
    
    Another good tip is you can perform Find/Replace across multiple worksheets by simply highlighting (aka grouping) all the worksheets you want to search within (I used to click through each tab and do a Find/Replace for the active tab, very time consuming if you have a bunch of tabs to cycle through)
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1439)
    
    *   Great Tip Chris.. This would certainly save a lot of time!
        
        [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1442)
        
8.  Nice list of tips! Tom Urtis has another tip you may want to add – using find and replace to move formulas without changing references: [http://www.atlaspm.com/toms-tutorials-for-excel/toms-tutorials-for-excel-copying-formulas-while-keeping-their-relative-and-absolute-references/](http://www.atlaspm.com/toms-tutorials-for-excel/toms-tutorials-for-excel-copying-formulas-while-keeping-their-relative-and-absolute-references/)
    
    [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1438)
    
    *   Great tip by Tom.. Thanks for sharing Dave 🙂
        
        [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1443)
        
    *   Dave.. You gave me the idea and I tried something different to do the same thing (to copy references).  
        Select all the cells that have formula reference that needs to be copied –> change the format to text –> click F2 and hit Control + Enter. Now copy wherever you want, change the format to general, click F2 and press Control + Enter
        
        [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1445)
        
        *   Sumit – Cool approach; very clever and quick. Just tested on a Mac (need to use control-U instead of F2). Works great!
            
            [Reply](https://trumpexcel.com/find-and-replace-in-excel/#comment-1446)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/find-and-replace-in-excel/#respond)

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