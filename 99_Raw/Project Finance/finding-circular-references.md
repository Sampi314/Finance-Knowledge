# Finding Circular References

**Source:** https://edbodmer.com/finding-circular-references

---

When you have circular references in a workbook, it may be difficult to find them. I have wrote some code that you can use to find the circular references. The way this should work is that you press the Initialise button and then you can press CNTL, ALT, r. This calls a program and then puts in the circular references into a new sheet as shown in the screenshot below. I also put comments in the cells that have the circular reference and display the circular reference. The process works using the find precedent account. At first I thought this would not be a very useful program but because excel is not very good at showing the circular references, I think it may be helpful.

![](https://edbodmer.com/wp-content/uploads/2020/09/image-120.png)

![](https://edbodmer.com/wp-content/uploads/2020/09/image-119.png)

![](https://edbodmer.com/wp-content/uploads/2020/09/image-118.png)

Makes a new sheet named circular references

    Sub Find_circular()
                 
    ' Before Loop Around Sheets
    
    
     MsgBox " This progam finds circular references and lists them on a sheet"
    
    '
    ' Msgbox is very helpful to show errors and understand what is going on
    '
                         
    comment_question = MsgBox("Do you want to include Comments on the Circular References?", vbYesNoCancel) ' 6 is yes and 7 is no
    
    '
    '  Input box
    '
    
     Dim start_sheet, end_sheet As Single
     
     start_sheet = InputBox("Number (not name) of Starting Sheet")
     end_sheet = InputBox("Number (not name) of Final Sheet")
                             
    '
    '  Cells, Sheets and Workbooks Add a sheet
    '
    
    Application.DisplayAlerts = False           ' You are going to delete a sheet and you don't want the are you sure question
    
     On Error Resume Next                        ' Error trapping can be a real pain
     
     Sheets("Circular References").Delete       ' May or may not exist
     Sheets.Add
     
     ActiveSheet.Name = "Circular References"   ' Re-name the sheet and understand that you have workbooks, sheets, and cells
      
     Count_of_circular_references = 4           ' Initialsise row number for output.  I do not bother defining it
        
    '
    ' Loop around all of the sheets
    '
    
    Dim cell_string1 As String
    
    For Sheet = start_sheet To end_sheet        ' For loop and other kinds of loops are key in VBA
    
        Sheets(Sheet).Select                    ' Sheets() with name or number
                
        base_sheet = ActiveSheet.Name
             
        Cells.Select                            ' Select all of the cells
        Selection.ClearFormats                 ' Clear all of the comments from the sheet
        ActiveSheet.Calculate
                    
        For Row = 1 To 20                               ' Get used to looping around rows and columns
            For col = 1 To 20
               
              cell_string = Cells(Row, col).Formula      ' Can get formula and address from a cell
              cell_address = Cells(Row, col).Address
                     
              cell_string1 = "'" & cell_string           ' So you can print out a formula
                                
                  If Left(cell_string, 1) = "=" Then
                                                      
                       On Error GoTo notcircular         ' BIG point.  When trap error, need to get out of the loop
                                                      
                        cell_precedent = Cells(Row, col).Precedents.Address
                       
    '
    ' This is the big formula to find if there are circular references
    ' If cell intersects with precedents, cell has circular reference.
    '
    
                        result = Intersect(Range(cell_address), ActiveSheet.Range(cell_precedent))
        
                        Count_of_circular_references = Count_of_circular_references + 1           ' count circular references in sheet
        
                        Sheets("Circular References").Cells(Count_of_circular_references, 3) = "  Circular Cell Address "
                        Sheets("Circular References").Cells(Count_of_circular_references, 4) = cell_address
                        Sheets("Circular References").Cells(Count_of_circular_references, 5) = "  Formula "
                        Sheets("Circular References").Cells(Count_of_circular_references, 6) = cell_string1
                        Sheets("Circular References").Cells(Count_of_circular_references, 7) = "  Precedents in Formula "
                        Sheets("Circular References").Cells(Count_of_circular_references, 8) = cell_precedent
                        Sheets("Circular References").Cells(Count_of_circular_references, 1) = "  Sheet Name  "
                        Sheets("Circular References").Cells(Count_of_circular_references, 2) = base_sheet
          
                        Cells(Row, col).Select                       ' Select the cells for colouring
                          
                           With Selection.Interior
                                .Pattern = xlSolid
                                .PatternColorIndex = xlAutomatic
                                .Color = 65535
                           End With
                                
                        If comment_question = 6 Then
                        
                            Cells(Row, col).AddComment
                            Selection.Comment.Visible = True
                            Selection.Comment.Text Text:="Circular Reference Formula:" & cell_string & Chr(10) & "Address" & cell_address & Chr(10) & _
                            " Precedents" & cell_precedent
                            
                        End If
        
                End If
                        
            Next col
            
    skipitem:
            
        Next Row
       
    Next Sheet
    
    ' Next Sheet
       
       
    Sheets("Circular References").Select
       
        Columns("A:H").Select
        Columns("A:H").EntireColumn.AutoFit
          
    Exit Sub
       
    notcircular:
       
    Resume skipitem:
       
    End Sub
    

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=11935&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10268&rand=0.6751160840075259)