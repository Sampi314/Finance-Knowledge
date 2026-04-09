# Re-Financing Analysis

**Source:** https://edbodmer.com/re-financing-analysis

---

This webpage addresses issues of re-financing in project finance from a theoretical and mechanical perspective. I show you how to incorporate multiple debt re-financing in a model where you size the re-financing, re-pay existing debt, incorporate multiple re-financings, include fees on re-financed debt and prepare sensitivity analysis. Re-financing can have a dramatic effect on the economics of an investment from the perspective of investors.  Whether re-financing should be assumed is an item that can lead to vigorous debates among project finance analysts.  I am on the philosophical side of the issue that suggests re-financing is an essential element of analysis in project finance.  This is particularly the case when the term of the initial project finance loan is less than the life of the project.  I think you can go to the extreme of saying that whenever the term of the loan is less than the economic life, the measurement of equity IRR is distorted. I have made some power point slides that describe various issues associated with re-financing that you can download by pressing the button below.  As usual, the mechanics of re-financing are easy without addressing circular references, but the modelling becomes difficult with circular references that arise because of the tax effects of interest and fees on the re-financed debt.

.

**[Power Point Slides the Describe Theory and Modelling Issues Associated with Debt Re-financing in PF](https://edbodmer.com/wp-content/uploads/2018/04/Re-financing-1.pptx)
**

.

.

Illustration of Re-financing without Circular References (Mainly from Taxes and Interest Deduction)
---------------------------------------------------------------------------------------------------

I have created a file that evaluates re-financing in the context of project financing. This file does not include taxes or DSRA accounts and therefore does not include circular references.  But it is a good way to demonstrate the effects of re-financing on the equity IRR.  Your can download the file that is explained on this page by pressing the button below.

.

[Project Finance Model with Flexible Re-financing Amounts and Timing Including Effects of Cash Flow Sweep](https://edbodmer.com/wp-content/uploads/2019/06/Refinancing-Analysis-without-Tax-1.xlsm)

.

Refinancing Mechanics and Flags
-------------------------------

I start with some of the inputs that you should consider when adding re-financing to your model.  You need to put in dates of assumed financing and you want to be flexible in terms of the dates.  You also want to put in the size of the re-financing that will probably come from an assumed DSCR.  Then you will need a sizing section somewhere as described in the next paragraph.  After the sizing, you need some kind of assumption about the tenure of the debt. I suggest that you use a tail and you back into the tenure from the assumed tail.  In that way, you can assure that your tenure will not extend past the date of the end of the project life.  When you enter the dates, you can put the date of the re-financing after the project life and then you can take the re-financing out of the analysis.  The reset buttons change the date of re-financing to after the project life. Note that the size of the debt is separate from the debt schedule that may have more details like the fees.

![](https://edbodmer.com/wp-content/uploads/2019/05/Refinance-Assumptions-simple-1.jpg)

When you incorporate re-financing, the first step is often sizing the re-financing from an assumed DSCR. Of course you do not know the DSCR beforehand and you may have to make sensitivity analysis. So what — you are afraid of sensitivity.  So, the first mechanical step is to size the debt with some flags (switches or masks) and then to compute the PV of the debt service over the remaining tenor. Note in the screenshot below that there is a line for re-financing and the total balance of the debt is paid at re-financing.

![](https://edbodmer.com/wp-content/uploads/2018/05/refinancing-5.jpg)

.

The screenshot below illustrates the mechanics of the new re-financing in the time period when the debt has been repaid. This example includes two re-financings with an illustration of the sizing of the debt using flags. I almost always use two switches, one for the period of the re-financing and a second for the repayment period of the re-financing.

.

![](https://edbodmer.com/wp-content/uploads/2019/05/Debt-Balances-Re-structuring.jpg)

.

Illustration of the Effects of Refinancing Using Spinner Boxes
--------------------------------------------------------------

The first graph below illustrates a case with a short-term tenure and no re-financing.  I say short-term tenure because the debt tenure is much shorter than the life of the project.  You can find this graph in the file above and you can press the re-set button so that no re-financing is assumed.  In this case the equity IRR is 14.36% (very high).

![](https://edbodmer.com/wp-content/uploads/2018/05/Re-financing-1.jpg)

Advantage of long tenure — note the increase in the equity IRR. (Start with project IRR versus debt cost).

![](https://edbodmer.com/wp-content/uploads/2018/05/Refinancing-2.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/05/Refinancing-3.jpg)

.

.

![](https://edbodmer.com/wp-content/uploads/2018/05/refinancing-6.jpg)

.

Re-setting Re-financing
-----------------------

Other subjects with re-financing include re-setting the re-financing assumptions so you can try another scenario.  You can include a reset button along with the spinner boxes to illustrate what is going on.  This can apply to the basic case above or a fancier analysis with re-financing.  The process of using spinner boxes and a re-set button is illustrated in the screenshot below.  The re-set button is so simple it is hardly worth mentioning.  All you do is to define range names and make a macro that puts the re-set values into the VBA code as illustrated below. You just have to set the refinance period to after the life or the project and then the re-financing will be irrelevant.

![](https://edbodmer.com/wp-content/uploads/2019/05/reset-refi.jpg)

.

Sub Button16\_Click()

Range("refi1") = 50
Range("refi2") = 50
Range("refi3") = 50


End Sub


.

You can even go further and suggest that the re-financing analysis should include terminal value.

Re-financing and Circular References
------------------------------------

Here I will show how the process works with the parallel model where the taxes change because of the interest on re-financing.  If the taxes change, then the CFADS changes and the amount of the re-financing changes. Here are some of the things you can do to incorporate the circular reference into your model and avoid the pain of circular references with copy and paste macros.  You can put the inputs and parameters into your model much like in the above case.

When you add a new debt issue, don’t forget to adjust the input size and include the last debt issue.

Files with re-financing analysis that you can find if you request resources and edwardbodmer@gmail.com

*   Multiple Re-Financing Exercise.xlsx
*   Cash Sweep and Re-financing.xlsm
*   Multiple Re-financings with Sweep.xlsm

Re-financing model.

![](https://edbodmer.com/wp-content/uploads/2019/07/Refinancing-Inputs.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Refinance-Assumptions.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1659&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13004&rand=0.9228935875371795)