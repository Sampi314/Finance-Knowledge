# Real Financial Modeling is a Waste of Your Time

**Source:** https://pivotal180.com/real-financial-modeling-is-a-waste-of-your-time-2

---

[Skip to content](https://pivotal180.com/real-financial-modeling-is-a-waste-of-your-time-2/#fl-main-content)

Real financial modeling is a waste of your time
===============================================

By Michael | October 10, 2019

**[New students to project finance modeling](https://pivotal180.com/available-project-finance-courses/)
** commonly approach financial models with the same question: should I build my model in nominal or real terms?

You may hope the $5 coffee you are buying now (at midnight before getting back to your financial model) will still cost $5 in 3 years, meaning it will have the same ‘purchasing power’. Maybe you are even more hopeful, perhaps it will cost even less?

**Real modeling explained: keeping numbers constant**
-----------------------------------------------------

Modelling assuming your purchasing power will remain the same is called ‘real modeling’. Let’s think about rent as an example, shown below.

![Financial Modeling ](https://pivotal180.com/wp-content/uploads/2019/10/michael-waste-1.png)  
In this example, we are paying $1,000 in year 1 for rent. Assuming purchasing power stays the same, our $1,000 will still be enough to pay for the rent in year 10. There is something reassuring with this calculation, just seeing the rent amount not change over time.

**_While real cash flows are cash flows in the future but at today’s equivalent value, they are not actual cashflows_**

We like simplicity at Pivotal180, however there are major issues with real modeling in project finance, which I will come to shortly.

**Nominal modeling: inflating** **numbers to the actual cash required in the future**
-------------------------------------------------------------------------------------

The problem is, we know that rent seems to get more expensive every year. As a renter, I wish it didn’t, but due to inflation the cost of rent to me increases every year. Assuming inflation is 5% p.a., we can see the amount rent would cost me in the future below.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20697%2065'%3E%3C/svg%3E)

This means the actual amount of cash I need to outlay in 1, 2, or 3 years will be more than $1,000. This higher amount of cash needed in year 2 ($1,050) has the same worth to the property owner as $1,000 does now. Another way of saying that, is that to maintain the same purchasing power in year 2, I will need to have $1,050 instead of $1,000.

Keep in mind that inflation is compounding; if inflation for rent is 5% per year, the rent will have to increase by 5% compared to the **_previous_** year rather than 5% x $1,000 ($50) every year.

**_Nominal Cash Flow (# Year) = (Real Cash Flow) \* (1 + Inflation) Time Period_**

In Year 3, we need to solve for actual cash flows, based on our 5% inflation rate, and our real cash flows of $1,000.

**_Nominal Cash Flow (Year 3) = ($1,000) \* (1 + 5%) 3 = $1,158_**

This equation works for **_constant_** inflation rates – for non-contiguous inflation, inflation has to be applied to the **_preceding_** year. More information on inflation is available through our courses.

 

**_Nominal cashflows are the actual cashflows you expect to pay or receive in the future_**

Isn’t that easier to imagine! We love simplicity, but there are other important reasons why we model in nominal terms

**Model in nominal terms to keep your terms straight**
------------------------------------------------------

### Project finance contracts are written this way

Contracts in project finance typically provide contract values in real terms, but with defined escalation to be applied every year to that contract price (excluding the construction contract). The contracts are informing you that you will pay cash based on escalation in the future.

### Debt repayments are already nominal

We need to model operating cash flows, debt repayments and then equity cash flows.

When the bank offers you a term loan, the Facility Agreement specifies the actual amount of cash to be repaid in each future period. It is completely non-sensical for a lender to tell you to repay in the value of the future repayments in today’s $s…. If you modeled in real terms you would have to back-calculate loan repayments into silly numbers… What the?

### Investors ask for nominal returns

As a fund or investor, your ultimate investors are often seeking, say, a 2.5x multiple on the cash they receive from the investment vs what they commit to the investment in year 0. This is nominal as it is an actual cash expectation.

### Depreciation and Tax Losses

Governments do not tax on real earnings; they tax on actual earnings. Depreciation of assets and net operating losses are nominal, and represent the actual losses that can be used. 

Let’s say that in Year 1, after receiving our rent, paying for the upkeep of the building, and accounting for depreciation of the building, our net operating loss for the first year is $1,000.

Despite having to wait a year to realize the tax benefits, the government does not inflate the losses – they are already in nominal (actual cash) terms.

If you wanted here to consider tax losses on a real basis, you would need to deflate the NOLs in year 2, which are not used by anyone else! To learn more about net operating losses and tax losses, refer to our course material here.

### LIBOR is provided in nominal terms

LIBOR is the benchmark rate for most loans and is provided in nominal terms. To model debt interest rates correctly in a model with real cash flows, you would have to deflate LIBOR to present-day dollars! For those new to finance, refer to our post on LIBOR to see more insights on the history and future of the benchmark.

### Foreign Exchange Rates are also in nominal terms

Inflation assumptions are already built into foreign exchange contracts. To convert foreign currencies into a local currency, you would have to solve for the uninflated values with the equivalent power purchasing method. This step is beyond what anyone needs to understand to build an effective model in project finance!

### Fuel and Commodity Prices

Most companies rely on fuel and commodity price curves published by research firms to develop their models. Whilst you need to take your own view of the underlying inflation rates within the price curves regardless of if you are modeling in nominal or real, you would need to modify the price curves for real cash flow modeling.

**Real modeling is mostly a waste of time, but there are some benefits**
------------------------------------------------------------------------

With all of the complications and downsides we’ve identified in attempting to model in real terms, why would anyone create a project finance model in real terms?

1.  It’s easier to comprehend for new modelers as inflation calculations can be tricky
2.  Corporate policy for valuations (treasury will apply their own inflation assumptions)
3.  For normalization
    1.  To review one project versus another without the effect of escalation (especially if projects are in different countries).
    2.  Understanding how EBTIDA margins change over time, based on items specific to the project (i.e. excluding inflation)

**Be careful modeling in real terms in project finance models**
---------------------------------------------------------------

Avoid the complications of deflating your taxes, interest rates, debt, foreign exchange, return targets. Working in real terms adds additional calculations and complications to a relatively straight forward series of cashflows. Essentially, it’s crazy to work in real cash flows below operating cashflows. Instead, inflate your revenues and costs based on the contracted rates or assumed price escalation, and calculate the nominal rate of return.

### Can you calculate the real returns?

Yes, but it is more complicated than first thought. If you are asked the return in real terms, you would have to create a weighted average inflation for your portfolio; the inverse of what we reviewed in this article. Even then, the calculation is exceedingly easy to do incorrectly. Save yourself from mathematical errors, and approximate your real returns using the Fisher Equation:

_**Nominal Rate of Return – Inflation = Real Rate of Return**_

This shorthand, back-of-the-envelope calculation is approximately accurate with low rates of inflation (less so in some developing countries with higher inflation), and could be accurate enough for questions on real returns.

For more **[insights and resources on financial modeling](https://pivotal180.com/)
**, visit us at pivotal180.com.

_![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20182%20182'%3E%3C/svg%3E)_

Michael Woods is a jack-of-all-trades renewable energy specialist with Pivotal180, providing financial modeling insights to those new to the industry. He is also a Master of Public Administration in Energy Policy and Finance candidate at Columbia University, and works with GDS Associates, Inc., an energy engineering consulting firm.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Freal-financial-modeling-is-a-waste-of-your-time-2%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Freal-financial-modeling-is-a-waste-of-your-time-2%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Freal-financial-modeling-is-a-waste-of-your-time-2%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#5b6439343f2266332f2f2b287e681a7e691d7e691d2b322d342f3a376a636b753834367e691d293e3a37763d32353a3538323a377636343f3e3732353c763228763a762c3a282f3e76343d7622342e29762f32363e76697e691d)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)

### Michael

[](https://pivotal180.com/real-financial-modeling-is-a-waste-of-your-time-2/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/real-financial-modeling-is-a-waste-of-your-time-2/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA