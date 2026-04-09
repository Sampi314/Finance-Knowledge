# Equity Return Metrics in a Project Finance Structure: Equity IRR – Finexmod

**Source:** https://www.finexmod.com/equityirr

---

[Skip to content](https://www.finexmod.com/equityirr#content)

Equity Return Metrics in a Project Finance Structure: Equity IRR

In my previous blog post, I talked about different forms of equity contribution and the role of the financial model to optimize the equity structure. In this episode, I want to show you different equity return measurements in a project finance transaction and basically the below metrics:

*   **Equity IRR**
*   Project IRR
*   Net Present Value
*   Multiple of Cash
*   Pay-back period

Let’s start with the equity IRR and we’ll cover the rest in the next episodes.

Equity IRR
----------

### What it is and how to interoperate it?

*   Is a measure of project’s financial viability from the sponsor point of view
*   The equity IRR is compared with a hurdle rate required by investor

![Project Finance equity metrics, equity IRR](https://www.finexmod.com/wp-content/uploads/2021/05/EIRR01.jpg)

### What is the basis for the hurdle rate?

This is a completely different topic and will gets us into the shareholder weighted cost of capital, country risk premium, market competition and other factors. For more on this topic, check the below link:

[Discussion on cost of capital by Professor Edward Bodmer](https://edbodmer.com/cost-of-capital/)

### How is it calculated?

*   The equity IRR is calculated using the net cash flow to equity
*   Net cash flow to equity includes equity invested in the project in any form (development capital, shareholder loan, pure equity…) as outflow and any cash return going to investor as inflow (Shareholder loan proceeds, dividends, premiums, management fees…)

### Different Equity IRRs

### Pure Equity IRR

In my previous blog post “[Forms of Equity Contribution in a Project Finance structure](https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity/)
“, I talked about pure equity versus shareholder loan. I mentioned that for tax purpose and for optimizing their return, shareholders might decide to raise part of their capital in form of shareholder loan and contribute the remaining as share capital. Both forms are considered as equity and should be included in the calculation of return to investor. However, for information purpose, you can include a separate IRR calculation for Pure equity and another for Shareholder loan but the main metric should be the blended equity IRR.

Pure equity IRR take any distribution to investor in form of dividends as cash inflow and the outflow will be pur equity invested during financing or construction. Cash calls should also be included but note that cash calls should be zero in the base case. However, in down cases, you might come across periods with cash shortfall and therefore cash calls will need to be triggered to cover the deficit but a check should be included to alert the user that there’s an issue with project cash flows.

![Project Finance equity metrics and equity IRR](https://www.finexmod.com/wp-content/uploads/2021/05/PureEquityIRR.jpg)

### Shareholder loan IRR

The shareholder loan IRR should be in principal equal to the interest on shareholder loan. Any deviation might be due to taxes, capitalization of interest or deferral of any shareholder loan payments. In the below example, Interest on shareholder loan is 15% but the calculated IRR is 14%. the difference is due to withholding tax on interest and deferral of interest.

![Project Finance equity metrics and equity IRR](https://www.finexmod.com/wp-content/uploads/2021/05/ShareholderLoanIRR.jpg)

### Blended Equity IRR at financial close

Blended equity IRR is the return to the combined cashflow. It is the return taking both the net cash flow to pure equity and net cash flow to shareholder loan.

![](https://www.finexmod.com/wp-content/uploads/2021/05/BlendedEquityIRRFC-1.jpg)

### Blended life-cycle Equity IRR

The difference between blended life-cycle IRR and blended equity IRR at financial close is the development phase cash flows.

The blended life-cycle IRR takes the net cash flow to pure equity and shareholder loan and the development capital paid during development and the development capital remuneration received post financial close.

You only need to calculate the blended life-cycle Equity IRR when the developer is continuing with the financing post financial close, in other words when the developer is also the investor during construction phase. So for example you have a company investing EUR 1 million during development and then the same shareholder continue with the construction. Then there’s other issue related to compensation of development capital versus construction equity.

![Project Finance equity metrics and equity IRR](https://www.finexmod.com/wp-content/uploads/2021/05/BlendedLIfecycleEquityIRR.jpg)

### Equity IRR per Investor

If there are more than one investor, then separate Equity IRR calculation should be done for each investor. This is because each investor might have a different tax treatment. An investor who is paying taxes in UK might be subject to different withholding tax on interest or dividends than a shareholder based in Kenya.

![Project Finance equity metrics and equity IRR](https://www.finexmod.com/wp-content/uploads/2021/05/Seperate-ReturntoInvestors.jpg)

Also watch my YouTube video on the same topic and I walk you through one of my project finance model and show you how I calculate different equity IRRs in my financial models.

In the next video and post, I will talk about Project IRR. Hope to see you there.

All my best,

_Hedieh_

_Hedieh Kianyfard_

_Financial Model Detective_

_\=choose (2, Past, Now, Future)_

[](https://www.finexmod.com/equityirr#)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-05-18T14:01:44+00:00May 16th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&t=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&text=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/equityirr/&title=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&title=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR&summary=In%20my%20previous%20blog%20post%2C%20I%20talked%20about%20different%20forms%20of%20equity%20contribution%20and%20the%20role%20of%20the%20financial%20model%20to%20optimize%20the%20equity%20structure.%20In%20this%20episode%2C%20I%20want%20to%20show%20you%20different%20equity%20return%20measurements%20in%20a%20project%20finance%20transaction%20 "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&name=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR&description=In%20my%20previous%20blog%20post%2C%20I%20talked%20about%20different%20forms%20of%20equity%20contribution%20and%20the%20role%20of%20the%20financial%20model%20to%20optimize%20the%20equity%20structure.%20In%20this%20episode%2C%20I%20want%20to%20show%20you%20different%20equity%20return%20measurements%20in%20a%20project%20finance%20transaction%20and%20basically%20the%20below%20metrics%3A%0D%0A%0D%0A%20%09Equity%20IRR%0D%0A%20%09Project%20IRR "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&description=In%20my%20previous%20blog%20post%2C%20I%20talked%20about%20different%20forms%20of%20equity%20contribution%20and%20the%20role%20of%20the%20financial%20model%20to%20optimize%20the%20equity%20structure.%20In%20this%20episode%2C%20I%20want%20to%20show%20you%20different%20equity%20return%20measurements%20in%20a%20project%20finance%20transaction%20and%20basically%20the%20below%20metrics%3A%0D%0A%0D%0A%20%09Equity%20IRR%0D%0A%20%09Project%20IRR&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F05%2FEquity-IRR-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fequityirr%2F&title=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR&description=In%20my%20previous%20blog%20post%2C%20I%20talked%20about%20different%20forms%20of%20equity%20contribution%20and%20the%20role%20of%20the%20financial%20model%20to%20optimize%20the%20equity%20structure.%20In%20this%20episode%2C%20I%20want%20to%20show%20you%20different%20equity%20return%20measurements%20in%20a%20project%20finance%20transaction%20and%20basically%20the%20below%20metrics%3A%0D%0A%0D%0A%20%09Equity%20IRR%0D%0A%20%09Project%20IRR "Vk")
[Email](mailto:?body=https://www.finexmod.com/equityirr/&subject=Equity%20Return%20Metrics%20in%20a%20Project%20Finance%20Structure%3A%20Equity%20IRR "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/equityirr)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/equityirr#)

[Go to Top](https://www.finexmod.com/equityirr#)