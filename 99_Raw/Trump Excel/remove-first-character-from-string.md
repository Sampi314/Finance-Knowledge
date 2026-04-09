# Remove First Character from String in Excel (4 Easy Ways)

**Source:** https://trumpexcel.com/remove-first-character-from-string

---

[Skip to content](https://trumpexcel.com/remove-first-character-from-string/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-first-character-from-string/#below-title)

Working with text data would often require slicing and dicing it.

And one such common thing people often have to do is to **remove the first characters from a string in Excel**.

Suppose you have a dataset as shown below (in column A) and you want to remove only the first characters from each cell and keep the rest of the text as is (resulting data shown in column B).

![Dataset where the first character needs to be removed from the text string](https://trumpexcel.com/wp-content/uploads/2019/11/Dataset-where-the-first-character-needs-to-be-removed-from-the-text-string.png)

There are multiple ways to do this in Excel…

And in this tutorial, I will show you different ways to remove the first characters from a string in Excel.

So let’s not waste any time and get to the point.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-first-character-from-string/#)

There are two types of methods covered in this tutorial. One that needs you to use an extra column and give that result in that extra column. And others where you get the result in the same column itself (Text to columns method and VBA macro method).

Replace the First Character with a Blank Using a Formula
--------------------------------------------------------

One of the easiest wat to remove the first character from a text string in a cell is to replace it with a blank (null character).

And you can easily do this using the [REPLACE function](https://trumpexcel.com/excel-replace-function/)
.

Suppose you have the dataset as shown below and you want to remove the first alphabet from all these cells.

The below formula will do this:

\=REPLACE(A2,1,1,"")

The above formula simply starts from the beginning and replaces 1 character from the beginning with a blank (“”).

![Formula to replace the first character with a blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20424'%3E%3C/svg%3E)

You can also use this to remove multiple characters from each cell. For example, if you want to remove the first two characters, you can use the below formula:

\=REPLACE(A1,1,2,"")

Extract Everything Except the First Characters from a Cell (using a formula)
----------------------------------------------------------------------------

Excel has a lot of Text functions and you can do the same thing in many different ways. In the above method, we replaced the first character with a blank, and in this method, we will use a formula to extract every character from a string except the first one.

This can be done using the RIGHT function (which extracts the given number of characters from the right of a text string).

Suppose you have a dataset as shown below:

![Dataset where there is a string from which first character needs to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20179%20378'%3E%3C/svg%3E)

Here is another formula method to do this by extracting everything except the first character from the cells.

\=RIGHT(A1,LEN(A1)-1)

![RIGHT formula to extract all characters except the first character](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20494%20430'%3E%3C/svg%3E)

The above formula uses the [LEN function](https://trumpexcel.com/excel-len-function/)
 to first find out the total number of characters in the cell. It then uses the [RIGHT function](https://trumpexcel.com/excel-right-function/)
 to get all the characters as a result of the formula, except the first one.

Also read: [Remove Last Character from Cells](https://trumpexcel.com/remove-last-character/)

Use Text to Column to Split the First Character and the Rest of the Text String
-------------------------------------------------------------------------------

The above two formula methods would require you to use an extra column and give the result in that extra column.

Here is a method that uses [Text to Columns in Excel](https://trumpexcel.com/excel-text-to-columns-examples/)
 and allows you to choose whether you want the result in the same cell or in a separate cell.

In case you decide to get the result in the same cells. it’s a good idea to keep a backup of the original data in case you need it in the future.

Suppose you have a dataset as shown below and you want to remove the first character and get all the remaining characters.

![Dataset where there is a string from which first character needs to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20179%20378'%3E%3C/svg%3E)

Below are the steps to do this using Text to Columns in Excel:

1.  Select the cells from which you want to remove the first character in Excel
2.  Click the Data tab![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20532%20198'%3E%3C/svg%3E)
3.  In the Data tools, click on Text to Columns![Click on the Text to Columns option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20141'%3E%3C/svg%3E)
4.  In the Convert Text to Column Wizard, make the following changes:
    *   Step 1 of 3: Select Fixed width (by default Delimited is selected so you need to change this) and click on Next![In Step 1 - Select Fixed Width option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20463'%3E%3C/svg%3E)
    *   Step 2 of 3: In the Data preview, place the cursor after the first character and right-click. This will insert a line as shown below. This line tells Text to Column to split the text into separate cells![Place the cursor where you want the text to be split](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20463'%3E%3C/svg%3E)
    *   Step 3 of 3: Select Do not import column (skip) and keep the destination cell as is (which would be the same cell where you have the data).![Step 3 - Do not import first column and specify the destination for the result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20463'%3E%3C/svg%3E)
5.  Click on Finish.

The above steps would instantly remove the first character from each cell and give you the rest.

**Let me quickly explain how this works:**

When you place the cursor and click after the first character in Step 2, Text to Columns was told to split the data using that line. So the characters before the line are split as one part and the rest as another part.

But in Step 3, since we selected the first column (which was to the left of the line we inserted in Step 2) and then selected ‘Do not import column’, it simply skipped the first character and gave us the remaining part in the same cell.

While I have used this method to remove the first character in Excel, you can use it to remove a second, third, or nth number of characters from the beginning of the end. You can also use this method to extract 2/3/n number of characters from the beginning or the middle of a text string.

Use Flash Fill to Instantly Remove the First Character
------------------------------------------------------

I love the [Flash Fill feature in Excel](https://trumpexcel.com/flash-fill-excel/)
 as it makes it so easy to do some level of text data manipulation.

And what we are trying to do here, Flash Fill is a perfect tool.

Note: Flash Fill is only available in Excel 2013 and later versions. If you’re using Excel 2010 or prior versions, you will not be able to use this method.

Suppose you have the dataset as shown below and you want to remove the first characters from each cell.

![Dataset where there is a string from which first character needs to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20179%20378'%3E%3C/svg%3E)

Here are the steps to do this:

1.  In a cell adjacent to the dataset’s first cell, enter the result you want. In this case, since I have M70 and I want to remove the first character, I will manually enter the value 271.![Manually Enter the value in the first adjacent cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20373'%3E%3C/svg%3E)
2.  In the second cell, enter the expected result, which would be 360 in this example. \[While you’re typing, you may see some values in gray. These are values Flash Fill guessed based on the pattern. If these are correct, stop typing and just hit the enter key and you will get the result. In case these values don’t show or disappear, move to the next step\]![Manually Enter the second value in the second adjacent cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20376'%3E%3C/svg%3E)
3.  Select both the cells, place the cursor at the bottom-right part of the selection (at the small green square) and double-click (or hold the left key of the mouse and drag till the end of the dataset).![Place the cursor on the green squae in the bottom right of the selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20308%20375'%3E%3C/svg%3E)
4.  At the bottom of the resulting data, you will see a small ‘Auto Fill Options’ icon. Click on it.![Click on the Autofill Options icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20317%20413'%3E%3C/svg%3E)
5.  Click on Flash Fill![Click on Flash Fill option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20555'%3E%3C/svg%3E)

That’s it!

You will see Flash Fill has automatically identified the pattern and now gives you all the characters from a cell except the first characters.

There are some really cool things you can do this Flash Fill and I cover those in this video below:

Use a Simple VBA Macro in the Immediate Window
----------------------------------------------

An [immediate window](https://trumpexcel.com/vba-immediate-window/)
 is a place in the [Excel VB Editor](https://trumpexcel.com/visual-basic-editor/)
 that allows you to quickly [run a macro code](https://trumpexcel.com/run-a-macro-excel/)
 (without getting into the hassle of inserting a module or saving the macro)

All you need to do is use the code, copy and paste it in the immediate window and hit the enter key.

Another great thing about this method is that you don’t need to use another column to get the result. As soon as you run the code, it gives you the resulting data in the same cells.

Caution: This method is fine if you have a few hundred or a few thousand cells from which you want to remove the first character. If you have a lot more, this can [slow down your Excel](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
.

Below is the line of code I will be using to remove the first character from each cell in a selected range:

For Each cell In Selection: cell.Value = Right(cell.Value, Len(cell.Value) - 1): Next cell

Here are the steps to use this code from the immediate window:

1.  Select the cells/range from which you want to remove the first character from the text string
2.  Right-click on the sheet tab name (the same sheet where you have this data)
3.  Click on View Code. This will open the VB Editor backend![Right click on sheet tab and then click on View Code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20329%20330'%3E%3C/svg%3E)
4.  In the VB Editor window, click on the View option in the menu and then click on Immediate Window. This will make the immediate window show up. This step is not needed in case the immediate window is already visible.![Click on the View option and then click on Immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20399%20497'%3E%3C/svg%3E)
5.  Copy and paste the above line of code in the immediate window![Copy and Paste the code in immediate window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20519'%3E%3C/svg%3E)
6.  Place the cursor at the end of the line![place the cursor at the end of the VBA code line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20519'%3E%3C/svg%3E)
7.  Hit the Enter key

The above steps would instantly run the code on the selected data and remove the first character from each cell.

**A quick explanation of the line of VBA code**

For Each cell In Selection: cell.Value = Right(cell.Value, Len(cell.Value) - 1): Next cell

The above line of code uses a [For Next loop](https://trumpexcel.com/vba-loops/)
 that goes through each cell in the selection. It then uses the RIGHT and LEN function to extract all the characters, except the first one.

These are the five simple methods you can use to get rid of the first character from a text string and extract the rest. You can choose what method to use based on your data set and your requirements.

For example, if you don’t want to use an extra column and want to get the results in the same cells, you’re better off using the Text to Columns method or the VBA Immediate Window method.

I hope you found this tutorial useful.

**You may also like the following Excel tutorials:**

*   [Remove](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
     [Leading, Trailing, and Double](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
     [Spaces in Excel](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [Extract Numbers from a String in Excel](https://trumpexcel.com/extract-numbers-from-string-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [Remove Characters From Left in Excel](https://trumpexcel.com/remove-characters-from-left-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “Remove First Character from String in Excel”
-----------------------------------------------------------

1.  This is great ..very useful
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-13781)
    
2.  This is great. Thanks, Sumit
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-12934)
    
3.  It really helps and saves time for large list of data
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-12927)
    
4.  Hi Sumit.. thanks for the tutorial. Here are a couple of other formula options that would work:  
    \=MID(A2,2,LEN(A2)-1)  
    \=RIGHT(A2,LEN(A2)-1)  
    \=SUBSTITUTE(A2,LEFT(A2,1),””)  
    Always fun to think of different ways to solve a problem. Thumbs up!
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-12926)
    
5.  Love the text to columns option. Didn’t know this one. Thank you 🙂
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-12921)
    
6.  I just loved it this tips!!! I already suffered a lot trying to Remove the Characters from the cells, in the past… Now everything looks so easy!!! 😉 Thank you!!
    
    [Reply](https://trumpexcel.com/remove-first-character-from-string/#comment-12920)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-first-character-from-string/#respond)

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