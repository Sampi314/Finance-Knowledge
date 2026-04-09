# Difference Between Sensitivities and Scenarios in Financial Modeling

**Source:** https://pivotal180.com/scenario-sensitivity-blog-post-part-1-haydn

---

[Skip to content](https://pivotal180.com/scenario-sensitivity-blog-post-part-1-haydn/#fl-main-content)

So, What’s With Sensitivities and Scenarios?
============================================

By Haydn Palliser | June 16, 2020

It’s that time of year when many of you graduates in the Northern Hemisphere are starting jobs in project finance positions at investors, lenders, developers, or utilities.

Starting a new job can be daunting, and it may be even more so this year as you will likely be working remotely. It is harder to get feedback from new colleagues in a remote environment, but it is even harder to learn critical skills if you don’t have someone you can turn to for questions.

We hope this can help a little! In this blog we will outline the difference between sensitivities and scenarios in project finance.

This blog covers:

*   The purpose of a project finance model
*   Defining scenarios versus sensitivities
*   Using scenarios to structure your project
*   The importance of sensitivities to assess project resilience
*   Identifying the most important drivers of your project

Part 2 of this blog will define the specific best practice scenarios and sensitivities in project finance and we will outline the skills that we think you need to gain in your first year on the job. Hint: these are not all financial modeling related!

**Purpose of a Project Finance Model**
--------------------------------------

Many different participants come together to develop a project and each of these parties have their own needs. Each participant requires enough money to pay their costs and to generate their own returns. Some examples of the parties in a project finance deal include:

1.  The construction contractor (build the project)
2.  Equipment suppliers (provide and deliver equipment)
3.  The operations and maintenance contractor (operate and maintain the project)
4.  ‘Offtaker’, a fancy word for the party buying the product from the project (i.e. energy, gold etc.)
5.  The Government (receiving tax or perhaps paying for part of the project)
6.  Lenders providing debt to the project
7.  Equity investors seeking to achieve a target return

Whilst each participant may have their own financial model, ‘the [project finance model](https://pivotal180.com/courses/introduction-to-project-finance-modeling-in-house-2/)
’ is typically developed by the equity investor or someone acting for the equity investor. The model consolidates the inputs from all participants and attempts to structure a deal that works for everyone.

The equity investor is of course most interested in their own position, and the model is used by them to:

*   Determine the minimum price of the offtake such that the project generates an IRR in excess of their required hurdle rate (essentially a goal seek)
*   Maximize debt size based on the lender interest rate, tenor of the loan and lender covenants
*   Check that covenants are met such that they don’t default on the deal
*   Evaluate suppliers for the project (i.e. which lender results in better risk-adjusted returns)
*   Evaluate project designs (which design gives the better risk-adjusted return)
*   Consider terminal values of the project
*   Maximize the returns to equity for an appropriate level of risk

Sounds easy, right?

Unfortunately, model inputs change significantly throughout the development of the project and we need to assess more than one set of assumptions. This is where scenarios and sensitivities come into play.

**Scenarios vs. Sensitivities**
-------------------------------

At Pivotal180 we define a scenario and a sensitivity as:

**Scenario** – _A structuring case used to optimize the project (i.e. determine a sales price required to achieve a target hurdle rate, size debt, and to calculate debt repayments over the life of the project)_

**Sensitivities** – _Testing the project’s response to variations in non-fixed items (i.e. to variable costs or the sales price if that is not fixed via contract). Debt size and structure is assumed fixed._

**Scenarios (optimizing the model) are required to negotiate the deal**
-----------------------------------------------------------------------

Investors optimize the amount of debt the project can sustain and determine the product price required to achieve a target return, among other things. Let’s call this ‘optimizing the model’.

The challenge is that the model inputs will change significantly throughout the development of the project. The model needs to be re-optimized each time any input is revised. This happens many, many, many times over the deal negotiation period.

Why is this important?

**The model outputs are used to inform very critical decisions on the project.**

A good example of this is ‘what is the price of the offtake required to achieve the target returns’. This is the minimum price that should be agreed with the offtaker. If the developer or equity investor doesn’t know a minimum price to accept, how can they negotiate?

Note that this minimum offtake price required is based on many underlying assumptions. The returns to the investor will decrease if the interest rate on debt increases, or an operating cost increases. If interest or costs increase, the offtake price would need to be increased such that the equity investor achieves their required return. The new offtake prices is calculated (re-optimized) in the financial model.

For reasons beyond the scope of this blog, project finance lenders like certainty. Lenders like fixed price construction contractor, fixed operating costs, fixed offtake prices. These model inputs are often fixed at Financial Close. Financial Close is the point in time in which all Agreements dictating these costs and prices are signed.

After Financial Close the need for scenarios drastically reduces. There is no need to run a scenario to re-optimize the debt size or offtake price if you have already signed an Agreement to fix those!

Yes, there are some scenarios you may still run after Financial Close, such as refinancing of debt. But broadly, the need has reduced.

**Sensitivity analysis (project resilience when things don’t go to plan).**
---------------------------------------------------------------------------

Spoiler alert: deals do not go perfectly to plan. Despite our efforts in developing the project, we will have some variations in performance. It could be something entirely outside of our control, such as COVID-19, or inflation/deflation. Or it could be that we were too aggressive in various assumptions such as the amount the wind will blow, or the number of cars driving on a toll road. Whatever the reason, your forecast will be wrong.

Sensitivity analysis reviews the impact on the project if things don’t go to plan. Sensitivities can keep some items as fixed, such as the debt size on the project, but will review the impact of variable items changing.

You can also think of sensitivity analysis as ‘resilience testing’. Equity can evaluate in what situations does their project become worthless?

**Sensitivities help us worry about what matters most.**

You should recognize that sensitivities should be analyzed BEFORE the deal is done. Analysts must understand these risks before the deal is done, such that appropriate terms can be negotiated to avoid disaster.

Here are some examples of sensitivities:

*   Wind not blowing as much as forecast (such that the project doesn’t generate as much energy as expected)
*   Traffic on a road is less than expected (such that the project collects less tolls)
*   The characteristics of the copper deposit in the ground are worse than we thought (such that we sell less or it costs more to produce the final product)

Sensitivities can also be a make or break on a project. If the project is not resilient, an investor may consider not investing in it. There are many investors who invest in power plants with fixed offtake prices, but would never invest in a project that is exposed to market prices. Their view of power prices could be constant, but they don’t like the risk of market prices as it isn’t resilient enough.

**What sensitivities and scenarios should I run?**
--------------------------------------------------

You may find that your new team already has predefined scenarios and sensitivities to be run. Don’t be a sheep and just take those for granted. Your job is to identify issues and communicate them to your teams.

So where do you start? Do you just run every possible scenario and sensitivity? Well, sort of, but only because you should learn how a project finance model reacts to changes in inputs. But a common issue with new analysts is ‘analysis paralysis’. They can’t see the wood from the trees and they run too many scenarios.

**There will be a limited set of very influential inputs.**

The question you should be asking yourself is ‘what inputs will impact my project the most?”. The assumptions that impact your required outputs the most are the those which will require the heaviest negotiation and thought – so be sure to sensitize those the most!

The common way to identify the most important variables is by building a tornado plots, similar to the one shown in the figure below.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20721%20422'%3E%3C/svg%3E)

The tornado plot shows us the proportional impact of different sensitivities on a chosen output. It can be ranked as shown above, such that you instantly identify the inputs that will have the biggest impact on your returns.

The example above assesses the impact on the NPV to a utility considering an Independent Power Producer (IPP) to develop a solar project. IPPs will solve a power price they need in order to achieve their target return. From the standpoint of the utility, the discount rate required of the IPP will have the largest impact on their returns. The capital cost of the project and operating cost have less impact, but are still relatively important.

If you extended this to, say 10 inputs, you could quickly see the items that matter most to you. These are the scenarios and sensitivities to focus on the most.

**How do i create scenarios and sensitivities?**
------------------------------------------------

Check out our webinar on creating scenarios and sensitivities [**here!**](https://pivotal180.com/?p=2193)

In the next blog, we will provide some specificity of the types of scenarios and sensitivities you need to run, stay tuned!

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fscenario-sensitivity-blog-post-part-1-haydn%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fscenario-sensitivity-blog-post-part-1-haydn%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fscenario-sensitivity-blog-post-part-1-haydn%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#8db2efe2e9f4b0e5f9f9fdfea8becca8bfcba8bfcbfde4fbe2f9ece1bcb5bda3eee2e0a8bfcbfeeee8e3ecffe4e2a0fee8e3fee4f9e4fbe4f9f4a0efe1e2eaa0fde2fef9a0fdecfff9a0bca0e5ecf4e9e3a8bfcb)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/scenario-sensitivity-blog-post-part-1-haydn/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA