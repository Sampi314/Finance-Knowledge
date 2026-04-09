# Waterfall Returns Distribution in an LBO Model [Video Tutorial]

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model

---

Waterfall Returns Distribution in an LBO Model (19:18)
======================================================

What is a “Waterfall Returns” Schedule? CONCEPT: In a leveraged buyout or any deal where an investment firm acquires another company, they’ll often own close to 100% of it…

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/#tab-signup)
    

Waterfall Returns Distribution in an LBO Model

What is a “Waterfall Returns” Schedule?
---------------------------------------

**CONCEPT:** In a leveraged buyout or any deal where an investment firm acquires another company, they’ll often own close to 100% of it…

But sometimes management will retain a small portion, or another investor group might retain a certain portion.

Sometimes it ends there – but sometimes, that smaller group gets ADDITIONAL ownership and a higher stake upon exit if the investment performs well.

This is called a “management promote” (if it’s the management team that receives this as an incentive).

**EXAMPLE:**

A new leveraged buyout takes place, and the PE firm structures the deal to heavily incentivize the management team:

For an IRR up to 10%, PE firm gets 95% and management team gets 5% of the proceeds.

Then, for the portion of the IRR between 10% and 15%, the PE firm gets 90% and the management team gets 10%.

For the portion of IRR between 15% and 20%, the PE firm gets 85% and the management team gets 15%.

Then for the IRR above 20%, the PE firm gets 80% and the management team gets 20%.

A PE firm might do this to create a “win win” scenario – yes, it loses some of its IRR by giving up a % to the management team… but if all goes well, the team should outperform and help the PE firm achieve a higher overall IRR.

How Do You Model This Scenario?
-------------------------------

1) Make assumptions for the initial investment and proceeds upon exit, plus the ownership percentages.

2) Make assumptions for how the proceeds split changes at different IRR levels.

3) For each “tier” of IRR, take the initial investment and calculate the amount of net proceeds upon exit that would correspond to that IRR.

Example: $1,000 initial investment, and 10% IRR tier – multiply by (1 + 10%), then multiply that number by (1 + 10%), and so on until the exit year.

4) Determine the split of proceeds within that tier.

If the actual proceeds are $1,500, for example, and $1,611 would correspond to a 10% IRR, you’re done – just split the $1,500 between the PE firm and management team in a 95% / 5% split.

But if it goes beyond that $1,611, you just split up the $1,611 according to those numbers and then save the rest for the next tier.

5) Determine the proceeds to distribute in the next tiers.

For $3,000, for example, you’d distribute $1,611 and save ($3,000 – $1,611) for the next tiers.

If you’re at the 10% level and you get something below $1,611, you’d set the “proceeds for the next tiers” number to $0 (use a MAX function for this).

6) Keep doing this for each tier of IRRs until the end.

The formulas get trickier as you move up because you need to use MIN and MAX to ensure that you don’t get negative or nonsensical values.

In Level 2, for example, the “Amount to Distribute and Split” is:

\=MIN(Net Proceeds That Correspond to 15% IRR in Year 5 minus Net Proceeds That Correspond to 10% IRR in Year 5, MAX(Total Net Proceeds minus Net Proceeds That Correspond to 10% IRR in Year 5, 0))

So you’re taking the lesser of the proceeds between 10% and 15% IRRs, or the total remaining amount that can be distributed AFTER the Level 1 distributions.

And that same type of logic continues as you move down, until the last tier.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Waterfall Distribution in a Leveraged Buyout Model (Or Any Other Investment) - Before (XLSX)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/109-03-Simplified-Waterfall-Distribution-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Waterfall Distribution in a Leveraged Buyout Model (Or Any Other Investment) - After (XLSX)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/109-03-Simplified-Waterfall-Distribution-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&mini=true)
[Email](mailto:?subject=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[](https://www.linkedin.com/shareArticle?title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&mini=true)
[](mailto:?subject=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[](https://api.whatsapp.com/send?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/#)
[Email](mailto:?subject=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&t=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/19075457/kb-waterfall-distribution-lbo-model.jpg&description=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/waterfall-distribution-lbo-model/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[SMS](sms:?&body=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[X](https://x.com/intent/tweet?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fwaterfall-distribution-lbo-model%2F&title=Waterfall%20Returns%20Distribution%20in%20an%20LBO%20Model%20%2819%3A18%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/19075457/kb-waterfall-distribution-lbo-model.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand