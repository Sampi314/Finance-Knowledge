# Remove Password from VBA Project in Excel (2 Easy Ways)

**Source:** https://trumpexcel.com/excel-vba/remove-password

---

[Skip to content](https://trumpexcel.com/excel-vba/remove-password/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/remove-password/#below-title)

In one of my previous articles, I discussed how to [unprotect worksheets](https://trumpexcel.com/unprotect-excel-sheets-without-password/)
 in Excel, and many people asked me how they can do the same when they have an Excel file with a locked VBA project.

While a VBA project is slightly more complex to unlock without the password, it can be done.

In this article, I will show you two simple methods to remove the password from a locked VBA project in Excel. First I’ll show you a VBA code to do this, and then I’ll show you how to do this using a free hex editor tool.

_**[Click here to download the example file and follow along](https://www.dropbox.com/scl/fi/lp7dr7btj54t1c8joe0qb/Example.xlsm?rlkey=krnnrj5zog0r5hzft9daix0xl&dl=1)
**_

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/remove-password/#)

Better safe than sorry – Always create a backup copy of your file before trying any of the following methods.

Remove VBA Password with VBA Code (64 Bit Excel)
------------------------------------------------

_**Disclaimer**: I did not create this VBA code, and the credit for it goes to a Vietnamese developer, Siwtom (which was further refined by another user). I copied this code from the following link – [https://stackoverflow.com/questions/1026483/is-there-a-way-to-crack-the-password-on-an-excel-vba-project/31005696#31005696](https://stackoverflow.com/questions/1026483/is-there-a-way-to-crack-the-password-on-an-excel-vba-project/31005696#31005696)
_

Below is the VBA code you can use in **64-bit Excel** to unlock VBA projects and remove passwords:

    Private Const PAGE_EXECUTE_READWRITE = &H40
    Private Declare PtrSafe Sub MoveMemory Lib "kernel32" Alias "RtlMoveMemory" _
        (Destination As LongPtr, Source As LongPtr, ByVal Length As LongPtr)
    Private Declare PtrSafe Function VirtualProtect Lib "kernel32" (lpAddress As LongPtr, _
        ByVal dwSize As LongPtr, ByVal flNewProtect As LongPtr, lpflOldProtect As LongPtr) As LongPtr
    Private Declare PtrSafe Function GetModuleHandleA Lib "kernel32" (ByVal lpModuleName As String) As LongPtr
    Private Declare PtrSafe Function GetProcAddress Lib "kernel32" (ByVal hModule As LongPtr, _
        ByVal lpProcName As String) As LongPtr
    Private Declare PtrSafe Function DialogBoxParam Lib "user32" Alias "DialogBoxParamA" (ByVal hInstance As LongPtr, _
        ByVal pTemplateName As LongPtr, ByVal hWndParent As LongPtr, _
        ByVal lpDialogFunc As LongPtr, ByVal dwInitParam As LongPtr) As Integer
    Dim HookBytes(0 To 11) As Byte
    Dim OriginBytes(0 To 11) As Byte
    Dim pFunc As LongPtr
    Dim Flag As Boolean
    Private Function GetPtr(ByVal Value As LongPtr) As LongPtr
    GetPtr = Value
    End Function
    Public Sub RecoverBytes()
    If Flag Then MoveMemory ByVal pFunc, ByVal VarPtr(OriginBytes(0)), 12
    End Sub
    Public Function Hook() As Boolean
    Dim TmpBytes(0 To 11) As Byte
    Dim p As LongPtr, osi As Byte
    Dim OriginProtect As LongPtr
    Hook = False
    
    #If Win64 Then
        osi = 1
    #Else
        osi = 0
    #End If
    pFunc = GetProcAddress(GetModuleHandleA("user32.dll"), "DialogBoxParamA")
    If VirtualProtect(ByVal pFunc, 12, PAGE_EXECUTE_READWRITE, OriginProtect) <> 0 Then
        MoveMemory ByVal VarPtr(TmpBytes(0)), ByVal pFunc, osi + 1
        If TmpBytes(osi) <> &HB8 Then
            MoveMemory ByVal VarPtr(OriginBytes(0)), ByVal pFunc, 12
            p = GetPtr(AddressOf MyDialogBoxParam)
            If osi Then HookBytes(0) = &H48
            HookBytes(osi) = &HB8
            osi = osi + 1
            MoveMemory ByVal VarPtr(HookBytes(osi)), ByVal VarPtr(p), 4 * osi
            HookBytes(osi + 4 * osi) = &HFF
            HookBytes(osi + 4 * osi + 1) = &HE0
            MoveMemory ByVal pFunc, ByVal VarPtr(HookBytes(0)), 12
            Flag = True
            Hook = True
        End If
    End If
    End Function
    
    Private Function MyDialogBoxParam(ByVal hInstance As LongPtr, _
        ByVal pTemplateName As LongPtr, ByVal hWndParent As LongPtr, _
        ByVal lpDialogFunc As LongPtr, ByVal dwInitParam As LongPtr) As Integer
    If pTemplateName = 4070 Then
        MyDialogBoxParam = 1
    Else
        RecoverBytes
        MyDialogBoxParam = DialogBoxParam(hInstance, pTemplateName, _
            hWndParent, lpDialogFunc, dwInitParam)
        Hook
    End If
    End Function
    
    Sub UnprotectVBA()
        If Hook Then
            MsgBox "VBA Project is unprotected!", vbInformation, "VBA Unlocked"
        End If
    End Sub

If using 32-bit Excel, you can try using the code here. Since I have 64-bit Excel, I have not tested the code for 32-bit Excel.

[_Here is how you can check what version of Excel you have_](https://trumpexcel.com/excel-version/)

Below are the steps to use this VB macro code to unlock VBA projects:

1.  Keep the Excel file open that has the VBA project that you want to unlock
2.  Open a new Excel file
3.  Open the VB editor in this new Excel file (You can use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
     ALT + F11, or you can go to the developer tab and then click on the Visual Basic icon)
4.  In the VB editor, insert a new module (this should be for this new Excel file we have opened that does not have the locked VBA project)

![Insert a new module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20269'%3E%3C/svg%3E)

5.  Copy and paste the above VBA code into this newly inserted module.

![Copy paste the VBA code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20338'%3E%3C/svg%3E)

6.  Place the cursor anywhere in the UnprotectVBA subroutine.

![Place the cursor in the code you want to run](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20338'%3E%3C/svg%3E)

7.  Run the macro code. You can do this by pressing the F5 key on your keyboard or by clicking on the run macro icon in the VB editor toolbar.

As soon as you run the macro, you should see a message box shown below, that says – _VBA Project is unprotected!_

![VBA project unlocked message box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20290%20208'%3E%3C/svg%3E)

Close the message box and go back into the VB editor, and the VB project should now be unlocked.

I tried this on my system with a couple of different locked VBA project Excel files, and it worked. However, some users have reported that it didn’t work for them. So give this a try, and if it doesn’t work, you can use the next method, which uses a Hex Editor to unprotect a VBA project.

Remove VBA Password HEX Editor
------------------------------

Another free and easy way to remove the VBA password from your Excel file is using a HEX editor.

A HEX Editor is a free lightweight third-party tool that allows you to edit the binary data that makes up a VBA project in Excel.

In this method, we open the VBA project within the HEX editor and replace the password that we do not know with the password that we do know so that we can unlock the project with that known password.

You can download the hex editor using the [following link](https://download.cnet.com/hxd-hex-editor/3000-2352_4-10891068.html)
 (takes you to CNET website)

Below are the steps to replace the password using the HEX Editor:

1.  Go to the folder where you have the Excel file with the VBA project that you want to unlock.
2.  Change the file extension from .XLSM to .ZIP. This will convert your Excel file into a zip folder.

![Converted xlsm file to zip file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20350'%3E%3C/svg%3E)

3.  Open the zip folder, locate the XL folder, and double-click on it to open it.

![Find XL Folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20178'%3E%3C/svg%3E)

4.  Locate the vbaProject.bin file, copy it, and paste the copy outside of the zip folder (so we can make changes to this file).

![Copy VBProject Bin file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20599%20213'%3E%3C/svg%3E)

5.  Open the HEX editor
6.  Open the vbaProject.bin file in the HEX editor. You’ll see the binary information of the file being displayed in the HEX editor.

![File opened in Hex Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20394'%3E%3C/svg%3E)

7.  Hold the Control key and press the F key. This will open the Find dialog box.

![Find dialog box in Hex Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20503%20365'%3E%3C/svg%3E)

8.  Search for the term **DPB** (enter DPB in the Find field and click OK). You notice that there is a binary code after the DPB within quotes (highlighted in red below).

![Code in double codes to unlock VBA password](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20429'%3E%3C/svg%3E)

9.  Replace the code in the double quotes with _0A08A6B1B6CEB6CE4932B7CE4B63A66D37B84BA3D4BAD58A6B495254585A5D3D675777675D_

If the length of the code that is already there being displayed in the Hex editor is different than the one that I have provided above, add a couple of zeros to the above code to make the length similar.

10.  Save the file and close the hex editor.
11.  Copy the vbaProject.bin file in which we have made the changes, Then go back into the xl folder within the zip folder, and replace the original vbaProject.bin file with the one you copied.
12.  Change the extension of the folder from .zip to .xlsm
13.  Open the Excel file and then open the VB Editor.
14.  Enter 123 as the password to unlock the VB Project.

You can keep the VB project locked and use 123 as the password, or you can first unlock the VB project and then remove the password altogether.

So, these are two simple methods you can use to remove the password from a VBA project quickly. Try using the VBA code first, and if for some reason that doesn’t work, then you can try the hex editor method.

I hope you found this article helpful. If you know of any other method that can be used to unprotect locked VB projects, do share it with us all in the comment section.

**Other Excel articles you may also like:**

*   [Excel VBA](https://trumpexcel.com/excel-vba/)
    
*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    
*   [Protect and Unprotect Sheet Using VBA](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [How to Hide a Worksheet in Excel (that can not be unhidden)](https://trumpexcel.com/hide-worksheet/)
    
*   [How to Convert Excel to PDF Using VBA](https://trumpexcel.com/convert-excel-to-pdf/)
    
*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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