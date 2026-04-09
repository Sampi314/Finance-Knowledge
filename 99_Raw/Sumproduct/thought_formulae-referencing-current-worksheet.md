# Formulae Referencing Current Worksheet

**Source:** https://sumproduct.com/thought/formulae-referencing-current-worksheet/

---

[Home](https://sumproduct.com/)

\> Formulae Referencing Current Worksheet

*   May 14, 2025

Formulae Referencing Current Worksheet
======================================

Looking at the possible errors that may occur when referencing other worksheets, and how to fix them.

Formulae Referencing Current Worksheet
======================================

Introduction
------------

_**Liam Bastick** highlights some of the common mistakes prevalent in financial modelling / Excel spreadsheeting. This article looks at an error even advanced modellers sometimes fall for._

Here’s an issue most of us notice everyday but don’t really _notice_. Imagine you are working in the worksheet ‘Sheet1’ of a particular workbook and you write a formula such as:

![](https://sumproduct.com/wp-content/uploads/2025/05/681758c0dd78c32f864330b4eed78115.jpg)

That’s right. Instead of using cell references on this worksheet, part-way through the calculation I have linked to another sheet (‘Sheet2’) and then linked back to this sheet again afterwards. The result is

**\=C8\*Sheet2!C6+Sheet1!C4**

I am sure we have all produced formulae such as this over the years.

As a model auditor though, I have a problem with this calculation – in particular the ‘Sheet1’ reference. The formula

**\=C8\*Sheet2!C6+C4**

is not only shorter but it’s easier to understand too. I _know_ it is a reference to a cell on this worksheet and that makes it easier to check and follow.

But there’s more to it than that.

Let me make a copy of ‘Sheet1’ as the formula is presently written. Copying the worksheet creates a new worksheet ‘Sheet1 (2)’ viz.

![](https://sumproduct.com/wp-content/uploads/2025/05/ba53e3fe0d9d1065fc3ec16f0a35fc6a.jpg)

Amazing, I know. I can rename the sheet, the formula will update and other than the fact the formula is longer than it needs to be necessarily (a bit like this sentence), it doesn’t appear to be a big deal. However, let me now copy the worksheet a different way…

In this instance, I am going to insert a new blank worksheet (say, ‘Sheet4’) and then simply copy and paste the entire ‘Sheet1’ worksheet in using **CTRL + C** and then **CTRL + V**:

![](https://sumproduct.com/wp-content/uploads/2025/05/74f0dfd947425ad0bb01d096132b8241.jpg)

The first thing you will notice is that my gridlines returned, but more importantly, take a look at my formula:

**\=C8\*Sheet2!C6+Sheet1!C4**

This is not referring to ‘Sheet4’ as expected. An end user may think it is correct too given the (correct) cell reference to ‘Sheet2’. You might argue that the formula is “ok” – just ensure the worksheet is copied correctly – but exactly how do you enforce the former method of sheet copying in a workbook when others may use it?

I find this Excel behaviour quite dangerous as it catches out accomplished modellers too. For example, I have seen highly experienced analysts build a template forecast sheet for a given business unit and then have it reviewed by model auditors – seemingly a very prudent course of action. Once checks have been completed, the sheet has been copied over and over again for a multitude of business units only to have certain calculations all reference the template sheet – something not picked up at the review stage.

Get into the practice of always removing sheet references to the current worksheet – then this cannot happen.

Excel’s built-in functionality ‘Find and Relace’ (**CTRL + H**) may be used (ensure ‘Workbook’ is selected as the ‘Within:’ category and that ‘Formulas’ is selected from the ‘Look in:’ drop down:

![](<Base64-Image-Removed>)

If you cannot see all of these options, click on the ‘Options’ button in the bottom right-hand corner of the dialog box.

Alternatively, you may use a macro instead. This is particularly useful if a worksheet is hidden and / or protected. A simple example of a macro is detailed below and is included in the [attached Excel file](https://sumproduct.com/assets/thought-files/formulae-referencing-in-the-current-worksheet/sp-removing-references-to-current-worksheet-example.xlsm)
.

Sub RemoveCurrentWorksheetReferencesFromFormulae()

Dim ws As Worksheet

Dim VisibleStatus As Variant

Dim ProtectStatus As Boolean

Dim ws\_NameReplace As String

Dim ws\_NameReplace2 As String

Dim dummyvariable As Variant

Dim NameSwap As String

NameSwap = “”

‘Speed up calculations by switching calculation and screen updating off

Dim InitialCalc As Variant

InitialCalc = Application.Calculation

Application.Calculation = xlCalculationManual

Application.ScreenUpdating = False

‘Reset Find/Replace behaviour to look at sheet only (not workbook)

Set dummyvariable = Worksheets(1).Range(“A1:A1”).Find(“Dummy”, LookIn:=xlValues)

‘Error handling – if there’s a problem, skip to the next worksheet

On Error GoTo NextWorksheet

‘Repeat the following code for each worksheet in the workbook

For Each ws In ActiveWorkbook.Sheets

    ‘Store whether worksheet is hidden or not, and unhide if necessary

    VisibleStatus = ws.Visible

    ws.Visible = xlSheetVisible

    ws.Activate

    ‘Store whether worksheet is protected or not, and unprotect if necessary

    ProtectStatus = ws.ProtectContents

    ws.Unprotect “”

    ‘Create variables to store the name of the worksheet in two different formulae forms – with/without space

    ws\_NameReplace = “‘” & ws.Name & “‘!”

    ws\_NameReplace2 = ws.Name & “!”

    ‘Replace if sheet name has a space

    ws.Cells.Replace What:=ws\_NameReplace, Replacement:=NameSwap, \_

        LookAt:=xlPart, SearchOrder:=xlByRows, MatchCase:=False, \_

        SearchFormat:=False, ReplaceFormat:=False

    ‘Replace if sheet name does not have a space

    ws.Cells.Replace What:=ws\_NameReplace2, Replacement:=NameSwap, \_

        LookAt:=xlPart, SearchOrder:=xlByRows, MatchCase:=False, \_

        SearchFormat:=False, ReplaceFormat:=False

    ‘Rehide the worksheet if it’s hidden

    ws.Visible = VisibleStatus

    ‘Reprotect the worksheet if it was protected previously

    If ProtectStatus = True Then

        ws.Protect

    End If

NextWorksheet:

Next ws

‘Reset calculation status

Application.Calculation = InitialCalc

Application.ScreenUpdating = True

End Sub

**_Word to the Wise_**

The macro may need to be amended if one or more worksheets is protected with a password or if a sheet is “very hidden”. No doubt someone will email me with some such instances!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/formulae-referencing-current-worksheet/#0)
    
*   [Register](https://sumproduct.com/thought/formulae-referencing-current-worksheet/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/formulae-referencing-current-worksheet/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/formulae-referencing-current-worksheet/#0)

[](https://sumproduct.com/thought/formulae-referencing-current-worksheet/#0 "close")

top