# Applying UDF – Fundamental Cases

**Source:** https://edbodmer.com/circular-template-and-simple-models

---

Maybe you want your modelling career to involve applying rules and filling in template models with best practices. Maybe you think that success is when an auditor writes that you have no formulas that violate what they consider are best practices. If these are your objectives are just meeting basic requirements, then this page is not for you. On the other hand, if you want to break through the problems with excel that limit effective analysis of difficult financial analysis, then you can become an innovative analyst through writing some of your own code. This page walks through selected relatively simple exercises of applying a method that requires some programming — user defined functions — to resolve problems with excel that include circular references. I begin with examples from project finance where there are multiple painful circular references that severely limit many of the very big advantages of excel including data tables, goal seek and rapid evaluation of alternative financing structures. The user defined function method allows you to avoid problems that occur with both the iteration method (no goal seek; unstable models; slow models) and the copy and paste method (lose transparency; stop model execution; difficulty with data tables).  I start with very simple examples that only have a few inputs and do not have do loops.  Then I move to more complex cases with loops and reading in more variables. Each of the cases involves first understanding how the financial model works and then working through the excel model with equations.  All of the cases involving making a model parallel to your excel model. I have included the code on this page and also included the sample files.

.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-3.png)

.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-1.png)

.

.

.

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

.

**[Excel File with Project Finance Model Exercises Including DSRA, Mini Perm and UDF Exercises](https://edbodmer.com/wp-content/uploads/2022/04/2022.07.04-File-for-Session-6_Start-ab.xlsm)
**

.

.

.

Project Finance Example 1 — Simple Fees without Accumulation
------------------------------------------------------------

The first example I make is very simple. In this example you can learn about the basics of a UDF. You need to have the name of the function defined as an output. You also cannot get any data from the spreadsheet unless you read data into the UDF. This is illustrated by the two hello functions below that include a function called hello() and a function named div\_1000 that simply divides a number by 1000. The FORMULATEXT function in excel shows the functions. All of the functions are included in the file that you can download below.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-2.png)

The hello function is shown below. This is the simplest case that demonstrates how you much have a definition of the function name in the code. I also include a little SUB so you can find the function by pressing ALT-F8. The second function named Div\_1000 demonstrates how you need to read data that is used in the function in UDF.

.

    Sub simple_functions()
    
    End Sub
    
    Function hello()
    
         hello = "beunos dias"
    
    End Function
    
    Function Div_1000(constant)
    
          Div_1000 = constant / 1000
    
    End Function
    

.

![](https://edbodmer.com/wp-content/uploads/2022/04/image.png)

Case 1: Simple Funding without Loop – Cash Sweep and LBO Case
-------------------------------------------------------------

For the first case I have set up a very simple sources and uses of funds model with fees on debt. The fees are computed on debt and are included in the uses of funds. In the example you can contrast different methods for solving circular references.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-5.png)

The traditional copy and paste would have something like the following.

Sub SweepMacro()

GoalSeek1

While Range("Int\_Difference").Value <> 0
     GoalSeek1
     Range("Fixed\_Int").Value = Range("Comp\_Int").Value

Wend
End Sub

The alternative method with a user defined function is illustrated below

Function SweepInterest(InterestRate, OpeningBalance, EBITDA, SweepPercent)

sweep\_difference = 999 ' Need a starting point that is not zero
Count = 1 ' protect against continuing look

While sweep\_difference <> 0 ' This is like copy and paste
   Count = Count + 1
   If Count > 20 Then Exit Function ' protection

     last\_sweep = SweepInterest 

' this will start with zero and used for the difference

      cash\_flow\_s = EBITDA - SweepInterest 

' this is what causes the circular reference

Sweeprepayment = WorksheetFunction.Min(cash\_flow\_s \* SweepPercent, OpeningBalance) 
 ' Use excel function

ClosingBalance = OpeningBalance - Sweeprepayment 

' keep going backwards and see what you need

AverageDebt = WorksheetFunction.Average(OpeningBalance, ClosingBalance) 

' Use excel functions

SweepInterest = AverageDebt \* InterestRate 

' start with the end, and see what you need

sweep\_difference = last\_sweep - SweepInterest

Wend
End Function

Case 2: LBO Sweep with Interest on Average Balance and Taxes
------------------------------------------------------------

