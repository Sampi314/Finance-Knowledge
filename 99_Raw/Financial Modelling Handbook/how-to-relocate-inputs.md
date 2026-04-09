# Core modelling skill 10: How to relocate inputs

**Source:** https://www.financialmodellinghandbook.org/how-to-relocate-inputs

---

* * *

Download the reference file to practice the steps below:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

The golden rule of modelling that everybody knows is to separate inputs, calculations and outputs.

However, when we are building up the calculations in our model, it can be helpful to add the inputs as we go, right there on the calculation sheet.

Think of this like working in "scratchpad" mode. We are sketching out what the calculation will be and what we need to perform it. There can be a discovery process in thinking through how the numbers work and how we will lay it out.

At this stage, I find it helpful to throw numbers down onto the page without worrying about structure too much. I'm still in thinking mode.

I still mark them as inputs as I go if I know they will be inputs. If I don't know that, or I know for sure that they will be a calculated ingredient later, I'll mark them as a placeholder.

![](https://www.financialmodellinghandbook.org/content/images/public/images/00626d35-f8f2-4fa0-9a06-69ef97cd46fc_938x297.jpeg)

Just adding the inputs on the calculation as I go . . . I’m still figuring out what inputs I need

Why not put them directly onto the input sheet?
-----------------------------------------------

**You absolutely can.** There is no problem doing this, and many people are more comfortable with this approach. If you find yourself coming out in a cold sweat at the thought of having inputs on your calculation sheet, even temporarily, ignore the rest of this chapter and move on.

I find, however, that it's often not until I've built up the calculation that I know what inputs I need. I'm comfortable therefore putting them with the calculation, knowing that I can relocate them quickly.

To me, the advantages are:

*   I separate the activities of building the calculation from time spent organising and structuring inputs. Once I know what inputs I have, I then spend the time organising them.
*   I don't spend time paging back and forward between the sheet I'm working on and the input sheet each time I add a new input to the calculation.

The relocation macro is faster than adding inputs to the input sheet by hand.

![](https://www.financialmodellinghandbook.org/content/images/public/images/05616f61-0d85-4f86-835d-96e1dfedb287_1112x274.jpeg)

The calculation is complete. I’m now ready to relocate the inputs.

How to relocate inputs.
-----------------------

Method 1 - Using the Productivity Pack Macros.
----------------------------------------------

### Step 1: Select the input or inputs you want to relocate.

The input relocation macro can relocate multiple inputs at once.

![](https://www.financialmodellinghandbook.org/content/images/public/images/6114fd5b-9808-40f1-b95c-85845e2c5109_1113x276.jpeg)

In this case, I have selected all three inputs. I could relocate them one at a time if I wanted.

Note that for the macro to work - you must be selected on an input that is properly formatted. You also need to have your input sheet set up in a specific way. [See this page for the range names you need](https://www.financialmodellinghandbook.org/range-names-needed-for-productivity-macros/)
.

### Step 2: Activate "Relocate input" macro

Ctrl+alt+r

### Step 3: Select the input sheet.

The macro will ask you which input sheet you want to move the inputs to. It will only ask you this once per session. The next time it will remember your choice and automatically move the inputs to that sheet.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4-9.jpg)

The macro will default to InpC as the sheet name. If your input sheet has a different name, you'll enter it here. The macro will remember your choice later.

Your calculation sheet will instantly look like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/98693200-e095-4509-845d-2d6c3da17088_1103x311.jpeg)

All inputs have been moved to the input sheet and replaced with row anchored links. (We’ll talk later about why links should be row anchored). The macro has coloured them blue since they are imported. (Again, we’ll come back to this).

The inputs are now located at the bottom of the input sheet and set up with a complete "Input scenario" structure.

The macro defaults to putting them at the bottom of the sheet as it has no way of knowing where you want to put them on the sheet.

![](https://www.financialmodellinghandbook.org/content/images/public/images/cc9d8146-10ed-4c16-8e6d-370d1b5881e4_1039x262.jpeg)

### Step 4: Look out for duplicates.

Given the number of inputs in a fully built model, creating duplicate inputs is easy. If this happens, replace the link you have just created with a link to the original input. Then delete the duplicate.

![](https://www.financialmodellinghandbook.org/content/images/public/images/ea43a8a9-eaac-46e0-972c-4803b08193ba_994x454.jpeg)

#### **Step 4: Move the inputs to where you want them on the input sheet.**

Now that you know what inputs you have, you’re better equipped to spend time organising them on the input sheet.

For this, you will need to select the input row (using Ctrl+Spacebar) then cut the input using Ctrl+x. Important: DO NOT COPY THE INPUT.

When you cut and move the input, all links pointing to that input will move with it.

![](https://www.financialmodellinghandbook.org/content/images/public/images/90c5e16c-fcfd-4356-af1d-5dff990856fe_1039x277.jpeg)

Consider grouping on the input sheet
------------------------------------

As you move your inputs around your input sheet, consider what the most useful grouping will be. This will vary from model to model. You'll also want to consider the users of the model and what grouping will make the most sense to them.

Use column A and B headings for section and sub-section headings.

Download the reference file after the inputs have been relocated:

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

Input sheet structure
---------------------

Note that in order for the input relocation macro to work, you need to have a template input line item on your input sheet. It must be named InputRowTemplate. The input relocation macro copies this template when relocating inputs.

![](https://www.financialmodellinghandbook.org/content/images/public/images/58bbe111-fa4c-4b4c-ad54-3a23d226dfc3_2598x1214.jpeg)

The start file provided has this Named Range already in it ready for you to use.

* * *

Method 2: Relocating inputs without the macro
---------------------------------------------

I have included this section because it's useful for you to know what the macro is doing and show you the number of steps that the macro cuts out. Also, not everybody can use the macros due to work admin rights restrictions.

There's no doubt that doing this manually is laborious.

### Step 1: Select the rows of the inputs you want to copy, copy the rows.

Shift+Spacebar, Ctrl+c

![](https://www.financialmodellinghandbook.org/content/images/public/images/41aedfeb-99af-48bb-b52d-452ab6daeaa2_2052x774.jpeg)

### Step 2: Go where you want to put them on the input sheet and paste the inputs down.

Shift+Spacebar, Enter

![](https://www.financialmodellinghandbook.org/content/images/public/images/547995b8-84ee-4cca-8cd1-08f02698c8a0_2458x576.jpeg)

### Step 3: Copy the "scenario" infrastructure from a nearby row on the input sheet.

Shift+right arrow to select, Ctrl+c

![](https://www.financialmodellinghandbook.org/content/images/public/images/cfc58506-254f-45f9-8e68-50aa89bf7d04_3254x1270.jpeg)

### Step 4: Paste it down next to your new inputs.

Shift and arrows to select, Enter

![](https://www.financialmodellinghandbook.org/content/images/public/images/8ed9111b-f08e-48ac-989a-47f7a47ed853_3278x1034.jpeg)

### Step 5: Copy the correct values into the scenarios.

Ctrl+c, Enter

![](https://www.financialmodellinghandbook.org/content/images/public/images/8dda6034-72c9-46c1-92eb-be4d5f54189c_3288x1248.jpeg)

### Step 6: Paste the scenario selection formula from a row above.

![](https://www.financialmodellinghandbook.org/content/images/public/images/759efa78-e74c-4c11-9cf5-556944fefd98_2794x1336.jpeg)

#### Step 7: Local recalculation to check the values.

Shift+F9

![](https://www.financialmodellinghandbook.org/content/images/public/images/d9ed5544-b2f4-44fb-b8ff-d3a474545f3f_2816x1258.jpeg)

### Step 8: Create links from the new inputs to the calculation sheet.

See [Modelling Skill 2](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)
 on creating links. You can paste the links over the top of the existing inputs on the calculation sheet.

* * *

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--127.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-relocate-inputs#/portal/signup)