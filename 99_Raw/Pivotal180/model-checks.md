# Best Practices for Model Checks in Financial Modeling

**Source:** https://pivotal180.com/model-checks

---

[Skip to content](https://pivotal180.com/model-checks/#fl-main-content)

Best Practices for Model Checks in Financial Modeling
=====================================================

By Alison Leckie | April 25, 2023

**Overview**

This is one of our videos from our renewable energy, tax equity, and infrastructure project finance modeling courses.

Video
-----

**Video Transcript** 
---------------------

In this video, we’ll discuss model checks. Now, model checks are a must have in a best practice model, so of course we use them in all of our Pivotal180 financial modeling courses and you must use them in your models.

So what is a model check and why do we use them?

A model check is a pre-formatted alert in your model that clearly highlights a potential problem that needs attention or a fix. The purpose of a check is to help you identify an error or to verify a calculation is accurate. They’re also formatted to be visually obvious. For example, a check may display as a red warning if there’s a problem or a white OK if no error is found. The bigger and more complicated the model, the more important checks are. Let’s first consider what sort of checks we may want in a model. Haydn, what sort of things do you wish to check in a model?

Required checks vary depending on the use of the model or maybe the key risks of an investment. You should build checks that make sense for your analysis. But look, some common checks in financial models include,

*   is our business forecast to run out of cash in any future period?
*   are we forecasting debt to be repaid on time?
*   is the business forecasted return meeting our required return?
*   does the balance sheet balance?
*   have you perhaps entered a nonsensical input? Or
*   perhaps do we not have enough money to fund an expansion?

Look there are many, many more, but these are at least a few examples.

Let’s take a look at how we use model checks. You can see on screen a set of checks grouped into two categories, being compliance and coding. We don’t always group checks in into categories, but in larger models we do.

Compliance checks include items such as,

*   is the debt forecast to be repaid on time or
*   is the cash balance forecast to go negative?

These error checks are mostly commercial in nature. If one of these checks result in a warning, it means there may be a commercial error. This type of error typically requires an input to be changed.

Coding checks include items such as

*   the balance sheet doesn’t balance,
*   the annual outputs don’t have the same totals as the quarterly outputs.

These are coding error and often mean a calculation is incorrect or you have incorrectly linked a calculation to the false precedent.

Both categories are errors. One category isn’t worse than the other, but the categories help us understand the nature of the errors.

Here is how the checks flow through a model. Right now, the checks in our model show OK, this means the model is working as intended and no checks are failing. The total compliance check here is OK because all of the checks in the compliance section are OK. If even one of the checks fails like now, then the master check will fail. If the master check fails, see how the top of my model includes the error checks to show the user that there is an error, and as we cycle across sheets in my model, all sheets highlight that I have an error. It is really obvious that I have an error because of the big red warning box being shown throughout my model. You can imagine how this central check section in my model can be useful in quickly identifying any issues that I may have. It isn’t easy to see all of these issues, so centralizing them in one section is really helpful.

We’ll show you how to build these model checks in future lessons and model walkthroughs. You will learn how create them and to format them as we showed you. But start thinking now, what checks will you want to add to your model?

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fmodel-checks%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fmodel-checks%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fmodel-checks%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#96a9f4f9f2efabfee2e2e6e5b3a5d7b3a4d0b3a4d0e6ffe0f9e2f7faa7aea6b8f5f9fbb3a4d0fbf9f2f3fabbf5fef3f5fde5b3a4d0)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Alison Leckie

[https://www.linkedin.com/in/alison-leckie-56023364/](https://www.linkedin.com/in/alison-leckie-56023364/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/model-checks/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA