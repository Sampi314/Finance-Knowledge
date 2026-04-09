# Interpolate-Lookup Function

**Source:** https://edbodmer.com/interpolate-lookup-function

---

It is remarkable that excel does not have an interpolate function.  You can search the internet and find a couple of interpolate user defined functions (and pay), or you can use the interpolate function that is available for download below at no charge.  The interpolate UDF works very much like the lookup function but it allows you to have numbers that gradually increase or decrease rather than moving in steps.  You can use the interpolate function with either compound growth interpolation or with straight line interpolation.

This page explains how to use the interpolate function and the technical details of how to make the user defined function yourself. To understand the interpolate function, you should first know that the LOOKUP function is better than VLOOKUP, HLOOKUP or MATCH and INDEX. You typically lookup on a date, then click on an entire row or columns of dates that correspond to you input.  You then finally click on an entire row or column of values that correspond to the dates. When using the LOOKUP function it almost seems obvious that there should be an interpolate option so values in the intermediate periods are filled in. On this page I walk through how to use and create an interpolate function after discussing the dynamic goal seek function method.

Implementation of the LOOKUP INTERPOLATE Function
-------------------------------------------------

To use the interpolate function you should download the file below which contains the function and some examples of how the function can be used.  There are in fact two versions of the function that allow you to interpolate in different ways.  The first interpolate function uses a compound growth method.  The compound growth rate between an interval is computed.  This compound growth rate is applied to the interval.

To implement the interpolate function, first download the file below.  Once you open the file you have to copy the UDF function from this sheet to your sheet.  To do this you can press the ALT and F8 keys to get the list of macros.  Then you copy the entire contents of what is in the Lookup\_functions VBA module to a module in your workbook.  An illustration of pressing the ALT and F8 key is shown below.  After this you edit the module; then press ALT A to select everything; then ALT C to copy everything; then go to your workbook and either enter a new module or go to the top of an exiting one; then press CNTL V to paste everything.

