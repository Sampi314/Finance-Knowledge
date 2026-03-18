# How To Quickly Calculate IRR in LBO Models [Video Tutorial]

**Source:** https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually

---

Quick IRR Calculation in LBO Models (20:02)
===========================================

In this tutorial, you’ll learn tricks to approximate IRR quickly in leveraged buyouts, how to think about IRR intuitively, and how to apply these tricks to both simple and more complex private equity case studies.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#tab-signup)
    

Quick IRR Calculation in LBO Models

Tips for Quickly Approximating the IRR
--------------------------------------

Yes, you can quickly approximate IRR in a leveraged buyout scenario, but \*only\* if there’s a simple upfront investment and simple exit, and nothing else in between, such as dividends, [dividend recaps](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/dividend-recap/)
, asset sales, or an IPO exit where the PE firm sells its stake gradually over time.

The internal rate of return, or IRR, represents the “effective compounded interest rate” of an investment.

In other words, if you invest $100 today and get back $150 in 5 years, what interest rate on your initial $100, compounded each year, would let you earn that $150 by the end?

To approximate the IRR, you start by calculating the money-on-money multiple and the holding period.

If you double your money in 1 year, that’s a 100% IRR. Invest $100 and get back $200 in 1 year, and you’ve just earned 100% of what you put in.

If you double your money in 2 years, you need to earn \*roughly\* 50% per year to get there.

Due to compounding, it’s actually less than 50%; it’s closer to 40% if you calculate it in Excel.

So the rule of thumb is that, for “double your money” scenarios, you take 100%, divide by the # of years, and then estimate the IRR as about 75-80% of that value.

For example, if you double your money in 3 years, 100% / 3 = 33%.  
75% of 33% is about 25%, which is the approximate IRR in this case.

The most important approximations are as follows:

Double Your Money in 1 Year = 100% IRR  
Double Your Money in 2 Years = ~40% IRR  
Double Your Money in 3 Years = ~25% IRR  
Double Your Money in 4 Years = ~20% IRR  
Double Your Money in 5 Years = ~15% IRR

Triple Your Money in 3 Years = ~45% IRR  
Triple Your Money in 5 Years = ~25% IRR

How to Apply These Rules to Case Studies and Modeling Tests
-----------------------------------------------------------

You can use these rules of thumb to determine what your investment recommendation might say, and also to check your work before you complete a time-consuming exercise.

For example, let’s say that in one case study, you buy a $50 million EBITDA company for 7x EBITDA, using 4.5x Debt/EBITDA.

EBITDA grows by roughly 10% per year over 3 years.

Approximately $90 million of Debt amortizes over those 3 years as well.

The exit multiple is 8x EBITDA.

You can approximate the IRR in this scenario using the following logic:

$50 million EBITDA \* 7x multiple = $350 million purchase price.

The equity contribution is 7.0x minus 4.5x, or 2.5x EBITDA, which is $125 million here.

If EBITDA grows by 10% per year over 3 years, it reaches approximately $70 million by Year 3.

$70 million \* 8 = $560 million Exit Enterprise Value.

Since the initial leverage ratio was 4.5x Debt/EBITDA, the initial Debt was 4.5 \* $50 million = $225 million.

$90 million of that Debt amortized over time, so there’s $225 – $90 = $135 million at the end.

So the Equity Proceeds Upon Exit are $560 million – $135 million = $425 million.

$425 million / $125 million = just over a 3x multiple, or 3.4x more precisely.

Since the PE firm earned back over 3x its equity in 3 years, you could approximate the IRR as “just over 45%” here.

This is an extremely high IRR, and well above the usual target of 20%, so you would lean toward an “Invest” recommendation in this case.

In our real Excel model, the IRR is only 43% because of the transaction fees, the fact that our Year 3 EBITDA estimate was off, and the fact that the Debt had [PIK Interest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/pik-interest/)
, which increased the Debt principal over time.

Still, this is very good for a 60-second approximation.

[Sign Up for Private Equity Modeling](https://breakingintowallstreet.com/private-equity-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Can You Quickly Approximate the Internal Rate of Return (IRR) in a Leveraged Buyout? (PDF)](https://youtube-breakingintowallstreet-com.s3.amazonaws.com/109-12-Quick-IRR-Calculation-Slides.pdf)
    

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

[X](https://x.com/intent/tweet?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&mini=true)
[Email](mailto:?subject=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)

#### Master LBO Modeling & PE Cases

Complete 6 short models and 6 real-life case studies and master the key skills for PE interviews, from paper LBOs to detailed models.

[LEARN MORE](https://breakingintowallstreet.com/private-equity-modeling/)

[](https://x.com/intent/tweet?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[](https://www.linkedin.com/shareArticle?title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&mini=true)
[](mailto:?subject=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[](https://api.whatsapp.com/send?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Copy](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#)
[Email](mailto:?subject=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&t=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
[Pinterest](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#)
[Print](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[SMS](sms:?&body=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[X](https://x.com/intent/tweet?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fleveraged-buyouts-and-lbo-models%2Fhow-to-calculate-irr-manually%2F&title=Quick%20IRR%20Calculation%20in%20LBO%20Models%20%2820%3A02%29&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand