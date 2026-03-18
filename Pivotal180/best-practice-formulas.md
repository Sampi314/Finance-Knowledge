# Formulas You should Know for Working in Project Finance

**Source:** https://pivotal180.com/best-practice-formulas

---

[Skip to content](https://pivotal180.com/best-practice-formulas/#fl-main-content)

Best Practice Formulas
======================

By Haydn Palliser | March 13, 2024

### OVERVIEW

Gain some tips and tricks of best practice financial modeling in this extract from a Pivotal180 course.

Although in many ways obvious, these concepts are a useful reminder for experienced analysts and a priority for new analysts to learn.

**Video**

**Video Transcript**

In this video, we’ll discuss Pivotal180’s best practice guidelines for writing formulas into financial models. One key best practice for modeling is keeping the models’ inputs, outputs, and calculations on separate sheets. The best practices for formulas that we’ll cover in this lesson are most relevant to the calculation sheet, which is kind of the engine room of the model. It’s crucial that the formulas are not just accurate, but also easy to understand. And the two main goals of these best practices are, one, to ensure users and reviewers know what the formula is calculating, and, two, to easily identify errors. Let’s start by taking a look at an example of a bad formula. Ironically, it’s easier to identify best practices when they aren’t used at all. This formula calculates EBITDA, or earnings before interest, tax, depreciation, and amortization. For our example, EBITDA is essentially just revenue minus costs. Now, some of you might see this formula and think, “Wow, I have no idea what this formula is doing. “The modeler must be really advanced.” However, I’ll tell you upfront that this is really a pretty poorly constructed formula, so let’s see what Bastian thinks. Bastian, what can you identify in this formula that’s not ideal?

\-Well, for starters, I also don’t know what this formula is doing. It’s very unclear. It basically stretches all the way across the screen and has more components that I can count. We want to keep formulas short and simple. This formula is also linking to three different tabs. First, it links to a cell in the Price tab, then to a cell in the Volumes tab, and then some cells in the Cost tabs. What does Price!T341 even mean? Linking formulas across sheets make them hard to trace. Ideally, your formulas should only reference cells in the current tab. Another issue is that the formula references cells in multiple columns, both Column T and Column I. This is a potential red flag because we want to ensure formulas are referring to the correct time periods. The model should be structured so that every sheet has the same timing resolution. This means that if Column F refers to January through March, 2023, Column F should correspond to that period in every other sheet in the model, with the exception of some annual summary sheets. It’s then much easier to confirm your formula is referring to the correct timing period. Also, notice that the formula is multiplied by 1/10th at the end. This is called a hard code, and it’s definitely not best practice. We don’t know what 1/10th means or why it’s in the formula. Do not hard code numbers into your formulas, with the possible exception of some ones and zeroes. Instead, create another cell labeling the number, in this case, 1/10th, and reference that cell in the formula. Lastly, this row does not have a total column. We almost always want to build in a column to the left that sums the cells in that row. This also helps us identify errors. Now, remember, this formula might 100% accurate. The problem is that users will have a difficult time understanding it and identifying potential errors.

Now, here’s our good formula example. Note that this formula is also calculating EBITDA, and it’s coming up with the same result as the last formula for each year of 48.5 million. There are some key differences, though. First, this formula is really simple. It’s simply summing two cells, and because those two cells are on the same sheet, we can see their labels and units, so we know we’re adding revenue and the negative costs. Second, we can tell how different these formulas are just by the dimensions of the screenshot. The formula isn’t very long, but it requires many more rows. The good example formula actually requires seven rows instead of the one row in our bad example. The extra rows are because we are bringing information from other sheets over to this one instead of just linking to the other sheets in our formula. For example, rows 8 and 9 for price and volume are likely linked over from other sheets. And this may seem repetitive, but actually more calculation lines increases the model’s transparency. If it looks too cumbersome, you can always group and then ungroup rows. Additionally, Column E shows the total for each row. If you come, say, from an accounting background, you might be familiar with total columns on the right-hand side. In modeling, however, they’re located on the left. They’re on the left because we might build a model with dozens or even hundreds of columns, and it’s really inefficient to scroll that far to the right. Occasionally, the left-hand column will also calculate the net present value of the cells in that row instead, in addition to the sum. Also note that this example includes units for each row. Really simple but very important. Another important formula best practice is to only use one formula per row. We can’t see it in the screenshot, but Column F must have the same formula as Column J or as Column ZZ. Always drag the formula all the way across the row to ensure consistency. This is very important and bears repeating, never change the formula across a row. Finally, and perhaps the most important one is just to keep things simple, silly. Most models work with simple addition, multiplication, and subtraction. It’s simply high-school math. Just because you recently learned the index match formula doesn’t mean you need to use it on every line, and, believe me, I’ve seen that. Complicated formulas that less people understand should be used sparingly. The more people that understand our model, the better. And please, please don’t use embedded IF statements. An embedded IF statement is a formula such as =IFA1=1, IF, open brackets again. That’s just horrible. You can do one row with a first IF statement and a second row with the next, then add them or do whatever has to be done. Make it easy for your colleagues and friends, or you may find you don’t have any. Look, just keep it simple, simple enough for me to understand.

– Let’s summarize these key best practices made apparent by these example formulas. First, keep formulas short and simple. Use multiple rows if necessary. Second, never link formulas across sheets. Copy data from other sheets instead. Use the same timing resolution for all calculation sheets. Do not hard code numbers in your formulas. Create reference cells instead. Include row total columns and use easy-to-understand formulas. You’ll find these guidelines will help you review formulas and identify errors quickly. Good luck.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fbest-practice-formulas%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fbest-practice-formulas%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fbest-practice-formulas%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#8db2efe2e9f4b0e5f9f9fdfea8becca8bfcba8bfcbfde4fbe2f9ece1bcb5bda3eee2e0a8bfcbefe8fef9a0fdffeceef9e4eee8a0ebe2ffe0f8e1ecfea8bfcb)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/best-practice-formulas/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA