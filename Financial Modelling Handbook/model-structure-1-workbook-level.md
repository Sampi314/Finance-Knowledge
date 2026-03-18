# Model structure 1: Workbook level

**Source:** https://www.financialmodellinghandbook.org/model-structure-1-workbook-level

---

When it comes to the structuring and layout of financial models, modellers disagree about many things.

I have never come across anybody who disagrees that models should always separate inputs, calculations, and outputs.

In my opinion, it's possible to apply this principle and still create a model that's an unreadable hot mess. But any model that fails to apply this will fail to meet even the minimum professional standard.

Worksheet order
---------------

We are going to have a worksheet for each “chapter” in our book. There are four different categories of worksheet:

*   Inputs. Sometimes just a single sheet, but there can be several.

*   Calculations. In any substantial model, there will be several calculation sheets split up into topic areas.
*   Outputs. These include financial statements, dashboards, output comparison sheets.
*   Controls. These include sheets containing things like error checks and a changelog.

It's helpful to show the categorisation of the sheets using a specific colour for each category. This "metadata" tells the user what kind of sheet it is before they click on it.

Generally, we want to follow a left to right reading order. If we follow the logical flow of the model, we'll start with inputs, then have calculations and outputs.

A logical flow to the calculation sheet order also helps. I find that sequencing in line with the order in which items appear on the income statement is useful. Since our time calculations underpin everything in the model, it's helpful to have that sheet first. It works well to structure the order of the sheets to follow the flow of the Income Statement.

![](https://www.financialmodellinghandbook.org/content/images/public/images/eb781e2d-74da-4cce-9ee7-56e9d6cf50a2_1724x238.jpeg)

An exception to this left to right rule would be to apply the "bottom line up front" principle and put financial statements and critical output summary sheets at the front. These are the sheets in which users of the model will be most interested. It, therefore, makes sense for them to be as accessible as possible.

![](https://www.financialmodellinghandbook.org/content/images/public/images/58d87652-81e7-4395-bed0-b627f24aeea9_1730x248.jpeg)

Worksheet naming
----------------

Keep your sheet names as short as possible while still keeping it clear what the sheet is. We use "Ops" instead of "Operations", "FS" instead of financial statements, "FS Ann" for "Annual financial statements".

Short sheet names are helpful because frequently there are numerous calculation sheets; seeing more of them at once is helpful.

(Note to Microsoft: when oh when can we get two rows of tab names?)

This recommendation applies to file names as well. The shorter, the better.

Template sheet
--------------

As you'll see when we look at worksheet structure shortly, each sheet in the model carries a consistent and well-defined structure. We don't want to recreate that structure every time we need a new worksheet.

It's helpful, therefore, to have a Template sheet in the model. You'll copy the template sheet each time you add a worksheet into your model. As we'll see later, this is also an excellent place to store template code that we frequently reuse in our models.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--24.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/model-structure-1-workbook-level#/portal/signup)