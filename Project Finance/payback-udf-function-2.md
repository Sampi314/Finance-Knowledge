# Depreciation Vintage

**Source:** https://edbodmer.com/payback-udf-function-2

---

This page demonstrates how you can apply a user defined function instead of one of those diagonal matrices that has a diagonal thing. You can use this idea for many different applications that are similar to the depreciation problem. Please note that this depreciation problem is not at all necessary if you have straight line depreciation. The screenshot below illustrates the result of the depreciation function compared to creating a matrix

![](https://edbodmer.com/wp-content/uploads/2021/01/image-38.png)

The second example illustrates a case with remaining life straight line depreciation

![](https://edbodmer.com/wp-content/uploads/2021/01/image-39.png)

Sub A\_Depreciation\_Functions()
End Sub
Function depreciation(capital\_expenditure, depreciation\_rate) As Variant ' When the output is an array define as Variant
asset\_life = depreciation\_rate.Count ' Find Life from the depreciation rate array
cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled
ReDim Depreciation\_Expense(cap\_exp\_periods) As Single ' Make a new array variable that is the output
For model\_year = 1 To cap\_exp\_periods ' loop around each period

`For vintage = 1 To cap_exp_periods ' make a second loop to evaluate asset by asset age = model_year - vintage + 1 ' calculate the age of each expenditure (the diagonal) If (age > 0 And age <= asset_life) Then ' Only when asset is alive Depreciation_Expense(model_year) = _ capital_expenditure(vintage) * depreciation_rate(age) + Depreciation_Expense(model_year) End If Next vintage ' Note that the vintage is usef for the capital expenditure`
Next model\_year
depreciation = Depreciation\_Expense
End Function


Function depreciation\_remaining\_life(capital\_expenditure, remaining\_life) As Variant ' When the output is an array define as Variant
cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled
Dim Depreciation\_Expense(5000) As Single ' Make a new array variable that is the output
For model\_year = 1 To cap\_exp\_periods ' loop around each period and make a square with columns and rows
`For vintage = 1 To cap_exp_periods ' make a second loop to evaluate asset by asset age = model_year - vintage + 1 ' calculate the age of each expenditure (the diagonal) If (age > 0 And remaining_life(vintage) <> 0) Then ' Only when asset is alive Depreciation_Expense(model_year) = _ capital_expenditure(vintage) / remaining_life(vintage) + Depreciation_Expense(model_year) End If Next vintage ' Note that the vintage is usef for the capital expenditure`
Next model\_year
depreciation\_remaining\_life = Depreciation\_Expense
End Function


Function depreciation\_remaining\_life\_1(capital\_expenditure, remaining\_life, max\_life) As Variant ' When the output is an array define as Variant
cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled
Dim Depreciation\_Expense(5000) As Single ' Make a new array variable that is the output
Dim remaining\_life1(5000) As Single
For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset
If remaining\_life(vintage) >= max\_life Then
remaining\_life1(vintage) = max\_life
Else
remaining\_life1(vintage) = remaining\_life(vintage)
End If
`Depreciation_Expense(vintage) = remaining_life1(vintage)`
Next vintage
depreciation\_remaining\_life\_1 = Depreciation\_Expense
Exit Function
For model\_year = 1 To cap\_exp\_periods ' loop around each period and make a square with columns and rows
`For vintage = 1 To cap_exp_periods ' make a second loop to evaluate asset by asset age = model_year - vintage + 1 ' calculate the age of each expenditure (the diagonal) If (age > 0 And remaining_life1(vintage) <> 0) Then ' Only when asset is alive Depreciation_Expense(model_year) = _ capital_expenditure(vintage) / remaining_life1(vintage) + Depreciation_Expense(model_year) End If Next vintage ' Note that the vintage is usef for the capital expenditure`
Next model\_year
depreciation\_remaining\_life\_1 = Depreciation\_Expense
End Function


Function depreciation\_remaining\_life\_2(capital\_expenditure, remaining\_life, max\_life) As Variant ' When the output is an array define as Variant
cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled
Dim Depreciation\_Expense(5000) As Single ' Make a new array variable that is the output
Dim remaining\_life1(5000) As Single
' Determine whether to use remaining life or something shorter
For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset
If remaining\_life(vintage) >= max\_life Then
remaining\_life1(vintage) = max\_life
Else
remaining\_life1(vintage) = remaining\_life(vintage)
End If
Next vintage
For model\_year = 1 To cap\_exp\_periods ' loop around each period and make a square with columns and rows
`For vintage = 1 To cap_exp_periods ' make a second loop to evaluate asset by asset age = model_year - vintage + 1 ' calculate the age of each expenditure (the diagonal) If (age > 0 And remaining_life1(vintage) <> 0 And remaining_life1(vintage) >= age) Then ' Only when asset is alive Depreciation_Expense(model_year) = _ capital_expenditure(vintage) / remaining_life1(vintage) + Depreciation_Expense(model_year) End If Next vintage ' Note that the vintage is usef for the capital expenditure`
Next model\_year
depreciation\_remaining\_life\_2 = Depreciation\_Expense
End Function


Function depreciation\_remaining\_life\_3(capital\_expenditure, remaining\_life, max\_life, factr) As Variant ' When the output is an array define as Variant
cap\_exp\_periods = capital\_expenditure.Count ' See how many capital expenditure periods are modelled
Dim Depreciation\_Expense(5000) As Single ' Make a new array variable that is the output
Dim dep\_rate(5000, 5000) As Single
For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset
If remaining\_life(vintage) >= max\_life Then
adjusted\_life = max\_life
dep\_rate(vintage, 1) = 1 / adjusted\_life \* factr
`For j = 2 To adjusted_life dep_rate(vintage, j) = WorksheetFunction.Vdb(1, 0, adjusted_life, j - 1, j, factr) Next j Else adjusted_life = remaining_life(vintage) dep_rate(vintage, 1) = 1 / adjusted_life * factr For j = 2 To adjusted_life dep_rate(vintage, j) = 1 / adjusted_life dep_rate(vintage, j) = WorksheetFunction.Vdb(1, 0, adjusted_life, j - 1, j, factr) Next j End If`
Next vintage
For model\_year = 1 To cap\_exp\_periods ' loop around each period and make a square with columns and rows
For vintage = 1 To cap\_exp\_periods ' make a second loop to evaluate asset by asset
age = model\_year - vintage + 1 ' calculate the age of each expenditure (the diagonal)
If (age > 0 And remaining\_life(vintage) <> 0) Then ' Only when asset is alive
Depreciation\_Expense(model\_year) = \_
capital\_expenditure(vintage) \* dep\_rate(vintage, age) + Depreciation\_Expense(model\_year)
End If
Next vintage ' Note that the vintage is usef for the capital expenditure
Next model\_year
depreciation\_remaining\_life\_3 = Depreciation\_Expense
End Function


Function dep(capexp, life) As Variant
num = capexp.Count ' find the length of the cap exp array
ReDim dep1(num) As Single ' create a flexible array as the output
For model\_year = 1 To num
For vintage = 1 To num
age = model\_year - vintage + 1
`If (age > 0 And age <= life) Then dep1(model_year) = capexp(vintage) / life + dep1(model_year) End If Next vintage`
Next model\_year
dep = dep1
End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1586&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11384&rand=0.6459900611491058)