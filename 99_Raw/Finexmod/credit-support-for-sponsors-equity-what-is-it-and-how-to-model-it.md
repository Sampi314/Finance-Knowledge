# Credit Support for Sponsors’ Equity: What is it and how to model it – Finexmod

**Source:** https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it

---

[Skip to content](https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it#content)

Credit Support for Sponsors’ Equity: What is it and how to model it

Let’s start with the definition and answer the question:

What is project finance?
------------------------

*   Project finance is a method of raising long-term debt for infrastructure, industrial projects, and public services using a **non-recourse or limited recourse** financial structure.
*   meaning that in such a transaction lenders only have access to projected project’s cash flows of the project for the servicing and repayment of the debt.
*   with the project’s assets and rights held as secondary collateral.
*   Off-balance sheet

**So, does that mean that in a project finance transaction, no guarantee from the sponsor is required?**
--------------------------------------------------------------------------------------------------------

Although shareholders are typically liable up to their base equity commitment, there are typically different support or guarantees required from sponsors.

In a previous video and blog post, I talk about sponsor contingent equity:<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>

Another guarantee required from the sponsor is…
-----------------------------------------------

“Credit Support for Sponsors’ Obligations”

Because there is a possibility for investors not to commit all their equity up-front at financial close, lenders require credit support from sponsors to guarantee their obligations (Maximum sponsor equity commitment).

To understand this topic, you first need to understand the different equity injections possibilities. I have a dedicated blog post where I explain 6 different equity injection schedules. You can also download the demo model for free from the below source:  
<span data-mce-type="bookmark" style="display: inline-block; width: 0px; overflow: hidden; line-height: 0;" class="mce\_SELRES\_start">﻿</span>

Let’s simplify it
-----------------

Now that you know the legal terms, let’s simplify it by telling the story. First of all, remember that everything that is in a contract is because we humans, we don’t have trust in each other and to protect ourselves from each other, we create contracts and each clause in a contact is to protect a party from another’s party’s actions and decisions or to allocate a risk to someone else.

This particular clause in a loan agreement is to provide guarantee to lenders that sponsor will have their share of committed funds when they are due. The story goes like this:

A sponsor will go to a bank and ask them to co-fund a project with them.

Lenders agree to fund 70% of construction cost given that 30% remaining is coming from sponsors.

They agree on the amount. Then lenders ask sponsor to put all the money up-front.

Sponsors disagree and ask lenders to fund pro-rata. Meaning at each disbursement date, lenders commit 70% and equity 30%. Lenders agree but ask sponsors to provide them with some sort of guarantee that the money is going to be available during the construction of the project. Sponsor agree and go to another lending institution and open an LC with them and submit the evidence to lenders before the financial closing of the project.

![](https://www.finexmod.com/wp-content/uploads/2021/12/storytelling-4-frames.jpg)

Commercial Impact of **Undrawn Equity guarantee**
-------------------------------------------------

![](https://www.finexmod.com/wp-content/uploads/2021/12/LC-issuing-bank.jpg)

There’s a fee attached to issuing the letter of credit for the undrawn equity and someone needs to pay the fee.

1\. The LC fee is included in the project cost and paid by the project as part of the uses of funds

2\. The LC fee is paid directly by sponsor and reducing the sponsor return with no impact on the project

Depending on the negotiation, any of the two options can be considered.

Financial modeling of **Undrawn Equity guarantee LC fee**
---------------------------------------------------------

Download the demo financial model which is a complete but simple model meaning that it has all essential component of a typical project finance model:

### Step 1: Inputs

Include the inputs that you need in your input sheet. You mainly need 3 inputs:

1.  Undrawn equity LC fee
2.  #days in a year for calculation of LC fee
3.  a True/False switch to include LC fee in the S&U or to include in the IRR calculation

![Credit Support for Sponsors’ Equity: What is it and how to model it #projectfinancestorytelling](https://www.finexmod.com/wp-content/uploads/2021/12/Credit-Support-for-Sponsor-equity-FM-Inputs.jpg)

### Step 2: Calculation

*   You most probably already have an equity balance in your financial model. You need to calculate the undrawn equity balance and it’s going to be the base for calculating the LC fee.

![](https://www.finexmod.com/wp-content/uploads/2021/12/formula.jpg)

![Credit Support for Sponsors’ Equity: What is it and how to model it #projectfinancestorytelling](https://www.finexmod.com/wp-content/uploads/2021/12/Undrawn-LC-calculation-block.jpg)

### Step 3: Summary

Include the LC fee in summary sources and Uses in your summary sheet. You can also include a chart showing the drawdown schedule on different facilities and include the equity IRR and the LC fee switch in the chart and dynamically see how the drawdown schedule and the LC fee on undrawn equity will have an impact on total project cost or equity IRR.

![](https://www.finexmod.com/wp-content/uploads/2021/12/summary.jpg)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-12-06T17:44:07+00:00December 5th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&t=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&text=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it/&title=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&title=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it&summary=Let%27s%20start%20with%20the%20definition%20and%20answer%20the%20question%3A%0D%0AWhat%20is%20project%20finance%3F%0D%0A%0D%0A%20%09Project%20finance%20is%20a%20method%20of%20raising%20long-term%20debt%20for%20infrastructure%2C%20industrial%20projects%2C%20and%20public%20services%20using%20a%20non-recourse%20or%20limited%20recourse%20financial%20st "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&name=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it&description=Let%26%2339%3Bs%20start%20with%20the%20definition%20and%20answer%20the%20question%3A%0D%0AWhat%20is%20project%20finance%3F%0D%0A%0D%0A%20%09Project%20finance%20is%20a%20method%20of%20raising%20long-term%20debt%20for%20infrastructure%2C%20industrial%20projects%2C%20and%20public%20services%20using%20a%20non-recourse%20or%20limited%20recourse%20financial%20structure.%0D%0A%20%09meaning%20that%20in%20such%20a%20transaction%20lenders%20only "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&description=Let%26%2339%3Bs%20start%20with%20the%20definition%20and%20answer%20the%20question%3A%0D%0AWhat%20is%20project%20finance%3F%0D%0A%0D%0A%20%09Project%20finance%20is%20a%20method%20of%20raising%20long-term%20debt%20for%20infrastructure%2C%20industrial%20projects%2C%20and%20public%20services%20using%20a%20non-recourse%20or%20limited%20recourse%20financial%20structure.%0D%0A%20%09meaning%20that%20in%20such%20a%20transaction%20lenders%20only&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F12%2FBase-equity-LC-cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fcredit-support-for-sponsors-equity-what-is-it-and-how-to-model-it%2F&title=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it&description=Let%26%2339%3Bs%20start%20with%20the%20definition%20and%20answer%20the%20question%3A%0D%0AWhat%20is%20project%20finance%3F%0D%0A%0D%0A%20%09Project%20finance%20is%20a%20method%20of%20raising%20long-term%20debt%20for%20infrastructure%2C%20industrial%20projects%2C%20and%20public%20services%20using%20a%20non-recourse%20or%20limited%20recourse%20financial%20structure.%0D%0A%20%09meaning%20that%20in%20such%20a%20transaction%20lenders%20only "Vk")
[Email](mailto:?body=https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it/&subject=Credit%20Support%20for%20Sponsors%E2%80%99%20Equity%3A%20What%20is%20it%20and%20how%20to%20model%20it "Email")

Related Posts
-------------

![Accuracy in Financial Modeling](https://www.finexmod.com/wp-content/uploads/2025/06/2-500x383@2x.png)

[](https://www.finexmod.com/draft-post-2/)

#### [Accuracy in Financial Modeling](https://www.finexmod.com/draft-post-2/ "Accuracy in Financial Modeling")

June 12th, 2025

![My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/wp-content/uploads/2024/09/Copy-of-White-Minimalist-Blog-Post-Linkedin-Article-Cover-500x383@2x.png)

[](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/)

#### [My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/ "My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn")

September 27th, 2024

![Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/wp-content/uploads/2024/09/contingency-Cover-500x383@2x.png)

[](https://www.finexmod.com/project-finance-contingency/)

#### [Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/project-finance-contingency/ "Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision")

September 13th, 2024 | [0 Comments](https://www.finexmod.com/project-finance-contingency/#respond)

[Page load link](https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it#)

[Go to Top](https://www.finexmod.com/credit-support-for-sponsors-equity-what-is-it-and-how-to-model-it#)