# Advanced linking

**Source:** https://www.financialmodellinghandbook.org/advanced-linking

---

* * *

What's covered in this chapter:

*   Combining link navigation with link creating to get super-efficient
*   Linking to multiple line items at once.

* * *

When there are a lot of links in our model, navigating around the model becomes very efficient. As a quick refresher, to navigate using links, we can either use the built-in Excel keystrokes:

Ctrl + \[ to jump back on a link then F5, Enter to return\
\
Or we can use the Productivity Pack keystrokes:\
\
Ctrl+Shift+j to jump back on a link and Ctrl+Shift+k to return\
\
We've also seen that the sequence to create a link is:\
\
Ctrl+c on the label of the line item we want to link to\
\
Ctrl+Shift+q to create the link at the desired destination\
\
Ctrl+Shift+a to copy the link across.\
\
Combining navigating using links with link creation\
---------------------------------------------------\
\
We can combine these two skills to get very efficient at creating cross worksheet links.\
\
In this example, we have modelled revenue and linked it to the financial statements. We now want to do the same with Operations and Maintenance cost (O&M cost). O&M cost has already been sign switched as is ready to go.\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/75b60873-c704-4cfb-9c72-31ff00d509a8_2866x850.jpeg)\
\
Imagine we are starting the process while looking at the financial statements. We have a link to revenue already, and a placeholder for O&M cost:\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/06fff755-d894-49a2-97b8-686dd07ffdf4_2878x1238.jpeg)\
\
#### **Step 1:** Use the revenue link to hop back to the Ops sheet\
\
Ctrl+Shift+j\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/e7de6dd5-d398-4f55-bdec-bf015a748952_2572x866.jpeg)\
\
You'll land on revenue. Move down to Operating Cost.\
\
### Step 2: Copy the label of Operating costs (the first step in our link creation process\
\
Ctrl+c\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/ad066830-9835-4f7e-9ebe-a5c6a48a98aa_2484x842.jpeg)\
\
### Step 3: Hop back to the financial statements\
\
Ctrl+Shift+k\
\
You'll land back on revenue on the financial statements. Move down to the O&M cost placeholder.\
\
### Step 4: Create the link\
\
Ctrl+Shift+q\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/92b81475-2ae7-485a-b11f-11f32ed7a2cd_3028x960.jpeg)\
\
#### Step 5: Copy the link across\
\
Ctrl+Shift+a\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/59eacaf8-4f64-4b83-943e-846a8a9e28f0_3168x946.jpeg)\
\
In this example, because we are replacing a placeholder with a link, we will also want to clear out the placeholder yellow shading. We can clear shading with Ctrl+Shift+c\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/5a0832b2-b71e-46bc-bf20-138afc4e8054_3008x860.jpeg)\
\
Linking to multiple line items\
------------------------------\
\
We have created the Ctrl+Shift+q "Quick link" macro so that it can link to multiple line items simultaneously.\
\
In this example - we have four inputs for seasonability adjustment. We want to create links to all four in our revenue calculations.\
\
### Step 1: Select all four items\
\
Shift+down arrow to select the range\
\
### Step 2: Copy the labels\
\
Ctrl+c\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/eb7f0a75-ffa7-4f1a-926e-9f0b0653160e_1246x386.jpeg)\
\
### Step 3: Navigate to where we want to put the links & Create the link\
\
Ctrl+Shift+q\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/5098f269-7fd4-4e7c-b20e-b65c49f857a0_2308x704.jpeg)\
\
The macro will create 4 row anchored links, ready to be copied across. Note that the macro will apply the correct import formatting if required.\
\
### Step 4: Copy across\
\
Ctrl+Shift+a\
\
![](https://www.financialmodellinghandbook.org/content/images/public/images/4ecb4c2f-38af-4732-ac85-7eabbf8fc886_2460x638.jpeg)\
\
The "copy across" macro will copy all four line items over simultaneously. If you are linking to a constant, the macro will only copy across as far as column H. If you are linking to a series line item, the macros will copy over to the end of the timeline.\
\
* * *\
\
[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--172.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)\
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
Subscribe](https://www.financialmodellinghandbook.org/advanced-linking#/portal/signup)