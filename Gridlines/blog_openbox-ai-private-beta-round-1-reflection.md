# Openbox AI Private Beta Round 1 Reflection - Gridlines

**Source:** https://www.gridlines.com/blog/openbox-ai-private-beta-round-1-reflection

---

[Skip to content](https://www.gridlines.com/blog/openbox-ai-private-beta-round-1-reflection#content)

Openbox AI Private Beta Round 1 Reflection
==========================================

*   September 29, 2023

Starting a beta – particularly a beta for a rapidly developing technology such as AI is always going to show you things you didn’t expect. Oh, so people don’t actually care about that feature we worked hard on? And people want to do _what?!_ And actually most of their time is spent… you get the idea.

And of course with an early beta there are always bugs. One big one was that for some types of model not all the required files were in the installation package. That’s now been fixed.

The main learning however, is that customisation is essential. The usual approach to building a model with Openbox has three stages:

1\.   Decide the type of model (e.g. project finance)

2\.   Add standard components

3\.   Customise, because every project and business is unique

The current Openbox AI helps with the first two of these. But until now, you were on your own for customisation. That’s why we are introducing the first version of our Openbox AI formula expert. It helps you write Openbox formulas to do common tasks, letting you customise the model the AI produces to fit your needs more closely.

“_Isn’t that the same as Copilot?”,_ I can hear someone asking. It is certainly similar, in that Copilot is designed to help you with common tasks in Excel. But [Copilot is designed to help you analyse data.](https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a)
 Financial models certainly use data, and particularly if you’re including lots of historic or actuals in a model, that analysis can be useful. But what you really want is to _forecast,_ and often that forecast needs your understanding of how the future will work, which is different to the past. To take an extreme example, for a greenfield project, there’s no historic data to analyse.

The Openbox formula expert can help here. What it does is draw on its “general knowledge” (in reality, what the underlying LLM learnt from the Web) to come up with a plausible formula. Here’s what the AI said when asked to calculate Loan Life Cover Ratio (LLCR):

_Certainly, the Loan Life Cover Ratio (LLCR) is a financial metric used to evaluate the ability of a project to repay its outstanding debt over the loan’s remaining life. The LLCR is calculated by dividing the present value of cash flows available for debt service by the remaining debt balance. Here’s how you can calculate LLCR in Openbox step by step:_

 _### Step 1: Create New Calculation Blocks_

_1\. \[Net Cash Flow for Debt Service\]: This represents the cash flows available for debt service (often EBITDA – taxes + depreciation – capital expenditures – change in working capital)._

_2\. \[Discount Rate\]: The discount rate used to calculate the present value of the cash flows._

_3\. \[Remaining Loan Balance\]: The outstanding loan balance at a particular period._

_4\. \[Present Value of Cash Flows\]: This is the present value of \[Net Cash Flow for Debt Service\] over the remaining loan period._

_5\. \[Loan Life Cover Ratio\]: This is the LLCR, which we’ll calculate._ 

_\### Step 2: Set Values and Formulas_

_1\. Set values for \[Net Cash Flow for Debt Service\], \[Discount Rate\], and \[Remaining Loan Balance\] based on your financial model’s assumptions and calculations._

  _2. Calculate \[Present Value of Cash Flows\] using the formula:_

     _NPV(\[Discount Rate\], FUTUREVALUES(\[Net Cash Flow for Debt Service\], 1))_

     _This formula calculates the present value of future net cash flows available for debt service, starting from the current period and extending for the life of the loan._

 _3. Calculate \[Loan Life Cover Ratio\] using the formula:_

    _\[Loan Life Cover Ratio\] = \[Present Value of Cash Flows\] / \[Remaining Loan Balance\]_

    _This formula divides the present value of future cash flows by the remaining loan balance to get the LLCR._

 By following these steps, you will have calculated the LLCR, which will provide insights into the project’s ability to cover its remaining debt obligations.

Not bad, and it even correctly uses the FUTUREVALUES function.

So how do you get access to this? Well in a spirit of openness we’re making it available to everyone for free, as a prompt for ChatGPT. Just insert the prompt then ask away. If you’d like to get this please just [email us](mailto:hello@openboxmodels.com)
. We’ll be making updated versions of the prompt available over time.

_(Small print: this is an AI not a professional financial modeller so treat its responses as suggestions rather than following them blindly)._

With the Openbox AI, and this prompt, you can now create, modify and customise your Openbox models quickly and easily. Happy modelling!

Share:

*   [](https://uk.linkedin.com/company/gridlines-com)
    

More Posts

[![Man and woman in a professional meeting space, working on a laptop together](https://www.gridlines.com/wp-content/uploads/2024/05/ExcelError-1-300x199.jpg)](https://www.gridlines.com/blog/are-you-relying-on-excel-based-analysis-to-make-business-critical-decisions/)

[Are you relying on Excel based analysis to make business critical decisions?](https://www.gridlines.com/blog/are-you-relying-on-excel-based-analysis-to-make-business-critical-decisions/)

In many businesses, Excel is used for critical reporting and decision making. As has been widely trailed, the flexibility and

[![man working on financial forecasts on his tablet, charts coming out of the tablet](https://www.gridlines.com/wp-content/uploads/financial-forecasting-300x169.jpg)](https://www.gridlines.com/blog/building-a-robust-and-flexible-financial-model/)

[Building a robust and flexible financial model](https://www.gridlines.com/blog/building-a-robust-and-flexible-financial-model/)

Building a robust and flexible financial model is a critical task for businesses. Whether you’re trying to secure funding for

[![Solar panels](https://www.gridlines.com/wp-content/uploads/Solar-300x225.jpg)](https://www.gridlines.com/blog/insights-from-solar-storage-live-2024/)

[Insights from Solar and Storage Live 2024.](https://www.gridlines.com/blog/insights-from-solar-storage-live-2024/)

By Gaurav Singh, Head of Infrastructure Finance. I recently attended the Solar and Storage Live 2024 exhibition at the Birmingham

[![Numbers](https://www.gridlines.com/wp-content/uploads/numbers-300x169.jpg)](https://www.gridlines.com/blog/financial-modellers-are-changing-the-world/)

[Financial Modellers are Changing the World](https://www.gridlines.com/blog/financial-modellers-are-changing-the-world/)

Whilst staring at a financial model, it is really easy to get lost in the numbers. It’s all rows and

[PreviousHow Google taught Bard to doubt itself](https://www.gridlines.com/blog/how-google-taught-bard-to-doubt-itself/)

[NextUnlocking new possibilities – quantum computing and financial modelling](https://www.gridlines.com/blog/unlocking-new-possibilities-quantum-computing-and-financial-modelling/)

Tell us about your project
--------------------------

[![Akram Mostafa](<Base64-Image-Removed>)](mailto:akram.mostafa@gridlines.com)

Akram Mostafa
-------------

Associate Director

akram.mostafa@gridlines.com

[![](<Base64-Image-Removed>)](mailto:morag.loader@gridlines.com)

Morag Loader
------------

Director of Accounting & Tax

morag.loader@gridlines.com