# Maxif and Minif

**Source:** https://edbodmer.com/maxif-and-minif

---

The SUMIF and AVERAGEIF are really helpful functions in excel. But sometimes you may want to show the maximum or the minimum value in a certain range with a MAXIF or a MINIF function.  For example, you may want to show the minimum DSCR or the maximum interest rate only over the period after the plant is operational for some periods.  You can write a MAXIF and a MINIF very quickly as shown below.  I have uploaded a little file that demonstrates how it works.  You can download the file by clicking on the button below. I have included this on the website even though it is really easy because I sometimes forget how it works.

**[Excel File with VBA Code and Macro for Determing Whether an Input Cell has a Depenednt and Marking It](https://edbodmer.com/wp-content/uploads/2020/05/IDC-and-Dependents.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2020/04/maxmin.png)

The simple code for the MAXIF and MINIF functions is shown below.  All you do is make a loop around the array and use the worksheetfunction for finding the MAX or the MIN.  You have to initialise the amount in the function and name the result the same name as the function.  Note that the Option Base 1 is used because I use loops that begin with 1.  For the loop I also use the length of the array that is read in.

Option Base 1

Function maxif(test, values)

maxif = -1E+28

For i = 1 To test.Count

    If test(i) Then
        maxif = WorksheetFunction.Max(values(i), maxif)
     End If

Next i
End Function

Function minif(test, values)

minif = 1E+28

For i = 1 To test.Count

     If test(i) Then
          minif = WorksheetFunction.Min(values(i), minif)
     End If
Next i

End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9800&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11352&rand=0.6388687952480714)