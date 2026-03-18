# Report at the Double

**Source:** https://sumproduct.com/thought/report-at-the-double/

---

[Home](https://sumproduct.com/)

\> Report at the Double

*   May 14, 2025

Report at the Double
====================

How to use macros to copy report pages to a new document without creating links to confidential data.

Report at the Double
====================

This article considers how to automatically produce a report for third parties without revealing confidential information. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

I have to produce reports which refer to confidential data that I don’t want end users to see. I am planning to copy and paste the relevant pages into a separate report, but this could be a long laborious process given I will have to create this report regularly and it needs to have quite a few worksheets. Any suggestions?

Advice
------

Whenever you think of tedious, repetitive tasks, try to think about automation, i.e. macros. Copying and pasting between workbooks is fairly trivial (simply set up Macro Recorder and copy a sheet between two workbooks).

Therefore, rather than produce the shortest article yet, I have decided to extend the idea to show how this becomes an issue when copying multiple sheets.

Let’s start from the beginning.

To record a Macro in Excel 2007 onwards, if you are a member of the point and click brigade you are going to need show the Developer tab on the Ribbon:

*   **Excel 2007**: Click on the ‘Office’ button, then click on the ‘Excel Options’ button (**ALT + T + O**), select ‘Popular’ in the left hand column of the resultant ‘Excel Options’ dialog box and then activate the third check box, ‘Show Developer tab in the Ribbon’ and click ‘OK’
*   **Excel 2010 and Excel 2013**: Click on the ‘File’ tab in the Ribbon, then select ‘Options’ from the left hand column (again, **ALT + T + O**). Then, select ‘Customize Ribbon’ in the left hand column of the resultant ‘Excel Options’ dialog box and then in the right-hand window, check the ‘Developer’ box and click ‘OK’

![](https://sumproduct.com/wp-content/uploads/2025/05/4e97d0d1a3b088b14b643aa9f37a38e6.jpg)

Recording a Macro from the Ribbon

If all of this seems like a lot of hassle, the Excel 2003 keystrokes (**ALT + T + M + R**) still work, even with the Developer Tab not visible.

Once activated, enter appropriate details in the activated dialog box:

![](https://sumproduct.com/wp-content/uploads/2025/05/11d36a28bbebff0dc2da08ff5e5f95c6.jpg)

Record Macro dialog box

Macros can be activated with **CTRL** plus a character (to be specified) (see graphic above) and can be stored in the current workbook (“This Workbook”), a new workbook, another open workbook (sometimes) or something called your “Personal Macro Workbook”.

By default, when you first create a macro in a workbook, it works only in that workbook. To make your macros available every time you open Excel, you should create them in a workbook called **Personal.xlsb**. This is a hidden workbook stored on your computer, which opens every time you open Excel and is your “Personal Macro Workbook”, cited above. It should be noted that this feature is not available in Office on a Windows RT PC.

Once you click ‘OK’ everything you do in Excel is recorded (just don’t close the workbook!) until you stop recording:

![](https://sumproduct.com/wp-content/uploads/2025/05/e973bb2ebb12d5ea80b3fbb9e61efc47.jpg)

Stop Recording a Macro

Using this technique, we can record a macro where we copy a worksheet to a new workbook. Depending upon how you do it, the macro might look something like this in the Visual Basic Editor (**ALT + F11**) and then find the relevant module located in the file you chose to store the macro:

![](<Base64-Image-Removed>)

Simple Copy and Paste to a New Workbook

So far, so good, so what..?

Our problem here is that we want to copy multiple sheets across to multiple sheets in a new workbook. For this example, we will assume all elements copied are to be pasted as values and the sheet tab names are retained, i.e. we will be taking the values only in order to preserve the confidentiality and nature of the original underlying data. This will also prevent the annoying prompt upon opening asking users to update links too.

If we use the above technique for copying and pasting multiple sheets, things start going awry:

![](<Base64-Image-Removed>)

Attempting to Copy and Paste Multiple Worksheets to a New Workbook

Don’t worry if you can’t quite read this code: the point I am trying to make here is that it doesn’t take much to generate a program Tolstoy would have been proud of.

If you try this, you might find your macro is actually even longer and cites the name of the new workbook (e.g. “Book 2?) if you copy worksheets across individually (in my example I used ‘Move or Copy’ and copied all of the sheets I required in one go). If you do get this, this is a particularly inflexible macro which may not work if Book 2 is already in use / has been defined.  
Indeed, the macro above is “clunky” (that’s a technical term) and is going to get very long quite quickly if I require several more worksheets to be copied.

However, the aim of recording macros is usually to get an idea how to modify the code generated into your own personal work of art. With a little perseverance and some VBA knowledge, it’s just a proverbial hop, skip and a jump into something a little more workable.

The following was typed directly into the Visual Basic Editor revising the code from the earlier examples:

![](<Base64-Image-Removed>)

Suggested Code

The macro code:

**Option Explicit**

**Sub** MasterMacro()  
**Dim** wbNew **As** Workbook, wbThis **As** Workbook

_‘Define the two workbooks in question  
_**Set** wbThis = ThisWorkbook  
**Set** wbNew = Workbooks.Add

**Call** MoveSheetsAndHardcode(“Output1”, wbNew, wbThis)  
**Call** MoveSheetsAndHardcode(“Output2”, wbNew, wbThis)  
Call MoveSheetsAndHardcode(“Output3”, wbNew, wbThis)

Application.CutCopyMode = **False**

**End Sub**

**Sub** MoveSheetsAndHardcode(strSheetName **As String**, wbNew **As** Workbook, wbThis **As** Workbook)

_‘Copy source sheet to new workbook  
_wbThis.Worksheets(strSheetName).Copy Before:=wbNew.Sheets(wbNew.Sheets.Count)

_‘Hardcodes sheets in new workbook  
_**With** wbNew.Worksheets(strSheetName)  
.Cells.Copy  
.Cells.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks \_  
:=**False**, Transpose:=**False  
****End With**

Range(“A1”).Select

**End Sub**

There are actually two macros, **MasterMacro**, which keeps running a subroutine **MoveSheetsAndHardcode**, so that unnecessary repetition is avoided. To use this code for your own files, note that the first macro uses the subroutine three times copying the arbitrarily named worksheets **Output1**, **Output2** and **Output3**. Simply change these references to the worksheet names as they are depicted on the sheet tab. If you need to copy more worksheets, simply add lines to **MasterMacro** using the syntax

**Call** MoveSheetsAndHardcode(“OutputSheetName”, wbNew, wbThis)

To run this code, exit the Visual Basic Editor (simply close the main window) and then:

### Excel 2003 and earlier

*   Go to Tools -> Macro -> Macros… (**ALT + F8**)

### Excel 2007 and later

*   Go to the ‘Developer’ tab in the Ribbon;and
*   In the ‘Code’ group, click on ‘Macros’
*   Alternatively, ignore all of the above and simply use the keyboard shortcut **ALT + F8**

This will then bring up the following dialog box:

![](<Base64-Image-Removed>)

Run Macro dialog box

Select the macro ‘**MasterMacro**‘ macro and click on the ‘Run’ button. This will execute the macro and copy the sheets accordingly.

### Word to the Wise

Regarding this article’s Excel file, I would like to emphasise this file may not work with all versions of Excel. Caveat emptor – it is provided in good faith and should work for most readers. However, I do not have time to enter into correspondence for those unlucky enough to find this file does not appear to work as intended.

The macro is simple and a more complex version is included in the [attached Excel file](https://sumproduct.com/assets/thought-files/n-z/sp-copy-paste-macro-example.xls)
. If alternative color palettes or Themes are used in the source workbook, colours may not copy as intended between workbooks. This file allows for such issues. I’d like to offer special thanks to fellow Excel MVP Zack Barresse for coding this annoying complication.

Make sure you save the workbook as a macro enabled workbook or all will be for nought!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/report-at-the-double/#0)
    
*   [Register](https://sumproduct.com/thought/report-at-the-double/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/report-at-the-double/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/report-at-the-double/#0)

[](https://sumproduct.com/thought/report-at-the-double/#0 "close")

top