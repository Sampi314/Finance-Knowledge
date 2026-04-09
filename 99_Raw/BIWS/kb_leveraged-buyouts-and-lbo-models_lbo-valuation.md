# LBO Valuation: Full Tutorial + Excel Example

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation

---

LBO Valuation: The Power of Middle-School Math to Reverse a Model
=================================================================

In an “LBO valuation,” you \*reverse\* the standard leveraged buyout model setup and \*back into\* the purchase price based on the assumed exit multiple, exit year, and cash flows in the holding period; you can use Goal Seek or VBA to set this up, but you can also simplify the model and do it entirely with normal Excel formulas.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#tab-signup)
    

> **LBO Valuation:** In an “LBO valuation,” you \*reverse\* the standard leveraged buyout model setup and \*back into\* the purchase price based on the assumed exit multiple, exit year, and cash flows in the holding period; you can use Goal Seek or VBA to set this up, but you can also simplify the model and do it entirely with normal Excel formulas.

In [LBO modeling tests](https://mergersandinquisitions.com/lbo-modeling-test/)
 and case studies, you might be asked to create an “LBO valuation,” in which you value a company based on the **maximum price** that a PE firm can pay to achieve a **minimum return**.

For example, how much can the PE firm pay if it wants to earn a 20% annualized return over 5 years?

Since you are solving for the **maximum price**, the LBO valuation normally sets the “floor” for a company’s value in a deal.

If you have a traditional [LBO model](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/simple-lbo-model-excel/)
, you could use Goal Seek with the IRR in the exit year and back into the purchase price or purchase multiple like this:

![LBO Valuation via Goal Seek](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201910%20449'%3E%3C/svg%3E "LBO Valuation via Goal Seek")

But if you have more time, you can also use a few Excel formulas to calculate the purchase multiple based on the targeted IRR and exit year in a more robust way:

![LBO Valuation - IRR and Exit Year as Model Drivers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201906%20595'%3E%3C/svg%3E "LBO Valuation - IRR and Exit Year as Model Drivers")

We’ll walk through the steps in this process below, starting with the “Before” file and concluding with the “After” file:

### **Files & Resources:**

*   [LBO Valuation – Before (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-Before.xlsx)
    
*   [LBO Valuation – After (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-After.xlsx)
    
*   [LBO Valuation Walkthrough – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-Slides.pdf)
    

**LBO Valuation, Step 1: Make Model Modifications**
---------------------------------------------------

Start by adding fields for the Targeted IRR, Exit Year, Exit Equity Proceeds, and Required Investor Equity in the top “Assumptions” area of a standard LBO model:

![LBO Valuation - Additional Fields](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20888%20451'%3E%3C/svg%3E "LBO Valuation - Additional Fields")

You can apply Data Validation to the Targeted IRR and Exit Year based on your model setup and the number of years in the holding period.

You can use XLOOKUP to bring in the Exit Equity Proceeds from the bottom of the model in the returns area:

![Exit Equity Proceeds in an LBO](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201654%20374'%3E%3C/svg%3E "Exit Equity Proceeds in an LBO")

**LBO Valuation, Step 2: Calculate the Required Investor Equity**
-----------------------------------------------------------------

Next, you “back into” the Investor Equity required to earn the specified IRR over this time frame.

To do this, you can use the Compound Annual Growth Rate (CAGR) formula:

**CAGR** = (Ending Value / Starting Value) ^ (1 / # Years) – 1

And then you can use algebraic manipulation as follows to solve for the Starting Value:

![Reversing the CAGR Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201894%201202'%3E%3C/svg%3E "Reversing the CAGR Formula")

In Excel, the formula looks like this:

![Required Investor Equity Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20915%20360'%3E%3C/svg%3E "Required Investor Equity Formula")

**LBO Valuation, Step 3: Back Into the Purchase Enterprise Value and Purchase Multiple**
----------------------------------------------------------------------------------------

Note that the Required Investor Equity here is **NOT** the same as the Purchase Equity Value.

The Investor Equity is a component of the Sources side of the [Sources & Uses schedule](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/sources-and-uses/)
, so you must calculate Total Sources first by adding the Debt used in this deal to the Required Investor Equity.

You’ll also have to add a few additional lines to support these calculations:

![Required Total Sources in an LBO Valuation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20885%20565'%3E%3C/svg%3E "Required Total Sources in an LBO Valuation")

Then, since Total Sources = Total Uses, and Total Uses = Purchase Enterprise Value + Fees + Minimum Cash, you can say:

**Purchase Enterprise Value** = Total Uses – Fees – Minimum Cash

And then you can divide this by the EBITDA as of the deal announcement date to determine the required purchase multiple:

![Required Purchase Multiple in an LBO Valuation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201026%20574'%3E%3C/svg%3E "Required Purchase Multiple in an LBO Valuation")

You can test this setup by plugging in different values, such as a 25% IRR over 5 years or a 35% IRR over 4 years, and entering the calculated purchase multiple into the assumption at the top.

If it produces the 25% or 35% IRR you are seeking in the returns area at the bottom, the formula works.

**LBO Valuation: How to Make the IRR and Exit Year the Drivers and Fix Circular References**
--------------------------------------------------------------------------------------------

If you want to make this setup more **robust** by making the Targeted IRR and Exit Year model drivers, you can link the Purchase Multiple at the top to the calculated or required multiple.

This produces an immediate [circular reference](https://breakingintowallstreet.com/kb/excel/circular-reference-excel/)
:

![LBO Valuation and Circular References](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201066%201125'%3E%3C/svg%3E "LBO Valuation and Circular References")

This occurs because of the **fees:** The transaction fees depend on the Purchase Equity Value, but the Purchase Equity Value flows from the Purchase Enterprise Value, and these fees determine the Purchase Enterprise Value:

Purchase Equity Value –> Transaction Fees –> Total Sources/Uses –> Purchase Enterprise Value –> Purchase Equity Value

The simplest fix is to make the Transaction Fees a **constant $10 million** so they do not change with the deal price (which is reasonable within a narrow price range):

![Constant Transaction Fees to Remove the Circular References](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201917%20444'%3E%3C/svg%3E "Constant Transaction Fees to Remove the Circular References")

The Financing Fees and Minimum Cash should not have any circular dependencies.

**Footnotes, Fine Print, and Limitations**
------------------------------------------

As noted above, any circular reference in this model disrupts the calculations and the LBO valuation setup.

So, you should remove any circular references in the interest calculations, returns calculations, and other schedules before implementing this.

Also, if the model includes a [dividend recap](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
, [bolt-on acquisitions](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/bolt-on-acquisitions/)
, or [additional equity investments/distributions](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/cash-flow-lbo/)
 in the holding period, the simple CAGR formula for IRR will not work.

This “trick” relies on the same techniques used to make [quick IRR estimates](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
 and answer [LBO interview questions](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-interview-questions/)
, and it has the same limitations.

**Specifically, any cash inflows or outflows \*during\* the holding period complicate the IRR calculation and make it more than just the simple CAGR formula.**

In theory, you could try to work around this by incorporating their effects into the formula, but in practice, it’s probably not worth the time/effort.

In complex cases like these, we recommend using Goal Seek or Goal Seek + [VBA](https://breakingintowallstreet.com/kb/excel/excel-vba-programming/)
 to automate the process and refresh the model whenever a key assumption changes.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) LBO Valuation Walkthrough - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) LBO Valuation - Before (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) LBO Valuation - After (XL)](https://youtube-breakingintowallstreet-com.s3.dualstack.us-east-1.amazonaws.com/109-28-LBO-Valuation-After.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Private Equity Modeling (LBO Course)](https://breakingintowallstreet.com/private-equity-modeling/)

Master LBO modeling, paper LBOs, and case studies with 6 conceptual models and 6 full, step-by-step case studies. Includes interview questions, paper LBOs, and "quick business evaluation" exercises as well.

[Learn More](https://breakingintowallstreet.com/private-equity-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Private Equity Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/mM8atoiV)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A modeling from the ground up, along with a "deep dive" into leveraged buyouts, LBO models, and PE case studies. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/mM8atoiV)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&mini=true)
[Email](mailto:?subject=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[](https://www.linkedin.com/shareArticle?title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&mini=true)
[](mailto:?subject=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[](https://api.whatsapp.com/send?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#)
[Email](mailto:?subject=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&t=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[LinkedIn](https://www.linkedin.com/shareArticle?title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/lbo-valuation/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[SMS](sms:?&body=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[X](https://x.com/intent/tweet?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[WhatsApp](https://api.whatsapp.com/send?text=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Flbo-valuation%2F&title=LBO%20Valuation%3A%20The%20Power%20of%20Middle-School%20Math%20to%20Reverse%20a%20Model&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand