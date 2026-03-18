# Levelised Cost and Construction Period

**Source:** https://edbodmer.com/carrying-charge-2-inflation-in-carrying-charges-in-renewable-energy-prices

---

The levelised cost formulas developed in the other sheets have made the unrealistic assumption that the construction is made in exactly one year. To include the financing costs during the construction period (debt as well as equity costs) that change as the construction period changes, you can increase (or decrease) the capital cost with and adjustment. You can move values around with present value and future value with (1+discount rate)^ Thisconstruction period. The adjustment can be done with the FV formula if you assume a flat S-curve. The manner in which you can make adjustments for the construction period are demonstrated using simple examples below. I also explain how you can incorporate a specific S-curve in the analysis.

1\. You have to decide on the time period when you want to measure LCOE. Who cares really, but if you have a long construction period like a nuclear plant, you could use the start of construction or start of operation for example when computing the LCOE. If you are computing LCOE from npv of revenues and npv of generation, you can make the NPV index of 1.0 at financial close or COD. I assume that you use the COD. In theory this means that the comparison projects should be inflated (I know that solar costs have been coming down and you could argue a lot).

2\. The IDC is not good enough alone to evaluate the costs of a construction period.  The forgone equity return must be also included. The project IRR should do this. (Note if you are earning a really low project return the LCOE will be lower, but the LCOE should reflect the target project IRR — I cannot get myself to say WACC).

3\. You must account for the construction period in LCOE. If the construction period is longer, then the cost is higher because of higher financing costs.  If you are computing real LCOE, you do not have to worry about inflation issue above, but you do need to include the real cost of capital.

.

Basics of Including Construction Timing in Levelised Cost
---------------------------------------------------------

The calculation is illustrated in the screenshot below. As with other exercises, the formula is proved with a little financial model. The key formula to make this work is the FV formula shown in row 16 and in row 21. This increases the cost — it should be the real cost and not the nominal cost from real discount rates — but it considers the higher cost that is a result of financing construction. The first example below uses a one period example.

.

![](https://edbodmer.com/wp-content/uploads/2021/08/image-3.png)

.

The example below has a four period construction period and with a high discount rate of 10%, the cost increases by 16% which has an implicit flat S-curve.

![](https://edbodmer.com/wp-content/uploads/2021/08/image-4.png)

.

Capacity Charge and O&M Adjustments for Construction Period
-----------------------------------------------------------

This example is for a transmission where the levelised cost is computed at the start of the construction period. I have included various formulas that can be used to make the various adjustments with the FORMULATEXT function. The transmission case also includes proof of alternative ways to compute the levelized cost.

In the example below the S-curve is computed with an NPV formula and then the PV of the project is grossed up to one period. The first example uses and nominal LCOE case.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-4.png)

.

The second example below uses a real LCOE example. The formulas are the same but the real discount rate is used.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-5.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-6.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-7.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-8.png)

,

,

![](https://edbodmer.com/wp-content/uploads/2023/11/image-9.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1520&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9256&rand=0.6390045877904796)