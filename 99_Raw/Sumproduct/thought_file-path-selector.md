# File Path Selector

**Source:** https://sumproduct.com/thought/file-path-selector/

---

[Home](https://sumproduct.com/)

\> File Path Selector

*   June 14, 2019

File Path Selector
==================

VBA Blogs: File Path Selector
=============================

14 June 2019

_Welcome back to the VBA blog! This week we are going to cover something we had to do for one of our consulting jobs._

While working on a project we had to extract the file path of a file and display it in a cell in Excel; an example of what a file path is:

C:UsersSumProductDocumentsWorkExcel Summit

Essentially we wanted the file path to appear in a cell like this:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-710.jpg)

This can be done reasonably easily, just by copying and pasting the file path from Window’s File Explorer.

However, how do we automate it so the client can click on a button, and browse for a file from File Open Dialog Box, then have that file path and file appear in cell **B2**?

First give cell **B2** a range name of ‘File\_Path’.

Next we step into VBA:

**Sub** SelectFile()

**Dim** DialogBox **As** FileDialog

**Dim** path **As String**

**Set** DialogBox = Application.FileDialog(msoFileDialogFilePicker)

DialogBox.Title = “Select file for ” & FileType

DialogBox.Filters.Clear

DialogBox.Show

**If** DialogBox.SelectedItems.Count = 1 **Then**

    path = DialogBox.SelectedItems(1)

**End If**

ThisWorkbook.Names(“File\_Path”).RefersToRange.Value = path

**End Sub**

Let’s break down the code and explain what we did here, the first three lines of code:

**Sub** SelectFile()

**Dim** DialogBox **As** FileDialog

**Dim** path **As String**

starts the macro, and defines 2 variables we are going to use.

The next four lines:

**Set** DialogBox = Application.FileDialog(msoFileDialogFilePicker)

DialogBox.Title = “Select file for ” & FileType

DialogBox.Filters.Clear

DialogBox.Show

sets the DialogBox variable to use the File Open Dialog Box. The next few lines sets the title, clears filters, and displays the dialog box.

We had to include a line to clear filters, since the dialog box will inherit any other filters before.

The next three lines of code:

**If** DialogBox.SelectedItems.Count = 1 **Then**

    path = DialogBox.SelectedItems(1)

**End If**

is an **IF** loop, where VBA will check if we have selected a file, and when it does it will assign that file path to our ‘path’ variable.

The final 2 lines of code:

ThisWorkbook.Names(“File\_Path”).RefersToRange.Value = path

**End Sub**

assigns the range name File\_Path to equal our ‘path’ variable, then ‘End Sub’ ends the macro.

We can now create a Form Control Button and assign a macro to it:

![](<Base64-Image-Removed>)

Clicking on the ‘File Selector’ button will bring up our dialog box:

![](<Base64-Image-Removed>)

Allowing us to select a file, and Excel will retrieve the file path.

You can download an example file [here](https://sumproduct.com/assets/blog-pictures/2019/vba/fileselector/file-selector.xlsm)
.

Come back next week and we’ll expand on this macro.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/file-path-selector/#0)
    
*   [Register](https://sumproduct.com/thought/file-path-selector/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/file-path-selector/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/file-path-selector/#0)

[](https://sumproduct.com/thought/file-path-selector/#0 "close")

top