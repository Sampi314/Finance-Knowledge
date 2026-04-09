# Circular Reference On-Line Course – Advanced UDF’s

**Source:** https://edbodmer.com/circular-reference-on-line-course-advanced-udfs

---

In this page I have included some advanced issues that can be solved with the UDF functions.  In the case below you can use ideas of a slope and intercept to develop a dynamic goal seek. .

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

. .

Sub experiment()

debug2 = False
time\_saving\_mode = False

If time\_saving\_mode Then
Application.ScreenUpdating = False
Else
Application.ScreenUpdating = True
End If

If time\_saving\_mode = False Then
Application.StatusBar = "......................................................................."
test6 = DoEvents
End If

Range("start\_time") = Time

Range("prob\_scenario") = 1

Count = 1

Sheets("Summary").Calculate ' Make sure have recent parameters

low\_price = Range("low\_start") ' Can change these
high\_price = Range("high\_start") ' Can change
increment = (high\_price - low\_price) / 5 ' Divisor can change speed

If time\_saving\_mode = False Then
Application.StatusBar = "Part 1: Find Slope and Intercept ...................................................."
test6 = DoEvents
End If

Count = 1
iteration = 0 ' Counts iteration for output

For ppa\_price = low\_price To high\_price Step increment

iteration = iteration + 1

find\_npv ' Call routine to find NPV; need to calculate

npv\_output(iteration) = npv\_result ' Store Iteration in an array
ppa\_output(iteration) = ppa\_price

Count = Count + 1
If npv\_result > 0 Then Exit For ' When hit positive NPV stop (start with low price)

Next ppa\_price

' Now go back and get numbers between zero

If iteration > 1 Then ' After exit, make low and high for slope
low\_ppa = ppa\_output(iteration - 1)
low\_npv = npv\_output(iteration - 1)
End If

high\_ppa = ppa\_output(iteration)
high\_npv = npv\_output(iteration)

' call find npv

' Y is the NPV
' X is the PPA Price

' Equation: NPV = A + B x Price

' B = Slope = (y1 - y2)/(x1 - x2)

If debug2 Then MsgBox " High PPA " & high\_ppa & " High NPV " & Format(high\_npv, "###,###.00") & " Low PPA " & low\_ppa & " Low NPV " & Format(low\_npv, "###,###.00")

b = (high\_npv - low\_npv) / (high\_ppa - low\_ppa)

' high\_npv = a + b x high\_ppa
' a = high\_npv - b x high\_ppa

a = high\_npv - b \* high\_ppa

If debug2 Then
Range("a") = a
Range("b") = b
End If

' MsgBox " Slope " & a & " Intercept " & b

' now find zero npv point
' NPV = a + b \* ppa\_price
' 0 = a + b \* ppa\_price
' -a = b \* ppa\_price
' - a/b = ppa\_price

If b <> 0 Then ppa\_price\_base = -a / b ' Theoretical zero NPV from Line
ppa\_price = ppa\_price\_base

find\_npv ' Find zero NPV from line

If debug2 Then MsgBox " Trying from Straight Line " & Chr(13) & \_
" PPA Price from Line " & Format(ppa\_price, "00.00") & " NPV Computed " & Format(npv\_result, "0.00") & " Increment " & increment

' Now re-do a and b

iteration = iteration / 10 ' Set divisor for slope calculation -- the high and low bound

re\_start\_iteration: ' Try new line with more precise slope and intercept

ppa\_price = ppa\_price\_base + iteration / 2 ' Last ppa price plus iteartion

find\_npv

high\_ppa = ppa\_price
high\_npv = npv\_result

ppa\_price = ppa\_price\_base - iteration / 2 ' start of iteration

find\_npv

low\_ppa = ppa\_price
low\_npv = npv\_result

' MsgBox " High PPA " & high\_ppa & " Low PPA " & low\_ppa

' Now re-compute the slope and intercept

If (high\_ppa - low\_ppa) <> 0 Then b = (high\_npv - low\_npv) / (high\_ppa - low\_ppa)
a = high\_npv - b \* high\_ppa

If debug2 Then
Range("a") = a
Range("b") = b
End If

If b <> 0 Then ppa\_price\_base = -a / b
ppa\_price = ppa\_price\_base

find\_npv ' Get the zero NPV value from the line

If debug2 Then MsgBox " Trying from Straight Line " & Chr(13) & \_
" PPA Price from Line " & Format(ppa\_price, "00.00") & " NPV Computed " & Format(npv\_result, "0.00") & " Increment " & increment

iteration = iteration / 8

Count = Count + 1

If Abs(npv\_result) < 100 Then ' Put in criteria

If debug2 Then MsgBox " Final NPV " & Chr(13) & \_
" NPV " & Format(npv\_result, "###,###.00") & " PPA Price " & Format(ppa\_price, "00.00")

GoTo finish\_sub

End If
If Count > 180 Then Exit Sub

If time\_saving\_mode = False Then
Application.StatusBar = "Part 2 ................................ Iteration " & Count & " NPV " & Format(npv\_result, "###,##.00")
test6 = DoEvents
End If

GoTo re\_start\_iteration:

finish\_sub:

Range("ppa\_price").Value = ppa\_price
Range("ppa\_price").Calculate

Range("end\_time") = Time
Range("iterations") = Count
Sheets("Summary").Calculate

Application.StatusBar = False
test6 = DoEvents

End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3658&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13108&rand=0.5721429404505968)