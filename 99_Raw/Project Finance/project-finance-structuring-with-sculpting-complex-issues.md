# Project Finance Structuring with Sculpting — Complex Issues

**Source:** https://edbodmer.com/project-finance-structuring-with-sculpting-complex-issues

---

Developing a project finance model that can efficiently evaluate a debt structuring issues can be difficult. Videos and files on this page describe a series of issues associated with structuring that require more complex programming and financial equations. The project finance structuring and sculpting analysis below addresses incorporation of DSRA interest income, DSRA cash changes, DSRA L/C fees and balloon payments. If you really want to see how all of debt sculpting in project finance works you can torture yourself by working through the project finance debt sculpting videos and then trying the debt sculpting exercises.

There are a couple of key files where I put the financial formulas, modelling examples and the VBA code for cases where you run into circular references.  You can file these file on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  The files are available for download by pressing the button below.  The second file includes a function for determining the pattern of DSCR’s that achieve a target average loan life if the debt to capital constraint drives the size of the debt (sorry that this sounds like a foreign language).

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

Advanced Sculpting Exercise 1: Multiple Debt Issues and Balloon Payment
-----------------------------------------------------------------------

Very often, there is more than one debt isssue in project finance transactions. When there are multiple debt issues and one of the debt issues (defined as Last or the sculpting capture issue) is used for sculpting. In this case the basic formula can be adjusted and the process if straightforward. You can start with the DSCR formula and derived the debt service for the last formula. Note that if you are sculpting two debt facilities at the same time and these facilities have different interest rates and different tenures, then the process is difficult because for the NPV formula you need a common interest rate.  You can use the following equations to resolve the issue of multiple debt issues.  For the equations, the Other DS is the debt issue on the non-sculpted issue such as the balloon payment issue.  The Last DS is the debt issue that will be sculpted.

DSCR = CF/(Other DS + Last DS)

Other DS + Last DS = CF/DSCR

Last DS = CF/DSCR – Other DS

The modelling of multiple debt issues is illustrated in the screenshot below. Note that there are two debt issues and the first debt issue is entered separately.  If the debt is separated in this manner, developing sculpting is pretty easy.  The problem comes when the first issue is a function of the sculpting itself.  This is the issue with balloon payment.

![](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-3.jpg)

Note that if there is a bullet repayment at the end of the debt term (say 15% of the repayment), then the bullet repayment can be considered a separate debt facility. So, if the bullet repayment is 15% then the PV of the repayment is a separate facility with interest over time etc. The NPV of the remaining debt should subtract the interest and the repayment on this separate debt. Since the bullet repayment affects the amount of sculpting and the NPV of the debt multiplied by 15% drives the bullet repayment, the bullet repayment causes a circular reference.

You can see more details of how to model balloon payments in a separate section of the website.  The button below provides a link to the balloon repayment section which includes VBA necessary to make the models.

