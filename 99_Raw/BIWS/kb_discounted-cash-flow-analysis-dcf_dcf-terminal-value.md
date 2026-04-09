# DCF - Terminal Value - Gordon Growth Method Intuition [Video Tutorial]

**Source:** https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value

---

DCF – Terminal Value – Gordon Growth Method Intuition (24:35)
=============================================================

We review the \*intuition\* behind the Gordon Growth Formula used to calculate Terminal Value in a Discounted Cash Flow (DCF) analysis.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/#tab-signup)
    

DCF - Terminal Value - Gordon Growth Method Intuition

Gordon Growth Method Intuition
------------------------------

The basic intuition here is that we can pay:

### Annual Free Cash Flow / Discount Rate

For an investment, if the cash flow stays the same each year and we’re targeting a specific yield on our investment (known as the “discount rate” in a [DCF model](https://www.mergersandinquisitions.com/dcf-model/)
).

Why?

Think about if you could make an investment that earned $100 in cash flows each year.

You’re targeting a 10% yield on your investment.

How much could you pay for it?

$1,000, because $1,000 \* 10% = $100 in cash flows each year.

You can use the NPV function in Excel with $100 in cash flow each year (e.g., =NPV(10%, Long series of $100 you’ve entered in consecutive cells)) to verify this.

The NPV, or “[net present value](https://breakingintowallstreet.com/kb/finance/net-present-value/)
,” IS this number – what we could afford to pay for a series of cash flows at a given yield we’re targeting.

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

The Intuition — Growth in Cash Flows

This works fine if there’s no growth and the cash flows stay the same each year, but what if they’re growing?

Well, in that case we can afford to pay MORE than that $1,000 and still get the same 10% yield… because there’s growth!

Specifically, we can now pay:

### First Year Free Cash Flow / (Discount Rate – FCF Growth Rate)

for this investment.

In the Terminal Value calculation, that “First Year Free Cash Flow” is written as Final Year Projected Free Cash Flow \* (1 + FCF Growth Rate)…

…because we’re going one year BEYOND the end of our projection period in the model.

By \*subtracting\* the growth rate in the denominator, we make the denominator smaller… which makes the amount we can pay significantly bigger.

If cash flows grow more quickly, the denominator gets even smaller and the entire number gets even bigger.

If cash flows grow more slowly, the denominator gets bigger and the entire number gets smaller.

Let’s say the cash flows start at $100 and grow by 3% per year.

We’re targeting a discount rate of 10%.

The NPV here would be $1,429, or $100 / (10% – 3%).

Why does this work?

Why can we pay $1,429 and still get that 10% yield?

Think about it like this…

The yield in Year 1 is is $100 / $1429, or 7.0%

But then by Year 5, it’s $113 / $1429, or 7.9%.

And then as you keep going, the Yield gets higher and higher… because we have growth.

By Year 20, it’s $175 / $1429, or 12.3%.

So, over all those years into the future, the average comes out to 10%… because it’s LESS than 10% in the early years and greater than 10% much later on.

So the weighted average, factoring in the [time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
, still comes out to that 10% yield we were targeting.

The Algebra Behind Gordon Growth
--------------------------------

Please see the video for this part – it’s almost impossible to explain in text form.

Gordon Growth Method Summary
----------------------------

We care about this because everyone uses this formula to calculate Terminal Value in a DCF, but hardly anyone explains where it comes from.

The basic idea is that you can pay more for a company that’s growing its cash flows than for one that’s NOT growing its cash flows.

And to represent that, you use the formula:

Final Year, Projected Period Free Cash Flow \* (1 + FCF Growth Rate) / (Discount Rate – FCF Growth Rate)

To approximate the amount you could pay for the Free Cash Flows in the Terminal Period – which is the Terminal Value in a DCF.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

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

[X](https://x.com/intent/tweet?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&mini=true)
[Email](mailto:?subject=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[](https://www.linkedin.com/shareArticle?title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&mini=true)
[](mailto:?subject=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[](https://api.whatsapp.com/send?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Copy](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/#)
[Email](mailto:?subject=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&t=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/01/19075639/DCF-Terminal-Value-Gordon-Growth-Method-Intuition.jpg&description=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[Print](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/dcf-terminal-value/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[SMS](sms:?&body=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[X](https://x.com/intent/tweet?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[WhatsApp](https://api.whatsapp.com/send?text=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fdiscounted-cash-flow-analysis-dcf%2Fdcf-terminal-value%2F&title=DCF%20-%20Terminal%20Value%20-%20Gordon%20Growth%20Method%20Intuition%20%2824%3A35%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/01/19075639/DCF-Terminal-Value-Gordon-Growth-Method-Intuition.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand