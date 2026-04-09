# Sculpting and Grace Period

**Source:** https://edbodmer.com/sculpting-and-grace-period

---

This page discusses how to adjust the sculpting principles in the case of a grace period. I introduce two methods to accomplish this using the fundamental formulas: Target Debt Service = CFADS/DSCR; PV of Debt Service = Debt at COD; LLCR = PV CFADS/Debt. These formulas can be adjusted by starting the discount period at the grace period rather than the COD or the formulas can be adjusted with the notion of the Debt IRR that I use for multiple debt issues. When using the Debt IRR, you should compute the debt service without anything in the grace period (even though there is interest) and you should use then use the Debt IRR with the whole time series of Debt Service and CFADS with zeros in periods for the grace period. These two approaches are illustrated below.

Adjusting the Discounting Period
--------------------------------

The screenshot below illustrates computing PV from the grace period and computing the debt size from the DSCR and cash flow. In this case the FALSE means that the discount begins after the grace period and does not include the grace period. You could also compute an index using the period after the grace period.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-4.png)

If the debt is computed from the LLCR, then the adjustment should be made in the PV of CFADS as shown below.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-5-1024x275.png)

.

.

Adjusting the Debt IRR
----------------------

You can arrive at the same results if you use an adjusted debt IRR. To compute the Debt IRR, do not put any debt cash flow in the grace period (even though there is interest). Then use the debt IRR with the cash flow were there is no debt service computed for the first grace period (again, where the is interest in fact). Note in the screenshot below, the first debt service is zero and the debt IRR is 6.20%. Using the 6.20%, the PV of the debt service is computed correctly.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-6.png)

.

In the second screenshot, the debt is given and the CFADS is computed with the debt IRR. Note that the PV of the debt service is computed with zero in the first period when the debt IRR is used.

![](https://edbodmer.com/wp-content/uploads/2022/04/image-7.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=15293&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11596&rand=0.2876582133699658)