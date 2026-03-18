# Macros for Consolidating Projects

**Source:** https://edbodmer.com/consolidating-spvs-or-projects-with-macro

---

After creating the template file, you can create separate models for a lot of different projects which will become part of a consolidated portfolio.  The general trick is to make sure that all of the inputs for the model are driven by Each of the projects is defined by a name that becomes the sheet name.  You can then run or create a macro to copy the template sheet to another sheet. Once you have a lot of templates, you can consolidate the templates into a consolidation.  The consolidation uses the INDIRECT function to gather data from the different files. A few screenshots may give you an idea of how the file to consolidate different SPV’s works.  The first picture is intended to give you an idea of how the final consolidated process works.  This consolidation works by using the INDIRECT function to add together cash flows and balances from individual sheets. The second screenshot below shows how you can use the INDIRECT function. The INDIRECT function looks painful, but you can get the hang of it quickly.

.

To consolidate after running the macro, use an old fashioned formula from lotus that sums everything in the same cell over a range of sheets:

SUM(Start:End!A1)
-----------------

![](https://edbodmer.com/wp-content/uploads/2023/10/image-1-2048x1053.png)

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-1.jpg)

.

![](https://edbodmer.com/wp-content/uploads/2018/11/SPV-4-1.png)

.

.

Macro Examples to Consolidate Files
-----------------------------------

Some examples of macros that copy and paste the template are shown below. Besides defining the range names, you should be able to copy these macros into your sheet. You can also look at them and then try to write the macros by yourself.

.

Sub CreateTemplate()

lastsheet = Sheets.Count ' This is the number of the sheets to move the file to
currentsheet = ActiveSheet.Name
 ' This is where to go back to after finished

Newspv = row 
' This is a public variable from the multiple sheet row

Sheets("Master").Select ' Start with the TEMPLATE

Newname = Cells(Newspv, 2) 

' This is the PROJECT NAME that you put in the template sheet to define variables

Sheets("Template").Select ' Go to the template sheet
Sheets("Template").Copy After:=Sheets(lastsheet) 

' Copy the sheet to the end of the file

Sheets(lastsheet + 1).Select ' Go to the new sheet that you made
Sheets(lastsheet + 1).Name = Newname ' Put the name of the new sheet in the file
Cells(1, 2) = Newname

Sheets(currentsheet).Select ' Go back to the original sheet

End Sub

.

The next macro shows how you can consolidate differnt files. The above macro is only for one sheet.

Sub multiplesheet()

remember\_calc = Application.Calculation ' Will set calc to manual, so remember last value
Application.Calculation = xlCalculationManual ' Set to manual

Dim startrow, endrow As Single ' Need to dimension the variables that are defined by the input box

    startrow = InputBox("Ligne de début ?")   
    endrow = InputBox("Ligne de fin ?")

For row = startrow To endrow ' Loop around rows in the master page
        CreateTemplate ' Run the macro that creates a template
Calculate

Next row

Application.Calculation = remember\_calc ' re-set calculation to original value

End Sub

.

![](https://edbodmer.com/wp-content/uploads/2018/08/SolarSPV-Consolidated-4.jpg)

Macro with Screens that Show Which SPV is Being Created
-------------------------------------------------------

There is a lot of psychology in financial models surrounding the time it takes to complete a task. A few seconds of waiting for something to recalculate can seem like forever. In the code below I use two user forms that allows you to see the project being created without having to press a button. The first thing is to create userforms. To create the userform just go to VBA menu and insert as shown below. You should create two userforms and not one. This will allow you to see what is being created without stopping. You will have to use the MOD function.

![](https://edbodmer.com/wp-content/uploads/2022/02/image.png)

After inserting the userform, you can add labels and or text boxes and other items. You can put in pictures in the Userform and have the userform tell you what SPV you are created. You can do the same thing when you delete the files. The manner in which the userforms are shown is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2022/02/image-1.png)

The coding to allow this method is shown below. Note that the first thing to do is to use the userform1.label1.value = ” Project to change “. This will allow different items to be shown in the userform. You could add values to this or you could put in the time and you could use the FORMAT function in VBA which is similar to the TEXT function in excel. After you put in what you want in the userform, you need to include the statement DoEvents.

DoEvents

Then, to print the forms, you can use the MOD function in excel. This is important and will allow you to show one form, then remove the form and show the next form. Once you use the MOD function to show one of the two forms, you use the following code to show the userforms. Finally, at the end of the process, you should remove all of the userforms that you have made.

UserForm3.Show vbModeless  
Unload UserForm4

    Sub Create_Projects()
    '
    ' Create_Projects Macro
    '
    current_status = Application.Calculation
    Application.Calculation = xlCalculationManual
    
    Application.ScreenUpdating = False
    
    start_sheet = Sheets("Start").Index
    
    MsgBox " Copying Template to Projects After Sheet " & start_sheet & " Total Projects " & Range("num_projects")
                    
    Range("time_start") = Time
    
    Count = 1
    
    For sheet_num = 1 To Range("num_projects").Value
            
        If Range("project_select").Cells(1, sheet_num) = True Then
        
            Count = Count + 1
        
            UserForm3.Label2 = " Project " & sheet_num
            UserForm4.Label2 = " Project " & sheet_num
        
        newHour = Hour(Now())
        newMinute = Minute(Now())
        newSecond = Second(Now()) + 1
        waitTime = TimeSerial(newHour, newMinute, newSecond)
    '    Application.Wait waitTime
        
            DoEvents  ' This is necessary for displaying forms
        
            start_sheet = start_sheet + 1
                
            Sheets("Template").Select
            
            Range("project_name") = Range("projects").Cells(1, sheet_num)
            
            Application.Goto Reference:="copy_range"
            Selection.Copy
            
            Sheets(start_sheet).Select
            Sheets.Add
            
            Selection.PasteSpecial Paste:=xlPasteAll, Operation:=xlNone, SkipBlanks:= _
                False, Transpose:=False
            Selection.PasteSpecial Paste:=xlPasteColumnWidths, Operation:=xlNone, _
                SkipBlanks:=False, Transpose:=False
            ActiveWindow.DisplayGridlines = False
                                    
            On Error GoTo error1:
            ActiveSheet.Name = Range("project_name")
            
    '        Application.StatusBar = " Copying Project " & sheet_num
            
    '     MsgBox sheet_num Mod 2
         
         If Count Mod 2 = 0 Then                   ' Go between the two forms
            
            UserForm3.Show vbModeless
            Unload UserForm4
         Else
            
            UserForm4.Show vbModeless
            Unload UserForm3
         End If
            
            
        End If
    
    Next sheet_num
    
            Unload UserForm4
            Unload UserForm3
    
    Application.Calculation = current_status
    ' Application.StatusBar = False
    
            Sheets("Template").Select
            
            Range("project_name") = Range("projects").Cells(1, 1)
    
    Range("time_end") = Time
    
    Application.ScreenUpdating = True
    
    Sheets("Start").Select
    
    GoTo final_end:
    
    error1:
    
    MsgBox " Please make sure the sheets are deleted "
    
    final_end:
    
    End Sub
    

Playlist on Creating and Anlysing Portfolio of Projects or Assets
-----------------------------------------------------------------

I have put together some of the videos that I have made on creating a portfolio of projects or SPV’s. Some of the videos do not reflect the final method that I have created and may be repetitive. But if you want to torture yourself you can take a look. The various videos in this playlist include different examples of how to create a portfolio and write the macros.

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=15018&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9688&rand=0.1518078933253385)