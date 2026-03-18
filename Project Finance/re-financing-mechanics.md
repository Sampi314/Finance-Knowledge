# Re-financing Mechanics

**Source:** https://edbodmer.com/re-financing-mechanics

---

Re-financing can provide an important upside for equity investors in project finance. The conceptual idea is all about risk reduction and the debt providers giving you information about the risk of cash flow. On this page I include some mechanics of computing re-financing and illustrate some of the impacts. The first example is a case where you can evaluate re-financing of loans for small businesses. As with just about any re-financing analysis, you can go a long way with some flags for the re-financing period and flags for the new debt repayment period. In project finance, one of the essentials is to use the formula that the NPV of debt service is the amount of the debt. You can compute debt service as the cash flow divided by the DSCR which should naturally increase from a P90 level.

The first example below is re-financing a lot of loans in a database. This example illustrates how to use flags to compute the existing loan balance and the date of re-financing. The example also demonstrates how to use a macro with a for loop to manage a large amount of data. In the first page I present some generic assumptions with the date of re-financing and the interest rate on the re-financing along with data on the fees. The example also includes a simple technique to download data from a database.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image.png)

.

The database of loans is illustrated in the screenshots below. The idea is to compute the amount of remaining loan balance that is affected by interest rate changes, the tenor of the loan and the repayment. You can then use a macro to compute the re-financing amount and payment for each loan.

.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-1.png)

.

A summary of one loan with re-financing is shown below. You can use lookup and find the amount of the re-financing. This involves re-computing the payment in annual periods and re-computing the interest when the prime rate changes.

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-4.png)

.

![](https://edbodmer.com/wp-content/uploads/2025/04/image-5.png)

.

    Sub RunLoans()
    
    Dim total_loans As Single
    
    total_loans = InputBox(" Enter the total number of loans to evaluate ")
    
    
    For Row = 2 To total_loans
    
       [loan_num] = Row - 1
       
       UserForm1.Label1 = " Analysis of Loans and Re-financing " & Chr(10) & Chr(10) & _
                          " Loan Number " & Row - 1 & " Out of " & total_loans & " Total Loans" & Chr(10) & Chr(10) & _
                          " Loan Balance " & Format([outstand], "###,###") & " Refinanced " & Format([refinanced], "###,###") & Chr(10) & Chr(10) & _
                          " Prior Monthly Payment " & Format([cur_pay], "###,###") & " New Payment " & Format([refi_pay], "###,###")
                          
       DoEvents
       UserForm1.Repaint
       UserForm1.Show vbModeless
       
       Sheets("Loan Database").Cells(Row, 19) = [outstand]
       Sheets("Loan Database").Cells(Row, 20) = [cur_pay]
       Sheets("Loan Database").Cells(Row, 21) = [closing]
       Sheets("Loan Database").Cells(Row, 22) = [sba]
       Sheets("Loan Database").Cells(Row, 23) = [refinanced]
       Sheets("Loan Database").Cells(Row, 24) = [refi_pay]
       
    
    Next Row
    
    Unload UserForm1
    
    End Sub
    
    .
    

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=18063&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=20260&rand=0.4259658729629823)