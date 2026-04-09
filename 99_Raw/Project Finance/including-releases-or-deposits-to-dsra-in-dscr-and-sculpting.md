# DSRA Cash Flow Movement and Sculpting

**Source:** https://edbodmer.com/including-releases-or-deposits-to-dsra-in-dscr-and-sculpting

---

This page discusses treatment of cash flow that comes from changes in the DSRA when sizing debt from sculpting with a given DSCR. If cash flow from changes from the DSRA account result in positive effects on the CFADS, meaning that the DSRA is reduced through withdrawals from the bank account, then some would argue (correctly) that this cash flow should be included in calculation of the DSCR. If the cash that is made available from reduction in the DSRA is included in the CFADS, then that cash flow should also be included in the sculpting calculations and increase the size of the debt. The biggest positive cash flow will typically come at the maturity of the debt when the DSRA is extinguished meaning that you have a bump in cash flow in that period and you should be able to use this cash flow to repay debt. After all, CFADS is cash that is available to pay debt service and the reduction in the DSRA is cash that is available to pay debt service. Similarly, if the DSRA account is required to be increased (because CFADS and therefore debt service is increasing) and you must deposit cash into the DSRA bank account, one could argue that CFADS and the DSCR should be reduced. Including deposits or withdrawals from the DSRA in the calculation of repayments with sculpting and the DSCR is not easy from a mechanical perspective and it can can cause painful circular reference issues.

I have struggled with this issue for a long time. But after trying absurdly complex things, I have come up with the following step by step process that is relatively simple. This process separately computes the debt from non-DSRA changes like EBITDA and taxes. The DSRA is computed on this amount of debt and that does not include the debt itself. This step by step process is summarised below:

|     |
| --- |
| Step 1: Compute DS and PV of DS from EBITDA |
| Step 2: Compute DSRA Balance and Flows from Step 1 Debt |
| Step 3: Compute PV of DSRA Change/DSCR for Added Debt |
| Step 4: Add Debt Service from Step 1 and Step 3 for Sculpting |

Many years ago I had a very smart student who explained to me that in a PPP project with a tight debt service coverage, including changes in the DSRA in the DSCR can be an important issue in financial models. He told me that my class sucked because I did not include this or other complex issues in my models. I then became obsessed putting changes in the DSRA into CFADS for years.  But when trying a copy and paste macro or a UDF to resolve the fact that the DSRA is driven by debt but the debt is driven by CFADS, the process blew up. Later, another student told me that the DSRA balance can be used to pay debt service in the final year.  This is a variation of the same issue. Here, the last period change in DSRA is the repayment of the DSRA and this change can be included in sculpting. This again caused some nightmare circular reference issues. A file that illustrates resolution of the DSRA movement and sculpting issues is attached to the button below. The first button is a very simple example with a completed exercise and with a blank exercise.

.

**[CFADS Exercise where the DSRA change is Included in the Computation of CFADS for Sculpting](https://edbodmer.com/wp-content/uploads/2023/01/DSRA-Change.xlsx)
**

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-1.png)

.

