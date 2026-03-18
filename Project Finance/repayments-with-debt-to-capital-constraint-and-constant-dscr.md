# Debt to Capital Constraint and Constant DSCR

**Source:** https://edbodmer.com/repayments-with-debt-to-capital-constraint-and-constant-dscr

---

This page describes structuring and debt sculpting in project finance in the case where the debt to capital drives the size of the debt, but sculpting is still used. The discussion on this page addresses the special situation where the DSCR is adjusted upward and remains constant over the debt tenure to derive the debt repayment. The LLCR is the same as the period by period DSCR when sculpting is used to size the debt. This means the LLCR computed from PV of CFADS/Maximum Debt can be used as the basis for sculpting.  In this case the PV of the debt service using the LLCR to derive debt service results in the maximum debt. This page also describes the issue of sculpting when a grace period is allowed.  In this case the PV formulas must begin after the grace period. The case where DSCR is constant over the lifetime of the debt may not reflect actual term sheets.  Term sheets may allow a DSCR that is not constant over the debt term, but must not exceed a minimum level. But this case of constant DSCR is used as the basis to begin evaluation of sculpting in the case where the debt is fixed. More complex cases where the minimum DSCR and the average debt life is used to derive debt repayments are addressed in subsequent pages.

Developing a model that can efficiently evaluate how to structure repayments should begin with the idea that if the DSCR is constant over the loan life, then the DSCR equals the loan life coverage ratio. In terms of formulas:

DSCRt = CFADSt/Debt Servicet

If DSCR is constant, DSCR1 = DSCR2 = DSCR3 …. = DSCRtenor

LLCR = PV CFADS/ PV Debt Service

LLCR = PV CFADS/Debt

In this case LLCR = DSCRt

In terms of mecanics, use of LLCR and automatically changing from the debt to capital ratio to the DSCR method of debt sizing.

The file that includes sculpting in the situation where debt is fixes is available for download by pressing the button below.  The second file includes a function for determining the pattern of DSCR’s that achieve a target average loan life if the debt to capital constraint drives the size of the debt (sorry that this sounds like a foreign language).

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

**[Excel File that Sculpting Issues with Fixed Debt to Capital and Changing DSCRs Over the Tenor of the Loan and Multiple Issues](https://edbodmer.com/wp-content/uploads/2022/01/Mini-Grid-Financial-Model-Exercise.xlsx)
**

 Use of LLCR with Debt Capacity Constraint
------------------------------------------

One of the fundamental principles of project finance structuring is that debt size may be either driven by a maximum debt to capital constraint or a minimum DSCR.  If you do not fully understand this, you should not be making project finance structuring models. If the maximum debt to capital constraint limits the amount of debt rather than the DSCR as in the example above, then the formulas in the previous section will not work.

A typical situation in sculpting is where the debt to capital is given, but repayments are driven by sculpting. In this case you cannot input a DSCR which itself determines the debt size. Instead, you can use the idea the with sculpting, the LLCR = DSCR. Here, the issue is how to compute sculpted debt repayments when debt is sized with the debt to capital ratio and the DSCR is not given. When the Debt is Sized by Debt to Capital the LLCR = NPV(CFADS)/Debt can be used to size the debt, if you assume that the debt repayments will be structured to provide the same DSCR over time. Formulas in this case include two principles:

Principle 1: If the DSCR is constant in sculpting debt repayments, the LLCR is equal to the DSCR

Principle 2: The LLCR can be expressed as PV of CFADS/Debt

Using these two principles, you can derive the target DSCR using the above formula where the amount of debt is defined as the total project cost multipled by the maximum debt to capital ratio.  This is because the PV of debt service is equal to the debt at COD. Once you have the DSCR applied you can use this DSCR in sculpting:

**Target Debt Service = CF/LLCR**

**LLCR = NPV(Interest Rate, CFADS)/Max Debt from Debt to Capital**

**DSCR Applied = MAX(Target DSCR,LLCR with Max Debt)**

These equations are demonstrated in the screenshot below from the same sculpting file that is available for download from the button in the introductory section.  Note that this time you need to compute the PV of CFADS and not only the PV of the debt service. Once you compute the PV of the debt service, put it in the yellow slots.

![](https://edbodmer.com/wp-content/uploads/2018/06/Sculpting-2-1.jpg)

_**Important note: You do not necessarily have to assume that the repayments will be designed on a sculpted basis. Instead, you can design the sculpting so that the minimum DSCR will still be obtained, but that: (1) the total debt will be repaid (NPV of debt service) = debt; and (2) the average loan life is less than a specified loan life in the term sheet or loan agreement. You can go to a more advanced page to see how this can be accomplished.**_

The video below works through this example in case you need further explanation.  The video includes discussion of how you can make some kind of message that documents whether the DSCR constraint or the debt to capital constraint is operative.  In the circular reference complete template you can choose whether the debt to capital constraint is applied, the DSCR constraint, or both. Note the LLCR constraint as describe only works when the DSCR is constant over time.

.

Sculpting with Grace Period
---------------------------

If there is a grace period, the process for sculpting does not change much.  In the case with a grace period, the following two concepts should be applied:

1.  The PV of Debt Service is computed beginning in the period after the grace period.  This means the discounting should not apply a zero cash flow to the grace period.
2.  If the LLCR is used as described above, the PV of CFADS that is used as the basis for the LLCR should begin after the grace period.

An illustration of the first principle is demonstrated in the screenshot below. Note that when the PV of the debt service begins after the grace period, the closing balance correctly declines to zero.

![](https://edbodmer.com/wp-content/uploads/2018/08/Grace-Period-1.jpg)

An illustration of how to use the LLCR is shown in the second screenshot below.  Note that the PV of the CFADS excludes the grace period.

![](https://edbodmer.com/wp-content/uploads/2018/08/Grace-Period-2.jpg)

Playlist on Sculpting Issues
----------------------------

If you are in the mood for torture or maybe if you are having trouble sleeping, you can look through the sculpting playlist. I have put together various sculpting videos that I have made over the years. I have tried to put the more basic videos first (with the exception of the very first). The videos all apply the fundamental formula that the PV of debt service over the repayment period is equal to the debt size at the beginning of the repayment period (i.e. the period just prior to the commercial operation date). Over time I have learnt more about sculpting issues that can involve curved DSCR’s, multiple debt issues, incorporation of on-going fees, alternative debt sizing options, complex income taxes and computation of DSRA moves as part of the CFADS. I hope I have covered a lot of these issues in the videos. As with other items, you can always send me an email at edwardbodmer@gmail.com.

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3298&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7604&rand=0.06235438109047031)