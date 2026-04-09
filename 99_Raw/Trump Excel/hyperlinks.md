# Hyperlinks in Excel (A Complete Guide + Examples)

**Source:** https://trumpexcel.com/hyperlinks

---

[Skip to content](https://trumpexcel.com/hyperlinks/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/hyperlinks/#below-title)

Excel allows having hyperlinks in cells which you can use to directly go to that URL.

For example, below is a list where I have company names which are hyperlinked to the company website’s URL. When you click on the cell, it will automatically open your default browser (Chrome in my case) and go to that URL.

There are many things you can do with hyperlinks in Excel (such as a link to an external website, link to another sheet/workbook, link to a folder, link to an email, etc.).

In this article, I will cover all you need to know to work with hyperlinks in Excel (including some useful tips and examples).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/hyperlinks/#)

How to Insert Hyperlinks in Excel
---------------------------------

There are many different ways to create hyperlinks in Excel:

*   Manually type the URL (or copy paste)
*   Using the HYPERLINK function
*   Using the Insert Hyperlink dialog box

Let’s learn about each of these methods.

### Manually Type the URL

When you manually enter a URL in a cell in Excel, or copy and paste it in the cell, Excel automatically converts it into a hyperlink.

Below are the steps that will change a simple URL into a hyperlink:

1.  Select a cell in which you want to get the hyperlink
2.  Press F2 to get into the edit mode (or double click on the cell).
3.  Type the URL and press enter. For example, if I type the URL – https://trumpexcel.com in a cell and hit enter, it will create a hyperlink to it.

![URL gets converted to a hypoerlink when entered](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20432%20176'%3E%3C/svg%3E)

Note that you need to add http or https for those URLs where there is no www in it. In case there is www as the prefix, it would create the hyperlink even if you don’t add the http/https.

Similarly, when you copy a URL from the web (or some other document/file) and paste it in a cell in Excel, it will automatically be hyperlinked.

### Insert Using the Dialog Box

If you want the text in the cell to be something else other than the URL and want it to link to a specific URL, you can use the insert hyperlink option in Excel.

Below are the steps to enter the hyperlink in a cell using the Insert Hyperlink dialog box:

1.  Select the cell in which you want the hyperlink
2.  Enter the text that you want to be hyperlinked. In this case, I am using the text ‘Sumit’s Blog’
3.  Click the Insert tab. ![Insert Tab in the Ribbon in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20198'%3E%3C/svg%3E)
4.  Click the links button. This will open the Insert Hyperlink dialog box (You can also use the keyboard shortcut – Control + K).![Click on the Link option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20192'%3E%3C/svg%3E)
5.  In the Insert Hyperlink dialog box, enter the URL in the Address field.
6.  Press the OK button.

![Insert Hyperlink Dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20362'%3E%3C/svg%3E)

This will insert the hyperlink the cell while the text remains the same.

![Sumit's Blog hyperlinked to the blog URL](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20258%20116'%3E%3C/svg%3E)

There are many more things you can do with the ‘Insert Hyperlink’ dialog box (such as create a hyperlink to another worksheet in the same workbook, create a link to a document/folder, create a link to an email address, etc.). These are all covered later in this tutorial.

### Insert Using the HYPERLINK Function

Another way to insert a link in Excel can be by using the HYPERLINK Function.

Below is the syntax:

_HYPERLINK(link\_location, \[friendly\_name\])_

*   link\_location: This can be the URL of a web-page, a path to a folder or a file in the hard disk, place in a document (such as a specific cell or named range in an Excel worksheet or workbook).
*   \[friendly\_name\]: This is an optional argument. This is the text that you want in the cell that has the hyperlink. In case you omit this argument, it will use the link\_location text string as the friendly name.

Below is an example where I have the name of companies in one column and their website URL in another column.

![Hyperlink Function - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20198'%3E%3C/svg%3E)

Below is the HYPERLINK function to get the result where the text is the company name and it links to the company website.

![Hyperlink Formula to get the result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20245'%3E%3C/svg%3E)

In the examples so far, we have seen how to create hyperlinks to websites.

But you can also create hyperlinks to worksheets in the same workbook, other workbooks, and files and folders on your hard disk.

Let’s see how it can be done.

Create a Hyperlink to a Worksheet in the Same Workbook
------------------------------------------------------

Below are the steps to create a hyperlink to Sheet2 in the same workbook:

1.  Select the cell in which you want the link
2.  Enter the text that you want to be hyperlinked. In this example, I have used the text ‘Link to Sheet2’.
3.  Click the Insert tab.
4.  Click the links button. This will open the Insert Hyperlink dialog box (You can also use the keyboard shortcut – Control + K).
5.  In the Insert Hyperlink dialog box, select ‘Place in This Document’ option in the left pane.![Select Place in This Document in the Insert Hyperlink Dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20424'%3E%3C/svg%3E)
6.  Enter the cell which you want to hyperlink (I am going with the default A1).![Enter the cell to which you want to link](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20424'%3E%3C/svg%3E)
7.  Select the sheet that you want to hyperlink (Sheet2 in this case) ![Select the sheet to which you want to link](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20424'%3E%3C/svg%3E)
8.  Click OK.

Note: You can also use the same method to create a hyperlink to any cell in the same workbook. For example, if you want to link to a far off cell (say K100), you can do that by using this cell reference in step 6 and selecting the existing sheet in step 7.

You can also use the same method to link to a defined name (named cell or [named range](https://trumpexcel.com/named-ranges-in-excel/)
). If you have any named ranges (named cells) in the workbook, these would be listed in under the ‘Defined Names’ category in the ‘Insert Hyperlink’ dialog box.

Apart from the dialog box, there is also a function in Excel that allows you to create hyperlinks.

So instead of using the dialog box, you can instead use the HYPERLINK formula to create a link to a cell in another worksheet.

The below formula will do this:

\=HYPERLINK("#"&"Sheet2!A1","Link to Sheet2")

Below is how this formula works:

*   “#” would tell the formula to refer to the same workbook.
*   “Sheet2!A1” tells the formula the cell that should be linked to in the same workbook
*   “Link to Sheet2” is the text that appears in the cell.

Create a Hyperlink to a File (in the same or different folders)
---------------------------------------------------------------

You can also use the same method to create hyperlinks to other Excel (and non-Excel) files that are in the same folder or are in other folders.

For example, if you want to open a file with the Test.xlsx which is in the same folder as your current file, you can use the below steps:

1.  Select the cell in which you want the hyperlink
2.  Click the Insert tab.
3.  Click the links button. This will open the Insert Hyperlink dialog box (You can also use the keyboard shortcut – Control + K).
4.  In the Insert Hyperlink dialog box, select ‘Existing File or Webpage’ option in the left pane.
5.  Select ‘Current folder’ in the Look in options
6.  Select the file for which you want to create the hyperlink. Note that you can link to any file type (Excel as well as non-Excel files)![Link to a file in the current folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20367'%3E%3C/svg%3E)
7.  \[Optional\] Change the Text to Display name if you want to.
8.  Click OK.

In case you want to link to a file which is not in the same folder, you can Browse the file and then select it. To Browse the file, click on the folder icon in the Insert Hyperlink dialog box (as shown below).

![Browse files or folder to link](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20367'%3E%3C/svg%3E)

You can also do this using the HYPERLINK function.

The below formula will create a hyperlink that links to a file in the same folder as the current file:

\=HYPERLINK("Test.xlsx","Test File")

In case the file is not in the same folder, you can copy the address of the file and use it as the link\_location.

Create a Hyperlink to a Folder
------------------------------

This one also follows the same methodology.

Below are the steps to create a hyperlink to a folder:

1.  Copy the folder address for which you want to create the hyperlink
2.  Select the cell in which you want the hyperlink
3.  Click the Insert tab.
4.  Click the links button. This will open the Insert Hyperlink dialog box (You can also use the keyboard shortcut – Control + K).
5.  In the Insert Hyperlink dialog box, paste folder address![Enter the address of the folder to create a link to it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20367'%3E%3C/svg%3E)
6.  Click OK.

You can also use the HYPERLINK function to create a hyperlink that points to a folder.

For example, the below formula will create a hyperlink to a folder named TEST on the desktop and as soon as you click on the cell with this formula, it will open this folder.

\=HYPERLINK("C:\\Users\\sumit\\Desktop\\Test","Test Folder")

To use this formula, you will have to change the address of the folder to the one you want to link to.

Create Hyperlink to an Email Address
------------------------------------

You can also have hyperlinks which open your default email client (such as Outlook) and have the recipients email and the subject line already filled in the send field.

Below are the steps to create an email hyperlink:

1.  Select the cell in which you want the hyperlink
2.  Click the Insert tab.
3.  Click the links button. This will open the Insert Hyperlink dialog box (You can also use the keyboard shortcut – Control + K).
4.  In the insert dialog box, click on ‘E-mail Address’ in the ‘Link to’ options
5.  Enter the E-mail address and the Subject line![Create link to Email address with subject line](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20366'%3E%3C/svg%3E)
6.  \[Optional\] Enter the text you want to be displayed in the cell.
7.  Click OK.

Now when you click on the cell which has the hyperlink, it will open your default email client with the email and subject line pre-filled.

You can also do this using the HYPERLINK function.

The below formula will open the default email client and have one email address already pre-filled.

\=HYPERLINK("mailto:abc@trumpexcel.com","Send Email")

Note that you need to use **mailto:** before the email address in the formula. This tells the HYPERLINK function to open the default email client and use the email address that follows.

In case you want to have the subject line as well, you can use the below formula:

\=HYPERLINK("mailto:abc@trumpexcel.com,?cc=&bcc=&subject=Excel is Awesome","Generate Email")

In the above formula, I have kept the cc and bcc fields as empty, but you can also these emails if needed.

Here is a detailed guide on how to [send emails using the HYPERLINK function](https://trumpexcel.com/send-email-from-excel-hyperlink/)
.

Remove Hyperlinks
-----------------

If you only have a few hyperlinks, you can remove these manually, but if you have a lot, you can use a [VBA Macro](https://trumpexcel.com/excel-macro-examples/)
 to do this.

### Manually Remove Hyperlinks

Below are the steps to remove hyperlinks manually:

1.  Select the data from which you want to remove hyperlinks.
2.  Right-click on any of the selected cell.
3.  Click on the ‘Remove Hyperlink’ option.![Select Remove Hyperlinks option from the right-click menu](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20472'%3E%3C/svg%3E)

The above steps would instantly remove hyperlinks from the selected cells.

In case you want to remove hyperlinks from the entire worksheet, select all the cells and then follow the above steps.

### Remove Hyperlinks Using VBA

Below is the VBA code that will remove the hyperlinks from the selected cells:

Sub RemoveAllHyperlinks()
'Code by Sumit Bansal @ trumpexcel.com
Selection.Hyperlinks.Delete
End Sub

If you want to remove all the hyperlinks in the worksheet, you can use the below code:

Sub RemoveAllHyperlinks()
'Code by Sumit Bansal @ [trumpexcel.com](https://trumpexcel.com/)

ActiveSheet.Hyperlinks.Delete
End Sub

Note that this code will not remove the hyperlinks created using the HYPERLINK function.

You need to add this VBA code in the regular module in the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
.

If you need to remove hyperlinks quite often, you can use the above VBA codes, save it in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
, and add it to your Quick Access Toolbar. This will allow you to remove hyperlinks with a single click and it will be available in all the workbooks on your system.

Here is a detailed guide on how to [remove hyperlinks in Excel](https://trumpexcel.com/remove-hyperlinks/)
.

Prevent Excel from Creating Hyperlinks Automatically
----------------------------------------------------

For some people, it’s a great feature that Excel automatically converts a URL text to a hyperlink when entered in a cell.

And for some people, it’s an irritation.

If you’re in the latter category, let me show you a way to prevent Excel from automatically creating URLs into hyperlinks.

The reason this happens as there is a setting in Excel that automatically converts ‘Internet and network paths’ into hyperlinks.

Here are the steps to disable this setting in Excel:

1.  Click the File tab.
2.  Click on Options.![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20284'%3E%3C/svg%3E)
3.  In the Excel Options dialog box, click on ‘Proofing’ in the left pane.![Proofing option in the left pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20254'%3E%3C/svg%3E)
4.  Click on the [AutoCorrect](https://trumpexcel.com/autocorrect/)
     Options button.![Click on the Autocorrect Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20254'%3E%3C/svg%3E)
5.  In the AutoCorrect dialog box, select the ‘AutoFormat As You Type’ tab.![Select Autoformat as you type tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20183'%3E%3C/svg%3E)
6.  Uncheck the option – ‘Internet and network paths with hyperlinks’![Uncheck Internet and Network Paths with hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20407%20174'%3E%3C/svg%3E)
7.  Click OK.
8.  Close the Excel Options dialog box.

If you’ve completed the following steps, Excel would not automatically turn URLs, email address, and network paths into hyperlinks.

Note that this change is applied to the entire Excel application, and would be applied to all the workbooks that you work with.

Extract Hyperlink URLs (using VBA)
----------------------------------

There is no function in Excel that can extract the hyperlink address from a cell.

However, this can be done using the power of VBA.

For example, suppose you have a dataset (as shown below) and you want to [extract the hyperlink URL](https://trumpexcel.com/extract-url-from-hyperlinks-excel/)
 in the adjacent cell.

![Extract Hyperlink from the dataset in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20463'%3E%3C/svg%3E)

Let me show you two techniques to extract the hyperlinks from the text in Excel.

### Extract Hyperlink in the Adjacent Column

If you want to extract all the hyperlink URLs in one go in an adjacent column, you can so that using the below code:

Sub ExtractHyperLinks()
Dim HypLnk As Hyperlink
For Each HypLnk In Selection.Hyperlinks
    HypLnk.Range.Offset(0, 1).Value = HypLnk.Address
Next HypLnk
End Sub

The above code goes through all the cells in the selection (using the [FOR NEXT loop](https://trumpexcel.com/for-next-loop-excel-vba/)
) and extracts the URLs in the adjacent cell.

In case you want to get the hyperlinks in the entire worksheet, you can use the below code:

Sub ExtractHyperLinks()
On Error Resume Next
Dim HypLnk As Hyperlink
For Each HypLnk In ActiveSheet.Hyperlinks
    HypLnk.Range.Offset(0, 1).Value = HypLnk.Address
Next HypLnk
End Sub

Note that the above codes wouldn’t work for hyperlinks created using the HYPERLINK function.

### Extract Hyperlink Using a Formula (created with VBA)

The above code works well when you want to get the hyperlinks from a dataset in one go.

But if you have a list of hyperlinks that keeps expanding, you can create a [User Defined Function](https://trumpexcel.com/user-defined-function-vba/)
/formula in VBA.

This will allow you to quickly use the cell as the input argument and it will return the hyperlink address in that cell.

Below is the code that will create a UDF for getting the hyperlinks:

Function GetHLink(rng As Range) As String
    If rng(1).Hyperlinks.Count <> 1 Then
        GetHLink = ""
    Else
        GetHLink = rng.Hyperlinks(1).Address
    End If
End Function

Note that this wouldn’t work with Hyperlinks created using the HYPERLINK function.

Also, in case you select a range of cells (instead of a single cell), this formula will return the hyperlink in the first cell only.

Find Hyperlinks with Specific Text
----------------------------------

If you’re working with a huge dataset that has a lot of hyperlinks in it, it could be a challenge when you want to find the ones that have a specific text in it.

For example, suppose I have a dataset as shown below and I want to find all the cells with hyperlinks that have the text 2019 in it and change it to 2020.

![Find and Replace Hyperlink Text - dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20258%20367'%3E%3C/svg%3E)

And no.. doing this manually is not an option.

You can do that using a wonderful feature in Excel – [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
.

With this, you can quickly find and select all the cells that have a hyperlink and then change the text 2019 with 2020.

Below are the steps to select all the cells with a hyperlink and the text 2019:

1.  Select the range in which you want to find the cells with hyperlinks with 2019. In case you want to find in the entire worksheet, select the entire worksheet (click on the small triangle at the top left).
2.  Click the Home tab.![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20339%20192'%3E%3C/svg%3E)
3.  In the Editing group, click on Find and Select![Find and Select in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20384%20120'%3E%3C/svg%3E)
4.  In the drop-down, click on Replace. This will open the Find and Replace dialog box.![Replace Option in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20431'%3E%3C/svg%3E)
5.  In the Find and Replace dialog box, click on the Options button.This will show more options in the dialog box. ![Click on the Options button in Find and Replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20187'%3E%3C/svg%3E)
6.  In the ‘Find What’ options, click on the little downward pointing arrow in the Format button (as shown below). ![Click the downward pointing arrow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)
7.   Click on the ‘Choose Format From Cell’. This will turn your cursor into a plus icon with a format picker icon.![Select Choose format from cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20750%20293'%3E%3C/svg%3E)
8.  Select any cell which has a hyperlink in it. You will notice that the Format gets visible in the box on the left of the Format button. This indicates that the format of the cell you selected has been picked up.![Selecting a cell with hyperlink will change the preview](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)
9.  Enter 2019 in the ‘Find What’ field and 2020 in the ‘Replace with’ field.![Enter the values in find what and replace what fields](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)
10.  Click on the Replace All button.![Click on the Replace ALL button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

In the above data, it will change the text of four cells that have the text 2019 in it and also has a hyperlink.

![Message Box to show the number of replacements](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

You can also use this technique to [find all the cells with hyperlinks](https://trumpexcel.com/find-hyperlinks-in-excel/)
 and get a list of it. To do this, instead of clicking on Replace All, click on the Find All button. This will instantly give you a list of all the cell address that has hyperlinks (or hyperlinks with specific text depending on what you’ve searched for).

Note: This technique works as Excel is able to identify the formatting of the cell that you select and use that as a criterion to find cells. So if you’re finding hyperlinks, make sure you select a cell that has the same kind of formatting. If you select a cell that has a background color or any text formatting, it may not find all the correct cells.

Selecting a Cell that has a Hyperlink in Excel
----------------------------------------------

While Hyperlinks are useful, there are a few things about it that irritate me.

For example, if you want to select a cell that has a hyperlink in it, Excel would automatically open your default web browser and try to open this URL.

Another irritating thing about it is that sometimes when you have a cell that has a hyperlink in it, it makes the entire cell clickable. So even if you’re clicking on the hyperlinked text directly, it still opens the browser and the URL of the text.

So let me quickly show you how to get rid of these minor irritants.

### Select the Cell (without opening the URL)

This is a simple trick.

When you hover the cursor over a cell that has a hyperlink in it, you’ll notice the hand icon (which indicates if you click on it, Excel will open the URL in a browser)

![Hand Icon when you hover over a hyperlink cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20253%20191'%3E%3C/svg%3E)

Click the cell anyway and hold the left button of the mouse.

After a second, you’ll notice that the hand cursor icon changes into the plus icon, and now when you leave it, Excel will not open the URL.

![Plus icon when you hold the left mouse button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20191'%3E%3C/svg%3E)

Instead, it would select the cell.

Now, you can make any changes in the cell you want.

Neat trick… right?

### Select a Cell by clicking on the blank space in the cell

This is another thing that might drive you nuts.

When there is a cell with the hyperlink in it as well as some blank space, and you click on the blank space, it still opens the hyperlink.

![Click hand icon when hover over white space of a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20251%20188'%3E%3C/svg%3E)

Here is a quick fix.

This happens when these cells have the wrap text enabled.

If you disable wrap text for these cells, you will be able to click on the white space on the right of the hyperlink without opening this link.

Some Practical Example of Using Hyperlink
-----------------------------------------

There are useful things you can do when working with hyperlinks in Excel.

In this section, I am going to cover some examples that you may find useful and can use in your day-to-day work.

### Example 1 – Create an Index of All Sheets in the Workbook

If you have a workbook with a lot of sheets, you can use a VBA code to quickly create a list of the worksheets and hyperlink these to the sheets.

This could be useful when you have 12-month data in 12 different worksheets and want to create one index sheet that links to all these monthly data worksheets.

Below is the code that will do this:

Sub CreateSummary()
'Created by Sumit Bansal of trumpexcel.com
'This code can be used to create summary worksheet with hyperlinks
Dim x As Worksheet
Dim Counter As Integer
Counter = 0
For Each x In Worksheets
Counter = Counter + 1
If Counter = 1 Then GoTo Donothing
    With ActiveCell
        .Value = x.Name
        .Hyperlinks.Add ActiveCell, "", x.Name & "!A1", TextToDisplay:=x.Name, ScreenTip:="Click here to go to the Worksheet"
        With Worksheets(Counter)
            .Range("A1").Value = "Back to " & ActiveSheet.Name
            .Hyperlinks.Add Sheets(x.Name).Range("A1"), "", \_
            "'" & ActiveSheet.Name & "'" & "!" & ActiveCell.Address, \_
            ScreenTip:="Return to " & ActiveSheet.Name
        End With
    End With
ActiveCell.Offset(1, 0).Select
Donothing:
Next x
End Sub

You can place this code in the regular module in the workbook (in [VB Editor](https://trumpexcel.com/visual-basic-editor/)
)

This code also adds a link to the summary sheet in cell A1 of all the worksheets. In case you don’t want that, you can remove that part from the code.

![Creating Summary sheet with VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20423'%3E%3C/svg%3E)

You can [read more about this example here](https://trumpexcel.com/create-summary-worksheet-in-excel/)
.

Note: This code works when you have the sheet (in which you want the summary of all the worksheets with links) at the beginning. In case it’s not at the beginning, this may not give the right results).

### Example 2 – Create Dynamic Hyperlinks

In most cases, when you click on a hyperlink in a cell in Excel, it will take you to a URL or to a cell, file or folder. Normally, these are static URLs which means that a hyperlink will take you to a specific predefined URL/location only.

But you can also use a little bit for [Excel formula](https://trumpexcel.com/excel-functions/)
 trickery to create dynamic hyperlinks.

By dynamic hyperlinks, I mean links that are dependent on a user selection and change accordingly.

For example, in the below example, I want the hyperlink in cell E2 to point to the company website based on the drop-down list selected by the user (in cell D2).

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20175'%3E%3C/svg%3E)

This can be done using the below formula in cell E2:

\=HYPERLINK(VLOOKUP(D2,$A$2:$B$6,2,0), "Click here")

The above formula uses the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 to fetch the URL from the table on the left. The HYPERLINK function then uses this URL to create a hyperlink in the cell with the text – ‘Click here’.

When you change the selection using the drop-down list, the VLOOKUP result will change and would accordingly link to the selected company’s website.

This could be a useful technique when you’re creating a dashboard in Excel. You can make the hyperlinks dynamic depending on the user selection (which could be a [drop-down list](https://trumpexcel.com/excel-drop-down-list/)
 or a [checkbox](https://trumpexcel.com/insert-checkbox-in-excel/)
 or a [radio button](https://trumpexcel.com/insert-use-radio-button-in-excel/)
).

Here is a more detailed article of using [Dynamic Hyperlinks in Excel](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/)
.

### Example 3 – Quickly Generate Simple Emails Using Hyperlink Function

As I mentioned in this article earlier, you can use the HYPERLINK function to quickly create simple emails (with pre-filled recipient’s emails and the subject line).

**Single Recipient Email Id**

\=HYPERLINK("**mailto:abc@trumpexcel.com**","Generate Email")

This would open your default email client with the email id abc@trumpexcel.com in the ‘To’ field.

**Multiple Recipients Email Id**

\=HYPERLINK("mailto:abc@trumpexcel.com**,def@trumpexcel.com**","Generate Email")

For sending the email to multiple recipients, use a comma to separate email ids. This would open the default email client with all the email ids in the ‘To’ field.

**Add Recipients in CC and BCC List**

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com**?cc=123@trumpexcel.com&bcc=456@trumpexcel.com**","Generate Email")

To add recipients to CC and BCC list, use question mark ‘?’ when ‘mailto’ argument ends, and join CC and BCC with ‘&’. When you click on the link in excel, it would have the first 2 ids in ‘To’ field, 123@trumpexcel.com in ‘CC’ field and 456@trumpexcel.com in the ‘BCC’ field.

**Add Subject Line**

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&**subject=Excel is Awesome**","Generate Email")

You can add a subject line by using the &Subject code. In this case, this would add ‘Excel is Awesome’ in the ‘Subject’ field.

**Add Single Line Message in Body**

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&subject=Excel is Awesome&**body=I love Excel**","Email Trump Excel")

This would add a single line ‘I love Excel’ to the email message body.

**Add Multiple Lines Message in Body**

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&subject=Excel is Awesome&**body=I love Excel.%0AExcel is Awesome**","Generate Email")

To add multiple lines in the body you need to separate each line with **%0A**. If you wish to introduce two [line breaks](https://trumpexcel.com/start-a-new-line-in-excel-cell/)
, add **%0A** twice, and so on.

Here is a detailed article on how to [send emails from Excel](https://trumpexcel.com/send-email-from-excel-hyperlink/)
.

Hope you found this article useful.

Let me know your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Excel AutoCorrect](https://trumpexcel.com/autocorrect/)
    
*   [How to Find External Links and References in Excel](https://trumpexcel.com/find-external-links-excel/)
    
*   [100+ Excel Interview Questions & Answers](https://trumpexcel.com/excel-interview-questions/)
    
*   [Excel Text to Columns](https://trumpexcel.com/excel-text-to-columns-examples/)
    
*   [Excel Sparklines](https://trumpexcel.com/sparklines/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “Hyperlinks in Excel (A Complete Guide + Examples)”
-----------------------------------------------------------------

1.  Dear Sumit Bansal, your “Example 1 – Create an Index of All Sheets in the Workbook” has an error and works not correctly.  
    #1 if the sheets has “(” or space ” ” in the name, the links in the Summary sheet are wrong. You get an error message after clicking them. Try simple Excel Workbook with Sheets named “S”, “S(2)” and “S 3” for example.  
    #2 the Summary sheet in my opinion should be generated automatically AND more important active cell set to A1. You do either one nor second.  
    Whatt follows is a summary elswhere in the active sheet (after the active cell of course).  
    The code example is only partially usefull – I would not publish it (I was programmer since 1977, now retired). Best regards
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-35685)
    
2.  Sir, 11th July,2020.  
    Very neatly and clearly you have shown the article ” Hyperlink”.  
    I must salute your efforts.  
    Moreover, I eagerly await such Tips and Tricks in near future too.  
    Once again thanking you.  
    Kanhaiyalal Newaskar.
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-14395)
    
3.  How to return a value when click on a hyper link. For example value in Sheet1 A1 is “Test” and there is an hyperlink to sheet2 A1 , so after when click, the value “Test1” should reflect in Sheet2 A1..
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-14282)
    
4.  I would like to be able to hover over a hyperlink and display specific text. How can I do that?
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-13826)
    
5.  Hi. Thanks for the excellent tutorial on hyperlinks. I am trying to record a macro in excel that inserts a dynamic hyperlink into an image which is then added to an email. The only part that I am stuck on is when using the “Insert Hyperlink” dialogue box, I can’t paste the URL into the address tab. All of the options are greyed out. Interestingly, when I do the same action within Outlook, I CAN paste the URL into the dialogue box if I try to insert within Outlook. Any tips on what is causing the dialogue box in excel to grey out the paste functions? Any help much appreciated – Thanks.
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-13672)
    
6.  The marcos here are lifesavers. Thank you!
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-13643)
    
7.  Is it possible to link a portion of the sheet to email directly to an email by simply clicking the hyperlink? i.e if i have several data sets that need to go to different people in a single sheet. I cannot just send the entire sheet for privacy reasons.
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-13069)
    
8.  how to link a folder contains multiple jpg photos with serial number 1 to so on such as 1.JPG,2.JPG,…
    
    [Reply](https://trumpexcel.com/hyperlinks/#comment-11403)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/hyperlinks/#respond)

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