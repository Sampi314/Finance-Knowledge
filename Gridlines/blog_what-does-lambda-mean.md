# What does Lambda mean? - Gridlines

**Source:** https://www.gridlines.com/blog/what-does-lambda-mean

---

[Skip to content](https://www.gridlines.com/blog/what-does-lambda-mean#content)

What does Lambda mean?
======================

*   December 4, 2020

Those of you, like me, who follow Excel on social media (do your children take the p\*\*\* for this the way mine do?) may have seen a new article this week. Microsoft has [announced a new feature](https://techcommunity.microsoft.com/t5/excel-blog/announcing-lambda-turn-excel-formulas-into-custom-functions/ba-p/1925546)
 in Excel called Lambda (λ).

Lambda matters a lot. Both because of what it allows Excel to do, and because of what it tells us about how Microsoft sees the future of Excel. Lambda means Microsoft is continuing to develop Excel as a platform for serious analysis, now and in the future.

As an aside, why did they call it Lambda? For those interested, and with a reasonable math(s) background, have a look [here](https://en.wikipedia.org/wiki/Lambda_calculus)
.

Let’s look at what it is, then at the part that’s really exciting – Lambda functions are recursive.

First of all, it’s a way to create user-defined functions. You could already do that in Excel, of course, but you had to use VBA. That comes with a couple of drawbacks. Your functions are not available if someone turns off macros or if they try to run your spreadsheet in the cloud. Lambda doesn’t suffer from those problems. Just create any formula you like. Then with a few tweaks it can become a user-defined function that will always work, wherever it is used.

So far so good, but there’s one immediate drawback to me: Lambda seems to require you to put the formula that defines each function into a named range. This means that it is hard to see what the formula is doing.

Suppose you are working with loans, and you define a function called “Interest” which is “Balance” times “Interest rate”. Let’s suppose the balance is in row 10 and the interest rate in row 11. Then, in your Excel file, one cell will contain something like this: “=INTEREST(J10,$F11)”.

How, as a reader of a model, do you tell what calculation is being done here? You need to look into the list of named ranges and look at how “INTEREST” is defined. That’s not very transparent.

Openness, and the ability to see what calculations are being done, is fundamental to well written Excel models. If you’ll allow me a quick plug, it’s one reason we called our software Openbox.

And that’s not the only thing. Compared to VBA, Excel formulas are pretty limited. Surely you can’t create a user-defined function using Lambda that could do everything that a VBA user-defined function could? How are you going to do loops, in particular?

The answer – and this is the really exciting part of the whole thing – is that actually, you can.

Lambda now includes something called recursion. This means that a Lambda function can call itself, so it can have a loop inside it. And this, according to Microsoft, means that Excel is now something called [“Turing complete”](https://en.wikipedia.org/wiki/Turing_completeness)
.

Here’s the implication: **Excel formulas – without using any VBA, JavaScript or other tools – can now do any calculation at all.**

(To any computer scientists reading: yes, I know. It should read “any calculation that can be done on a universal Turing machine”. Bear with me).

In short, this means that there is now nothing that some other software could do that Excel formulas cannot. The argument “Excel cannot be used for X because…” has been killed. There’s a separate argument about whether it should be used, but that’s a different discussion that needs to look at the pros and cons of Excel versus another tool.

And that matters because of what it says about Microsoft’s view of Excel. It says that Microsoft is willing to go to a lot of effort – and adding Lambda must have been that – to make Excel a first-rank analytical tool. And that means that they see Excel being around for a very long time to come.

Share:

*   [](https://uk.linkedin.com/company/gridlines-com)
    

More Posts

[![Man and woman in a bright office, smiling and talking during a meeting](https://www.gridlines.com/wp-content/uploads/2024/05/jason-goodman-Ti7LQ0r-zy4-unsplash-scaled-1-300x208.jpg)](https://www.gridlines.com/blog/financial-model-audit-what-makes-a-good-audit/)

[Financial Model Audit: What makes a good audit?](https://www.gridlines.com/blog/financial-model-audit-what-makes-a-good-audit/)

We are constantly striving to make our model audit service as good as it possibly can be. Here’s what we

[![financial software](https://www.gridlines.com/wp-content/uploads/financial-software-300x169.jpg)](https://www.gridlines.com/blog/openbox-v1-0/)

[Openbox V1.0](https://www.gridlines.com/blog/openbox-v1-0/)

The last year has been quite a journey for Openbox. The pace of change really picked up over the last

[![mistakes in finance](https://www.gridlines.com/wp-content/uploads/mistakes-in-finance-300x169.jpg)](https://www.gridlines.com/blog/killer-errors-adding-when-you-mean-to-subtract/)

[Killer Errors – Adding when you mean to subtract!](https://www.gridlines.com/blog/killer-errors-adding-when-you-mean-to-subtract/)

It still surprises me when we are completing a financial model audit, how often we encounter errors where rather than

[![Barber cutting a mans hair](<Base64-Image-Removed>)](https://www.gridlines.com/blog/why-can-i-never-get-a-good-haircut/)

[Why can I never get a good haircut?](https://www.gridlines.com/blog/why-can-i-never-get-a-good-haircut/)

Every few weeks the facial recognition on my iPhoneX (humble brag) stops working. This inability of my phone to recognise

[PreviousThe Multi-Billion Dollar Excel Error that didn’t happen today](https://www.gridlines.com/blog/the-multi-billion-dollar-excel-error-that-didnt-happen-today/)

[NextOpenbox release notes: December update v0.8.21](https://www.gridlines.com/blog/openbox-release-notes-0-8-21/)

Tell us about your project
--------------------------

[![Akram Mostafa](<Base64-Image-Removed>)](mailto:akram.mostafa@gridlines.com)

Akram Mostafa
-------------

Associate Director

akram.mostafa@gridlines.com

[![](<Base64-Image-Removed>)](mailto:morag.loader@gridlines.com)

Morag Loader
------------

Director of Accounting & Tax

morag.loader@gridlines.com