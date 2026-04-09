# UDF for Simple IDC

**Source:** https://edbodmer.com/dsra-and-cash-sweep-case

---

This page illustrates how to create a UDF for a model with only a problem where the IDC drives the project cost and the project cost drives the debt and therefore the IDC. This is perhaps the most common circular reference in project finance models. The UDF for solving this problem is not as easy as the simple example I used for the fee example because as the debt is built -up during construction the IDC increases. This means you must simulate the accumulation of debt in the UDF and create a loop. It also can mean that you do not want to put the output of the UDF in a line rather than in a single number. This means that you can create a UDF with an Array where you need to go backwards and accumulate the debt. The file below includes the simple IDC method.

The screenshot illustrates the IDC resolution problem. The IDC and the EBL interest create a circular reference that could be resolved with a copy and paste macro. But as there is only one debt issue and you do not have many complicated items, you can write a UDF. In the screenshot, the line for IDC in the uses of funds comes from the UDF below and allows you to change scenarios and evaluate the costs of delay. You can then connect the applied column to the UDF and there is no need for a button. I have included the example with the UDF and without the UDF in buttons below.

![](https://edbodmer.com/wp-content/uploads/2022/03/image-10.png)

.

**[Excel File with Analysis of Monte Carlo Simulation to Verify the Volatility Input Equals the Volatility Output](https://edbodmer.com/wp-content/uploads/2022/03/Time-Series-Analysis-10000.xlsm)
**

**[Excel File with Example of Computing Bid with Conventional Macro Buttons without User Defined Functions](https://edbodmer.com/wp-content/uploads/2022/03/Example-with-No-Buttons.xlsm)
**

.

When creating a UDF like this, I forget how to make an array variable sometimes. The except below shows the steps that includes:

*   Use Variant in the function name
*   Create a variable with an array (I use something like output). Make sure it has rows and columns.
*   Define the output variable in a loop. This should have a row and a column
*   Assign the name of the function to the variable with a loop

    Function funding(time_range, cap_exp, debt_percent, interest_rate, EBL_rate, EBL_pct) As Variant
    
    Dim output(2, 1) As Double
    Dim financing_requirements(), debt_financing(), equity_financing() As Double
    Dim debt_balance(), EBL_balance(), EBL(), IDC() As Double
    
    difference = 999
    
    Count = 0
    For i = 1 To time_range.Count
        If time_range(i) Then Count = Count + 1
    Next i
    construction_period = Count
    
    ReDim financing_requirements(construction_period)
    ReDim financing_requirements(construction_period), debt_financing(construction_period), equity_financing(construction_period)
    ReDim debt_balance(construction_period), EBL_balance(construction_period), EBL(construction_period), IDC(construction_period)
    
    ' MsgBox " Cap Exp Sum " & WorksheetFunction.Sum(cap_exp)
    ' MsgBox " Periods " & construction_period
    
    Do While difference <> 0
    
        For Period = 1 To construction_period
                
            financing_requirements(Period) = cap_exp(Period) + IDC(Period) + EBL(Period)
            
            debt_financing(Period) = financing_requirements(Period) * debt_percent
            equity_financing(Period) = financing_requirements(Period) - debt_financing(Period)
            
            If Period > 1 Then
                IDC(Period) = debt_balance(Period - 1) * interest_rate
                EBL(Period) = EBL_balance(Period - 1) * EBL_rate
                
                debt_balance(Period) = debt_balance(Period - 1) + debt_financing(Period)
                EBL_balance(Period) = EBL_balance(Period - 1) + equity_financing(Period) * EBL_pct
            End If
                
            If Period = 1 Then
                 debt_balance(Period) = debt_financing(Period)
                 EBL_balance(Period) = equity_financing(Period) * EBL_pct
            End If
    
    
        Next Period
    
        IDC_Last = IDC_output
        EBL_Last = EBL_output
    
        IDC_output = WorksheetFunction.Sum(IDC)
        EBL_output = WorksheetFunction.Sum(EBL)
        
        difference = IDC_Last - IDC_output + EBL_Last - EBL_output
    
    '    MsgBox " IDC " & IDC_output
    '    MsgBox " EBL " & EBL_output
    '    MsgBox " Period " & Period
        
    '    MsgBox " Debt Balance " & debt_balance(Period - 1)
    '    MsgBox " EBL Balance " & EBL_balance(Period - 1)
    
    Loop
    
    output(1, 1) = IDC_output
    output(2, 1) = EBL_output
    
    funding = output
    
    End Function
    
    

The first example below isolates on what you have to do to create the array function.

    Function idc_shell() As Variant
    
    Dim output(1,1000) As Variant
    
    For Period = 1 To 100
        
        output(1,Period) = 100
    
    Next Period
    
    idc_shell = output
    
    End Function
    

The second example illustrates the IDC calculation. I made a mistake at first by defining the loop to be longer than the number of inputs for the capital expenditures. Note also that you do not have define the capital expenditure and the flag with the DIM statement.

    Function idc(constr_flag, int_rate, debt_pct, cap_exp) As Variant
    
    Dim idc_output(1000) As Variant
    Dim debt_balance(1000), debt_draws(1000), funding_needs(1000), cap_exp1(1000) As Double
    
    For i = 1 To 15
    
        For Period = 1 To 10
              
          funding_needs(Period) = cap_exp(Period) + idc_output(Period)
          debt_draws(Period) = funding_needs(Period) * debt_pct
            
          If Period > 1 Then
            If constr_flag(Period) = 1 Then idc_output(Period) = debt_balance(Period - 1) * int_rate
             
            debt_balance(Period) = debt_balance(Period - 1) + debt_draws(Period)
          Else
            debt_balance(Period) = debt_draws(Period)
          End If
        
        Next Period
    
    Next i
    
    idc = idc_output
    
    End Function

Another example of using an array for a function is shown below. It is called the read array and the file is attached below.

    Function Read_Array(op_switch, EBITDA, Optional other) As Variant
        Dim output(4) As Variant
        If IsMissing(other) Then other = 0
        tot_num = 1000
        For i = 1 To tot_num
            If op_switch(i) = True Then
                start_oper = i
                Exit For
            End If
        Next i
        
        For i = 2 To tot_num
            If op_switch(i - 1) = True And op_switch(i) = False Then
                end_oper = i - 1
            End If
        Next i
        For i = start_oper To end_oper
            total_ebitda = total_ebitda + EBITDA(i)
        Next i
        output(1) = tot_num
        output(2) = start_oper
        output(3) = end_oper
        output(4) = total_ebitda
        
        Read_Array = output
    
    End Function
    

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1375&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8588&rand=0.5647007157183551)