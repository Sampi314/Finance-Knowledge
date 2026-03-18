# Core modelling skill 2: How to create a link

**Source:** https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model

---

* * *

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

When we created the power tariff input, we expressed the value in USD / kWh.

The standard monetary unit in the model is thousands of dollars. We have modelled electricity generation in GWh. We, therefore, need conversion factors.

The conversion factors we need are already on the input sheet.

![](https://www.financialmodellinghandbook.org/content/images/2023/02/1-2.jpg)

We need to link to them to bring them into our calculation block.

### Step 1: Position yourself in Column E of the line item you want to link to.

![](https://www.financialmodellinghandbook.org/content/images/2023/02/2-1.jpg)

### Step 2: Copy the label

**Ctrl+c**

![](https://www.financialmodellinghandbook.org/content/images/2023/02/3-1.jpg)

### Step 3: Navigate to where you want to create the link.

![](https://www.financialmodellinghandbook.org/content/images/2023/02/4-1.jpg)

### Step 4: Create the link

**Ctrl+Shift+q**

![](https://www.financialmodellinghandbook.org/content/images/2023/02/5-1.jpg)

Ctrl+Shift+q triggers the "quick link" from the Productivity Pack macros. The macro knows when you create a cross-worksheet link and will mark the link as an import.

### Step 5: Copy the link across

**Ctrl+Shift+a**

![](https://www.financialmodellinghandbook.org/content/images/2023/02/6.jpg)

Ctrl+Shift+a triggers the "copy across" operation from the Productivity Pack macros. The macro knows when you are linking to a constant and will only copy across as far as the units column. As you'll see below, when you link to a series line item, Ctrl+Shift+a will copy all the way over the timeline.

Repeat the process for the other constant we need, units in a thousand.

![](https://www.financialmodellinghandbook.org/content/images/2023/02/7-1.jpg)

Further practice - creating a local link
----------------------------------------

We now want to link to electricity generation.

We will repeat the steps above, but this time we are linking to a line item that a. on the same sheet and b. is a series, not a constant.

The steps are the same, however.

### Step 1: Position yourself in Column E of the line item you want to link to

![](https://www.financialmodellinghandbook.org/content/images/2023/02/8.jpg)

#### Step 2: Copy the label

Control+c

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2023/02/9.jpg)

#### Step 3: Navigate to where you want to create the link.

![](https://www.financialmodellinghandbook.org/content/images/2023/02/10.jpg)

#### Step 4: Create the link

**Ctrl+Shift+q**

![](https://www.financialmodellinghandbook.org/content/images/2023/02/11.jpg)

Notice that this Quick Link macro knows that you are creating a link to a calculation on the same sheet - and therefore formats it in black rather than blue font.

#### Step 5: Copy the link across

**Ctrl+Shift+a**

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2023/02/12.jpg)

Notice that on this occasion, the copy across macro knows that you are linking to a series item and copies it all the way over the timeline.

What are the productivity pack macros actually doing?
-----------------------------------------------------

Both the "Quick link" and "Copy across" macros perform a series of steps that would be laborious to do by hand. However, it is helpful for you to know what steps the macro is performing.

### Paste link

The steps below list out what the macro is doing, and the keystrokes you would use if you did this operation manually. As you can see, the manual process involves a lot of steps that are automated by the macros.

**Step 1: Paste Special**

Alt, E, S

![](https://www.financialmodellinghandbook.org/content/images/public/images/4c69737e-f5b4-418c-8bc8-c8ee792c4baa_1026x858.jpeg)

**Step 2: Paste Link**

L (if paste special dialogue is active)

**Step 3: Fix row anchoring**

**Note:** See Skill 4 for more information on why links should always be row anchored

F2 (to enter edit mode), F4 twice to fix row anchoring.

**Step 4: Mark as import**

If the link is imported from another sheet, mark it as an import.

Ctrl+shift+m

### **Copy across**

Every time we create a link or write a formula, the next thing we want to do is copy it across the timeline.

Performing this manually without the copy across macro would involve the following steps. These are the steps that the macro is performing:

**Step 1: Copy the active cell**

Ctrl+c

**Step 2: Copy across the timeline**

Shift+Ctrl+right arrow

**Step 3: Return to the left of the timeline**

Home

**Step 4: Paste into the copied cells**

Enter

**Note:** Enter pastes the clipboard's contents, and clears the clipboard. Ctrl+v pastes the clipboard's contents but leaves the contents in the clipboard.

**Step 5: Return to the left of the timeline**

Home

**Step 6: Perform a local recalculation**

Shift+F9

Note - this calculates the active sheet only. It is a valuable check that what you have copied across is working as expected, without recalculating the whole model.

* * *

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--48.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model#/portal/signup)