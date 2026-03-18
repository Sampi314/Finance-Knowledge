# Comments in Excel VBA (Add, Remove, Block Commenting)

**Source:** https://trumpexcel.com/comments-excel-vba

---

[Skip to content](https://trumpexcel.com/comments-excel-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/comments-excel-vba/#below-title)

When working with VBA coding in Excel, you can easily add comments while writing the code.

Comments in VBA could be really useful for beginners, where you can add a comment to a line of code (or a block of code) that explains what it does.

So, the next time you come back to the code, you’ll not be completely lost and will have some context because of the comments.

Even for advanced Excel VBA programmers, once the code starts to get beyond a few lines, it’s a good idea to add context using comments (especially if there is a chance that someone else may have to work on the code in the future)

And since it’s a comment, VBA ignores it while executing the code.

In this short Excel tutorial, I will cover how to add comments in VBA and all the best practices around it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/comments-excel-vba/#)

Adding Single-Line Comment in VBA
---------------------------------

To add a comment in [VBA](https://trumpexcel.com/excel-vba/)
, simply add an apostrophe sign before the line that you want to be marked as a comment.

Anything after the apostrophe sign in that line would be considered a comment, and VBA would turn it into green color (to visually differentiate it from regular code).

![Comment in VBA Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20208'%3E%3C/svg%3E)

While executing the code, these comments are ignored.

There are two ways you can add a comment in VBA:

1.  Have a comment in a separate line, where this line starts with an apostrophe and then has the comment text after it

![Single line comment in Excel VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20517%20208'%3E%3C/svg%3E)

2.  Have a comment as a part of the regular code line, where after the code, you have a space character followed by an apostrophe and then the comment(as shown below)

![Comment can be added anywhere in vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20655%20180'%3E%3C/svg%3E)

While I’ve seen both of these being used by the VBA programmers, I prefer the first method where a comment has a separate line altogether.

Another (old-school) method of adding a comment is to add the word REM before the comment (where REM is short for Remark).

![REM comment in Excel VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20525%20200'%3E%3C/svg%3E)

Rem was used in the days of BASIC and has been kept in the current versions of VBA. While it’s good to know that it exists, I recommend you only use the apostrophe method while adding comments in VBA.

Adding Multi-Line Comment in VBA
--------------------------------

If you want to add multiple lines of comments in the code, you can have each sentence in a separate line and ensure that each line starts with an apostrophe.

Below is the VBA code where I have three lines of comments:

    Sub Hello()
    
    ' This is a sample code
    ' Code Created by Sumit Bansal
    ' It shows a Message box with the text Hello
    
    MsgBox "Hello"
    
    End Sub

When you put this code in the vb editor, all three lines have an apostrophe before it appears in green color.

![Multiline Comments in VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20502%20225'%3E%3C/svg%3E)

If you have a long comment and you want to break it down into multiple lines without converting each line into a separate comment, you can add a space character followed by an underscore sign and then press enter. This way, VBA would know that the comment continues.

    Sub Hello()
    
    ' Code Created by Sumit Bansal _
    It shows a Message box with the text Hello
    
    MsgBox "Hello"
    
    End Sub

![Long comment in multiple lines in Vba code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20216'%3E%3C/svg%3E)

Converting a Line of Code (or Block of Code) into a Comment
-----------------------------------------------------------

Sometimes, you may need to convert an existing line of code (or a block of code) into comments.

Programmers often do this when they’re working on a code and they want to quickly try out something else, while still keeping the already written code.

So you can quickly comment out a line, try a new one, and if you want to get the earlier code back, just remove the apostrophe and convert that comment back into a normal line of code.

For a line (or even a few lines), it’s best to manually add the apostrophe before these lines.

But if you have a large block of code, use the below steps to add the option to convert an entire block of code into a comment:

1.  Click the View tab

![Click the view tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20348%2091'%3E%3C/svg%3E)

2.  Go to the Toolbar option.
3.  When you hover your cursor over it, you’ll see more options
4.  Click on the Edit option. This will make the edit toolbar appear somewhere on your screen.

![Click on toolbars and then click on edit in vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20570'%3E%3C/svg%3E)

5.  Drag the Edit toolbars towards the toolbar area so that it would dock itself there (in case it’s not docked already)
6.  Select the block of code that you want to comment out
7.  Click on the ‘Comment Block’ option in the toolbar

![Click on the comment block option in vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20478%20127'%3E%3C/svg%3E)

The above steps would instantly convert a block of code into comments by adding an apostrophe in front of every line in that code.

In case you want to remove the comment and convert it back into regular code lines, select that block of code again and click on the ‘Uncomment block’ option in the Edit toolbar

Changing the Color of the Comment in Excel VBA
----------------------------------------------

While VB doesn’t allow a lot of formatting, it does allow you to change the color of the comment if you want to.

One of my [VBA course](https://www.youtube.com/playlist?list=PLm8I8moAHiH2n5HC4ZXBgS-cBLjxWDreu)
 students emailed me and told me that the ability to change the color of comments in VBA was really useful for people suffering from color blindness.

Below are the steps to change the color of the comment in Excel VBA:

1.  Open the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
    
2.  Click the Tools option in the menu

![Click on the tools option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%2092'%3E%3C/svg%3E)

3.  Click on Options
4.  In the Options dialog box, click on the ‘Editor Format’ tab

![Click on options in the Dropdown Menu in vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20227'%3E%3C/svg%3E)

5.  In the Code colors options, select Comment Text

![Select common text in vba](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20579%20440'%3E%3C/svg%3E)

6.  Change the Foreground and/or the background color

![Select the foreground and the background color for the vba comment](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20579%20440'%3E%3C/svg%3E)

7.  Close the dialog box

When you change the comment color, it would also change the color for all the existing comments in your code.

Some Best Practices When Working with Comments in VBA
-----------------------------------------------------

Here are some of the best practices to keep in mind when using comments in the VBA code.

1.  **Keep the comment meaningful and add context**. When adding a comment, consider what would be helpful for a new user who has never seen this code and is trying to make sense of it.
2.  **Avoid excessive commenting,** as it would make your code look a bit cluttered. While it’s alright to add more comments when you are a beginner, as you gain more experience in VBA coding, you will not need to add a lot of comments.
3.  For every new Subroutine or Function, it’s a good idea to add a comment that explains what it does.
4.  When working with complex code, it’s a good idea to **add comments before [conditions and loops](https://trumpexcel.com/vba-loops/)
    **, so that it’s easier for you to get a handle on what you had done when you revisit the code (or when someone else goes through the code)

In this article, I showed you how to add **comments in VBA** codes and some best practices while doing it.

I hope you found this article useful. If you have any questions or suggestions for me do let me know in the comments section.

**Other Excel tutorials you may also like:**

*   [How to Insert / Delete Comments in Excel (including Shortcuts)](https://trumpexcel.com/insert-delete-comments-excel/)
    
*   [How to Print Comments in Excel](https://trumpexcel.com/print-comments-excel/)
    
*   [Get a List of All the Comments in a Worksheet in Excel](https://trumpexcel.com/get-list-of-comments-in-a-worksheet-excel/)
    
*   [Working with Worksheets using Excel VBA](https://trumpexcel.com/vba-worksheets/)
    
*   [Using Workbook Object in Excel VBA (Open, Close, Save, Set)](https://trumpexcel.com/vba-workbook/)
    
*   [Useful Excel Macro Examples for VBA Beginners (Ready-to-use)](https://trumpexcel.com/excel-macro-examples/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/comments-excel-vba/#respond)

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