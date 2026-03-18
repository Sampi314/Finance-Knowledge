# Section 382 Limitations and Net Operating Losses in M&A

**Source:** https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382

---

Section 382 Limitations and Net Operating Losses (NOLs) in the U.S. Tax Code
============================================================================

In this lesson, you’ll learn how the Section 382 limitations on Net Operating Loss (NOL) usage affect M&A deals and determine the transaction structures that Acquirers are likely to use.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/#tab-signup)
    

Section 382 Limitations and Net Operating Losses (NOLs) in the U.S. Tax Code

> **Section 382 Definition:** Section 382 of the U.S. tax code states that an Acquirer in an M&A deal structured as a Stock Purchase may use only a limited amount of the Target’s Net Operating Losses (NOLs) to reduce its Taxable Income each year and must write down the remaining NOL balance that will go unused.

The U.S. tax code is complicated and confusing, and Section 382 is a small part of it that sometimes affects [merger models](https://breakingintowallstreet.com/kb/ma-and-merger-models/merger-model-walkthrough/)
.

If you want the detailed “academic” treatment of this term, [take a look at Cornell’s summary here](https://www.law.cornell.edu/uscode/text/26/382)
.

We’re going to focus on the **practical implications in financial models** in this tutorial:

**Why Do Net Operating Losses Matter in M&A Deals?**
----------------------------------------------------

Traditionally, we discuss [Net Operating Losses (NOLs)](https://breakingintowallstreet.com/kb/accounting/net-operating-losses/)
 in the context of a company’s standalone operating performance.

If the company loses money (i.e., negative Pre-Tax Income) in one period, it accrues “losses” that it can use to reduce its Taxable Income in future periods.

**However, many companies lose money over long periods and build up _substantial NOL balances_ that could make them more attractive to potential acquirers**.

![Advanced M&A Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Advanced M&A Modeling for Investment Banking

*   #### Build a quarterly merger model with variable close dates
    
    You’ll learn to build “industrial-strength” M&A models for real-life deals
    
*   #### Analyze tax-free spinoff transactions
    
    Learn more advanced structures and analyze deals using Sum-of-the-Parts valuation
    
*   #### Model majority-stake acquisitions
    
    Understand the model setup and how the EPS accretion/dilution is counterintuitive
    

[Full Details](https://breakingintowallstreet.com/advanced-ma-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Advanced-MA-Course-Outline.pdf)

But it’s not as simple as an Acquirer finding a Target with a huge NOL balance and then acquiring the Target and “taking” all its NOLs.

First of all, the transaction must be structured as a **Stock Purchase** rather than an Asset Purchase or 338(h)(10) Election (a deal type specific to the U.S. tax code).

A “Stock Purchase” means that the Acquirer gets all the Target’s Assets and Liabilities _and_ all its off-Balance Sheet line items.

But in an “Asset Purchase,” the Acquirer selects the specific Assets it wants to acquire and the specific Liabilities it will assume, and it pays for _only_ the Assets Acquired – Liabilities Assumed:

![Stock Purchases vs. Asset Purchases](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20756%20467'%3E%3C/svg%3E "Stock Purchases vs. Asset Purchases")

These transaction structures also create tax implications in models.

The main one is that the depreciation & amortization on asset write-ups is **not** cash-tax-deductible in Stock Purchases but **is** deductible in Asset Purchases.

**Also, in an Asset Purchase or 338(h)(10) deal, the Target’s Net Operating Losses are written down 100%, so the Acquirer CANNOT use them after the deal closes.**

Therefore, if an Acquirer finds a Target with a huge NOL balance, it _must_ purchase the Target with a deal structured as a Stock Purchase – or the Target’s NOLs will be useless.

**What Do the Section 382 Limitations Say About NOLs in M&A Deals?**
--------------------------------------------------------------------

Section 382 says that the maximum allowable annual usage of a Target’s NOLs equals the Equity Purchase Price \* the Maximum of the Past 3 Months’ “Adjusted Long-Term Rates.”

For example, let’s say the Target’s [Equity Value](https://www.mergersandinquisitions.com/enterprise-value-vs-equity-value/)
 or Market Cap is $500 million. This Target also has $100 million in NOLs.

The Acquirer offers a 20% premium for the Target, so the Equity Purchase Price is $600 million.

The “Adjusted Long-Term Rates” are determined by the IRS (the tax agency in the U.S.), and [you can find a monthly list here](https://apps.irs.gov/app/picklist/list/federalRates.html)
.

These rates are close to the current Federal Funds Rate, or the interest rate that banks charge each other to borrow money. The Federal Reserve normally sets this rate.

So, if the Adjusted Long-Term Rates over the past 3 months were 1.0%, 1.5%, and 2.0%, the Acquirer in this deal could use:

*   $600 million \* MAX(1.0%, 1.5%, 2.0%) = $600 million \* 2.0% = $12 million per year of the Target’s NOLs

Would the Acquirer have to write down any portion of the Target’s NOL balance in this case?

**We don’t know because we don’t know when the Target’s NOLs expire – and there’s always an expiration date, which depends on the country and region (state/province).**

For example, let’s say that the Target’s NOLs expire 20 years after the deal closes.

Since 20 \* $12 million = $240 million, which is greater than the Target’s balance of $100 million, the Acquirer will be able to use all the Target’s NOL before they expire.

Therefore, it will not write down any portion of the NOLs in this case.

On the other hand, let’s say that the NOLs expire 5 years after the deal closes.

In this case, 5 \* $12 million = $60 million, which is _less than_ the Target’s balance of $100 million.

Therefore, the Acquirer cannot use all the Target’s NOLs, so it will have to write down $100 million – $60 million = **$40 million** when the deal closes.

**The bottom line is that if an Acquirer wants to do a deal because of the Target’s NOLs, it will have to scrutinize the expiration date(s) of those NOLs before making an offer to acquire the Target.**

Otherwise, the Acquirer could end up with an expensive asset that’s not very useful.

**Section 382 Limitations in a Real-Life Quarterly Merger Model**
-----------------------------------------------------------------

In a real merger model, you would apply Section 382 by finding the Target’s Net Operating Losses and calculating how much the Acquirer could use each year:

![Merger Model - Allowable NOL Usage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20323'%3E%3C/svg%3E "Merger Model - Allowable NOL Usage")

In this deal, no write-down is necessary because the Acquirer can easily apply the Target’s entire NOL balance before the NOLs expire.

But if the expiration period were much shorter, such as 3 years, a write-down would be necessary:

![Merger Model - Allowable NOL Usage with Shorter Expiration Period](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20311'%3E%3C/svg%3E)

Continuing with the first scenario here – the NOLs that expire in 10 years – we continue with the rest of the model by calculating the Taxable Income for the combined company.

We do this by adding together the Income Statements of the Acquirer and Target and adjusting for acquisition effects, such as the interest paid on new debt, the foregone interest on cash, and the depreciation & amortization on asset write-ups created in the deal.

Since this new D&A is **not** cash-tax deductible in a Stock Purchase, the Taxable Income looks like this:

![Taxable Income in a Stock Purchase M&A Deal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20279'%3E%3C/svg%3E "Taxable Income in a Stock Purchase M&A Deal")

Once we’ve calculated the “Pre-NOL Cash Taxable Income,” we can apply the amount of NOLs the Acquirer can use in each period.

The annual amount of $21.5 million is divided by 4 since this is a quarterly model:

![Section 382 Limitations on NOL Usage](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20647'%3E%3C/svg%3E "Section 382 Limitations on NOL Usage")

Because the Target’s NOL balance is so small here – less than $100 million vs. an Equity Purchase Price of $2.5 billion – it barely makes a difference.

The NOLs are a nice bonus for the Acquirer, but hardly a primary reason to do the deal.

The Section 382 limitations tend to make a bigger difference when:

1) The Target’s NOL balance is large relative to its Equity Purchase Price (e.g., 20%+); and

2) Interest rates are low, so the annual NOL usage is quite limited; and

3) The combined company has positive Taxable Income above the allowable NOL usage in each period.

_Some_ deals are motivated by the Target’s Net Operating Losses, but they’re not common in most industries.

Even in fields like technology and biotech, where early-stage startups lose huge sums of money, most acquisitions are motivated by companies’ **technology** and **intellectual property** rather than their tax attributes.

But an Acquirer will never say “no” to the bonus of an NOL balance acquired in a deal – at least, not if it understands Section 382 of the U.S. tax code.

_**This tutorial is a small taste of the knowledge you’ll gain in our paid courses.**_ **Breaking Into Wall Street** _**uses real-life modeling tests and interview case studies to prepare you for investment banking and private equity interviews – and a leg up once you win your offer and start working. Find out more about our advanced training by via the button below:**_

[Sign Up for Advanced M&A Modeling](https://breakingintowallstreet.com/advanced-ma-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/11-12-Book-vs-Cash-Taxes-Part-1.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Adjusted Long-Term Rates at the Time of This Deal (PDF)](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/11-12-Adjusted-Long-Term-Rates.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Section 382 Limitations and Net Operating Losses - Before (XL)](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/11-12-Book-vs-Cash-Taxes-Part-1-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Section 382 Limitations and Net Operating Losses - After (XL)](https://samples-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Mastery/11-12-Book-vs-Cash-Taxes-Part-1-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&mini=true)
[Email](mailto:?subject=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)

#### Master Advanced M&A Modeling

Learn quarterly merger models, advanced deal structures, spinoffs, and majority stake deals via 4 global case studies.

[LEARN MORE](https://breakingintowallstreet.com/advanced-ma-modeling/)

[](https://x.com/intent/tweet?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[](https://www.linkedin.com/shareArticle?title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&mini=true)
[](mailto:?subject=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[](https://api.whatsapp.com/send?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Copy](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/#)
[Email](mailto:?subject=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&t=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2021/07/04222334/section-382.jpg&description=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[Print](https://breakingintowallstreet.com/kb/ma-and-merger-models/section-382/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[SMS](sms:?&body=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[X](https://x.com/intent/tweet?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fma-and-merger-models%2Fsection-382%2F&title=Section%20382%20Limitations%20and%20Net%20Operating%20Losses%20%28NOLs%29%20in%20the%20U.S.%20Tax%20Code&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2021/07/04222334/section-382.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand