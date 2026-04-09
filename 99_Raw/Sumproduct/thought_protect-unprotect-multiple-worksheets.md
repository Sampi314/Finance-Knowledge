# Protect / Unprotect Multiple Worksheets

**Source:** https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/

---

[Home](https://sumproduct.com/)

\> Protect / Unprotect Multiple Worksheets

*   May 14, 2025

Protect / Unprotect Multiple Worksheets
=======================================

Wearing protection: how to get Excel to actually do what you want.

Wearing Protection
==================

Sometimes, Excel just isn’t as versatile as you’d like. Some of us find protection particularly wearing. In this article, we present an easier way to protect / unprotect multiple worksheets. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

Is there a way to protect / unprotect multiple worksheets in Excel at the same time?

Advice
------

I fear this article might give rise to a hornet’s nest of similar queries. Excel is a highly flexible piece of software, but sometimes it’s not all the modeller might hope for. Some readers will already have noted that some operations cannot be applied across multiple worksheets, with the application of protection just one item in that list.

However, before I address the above query, let me first summarise how protection works in Excel.

### The Three Levels of Protection in Excel

If you open any workbook and select any cell in a randomly selected worksheet, you will note that the cell is “locked” by default (simply go to the cell, then depress **CTRL + 1** and select the ‘Protection’ tab), viz.

![](https://sumproduct.com/wp-content/uploads/2025/05/image-01-format-cells-locked-1-.gif)

Cells are locked by default

As the narrative in the dialog box notes, locking cells has no effect until the worksheet is protected. This is simple to prove: all cells are locked by default yet anyone can still edit any cell at will.

In order to protect the contents, you have to protect the worksheet (**ALT + T + P + P** in all versions of Excel, otherwise ‘Home’ tab of the Ribbon, then select ‘Format’ in the ‘Cells’ group and then select ‘Protect Sheet…’ in Excel 2007 onwards). For later versions of Excel, this will promote the following dialog box:

viz.

![](<Base64-Image-Removed>)

Protect Sheet Dialog Box

Personally, I am not keen on using passwords (other than ‘\*\*\*\*’ so that I can see what I am typing!). This is because Excel is not secure software and more often than not, it’s the modeller who goes looking for a hack when they realise they have forgotten the password.

Nonetheless, this remains in the realm of the end user and may be entered if desired. It is only when the sheet has been protected that locked cells are protected. Other actions may or may not be allowed by checking the various check boxes displayed above.

But you can still delete this worksheet – even if it has been password protected. I don’t know about you, but that’s not my definition of “protected”! In order to protect sheets (e.g. prevent sheets being deleted, hidden or moved), you actually need to protect the workbook (**ALT + T + P + W** in all versions of Excel):

![](<Base64-Image-Removed>)

Protect Workbook Dialog Box

These are the three stages of protection in Excel: **cell**, **worksheet** and **workbook**.

### The Basic Problem

The actual issue is that you cannot protect more than one sheet at a time in Excel. If you have many sheets in Excel, this can become very time consuming if you wish to protect all sheets. The solution is to resort to macros.  
I have explained how to add macros before and to ensure that the workbook is saved as a macro-enabled workbook (please see either the article on [locating links](https://www.sumproduct.com/thought/locating-links-2)
 or the article on [automating a Table of Contents](https://www.sumproduct.com/thought/automating-a-table-of-contents)
 for more details).

To protect all sheets, I suggest the following code in the Visual Basic Editor (**ALT + F11**):

![](<Base64-Image-Removed>)

Protect All Sheets Macro

**Sub** ProtectAll()

**Dim** wSheet **As** Worksheet

**Dim** Pwd **As String**

Pwd = InputBox(“Enter your password to protect all worksheets”, “Password Input”)

**For Each** wSheet **In** Worksheets

wSheet.Protect Password:=Pwd, DrawingObjects:=**True**, Contents:=**True**, Scenarios:=**True**, \_

AllowFormattingColumns:=**True**, AllowFormattingRows:=**True**

**Next** wSheet

**End Sub**

I have added additional functionality (e.g. formatting of columns and rows) so that you can see how you can modify what may be adjusted once all the worksheets have been protected. The best way to learn VBA is to play with it – and try not to tear your hair out!

To unprotect all sheets, I suggest the following:

![](<Base64-Image-Removed>)

Unprotect All Sheets Macro

**Sub** UnProtectAll()

**Dim** wSheet **As** Worksheet

**Dim** Pwd **As String**

Pwd = InputBox(“Enter your password to unprotect all worksheets”, “Password Input”)

**On Error Resume Next**

**For Each** wSheet **In** Worksheets

wSheet.Unprotect Password:=Pwd

**Next** wSheet

**If** Err <> 0 **Then**

MsgBox “You have entered an incorrect password. All worksheets could not ” & \_

“be unprotected.”, vbCritical, “Incorrect Password”

**End If**

**On Error GoTo 0**

**End Sub**

Readers may note for this example I have included an error trap to capture what happens if you put the wrong password in. I always recommend allowing for user error!

These macros can then be run from the ‘Developer’ tab. This tab is not visible by default but can be displayed but can be displayed (please consult the ‘Help’ guide as this varies between versions of Excel).

### Word to the Wise

You can get quite clever regarding what functionalities are allowed in the protected worksheets. The [attached Excel file](https://sumproduct.com/assets/thought-files/n-z/sp-basic-protect-all-sheets-example.xls)
 provides a very simple example regarding how this might work in practice.

Regarding this month’s Excel file, I would like to emphasise this file may not work with all versions of Excel. Caveat emptor – it is provided in good faith and should work for most readers. However, I do not have time to enter into correspondence for those unlucky enough to find this file does not appear to work as intended. This is why I steer away from macros when I can!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/#0)
    
*   [Register](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/#0)

[](https://sumproduct.com/thought/protect-unprotect-multiple-worksheets/#0 "close")

top