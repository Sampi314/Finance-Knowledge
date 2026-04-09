# SaaS Accounting: Bookings, Billings, and Revenue

**Source:** https://breakingintowallstreet.com/kb/venture-capital/saas-accounting

---

SaaS Accounting: Bookings, Billings, Revenue, Deferred Revenue, and Accounts Receivable
=======================================================================================

In this tutorial, you’ll learn how SaaS accounting works and how line items on the financial statements change as a SaaS company bills customers, delivers services, and recognizes revenue.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#tab-signup)
    

SaaS Accounting: Bookings, Billings, Revenue, Deferred Revenue, and Accounts Receivable

> **SaaS Accounting Definition:** Software-as-a-Service (SaaS) accounting rules explain how common line items, such as revenue, deferred revenue, and accounts receivable, change as a software company bills customers, collects cash, and delivers services.

Many people incorrectly think that a SaaS company “only” has Deferred Revenue (DR) to reflect the cash collected from customers but not yet recognized as revenue.

![Venture Capital & Growth Equity Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Model and Value Startups, Understand Cap Tables, and Prepare for VC Interviews

*   #### Evaluate companies and deals like a pro
    
    You’ll understand cap tables, startup/growth valuations, and exits
    
*   #### Master financial modeling
    
    You’ll build forecasts and analyze metrics for tech and biotech startups
    
*   #### Complete 9 case studies
    
    You’ll learn the numbers and how to make investment recommendations
    

[Full Details](https://breakingintowallstreet.com/venture-capital-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Venture-Capital-Modeling-Course-Outline.pdf)

But this is incorrect: SaaS companies have significant Accounts Receivable (AR) balances because it takes time to collect the cash, even after the customers have received invoices.

When a SaaS company first issues an invoice to customers, its AR and DR balances both increase by the amount invoiced.

As the company waits for the customer to pay in cash, its AR balance _for that one customer_ stays constant, and when it finally collects the cash, the balance reaches $0.

Meanwhile, the [Deferred Revenue](https://breakingintowallstreet.com/kb/accounting/deferred-revenue/)
 balance decreases each month as revenue for the product or service is recognized.

To explore these concepts in SaaS accounting, this written tutorial and video will walk you through revenue recognition and cash collection.

Here’s the Excel file and slide presentation:

[SaaS Accounting – Simple Model (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/SaaS-Accounting.xlsx)

[SaaS Accounting – Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/SaaS-Accounting-Slides.pdf)

### **Video Table of Contents:**

**0:00:** Introduction

**1:26:** Part 1: Bookings vs. Billings vs. Revenue

**2:22:** Part 2: Simple Excel Schedule

**5:11:** Part 3: Accounts Receivable and Deferred Revenue

**9:05:** Part 4: 3-Statement Model Example

**11:05:** Recap and Summary

**SaaS Accounting, Part 1: Bookings vs. Billings vs. Revenue**
--------------------------------------------------------------

**Bookings** represent the total contract value.

So, if a customer signs a 3-year contract worth $300, the Bookings for _just this customer_ are $300.

**Billings** are based on when the customer receives the invoice, which could be once per month, once per year, once per 6 months, or any other frequency.

If this same 3-year contract customer gets an invoice once per year, the Billings are $100 per year, and the company collects $100 in cash per year.

**Revenue** is based on the delivery of the product or service, so Monthly Revenue = Billings / Months per Invoice.

In this same example, the Monthly Revenue is $100 / 12 = $8.3, and the Annual Revenue is $100.

**SaaS Accounting, Part 2: Simple Excel Schedule**
--------------------------------------------------

To illustrate these concepts in Excel, we’ll walk through a simple example of a customer contract worth $120 over 12 months with invoices 6 months apart and 3 months required to collect the cash for each invoice.

We show the $120 in **Bookings** if we’re currently in Month 0, when the contract is initially signed, or the start month of the next contract.

We can check for this condition with the MOD function in Excel, which divides two numbers and outputs the remainder, which is 0 if the numbers are evenly divisible:

![SaaS Bookings Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202069%20714'%3E%3C/svg%3E "SaaS Bookings Formula")

**Billings** are based on a similar idea, but now we check the month number against the invoice interval, not the contract dates.

We display the Billings only when the invoices are issued:

![SaaS Billings Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202051%20783'%3E%3C/svg%3E "SaaS Billings Formula")

We multiply the Total Contract Value by (Invoice Interval / Contract Length) because, for example, if the contract is 24 months and the invoices are 6 months apart, we need to divide the Total Contract Value by 4 to get the amount in each invoice.

**Revenue** is based on the product/service delivery, so it is simple: Total Contract Value / Contract Length:

![SaaS Accounting: Revenue Recognition](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202074%20801'%3E%3C/svg%3E "SaaS Accounting: Revenue Recognition")

This gets more complicated if the customer can cancel, upgrade, or change their contract, but it’s fine for this simple example.

**SaaS Accounting, Part 3: Accounts Receivable and Deferred Revenue**
---------------------------------------------------------------------

It always takes companies time to collect cash from customers after they issue an invoice, so Accounts Receivable (AR) increases based on the invoiced amount when the invoice is first issued.

It stays at that level and then reaches $0 when the cash is finally collected.

To track the Accounts Receivable, we need to add a row in the Excel model for “how many months have passed since the most recent billing”:

![Months Since Last Billing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202074%20794'%3E%3C/svg%3E "Months Since Last Billing")

In the AR formula, we first check to see if the # of months since the last billing is less than the # of months required to collect cash from customers.

If it is, it means the AR balance still exists at its initial level because the company hasn’t collected the cash from customers yet.

In this case, we use the OFFSET function to move back the correct number of months to this most recent billing:

![SaaS Accounting: Accounts Receivable Changes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202066%20905'%3E%3C/svg%3E "SaaS Accounting: Accounts Receivable Changes")

**Deferred Revenue** increases by the amount billed at the same time that Accounts Receivable does (when the invoice is first issued).

Then, it decreases each month as revenue is recognized due to the delivery of the product or service.

In this Excel model, therefore, Deferred Revenue equals the difference between _cumulative Billings_ and _cumulative Revenue_:

![SaaS Accounting: Deferred Revenue Changes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202076%20904'%3E%3C/svg%3E "SaaS Accounting: Deferred Revenue Changes")

**SaaS Accounting, Part 4: 3-Statement Model Example**
------------------------------------------------------

Investors strongly prefer companies with the pricing/market power to invoice for ~1 year upfront and collect the cash within 1-2 months.

And if you understand SaaS accounting, you’ll be able to recognize these companies and pick the most promising ones based on their financial statements.

To illustrate the financial statement impact, here’s an example of a company with 1-year contracts worth $1200 each that invoices every 4 months and requires 2 months to collect the cash.

The Income Statement and Balance Sheet are straightforward:

![SaaS Income Statement and Balance Sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202400%201435'%3E%3C/svg%3E "SaaS Income Statement and Balance Sheet")

The [Cash Flow Statement](https://breakingintowallstreet.com/kb/accounting/cash-flow-statement/)
 shows that the the overall cash flow impact is **negative** except for the periods in which the cash collection takes place:

![SaaS Cash Flow Statement: Impact of Revenue Recognition and Cash Collection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201114%20614'%3E%3C/svg%3E "SaaS Cash Flow Statement: Impact of Revenue Recognition and Cash Collection")

[See BIWS Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) SaaS Accounting - Presentation Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/SaaS-Accounting-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) SaaS Accounting - Simple Model (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Startups-VC/SaaS-Accounting.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Venture Capital & Growth Equity Modeling](https://breakingintowallstreet.com/venture-capital-modeling/)

Master cap tables, exit analysis, flow of funds, startup valuation, and growth-stage modeling - and win job offers at venture capital and growth equity firms.

[Learn More](https://breakingintowallstreet.com/venture-capital-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[VC Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/FrakNsSE)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with cap tables, exit analysis, startup valuation, and other VC-related topics. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/FrakNsSE)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&mini=true)
[Email](mailto:?subject=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)

#### Master Cap Tables and Startup Modeling

Learn VC and growth equity financial modeling via 5 short case studies and 4 extended case studies on everything from AI to SaaS to biotech.

[LEARN MORE](https://breakingintowallstreet.com/venture-capital-modeling/)

[](https://x.com/intent/tweet?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[](https://www.linkedin.com/shareArticle?title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&mini=true)
[](mailto:?subject=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[](https://api.whatsapp.com/send?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Copy](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#)
[Email](mailto:?subject=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&t=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[LinkedIn](https://www.linkedin.com/shareArticle?title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/)
[Pinterest](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#)
[Print](https://breakingintowallstreet.com/kb/venture-capital/saas-accounting/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[SMS](sms:?&body=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[X](https://x.com/intent/tweet?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[WhatsApp](https://api.whatsapp.com/send?text=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fventure-capital%2Fsaas-accounting%2F&title=SaaS%20Accounting%3A%20Bookings%2C%20Billings%2C%20Revenue%2C%20Deferred%20Revenue%2C%20and%20Accounts%20Receivable&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand