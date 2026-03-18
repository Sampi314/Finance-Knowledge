# Why we use placeholders

**Source:** https://www.financialmodellinghandbook.org/why-we-use-placeholders

---

When we’re building a model, we never start with a nicely ordered information folder providing us with all the data we need. Requirements and assumptions evolve during the model build process.

Remember back to the "conceptual model" we talked about earlier. We need to know what goes into a calculation before starting. Although we may know how to calculate something, the ingredients we need are often themselves calculations. And we may not yet have modelled those items.

We need the ability to hack in temporary lines that we will come back and fix later. We call these placeholders.

Now, just saying to ourselves, "I'll need to remember to come back and fix this later", is not enough. You will forget. And then you'll send out your model with your unmarked hack in it. And you'll look like a fool.

I don't want you to look like a fool.

So I'm going to give you a foolproof method for making your hacks so that you don't have to remember. Your model will show you all the places you told yourself you'd come back and fix.

Let's look at an example.

Suppose I'm building up this calculation block for electricity generation.

I know that solar panels degrade over time. I also know that I will need to adjust the generation for seasonality since the sun shines more in the summer than in the winter.

My first version of my calculation block looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/5d8499cd-055e-487d-b66c-093ddeeb2c0c_2878x896.jpeg)

I know I need degradation and seasonality adjustments, but I haven't modelled them yet. So I put in placeholders.

The formatting is deliberate:

The bright yellow is there to make the placeholders immediately noticeable when we look at the block. The formatting is deliberately ugly so that we don't miss it.

We have borrowed a technique from the lawyers and put square brackets around the row label. Square brackets do two things. They are another visual indicator that the line item is temporary. More importantly, we can search for square brackets before sending out our model. We can be sure we will find all the placeholders that we told ourselves we'd come back and fix later, without having to remember where they all are. The model is self documenting.

The placeholders allow us to complete the calculation block at hand, even though we don't have all the ingredients ready yet.

We can use the output of this block - electricity generation, in other calculations. We know the numbers are wrong, but we are just worried about the calculation structure at this stage. We'll worry about the numbers later.

(By the way - the numbers are always wrong. As the old saying goes - all models are wrong, some are useful).

Once we have modelled the ingredients, we can replace the placeholder with a link to the calculated component. We don't have to update the formula in the calculation block.

![](https://www.financialmodellinghandbook.org/content/images/public/images/8e648a44-4b7a-4b73-9787-195fe98b4f7b_2882x1126.jpeg)

In [Core Modelling Skill 3](https://www.financialmodellinghandbook.org/how-to-create-a-placeholder/)
, we will look in detail at the keystrokes to quickly create a placeholder.

And you'll see them used throughout our model build case study in [Part 4](https://www.financialmodellinghandbook.org/we-are-ready-to-start-building-our-model/)
.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--121.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/why-we-use-placeholders#/portal/signup)