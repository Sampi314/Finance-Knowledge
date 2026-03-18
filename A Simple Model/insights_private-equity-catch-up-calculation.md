# Private Equity Catch Up Calculation | A Simple Model

**Source:** https://www.asimplemodel.com/insights/private-equity-catch-up-calculation

---

Private Equity Catch Up Calculation
===================================

*   [](https://www.asimplemodel.com/contributors/peter-lynch)
    [Peter Lynch](https://www.asimplemodel.com/contributors/peter-lynch)
    
*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

The calculation behind the catch-up provision that determines the general partner’s (GP) carried interest at a private equity fund can cause some confusion. In this post we will explain the math in the Excel template available on ASM.

For reference, the calculation refers to the second example cited in this Excel template: [Distribution Waterfall with 5 Examples](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation#mailSentPopup)
 (related [post](https://www.asimplemodel.com/insights/distribution-waterfall/)
). The language for the second example cited in the Excel file is as follows:

> **First,** 100% of all cash inflows to the LP until the cumulative distributions equal the original capital invested plus some preferred return.
> 
> **Second,** a “20% catch up” to the GP equivalent to 20% of the of the distributions realized in step 1 plus the distributions realized in this step.
> 
> **Third,** thereafter, cash flows in excess of distributions made in step 1 and step 2 (if any) are distributed 80% to the LP and 20% to the GP.

[![Private Equity Catch Up](https://www.asimplemodel.com/wp-content/uploads/2021/10/Distribution-Waterfall-Explanation_04_Summary-Text_202009-980x565.png)](https://www.asimplemodel.com/wp-content/uploads/2021/10/Distribution-Waterfall-Explanation_04_Summary-Text_202009.png)

Based on the emails I receive, most of the confusion comes from the calculation used in the second step. So let’s reframe the objective: In step 2 you want the GP to receive 20% of all distributions up to and including step 2. For this exercise, think about (All Distributions up to and including Step Two) as all cash flows received by both the GP and LP up to and including Step Two.

If the GP is supposed to get 20% of (All Distributions up to and including Step Two), it follows that the LP has received 80% of (All Distributions up to Step Two):

> (All Distributions up to and including Step Two) \* 0.8 = (LP First Distribution)
> 
> (All Distributions up to and including Step Two) = (LP First Distribution) /0.8
> 
> And since the GP only receives what is not allocated to the LP (what the GP receives = the catch up):
> 
> (Catch Up) = (LP First Distribution) /0.8 – (LP First Distribution)
> 
> If subtracting the “(LP First Distribution)” is confusing, think about it this way (different formula, same result):
> 
> (Catch Up) = ((LP First Distribution) /0.8)\*0.2

**To help this sink in I thought I would provide an additional way to think through this exercise:** The Catch Up is equal to 20% of all cash flows received in both steps 1 and 2. It follows that:

C = Catch Up

P = LP return in First Distribution

> C = 0.2\*P + 0.2\*C
> 
> 0.8\*C = 0.2\*P
> 
> C = P\*0.2/0.8
> 
> C = P \* 0.25

For the exercise I thought the first approach would make it easier to follow the formulas (I find the 0.25 in the second formula has the potential to be confusing), but generally multiple examples help.

**Learn more about private equity transactions with ASM’s [Private Equity Training](https://www.asimplemodel.com/financial-curriculum/private-equity)
 course.** The Private Equity Training course was developed by industry professionals. The content goes beyond the [LBO](https://www.asimplemodel.com/financial-curriculum/lbo-case-study)
 model to explain how private equity professionals source, structure and close transactions.

*   [X](https://www.asimplemodel.com/#x)
     [Facebook](https://www.asimplemodel.com/#facebook)
    

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

Download links are sent directly to your inbox! Input your email address below and we will send you an email with the information requested.

 I agree to ASM's [Terms of Use](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation#)
 and [Privacy Policy](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation#)
.  

     

You will only need to provide your email address the first time. All future downloads will be sent to the same email address.

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

X ![](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation) [Click Here to Visit URL](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation)

![Free Financial Modeling ](https://www.asimplemodel.com/wp-content/uploads/ASM-Logo-svg.svg)

X

A link to this file will be sent to the following email address:

If you would like to send this to a different email address, Please click here then click on the link again.

Copy link

✓

Thanks for sharing!

Find any service

[AddToAny](https://www.addtoany.com/ "Share Buttons")

[More…](https://www.asimplemodel.com/insights/private-equity-catch-up-calculation#addtoany "Show all")