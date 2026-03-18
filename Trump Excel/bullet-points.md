# 5 Simple Ways to Add Bullet Points in Excel (Shortcut + VIDEO)

**Source:** https://trumpexcel.com/bullet-points

---

[Skip to content](https://trumpexcel.com/bullet-points/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/bullet-points/#below-title)

**Watch Video – How to Add Bullet Points in Excel**

You can easily add bullet points in a cell Excel (Yes.. easily).

Until I knew this trick, I used to put a dash (-) or arrow greater than (>>) at the beginning of the text, and that could sometimes be a pain.

I always wondered why was Excel devoid of such basic functionality.

But that was just my ignorance. There is not one, but many ways to add bullet points in a cell in Excel.

How to Add Bullet Points in Excel

[Toggle](https://trumpexcel.com/bullet-points/#)

How to Add Bullet Points in Excel
---------------------------------

In this tutorial, you’ll learn various ways to insert bullet points in Excel. While all these methods are quite simple, you only need to know a couple to get your work done.

How to Add Bullet Points in Excel

[Toggle](https://trumpexcel.com/bullet-points/#)

### Using Keyboard Shortcut

You can quickly insert bullet points in Excel using the following keyboard shortcuts.

If you have a numeric keypad on your keyboard:

*   Select the cell in which you want to insert the bullet.
*   Either double click on the cell or press F2 – to get into edit mode.
*   Hold the ALT key, press 7 or 9, leave the ALT key.
*   As soon as you leave the ALT key, a bullet would appear.

![Bullet points in Excel - Alt 7](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20511%2070'%3E%3C/svg%3E)

ALT + 7 and ALT + 9 both inserts a different kind of bullet (see below):

![Bullet points in Excel - Shortcuts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20292%20136'%3E%3C/svg%3E)

If you do not have a numeric Keyboard (like my laptop), activate the NumLock first and then repeat the above steps (or try with ALT + FUNCTION + 7)  

If you want to insert more bullet points in the same cell, in the case of having a list in a single cell, repeat the same steps. For example, if you are building a list in a cell, enter the bullet followed by the item name, press Alt + Enter to insert a line break, and then insert the bullet again (as shown below):

![Insert Bullet points in Excel - Multiple Bullets in Same Cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20208'%3E%3C/svg%3E)

_**Note:**_ Once you have the bullet in a cell, you can copy it like any other character.

**See Also:** [200+ Excel Keyboard Shortcuts.](https://trumpexcel.com/excel-keyboard-shortcuts/)

### Using Insert Symbol Dialogue Box

You can use the Insert Symbol option in Excel to insert bullet points in Excel.

Here are the steps:

*   Go to Insert –> Symbols –> Symbol.![Add Bullet points in Excel - Symbols](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20814%20162'%3E%3C/svg%3E)
*   In the Symbols dialogue box, within the Symbols tab, select the Font.![Add Bullet points in Excel - Select Font](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20386'%3E%3C/svg%3E)
*   Scroll down the symbols list and select the bullet you want to insert.![Bullet points in Excel - Select Bullet Symbol](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20564%20387'%3E%3C/svg%3E)
*   Click on the Insert button.![Bullet points in Excel - Insert Bullet Symbol](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20566%20389'%3E%3C/svg%3E)

This will insert the bullet in the selected cell. Once you have the bullet in a cell, you can copy-paste it wherever you need it.

Also read: [Start New Line in Excel Cell](https://trumpexcel.com/start-a-new-line-in-excel-cell/)

### Using the CHAR Function

You can also use the CHAR function to insert bullet points in Excel.

If you enter =CHAR(149) in Excel, it automatically gets converted into a bullet.

![Insert Bullets in Excel - CHAR function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20132'%3E%3C/svg%3E)

This could be useful when you have a list of items and you want to add a bullet to all the items at one go. Something as shown below:

![Bullet points in Excel - Using CHAR function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20273%20100'%3E%3C/svg%3E)

In the above example, bullet points were added to the list of fruits in A1:A4. Here is the formula used in cell B1:

\=CHAR(149)&" "&A1

CHAR(149) inserts the bullet and a space character ensures there is space after the bullet and before the item name.

![Insert Bullets in Excel - Using CHAR function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20288%20144'%3E%3C/svg%3E)

Also read: [Insert Arrows in Excel](https://trumpexcel.com/excel-insert-symbols/arrows/)

### Using Custom Number Formatting

This one is awesome. You can use custom number formatting to automatically insert bullets in excel as soon as you enter anything in a cell.

Something as shown below:

![Insert Bullets in Excel - Custom Number Formatting Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20324'%3E%3C/svg%3E)

Magic. Isn’t it?

Well… Sort of 🙂

What’s working here in the back end is a nifty custom number formatting trick.

Before I get to the trick, here is what you need to know about custom number formatting in Excel. It allows you to specify the format for four kinds of data type:

<Positive numbers> ; <Negative Numbers> ; <Zeroes> ; <Text>

Using custom number formatting, you can specify how each of these data types would be displayed in the cell.

Using this, I can customize cells so that a bullet is automatically displayed as soon as you enter anything in it.

Here are the steps to do it:

*   In any cell, insert a bullet (use the shortcut or insert symbol technique shown above).
*   Double click on the cell that has the bullet (or press F2 to get into the edit mode), select the bullet, and copy it.![Insert Bullet in Excel - Copy Bullet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20296'%3E%3C/svg%3E)
*   Select the cells on which you want to apply the [custom number format](https://trumpexcel.com/excel-custom-number-formatting/)
     (so that the bullet points are automatically inserted).![Insert Bullet in Excel - Copy Cells custom formattin](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20237'%3E%3C/svg%3E)
*   Press Control + 1. It will open the Format Cells Dialogue box.![Insert Bullet in Excel - Format Cells Dialogue Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20467'%3E%3C/svg%3E)
*   In the Number Tab, select Custom.![Add Bullet points in Excel - Select Custom](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20537%20471'%3E%3C/svg%3E)
*   In the type field, enter:  • General;• General;• General;• General![Insert Bullet in Excel - enter format in custom number format field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20469'%3E%3C/svg%3E)
*   Click OK.

That’s it. Go to the cells and try entering anything. It will automatically show the bullet at the beginning.

Also read: [Insert Symbols in Excel](https://trumpexcel.com/excel-insert-symbols/)

### Copy Pasting a list from MS Word or PowerPoint  

You can easily copy and paste a list with bullet points from MS Word into Excel.

If you have a bullet point list in Word, you can paste it in either a single cell in Excel, or get each bullet point in a different cell.

_(Note: Copied list from Word and PowerPoint behave a bit differently when pasted in Excel)._

#### Copy bullet points in a single cell

*   Copy the bullet points from Word.![Insert Bullet in Excel - Copy List Word](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20241%20210'%3E%3C/svg%3E)
*   Double-click on the cell where you want to copy the list.
*   Press Control + V to paste it. ![Insert Bullets in Excel - Single Cell Copy](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20192%20216'%3E%3C/svg%3E)

This will paste the bullet list in the same cell.

_**Note:** In this case, MS Word and PowerPoint behaves differently. While the bullet list from word gets pasted as is (as shown above), the one from PowerPoint gets pasted without the bullet points._

#### Copy bullet points in different cells

*   Copy the bullet points from Word or PowerPoint.
*   Select the cell where you want to copy the list.
*   Press Control + V to paste it. ![Insert Bullets in Excel - paste on different cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20264%20220'%3E%3C/svg%3E)

These are the five simple ways you can use to add bullet points in Excel. Every method has its own benefits and can be used accordingly.

Hope you have enjoyed this article. Let me know your thoughts by leaving a comment below.

**You May Also Like the Following Excel Tutorials:**

*   [How to Insert Watermark in Excel Worksheets](https://trumpexcel.com/insert-watermark-in-excel/)
    .
*   [How to Type Degree Symbol in Excel](https://trumpexcel.com/degree-symbol-in-excel/)
    .
*   [How to Insert Delta Symbol in Excel](https://trumpexcel.com/delta-symbol/)
    .
*   [How to Insert Line Break in Excel](https://trumpexcel.com/insert-line-break-in-excel/)
    .
*   [How to Insert Picture Into an Excel Cell](https://trumpexcel.com/insert-picture-into-excel-cell/)
    
*   [How to Insert Rows in Excel](https://trumpexcel.com/how-to-insert-multiple-rows-in-excel/)
    .
*   [How to Insert bullet points in Google Sheets](https://spreadsheetpoint.com/bullet-points-google-sheets/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “5 Simple Ways to Add Bullet Points in Excel (Shortcut + VIDEO)”
------------------------------------------------------------------------------

1.  Really helpful video, not only you show a way to do it but you shared various methods, awesome thank you!
    
    [Reply](https://trumpexcel.com/bullet-points/#comment-13387)
    
2.  I can not insert bullets by Alt+7 or Alt+9 in Excel 2010. Why?
    
    [Reply](https://trumpexcel.com/bullet-points/#comment-2712)
    
3.  Really Very Helpful Sumit…………..
    
    [Reply](https://trumpexcel.com/bullet-points/#comment-2599)
    
    *   Thanks for commenting Anand.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/bullet-points/#comment-2601)
        
4.  #4 Custom Number Formatting allows the Numbers or Text to still be used as such. “● 1” & “● 2” in two cells added together will result in “● 3”. All other methods will result in an error.
    
    “● A” & “● B” concatenated will result in “● AB”, instead of “● A● B” with the other methods.  
    However, if you have different symbols in the formatting and concatenate or add, the formatting of the result can be unpredictable.
    
    [Reply](https://trumpexcel.com/bullet-points/#comment-2596)
    
    *   Thanks for commenting Jim.. These methods are not interchangeable but can be used based on the situation. As you mentioned, Custom Number format just changes the way data is displayed in the cell, but the data/values remain the same.
        
        [Reply](https://trumpexcel.com/bullet-points/#comment-2600)
        
5.  Wasn’t aware about  
    #4 Using Custom Number Formatting.  
    Thanks for Sharing.
    
    [Reply](https://trumpexcel.com/bullet-points/#comment-2595)
    
    *   Thanks for commenting Rudra.. Glad you find the tutorial useful 🙂
        
        [Reply](https://trumpexcel.com/bullet-points/#comment-2597)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/bullet-points/#respond)

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