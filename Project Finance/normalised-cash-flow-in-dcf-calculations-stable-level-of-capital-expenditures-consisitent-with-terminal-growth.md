# Normalised Cash Flow in DCF Calculations – Stable Level of Capital Expenditures Consisitent with Terminal Growth

**Source:** https://edbodmer.com/normalised-cash-flow-in-dcf-calculations-stable-level-of-capital-expenditures-consisitent-with-terminal-growth

---

This page explains how to create a model that has normalisation of terminal cash flow consistent with terminal growth assumptions.  Two different methods are explained that provide a normalised ration of capital expenditures to depreciation.  The first method accounts for the depreciation life and the terminal growth rate.  The second method incorporates the projected life and the depreciation life and also the historic growth in capital expenditures which drive the replacement of existing assets.  User defined functions that define the stable amount of capital expenditure to depreciation given a couple of inputs for terminal growth, depreciation rates and in some cases historic growth. A very basic idea in life is that you have to make an investment to achieve something good. In the context of terminal value, if the growth in terminal cash flow is higher, the capital investment must also be higher.  This means that the projected normalised capital expenditures cannot be independent of the level of growth.

**[Excel File with Demonstration of Stable Working Capital and Capital Expenditure that Depends on Terminal Growth](https://edbodmer.com/wp-content/uploads/2019/03/Stable-Ratio-Analysis.xlsm)
**

*   If you are assuming a higher rate of growth in EBITDA, you must assume a higher level of stable capital expenditures. This should be obvious.
*   You also need to replace existing assets at some time if the EBITDA is to continue.
*   The growth includes growth from inflation as well as real growth.
*   You can make a little growth and depreciation analysis to evaluate how what happens to the stable ratio of capital expenditures to depreciation, where the depreciation reflects the status of existing assets.

The basic method without considering historic growth is shown in the code below.  All you have to do is copy this code into your excel workbook (but since Option base 1 is at the top, make sure it is at the top of a module page).  Then you have a function that will give you the capital expenditures to depreciation as a function of the depreciation life and the growth rate.  You can also use a timing switch.

.

Option Base 1
Function cap\_exp\_depreciation\_simple(life, growth, Optional timing\_code)

If IsMissing(timing\_code) Then timing\_code = 1

base\_capexp = 100
capexp = 100

plant\_balance = 100

For i = 2 To life + 1

capexp = capexp \* (1 + growth) ' Capital Expenditure After Depreciation
If i = life + 1 Then retirement = base\_capexp

If timing\_code = 3 Or timing\_code = 2 Then \_ 
    plant\_balance = plant\_balance + capexp - retirement ' Closing Balances

depreciation\_exp = plant\_balance / life ' Depreciation on Opening Balance
If timing\_code = 2 Then depreciation\_exp = (plant\_balance - (capexp - retirement) / 2) / life ' Depreciation on Opening Balance


If timing\_code = 1 Then plant\_balance = plant\_balance + capexp ' Closing Balances

Next i

cap\_exp\_depreciation\_simple = capexp / depreciation\_exp


End Function

.

The next function below that you can also copy is a more complex function where you reflect the historic growth rate of the corporation as well as the life and the projected growth rate.  The output again is the stable capital expenditures to depreciation.

.

Option Base 1

Function cap\_exp\_depreciation\_simple(life, growth, Optional timing\_code)

If IsMissing(timing\_code) Then timing\_code = 1

base\_capexp = 100
capexp = 100

plant\_balance = 100

For i = 2 To life + 1

capexp = capexp \* (1 + growth) ' Capital Expenditure After Depreciation
If i = life + 1 Then retirement = base\_capexp

If timing\_code = 3 Or timing\_code = 2 Then plant\_balance = plant\_balance + capexp - retirement ' Closing Balances

depreciation\_exp = plant\_balance / life ' Depreciation on Opening Balance
If timing\_code = 2 Then depreciation\_exp = (plant\_balance - (capexp - retirement) / 2) / life ' Depreciation on Opening Balance


If timing\_code = 1 Then plant\_balance = plant\_balance + capexp ' Closing Balances

Next i

cap\_exp\_depreciation\_simple = capexp / depreciation\_exp


End Function

.

Evaluating Capital Expenditure to Depreciation With Difference in Historic Growth and Replacement of Assets
-----------------------------------------------------------------------------------------------------------

Consider population.  If there was a baby boom with a lot of births and you must replace the births.  Then there will be a second cycle when the baby boom comes to the age when they have children.  In a similar but not exact way, if you are replacing EBITDA and you made a lot of capital expenditures, one day you will have to either allow the EBITDA to decline to nothing or replace the capital expenditures.  The problem is that these are not smooth.  Further, tying to levelize out the capital expenditures is tricky.

**[Excel File with Simulated Depreciation Expense, Capital Expenditure and Retirment Analysis and Varying Growth Rates](https://edbodmer.com/wp-content/uploads/2019/03/Stable-Cap-Exp-Depr-Historic-Growth.xlsm)
**

The table below illustrates the effects of different historic growth rates.  Note that incorporation of historic growth does somewhat improve the valuation.  In the file there is a theoretically correct value and then the different methods of measuring capital expenditures in the terminal value are applied.  The method of not including any adjustment is dramatically wrong.

![](https://edbodmer.com/wp-content/uploads/2019/03/Comparative-Values.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/03/Plant-Time-Line.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/03/Plant-Cycles-Graph.jpg)

You can think of a case where you have made more capital expenditures in the past.  Then you have to replace the capital expenditures to maintain the EBITDA.  But the depreciation expense is also higher even though the expenditures were made.

**[Excel File with Capital Expenditure and Depreciation Analysis with Varying Growth Rates for Terminal Value](https://edbodmer.com/wp-content/uploads/2019/03/Cap-Exp-Stable.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2019/03/Data-Table-Growth-and-Rate.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/03/Cycles-of-Cap-Exp.jpg)

This function shows how to evaluate the adjusted capital expenditures if you have an idea of what the is the historic growth.  You can copy this function into your model.

.

Option Base 1
Sub depreciation\_Rate\_functions()

End Sub



Function adjusted\_cap\_exp(historic\_growth, future\_growth, life, wacc)

Dim cap\_exp(1000)

gross\_plant = 1

method = 1
' method 2

If method = 2 Then
base = gross\_plant / life
End If

If method = 1 Then
base = find\_base(historic\_growth, life)
End If


If life < 0 Then Exit Function

cap\_exp(1) = base

total\_test = base

For i = 2 To life

Select Case method:

Case 1:
cap\_exp(i) = cap\_exp(i - 1) \* (1 + historic\_growth)
Case 2:
cap\_exp(i) = cap\_exp(i - 1)
Case 3:
cap\_exp(i) = cap\_exp(i - 1) \* (1 - historic\_growth)

End Select

total\_test = total\_test + cap\_exp(i)

Next i

' MsgBox " base " & base & " total test " & total\_test


opening\_balance = gross\_plant

pv\_factor = (1 + wacc)

For i = life + 1 To 500

pv\_factor = pv\_factor \* (1 + wacc)

closing\_balance = opening\_balance \* (1 + future\_growth)

retirement = cap\_exp(i - life)
cap\_exp(i) = closing\_balance - opening\_balance + retirement
depreciation = opening\_balance / life

pv\_cap\_exp = pv\_cap\_exp + cap\_exp(i) / pv\_factor
pv\_dep = pv\_dep + depreciation / pv\_factor

opening\_balance = closing\_balance

Next i

adjusted\_cap\_exp = pv\_cap\_exp / pv\_dep


End Function

.

Stable Deferred Tax
-------------------

The file that you can download below includes analysis of stable deferred tax changes as deferred tax changes should be in cash flow and not in the bridge between equity value and enterprise value.

**[Excel File with Simulation of Stable Deferred Tax Including User Defined Function for Deferred Tax Change/Cap Exp](https://edbodmer.com/wp-content/uploads/2019/03/Deferred-Tax-Functions.xlsm)
**

Simulated Depreciation Expense and Retirements
----------------------------------------------

**[Excel File with Simulated Depreciation Expense Analysis and Varying Long-term Growth Rates](https://edbodmer.com/wp-content/uploads/2019/03/Stable-Cap-Exp-Ratio.xlsm)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2453&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=14908&rand=0.02678909221706971)