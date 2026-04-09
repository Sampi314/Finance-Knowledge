# Twelve core financial model build skills

**Source:** https://www.financialmodellinghandbook.org/twelve-core-financial-modelling-skills

---

In the next section of the book, we will create a model from scratch, step by step.

When we do that, you will see that there are twelve "modelling mechanics" that we will use repeatedly.

If you get proficient in these skills they will transform your model build effectiveness.

Since we will use these sequences so frequently throughout the model build process, I won't keep spelling them out each time we use them. I'll refer to the operation by name - and you can check back to this chapter for the steps.

This stuff doesn't need to be complicated.

Like all skills, you'll get good at these operations if you practice them. They will also make more sense to you if you do them yourself.

For each skill, you will be able to download a file to practice the skill.

**Conceptual model**
--------------------

To practice the first few skills, we will build a calculation block for Electricity generation revenue.

The ingredients we need for this calculation are as follows:

*   Power tariff - an input & a constant - expressed in USD / kWh. We are going to assume 6.5 cents per kWh initially.
*   Electricity production - a series line item already calculated in our model, expressed in GWh per period
*   An escalation factor as the Electricity revenue is going to increase with inflation over time.
*   An Operating period flag to ensure that we only recognise revenue during the operating period.
*   Conversion factors. Our standard monetary unit is USD 000s, and our generation is expressed in GWh, whereas our tariff is expressed in kWh.

Before we begin, a good first step is to create a section label using the heading columns of our model. Feel free to create plenty of headings or sub-headings. The more signposts there are in your model, the easy it will be for you and others to find your way around.

![](https://www.financialmodellinghandbook.org/content/images/public/images/7329f836-570f-41be-9d57-5cd05e7a990f_1930x632.jpeg)

* * *

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--67.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

Sorry, comments couldn't be loaded. It looks like this account is not currently active.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/twelve-core-financial-modelling-skills#/portal/signup)