[Excel File that Addresses Advanced Issues Including Alternative Currencies and Translation Adjustments in Models](https://edbodmer.com/wp-content/uploads/2021/05/Advanced-Course.xlsm)

Case 3: Simple Corporate Model with Short-term Debt and Cash Balance and Average Balances
-----------------------------------------------------------------------------------------

In this example we work through the classic corporate model circular reference. In the example below I illustrate a case where a loan is repaid with a cash flow sweep.  The interest is computed on the average debt and not the initial debt. As the interest expense is a deduction for cash flow calculation.  So the interest drives the cash flow and the cash flow drives debt which drives interest.  The first screenshot below illustrates the interest calculation.

![](https://edbodmer.com/wp-content/uploads/2020/01/Circular-Sweep-Average.jpg)

The UDF can resolve this circular reference in a very easy way.  You just create a little program that defines the sweep as an algebraic formula which is shown first.  Alternatively, the second function demonstrates how to work through the same equations in parallel.  You begin by writing an equation for the sweep and then work backwards.

.

.

The screenshot below illustrates how to implement the UDF.  Note that you can find the inputs with either the Shift and F3 short-cut or with the fx thing in the formula bar.

![](https://edbodmer.com/wp-content/uploads/2020/01/Circular-Sweep.jpg)

Case 4: More Complex Corporate Model with Taxes and Net Operating Losses
------------------------------------------------------------------------

With taxes, the taxes affect the cash flow, but the taxes are affected by the interest expense.  Here, the tax calculations must be part of the UDF.  The UDF function is demonstrated below the screenshot.  I hope that you can see that the formulas are just the same as the formulas in the spreadsheet with some convergence routines added.

![](https://edbodmer.com/wp-content/uploads/2020/01/Circular-Complex-Case.jpg)

Function average\_interest\_taxes(interest\_rate, cash\_flow, opening\_debt\_balance, tax\_rate, opening\_NOL\_Balance)

For Iteration = 1 To 30
last\_sweep = sweep

average\_interest\_taxes = ((opening\_debt\_balance + closing\_debt\_balance) / 2) \* interest\_rate

taxable\_income = cash\_flow - average\_interest\_taxes
NOL\_created = WorksheetFunction.Max(0, 0 - taxable\_income)
NOL\_used = WorksheetFunction.Min(opening\_NOL\_Balance, WorksheetFunction.Max(0, taxable\_income))
closing\_NOL\_Balance = opening\_NOL\_Balance + NOL\_created - NOL\_used
adjusted\_taxable\_income = taxable\_income + NOL\_created - NOL\_used
taxes\_paid = adjusted\_taxable\_income \* tax\_rate

sweep = WorksheetFunction.Min(cash\_flow - average\_interest\_taxes - taxes\_paid, opening\_debt\_balance)

closing\_debt\_balance = opening\_debt\_balance - sweep

Next Iteration

converge = Abs(sweep - last\_sweep)

If converge < 0.000001 Then Exit Function

End Function

Case 5: Interest During Construction with Loop
----------------------------------------------

This exercise demonstrates how to address the classic circular reference loop in a project finance model.  The screenshot below demonstrates how the debt size comes from the total cost which in turn comes from the interest during construction. Then, the pro-rata percent for determining how much debt is issue comes from a ratio of the total expenditures including IDC.  To solve this circular reference problem this time you need a loop.  With a loop you need to re-set things to zero and be more carefule with the order of things. The UDF function is in line 19 and is an array function.  Arguments for the UDF function include the debt to capital percent, the interest rate and the series of capital expenditures.

![](https://edbodmer.com/wp-content/uploads/2020/04/IDC-UDF-Example.png)

The circular reference is illustrated below.  The total debt drives the IDC which drives the pro-rata percentage.  The pro-rata percentage level then drives the IDC which in turn drives the pro-rata percent.  When the blue arrows go back and forth like they do in the diagram below, you probably need a loop to solve the problem.  You also need to put the output of the UDF into an array variable rather than a single variable. The file that has this example is attached to the button below.

**[Excel File with Simple Example of Solving Circular Reference from Interest During Construction with UDF](https://edbodmer.com/wp-content/uploads/2020/04/IDC-and-Dependents.xlsm)
**

![](https://edbodmer.com/wp-content/uploads/2020/04/Circular-IDC-1.png)

The code below illustrates computation of a UDF in the loop.  I have put comments in the loop.  Note that you do not need to put anything in the UDF to say that it is an array output.  Note also that the total debt is computed separately from the debt balance.

Option Base 1 ' Use option base 1

Function idc\_result(int\_rate, pct\_debt, cap\_exp) ' The output is an array variable

Dim idc(10) As Double ' Put arrays on variables you need to remember

For iter = 1 To 20 ' This is arbitrary; it should be modified to check convergence

      project\_cost = 0 ' Reset the project cost before the loop

     For i = 1 To cap\_exp.Count
         project\_cost = project\_cost + cap\_exp(i) + idc(i) ' Cap Exp is an array variable because of the way it is read in
     Next i

     debt\_balance = 0
     debt = project\_cost \* pct\_debt ' You need the project cost to get the debt

     For i = 1 To cap\_exp.Count
         uses = cap\_exp(i) + idc(i)
         pro\_rata = uses / project\_cost ' Compute the pro-rata
         draws = pro\_rata \* debt ' Draws from pro-rata

         idc(i) = debt\_balance \* int\_rate

         debt\_balance = debt\_balance + draws
     Next i

  Next iter

idc\_result = idc ' The result does not have to be an array

End Function

Case 6: Sculpting with Taxes
----------------------------

Sculpting with taxes creates a circular reference because the interest expense is deductible for taxes and the taxes drive the amount of CFADS which in turn drives the balance of debt

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1065&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10800&rand=0.5058995771826634)