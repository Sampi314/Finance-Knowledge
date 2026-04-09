# Best add-in for comparing versions of Excel spreadsheets

**Source:** https://pivotal180.com/comparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have

---

[Skip to content](https://pivotal180.com/comparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have/#fl-main-content)

The Best Excel add-in for comparing spreadsheet versions
========================================================

By Haydn Palliser | October 14, 2020

Sure, there are some great Excel add-ins that help modelers with efficiency, analysis of data, and navigating around models, but the ability to compare between versions of a model tops the list for me.

Most companies maintain the good practice of comparing large legal documents in Microsoft Word to review what changes have been made between versions (called blacklining). So how do organizations not have the ability to compare versions of Excel spreadsheets?

If you care at all about risk, you must have the functionality to compare versions of spreadsheets.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20736%20385'%3E%3C/svg%3E)

**_The situation – late night “quick” changes to a model_**
-----------------------------------------------------------

Your financial modeler makes last minute, late night changes to a financial model. Critical analysis is required for an important meeting first thing in the morning. Early in the AM you receive a new model with a list of the changes made and a set of new outputs.

**_The problem – what on earth did you change??_**
--------------------------------------------------

You need to know that the changes made to the model are:

1.  The only changes made
2.  Correct

I live by the mantra of ‘trust but verify’, the saying perhaps made most famous (in English) by Ronald Reagan. Yes, perhaps the saying is a contradiction with the word “but”, BUT when results matter it is appropriate.

I have been the modeler making last minute changes late at night. I know a lack of sleep and urgency creates an environment that only exacerbates errors. I have made those errors. Trust but verify!

**_The solution – run a comparison software_**
----------------------------------------------

A list of changes prepared by an analyst can only be trusted so far as you can verify them. This is the reason we need a tool that can check what was actually changed in the model (called ‘running comparisons’). We can only check the changes once we know what they are.

Several tools in the market can compare two versions of an Excel spreadsheet. The tools check which formulas were changed as well as how they were changed. They also check how the outputs of the model varied between versions.

**_Come on, enough background. Show us an example!_**
-----------------------------------------------------

I have demonstrated below the main functionality of comparisons using [Spreadsheet Advantage](http://www.spreadsheetadvantage.com/)
. This is the tool I have used the most, developed by [Joseph Lau](https://www.linkedin.com/in/joseph-lau-a4296a110/)
 and [Douglas Murray](https://www.linkedin.com/in/doug-murray-8006b31b/)
. Joseph also happens to be the ‘World Champion Financial Modeler’. It is not a title that has made him a fortune, or granted him fame, but he certainly deserves some respect when it comes to financial modeling. I also know him as an excellent project financier in Australia. Doug Murray is no slouch himself, having led more financial modeling and model review engagements than almost anyone in the world.

The initial model
-----------------

Here is the world’s simplest example…

The project has $80m of revenue and $25m of costs for a period of 4 years (shown with a flag in row 12). We have calculated Cash Available for Debt Service (CADS) beneath that, equal to Revenue less costs.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20749%20382'%3E%3C/svg%3E)

The modified model
------------------

We can visually inspect this model, and see there are some differences, mainly because this is a simple model. However, that is both slow and dangerous so let us turn to a comparison report.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20361'%3E%3C/svg%3E)

Comparison report (calculations and inputs)

An extract of the comparison report (shown below) is comparing the calculations and inputs between the two versions of the model with the click of a button. It is all consolidated in one place in a printable Excel spreadsheet.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20115'%3E%3C/svg%3E)

The changes are:

*   Cell C6 (input for revenue) was increased from $80m to $85m
*   Cells F15:I15 were changed, by removing the multiplication of the row to the flag in row 12.
*   Cell J15 was initially copied across from column I15 (denoted by ”), but is now hardcoded as negative $25m.

You could see some of these changes, but you could not easily see that a formula was replaced by a hardcode in cell J15.

Whatever the changes to the model are, the benefit of having them listed out helps you determine if the changes should have been made at all.

I have seen modelers hardcode values over a cell in the model. I have seen modelers accidently change an input. We are human, we make mistakes. Trust but verify.

**_Can you also check how outputs changed between versions of the model?_**
---------------------------------------------------------------------------

Absolutely! Most comparison tools allow you to check for different values in a model, either across the whole model, on certain sheets (e.g. outputs sheets), or on a defined range of cells.

What’s not to love?

Want to learn more on Spreadsheet Advantage?

Learn more about comparisons and other functionality provided by **[Spreadsheet Advantage.](http://www.spreadsheetadvantage.com/)
**

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fcomparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fcomparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fcomparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#d8e7bab7bca1e5b0acaca8abfdeb99fdea9efdea9ea8b1aeb7acb9b4e9e0e8f6bbb7b5fdea9ebbb7b5a8b9aab1b6bff5aebdaaabb1b7b6abf5b7bef5bda0bbbdb4f5aba8aabdb9bcabb0bdbdacabf5b9b6f5bda0bbbdb4f5b9bcbcf5b1b6f5a1b7adf5b5adabacf5b0b9aebdfdea9e)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/comparing-versions-of-excel-spreadsheets-an-excel-add-in-you-must-have/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA