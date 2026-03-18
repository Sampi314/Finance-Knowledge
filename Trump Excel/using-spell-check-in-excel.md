# Spell Check in Excel – Where is it and How to Use it?

**Source:** https://trumpexcel.com/using-spell-check-in-excel

---

[Skip to content](https://trumpexcel.com/using-spell-check-in-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/using-spell-check-in-excel/#below-title)

**Watch the Video Tutorial – Spell Check in Excel**

Spell Check in Excel is often ignored given that Excel users often work with numbers as compared with text. But it is still one of the important checks one should have in place.

As compared to MS Word or PowerPoint, where you can visually see a red underline below the word that has been misspelled, nothing of that sorts happen in Excel.

Imagine a disastrous spelling error glaring out of your worksheet when you sent it to your client. No matter how much hard work you put into data crunching and analysis, all your credibility goes down the drain.

Well – NOT anymore.

In this tutorial, I will show you how to use spell check in Excel and how you can maximize your efforts by the options available to you.

##### Where to find Spell Check in Excel

You can find spell check option in review tab in the ribbon in Excel.

![Spell Check in Excel - Review Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20140'%3E%3C/svg%3E)

When you click on the Spelling option in the review tab, it opens the Spell Check dialogue box.

![Spell Check in Excel - Spelling Dialogue box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20303'%3E%3C/svg%3E)

##### Keyboard Shortcut to Run Spell Check in Excel

You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 F7 to run spell Check in Excel. To use this, activate the worksheet in which you want to run spell check, select the cell/range of cells, and press F7 from your keyboard.

![Spell Check in Excel - Keyboard Shortcut](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%2095'%3E%3C/svg%3E)

##### How Does Spell Check Works in Excel  

An important thing worth knowing is how spell check in Excel works.

If you select cell A1, it will go through all the cells in the first row, then moves to the second row and check all the cells in the second row (from left to right) and then move to the third row and so on. If it identifies a cell with a spelling error, it displays the Spelling dialogue box.

If you select a cell somewhere else in the worksheet, let’s say B3, then it will go through the cells to the right and then to the row below it. When it is done with checking for all the cells after B3, it will show a prompt that asks the user if he wants to continue checking at the beginning of the sheet. Something as shown below:

![Spell Check in Excel - check from sheet beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20118'%3E%3C/svg%3E)

If the user selects Yes, it goes back and checks the remaining cells (which would be A1 to B2 in our example).

To get a better understanding, have a look at this example below (cell shaded are the ones with a spelling error):

![Spell Check in Excel - flow of spell check](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20856%20568'%3E%3C/svg%3E)

As shown, when we begin the spell check with A1, it completes the spell check for all the cells. But when we begin with cell B3, it checks for all the cells from B3 and then asks the user if he/she wants to continue checking from the beginning.

##### Understanding the Spell Check Dialogue Box

Whenever you run spell check in excel and it finds an error, it shows the Spell check dialogue box (as shown below):

![Spell Check in Excel - understanding the dialogue box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20305'%3E%3C/svg%3E)

Let’s quickly understand the different options available in the spell check dialogue box:

*   **Ignore Once**: If spell check encounters a word it identifies as an error, but you want to keep it that way, you can click on Ignore Once. This will ignore that error once.
*   **Ignore All**: If excel identifies a word as an error, but you want to keep all instances of that word (as is), click on Ignore All.
*   **Add to Dictionary**: If Excel flags a word as an error but it is the correct word to be used (maybe it’s a name or abbreviation that you use in your company), then you can add it to the dictionary. When such a word is flagged as an error and you click on Add to Dictionary, Excel will make that a part of acceptable words and won’t flag it again. Note that this word is now part of Excel dictionary and would never be flagged in any of the workbooks.
*   **Change**: When Excel highlights an error, it also shows some suggestions (for example it suggests Good in place of Goood). There can be one or more that one suggestion. Select the suggestion that you want to use and click on Change to apply that.
*   **Change All**: If you click on this button, it will change all the occurrence of the misspelled word with the selected suggestion.
*   **AutoCorrect**: [Excel autocorrect](https://trumpexcel.com/autocorrect/)
     option will change the misspelled word with the selected suggestion, and also add it to the autocorrect list. This means, that next time you type the same misspelled word, excel would automatically convert it into the suggestion that you selected.
*   **Dictionary Language**: You can change the dictionary language using this drop down.

Here are some default settings in Spell Check in Excel:

1.  It ignores words which are in Upper Case. For example, if you have the word HELLOOO, it will not be flagged as an error.
2.  It ignores words that contain numbers. For example, if you have the word Hello123, it will not be flagged as an error.
3.  It ignores internet and file addresses.
4.  It DOES NOT ignore repeated words. For example, if you have the text – Hello, How are are you? – then it the additional are will be flagged as an error.

You can change these default setting by clicking on the ‘Option’ button in the Spell Check Dialogue box. It will open the Options dialogue box where you can make the necessary changes.

![Spell Check in Excel - options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20366'%3E%3C/svg%3E)

Hope you found this tutorial helpful. Let me know your thoughts by leaving a comment below.

**You May Also Like the Following Excel Tutorials:**

*   [10 Super Neat Ways to Clean Data in Excel Spreadsheets](https://trumpexcel.com/clean-data-in-excel/)
    .
*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    .
*   [How to Track Changes in Excel](https://trumpexcel.com/track-changes-in-excel/)
    .
*   [MS Help – Checking Spelling and Grammar](https://support.office.com/en-us/article/Check-spelling-and-grammar-5cdeced7-d81d-47de-9096-efd0ee909227)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “Spell Check in Excel – Where is it and How to Use it?”
---------------------------------------------------------------------

1.  Very helpful! Thank you!
    
    [Reply](https://trumpexcel.com/using-spell-check-in-excel/#comment-14675)
    
2.  A good spelling tutorial, but there are some grammatical errors: “How Does Spell Check Works in Excel” and “There can be one or more that one suggestion” are two.
    
    [Reply](https://trumpexcel.com/using-spell-check-in-excel/#comment-10545)
    
3.  Very great reminder, I always seem to forget. Cheers!
    
    [Reply](https://trumpexcel.com/using-spell-check-in-excel/#comment-9498)
    
4.  good information dear
    
    [Reply](https://trumpexcel.com/using-spell-check-in-excel/#comment-9395)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/using-spell-check-in-excel/#respond)

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