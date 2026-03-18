# Core modelling skill 7: Copying a calculation block

**Source:** https://www.financialmodellinghandbook.org/copying-a-calculation-block

---

Download the reference file to practice:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

When I introduced Core skill 5 (Creating a calculation), I recommended not to apply row anchoring in a calculation.

Row anchoring in a calculation makes it harder to copy the calculation block.

Compare these two examples.

Example 1 - Copying a calculation block where the elements are row anchored.
----------------------------------------------------------------------------

In this exercise, we want to copy the electricity generation block. Perhaps we want to add a calculation showing a P90 yield. (Don't worry if you don't know anything about "P50" or "P90" yields in renewables - they represent different probabilities of their being a certain amount of renewable energy resource).

In this first example, the modeller has row anchored each calculation element:

![](https://www.financialmodellinghandbook.org/content/images/public/images/6a002ae6-6486-4d0b-8ca3-537f90da10ec_2178x1368.jpeg)

The steps to copy the calculation block:

### Step 1: Select the rows we want to include

Shift + down arrow (native excel)

![](https://www.financialmodellinghandbook.org/content/images/public/images/da597702-36c6-4cea-8e9c-d214b1972311_2588x524.jpeg)

### Step 2: Select the whole rows, creating the copy areae

Shift + spacebar

![](https://www.financialmodellinghandbook.org/content/images/public/images/8f395973-c8f0-4099-b6df-6877cc91058d_2506x504.jpeg)

### Step 3: Copy the block

Ctrl + c (native excel)

### Step 4: Position your cursor where the top line of the copied version of the calculation block will be.

![](https://www.financialmodellinghandbook.org/content/images/public/images/4e0859bc-9264-464b-a904-077a1d0433be_2540x628.jpeg)

### Step 5: Select that row

Shift + spacebar (native excel)

![](https://www.financialmodellinghandbook.org/content/images/public/images/129cfdf7-d6c3-452f-9f2c-0a665c56c56b_2652x678.jpeg)

### Step 6: Paste the block

Enter

![](https://www.financialmodellinghandbook.org/content/images/public/images/944edad7-4dab-477e-97a4-1113902c241e_2670x820.jpeg)

When we trace precedents on the new calculation block, each element is still pointing back at the old block.

To use the new block we’d have to go through and edit each element of the formula. **This is not what we want.**

![](https://www.financialmodellinghandbook.org/content/images/public/images/60d2523e-905c-49d0-8957-cf6edd200139_2542x904.jpeg)

### Example 2: No row anchoring in the calculation

In this example, we start with this calculation block that has none of the element row anchored.

![](https://www.financialmodellinghandbook.org/content/images/public/images/d9e9668c-b11a-4b8e-b375-6a14c8b0723c_2282x1178.jpeg)

If we repeat the above steps, the result looks the same. However, when we trace precedents, we see that each block element refers to the new block's ingredients. They don't point back at the old block. We don’t have to do any editing to the formula. We just have to replace the ingredients.

**This is exactly what we want.**

![](https://www.financialmodellinghandbook.org/content/images/public/images/e3628e8a-15ad-4346-a267-d6db74897590_2468x908.jpeg)

We never know when we may want to copy one of our calculation blocks in the future. Therefore we set them all up without row anchoring to all be copyable.

Creating space for our copied calculation block
-----------------------------------------------

Sometimes we want to copy a calculation block and insert it between two existing blocks.

To do this, select the block following the steps outlined above.

When selecting the rows to copy, be sure to include a blank row.

![](https://www.financialmodellinghandbook.org/content/images/public/images/13c15663-f2bd-4bf2-ae55-c15b0e175bba_2788x932.jpeg)

Copy the block, then position your cursor on the row where the first row of the new block will be. In this case, this is "on top" of the existing block.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f7d6a5af-b8cd-45a9-b285-0e3dec7eb8fd_2600x896.jpeg)

If you press Enter at this stage, you'll paste over the top of the existing block.

Ctrl + shift + =

This will insert the correct number of rows and paste down the clipboard contents.

![](https://www.financialmodellinghandbook.org/content/images/public/images/f6945005-9471-4935-96c2-b68a810cd3a3_2836x1232.jpeg)

Note: In reality the keystroke is Ctrl and "plus" / "+".

On most keyboards, the plus symbol is on the shift position of the equals / = key; therefore, the full keystroke is Ctrl+Shift+=

* * *

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--149.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/copying-a-calculation-block#/portal/signup)