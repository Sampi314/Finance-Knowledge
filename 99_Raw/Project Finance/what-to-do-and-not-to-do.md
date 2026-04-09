# What to Do and Not to Do

**Source:** https://edbodmer.com/what-to-do-and-not-to-do

---

If you are worried about an interview things not to do include selecting one of the cases and trying it or just concentrating on things like sculpting that you think is a little compex. Instead, I suggest that you work through some simple cases that demonstrate model structuring, model formatting, working quickly with equations, creating model flags, finding key outputs and computing financial statements. If you do this many times then you will be able to work through these things really quickly and the come to the complex things. I have included some examples below with simple cases that you should practice a few times until you can go really fast. Once you have become really comfortable and fast at the fundamental model you can move to a few things that make the models more complex. These things include montly and maybe aggregation to semi-annual or quarterly timing; circular references related to interest during construction and/or taxes and different methods of debt sizing with sculpting. For these issues, you can focus your practice exercises and construct the models quickly.

In this page I begin by discussing what not to do with some examples that I have come accross. There is no particular order for this discussion and I illustrate some of the issues. I am being a hypocrite in what I am about to say, because my comments are arrogant. But my only skill is doing things the wrong way so many times and finally realising what an idiot I have been over many years. The arrogance in my opinion come from thinking that you are a good modeller because you made one case in a university class, trying to show off with excel formulas, not taking the time to study other models, running to the complex stuff without nicely laying out the structure of the model, not having an open mind about different modelling styles and techniques and not reading the directions of the test.

I have made my generic macros so that it can be your partner for modelling. If you are allowed to use your own computer, you should be able to use this model. I strongly suggest that you download the model and enable the macros (you may have to go to the explorer and allow turn off the stupid pink ribbon that comes up these days). It should only take minutes to be able to do this quickly. You can press the first button to download the file. Simple instructions as to what to do with the pink ribbon are shown by pressing the second button.

.

**[Generic Macro File for Copying to Right (SHIFT, CNTL, R), Formatting (CNTL, ALT, C) and Other Functions (UDFs)](https://edbodmer.com/wp-content/uploads/2026/03/Generic-Macros.xlsm)
**

.

**[Instructions for Downloading Files with Macros](https://edbodmer.com/downloading-files-with-macros/)
**

.

Example 1: Not Laying out the Model, Not Formatting the Model, Not Including Sums, Not Following Directions and Understanding Project IRR
-----------------------------------------------------------------------------------------------------------------------------------------

The first example is a comprehensive example that includes monthly cash flow and some questions about shareholder loans, deferred taxes and other items. One of the most painful aspects of this case is the use of quarterly payments in a monthly model. The instructions are shown below.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-1.png)

The case came with a poorly structured input page. (I don’t know if they expected you to fix the page that did not start with dates and timing). If you know a little accounting you can see a mistake in the questions. The word deferred implies that taxes are deferred and will reverse. The 90% of asset value is a disgusting question that would not result in deferred tax — it is a permanent difference. The shareholder loan benefit depends on the tax treatment and the treatment of IDC on the shareholder loan. This will take a little while to complete and you can maybe at least show that you know the issues without wasting time that nobody will be able to get to. Finally, maybe somebody can tell me about the difference between unlevered IRR and project IRR. In my opinion there is project pre-tax IRR which is unlevered pre-tax IRR, there is project after-tax IRR which is the same as unlevered after-tax IRR and there is equity IRR that is levered IRR. It seems that a lot of tests are written badly like the one above, but don’t freak out about this. The exam included input data so you do have to waste time typing it in. But the layout of the inputs was not good and you can make yourself look good by fixing the input structure.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-2.png)

.

The financing can cause some of the problems. Note that the payments are quarterly and you will need a quarterly flag. This will be painful, but you can do things without the quarterly summation (you can use the sumif). If you are working through this case yourself, then I suggest first re-structuring the input sheet and allowing for the scenarios. I have included instructions for this case in the file attached to the button below.

.

**[Excel File with Instructions for Exam that is a Comprehensive Example with Monthly Flows, Circular References and Other Things](https://edbodmer.com/wp-content/uploads/2024/04/Test-hard.xlsx)
**

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-3.png)

.

The attempt at this case with some of the problems is shown below. Some of the problems include wasting a lot of time on a complex formula for quarterly, no formatting, no sum column, no capital expenditure for computing the project IRR, not following directions with the after-tax IRR and the scenario analysis. All of these things are pretty easy before you get to the financing. You can even compute the enterprise value at this stage. A good thing is that the drivers are shown.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-4.png)

.

.

Other problems are not showing a clear index for degradation and inflation and most importantly not showing the capital expenditures without IDC at the beginning so you can see the free cash flow and compute the project IRR (or the unlevered pre-tax and after-tax IRR) per the instructions. All investments have capital expenditures, operating expenditures and revenues — these should be at the beginning of the sheet and then you can compute EBITDA and pre-tax free cash flow. With pre-tax free cash flow you can compute the unlevered pre-tax IRR or the pre-tax project IRR or whatever you want to call it. Then you can compute the depreciation on operations (without IDC and fees) that you will need later. With depreciation you can compute EBIT and operating taxes to get the project IRR or the unlevered after-tax IRR.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-5.png)

