# Net Present Value (NPV): Definition and Example Calculations

**Source:** https://breakingintowallstreet.com/kb/finance/net-present-value

---

Net Present Value (NPV): Definition and Example Calculations
============================================================

Net Present Value (NPV) equals the sum of an asset’s discounted future cash flows minus the upfront cost or “asking price” for this asset today; a positive NPV means that you can achieve more than your targeted returns by investing, while a negative NPV means the opposite.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/finance/net-present-value/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/finance/net-present-value/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/finance/net-present-value/#tab-signup)
    

Net Present Value (NPV): Definition and Example Calculations

> **Net Present Value (NPV) Definition:** Net Present Value (NPV) equals the sum of an asset’s discounted future cash flows minus the upfront cost or “asking price” for this asset today; a positive NPV means that you can achieve more than your targeted returns by investing, while a negative NPV means the opposite.

To understand Net Present Value, you must first understand [Present Value](https://breakingintowallstreet.com/kb/finance/present-value/)
, or what an investment’s future cash flows are worth TODAY based on the annualized rate of return you could potentially earn on other, similar investments (called the “Discount Rate”).

Net Present Value goes a step further and subtracts the investment’s upfront cost or “asking price” to determine if its **Present Value** exceeds its **current cost**.

If it does, it suggests that you should invest; if it does not, an investment may not achieve your desired goals.

Net Present Value is critical because it helps investors determine if an investment is worthwhile by comparing the _actual_ annualized return to the _targeted_ annualized return (the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
).

### **Files & Resources:**

*   [Simple Template for Net Present Value, IRR, and WACC (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/PV-NPV-IRR-WACC.xlsx)
    

**Simple Rules for the Net Present Value**
------------------------------------------

The NPV, PV, Discount Rate, and IRR are all linked by simple rules. We defined the NPV and PV above, but for the latter two:

*   **Discount Rate:** This represents your _targeted or expected_ annualized return on investment. We normally use the [Weighted Average Cost of Capital (WACC)](https://mergersandinquisitions.com/wacc-formula/)
     for this when valuing companies, but other methods are possible, such as the Cost of Equity.

*   **Internal Rate of Return (IRR):** This represents the _actual_ annualized return you could earn from an investment based on your forecasts for it and the upfront cost or “asking price.”

Based on this, we can say:

*   **NPV is Positive:** This means the IRR exceeds the Discount Rate. In other words, the future cash flows of an investment are worth more to you today than its cost.
*   **NPV is Zero:** This means the IRR equals the Discount Rate, so the future cash flows are worth the same as its cost today.
*   **NPV is Negative:** This means the IRR is less than the Discount Rate, so the future cash flows are worth less to you today than the cost of the investment.

Here are a few simple examples of these relationships in Excel, based on a simple example of buying an apartment for $200,000, earning $12,000 of income from it per year, and selling it again for $200,000 after 5 years.

### **Positive NPV:**

![Positive Net Present Value (NPV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201491%20714'%3E%3C/svg%3E "Positive Net Present Value (NPV)")

### **Negative NPV:**

![Negative Net Present Value (NPV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201497%20711'%3E%3C/svg%3E "Negative Net Present Value (NPV)")

### **Zero NPV:**

![Zero Net Present Value (NPV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201499%20710'%3E%3C/svg%3E "Zero Net Present Value (NPV)")

**Notice that all that changes in each example is the Discount Rate, or our _expectations_ for the annualized returns.**

Like dating, you can always get a positive result if you lower your expectations enough.

Other ways to change the Net Present Value include modifying the upfront cost, the apartment’s selling price, or the annual income earned by renting out this property.

But, as with dating once again, these are the equivalent of “doing work on yourself” to improve, so they all require more time and effort and may or may not be feasible.

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

**How to Calculate the Net Present Value in Excel**
---------------------------------------------------

Confusingly, the NPV function in Excel calculates _both_ the Present Value (PV) and the Net Present Value (NPV) of an investment, depending on what you input into the function.

*   **Present Value:** If you want to calculate _just_ the Present Value, input only the _positive future cash flows_ from the investment and the Discount Rate and ignore the upfront cost. Here’s an example:

![Present Value vs. Net Present Value (NPV)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201498%20714'%3E%3C/svg%3E "Present Value vs. Net Present Value (NPV)")

*   **Net Present Value:** If you want to factor in the upfront cost or asking price, change the formula so that it includes this negative number in the beginning:

![Net Present Value (NPV) with the NPV Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201492%20707'%3E%3C/svg%3E "Net Present Value (NPV) with the NPV Function")

There is another option for calculating the Net Present Value as well: We could take the PV of the future cash flows and subtract the upfront cost, but the results will differ slightly because of how the NPV function works:

![Manual Net Present Value (NPV) Calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201496%20758'%3E%3C/svg%3E "Manual Net Present Value (NPV) Calculation")

In general, it’s best to use Excel’s built-in NPV function to calculate the Net Present Value consistently.

Also, it’s essential if there are _multiple_ upfront investments required to buy an asset or company, as in the example below:

![Net Present Value (NPV) for Multiple Upfront Investments](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201659%20983'%3E%3C/svg%3E "Net Present Value (NPV) for Multiple Upfront Investments")

**How to Use Net Present Value in Real Life**
---------------------------------------------

To calculate the Net Present Value in real life, you need to estimate the [future cash flows](https://breakingintowallstreet.com/how-to-calculate-unlevered-free-cash-flow/)
 of an investment, the WACC (discount rate), and the cost of the initial investment.

For real companies, you calculate the Discount Rate using the Weighted Average Cost of Capital (WACC) formula, which we describe in separate articles ([how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/)
 and the [WACC formula](https://mergersandinquisitions.com/wacc-formula/)
).

You can make an investment decision based on either the IRR and WACC or the NPV:

*   **If IRR > WACC, NPV is positive, so you invest.**
*   **If IRR < WACC, NPV is negative, so you do not invest.**

In the following example, the Virgin Company is determining whether they should invest in Virgin Galactic (for trips to Jupiter) or Virgin Asia (for low-cost flights to Southeast Asia).

Each subsidiary has its own Discount Rate because sending passengers to Jupiter is much riskier than operating low-cost flights to Southeast Asia.

The Virgin Galactic plan has a higher IRR, but the upfront cost is also much higher, which means its **Net Present Value** is lower.

Therefore, it makes more sense to launch Virgin Asia since it has a higher **Net Present Value** despite having a lower IRR:

![Net Present Value (NPV) by Business Segment](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201456%201274'%3E%3C/svg%3E "Net Present Value (NPV) by Business Segment")

**Other Applications of Net Present Value (NPV)**
-------------------------------------------------

Net Present Value is widely used in analyses such as the [Discounted Cash Flow (DCF) model](https://mergersandinquisitions.com/dcf-model/)
 to value companies and in planning and budgeting in roles such as [FP&A at normal companies](https://mergersandinquisitions.com/fpa-director/)
.

It’s also common in [real estate investing](https://mergersandinquisitions.com/real-estate-private-equity/)
, [fixed income research](https://mergersandinquisitions.com/fixed-income-research/)
, [credit analysis](https://mergersandinquisitions.com/credit-analyst-career-path/)
, and even [venture capital and startup modeling](https://breakingintowallstreet.com/kb/venture-capital/)
 to determine a growth company’s potential value.

It’s not quite as common in [M&A analysis and merger models](https://breakingintowallstreet.com/kb/ma-and-merger-models/merger-model-walkthrough/)
 because they often focus on short-term [EPS accretion/dilution](https://breakingintowallstreet.com/kb/ma-and-merger-models/eps-accretion-dilution/)
, but even there, it can come up in valuations.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Template for Net Present Value, IRR, and WACC (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/PV-NPV-IRR-WACC.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&mini=true)
[Email](mailto:?subject=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[](https://www.linkedin.com/shareArticle?title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&mini=true)
[](mailto:?subject=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[](https://api.whatsapp.com/send?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Copy](https://breakingintowallstreet.com/kb/finance/net-present-value/#)
[Email](mailto:?subject=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&t=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/net-present-value/)
[Pinterest](https://breakingintowallstreet.com/kb/finance/net-present-value/#)
[Print](https://breakingintowallstreet.com/kb/finance/net-present-value/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[SMS](sms:?&body=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[X](https://x.com/intent/tweet?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fnet-present-value%2F&title=Net%20Present%20Value%20%28NPV%29%3A%20Definition%20and%20Example%20Calculations&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand