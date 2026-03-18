# Why we mark imports and exports

**Source:** https://www.financialmodellinghandbook.org/why-we-mark-imports-and-exports

---

What's covered in this chapter:

*   The difference between imported and local links
*   Why we mark imported links
*   Why we mark exported links
*   How to apply import and export formatting

* * *

Calculation blocks are up made of links.

Those links become very useful for navigating around the model.

You may have noticed that we use a variety of colours in the formatting of links and calculations.

This colouring is all about understanding how data is flowing in the model.

The difference between an imported and a local link
---------------------------------------------------

One of the goals in this modelling system is to reduce the amount of Stupid Unnecessary Thinking Time. Achieving this means increasing the number of things we can do without thinking about them.

Let's take a look at an example:

![](https://www.financialmodellinghandbook.org/content/images/public/images/796dec4c-f8ef-47bc-a6bb-7fed55f5b8e4_2846x618.jpeg)

What can we tell about these calculation structures without looking at a single formula? Knowing two rules, we can tell quite a lot.

Those rules are:

*   Imported links (links coming from another sheet) are marked blue
*   Local links are marked black
*   Calculations are always the last item in a block.

Although local links and calculations are both black, we can tell them apart because only calculations are at the bottom of a block.

Why we mark imports
-------------------

Import and export marking allows us to know quite a lot about what's going on in the calculation structure without looking at a single formula.

We can think of this as metadata. This is data about our data encoded using formatting and positioning within the calculation block.

This metadata helps us cut down the amount of thinking time.

Looking at the electricity production calculation block, we can tell that:

*   Year 1 P50 yield & Availability are both coming from another sheet. Most likely the input sheet.
*   Compound degradation and Seasonality adjustments are both coming from the same sheet.
*   Electricity generation is the calculation.

Similarly, with the Electricity revenue calculation block, we can tell that:

*   Power tariff, GWh to kWh conversion, Units in a thousand and the Operating Period Flag are all coming from another sheet,
*   Electricity production is coming from the same sheet and must therefore be a link to the block above.
*   Electricity revenue is the calculation.

We create a lot of links in our models. And we copy those links a lot when we need to use them again. Blue links (imported) can be copied anywhere in the model and will continue to point back to the source calculation. We can only copy local links within their own calculation sheet since they don't have the sheet name in the cell address.

**Why we mark exports**
-----------------------

Suppose our example looked like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/cebb93fd-01a2-43c7-8524-923e443fe59a_2730x656.jpeg)

We now have an additional piece of metadata encoded. Electricity Generation Revenue is now marked red, telling us that another calculation, somewhere else in the model, is linking to this calculation.

This metadata is helpful for two reasons:

### It indicates the relative importance of this line item.

Often it's the most critical link items in a section that gets exported. Things like revenue, opex, debt interest, depreciation etc. We often link these important line items into our financial statements or other critical calculations. By marking the lines that are being exported, we can quickly see which are those "needed elsewhere in the model" critical line items.

### It tells us we are going to have #REFs elsewhere in the model if we delete the line item.

If we delete a link item that is being linked to by another part of the model, we may not get immediate feedback that we have caused a problem. The resulting #REFs will be on another sheet and may not be visible to us. By marking an exported calculation red, we know, even before deleting it, that another part of the model relies on this line item. We may still want to delete it, but we know there will be an issue elsewhere in the model we will have to deal with if we do.

How to apply import and export marking
--------------------------------------

If you use Ctrl+Shift+q to create links ([See Financial Modelling Skill 2 - How to create a link](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)
), the macro will automatically apply the correct formatting to both sides of the link;

*   it will correctly mark the link at the destination as either local (black) or imported (blue)
*   it will correctly mark the link at source as exported if applicable.

Using Ctrl+Shift+q means you don't have to think much about applying the correct formatting.

If you do need to format a link:

Ctrl+Shift+m applies import formatting

Ctrl+Shift+x applies export formatting

Ctrl+Shift+b applies black font for calculations / local links.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--157.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

* * *

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
Subscribe](https://www.financialmodellinghandbook.org/why-we-mark-imports-and-exports#/portal/signup)