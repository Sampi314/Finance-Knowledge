# Lease Analysis

**Source:** https://edbodmer.com/lease-analysis

---

This sheet describes issues associated with modelling leases and the risks assocated with residual value. The lease analysis could apply to leases of batteries, leases of hydrogen equipment and corporate PPA’s which cover part of the lifetime of a solar or wind project. The analysis where different projects are put together with different lives and different contracts also applies to buildings and energy efficiency programs. To address different issues associated with modelling leases I begin by describing how to compute the lease rates given capital expenditures, the target IRR and an estimate of the residual value on this page. As with the discussion of levelised cost of electricity, . Once the lease rate is established through alternative structuring of the initial lease, risk analysis of the lease can be established. The risk analysis can include variation during the first term and the risk of residual value variation. Third, with the risk analysis established, taxes and actual data is introduced. Finally, the leases are put together into a portfolio. The file assocated with the analysis, macros and the videos below is attached to the button below.

.

**[Excel File with Analysis of Portfolio of Leases including Lease Structuring from Residual Risks of Degradation and Obsolesence](https://edbodmer.com/wp-content/uploads/2022/01/Lease-Analysis-Portfolio-Advanced-V3.xlsm)
**

.

**[Power Point Slides with Analysis of Portfolio of Leases including Discussion of Lease Structuring and Lease Risk Analysis](https://edbodmer.com/wp-content/uploads/2022/01/Lease-Analysis.pptx)
**

.

Analogy to Corporate PPA’s
--------------------------

A corporate PPA typically has a tenor that is less than the life of the plant (e.g. a solar project) . The IRR (and value) depends a lot on what happens after the PPA term (i.e., merchant prices). Another way to look at the value is to assess the value of a solar project at the end of the PPA term. If you have a value at the end of the tenor that is a lot higher than the value of building a new project, something is wrong.

*   There can be a lot of different structures for a corporate PPA:
*   Price at the hub (resource risk and basis price risk)
*   Fixed revenue contract (no resource risk)
*   Standard PPA type contract with fixed price per kWh úStandard PPA type contract with escalating prices

No matter what type of contract is initially used, the value after the contract depends on the physical operation of the plant and the market condition

*   Formula for achieving Target IRR:
*   **PV of Lease Payments in Initial Term + PV of Residual Value = Capital Expenditures**
*   Use the Target IRR as the Discount Rate
*   Do not Need Goal Seek
*   Value at Renewal Depends on degradation over first lease and expected degradation Obsolescence úInflation úCompetitive Conditions at end of lease term
*   Level Payment for Initial Lease (No Taxes): Need Capital Expenditures, Target IRR, Lease Term, Value at Renewal úTarget IRR can be adjusted later for degradation, inflation etc.
*   **PMT(Target IRR, Lease Term, Capital Expenditures – Value at Renewal)**

Step 1: Get the Level Lease Payment with PMT úFlat Nominal Lease = **PMT(Target IRR, Life, Capital Expenditure)**

Step 2: Find the Remaining Life after Initial Term úRemaining Life = Total Life – Lease Term

Step 3: Compute the Value at the Terminal Date with PV úSimple Residual = **PV(Target IRR, Remaining Term, Flat Nominal Lease)**

Step 4: Make a series of adjustments to Simple Residual for Obsolescence, Degradation and Inflation úAdjusted Residual = Simple Residual x Factors

Step 5: Compute Initial Lease Rate from Adjusted Residual using PMT úInitial Lease = **PMT(Target IRR, Lease Term, Capital Expenditure – Adjusted Residual)**

Making the SUM(Start:End!k10) Function Flexible
-----------------------------------------------

When you consolidate the different projects you can use the SUM function that grabs data from different sheets. But the

Sub sum\_fix()
Application.Calculation = xlCalculationManual
Dim new\_formula As String

start\_cell = Selection.Address

rows\_to\_adjust = Range("sum\_formulas").Rows.Count
Sheets("Consolidated").Select

For Row = 1 To rows\_to\_adjust
   `Range("sum_formulas").Cells(Row, 1).Select` 
   `current_formula = Selection.Formula`
    `If Left(current_formula, 2) <> "=S" Then GoTo end_of_loop: new_cell_reference = Range("sum_cells").Cells(Row, 1) new_formula = "=Sum(start:end!" & new_cell_reference & ")"`

     `Range("sum_formulas").Cells(Row, 1) = new_formula`
     end\_of\_loop:
Next Row

`Range("sum_formulas").Select Range(Selection, Selection.End(xlToRight)).Select Selection.FillRight`
Range(start\_cell).Activate
End Sub

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14874&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10200&rand=0.14544009775404332)