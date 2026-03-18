# Mid-Year Convention DCF and Mid-Year Discounting

**Source:** https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf

---

The Mid-Year Convention and Mid-Year Discounting in a DCF with Stub Periods
===========================================================================

In this tutorial, you’ll learn about the mid-year convention in DCF models, as well as stub periods, and how to combine these concepts in the FCF projections and Terminal Value calculations.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/#tab-signup)
    

The Mid-Year Convention and Mid-Year Discounting in a DCF with Stub Periods

> Mid-Year Convention Definition
> ------------------------------
> 
> When you use the mid-year convention in a discounted cash flow (DCF) analysis, you assume that the company’s cash flows arrive halfway through each year rather than at the end, more accurately reflecting reality and boosting the company’s implied value in the DCF.

The mid-year convention is an additional feature of [DCF models](https://www.mergersandinquisitions.com/dcf-model/)
 often used by [investment banks](https://www.mergersandinquisitions.com/investment-banking/)
 and [equity research teams](https://www.mergersandinquisitions.com/equity-research/)
.

[Click here to get a sample Excel file with a simple DCF model that illustrates the mid-year convention](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Mastery/08-17-Mid-Year-Stub-Discount-Simple-DCF.xlsx)
.

![PowerPoint Pro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Financial Modeling for Investment Banking With **BIWS Core Financial Modeling**

*   #### Become a financial modeling pro
    
    158 videos, detailed written guides, Excel files, quizzes, and more
    
*   #### Complete 10+ detailed global case studies
    
    These include both the theory and the practical applications
    
*   #### Prepare for your internship or full-time job
    
    Gain the skills you need to “hit the ground running” on Day 1
    

[Full Details](https://breakingintowallstreet.com/core-financial-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Core-Financial-Modeling-Course-Outline.pdf)

You can see how it differs from the “standard convention” below:

![Mid-Year Convention vs. Standard Convention in a DCF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201333%20263'%3E%3C/svg%3E "Mid-Year Convention vs. Standard Convention in a DCF")

In a standard DCF model, you project a company’s [Unlevered Free Cash Flow](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/)
 over 5-10 years, estimate its [Terminal Value](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
 at the end of that period, and discount everything to Present Value.

You then compare that Present Value figure to the company’s current Enterprise Value (or back into the implied share price and compare that to the current share price) to determine if the company is valued appropriately.

When you discount the company’s future cash flows to their Present Value, you use periods such as 1, 2, 3, and 4 in a standard DCF analysis:

![Standard Discount Periods in a DCF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20964%20319'%3E%3C/svg%3E "Standard Discount Periods in a DCF")

In other words, to calculate the Present Value (PV) of a Free Cash Flow generated in Year 3, you use this formula:

PV of Year 3 FCF = Free Cash Flow in Year 3 / ( (1 + Discount Rate) ^ 3)

You can see this formula in Excel in the image below:

![Standard Discount Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20954%20233'%3E%3C/svg%3E "Standard Discount Formula")

But that’s **not** accurate because a period of “3.000” implies that all the company’s FCF in Year 3 is generated _at the end of Year 3_.

In reality, though, the company generates cash flow **every day**, and _on average_, that cash flow is distributed throughout the year (with exceptions for highly seasonal companies).

So, it is more accurate to use discount periods such as 0.5, 1.5, 2.5, and 3.5 when you calculate the Present Value of Free Cash Flows:

![Mid-Year Convention Impact on Free Cash Flow Discounting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20954%20288'%3E%3C/svg%3E "Mid-Year Convention Impact on Free Cash Flow Discounting")

Using these discount periods in a DCF is known as the “Mid-Year Convention” because you’re assuming that the cash flows arrive midway through each year.

**The company’s Implied Value increases because the cash flows arrive earlier, and money today is worth more than money tomorrow.**

To implement the mid-year convention, you discount each cash flow manually using the Present Value formula above, with discount periods based on 0.5 rather than whole numbers.

Here is the traditional method vs. the Mid-Year Convention:

![Mid-Year Convention vs. Standard Convention in a DCF](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201333%20263'%3E%3C/svg%3E "Mid-Year Convention vs. Standard Convention in a DCF")

The PV of each Unlevered Free Cash Flow increases because it’s generated earlier.

**How the Terminal Value Changes with the Mid-Year Convention**
---------------------------------------------------------------

If you use the Multiples Method to calculate the Terminal Value in a DCF (e.g., assign a Terminal EBITDA Multiple to the company’s [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/)
 in its final projected year), nothing changes.

That’s because the Terminal Multiple always applies to the company’s financial metrics in the final projected year _at the end of that year_ – regardless of when the cash flows in the projected period are generated.

However, if you calculate the Terminal Value using the Perpetuity Growth method and use the **mid-year convention**, you need to use a discount period half a year earlier to discount the Terminal Value to its [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
.

Under this method, the Terminal Value is based on the company’s _cash flows_, and with the mid-year convention applied, these cash flows are generated halfway through each year.

Therefore, if the DCF projection period is 10 years, the Terminal Value is as of _Year 9.5_ rather than _Year 10.0_ under the mid-year convention and the Perpetuity Growth method.

So, you use 9.5 rather than 10.0 in the Present Value formula, resulting in a higher implied value:

![Mid-Year Convention - Terminal Value Differences](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20814%20407'%3E%3C/svg%3E "Mid-Year Convention - Terminal Value Differences")

You could adjust these calculations to make them comparable, but it’s rarely the time and effort since the discrepancy is small (~2-3%).

**Should You Always Use the Mid-Year Convention?**
--------------------------------------------------

While many banks use the mid-year convention in DCF models, it is **not** always appropriate.

For example, if a retailer earns most of its sales in Q4 of the year due to the holiday shopping season, the bulk of its Free Cash Flow probably _is_ generated at the end of the year.

You may not want to use periods of 1.0, 2.0, etc., as they would imply that 100% of the FCF gets generated on December 31, but you could use periods such as 0.75 or 0.80 to “weight” the FCF generation slightly earlier.

You would not want to use 0.5, 1.5, 2.5, etc., for the discount periods because this company’s sales and FCF are not evenly distributed over the entire year.

**The Mid-Year Convention with Stub Periods**
---------------------------------------------

Another trickier feature also results from timing differences: **stub periods**.

When you value a company, **much of its cash flow for the first projected year has already been generated** (unless you’re valuing it on January 1).

So, you should **reduce** the cash flow for Projected Year 1 by the amount that the company has _already_ generated.

For example, if it’s April 30, the company is expected to generate $300 in FCF for the year, and it has _already_ generated $100, you subtract the $100 and use $200 for the FCF for the first period in a DCF:

![Stub Period - Deduction for Cash Flow](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20182'%3E%3C/svg%3E "Stub Period - Deduction for Cash Flow")

But you _also_ need to change the **discount periods** because April 30 to December 31 represents about 2/3 of the year.

This interval between April 30 and December 31 is called the **stub period**.

To determine the discount period for this **stub period**, you take the remaining days of the year and divide by the total days in the year.

There are 245 days between April 30 and December 31 and 365 total days in the year, assuming it’s not a leap year.

Since 245 / 365 = 0.671, 0.671 will be the **discount period** for this first year.

_Without_ the mid-year convention, the first discount period in a DCF will be 0.671 rather than 1.000, the next period will be 1.671 rather than 2.000, and the next one will be 2.671 rather than 3.000.

You subtract the already-generated cash flow only in the first period.

The projected cash flow in all the subsequent years is the same because no cash flow for Years 2, 3, and beyond has been generated as of April 30 of Year 1.

Here’s what it looks like in Excel:

![Stub Periods - FCF Deductions and Discount Periods](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20988%20390'%3E%3C/svg%3E "Stub Periods - FCF Deductions and Discount Periods")

You can also combine the stub period with the mid-year convention.

If you do this, the first discount period will be the stub period fraction divided by 2.

Continuing with the April 30 example, dividing by 0.671 by 2 produces 0.336.

By doing this, you’re assuming that the cash flow arrives **midway** between **today** – April 30 – and the **end of the year** – December 31.

“Midway between April 30 and December 31”  means an exact date of August 31.

**In each period AFTER that first one, you take the normal discount period and subtract 0.5.**

Here are the normal and mid-year discount periods for a valuation date of April 30:

![Mid-Year Convention and Stub Discount Periods](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201355%20467'%3E%3C/svg%3E "Mid-Year Convention and Stub Discount Periods")

You do **NOT** keep dividing the “Normal Discount Period” by 2 – that’s only in Year 1!

**If you divided the Year 2 “Normal Discount Period” by 2, you’d be assuming that the Year 2 cash flow arrives midway between April 30 of Year 1 and December 31 of Year 2.**

**In other words, you’d be incorrectly assuming that the _Year 2 cash flow_ arrives on March 1 of Year 2.**

But that’s not what happens!

Assuming that the Year 2 cash flow is evenly distributed, it should arrive on June 30 of Year 2 –  midway through _that year_.

By using the correct discount period of 1.171 for Year 2, you’re saying:

**“Today is April 30 of Year 1. We don’t get any Year 2 cash flows in Year 1, so let’s add the whole stub period of 0.671. We do get cash flows in Year 2, but they arrive midway through the year, so let’s add 0.5 to reflect that we get them midway through Year 2. 0.671 + 0.500 = 1.171.”**

If you move forward another year, you add 0.671 for the remainder of Year 1, 1.000 for all of Year 2, and 0.500 for the cash flows that arrive midway through Year 3.

That produces 2.171 for the mid-year discount period for Year 3, as shown above.

**The Mid-Year Convention and Stub Period in the Terminal Value Calculation**
-----------------------------------------------------------------------------

This **stub period** affects the PV of Terminal Value calculation because it _reduces_ the time between today’s date and the end of the projection period.

So, if the stub period is 0.671, as in the example above, and you’re _not_ using the mid-year convention, you use 9.671 rather than 10.000 to discount the Terminal Value under both methods:

![Stub Period Impact on Terminal Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20809%20383'%3E%3C/svg%3E "Stub Period Impact on Terminal Value")

But if you use the stub period and the mid-year convention together, the discount periods are as follows:

*   **Multiples Method:** Still 9.671
*   **Perpetuity Growth Method:**171

Once again, you need to “move back” half a year under the Perpetuity Growth Method since it’s based on the company’s cash flows, which arrive halfway through each year under the mid-year convention.

You can see the impact below:

![Mid-Year Convention and Stub Period Impact on Terminal Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20811%20454'%3E%3C/svg%3E "Mid-Year Convention and Stub Period Impact on Terminal Value")

**The Mid-Year Convention and the Stub Period in a DCF: Final Thoughts**
------------------------------------------------------------------------

If you find these concepts confusing, we recommend **skipping them** and simplifying your models.

The mid-year convention will never change the results of a DCF by more than a few small percentage points.

Stub periods can potentially make a bigger difference, but they are unlikely to do so for most standard companies.

They would matter if something unusual happened in the first portion of the first projected year that is _not_ expected to recur in the second portion, such as a significant acquisition or [divestiture](https://breakingintowallstreet.com/kb/ma-and-merger-models/divestitures/)
.

These features are **bells and whistles** in the DCF: nice to have but not essential in making investment decisions or client recommendations.

Finally, these topics are **unlikely** to come up in interview questions unless you’ve had significant work experience or [financial modeling exposure](https://www.mergersandinquisitions.com/financial-modeling/)
.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Mastery/08-17-Mid-Year-Stub-Discounts.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple DCF Example with the Mid-Year Convention and Stub Periods (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Mastery/08-17-Mid-Year-Stub-Discount-Simple-DCF.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[BIWS Premium](https://breakingintowallstreet.com/biws-premium/)

Get the Excel & VBA, Core Financial Modeling, and PowerPoint Pro courses together and learn everything from Excel shortcuts up through financial modeling, valuation, M&A and LBO deals, and the key PowerPoint shortcuts and commands.

[Learn More](https://breakingintowallstreet.com/biws-premium/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)
: Learn accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up with 10+ real-life case studies from around the world. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/core-financial-modeling/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&mini=true)
[Email](mailto:?subject=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&mini=true)
[](mailto:?subject=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[](https://api.whatsapp.com/send?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Copy](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/#)
[Email](mailto:?subject=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&t=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2022/01/04221631/The-mid-year-convention.jpg&description=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[Print](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/mid-year-convention-dcf/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[SMS](sms:?&body=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[X](https://x.com/intent/tweet?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fmid-year-convention-dcf%2F&title=The%20Mid-Year%20Convention%20and%20Mid-Year%20Discounting%20in%20a%20DCF%20with%20Stub%20Periods&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2022/01/04221631/The-mid-year-convention.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand