# NAV Model (Oil & Gas): Production Decline Curve [Video Tutorial]

**Source:** https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas

---

NAV Model (Oil & Gas): Production Decline Curve (24:27)
=======================================================

When you’re valuing an E&P (Exploration & Production) company, the Net Asset Value (NAV) Model is the key methodology.

 Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/#tab-signup)
    

UNLIKE in a [DCF model](https://www.mergersandinquisitions.com/dcf-model/)
, where cash flow growth is assumed into infinity, in a NAV model, you assume the company’s cash flows go to $0 eventually as it completely produces all of its reserves and has nothing left.

A granular NAV model is complex, but it comes down to a 2-step process:

**Step 1:** Model the company’s existing production from wells it already has… and assume a decline rate for the annual production each year, also assuming commodity prices to determine revenue, and linking operating expenses to production and calculating cash flow like that.

**Step 2:** Assume the company drills new wells in its PUD (Proved Undeveloped), PROB (Probable), and POSS (Possible) reserves.

The second step involves dozens of sub-steps and assumptions, but here we’re just going to focus on ONE small part of this process: estimating the decline rate of a new well the company drills.

It starts off at a very high production rate, but then declines quickly within even the first year of its useful life – and we need to estimate the decline rates each year to build the rest of the model.

You COULD do lots of complicated math, try fitting hyperbolic or exponential functions, run a regression analysis, etc., but we suggest a much simpler approach here: if the company doesn’t disclose data on its decline rates for individual wells, find data from another company operating in the same region and fit it to your company’s “average” wells.

How to Do That:
---------------

**Step 1:** Find the company’s key data, such as the EUR per well and IP rate per well in the region you’re looking at.

**Step 2:** Now, see if the company discloses data on its own decline rates… if so, you’re set!

If not, or if it’s not enough, find another company operating in the region that discloses more data (EQT here), and go to that company’s investor presentations to get the numbers.

**Step 3:** In the first year, assume that production is some % of 365 \* IP Rate per Well… because there is a huge drop-off in daily production from Month 1 to Month 12 in that first year.

EQT’s data shows 45%; we assume 60% here since UPL has a slightly flatter decline curve.

**Step 4:** Copy and paste the other company’s decline rates into each year of your decline curve.

**Step 5:** Enter the correct formula for calculating annual production each year AFTER the initial year… here:

\=MIN(AU129\*(1+AT130),$AT$126-SUM(AU$129:AU129))

Want to take either Last Year Production \* (1 + Decline Rate) (the first part), or the total remaining reserves in this well (the second part).

**Step 6:** Set up Subtotal / Remainder / Total math and ensure that everything is produced.

**Step 7:** “Fit the data” using Goal Seek and the Factor – multiply each decline rate by a certain factor and use Goal Seek (Alt + A + W + G) to solve for the factor that makes the Subtotal equal to the EUR.

**Step 8:** Build in support for a different EUR by scaling the production up or down in the “Total” column.

**Step 9:** Allocate the production to oil vs. gas. vs. NGLs.

**Step 10:** Complete the Subtotal / Remainder / Total math at the bottom.

What Next?
----------

Next, we’d complete this process for all the wells the company drills in every region, estimate revenue, expenses, and cash flow for each one, and then aggregate the discounted cash flow values in every region across all reserve types…

Which brings us closer to the implied NAV per share, which is what the NAV model is really all about.

[Premium Course Signup](https://breakingintowallstreet.com/oil-gas-modeling/)

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

[Oil & Gas Modeling](https://breakingintowallstreet.com/oil-gas-modeling/)

Master financial modeling and valuation for the Upstream, Midstream, Downstream, and Oilfield Services verticals via U.S., European, and Asian case studies.

[Learn More](https://breakingintowallstreet.com/oil-gas-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&mini=true)
[Email](mailto:?subject=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)

#### Master Oil & Gas Modeling

Learn financial modeling and valuation for the Upstream, Midstream, and Downstream verticals via U.S. and European case studies.

[LEARN MORE](https://breakingintowallstreet.com/oil-gas-modeling/)

[](https://x.com/intent/tweet?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[](https://www.linkedin.com/shareArticle?title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&mini=true)
[](mailto:?subject=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[](https://api.whatsapp.com/send?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Copy](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/#)
[Email](mailto:?subject=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&t=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/12223133/86.jpg&description=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[Print](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model-oil-and-gas/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[SMS](sms:?&body=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[X](https://x.com/intent/tweet?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[WhatsApp](https://api.whatsapp.com/send?text=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model-oil-and-gas%2F&title=NAV%20Model%20%28Oil%20%26%20Gas%29%3A%20Production%20Decline%20Curve%20%2824%3A27%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2020/03/12223133/86.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand