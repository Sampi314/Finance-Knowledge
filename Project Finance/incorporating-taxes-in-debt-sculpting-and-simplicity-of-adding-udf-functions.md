# Taxes in Sculpting and Circularity

**Source:** https://edbodmer.com/incorporating-taxes-in-debt-sculpting-and-simplicity-of-adding-udf-functions

---

This webpage addresses the problem that occurs when taxes are included in sculpted debt analysis. With the payment of corporate income taxes the issue of sculpting changes from a simple matter of evaluating a couple of mathematical formulas (debt service = CFADS/DSCR and PV of Debt Service = Debt), into a circular reference issue.  The problem arises because income taxes are deducted in computing CFADS. But the income taxes are affected by interest expense and therefore the level of debt. I discuss the issue of this circular reference below and show how you can solve the issue with a copy and paste macro or a user defined function.

There are a couple of key files where I put the financial formulas, modelling examples and the VBA code for cases where you run into circular references.  You can file these file on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  Some of the files are available for download by pressing the button below.  The second file includes the comprehensive circular reference resolution (sorry that this sounds like a foreign language). If you solve the taxes with a copy and paste macro, then you can go the tax calculation row of the model and then write a copy and paste macro. As with other copy and paste macros, copy from computed to fixed (in the VBA just use something like \[fixed\_tax\].value = \[compute\_tax\].value) and then compute the difference between the fixed and computed taxes in each period. Finally, you can sum the differences and use the difference in the do while loop (Do While \[difference\_tax\].value <> 0, or Do Until \[difference\_tax\].value = 0.

.

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

.

Sculpting and Circularity from Income Taxes with Deductible Interest
--------------------------------------------------------------------

I have recently heard from some people that taxes are just too complicated to incorporate in the UDF method.  This is complete BS.  As with other items, as long as you can work through the stuff in excel, you can easily replicate the formulas in a UDF function.  Once again, the important thing is that you understand how taxes work, which items are deductible (the problem is that interest and fees are deductible and CFADS is after tax).  Incorporating a NOL calculation into the UDF is also easy. Indeed, if the only problem you are having with circular references is tax (which is very unlikely in a sophisticated model), then you should be able to write a UDF function for solving the problem in a few minutes.

I have included two videos below that demonstrate how to write a UDF to deal with taxes.  The first video is very simple and does not even include depreciation.  The second is a bit more complex with depreciation added in the equation.

.

Sculpting With Taxes when Debt Amount is Fixed
----------------------------------------------

.

If the amount the debt is fixed and the period by period DSCR or the LLCR is derived, the circular reference from interest, debt balance and taxes does not go away. You can go to another page and find how to use the LLCR method to compute debt size or if you are basic, you can use a MIN function in the debt schedule. In this case the LLCR drives the debt service, but the debt service affects the tax and the CFADS. The PV of CFADS can be fixed with a copy and paste macro or a function can be used that is similar to the function in the case when the debt is not fixed.

.

Technical VBA Issues, Sculpting and Taxes
-----------------------------------------

.

After a very simple case where circular references can be resolved without taxes, the case of sculpting and taxes is perhaps the simplest case of resolving a circular reference with a loop. This occurs because you have to work through the lifetime of the loan to establish the present value of debt service (which in turn comes from CFADS).  This is because the interest expense and therefore tax depends on the loan size.  But the interest expense and loan size also depend on the period by period CFADS.  So, you can create a loop as shown in the code below that works through the CFADS and the tax payment.  On top of this loop you can create an iteration loop that re-computes debt from the tax payments.

The box below demonstrates the VBA code you can create to resolve the tax circularity issue.  Note first that the EBITDA is read into the function as a vector.  This means in the function the EBITDA has an index and is an array.  A second point is that interest expense is computed first followed by taxes and finally by the CFADS. Finally, the target debt service, the repayment, the NPV of the debt service and the debt balance is computed.  These elements should be present in any

Function npv\_taxes(int\_rate, ebitda\_vector, tax\_rate, dscr)

Dim debt\_service(100)

For iter = 1 To 10
 For i = 1 To ebitda\_vector.Count
   interest = debt\_balance \* int\_rate
   ebt = ebitda\_vector(i) - interest
   taxes = ebt \* tax\_rate
 
   cfads = ebitda\_vector(i) - taxes
   debt\_service(i) = cfads / dscr
   repayment = debt\_service(i) - interest
   debt\_balance = debt\_balance - repayment
 Next i
 
 debt\_balance = WorksheetFunction.NPV(int\_rate, debt\_service)
Next iter

npv\_taxes = debt\_balance

End Function
.

  When you make a UDF like this for taxes, you need to include all the stuff that goes into the tax calculation.  If there  in mezzanine debt that has interest deductible for interest, this must be included; if there is a limit on the taxes as a function of EBITDA, this must be included; if there is an NOL this must be included; if the NOL has an expiration (one of the really tricky modelling issues), this must be included.  The video below illustrates this process with only tax depreciation.  

 

.

Playlist on Sculpting Issues
----------------------------

.
-

If you are in the mood for torture or maybe if you are having trouble sleeping, you can look through the sculpting playlist. I have put together various sculpting videos that I have made over the years. I have tried to put the more basic videos first (with the exception of the very first). The videos all apply the fundamental formula that the PV of debt service over the repayment period is equal to the debt size at the beginning of the repayment period (i.e. the period just prior to the commercial operation date). Over time I have learnt more about sculpting issues that can involve curved DSCR’s, multiple debt issues, incorporation of on-going fees, alternative debt sizing options, complex income taxes and computation of DSRA moves as part of the CFADS. I hope I have covered a lot of these issues in the videos. As with other items, you can always send me an email at edwardbodmer@gmail.com.

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3305&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.9164148880803242)