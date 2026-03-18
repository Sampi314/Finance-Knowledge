# Why to avoid Daisy chains - linking to links

**Source:** https://www.financialmodellinghandbook.org/why-to-avoid-daisy-chains-linking-to-a-link

---

As we build up our model using calculation blocks, we will have lots of links in the model. In the last chapter, we saw that we could either copy an existing link or link back to the source.

In this chapter, we will talk about why we should never link to a link.

What do we mean by linking to a link?
-------------------------------------

In the last chapter, we copied the Operating Period Flag from row 37 of our calculation into our Operations and Maintenance cost block.

The original link in row 37 and the copied link in Row 43 both point back to the Timesheet.

If we had linked to the link, row 43 would be pointing to Row 37 rather than to the Timesheet.

![](https://www.financialmodellinghandbook.org/content/images/public/images/6c980ea1-2eea-40fc-bd2a-050a2a3d537e_2992x756.jpeg)

Row 43 points to Row 37: A link to a link or a “Daisychain”

Let's say we set our model with a series of links, all linking to each other.

Conceptually it would look like this.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e163617a-6a02-403e-866f-8497a9418595_1648x326.jpeg)

Each link points to another link, which points to another link. And so in through the chain.

All of the calculations in the chain would work fine until we want to delete something from the model.

Let's say we no longer need link B, and we decide to delete it.

![](https://www.financialmodellinghandbook.org/content/images/public/images/1c1dd37a-bea1-460f-b26c-46cebd8c8827_1622x368.jpeg)

The problem is that link B is part of a daisy chain of links. Usually, in a model, we have no visibility that a daisy chain of links exists. When we delete link B, the model instantly blows up with #REF errors everywhere

![](https://www.financialmodellinghandbook.org/content/images/public/images/a87e8deb-7947-4d89-9753-b7b9b32f9a7d_1646x324.jpeg)

Many of you will have had this experience. Models where you are terrified to delete anything because the model will blow up. This situation is usually caused by Daisy chains.

The other negative consequence of Daisychains is that the navigation that we have come to rely on using Ctrl+\[ no longer works.\
\
We are going to avoid this by avoiding daisy chains.\
\
If we always copy links rather than linking to them, they will all point back to the source calculation. Our navigation keystroke navigation will work well. We will also be able to delete code as we need to.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/42524432-6d91-47f2-b649-58abbd038d80_900x450.jpeg)\
\
All links point back to the source calculation - never to another link\
\
If we need to delete any of the links, the rest of the model is not affected. In this example, we can delete link B without links C, D, and E being affected.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/e6c97f4b-146a-4779-9bd3-43a040937a3e_892x440.jpeg)\
\
You can delete any link without any of the others being affected\
\
Productivity Pack inbuilt protection against Daisy chains.\
----------------------------------------------------------\
\
We have seen in Skill 2 that the quickest way to create a link is to use the Ctrl+Shift+q macro. If you try to create a link to a link, the macro will warn you.\
\
Let's say, instead of copying the link in row 37, I try to create a link to it.\
\
I follow my Skill2 process:\
\
First, I copy the label in E37.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/6870b082-4dc5-49f0-a9d1-1be11621652f_3096x804.jpeg)\
\
Copying the label of the row you want to link to is the first step in creating a link. See Skill 2\
\
I then come to where I want to put the link in row 43 and hit Ctrl+Shift+q.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/ee421c52-4b3c-4f72-adc7-796d77717428_2400x752.jpeg)\
\
The macro will warn you that you are about to create a daisy chain.\
\
The macro will warn me that a "possible daisy chain" is detected. The macro has seen that what you copied in row 37 was a link.\
\
The macro asks you if you'd like to create the link from the source rather than the link.\
\
If you say Yes, the macro will create the link but will link to the Operating Period Flag source calculation on the Timesheet. The macro will "look through" the link you are trying to copy and link to the source, thus avoiding the daisy chain.\
\
If you say no, the macro will create the daisy chain link.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/5585f053-0f46-49f3-8b57-aa88919e02a9_2726x1396.jpeg)\
\
We said yes and the macro created a proper “non daisy chained” link back to the source on the Timesheet\
\
* * *\
\
[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--123.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)\
\
Comments\
--------\
\
Sign in or become a Financial Modelling Handbook member to join the conversation.  \
Just enter your email below to get a log in link.\
\
 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.\
\
Sorry, comments couldn't be loaded. It looks like this account is not currently active.\
\
### Subscribe to Financial Modelling Handbook\
\
Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.\
\
[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/why-to-avoid-daisy-chains-linking-to-a-link#/portal/signup)