**[Download Excel File with the Function for Interpolation Using Either Compound Growth or Linear Interpolation](https://edbodmer.com/wp-content/uploads/2019/04/Lookup-and-Interpolate.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2018/04/Lookup-1.jpg)

Once you have followed the implementation process described above, you can enter the function in your spreadsheet similar to other functions.  The only difference is that the arguments for the function are not shown automatically with a user defined function.  Instead, you can press SHIFT and F3 to show the required arguments.  Using the interpolate\_lookup function with the growth method for interpolation is illustrated  in the screen shot below  (the difference between the growth method and the linear method is explained below.  If you look at the screen shot, the line titled ROIC uses the LOOKUP function that is described in detail in the basic function page of the website.

![](https://edbodmer.com/wp-content/uploads/2018/04/Lookup-2.jpg)

The second screenshot shows the equation of an interpolation where the amounts between the two values are divided into equal increments rather than using a growth rate method.  This results in larger changes in the early part of the interpolation and lower changes later on.  To apply the linear interpolation, you can use the same process with a function named interpolate\_look\_up\_linear.

Pasting the Interpolate Function into Your Sheet
------------------------------------------------

Once you have copied the VBA code (either from the userform, from pressing ALT, F8 and copying the entire sheet or from copying the code below), you can copy it into your file.  To do this, you can press ALT, F8 to get the VBA screen.  Then put in any name (e.g. Stormy).  Then go to the top of the file and copy the code (CNTL, V).  Some of this is demonstrated in the couple of  screenshots below.  The first screen shot illustrates how to create a new VBA page after you press ALT, F8; the second shows how you should insert a line to put the code at the top of the page; the third shows the results after you copy.

![](https://edbodmer.com/wp-content/uploads/2018/05/Payback-3.jpg)

After making the new page with you blank macro named Stormy, go above the new macro and enter a couple of blank lines.  When you have entered the blank lines you will press the CNTL, V and copy the code to the top of the page.

![](https://edbodmer.com/wp-content/uploads/2018/05/payback-4.jpg)

After you have copied the code into your sheet, you should see OPTION BASE 1 at the top of the page.  Now you are ready to go and the function should work in your workbook.

![](https://edbodmer.com/wp-content/uploads/2018/05/payback-5.jpg)

### Copy the Interpolate Function Directly from Here

Alternatively, if you just want to try copying the interpolate function from here, you can copy the code below into your spreadsheet.  To do this, press the ALT, F8 sequence to see the list of macros.  Then type in some new name (e.g. STORMY).  Then, press the CREATE button and make sure that your new function is at the top of the page.  Once you have the function defined, copy the code below to the TOP of the VBA page.  In particular, make sure the OPTION BASE 1 is at the top of the page.

.

Option Base 1


Function interpolate\_look\_up(lookup\_value, lookup\_series, value\_series, Optional on\_off)
 
 Dim lookup\_ser(1000) ' Allow for 1000 values
 Dim value\_ser(1000) ' These dimensions are for finding numbers
 
 If IsMissing(on\_off) Then on\_off = True
 If on\_off = False Then Exit Function
 
 max\_series = WorksheetFunction.Max(lookup\_series) ' find the maximum year etc. -- the key for lookup
 tot\_count = WorksheetFunction.Match(max\_series, lookup\_series, 0) ' use the max to count how many in the series
 
 Count = 1
 For i = 1 To tot\_count ' make a new array that only uses the series in case clicked on entire row
    If WorksheetFunction.IsNumber(lookup\_series(i)) Then ' use to find the numbers
    lookup\_ser(Count) = lookup\_series(i) ' find the look up value
    value\_ser(Count) = value\_series(i) ' two new arrays that have counts from 1 to Count -- lookup\_ser and value\_ser
    Count = Count + 1
 End If
 Next i
 
 Count = Count - 1
 
 For i = 1 To Count ' go around counted
 
 If lookup\_value = lookup\_ser(i) Then ' If the year looking up (or date,no etc) is equal to a number -- dont interpolate
    interpolate\_look\_up = value\_ser(i) ' If there is an exact match with then put in the number and skip rest
    Exit Function
 End If
 
 If lookup\_value < lookup\_ser(i + 1) Then ' When the year is less than the next year that read and adjusted

      If value\_ser(i) <> 0 Then ratio = value\_ser(i + 1) / value\_ser(i) ' ratio is the current next value divided by next value

      numerator = lookup\_value - lookup\_ser(i) ' this is a number like 2018 - 2016

      num\_of\_periods = lookup\_ser(i + 1) - lookup\_ser(i) ' this is the total -- nothing to do with the current year in model

      If num\_of\_periods <> 0 Then num\_raise = numerator / num\_of\_periods ' how much should raise to the power for interpolating

      compound\_fac = WorksheetFunction.Power(ratio, num\_raise) ' need to use the power function to compute compound growth

      interpolate\_look\_up = value\_ser(i) \* compound\_fac ' final value of the function -- initial value x compound ratio

 Exit Function
 End If
 
 If lookup\_value > lookup\_series(tot\_count) Then
 interpolate\_look\_up = value\_series(tot\_count)
 Exit Function
 End If
 
 Next i

interpolate\_look\_up = value\_series(Count)

End Function

.

If you want to put the interpolate function with a linear instead of compound growth, you can download the alternative VBA code below.  This code contains the different equations to make the increment equal between time periods.  As with the other code, all you have to do is copy this into your file.

.

Option Base 1

Function interpolate\_look\_up\_linear(lookup\_value, lookup\_series, value\_series, Optional on\_off)

Dim lookup\_ser(1000)
 Dim value\_ser(1000)

If IsMissing(on\_off) Then on\_off = True
 If on\_off = False Then Exit Function

If lookup\_value < lookup\_series(1) Then
 interpolate\_look\_up\_linear = value\_series(1)
 Exit Function
End If
 
max\_series = WorksheetFunction.Max(lookup\_series)
tot\_count = WorksheetFunction.Match(max\_series, lookup\_series, 0)

Count = 1
For i = 1 To tot\_count
    If WorksheetFunction.IsNumber(lookup\_series(i)) Then
      lookup\_ser(Count) = lookup\_series(i)
      value\_ser(Count) = value\_series(i)
      Count = Count + 1
     End If
Next i
Count = Count - 1

For i = 1 To Count
 If lookup\_value = lookup\_ser(i) Then ' lookup\_value is current number for year etc (e.g. 10)
    interpolate\_look\_up\_linear = value\_ser(i) ' if the look\_up value is the same as a value in table set to value
    Exit Function
 End If
 If lookup\_value < lookup\_ser(i + 1) Then ' case where the look up value is less than the last one
    num\_difference = lookup\_ser(i + 1) - lookup\_ser(i) ' find the difference in total years for the denominator
    val\_difference = value\_ser(i + 1) - value\_ser(i) ' difference in total values for numerator
    If num\_difference <> 0 Then increment = val\_difference / num\_difference
 
    num\_of\_increments = lookup\_value - lookup\_ser(i) ' total number of increments from start
    total\_adder = num\_of\_increments \* increment
 
    interpolate\_look\_up\_linear = value\_ser(i) + total\_adder
    Exit Function
 End If
 If lookup\_value > lookup\_series(tot\_count) Then
    interpolate\_look\_up\_linear = value\_series(tot\_count)
    Exit Function
 End If

Next i
interpolate\_look\_up\_linear = value\_ser(i - 1)
End Function

.

Interpolating without a Function
--------------------------------

Many people interpolate in excel without a function.  This can be done with the GROWTH function in excel using a few steps or you can compute the compound growth rate by yourself.  This is a painful process for something that should be automatic and of course I don’t think this is a very good idea.  For some reason when I made the not very good video below that describes this process I recieved a lot of views.

Video that introduces the macro process with cells.select

Making a Lookup function with Na like the false

Re-Creating the LOOKUP function to Introduce the Technical Process
------------------------------------------------------------------

Lookup\_NA.xlsm

This video introduces the technical process through explaining how to make your own LOOKUP function.  But when re-creating the LOOKUP function you can design it so the nasty NA does not appear when there are no values associated with one of your dates (or key values).  For example if you model starts in 2018 and you start your look-up values in 2019, the excel lookup will put in NA.  You can write your own function to put in a FALSE instead of an NA which will cause a whole lot less problems when you are making a model.

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1199&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10768&rand=0.3922750833419302)