I have included a revised attempt at the test (it is tough to complete in three hours and I bet the creator of the test did not try it). I began by re-formatting the input sheet with the scenarios. Then you can use the generic macros to make a nice format. My revised attempt is attached to the button below. The revised input that shows you can makeeffective scenario analysis is illustrated first. Using the INDEX function and should demonstrate you can make nice sensistivity presentations.

.

**[Excel File with Completed Case for Comprehensive Example with Monthly Flows, Circular References and Other Things](https://edbodmer.com/wp-content/uploads/2024/04/Test-Hard-Revised-1.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-6.png)

.

You can look at how I tried the model and made modifications. Note that I did not bother with the deferred tax or the shareholder loan. I think this would be very difficult to complete in three hours although you can try to complete it. Note that I have put two columns for units — one for the driver units and a second for the model units. I am interested in seeing if you have better ideas about this — maybe you could put the model units on the left.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-7.png)

.

As the assignement at least allowed three hours, you may have time to show how you can make circular references associated with IDC and in this case also for taxes. In the video I explain how to use the SUMIF function to efficiently aggregate monthly interest, CFADS and other data into a monthly model.

.

Attempting to Complete Exam without Understanding Principles and By Using Guidlines that Do Not Make Sense
----------------------------------------------------------------------------------------------------------

.

I understand why the idea of having a highly structured model using SMART or FAST modelling standards can be advantageous. But if you have taking some kind of course or reviewed models using these standards, not only will the exam process be very difficult, but This case had a reasonable set of instructions except for the taxes and sculpting that are combined. I suspect that the writers of the case may not have realised the problem created by this. The assignement is summarised below.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-8.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-9.png)

.

The excel file attached to the button below shows how I have completed this exam as well as an example of what not to do. This is a resaonable annual exam except for the tax assumption that creates a circular reference with sculpting. Instead of wasting time on meaningless rules.

.

**[Excel file with Example of Simpler Formatting and Structuring of Toll Road Exam with Debt Sizing and Circular Macro](https://edbodmer.com/wp-content/uploads/2024/04/Toll-Road-Completed.xlsm)
**

.

**[Excel file with Example of What Not to Do -- Following Rules that Are Not Important and Excessive Formatting and Time Lines](https://edbodmer.com/wp-content/uploads/2024/04/Example-of-What-Not-to-Do-Excessive-Rules-and-Formatting-1.xlsx)
**

.

Wasting Time on Formatting Rules, Excessive Sheets, Data Transfer Rules, and Too Many Account Balances
------------------------------------------------------------------------------------------------------

If you have looked at websites of companies that make fancy models you may be impressed by what seems to be fancy structured formats with their rules. For an exam, I suggest that you may be lead down the wrong path by thinking you are a good modeller by following the rules. The attempt shown below is an example of this and it made me sad. The person may have spent money on some kind of course and put the things in a separate sheet including a whole lot of flags. This is often done in models these days but I can tell you that users really hate it. Note that there are no timelines at the top of the page. The share balance on the balance sheet should take a couple of lines at the bottom of the page and there is no need to go from page to page for a simple account.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-10.png)

.

The next screenshot illustrates how crazy things can get if you follow one of the techniques like the FAST modelling standard. This was a simple annual case, but somehow there were two different pages with timelines and the page below has more than 100 lines in a page that only had timelines for the construction period. You only need a construction switch and operation switch and later a switch for the debt tenure. Please do not get lost by following a template.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-11.png)

.

This example also shows something that you should not do in answering an exam. It involves showing off and doing something that is not asked for. In this case a DSRA account was added even though it was not requested in the exam. Note at the bottom that instead of putting the driver in a left column of the model that the transferred input is put in a separate line. This magnifies the size of the model, increases the time to construct a model and makes the model more difficult to read. If you are worried about the units on the transferred varaiables versus the model units, you can make two columns for units as shown in the screenshot after the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-12.png)

.

Instead of Silly Rules, Follow a Natural Progression of the Model, Use Efficient Formatting, Include Debt Sizing Before Sources and Uses and Do the Circular Reference at the End
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.

Instead of getting lost in the rules, I suggest a clear layout of the revenues, expenses and capital expenditures. Then (maybe after taxes and working capital) you can compute the debt sizing which in this case was the trickiest part of the model. The manner in which I suggest working through these issues is shown with the equations and screenshot below.

For debt sizing, remember:

Debt service = CFADS/DSCR \* repayment flag

PV of debt service from repayment period (not including construction) is the debt size from DSCR

If the debt from debt to capital (project cost including IDC x debt to capital) is less, then use the lower amount

When you compute repayment, first compute the debt service — CFADS/DSCR and then subtract interest (always on opening balance) then use the MIN function with the opening balance to make sure the repayment is not too much.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-13.png)

.

As with other exams, I have re-strutured the input page so that it is strutured with dates first, then quantities and then revenue, expense and capital expenditure outputs. After that you should show the taxes and the financing inputs.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-14.png)

.

Stop Being an Excel Show-off and See if You Can Complete the Financial Statements in Minutes from Information that You Have Already Computed
--------------------------------------------------------------------------------------------------------------------------------------------

Problems with multiple sheets. Don’t use the Shell method that I have advocated before. Be careful with plus and minus signs and put negative numbers in the cash flow statement for outflows.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=17276&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9104&rand=0.40665917990205036)