# Construction Analysis and EPC

**Source:** https://edbodmer.com/construction-analysis-and-epc

---

This page addresses some details of projecting construction costs in project finance models. I discuss the modelling of S-Curves; analysis of Liquidated Damages and Construction Delay; Retainage of the final progress payment and analysis of risk from the perspective of the EPC contractor. As I forget how to use the Weibull to demonstrate skewed, I put the Weibull distribution in this section. The file that evaluated the EPC profits with different risk and retainage, liquidated damages is attached to the button below.

**[Excel File with EPC Economic Analysis Including Risk Distributions, Delay, Liquidated Damages and Other](https://edbodmer.com/wp-content/uploads/2020/10/class-working-file-exercise2.xlsm)
**

You can model S-curves with the normal distribution of the Weibull distribution. The screenshot below shows how to model the S-curves with the Weibull distribution. Note that the alpha and the beta can be changed to affect both the shape of the distribution and also the skewness of the curve. Note that I have inserted sparklines for the different curves which are easy to incorporate.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-14-2048x874.png)

From the EPC perspective, you should account for the possibility of different costs and distribution of costs. You can argue that the EPC profit should have set-aside capital like a loan for a bank. You can also recognize that relative to a base case, there is more chance of an increase than a decrease.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-18-2048x934.png)

You can include retainage and a delay relative to the S-Curve. In this case the S-Curve is reduced by the retainage percent. The retainage percent is then put into the final period of payment.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-16-2048x393.png)

The profit earned by the EPC contractor is demonstrated on the screenshot below. Note how the nominal profit is computed as well as the present value of the profit. In addition, the expected value of the profit is presented as well as the profit as a percent of the cost. Note that this analysis is before liquidated damage.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-19.png)

### Liquidated Damages

Inputs that you can include for liquidated damages are shown in the table below. Note that you can include a target construction date and a cost per day of delay if the target date is not met. Switches are included for how the liquated damages will apply and the maximum liquidated damage.

![](https://edbodmer.com/wp-content/uploads/2020/10/image-20.png)

![](https://edbodmer.com/wp-content/uploads/2020/10/image-23-2048x872.png)

### Alternative Currencies and Borrowing

The screenshot below illustrates the effect of borrowing in different currencies. When you apply the following formula:

Interest Rate = (1+Real Rate) \* (1 + Inflation Rate) \* (1 + Credit Spread) -1

then everything works

![](https://edbodmer.com/wp-content/uploads/2020/10/image-22-2048x1199.png)

### Financing and Lease Payment

![](https://edbodmer.com/wp-content/uploads/2020/10/image-24-2048x1136.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=11969&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10296&rand=0.04860275445682172)