# VBA Blogs: File Path Selector confined to CSV

**Source:** https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: File Path Selector confined to CSV

*   June 20, 2019

VBA Blogs: File Path Selector confined to CSV
=============================================

VBA Blogs: File Path Selector confined to CSV
=============================================

21 June 2019

_Welcome back to the VBA blog! This week we are going to expand on our blog from last week, relating to file path selectors._

Last week, we went over how to extract the file path of any other file and display it in a specific cell.

What if we wanted to set a restriction to the types of files that could be selected? For this example, we will limit the files that can be selected to be a csv file.

![](<Base64-Image-Removed>)

We have altered our code from last week:

**Sub** SelectFile()

**Dim** DialogBox **As** FileDialog

**Dim** path **As String**

**Set** DialogBox = Application.FileDialog(msoFileDialogFilePicker)

DialogBox.Title = “Select file for ” & FileType

**DialogBox.Filters.Add “Comma-Separated Value Files”, “\*.csv”, 1**

DialogBox.Show

**If** DialogBox.SelectedItems.Count = 1 **Then**

    path = DialogBox.SelectedItems(1)

**End If**

ThisWorkbook.Names(“File\_Path”).RefersToRange.Value = path

**End Sub**

The code remains the same as last week’s blog except for the changes in the Filters syntax. Let’s have a closer look at the code listed below:

DialogBox.Filters.Add “Comma-Separated Value Files”, “\*.csv”, 1

This part of syntax confines the type of file selected only to CSV file as shown below. Other file types will not be able to be selected in this case.

![](<Base64-Image-Removed>)

After altering the code, we can use the same ‘File Selector’ button as before to run the macro:

![](<Base64-Image-Removed>)

Clicking on the ‘File Selector’ button will bring up the following dialog box:

![](<Base64-Image-Removed>)

This allows us to select a CSV file retrieve the file path to cell **B2**.

You can download an example file [here](https://sumproduct.com/assets/blog-pictures/2019/vba/fileselector/file-selector.xlsm)
.

Come back next week for more VBA.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/#0)

[](https://sumproduct.com/blog/vba-blogs-file-path-selector-confined-to-csv/#0 "close")

top