**[Excel File with Analysis of Changes in DSRA to be Included in CFADS for Sculpting with DSRA Changes Independent](https://edbodmer.com/wp-content/uploads/2021/09/DSRA-Test-with-Template.xlsm)
**

•Use the Following Step by Step Process:

*   Compute debt size and sculpting as normal
*   Compute the DSRA from the debt size without DSRA itself 
*   Compute the changes in the DSRA
*   Compute the debt service effects of the DSRA through dividing by the DSCR Add the Debt Service from the base components and the DSRA
*   Compute the PV of the total debt service 
*   Verify the DSCR and the debt balance

.

.

The Key to Evaluating DSRA Changes, Compute the DSRA without the DSRA Changes Themselves
----------------------------------------------------------------------------------------

To see the problem with including DSRA changes in the calculation of the DSCR, you can begin with the end and not the beginning. The problem is that in the very last period there is a really big increase in the debt service because the cash in the DSRA is used to pay that last installment of debt. But now we have the problem. This big increase in debt service in theory would cause a really big increase in the DSRA in the second to last period. In this second to last period, the increase in the DSRA is a negative cash flow and it causes a big reduction in debt service. This causes an impossible situation. I demonstrate this below with some simple examples and I argue that the DSRA changes must be computed without this bouncing around, meaning that the DSRA should be computed from the sculpting without the DSRA.

#### Formulas Demonstrating DSRA Changes in the Last Period

In the formulas below I work through the debt service for the very last period where there is high cash flow from availability of the DSCR. I use EBITDA for cash flow and you can see that with the DSRA moves the formula for debt service is EBITDA/(DSCR – 1) instead of EBITDA/DSCR for the very last period. This means the project can support much more debt service in the last period.

DSRA Move (Negative Increases Cash Flow) = Debt Service Next – Debt Service Current

Last Period

*   DSRA Move = 0 – Debt Service Current
*   Debt Service = (EBITDA – DSRA Move)/DSCR
*   Debt Service = (EBITDA + Debt Service)/DSCR
*   Debt Service \* DSCR = EBITDA + Debt Service
*   Debt Service \* DSCR – Debt Service = EBITDA
*   Debt Service \* (DSCR -1) = EBITDA
*   Debt Service = EBITDA/(DSCR -1)

The example below the EBITDA is 400, but the DSRA change is 800 because debt service in this period was 800. This allows cash flow of 1,200 and the debt service of 800. This debt service of 800 had to be in the DSRA account that looks forward. As the DSRA at the end of the period is zero, the move in the DSRA is 800.

.

![](https://edbodmer.com/wp-content/uploads/2021/09/image.png)

#### Formulas Demonstrating DSRA Changes periods before the Last Period

Now lets move to the period before the last period. In this period the DSRA must be 800 at the end of the period. In the prior period it is the current debt service so the formulas for the DSRA moves are different. You can try to keep moving back but it will be a big mess. In this case the DSRA moves are positive instead of negative. It means that the debt service will be low and you have a situation with a very high debt service in the final period and a very low (negative) service in the earlier year. In the formula, the DSRA move will be positive and reduce the cash flow.

*   DSRA Move = Debt Service Next – Debt Service
*   Debt Service = (EBITDA – DSRA Move)/DSCR
*   Debt Service = (EBITDA – Debt Service Next + Debt Service)/DSCR
*   Debt Service \* DSCR = (EBITDA – Debt Service Next + Debt Service)
*   Debt Service \* DSCR – Debt Service = (EBITDA – Debt Service Next )
*   Debt Service \* DSCR – Debt Service = (EBITDA – Debt Service Next )
*   Debt Service \* ( DSCR – 1) = (EBITDA – Debt Service Next )
*   Debt Service = (EBITDA – Debt Service Next ) / (DSCR – 1)

When you go backwards and apply these formulas, you can see how the DSRA move bounces around. The debt service bounces around like this because the DSRA is computed on the total debt service. If the DSRA was computed on the EBITDA/DSCR, the bouncing around would not occur and you could make the calculations.

.

![](https://edbodmer.com/wp-content/uploads/2021/09/image-1.png)

.

Resolving the DSRA Cash Issue by Computing the DSRA Changes on the Sculpted Debt Without the DSRA Changes
---------------------------------------------------------------------------------------------------------

Developing a project finance model that can evaluate the effects of including DSRA deposits and releases in the DSCR and either CFADS or Debt service are discussed below.  Videos and files on this page describe how to resolve this problem with some NPV formulas that adjust the size of debt for purposes of sculpting. If you really want to see how all of debt sculpting in project finance works you can torture yourself by working through the project finance debt sculpting videos and then trying the debt sculpting exercises. I have modified the worksheet in evaluating the issue further. The revised model is attached to the button below.

There are a couple of key files where I put the financial formulas, modelling examples and the VBA code for cases where you run into circular references.  You can find these files on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  The first file is the sculpting file that includes a separate section that isolates on the issue of DSRA changes.  The second file is a model with the comprehensive parallel UDF.

.

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

.

Theory of How to Treat DSRA Deposits and Withdrawals and Simple Examples
------------------------------------------------------------------------

Perhaps the ultimate complex issue in project finance modelling is including changes in the DSRA account in CFADS and in the sizing of debt.  This issue can seem relatively minor from a structuring standpoint, but it illustrates a lot of programming and theoretical points.  So lets first discuss the theory.  If you are modelling MRA accounts, most would say that changes in the maintenance reserve account — the MRA — should be included as CFADS (when you deposit money in an account, you should treat it like a cash outflow; when you take money out of the account to pay for extraordinary maintenance, you should treat the money you take out of the MRA account, you should treat it like a cash inflow for purposes of computing CFADS and the DSCR).  This treatment of MRA flows will smooth out the CFADS to account for capital expenditures for things like re-surfacing of a road. You can then say why not do the same with changes in cash associated with the DSRA account, and you would be largely correct.  As the DSRA account will eventually be extinguished, including the changes in DSRA account will increase cash flow and allow for more debt.  It will thus make the DSRA a less painful item.  

You could also argue that the above discussion is all wrong and changes in the DSRA should be treated as debt service in the denominator and not cash flow in the numerator. When you think about the DSRA you could think about the corporate concept of net debt and specifically the notion that cash is tantamount to negative debt. It is very standard to treat cash as negative debt in corporate finance; this includes treatment of interest income and debt repayments — both of which are financing flows and not operating flows. For example, when computing the LLCR as the present value of cash flow divided by debt, you should subtract the DSRA from debt in the denominator and not add the DSRA to the present value of cash flow in the numerator. This is consistent with the idea that cash on the balance sheet (and that is dedicated to debt repayment) can be called negative debt. The same idea should be applied to computing the DSCR. .  

**LLCR = PV of Cash Flow over Debt Repayment/(Debt – DSRA Balance)** .  

If you agree with this idea, instead of adding DSRA cash to the CFADS, the DSRA cash should be deducted from debt service.  This will increase the effect of the DSRA changes. 

Maybe the best way to think about this is the large reduction in the DSRA that occurs at the end of the debt term. This money that is received from the DSRA should reduce the debt service on a one-for-one basis. If the change in the DSRA is deducted from the denominator, this happens.  If the DSRA change is in the numerator, the debt service is reduced only in part depending on the DSCR. For example if the DSCR is 1.5, then the DSRA cash will only produce 50% of a reduction in required debt service.  

In terms of programming a financial model, you cannot try to force the CFADS and then apply some kind of copy and paste macro if you want to apply the formulas.  This will create a crazy cash flow as there will be a really large reduction in debt service in the last period and it will continue to magnify.  Instead, you need to use some math and follow the following steps:

*   Step 1: Compute the DSRA movements using debt service that is computed from sculpting and not the final debt service that is computed with the DSRA moves.
*   Step 2: Compute the present value of the DSRA movements (discounted at the debt interest rate or the debt IRR) divided by the DSCR (that is, if you want to use the method at the beginning of the paragraph where the DSRA movements are in cash flow.)
*   Step 3: Compute the PV of the debt service without the adjustment for the DSRA moves as you would normally do — i.e. compute the CFADS without the debt service reserve account moves and use this with a PV formula.
*   Step 4: Finally, you can compute the debt repayments as the repayments for sculpting without the adjustment, but then you later make the adjustment for the DSRA. You do this outside of the debt sculpting process. 

This four step process is summarized below for the case where changes in the DSRA are treated like other cash flows and where the DSRA changes are treated as negative debt.  The key is to not include the changes in the DSRA, which is the theoretically correct thing to do.    

.

Change in the DSRA Balance with Sculpting when DSRA Changes are Included in CFADS
---------------------------------------------------------------------------------

.

The key for incorporating changes in the DSRA account into sculpting is to split the problem into parts as summarized above. In this explanation, I repeat things, but I include formulas and screenshots.

First, you evaluate the sculpting formulas as if there were no movements in the DSRA as normal.  The two key formulas are:

*   Target Debt Service = CFADS without Changes in DSRA/DSCR
*   Debt = PV of Debt Service

The process for this calculation is shown below using the file that you can download with the above button. Note that the taxes are part of the sculpting computation and a debt balance account is computed for this standard sculpting.

.

![](https://edbodmer.com/wp-content/uploads/2021/09/image-2.png)

.

Second you compute the DSRA from the debt service from this sculpting that does not include the DSRA adjustment. Make sure to separate DSRA flows before and after COD. Just use flows after COD. Note that you could compute the DSRA using other methods, but you cannot use the DSRA moves itself for the last period in the computation. Otherwise you will have the endless bouncing around. The formulas are:

*   DSRA = Prospective Debt Service – Current Debt Service
*   Prospective Debt Service is from Step 1
*   Current Debt Service is from Step 1

.

![](https://edbodmer.com/wp-content/uploads/2021/09/image-3.png)

.

Third, make an adjustment to the debt size because of added cash flow that comes from the DSRA releases. This is the total debt plus the PV of DSRA changes.  You can compute the debt service effects of the DSRA changes using the DSCR as you normally would through dividing the cash flow from DSRA changes by the DSCR. Then you compute the NPV of the debt service using the interest rate on the debt. This is illustrated by the formulas below:

*   DSRA Changes Debt Service = DSRA Change/DSCR
*   PV of DSRA Changes Debt Service = Debt Effect of DSRA
*   Repayment of Debt from DSRA Changes = Debt Service – Interest

The screenshot below shows you you can compute a little separate debt facility for the DSRA Changes with the affected repayments and interest. In this example I have a very high growth rate that increases the DSRA requirements before the last period.

.

![](https://edbodmer.com/wp-content/uploads/2021/09/image-4.png)

.

Fourth, Put the repayment from the DSRA and the standard sculpting together and put the total debt together and run the rest of the model. Finally make sure that the combined debt service and the CFADS using the DSRA results in the targeted DSCR. This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2021/09/image-5.png)

Legacy Discussion
-----------------

There are two ways the DSRA could apply are to treat the cash flow like operating cash flow (Case 1) or to treat the cash flow as a reduction in debt service (Case 2).  For each of the cases the, the method for computing repayments in the case where the DSCR drives the debt size and the method where the debt size is given and the debt is sculpted.     **Case 1: DSRA Changes Treated Like Other Cash Flow and Debt Sizing from DSCR**

*   First, compute the NPV of DSRA moves (this only will really work with the UDF approach) and divided the NPV by the DSCR — the formula is NPV(interest rate, DSRA Moves)/DSCR.
*   Second, Sculpt the Debt without DSRA moves (i.e. CFADS without DSRA Moves/DSCR)
*   Third, Compute the Debt Balance from Sculpting without DSRA and subtract PV of DSRA Moves/DSCR: Debt Balance = NPV(Interest Rate, Debt Service from Normal CFADS) + PV of DSRA Moves/DSCR
*   Fourth, Compute the Repayment as the Repayment from Sculpting Less the DSRA Moves/DSCR

This method is illustrated in what I thought was a simple example below where the interest rate is zero and the moves in the DSRA are only for releasing the DSRA at the end of the debt term. There are only two years of cash flow. In the example below, note that the 100 of DSRA is divided by the DSCR of 1.5 to arrive at the amount for sculpting, which is 67. This example needs some explaining.  First, there are two years of cash flow when you exclude the DSRA payments.  With a zero interest rate, the PV of the CFADS is 1,20 as shown above.  The target DSCR is given as 1.50.  This means that without consideration of the DSRA moves in sculpting, the target debt service is 400.  Without the DSRA, the present value of this debt service is 400 plus 400 or 800. I assumed the DSRA is 67 (I don’t know why I did not assume a half year of debt service or 200).  So, if we apply the formula above, we get the following:  

1.  **PV without DSRA = Sum of 400 + 400 = 800**
2.  **PV of DSRA = 100/1.5 = 67**
3.  **Total Debt = 800 + PV of DSRA = 800 + 67 = 867**
4.  **Repayment = Base Repayment + DSRA Adjustment = 400 in year 1 and 400 + 67 in year 2**

When you apply these formulas, you arrive at the correct closing balance and the correct DSCR where the DSCR = (EBITDA + DSRA Flows)/Debt Service. For the first year the DSCR = 600/400 which is 1.5 — that is easy.  For the second year, the DSCR = 700/467 = 1.5, which is DSCR = EBITDA/(Base DS + DSRA DS).   This was a real pain, even in the simple example.  But it is a solvable problem.  The problem is solvable even with multiple periods; with taxes and interest deductions; with different DSRA sizing and with changing DSCR’s.  But you do need to separate the process and add the DSRA PV and the DSRA/DSCR separately.  

![](https://edbodmer.com/wp-content/uploads/2018/06/DSRA-Moves-1-1.jpg)

**Case 1a: DSRA Changes Treated Like Other Cash Flow and Debt Size Given  
**  When the Debt to Capital ratio is the constraint used to size the debt, the equations are similar, but you need to adjust the LLCR that you use for sculpting:

*   **First, compute the NPV of DSRA moves; for this you may need to compute the DSRA separately from the debt service  (this only will really work with the UDF approach)**
*   **Second, compute the LLCR that will yield the correct debt balance with which allows DSRA changes to be included.  This is LLCR = PV (CFADS+DSRA Moves)/Debt — when you think about this formula, you have more debt because of the DSRA that will provide you some money.  In this case, the debt is fixed and you do not make an NPV adjustment.  When you are using the non-constant or non-constant DSCR, you will have to make an adjustment to the goal seek.**
*   **Third, compute the repayment using the process where you make a calculation without the DSRA adjustment and you separately add the adjustment. This adjustment is the Repayment from Sculpting Less the (CFADS/LLCR) and later add the DSRA Move/LLCR to the repayment**

![](https://edbodmer.com/wp-content/uploads/2018/06/Simple-DSRA-Move-3.jpg)

       .   **Case 2: DSRA Changes Treated Like Negative Debt**   First, compute the NPV of DSRA moves (this only will really work with the UDF approach)   Second, Sculpt the Debt without DSRA moves but do not divide by DSCR (i.e. CFADS without DSRA Moves)   Third, Compute the Debt Balance as Sculpt without DSRA – PV of DSRA Moves   Fourth, Compute the Repayment as the Repayment from Sculpting Less the DSRA   When the Debt to Capital is the Constraint, you need to make the following adjustments:      

Illustration of Alternative Methods in Cash Flow
------------------------------------------------

The screenshot below demonstrates how different methods could be presented in the cash flow statement.  For the method where DSRA moves are ignored in computing the DSCR and evaluating sculpting, the DSRA changes are shown at the bottom of the cash flow statement.  In the case where DSRA changes are treated like other cash flows, the DSRA changes are part of CFADS.  In this case a reduction in the DSRA account is treated as positive cash flow for purposes of computing the DSCR and sculpting. In the final year the cash flow is much higher and the debt service requirement may be negative. For the third case where the changes in DSRA are treated like negative cash flow using the concept of net debt, the DSRA changes in the debt service section of the cash flow.

![](https://edbodmer.com/wp-content/uploads/2018/06/DSRA-Moves-Cash-Flow.jpg)

    The effects of including the DSRA moves in the sculpting process is illustrated in screen shots below. In the first case the DSRA is not funded but instead an L/C is applied. You should look at the equity IRR.  You can press the check boxes and choose different methods.   In the next screen shot, a funded DSRA is applied, but the DSRA moves are not in the sculpting process.  This is the worst case for the DSRA from the perspective of the equity investor.  In this case the equity falls to a lower level. Note that the check box is unclicked. Not only is the IRR reduced to 12.09%, the debt to capital ratio is also reduced.  The DSCR is the same as the case with the letter of credit.       The third screenshot presents the case with the DSRA funded, but the DSRA moves are included in the DSCR using the mathematical equations shown above. In this case the equity IRR increases relative to the case without the DSRA being included. But the equity IRR is still below the best case where the Letter of credit is used instead of a funded DSRA account. In this case the debt to capital is somewhat higher than the case without making the adjustment.  Note that in these cases the Letter of credit fee and the interest income is not included.  Also note that the check box fir the DSRA in the CFADS is checked and also that the CFADS is increased in the final period.        

Cannot Include Debt Service Effects of DSRA Changes in the DSRA Itself from Either a Theoretical or a Practical Standpoint
--------------------------------------------------------------------------------------------------------------------------

The DSRA balance comes from debt service. With sculpting and changes in the DSRA included in CFADS, the size of the DSRA is driven by the debt service but the debt service comes from the DSRA.  This idea does not make sense and the change in DSRA that is part of debt service should not be included in the DSRA itself.

Consider a simple example. You need liquidity for a trip — some cash in case things can go wrong.  After the trip, you will not need the cash.  You need to decide how much liquidity you will need from your fixed costs.  At the end of the trip you can subtract the money you have in the bank for liquidity from the fixed costs.  The liquidity is the DSRA and the fixed cost is the debt service.  Assume your fixed cost is 100 for three months — a long trip.  Assume you need to put aside 100 for the trip. If the liquidity requirement is reduced for the last period, then the fixed cost is reduced to zero and you don’t need the liquidity anymore. This does not make sense.  The fixed costs still exist and the liquidity account must not be distorted by changes in the account itself.

Video Discussion of DSRA Changes and Sculpting
----------------------------------------------

   A couple of videos that work describe the process for sculpting. The first video works through the case where the DSRA moves are included as cash in the numerator of the DSCR.  The video does go into detail about how the VBA programming works, but describes the formulas and how to use the user defined function.  

A second video explains the case where the DSRA moves are adjusted in the denominator of and the repayment rather than the numerator. In this case, the change in the DSRA affects the debt repayments on a one for one basis.  This means that if there is cash flow coming from the DSRA of 100, the debt repayments are lowered by 100. You could certainly argue that from a theoretical perspective, if the DSRA gives you cash, it should directly reduce the debt.  

![](https://edbodmer.com/wp-content/uploads/2019/05/DSRA-Sculpting-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/DSRA-Sculpting-2.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/DSRA-Sculpting-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/Sculpting-and-DSRA-1.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3336&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7808&rand=0.7659863251358885)