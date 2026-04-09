# Sculpting with Fixed Debt and Changing DSCR – User Defined Function

**Source:** https://edbodmer.com/sculpting-with-fixed-debt-and-changing-dscr-user-defined-function

---

Function Compute\_LLCR() 
' This is initial LLCR with sculpting from constant DSCR

Dim output1(1, 20) As Single
' First iterate around the LLCR factor to find close
llcr = min\_dscr 
' Set iniital DSCR for first iteration

For iter = 1 To 3 
' Three iterations should be enough to get reasonable estimate

`debt_balance = debt_amount ' Debt amount comes from input in the read data file` 
`pv_debt_service = 0 ' Re-set the PV for each iteration` 
`pv_cfads = 0` 
`compound_factor = 1` 
`For i = 1 To tenure` 
`interest_expense(i) = debt_balance * interest_rate(i) ' The debt balance starts high and then goes down` 
`debt_bal(i) = debt_balance ' Debt balance in array` 
`ebit = ebitda(i) - dep_exp(i)` 
`' Ebit is from subtracting depreciation ebt = ebit - interest_expense(i) taxes(i) = ebt * tax_rate` 
`' Change this and include the ebt` 
`cfads(i) = ebitda(i) - taxes(i)` 
`If llcr <> 0 Then debt_service(i) = cfads(i) / llcr - other_debt_service(i)` 
`' Now compute the debt service as pv of cfads` 
`repayment(i) = debt_service(i) - interest_expense(i)` 
`' repayment is from CFADS and thus tax` 
`debt_balance = debt_balance - repayment(i)` 
`compound_factor = compound_factor * (1 + interest_rate(i))` 
`' Overall debt IRR` 
`pv_cfads = pv_cfads + cfads(i) / compound_factor` 
`' PV of debt service is debt` 
`pv_debt_service = pv_debt_service + debt_service(i) / compound_factor` 
`' PV of debt service is debt Next i If debt_amount <> 0 Then llcr = pv_cfads / debt_amount`
Next iter
End Function

Goal Seek Function
------------------

Function Goal\_Seek\_for\_LLCR\_Factor() ‘ Goal seek to find the LLCR factor

Dim output1(1, 20) As Single

ReDim repayment\_sum(tenure), debt\_period(tenure)

‘ First iterate around the LLCR factor to find close

Increment\_to\_LLCR\_Factor = (max\_llcr – 1) / 20 ‘ This is to try different increments to find the LLCR

Count = 1  
Count\_of\_Iterations = 0

Linear\_Interpolate\_Option = True

pv\_debt\_service = 0  
NPV\_of\_Debt\_Service = 0  
Debt\_Balance = debt\_amount  
Start\_LLCR\_Factor = 1  
End\_LLCR\_Factor = max\_llcr

re\_start: ‘ After you have found a NPV that exceeds the amount, go back and restart

Count\_of\_Iterations = Count\_of\_Iterations + 1

‘ The first few iterations use the slope and intercept method

If Count\_of\_Iterations > 5 Then GoTo slope\_intercept: ‘ Start with simple raw iteration

‘—————————————————————————————————————————  
‘—————————————————————————————————————————  
‘  
‘ This is the key loop for finding the LLCR Factor that Results in PV of Debt Service = Debt  
‘  
‘—————————————————————————————————————————  
‘—————————————————————————————————————————

For LLCR\_Factor = Start\_LLCR\_Factor To End\_LLCR\_Factor Step Increment\_to\_LLCR\_Factor ‘ Go from small to big and go until hit the debt amount

      Count = Count + 1
    
      last_pv = NPV_of_Debt_Service
    
      Last_LLCR_Factor = LLCR_Factor - Increment_to_LLCR_Factor      ' Rember the last increment because that may be the good one

‘ Create the 2 x 2 matrix for the Interpolate

      period_range(1) = 1                                              ' This is table for interpolate
      period_range(2) = end_time
    
      dscr_range(1) = llcr * LLCR_Factor
      dscr_range(2) = min_dscr
    
      compound_factor = 1
      pv_debt_service = 0
      Debt_Balance = debt_amount
    
      For i = 1 To tenure
    
          debt_period(i) = i
    
          interest_expense(i) = Debt_Balance * interest_rate(i)
          Debt_Balance_Array(i) = Debt_Balance
    
          If Linear_Interpolate_Option = False Then Curved_DSCR(i) = interpolate_look_up1(i, period_range, dscr_range)
          If Linear_Interpolate_Option = True Then Curved_DSCR(i) = interpolate_look_up_linear1(i, period_range, dscr_range)
    
          ebit = ebitda(i) - dep_exp(i)
          ebt = ebit - interest_expense(i)
    
          taxes(i) = ebt * tax_rate
          cfads(i) = ebitda(i) - taxes(i)
    
          If Curved_DSCR(i) <> 0 Then debt_service(i) = cfads(i) / Curved_DSCR(i) - other_debt_service(i)              ' Now compute the debt service as pv of cfads
    
          repayment(i) = debt_service(i) - interest_expense(i)
    
          repayment_sum(i) = repayment(i)    ' Dimensioned for the
    
          Debt_Balance = Debt_Balance - repayment(i)
    
          compound_factor = compound_factor * (1 + interest_rate(i))                        ' Overall debt IRR
          pv_debt_service = pv_debt_service + debt_service(i) / compound_factor        ' Accumulate PV of debt service over the debt life
    
      Next i
    
      NPV_of_Debt_Service = debt_amount - pv_debt_service
      If NPV_of_Debt_Service > 0 Then Exit For                      ' When NPV moves to positive, stop the loop

Next LLCR\_Factor

‘ This is after you have exited the FOR loop and you will change the increment

Start\_LLCR\_Factor = LLCR\_Factor – Increment\_to\_LLCR\_Factor ‘ Try a new LLCR Factor  
End\_LLCR\_Factor = LLCR\_Factor + Increment\_to\_LLCR\_Factor

Increment\_to\_LLCR\_Factor = Increment\_to\_LLCR\_Factor / 10 ‘ Reduce the Increment to get more precise

GoTo re\_start:

slope\_intercept:

‘  
‘ Now try slope and intercept  
‘ Slope is pv\_debt\_service/LLCR\_Factor  
‘  
If (LLCR\_Factor – Last\_LLCR\_Factor) <> 0 Then \_  
Slope = (NPV\_of\_Debt\_Service – last\_pv) / (LLCR\_Factor – Last\_LLCR\_Factor)

    Intercept = NPV_of_Debt_Service - Slope * LLCR_Factor
    
    If Slope <> 0 Then LLCR_Factor_final = -Intercept / Slope
    
    sum_prod = WorksheetFunction.SumProduct(debt_period, repayment_sum)
    
    If debt_amount <> 0 Then average_life = sum_prod / debt_amount
    
    output1(1, 1) = LLCR_Factor_final
    
    Goal_Seek_for_LLCR_Factor = output1

End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=10365&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.9146493154177437)