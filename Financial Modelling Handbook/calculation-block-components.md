# The components of calculation blocks

**Source:** https://www.financialmodellinghandbook.org/calculation-block-components

---

There can only be four different kinds of line items in a calculation block.

1.  A calculation
2.  A link
3.  A placeholder
4.  An input

In this section, we are only going to look at what these things are, and how and why we use them. In the next section, we will go step by step through how we build them.

![](https://www.financialmodellinghandbook.org/content/images/public/images/143b3ec1-75c7-4b5a-bd8d-b7750902b6e5_2430x420.jpeg)

Let's look at the types of line items we have in the block above:

*   Row 23: an input - we’ll move this later.
*   Row 24: an offsheet link
*   Row 25: a local link -
*   Row 26: a calculation. Always the last item in the block.

What we are aiming for here is the ability to look at the model and understand immediately what you’re looking at, without wasting your time interrogating formulas or trying to figure stuff out.

💡

The structure of the model tells you exactly what each item is visually, and therefore instantly.

1 A calculation
---------------

The calculation is always the last item in the block.  You can immediately recognise a calculation block from the structure of the model; and, therefore, immediately know that the last item is a calculation.

By extension, if something is not the last item in the block, it must not be a calculation and will instead be an ingredient to that calculation.

Take a minute to internalise this as it's core to all the modelling we will do in the rest of this book:

💡

**The calculation is always the last item in the block. If it's not the last item in the block, it's not a calculation.**

There will be times that you need to break this rule. Those times should be the exceptions. We will talk about some exceptions later in the book.

If it's not the last item in the block, and therefore not a calculation, there are only three possible things it can be.

2 A link
--------

Wherever possible, we present all of a calculation's ingredients in the block, next to the calculation itself. This helps to reduce thinking time. If everything driving the calculation is visible next to it, we reduce the time required to understand and decode a formula.

See [Modelling Skill 2](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)
 to learn more about creating a link, and [Modelling Skill 4](https://www.financialmodellinghandbook.org/how-to-copy-a-link/)
 to learn more about copying links.

3 A placeholder
---------------

Sometimes, when building up a calculation block, we don't have all the ingredients we need. We, therefore, need a structured and consistent plan for creating placeholders. These placeholders are temporary. Later in the process, we will replace them with links.

Core [Modelling Skill 3](https://www.financialmodellinghandbook.org/how-to-create-a-placeholder/)
 to learn more about creating placeholders

4 An input
----------

This one might make you uncomfortable. Most modellers know that separating inputs, calculations, and outputs is essential. And ultimately, all inputs will end up on a dedicated input sheet.

However, while building the model, it can be more productive to put the input next to the calculation. We have an automated process for relocating these inputs. Like placeholders, this is temporary. When the model is complete, we will replace these inputs with links.

See [Modelling Skill 10](https://www.financialmodellinghandbook.org/how-to-relocate-inputs/)
 to learn about relocating inputs.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--29.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/calculation-block-components#/portal/signup)