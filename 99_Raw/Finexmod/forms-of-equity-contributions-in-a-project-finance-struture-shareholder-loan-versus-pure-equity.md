# Forms of Equity Contributions in a Project Finance Structure: Shareholder loan versus pure equity – Finexmod

**Source:** https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity

---

[Skip to content](https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity#content)

Forms of Equity Contributions in a Project Finance Structure: Shareholder loan versus pure equity

**Sponsor Equity Contributions**
--------------------------------

One of the main benefits of a project finance transaction is that it increases the level of debt that can be borrowed. However, lenders involved in a project finance deal still require some equity contribution in the deal. It’s true that the level of debt raised depends on the project’s feature cash flow however even if a project can be funded with 100% debt, still lenders require a percentage usually 15% to 30% of equity contribution. The equity is fully subordinated to any payment to any operating contractor and lenders and it’s usually at the bottom of the cash flow waterfall (For more on **[cash flow waterfall check my blog post and suggested template here](https://www.eloquens.com/tool/nJeYHzd1/strategy/waterfall-chart-excel-templates/typical-cash-flow-waterfall-excel-template-and-pdf-manual/?ref=FinExMod)
**).

When it comes to equity, there are multiple way that shareholder can contribute. The most common forms are : pure equity and shareholder loan. Other forms are Equity Bridge loan and Letter of Credit which are short term facilities. In this blog post, I am going to talk about Pure equity and shareholder loan and show you how to incorporate these facilities in a project finance model.

![Equity contribution in a project finance transaction, shareholder loan versus share capital ](https://www.finexmod.com/wp-content/uploads/2021/05/FormOfEquity01.jpg)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Pure Equity**
---------------

*   It’s a source of financing from the shareholder to fund part of the construction costs during construction.
*   It’s the most expensive source of financing
*   Also called “Share Capital”, “Base equity” or simply “Capital”
*   Share capital is recorded under the equity account in the balance sheet.
*   The amount of capital invested into the project translates into shares that will be distributed to each shareholder accordingly.
*   the repayment of the share capital is not fixed and depends on cash availability.
*   Cash available for distribution as dividends to repay the share capital comes at the bottom of the cash flow cascade and subordinated to payment to operators and lenders.

**Shareholder Loan**
--------------------

*   It’s another source of financing
*   It’s usually prices at the rate or close to the required equity IRR
*   is recorded as a long-term liability and It should be treated like any other debt but fully subordinated to any other payment (Opex, senior debt, funding of reserve accounts)
*   typically the shareholder loan has a fixed tenor but with the flexibility to extend and defer any payment under shareholder loan
*   Same as pure equity, any payment under shareholder loan is subject to lenders covenants (for more on debt covenant please refer to my blog post on [**Distribution Lock-ups**](https://www.finexmod.com/distribution-lock-ups/)
    )

**Pure Equity versus Shareholder Loan? What is the Sponsor’s preference and why?**
----------------------------------------------------------------------------------

*   Tax shield: Depending on the jurisdiction, interest payments on the shareholder loan can be tax deductible and dividends are not tax deductible. in jurisdictions where the this capitalisation rule is adopted, then there’s a limit to how much interest can be deductible when computing the taxable income.
*   To avoid cash trap: Having a shareholder loan tranche might allow the shareholder to extract cash in years where dividends are not allowed. For example, dividends are only allowed when the project is profitable. There might be cases where the projected is generating cash but it’s not showing profit. In these years dividends are not allowed because of this accounting restriction however the same cash can be distributed as shareholder loan interest and principal.

Building flexibility to test the impact of different forms of equity contribution in a project finance model
------------------------------------------------------------------------------------------------------------

### Step 1: Inputs

First of all from the above discussion about the choice of shareholder loan versus share capital, we realize that it’s important to run the model and test whether a shareholder loan facility can improve equity IRR, and the quantum of shareholder loan that can benefit the project and it’s shareholder. In other words we need to optimize the equity contribution by testing different funding structures wile taking into consideration lenders convenants and requirements in terms of distributions and also reflect the taxation applicable to different facilities, in other words we need to answer the below questions:

*   Is shareholder Loan interest taxed? if yes by how much?
*   Is shareholder loan principal is taxed? if yes by how much?
*   Is dividend taxed? if yes by how much?
*   Is shareholder loan interest tax deductible and if yes by how much? meaning is it subject to thin capitalisation rules?

We also need to check restriction imposed on distribution by lenders in the loan agreement and see if any payment under shareholder loan is subject to same restrictions and tests as dividends or are there more flexibilities for payments under shareholder loan?

Unless we have the answer to the above questions and have a financial model to test different type of equity contribution, we will not be able to advise investors on how to optimize their equity contribution.

Once we have the above information and the terms of the shareholder loan, we need to build a shareholder loan tranche in the financial model and see if a shareholder loan is going to improve the project economics.

![Optimum financing structurem shareholder loan versus share capital in a project finance transaction and financial model ](https://www.finexmod.com/wp-content/uploads/2021/05/FormOfEquity02.jpg)

**Step 2: Sizing of Shareholder Loan and Pure equity**

Before reaching this step, debt should be sized and we should therefore know how much equity (in whatever form) is required. Once we have the total amount of equity required and the drawdown schedule, we use the inputs entered in the Input section to breakdown the equity into a percentage as shareholder loan and the remaining as Pure equity.

![Optimum financing structure shareholder loan versus share capital in a project finance transaction and financial model ](https://www.finexmod.com/wp-content/uploads/2021/05/FormOfEquity03.jpg)

**Step 3: Create a shareholder loan Corkscrew**

Same as any other debt tranche in a financial model we create a corkscrew account for the shareholder loan tranche.

The main differences between senior loan and shareholder loan are:

*   Any payment under shareholder loan is subject to cash flow availability and is also subject to satisfaction of covenants imposed by lenders(for more on debt covenant please refer to my blog post on [**Distribution Lock-ups**](https://www.finexmod.com/distribution-lock-ups/)
    ).
*   If in any period in the model, there’s not enough cash to pay interest or principal due on shareholder loan, it can be deferred. So the deferral mechanism needs to be built into the financial model and in the shareholder loan calculation block.

![Optimum financing structure shareholder loan versus share capital in a project finance transaction and financial model](https://www.finexmod.com/wp-content/uploads/2021/05/FormOfEquity04.jpg)

If you are interested in a more detail model walk-through, check the below YouTube video.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-05-12T07:05:26+00:00May 5th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&t=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&text=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity/&title=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&title=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity&summary=Sponsor%20Equity%20Contributions%20%0D%0AOne%20of%20the%20main%20benefits%20of%20a%20project%20finance%20transaction%20is%20that%20it%20increases%20the%20level%20of%20debt%20that%20can%20be%20borrowed.%20However%2C%20lenders%20involved%20in%20a%20project%20finance%20deal%20still%20require%20some%20equity%20contribution%20in%20the%20deal.%20It "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&name=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity&description=Sponsor%20Equity%20Contributions%20%0D%0AOne%20of%20the%20main%20benefits%20of%20a%20project%20finance%20transaction%20is%20that%20it%20increases%20the%20level%20of%20debt%20that%20can%20be%20borrowed.%20However%2C%20lenders%20involved%20in%20a%20project%20finance%20deal%20still%20require%20some%20equity%20contribution%20in%20the%20deal.%20It%26%2339%3Bs%20true%20that%20the%20level%20of%20debt "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&description=Sponsor%20Equity%20Contributions%20%0D%0AOne%20of%20the%20main%20benefits%20of%20a%20project%20finance%20transaction%20is%20that%20it%20increases%20the%20level%20of%20debt%20that%20can%20be%20borrowed.%20However%2C%20lenders%20involved%20in%20a%20project%20finance%20deal%20still%20require%20some%20equity%20contribution%20in%20the%20deal.%20It%26%2339%3Bs%20true%20that%20the%20level%20of%20debt&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F05%2FFormOfEquityCover-1.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fforms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity%2F&title=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity&description=Sponsor%20Equity%20Contributions%20%0D%0AOne%20of%20the%20main%20benefits%20of%20a%20project%20finance%20transaction%20is%20that%20it%20increases%20the%20level%20of%20debt%20that%20can%20be%20borrowed.%20However%2C%20lenders%20involved%20in%20a%20project%20finance%20deal%20still%20require%20some%20equity%20contribution%20in%20the%20deal.%20It%26%2339%3Bs%20true%20that%20the%20level%20of%20debt "Vk")
[Email](mailto:?body=https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity/&subject=Forms%20of%20Equity%20Contributions%20in%20a%20Project%20Finance%20Structure%3A%20Shareholder%20loan%20versus%20pure%20equity "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![Accuracy in Financial Modeling](https://www.finexmod.com/wp-content/uploads/2025/06/2-500x383@2x.png)

[](https://www.finexmod.com/draft-post-2/)

#### [Accuracy in Financial Modeling](https://www.finexmod.com/draft-post-2/ "Accuracy in Financial Modeling")

June 12th, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

[Page load link](https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity#)

[Go to Top](https://www.finexmod.com/forms-of-equity-contributions-in-a-project-finance-struture-shareholder-loan-versus-pure-equity#)