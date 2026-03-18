# Present Value (PV): Definition & Calculations

**Source:** https://breakingintowallstreet.com/kb/finance/present-value

---

Present Value (PV): Definition and Example Calculations
=======================================================

The Present Value (PV) of an investment is what that investment’s future cash flows are worth TODAY based on the annualized rate of return you could potentially earn on other, similar investments (called the “Discount Rate”).

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/finance/present-value/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/finance/present-value/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/finance/present-value/#tab-signup)
    

Present Value (PV): Definition and Example Calculations

> Present Value Definition
> ------------------------
> 
> The Present Value (PV) of an investment is what that investment’s future cash flows are worth **TODAY** based on the annualized rate of return you could potentially earn on other, similar investments (called the “Discount Rate”).

This concept of **Present Value** is critical in valuation because it determines what assets and companies are worth.

The foundation here is the [time value of money](https://breakingintowallstreet.com/kb/finance/time-value-of-money/)
, i.e., that $100 today is worth MORE than $100 in 1-2 years from now because you could invest that $100 today and earn more by then.

Yes, there’s also inflation, but that’s **not** the key factor; in an environment with 0% inflation, $100 today would also be worth more than $100 in 1-2 years because you could still invest it and end up with _more than_ $100 in 1-2 years.

What is Present Value (PV)?
---------------------------

Suppose that you received $100 today, and you could invest it and earn 5% per year on it.

That means that in 5 years, its [future value](https://breakingintowallstreet.com/kb/finance/future-value/)
 will be $100 \* (1 + 5%) ^ 5 = $127.63.

In other words, you multiply the $100 by (1 + 5%) to get $105, and then you multiply the $105 by (1 + 5%), and so on, until you get its value at the end of Year 5.

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

If you know this **future value** of $127.63 and your annualized rate of return – the [Discount Rate](https://breakingintowallstreet.com/kb/finance/discount-rate/)
, or 5% here – you can use this information to calculate the **Present Value**, or what it’s worth today:

![Present Value Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201112%20234'%3E%3C/svg%3E "Present Value Formula")

![Present Value Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20390'%3E%3C/svg%3E "Present Value Example")

[You can download our Present Value template here](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/BIWS-Present-Value-Examples.xlsx)
 to try different assumptions and see how the PV changes.

All company valuation, such as the [Discounted Cash Flow (DCF) model](https://mergersandinquisitions.com/dcf-model/)
, is based on this concept of forecasting a company’s cash flows into the future and then discounting them to today’s values based on how much you could earn on them today.

But rather than just discounting one cash flow to Present Value, you project the company’s financials over a 5, 10, or 20-year period and discount every single cash flow to Present Value.

Also, you normally estimate a “[Terminal Value](https://breakingintowallstreet.com/how-to-calculate-terminal-value/)
” for the company to represent what it’s worth after that period, and you discount that to Present Value and add it to the PV of all the cash flows to determine the entire company’s estimated value.

Here’s what it looks like when we take the Present Value of a company’s cash flows over a 10 year period and also take the Present Value of its “Terminal Value” and add that:

![Real-Life Present Value Application](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201462%20458'%3E%3C/svg%3E "Real-Life Present Value Application")

Confusingly, the **NPV function in Excel** calculates the _Present Value_, **not** the Net Present Value – _if you enter all positive cash flows_ over the forecast period:

![Present Value and the NPV Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201474%20460'%3E%3C/svg%3E "Present Value and the NPV Function")

To calculate the [Net Present Value](https://breakingintowallstreet.com/kb/finance/net-present-value/)
 instead, you must enter a negative cash flow in the beginning to represent the upfront purchase price or subtract the upfront price manually in the formula.

The Present Value (PV) Calculation
----------------------------------

To calculate Present Value in real life, you need to know the future cash flows of an investment and the **Discount Rate**, which represents your opportunity cost or expected annualized return.

For real companies, you calculate the Discount Rate using the Weighted Average Cost of Capital (WACC) formula, which we describe in separate articles ([how to calculate the Discount Rate](https://breakingintowallstreet.com/how-to-calculate-discount-rate/)
 and the [WACC formula](https://mergersandinquisitions.com/wacc-formula/)
).

You normally measure the company’s annual stock returns/volatility, interest expense, and other factors to estimate how much an investment in the company might return, on average, over the long term.

As an approximation in this simple example, you could just say that the Discount Rate represents **what you expect to earn** on other, similar investments.

So, let’s say you expect a cash inflow of $10,000 five years from now and use a Discount Rate of 8% to represent the risk and opportunity cost.

Plugging these values into the calculator, you get:

![Present Value Interpretation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20448'%3E%3C/svg%3E "Present Value Interpretation")

The **Present Value** here is approximately $6,806. You could interpret this in the following ways:

**1) Future Value** – If you invest this $6,806 today and earned 8% per year on it, compounded, you would end up with $10,000 after 5 years.

**2) Ability to Pay** – If you earn $10,000 from an investment in 5 years (and nothing in between now and then), you would be _willing to pay_ $6,806 for it today because you could earn 8% per year on this $6,806 starting today.

Other Applications of Present Value (PV) in Real Life
-----------------------------------------------------

Outside of company valuation, Present Value is widely used in fields such as real estate and fixed-income (bond) analysis.

For example, you could estimate a property’s value based on the Present Value of rental income and other cash flows from it, and you could determine a bond’s price based on its future cash flows and the appropriate Discount Rate.

The whole idea of [bond yields](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
 is closely linked to the Discount Rate and the time value of money, so a bond’s “price” is closely related to the Present Value of cash flows from that bond.

For more, please see our series on the [current yield](https://breakingintowallstreet.com/kb/debt-equity/current-yield/)
, [yield to call](https://breakingintowallstreet.com/kb/debt-equity/yield-to-call/)
, [yield to maturity](https://breakingintowallstreet.com/kb/debt-equity/yield-to-maturity/)
, and [yield to worst](https://breakingintowallstreet.com/kb/debt-equity/yield-to-worst/)
.

Present Value always puts future cash flows in _today’s context_, which lets you make better investment decisions.

[Sign Up To Core Financial Modeling](https://breakingintowallstreet.com/core-financial-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Present Value Calculations - Examples (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Finance/BIWS-Present-Value-Examples.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&mini=true)
[Email](mailto:?subject=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)

#### Learn Financial Modeling from A to Z

Learn accounting, valuation, and financial modeling from the ground up with 10+ global case studies.

[LEARN MORE](https://breakingintowallstreet.com/core-financial-modeling/)

[](https://x.com/intent/tweet?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[](https://www.linkedin.com/shareArticle?title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&mini=true)
[](mailto:?subject=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[](https://api.whatsapp.com/send?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Copy](https://breakingintowallstreet.com/kb/finance/present-value/#)
[Email](mailto:?subject=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&t=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/finance/present-value/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2024/02/04221304/Present-Value-PV.jpg&description=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[Print](https://breakingintowallstreet.com/kb/finance/present-value/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[SMS](sms:?&body=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[X](https://x.com/intent/tweet?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Ffinance%2Fpresent-value%2F&title=Present%20Value%20%28PV%29%3A%20Definition%20and%20Example%20Calculations&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2024/02/04221304/Present-Value-PV.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand