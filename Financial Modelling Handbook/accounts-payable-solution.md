# Modelling accounts payable - solution

**Source:** https://www.financialmodellinghandbook.org/accounts-payable-solution

---

* * *

Let’s take a step by step walkthrough of copying the Accounts receivable logic and adapting it for Accounts payable.

Step 1: New Section heading
---------------------------

Using Column A as usual.

![](https://www.financialmodellinghandbook.org/content/images/public/images/455b54c7-082e-49b1-bd74-e54c9058f71e_2214x1148.jpeg)

Step 2: Copy the Accounts Receivable logic
------------------------------------------

Use Skill 7: How to copy a calculation block.

In this instance, we will be copying a whole section with multiple calculation blocks.

First, we select the entire section:

![](https://www.financialmodellinghandbook.org/content/images/public/images/1af919a3-293b-4ca8-a689-0d5df535d162_2438x1182.jpeg)

Then we paste it down into our new Accounts Payable Section.

Note that we don't have enough space in the section. Therefore, we can Paste down the blocks that we have copied and create sufficient new rows. First, select the row, then paste and create rows using Ctrl+Shift+=.

![](https://www.financialmodellinghandbook.org/content/images/public/images/d8ce2c5c-01ff-43dc-81ce-2a6154b5a954_2254x1292.jpeg)

Step 3: Replace labels
----------------------

Leaving the rows selected, for now, we can quickly replace the text labels:

Ctrl+h to open the "find and replace" dialogue.

![](https://www.financialmodellinghandbook.org/content/images/public/images/7f59a3d4-46c8-43ee-81a5-978789266343_2084x1166.jpeg)

Then replace "receivable" with "payable".

If the rows are still selected, we will only run the search and replace on the selected rows.

Step 4: Review line items
-------------------------

We will need to make quite a few line-item replacements.

I have marked each line that I will need to change with an ugly green shade (Ctrl+Shift+r).

![](https://www.financialmodellinghandbook.org/content/images/public/images/e4e31814-41ca-411e-aff7-33f9cdf24ec0_2398x1132.jpeg)

This is a valuable step since it's common to be interrupted. And when I come back, I'll know that I still have line items to replace.

Step 5: Replace line items
--------------------------

The calculation structure is good; we just need to replace the links.

#### **Replace the link to Electricity Revenue in Row 105 with a link to O&M cost**

Use Skill 2: How to create a link.

![](https://www.financialmodellinghandbook.org/content/images/public/images/2c14f466-a313-4fbe-961a-da08b0f71c59_2196x1138.jpeg)

#### Replace the links to Electricity Revenue in rows 110 and 121 with links to O&M cost.

Use Skill  4: How to copy a link

![](https://www.financialmodellinghandbook.org/content/images/public/images/8bd50b20-2062-4c61-855e-3adc70be9c82_2424x1518.jpeg)

#### Replace the link to "Forecast accounts receivable balance" in row 111 with a link to  "Forecast accounts payable balance."

![](https://www.financialmodellinghandbook.org/content/images/public/images/758a9821-7119-47b2-b79c-05ee0fdac8bc_2462x908.jpeg)

#### Replace the link to "Accounts receivable balance BEG" in row 112 and with a link to Accounts payable balance BEG" from the new corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/public/images/b04f5845-fbbf-4a00-9863-834013d485a8_2488x908.jpeg)

#### Re-label "Cash received from invoices" to "Cash paid for operating costs POS".

We will sign switch this, so it's worth adding the POS already now. Since it will be sign-switched, the positive version will not be the line item exported to the cash flow statement. We should therefore remove the export marking - select the row (Ctrl+spacebar) and apply black font (Ctrl+Shift+b)

![](https://www.financialmodellinghandbook.org/content/images/public/images/408fd8cf-b694-4920-a62e-20e0d548ce98_2602x1326.jpeg)

Relink the download flow in the corkscrew to "Cash paid for operating costs POS."

![](https://www.financialmodellinghandbook.org/content/images/public/images/ce33db32-47fb-47e5-b0ee-82dbe2f7c16d_2656x1318.jpeg)

#### Create a new input on the input sheet for Accounts payable - initial balance

Then relink the new input into the corkscrew.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f0c9d4f4-409e-4155-a614-9495378ae874_2384x1352.jpeg)

We have systematically reviewed the calculation structure line by line and replaced all the ingredients.

Before wiring this calculation into our financial statements, the last step is to sign-switch the Cash paid for operating costs.

The quickest way to do this is to copy the sign switch line above for O&M costs:

![](https://www.financialmodellinghandbook.org/content/images/public/images/b9f084ba-8563-446f-90f3-dc51e1210d2d_2454x1522.jpeg)

Don't forget a quick Shift+F9 refresh, or the label will still read "O&M cost".

![](https://www.financialmodellinghandbook.org/content/images/public/images/ccf96459-66bc-41b2-a3b9-25fdb7a59d7a_2452x1496.jpeg)

We are now ready to add Cash paid for O&M costs to the cash flow statement:

![](https://www.financialmodellinghandbook.org/content/images/public/images/83f28a0e-3556-468c-9e96-de2b7a6c74e4_2398x946.jpeg)

And accounts payable to the balance sheet:

![](https://www.financialmodellinghandbook.org/content/images/public/images/5b02179f-32ce-4c7e-a4af-793950fa0aa7_2226x1546.jpeg)

The balance sheet will still show as not balancing until we do a complete recalculation of the model:

The balance sheet is now fully balanced.

![](https://www.financialmodellinghandbook.org/content/images/public/images/fc47a104-7ad0-4ee6-b633-7499169cd09a_2408x1288.jpeg)

As usual, we'll wrap up by running the Section Completion Checklist.

I found something I missed when I ran the checklist!
----------------------------------------------------

When I ran the Section Completion Checklist on my own modelling for this section, I noticed that I had not replaced the input of Accounts Receivable days with the correct input for Accounts payable days.

![](https://www.financialmodellinghandbook.org/content/images/public/images/5f66bda0-5d6d-4788-aa10-db9cb870ba97_2332x916.jpeg)

I considered amending the text of this page to include it in the steps above, but I think it's a perfect example of why we run the Section Completion Checklist. Had this been a real modelling job and I had not run the Checklist, I would have left this error in the model.

Lesson: Always run the checklist!
---------------------------------

Download the model completed to this point:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--140.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

* * *

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/accounts-payable-solution/#/portal/signup)