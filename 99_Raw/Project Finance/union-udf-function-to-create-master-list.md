# Union UDF & Master List

**Source:** https://edbodmer.com/union-udf-function-to-create-master-list

---

The UNION function allows you to take multiple lists in an excel file with different orders of names and then put them into a common list. The union function allows you to put together financial statements with different titles in different years.  Using this method you can make the process of creating a historic database of financial statements easier. This page includes demonstrates how to use the function and includes technical documentation of the function. To access the UNION function you need the read pdf file open.  You can then copy the function into your file using the ALT F8 method as any UDF function.  The Read Pdf to Excel file can be downloaded by pressing the button below.  This page also covers reading data from the SEC website into excel for which you can use an alternative file.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

**[Asian Version of Excel File the Reads PDF (or Internet) to Excel with Macros that are Implemented with SHIFT CNTL Afor](https://edbodmer.com/wp-content/uploads/2018/10/Read-PDF-to-Excel-Asian.xlsm)
**

**[File with Macros that Format Data Copied into and Excel File from the U.S.Securities and Exchange Website](https://edbodmer.com/wp-content/uploads/2019/04/Scenario-Reporter.xlsm)
**

Using the Union Function to Put Together Financial Statements
-------------------------------------------------------------

Like many functions, the UNION function is an array function.  This means the output does not go into one cell but rather into a series of cells.  To operate the UNION function you should leave a long space and then select the long space.  After that, you begin typing the UNION function.  Then like with any function press the tab key.  After that, you can select multiple other columns (or rows) that will be combined into one single column,  At the end press the SHIFT, CNTL, ENTER sequence.

Here is a step by step review of the union function:

Step 1: Insert some columns at the left of the sheet

Step 2: Use the Union Function which is an array function (SHIFT, CNTL, ENTER)

Step 3: Match the Cell from the UNION function list with original list of names for the year and put 0 at the end

Step 4: Combine the INDEX with the MATCH function and you will have a consistent set of columns

The video below is lengthy and bad but it goes through this.

The second video demonstrates the VBA code that is used to create the UNION function.  This video is more technical and has various sort routined.

.

Technical Details of the Union Function
---------------------------------------

The insert below shows the code for creating the UNION Function.  You can copy this function to your sheets like you can copy any UDF.  Just select the code below and copy it to a VBA module.

The code for this union function is shown in the box below:

Function union(range1, range2, Optional range3, Optional range4, Optional range5, Optional range6, Optional range7, \_
Optional range8, Optional range9, Optional range10, Optional range11, Optional range12) As Variant


Dim output(1000) As Variant ' output variables - for aggregate list
Dim output1(1000) As Variant ' variable with code number to maintain order
Dim output3(1000, 1) As Variant ' ultimate output variable


GoTo missing\_test:
missing\_return:

GoTo num\_range: ' Get the total number for the loop through counting variables
num\_range\_return: ' Where to come back after getting numbers

GoTo accumulate:
accumulate\_return:


' sort the output array without the numbers so that can remove duplicates

For i = 1 To tot\_num

For j = i To tot\_num

If output(j) < output(i) Then

str1 = output(i)
str2 = output(j)

output(i) = str2
output(j) = str1

str\_1 = output1(i)
str\_2 = output1(j)

output1(i) = str\_2
output1(j) = str\_1

End If
Next j
Next i


' eliminate duplicates from the output array without the numbers

Count = 2
For i = 2 To tot\_num Step 1 ' master list

If output(Count) = output(Count - 1) Then ' if last value = prior value

For j = Count To tot\_num Step 1 ' push everything up
If j > 1 Then output(j - 1) = output(j)
If j > 1 Then output1(j - 1) = output1(j)
Next j

Count = Count - 1

End If

Count = Count + 1
Next i

revised\_tot = Count - 1


' re-sort with number


For i = 1 To revised\_tot

For j = i To revised\_tot

If output1(j) < output1(i) Then

str1 = output1(i)
str2 = output1(j)

output1(i) = str2
output1(j) = str1

str\_1 = output(i)
str\_2 = output(j)

output(i) = str\_2
output(j) = str\_1

End If

Next j

Next i


For i = 1 To revised\_tot
output3(i, 1) = output(i)
Next i

union = output3
Exit Function

missing\_test:

' Create test for optional variables when you enter a variable


range3\_option = True
range4\_option = True
range5\_option = True
range6\_option = True
range7\_option = True
range8\_option = True
range9\_option = True
range10\_option = True
range11\_option = True
range12\_option = True

If IsMissing(range3) Then range3\_option = False
If IsMissing(range4) Then range4\_option = False
If IsMissing(range5) Then range5\_option = False
If IsMissing(range6) Then range6\_option = False
If IsMissing(range7) Then range7\_option = False
If IsMissing(range8) Then range8\_option = False
If IsMissing(range9) Then range9\_option = False
If IsMissing(range10) Then range10\_option = False
If IsMissing(range11) Then range11\_option = False
If IsMissing(range12) Then range12\_option = False

GoTo missing\_return:

' count the number in the series

num\_range:

num1 = range1.Count
num2 = range2.Count

If range3\_option Then num3 = range3.Count
If range4\_option Then num4 = range4.Count
If range5\_option Then num5 = range5.Count
If range6\_option Then num6 = range6.Count
If range7\_option Then num7 = range7.Count
If range8\_option Then num8 = range8.Count
If range9\_option Then num9 = range9.Count
If range10\_option Then num10 = range10.Count
If range11\_option Then num11 = range11.Count
If range12\_option Then num12 = range12.Count

tot\_num = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12
revised\_tot = tot\_num


GoTo num\_range\_return:

accumulate:

' Accumulate the data into output and output1


For i = 1 To num1 ' accumulate into a single array
Count = Count + 1

output1(Count) = i + 100 & " " & range1(i) ' use code numbers to maintain the order of the numbers
output(Count) = range1(i) ' make a big array with all of the ranges

Next i

For i = 1 To num2
Count = Count + 1

output1(Count) = i + 100 & " " & range2(i)
output(Count) = range2(i)

Next i

If range3\_option Then
For i = 1 To num3
Count = Count + 1

output1(Count) = i + 100 & " " & range3(i)
output(Count) = range3(i)
Next i
End If

If range4\_option Then ' only do when passed the missing test for range
For i = 1 To num4 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range4(i) ' use code numbers to maintain the order of the numbers
output(Count) = range4(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range

If range5\_option Then ' only do when passed the missing test for range
For i = 1 To num5 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range5(i) ' use code numbers to maintain the order of the numbers
output(Count) = range5(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range6\_option Then ' only do when passed the missing test for range
For i = 1 To num6 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range6(i) ' use code numbers to maintain the order of the numbers
output(Count) = range6(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range7\_option Then ' only do when passed the missing test for range
For i = 1 To num7 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range7(i) ' use code numbers to maintain the order of the numbers
output(Count) = range7(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range8\_option Then ' only do when passed the missing test for range
For i = 1 To num8 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range8(i) ' use code numbers to maintain the order of the numbers
output(Count) = range8(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range9\_option Then ' only do when passed the missing test for range
For i = 1 To num9 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range9(i) ' use code numbers to maintain the order of the numbers
output(Count) = range9(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range10\_option Then ' only do when passed the missing test for range
For i = 1 To num10 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range10(i) ' use code numbers to maintain the order of the numbers
output(Count) = range10(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range11\_option Then ' only do when passed the missing test for range
For i = 1 To num11 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range11(i) ' use code numbers to maintain the order of the numbers
output(Count) = range11(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


If range12\_option Then ' only do when passed the missing test for range
For i = 1 To num12 ' accumulate into an aggregate single array
Count = Count + 1

output1(Count) = i + 100 & " " & range12(i) ' use code numbers to maintain the order of the numbers
output(Count) = range12(i) ' make a big array with all of the ranges

Next i
End If ' end of missing test on range


tot\_num = Count
revised\_tot = tot\_num

GoTo accumulate\_return:

End Function


Sub A\_union\_function\_help()

UserForm11.Show


GoTo skip
MsgBox \_
Chr(1) & Chr(2) & Chr(3) & Chr(4) & Chr(5) & Chr(6) & Chr(7) & Chr(8) & Chr(9) & Chr(10) & Chr(11) & " Test Chars " & Chr(13) & Chr(13) & Chr(13) & \_
Chr(11) & Chr(12) & Chr(13) & Chr(14) & Chr(15) & Chr(16) & Chr(17) & Chr(18) & Chr(19) & Chr(20) & Chr(21) & " Find the A\_function\_help macro and copy entire module to you workbook" & Chr(13) & Chr(13) & Chr(13) & \_
Chr(21) & Chr(22) & Chr(23) & Chr(24) & Chr(25) & Chr(26) & Chr(27) & Chr(28) & Chr(29) & Chr(30) & Chr(31) & " Find the A\_function\_help macro and copy entire module to you workbook" & Chr(13) & Chr(13) & Chr(13) & \_
" Please make sure the Option Base 1 is at the top " & Chr(13) & Chr(13) & Chr(13) & \_
" To Sort, for now you must copy and paste special " & Chr(13) & Chr(13) & Chr(13) & \_
" There is an INDMAT -- Index and Match Function. This can be used with entire columns or rows" & Chr(13) & Chr(13) & Chr(13)

skip:

MsgBox \_
" Find the UNION functions (See the Button Below). COPY entire module to you workbook" & Chr(13) & Chr(13) & Chr(13) & \_
" Make sure the Option Base 1 is at the top " & Chr(13) & Chr(13) & Chr(13) & \_
" Use the UNION function to get a TITLE List -- Make Similar Titles " & Chr(13) & Chr(13) & Chr(13) & \_
" The UNION is only for getting a good master list of Similar Titles " & Chr(13) & Chr(13) & Chr(13) & \_
" Use the INDMAT function for the Numbers -- Enter the Account Title, the Master Title and the Numbers " & Chr(13) & Chr(13) & Chr(13) & \_
" To Sort, for now you must copy and paste special " & Chr(13) & Chr(13) & Chr(13) & \_
" The INDMAT -- Index and Match Function makes things easier. This can be used with entire columns or rows" & Chr(13) & Chr(13) & Chr(13), , \_
" MAKING THE UNION AND INDMAT WORK FOR READING FINANCIALS"

MsgBox \_
" After Reading in the Financials, you should do some PREPARATION " & Chr(13) & Chr(13) & Chr(13) & \_
" 1. Put the Financials in the Same Sheet " & Chr(13) & Chr(13) & Chr(13) & \_
" 2. Put the years in Order " & Chr(13) & Chr(13) & Chr(13) & \_
" 3. Adjust Titles to Make Them Similar " & Chr(13) & Chr(13) & Chr(13) & \_
" 4. Apply the UNION function for a comprehensive set of titles " & Chr(13) & Chr(13) & Chr(13) & \_
" 5. Use the INDMAT function with locked columns and copy down " & Chr(13) & Chr(13) & Chr(13) & \_
" The INDMAT -- Index and Match Function makes things easier. This can be used with entire columns or rows" & Chr(13) & Chr(13) & Chr(13), , \_
" MAKING THE UNION AND INDMAT WORK FOR READING FINANCIALS"


End Sub

Technical Details of the INDMAT
-------------------------------

The insert below shows the code for creating the INDMAT Function.  You can copy this function to your sheets like for the other functions.

Function indmat(lookup\_value, master\_list, values) As Single ' This function does the index and match together

Dim num As Single
num = 150

For i = 1 To num ' loop around a given number
If lookup\_value = master\_list(i) Then
indmat = values(i)
Exit Function
End If
Next i

' On Error GoTo no\_value:
' match1 = WorksheetFunction.Match(lookup\_value, master\_list, 0)
' indmat = WorksheetFunction.Index(values, match1)

' Exit Function
no\_value:
indmat = 0

End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2865&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9492&rand=0.18062526797765566)