**[Go to the Website Page that Describes the Modelling of Balloon Payments and Includes VBA](https://edbodmer.com/ballon-payments-and-sinking-funds/)
**

Advanced Sculpting Exercise 2: Including Debt Fees after COD and Fees on an Letter of Credit that Replaces the Funded DSRA Account
----------------------------------------------------------------------------------------------------------------------------------

Before modelling, you should understand that a debt fee is just like interest expense from the standpoint of a bank.  You should compute the debt IRR which can also be called the all-in interest rate. Debt fees such as the fee on a letter of credit is part of debt service.

To include the fees in the sculpting equations, you should subtract the fees when you compute the net present value of debt. To illustrate this, assume that the interest rate is zero and there are only fees on debt.  If the interest rate was zero and there were no fees, then the present value of the debt payment would be the sum of the repayments. If there is interest or fees, less debt service can support the same amount of cash flow.  To compute the PV of debt service and reduce the debt service for fees, the PV of debt service computed without fees must be lowered for the fees.

as the fees reduce the amount of debt service that can be supported by cash flow. This is just the same as deducting the interest to come up with the repayment. The fees reduce the amount of debt associated with CFADS compared to a situation without fees. Because the PV of debt service uses the debt interest rate without the effective rate that accounts for fees (which would be a higher interest rate), you can deduct the PV of fees at the debt interest rate and the debt schedule will work. To make the sculpting work you should also make the repayment lower by the fees as shown below:

Repayment = CFADS/DSCR – Interest – Fees

Debt = NPV(Interest Rate, Debt Service-fees) = NPV(rate, Debt Service) – NPV(rate, Fees)

A simple case with zero interest rate and a five percent interest rate is illustrated in the two screen shots below.  The first screen shot shows that you can just add up the required debt service, then subtract the sum of the fees and the target DSCR of 1.5 will be achieved.

![](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-4.jpg)

The second screen shot demonstrates the case with a 10% interest rate.  There is lower debt in this case because of interest being paid, but the ideas are the same (the total debt amount falls from 480 to 332.

![](https://edbodmer.com/wp-content/uploads/2018/04/sculpting-5.jpg)

Very often in sculpting, the debt is given and the repayments must be sculpted. When the debt is given, the fees affect the synthetic LLCR that is used to compute the debt service from the CFADS. In this case, the amount of repayment must be reduced because of the fees and the synthetic LLCR should be reduced. The sculpting analyses include calculation of the LLCR to evaluate whether the debt to capital constraint is driving the constraint. In this case the PV of CFADS is not the correct numerator for the analysis. Instead, the PV of the LC fees should be added to the denominator of the LLCR as follows:

 LLCR = PV(CFADS)/(Debt + PV of LC Fees), where

Debt = Project Cost x Debt to Capital

A problem here is that the NPV of the debt depends on the fees, but the LC fees depend on the DSRA, which in turn depends on the size of the debt and the NPV. This is a clear circular reference. Note Debt Service in the above equation means debt service without fees and debt is reduced by PV of fees.

Advanced Sculpting Exercise 3: Interest Income on DSRA and Sculpting
--------------------------------------------------------------------

If the DSRA account or the MRA or any other reserve account is funded with cash and not a letter of credit, then the modelling can become painful if you do not use a UDF function.  This is particularly true for the DSRA account.  In the case of the DSRA account, interest income changes the CFADS and therefore changes the amount of debt. But when you change the amount of debt, the DSRA account changes.  Dreaded blue lines and a nasty circular reference. Many modellers just say that the interest income rate is so low that we should assume a zero rate. Maybe true.  But what about currencies where the interest rate is positive.  But what about when interest rates change. But why make such a simplifying assumption when you go crazy about other tiny assumptions like getting the days of interest correct.

Resolving the interest rate can be accomplished efficiently with a UDF.  With a copy and paste macro you would have to copy the entire line of interest income and then paste special.  It would then be part of the interation where you copy and paste multiple items …. A better method is to include interest income in a UDF and compute the DSRA.  The first time you try this it is a pain.  Eventually it should become easier. The trick is to model the DSRA account in a separate loop and keep track of the interest income in an array. The method for writing such VBA code is described in the  video below.

Advanced Sculpting Exercise 4: Change in the DSRA Balance with Sculpting when DSRA Changes are Included in CFADS
----------------------------------------------------------------------------------------------------------------

Perhaps the ultimate complex issue in sculpting and structuring is including changes in the DSRA account in CFADS and in the sizing of debt.  This issue can be relatively minor but it demonstrates a lot of programming and theoretical points.  So lets first discuss the theory.  If you are modelling MRA accounts, most would say that changes in the MRA should be included as CFADS.  This smoothes out the CFADS to account for capital expenditures for things like re-surfacing of a road. You can then say why not do the same with changes in cash associated with the DSRA account.  As the DSRA account will eventually be extinguished, including the changes in DSRA account will increase cash flow and allow for more debt.  It will thus make the DSRA a less painful item.

The above discussion is wrong. When you think about the DSRA you should think about the corporate concept of net debt and specifically that cash is tantamount to negative debt. When computing the LLCR, you should subtract the DSRA from debt and not add the DSRA to the present value of cash flow in the numerator consistent with the idea that cash is like negative debt. The same idea should be applied to computing the DSCR.  Instead of adding DSRA cash to the CFADS, the DSRA cash should be deducted from debt service.  This will increase the effect of the DSRA changes.  The same can be applied to the MRA cash. Maybe the best way to think about this is the large reduction in the DSRA that occurs at the end of the debt term. This money that is received from the DSRA should reduce the debt service on a one-for-one basis. If the change in the DSRA is deducted from the denominator, this happens.  If the DSRA change is in the numerator, the debt service is reduced only in part.

In terms of programming, you cannot try to force the CFADS and then apply some kind of copy and paste macro.  This will create a crazy cash flow.  Instead, you need to use some math.  To solve the problem with equations, you can compute the present value of the DSRA movements divided by the DSCR if you want to use the method at the beginning of the paragraph. Then, you can compute the PV of the debt service without the adjustment for the DSRA moves.  Finally, you can compute the repayments as the repayments for sculping without the adjustment, less the adjustment for the DSRA.  This is summarised below for the case where changes in the DSRA are treated like other cash flows and where the DSRA changes are treated as negative debt.

**Case 1: DSRA Changes Treated Like Other Cash Flow**

First, compute the NPV of DSRA moves (this only will really work with the UDF approach)

Second, Scult the Debt without DSRA moves (i.e. CFADS without DSRA Moves/DSCR)

Third, Compute the Debt Balance as Sculpt without DSRA – PV of DSRA Moves/DSCR

Fourth, Compute the Repayment as the Repayment from Sculpting Less the DSRA/DSCR

When the Debt to Capital is the Constraint, you need to make the following adjustments:

 .

**Case 2: DSRA Changes Treated Like Negative Debt**

First, compute the NPV of DSRA moves (this only will really work with the UDF approach)

Second, Scult the Debt without DSRA moves but do not divide by DSCR (i.e. CFADS without DSRA Moves)

Third, Compute the Debt Balance as Sculpt without DSRA – PV of DSRA Moves

Fourth, Compute the Repayment as the Repayment from Sculpting Less the DSRA

When the Debt to Capital is the Constraint, you need to make the following adjustments:

The effects of including the DSRA moves in the sculpting process is illustrated in screen shots below. In the first case the DSRA is not funded but instead an L/C is applied. You should look at the equity IRR.  You can press the check boxes and choose different methods.

![](https://edbodmer.com/wp-content/uploads/2018/04/DSRA-Sculpting-1.jpg)

In the next screen shot, a funded DSRA is applied, but the DSRA moves are not in the sculpting process.  This is the worst case for the DSRA from the perspective of the equity investor.  In this case the equity falls to a lower level. Note that the check box is unclicked. Not only is the IRR reduced to 12.09%, the debt to capital ratio is also reduced.  The DSCR is the same as the case with the letter of credit.

![](https://edbodmer.com/wp-content/uploads/2018/04/DSRA-Sculpting-2.jpg)

The third screenshot presents the case with the DSRA funded, but the DSRA moves are included in the DSCR using the mathematical equations shown above. In this case the equity IRR increases relative to the case without the DSRA being included. But the equity IRR is still below the best case where the Letter of credit is used instead of a funded DSRA account. In this case the debt to capital is somewhat higher than the case without making the adjustment.  Note that in these cases the Letter of credit fee and the interest income is not included.  Also note that the check box fir the DSRA in the CFADS is checked and also that the CFADS is increased in the final period.

![](https://edbodmer.com/wp-content/uploads/2018/04/DSRA-Sculpting-3.jpg)

 A couple of videos that work describe the process for sculpting. The first video works through the case where the DSRA moves are included as cash in the numerator of the DSCR.  The video does go into detail about how the VBA programming works, but describes the formulas and how to use the user defined function.

A second video explains the case where the DSRA moves are adjusted in the denominator of and the repayment rather than the numerator. In this case, the change in the DSRA affects the debt repayments on a one for one basis.  This means that if there is cash flow coming from the DSRA of 100, the debt repayments are lowered by 100. You could certainly argue that from a theoretical perspective, if the DSRA gives you cash, it should directly reduce the debt.

Sculpting with Non-Constant DSCR to Meet Debt to Capital Constraint and Average Loan Life Constraint
----------------------------------------------------------------------------------------------------

The sculpting methods discussed up to now use an LLCR method to sculpt debt when there is a debt to capital constraint.  For example, say the minimum DSCR is 1.3 and the maximum debt to capital ratio is 75%. Say also that the debt to capital constraint is in place. If you don’t know what this means, you need to review the debt to capital versus the DSCR sizing analysis in the advanced structuring section. This section will demonstrate that the average life of a credit facility can have a big effect on the ultimate equity IRR for the investor.

If the debt to capital constraint is limiting the debt size and then, you could increase the DSCR so as to achieve the debt to capital constraint. You can do this with the LLCR formula which is nice an elegant, but it may not fully reflect the structuring issues. If the DSCR is allowed to fall to the minimum level over the life of the project the DSCR does not have to be constant.  If the DSCR is allowed to be higher at the beginning of the debt life and then fall to the minimum level, then the payments in the early part of the life of the project are reduced. This means that a level or flat DSCR over the debt life at a higher level than the LLCR computed flat amount is optimal. This idea is demonstrated in a simple example below with screenshots.

The first screen shot shows various components of a term sheet. Note that the minimum DSCR is specified as well as the maximum debt to capital. In addition, the minimum average debt life is stated as a constraint.  In this term sheet, if the DSCR of 1.35 results in a debt to capital ratio of above 80%, then the debt to capital constraint will be in place.  The minimum and average DSCR from tailoring the debt are not specified, but it is possible that the minimum DSCR can be 1.35 and the average DSCR can be above 1.35 (like the LLCR).  In this case, the average debt life of 10 must be maintained. Note first the language about the DSCR language. The minimum and average cannot be below 1.35. But the minimum could be 1.35 and the average could be above 1.35.  This could be the case if the LLCR sculpting is above 1.35 as shown a little bit later:

![](https://edbodmer.com/wp-content/uploads/2018/05/Min-DSCR.jpg)

Note the how the maturity provision works.  If you mess around with the DSCR, the average life of the loan must still not exceed 10 years.  This means that you could have changing DSCR’s all over the place, but the minimum must still be 1.35.

![](https://edbodmer.com/wp-content/uploads/2018/05/Average-Life-in-Term-Sheet.jpg)

So, let’s take a case where the DSCR is 1.35, but if you use 1.35 in every year, then the debt to capital will be too high.  This applies the rule that the NPV of debt is from the DSCR and CFADS.  By constraining the debt, you could come up with the scenario below with where the LLCR is used as the target in sculpting.

To illustrate the process, you should understand how the average debt life works.  If the repayment occurs at the end of the period which is the standard approach you generally use in analysis and modelling, then the average loan life can be computed in two ways as follows:

1\. Sumproduct method: Multiply the period of the debt by the repayment for each period. Then sum the product and finally divide the product by the opening balance of the debt. This demonstrates that the average loan life is indeed the weighted average life of the repayments.

2\. Opening Balanec method: Sum the opening balance of the debt (it gets smaller as the debt is repaid). Divide the sum of the opening balance by the balance at COD.

In the case without debt constraint (where the debt is sized by the DSCR and not the debt to capital ratio), you can demonstrate the effect of the DSCR and the interest rate on the average loan life.  This is demonstrated in a data table below.

To illustrate this case, I begin with a case where the debt to capital constraint is in place (because of a high debt life, a long debt tenure or a low interest rate).

Instead, the DSCR could be gradually reduced to achieve the minimum DSCR level as illustrated in two screen shots below.  The first screen is the case where a flat DSCR is applied using the LLCR method.  The second case uses a curved DSCR where the DSCR is gradually reduced until the minimum is reached.  This case is structured so the average loan life criteria is still met.

Sculpting Discount Rate Adjustment with Monthly Periods but Semi-Annual Debt Periods
------------------------------------------------------------------------------------

When a monthly model is used but the debt repayment is semi-annual, the discounting can become more complicated. (Note that is is not a very common problem because you should usually put the timing in your model to correspond to the repayment dates of the debt). As usual, when you are working with interest rates you simply divide by the number of months in a period. However when you are discounting target debt service to arrive at the amount of debt, you need to use different discount rates. The adjusted equations for discounting the target debt service is shown below.

 Annual: Rate for Discounting in Semi-Annual Model = (1+Annual Rate/2)^(1/6)-1  
Monthly: Rate for Discounting = (1+Monthly/12)^(1/12)-1

Videos for sculpting lessons are divided into two sections. The first section is the comprehensive set of lessons that begins with a simple case and moves to complex and quite difficult issues. All of the videos in the top set refer to the file name “sculpting course final”. The second set of videos are a bit redundant and includes my earlier attempts to explain sculpting in a less organized manner. If you have the google drive, you can find the files in a sub-directory of Chapter 1 as shown below.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2722&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8616&rand=0.3743803553569043)