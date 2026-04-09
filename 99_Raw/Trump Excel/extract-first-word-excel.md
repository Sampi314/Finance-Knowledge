# How to Extract the First Word from a Text String in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/extract-first-word-excel

---

[Skip to content](https://trumpexcel.com/extract-first-word-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-first-word-excel/#below-title)

Excel has some wonderful formulas that can help you slice and dice the text data.

Sometimes, when you have the text data, you may want to extract the first word from the text string in a cell.

There are multiple ways you can do this in Excel (using a combination of formulas, using Find and Replace, and using Flash Fill)

In this tutorial, I will show you some really simple ways to **extract the first word from a text string in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/extract-first-word-excel/#)

Extract the First Word Using Text Formulas
------------------------------------------

Suppose you have the following dataset, where you want to get the first word from each cell.

![Dataset to Extract the first word from text string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20300'%3E%3C/svg%3E)

The below formula will do this:

\=IFERROR(LEFT(A2,FIND(" ",A2)-1),A2)

![Formula to find and extract only the first word](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20355'%3E%3C/svg%3E)

Let me explain how this formula works.

The [FIND](https://trumpexcel.com/excel-find-function/)
 part of the formula is used to find the position of the space character in the text string. When the formula finds the position of the space character, the LEFT function is used to extract all the characters before that first space character in the text string.

While the [LEFT formula](https://trumpexcel.com/excel-left-function/)
 alone should be enough, it will give you an error in case there is only one word in the cell and no space characters.

To handle this situation, I have wrapped the LEFT formula in the [IFERROR formula](https://trumpexcel.com/excel-iferror-function/)
, which simply returns the original cell content (as there are no space characters indicating that it’s either empty or has only one word).

One good thing about this method is that the result is dynamic. This means that in case you change the original text string in the cells in column A, the formula in column B will automatically update and give the correct result.

In case you don’t want the formula, you can [convert it into values](https://trumpexcel.com/convert-formulas-to-values-excel/)
.

Extract the First Word Using Find and Replace
---------------------------------------------

Another quick method to extract the first word is to use [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 to remove everything except the first word.

Suppose you have the dataset as shown below:

![Dataset to Extract the first word from text string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20300'%3E%3C/svg%3E)

Below are the steps to use Find and Replace to only get the first word and remove everything else:

1.  Copy the text from column A to column B. This is to make sure that we have the original data as well.
2.  Select all the cells in Column B where you want to get the first word![Copy the text to Column B](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20340'%3E%3C/svg%3E)
3.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20201'%3E%3C/svg%3E)
4.  In the Editing group, click on Find and Select option and then click on Replace. This will open the Find & Replace dialog box.![Click on Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20553'%3E%3C/svg%3E)
5.  In the Find what field, enter  **\*** (one space character followed by the asterisk sign)![Enter Space character followed by asterisk in Find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)
6.  Leave the Replace with field empty![Leave the replace with empty](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)
7.  Click on Replace All button.![Click on replace all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)

The above steps would remove everything except the first word in the cells.

![result after find and replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20301'%3E%3C/svg%3E)

You can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 **Control + H** to open the Find and Replace dialog box.

**How does this work?**

In Find what field, we have used a space character followed by the asterisk sign. The asterisk sign (\*) is a [wild card character](https://trumpexcel.com/excel-wildcard-characters/)
 that represents any number of characters.

So when we ask Excel to find cells that contain space character followed by the asterisk sign and replace it with blank, it finds the first space character and removes everything after it – leaving us with the first word only.

And in case you a cell that has no text or only one word with no space characters, the above steps would not make any changes to it.

Also read: [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)

Extract the First Word Using Flash Fill
---------------------------------------

Another really simple and fast method to extract the first word using [Flash Fill](https://trumpexcel.com/flash-fill-excel/)
.

Flash Fill was introduced in Excel 2013 and is available in all the versions after that. It helps in text manipulation by identifying the pattern that you’re trying to achieve and fills it for the entire column.

For example, suppose you have the below dataset and you want to only extract the first word.

![Dataset to Extract the first word from text string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20300'%3E%3C/svg%3E)

Below are the steps to do this:

1.  In cell B2, which is the adjacent column of our data, manually enter ‘Marketing’ (which is the expected result)![Enter the first word in first cell manually](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20300'%3E%3C/svg%3E)
2.  In cell B3, enter ‘HR’![Enter manually in second cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20296'%3E%3C/svg%3E)
3.  Select the range B2:B10![Select the range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20298'%3E%3C/svg%3E)
4.  Click on the Home tab
5.  In the Editing group, click on the Fill drop-down
6.  Click on Flash Fill option![Click on Flash Fill](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20380%20401'%3E%3C/svg%3E)

The above steps would fill all the cells with the first word from the adjacent column (column A).

**Caution**: In most cases, Flash Fill works fine and gives the correct result, but in some cases, it may not give you the right result. Just make sure to double-check that the results are as expected.

_Note: When typing the expected result in the second cell in column B, you may see all text in all the cells in a light gray color. That is the result you will get if you hit the enter key right away. In case you don’t see the gray line, use the Flash Fill option in the ribbon._

So these are three simple methods to extract the first word from a text string in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [Extract Numbers from a String in Excel (Using Formulas or VBA)](https://trumpexcel.com/extract-numbers-from-string-excel/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [How to Combine First and Last Name in Excel](https://trumpexcel.com/combine-first-and-last-name-excel/)
    
*   [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-first-word-excel/#respond)

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