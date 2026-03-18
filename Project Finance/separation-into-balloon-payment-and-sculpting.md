# Separation into Balloon Payment and Sculpting

**Source:** https://edbodmer.com/separation-into-balloon-payment-and-sculpting

---

This page explains structuring and modelling of debt issues where a portion of the repayment is structured as a balloon payment.  A balloon payment is a cousin of a mini-perm where there is a separate amortisation period and maturity.  In the balloon payment case, the maturity is defined and a portion of the debt repayment occurs at the maturity date.  In the case where there is one debt issue with a balloon payment and sculpting, the balloon payment can be split from the rest of the debt issue and then be modelled as a two different debt issues, one of which operates as the sculpted debt issue.

Modelling Balloon Payments or Mini-Perm with Sculpted Debt Issues
-----------------------------------------------------------------

If there is a bullet repayment at the end of the debt tenure (say 15% of the repayment), then the bullet repayment can be considered a separate debt facility. So, if the bullet repayment is 15% then the PV of the repayment is a separate facility with interest over time etc. The NPV of the remaining debt should subtract the interest and the repayment on this separate debt. Since the bullet repayment affects the amount of sculpting and the NPV of the debt multiplied by 15% drives the bullet repayment, the bullet repayment causes a circular reference.

**[Go to the Website Page that Describes the Modelling of Balloon Payments and Includes VBA](https://edbodmer.com/ballon-payments-and-sinking-funds/)
**

### Computing Sculpting DSCR (LLCR for Sculpting) with Balloon Payments

If the amount of debt is fixed (maybe because of a debt to capital constraint) and the repayments are computed from the sculpting LLCR producing a constant DSCR, then a few adjustments must be made compared to the fundamental LLCR formula: PV CFADS/Debt. In the case of a debt issue with a balloon repayment, if you want the amount of repayments to add up to the loan including the repayment.  But the sculpted repayments must be reduced because of the balloon payment. Here then the LLCR that is used for sculpting will be lower than it would be without the balloon payment.  This is because the the addition of the repayments must sum to a lower amount that excludes the balloon payment.  If the sum must be lower and the CFADS is the same, then the denominator must be higher.

To explain concepts like this I use an absurdly simple example.  Assume that the interest rate is zero, the project cost is 1000 and CFADS is 600 for only two years.  The reason for assuming a zero interest rate is that you can compute the NPV by a simple sum and that the debt service is just the repayments.  In the case without the balloon payment, the LLCR is 600 x 2 divided by the assumed debt of 800.  This produces an LLCR of 1.5 as shown in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2018/06/1a.-Simple-Case-with-No-Balloon.jpg)

The second screenshot shows the same case that includes a balloon payment.  In this case, the LLCR increases to 1.85 which produces an amount of debt of 650 instead of 800.  The screenshot illustrates that the formula for the LLCR with balloon payments or for other debt can be expressed as follows:

**LLCR = PV of CFADS/(Sculpted Debt – PV of Non-Sculpted Debt)**

![](https://edbodmer.com/wp-content/uploads/2018/06/1.-Simple-Case-with-Balloon.jpg)

If there is interest on the balloon debt or the non-sculpted debt, the formula for the LLCR in the above simple examples is not correct.  For an issue with a balloon payment, to the extent that the balloon repayments are not included in the sculpting formula, the balloon repayment should be expressed in terms of present value.

![](https://edbodmer.com/wp-content/uploads/2018/06/1.-LLCR-with-Interest.jpg)

You can also compute the adjusted DSCR for sculpting.  In this case you can make an adjustment for the balloon payment and for the other debt service in an adjusted DSCR formula.

**Debt Service Adjusted = Total CFADS / Input DSCR – Non Sculpt DS + Balloon Repayment**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9602&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12932&rand=0.035643258602468086)