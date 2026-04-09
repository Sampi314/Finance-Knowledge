# Cap Rate in Real Estate: Excel Examples and Tutorial

**Source:** https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate

---

The Cap Rate in Real Estate: Formula, Examples, and Uses in Financial Models
============================================================================

In real estate, the Cap Rate (Capitalization Rate) of a property equals its projected, stabilized Net Operating Income divided by its current price or estimated value; the Cap Rate is the reciprocal of the EBITDA multiple commonly used to value companies.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#tab-signup)
    

The Cap Rate in Real Estate: Formula, Examples, and Uses in Financial Models

> **Cap Rate Definition:** In real estate, the **Cap Rate** (Capitalization Rate) of a property equals its projected, stabilized Net Operating Income divided by its current price or estimated value; the Cap Rate is the reciprocal of the EBITDA multiple commonly used to value companies.

Net Operating Income (NOI), like [EBITDA](https://breakingintowallstreet.com/kb/accounting/ebitda/)
, measures a property’s cash flow from operations on a capital structure-neutral basis before the “capital costs” (e.g., capital expenditures, tenant improvements, and leasing commissions).

Net Operating Income equals the property’s revenue from rental income, expense reimbursements, and other sources minus its operating expenses and property taxes.

Here’s an example calculation from a [simple pro-forma model](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-pro-forma-model/)
:

![Cap Rate Example](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201748%201113'%3E%3C/svg%3E "Cap Rate Example")

You should ideally use the projected, stabilized NOI in the Cap Rate calculation because you want to capture what investors pay for the property’s _future earnings potential_, not its historical performance.

The “Property Price” could be the asking price, the actual price paid for the property, or the market’s estimate of the property’s current value.

Sometimes you _calculate_ the Cap Rate, and sometimes you _select_ the Cap Rate to estimate the property’s price if you’re considering an acquisition or sale.

**You use Cap Rates in real estate because many investors view it more like a fixed-income investment (e.g., a corporate bond) than an equity investment (a stock).**

According to that analogy, Cap Rates are like [bond yields](https://breakingintowallstreet.com/kb/debt-equity/bond-yield/)
 and most closely resemble the “[current yield](https://breakingintowallstreet.com/kb/debt-equity/current-yield/)
” on a bond.

### **Files & Resources:**

*   [Simple Pro-Forma Real Estate Model with Cap Rate Calculations (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Real-Estate/Simple-Real-Estate-Pro-Forma.xlsx)
    
*   [The Cap Rate in Real Estate – Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Real-Estate/Cap-Rate-Slides.pdf)
    

### **Video Table of Contents:**

*   **0:00:** Introduction
*   **0:37:** The Short Version
*   **4:44:** Part 1: What Affects Cap Rates and How to Find Them
*   **6:58:** Part 2: Cap Rate vs. IRR vs. “Cash Yield”
*   **9:19:** Part 3: Cap Rates in Real Estate Models
*   **11:17:** Part 4: Cap Rates in REIT Models
*   **12:12:** Part 5: Cap Rates Variations, Controversies, and Trickery
*   **15:16:** Recap and Summary

**Example Cap Rate Calculation**
--------------------------------

For example, let’s say that a property generated **$4 million in NOI last year** and is expected to generate **$5 million next year**, based on the rental contracts, tenants, and direct operating expenses, such as maintenance, utilities, insurance, management fees, and property taxes.

Additionally, you expect to spend an average of $500K per year on “capital costs,” such as equipment replacements, tenant improvements, and leasing commissions to win new tenants and get the existing ones to renew their leases.

Since you’re planning to use **Debt** for some of the purchase price, there will be $2 million in interest expense and $1 million in principal repayments in the first year.

The “asking price” for this property is $100 million.

Therefore, the Cap Rate is $5 million / $100 million = 5%.

The previous year’s NOI, the $500K in capital costs, and the Debt Service are irrelevant – **all that matters is the property’s “core business performance” in the next year.**

We could also “work backwards” to calculate an appropriate asking price for the property, given its NOI and a range of Cap Rates.

For example, if similar properties in the region have sold for Cap Rates between 4% and 6%, this property should be worth between $5 / 6% = $83 million and $5 / 4% = $125 million.

**What Affects a Property’s Cap Rate?**
---------------------------------------

A Cap Rate reflects the property’s location, desirability, growth potential, and risk.

For example, a luxury apartment building in the center of Manhattan might sell for a 4% Cap Rate (equivalent to a 25x multiple), while a run-down, second-tier apartment building in The Middle of Nowhere, Iowa, might sell for a 10% Cap Rate (equivalent to a 10x multiple).

[The major real estate brokerage firms publish Cap Rate data for different cities and regions](https://www.cbre.com/insights/reports/us-cap-rate-survey-h1-2024)
, and you need to review this data to make the appropriate assumptions.

If an office building down the street recently sold for a 6% Cap Rate, that doesn’t necessarily tell you anything about _the office building you are currently valuing_ because it could be quite different:

*   Is it the same “class” (e.g., Class A, Class B, etc.) property with similar amenities and conditions?
*   How similar are the properties’ locations? The one that’s in a wealthy suburb will be a lot more desirable than the one in an area with a high crime rate.
*   What is the occupancy rate of each building? Are the tenants high quality (e.g., blue-chip, Fortune 500 companies), or are they riskier (e.g., small businesses or startups)?
*   How stable are the cash flows? Is there a substantial chance that many of the leases will expire in 2-3 years, or are the tenants on longer-term leases with staggered lease expirations?

As with [valuation multiples](https://breakingintowallstreet.com/kb/valuation/valuation-multiples/)
 for [comparable public companies](https://breakingintowallstreet.com/kb/valuation/comparable-company-analysis-cca/)
, Cap Rates for properties are meaningful only if they’re based on properties that are _truly comparable_.

**The Cap Rate vs. the IRR and “Cash Yield”**
---------------------------------------------

We mentioned above that Cap Rates are like the current yield on a bond in some ways.

For example, both give you an idea of what you can earn if you buy an asset at its current market price and hold it for a year.

However, they’re not quite _the same_ because the **current yield** on a bond gives you a much better idea of the cash earnings over a year.

By contrast, the Cap Rate for properties tends to **overstate** the potential earnings because it excludes capital costs (CapEx, TIs, and LCs) and financing costs, such as the interest expense and Debt principal repayments.

The **Cash Yield** or **Cash Flow to Equity** metric in real estate deducts these cash outflows and is much closer to what you might earn in cash after buying a property with Debt and Equity:

![Cash Yield in Real Estate](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201929%20972'%3E%3C/svg%3E "Cash Yield in Real Estate")

To move from the Cash Flow to Equity to the Cash Yield %, divide the Cash Flow to Equity by the Equity Invested in the property acquisition.

The Cap Rate is also different from another common returns-based metric, [the internal rate of return or IRR](https://breakingintowallstreet.com/kb/leveraged-buyouts-and-lbo-models/how-to-calculate-irr-manually/)
.

The IRR measures the **annualized return** you’d earn by purchasing an asset at one price, receiving cash flows from it, and then selling it in the future.

By contrast, the Cap Rate measures **only the potential earnings in one year**, and it doesn’t factor in changes in the property’s value between purchase and exit.

Also, as stated above, it usually overstates the cash earnings potential by excluding certain cash outflows.

The Cap Rate is a _key input_ to the IRR calculation because it determines the entry and exit values, but it is **not the same** as IRR.

It’s different because it just corresponds to the NOI in one year, and it represents _all investors_ rather than just the equity investors and cash flows to equity.

Here’s an example:

![Cap Rate and IRR Calculations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202321%20911'%3E%3C/svg%3E "Cap Rate and IRR Calculations")

**The Cap Rate in Real Estate Financial Models**
------------------------------------------------

The Cap Rate is a central part of nearly all [real estate financial models](https://mergersandinquisitions.com/real-estate-financial-modeling/)
.

Whether you’re modeling a new development, an acquisition of a stabilized property, a renovation, or a “turnaround” of a distressed property, the Cap Rate plays a key role.

The only type of real estate model in which the Cap Rate is _not_ important is one in which individual units are sold to people, as in the case of pre-sold condominium developments.

In these models, units’ selling prices based on $ per square foot or $ per square meter figures are the most important metrics **because the entire property is not being sold – only smaller portions of it**.

In all other property models, you use Cap Rates to:

*   **Determine** **the Purchase Price** – For a stabilized property, you can estimate the appropriate purchase price based on its forward NOI divided by the range of Cap Rates from similar, recent property acquisitions in the region.
*   **Determine the Debt to Use in a Refinancing** – When a [commercial real estate loan refinancing](https://breakingintowallstreet.com/kb/real-estate-modeling/commercial-real-estate-loan-refinancing/)
     takes place, the allowable Debt is based on a [“Loan to Value” or LTV Ratio](https://breakingintowallstreet.com/kb/real-estate-modeling/loan-to-value-ltv/)
    , such as 70% of the property’s value. The property’s value is based on the Cap Rate and the forward NOI at this time.
*   **Determine the Exit Price** – When you sell the property at the end of the holding period, you project the NOI one year into the future and divide it by the Exit Cap Rate to estimate the exit price. The proceeds to the equity investors equal this exit price minus the remaining Debt.
*   **Value a Property** – For example, if you build a [DCF model](https://mergersandinquisitions.com/dcf-model/)
     for a property, you can still calculate its [Unlevered Free Cash Flow](https://breakingintowallstreet.com/kb/discounted-cash-flow-analysis-dcf/unlevered-free-cash-flow/)
     each year (it’s close to NOI minus Capital Costs), but you’ll use a Cap Rate to estimate its [Terminal Value](https://breakingintowallstreet.com/how-to-calculate-terminal-value/)
     based on the NOI in the first year of the Terminal Period.

The **trickiest part** in all of this is determining whether the Exit/Terminal Cap Rate should _increase or decrease_ vs. the Purchase Cap Rate (also known as the “Going-In Cap Rate”).

Remember that Cap Rates are the opposite of valuation multiples, so a _higher Cap Rate_ corresponds to a _lower valuation_, while a _lower Cap Rate_ represents a _higher valuation_.

The general guidelines are as follows:

*   **Stabilized Properties** – If the property largely stays the same, you should assume a **higher Cap Rate upon exit** because it will be older and less appealing by then. You might look at the Cap Rate difference for older vs. newer properties in the area to get ideas for the differential.
*   **Renovated Properties** – If the property improves _significantly_, you could plausibly assume a lower Cap Rate upon exit, meaning a higher valuation. But the exact numbers depend heavily on the scope of the improvements and the comparison to peer properties in the area.
*   **Newly Developed Properties** – There is no “Purchase Cap Rate” to use as a reference, but the Exit Cap Rate should be based on properties of a similar age with similar amenities in the region.

![Real Estate Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Learn Property Modeling from A to Z with the **BIWS Real Estate Modeling Course**

*   #### Evaluate property developments and acquisitions
    
    You’ll assess the risks and rewards and make investment recommendations
    
*   #### Master financial modeling
    
    You’ll build office, retail, hotel, industrial, multifamily, and pre-sold condo models
    
*   #### Complete 11 case studies
    
    Build 6 shorter “crash course” models and 5 detailed “on the job” ones
    

[Full Details](https://breakingintowallstreet.com/real-estate-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Real-Estate-Modeling-Course-Outline.pdf)

**The Cap Rate in REIT Models**
-------------------------------

The **Cap Rate** is also important in models for [real estate investment trusts (REITs)](https://breakingintowallstreet.com/kb/reit-modeling/)
 because [REIT financial models](https://breakingintowallstreet.com/reit-modeling/)
 assume these entities constantly buy, sell, and develop properties.

You won’t know the exact Cap Rate for every single property in their portfolios, but you can make assumptions for the “average” Cap Rate in each segment, such as Acquisitions, Developments, and Redevelopments:

![The Cap Rate in REIT Financial Models](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202193%20799'%3E%3C/svg%3E "The Cap Rate in REIT Financial Models")

You can also break it down by geography and assign an “average” Cap Rate to each segment.

For example, if the Paris Cap Rate is 4%, while the Madrid Cap Rate is 5%, and the company plans to spend €500 million in each city, the additional Paris NOI should equal €500 million \* 4% = €20 million, while the Madrid NOI should equal €500 million \* 5% = €25 million.

When you’re aggregating the REIT’s financial statements, you can use these numbers to estimate the revenue and property-level expenses on the Income Statement.

**Variations of the Cap Rate in Other Regions**
-----------------------------------------------

In some European countries, the Cap Rate is called the “Yield,” as it represents the Net Operating Income that an investment in a property will “yield,” like bond yields.

But, as discussed above, bond yields and property NOI are quite different when you examine the details.

In some regions, the “Gross Yield” may be used instead of the “Net Yield,” especially with office, retail, and industrial properties that tend to use Triple Net (NNN) Leases.

In these NNN leases, most of the expenses (maintenance, insurance, property taxes, etc.) “pass through” to the tenants, who are responsible for their share; as a result, the Gross and Net Rental Income are quite close.

If a region uses the Gross Yield to value properties, it is based on the **Gross Rental Income** divided by the property’s value or asking price.

If a region uses the Net Yield, it is based on the **Net Rental Income** divided by the property’s value or asking price:

![Net Yields Rather Than Cap Rates in Paris](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202002%201088'%3E%3C/svg%3E "Net Yields Rather Than Cap Rates in Paris")

The Net Rental Income is always lower and deducts the expenses that the property owner(s) must pay.

You can use either the Net Yield or the Gross Yield, but whichever one you choose, you must be **consistent** with the calculations, or you’ll end up with distorted property valuations.

**What Makes the Cap Rate Calculation Trickier Than It Seems?**
---------------------------------------------------------------

Besides the “Gross vs. Net” issue above and the inconsistencies between certain cities (for example), the biggest issues with the Cap Rate calculation are:

1.  **Inconsistent Line Items and Calculations** – The main point of contention here is the treatment of **Reserves**, or funds the property sets aside to pay for upcoming capital costs, such as equipment upgrades, tenant improvements, and leasing commissions.
2.  **Lack of Data** – It’s easy to find Cap Rates for recent apartment or office building sales in Manhattan, but it’s far more difficult to find solid data for Class B retail properties in rural parts of Iowa.

With the first point, **consistency** is the most important principle.

Some people argue that “capital cost components” should be deducted when calculating Net Operating Income and that, therefore, the Cap Rate should reflect these cash outflows.

Others argue that the Cap Rate and NOI should completely exclude all capital costs, including Reserve allocations for upcoming CapEx.

You could make a case for either treatment, but in financial models, you must apply one of them consistently to all the numbers.

With the second point, if you cannot find solid data on certain properties in a region, you could use **alternative valuation methodologies**.

For example, the Replacement Cost method might work in some cases; with this one, you estimate the cost of developing the same property today at current land, material, labor, and permitting costs.

Or you could build a simple DCF and assume a long-term cash flow growth rate rather than calculating the Terminal Value using a Terminal Cap Rate.

The **bottom line** is that Cap Rates are universal in real estate financial modeling and deal analysis, but they also have flaws and drawbacks and must be used carefully and consistently.

[Sign up to BIWS Real Estate Modeling](https://breakingintowallstreet.com/real-estate-modeling)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) The Cap Rate in Real Estate - Slides (PDF)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Real-Estate/Cap-Rate-Slides.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Simple Pro-Forma Real Estate Model with Cap Rate Calculations (XL)](https://youtube-breakingintowallstreet-com.s3.us-east-1.amazonaws.com/Real-Estate/Simple-Real-Estate-Pro-Forma.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Real Estate Modeling](https://breakingintowallstreet.com/real-estate-modeling/)

Master financial modeling for real estate developments and acquisitions with 6 short case studies and 5 in-depth ones based on real properties from around the world.

[Learn More](https://breakingintowallstreet.com/real-estate-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Real Estate Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/F33HSJpg/)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with real estate developments and acquisitions. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/F33HSJpg/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&mini=true)
[Email](mailto:?subject=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)

#### Master Real Estate Modeling

Master financial modeling for real estate development and private equity with 11 global case studies based on property acquisitions, developments, and renovations.

[LEARN MORE](https://breakingintowallstreet.com/real-estate-modeling/)

[](https://x.com/intent/tweet?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[](https://www.linkedin.com/shareArticle?title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&mini=true)
[](mailto:?subject=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[](https://api.whatsapp.com/send?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Copy](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#)
[Email](mailto:?subject=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&t=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[LinkedIn](https://www.linkedin.com/shareArticle?title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/)
[Pinterest](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#)
[Print](https://breakingintowallstreet.com/kb/real-estate-modeling/cap-rate/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[SMS](sms:?&body=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[X](https://x.com/intent/tweet?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[WhatsApp](https://api.whatsapp.com/send?text=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Fcap-rate%2F&title=The%20Cap%20Rate%20in%20Real%20Estate%3A%20Formula%2C%20Examples%2C%20and%20Uses%20in%20Financial%20Models&image=&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand