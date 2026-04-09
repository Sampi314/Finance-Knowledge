# Range names needed for Productivity macros

**Source:** https://www.financialmodellinghandbook.org/range-names-needed-for-productivity-macros

---

The macro code, therefore, references Range Names to find the sections it needs. There are quite a few required Range Names and it will seem like a lot to set them up manually. However, the template [Start Model](https://www.financialmodellinghandbook.org/using-a-start-model/)
 already has the names in it. If you start your model build using this file, or a version of it, you won't have to add these names yourself.

[Download the latest version of the modelling productivity macros](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)
.

* * *

Input relocation
----------------

Ctrl+alt+r

### Used range: CASE\_ACTIVE

When the input relocation macro runs, it places the input bring relocated into the correct column for the active input case. It, therefore, needs to know which case is active.

The input which is driving the active input chase should have the range name CASE\_ACTIVE

This is often cell F4 in our standard input structure but, of course, may not be.

![](https://www.financialmodellinghandbook.org/content/images/2022/03/1.jpg)

### Used range: InputRowTemplate

The input relocation macro also needs to know the structure of the standard input row. The scenario input structure should have a template line named InputRowTemplate. See the [reference start model](https://www.financialmodellinghandbook.org/using-a-start-model/)
 for an example of how this should be set up.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/03/2.jpg)

* * *

Quick build corkscrew - no initial balance
------------------------------------------

Ctrl+shift+6, Q

### Used range: Corkscrew\_NoBal

The macro to quickly build a corkscrew without an opening balance will use the corkscrew where the name has been applied as a template. If this name is missing from the active file, the corkscrew will still work but the corkscrew will not be a match to the template corkscrew in your Tmp file.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/4-1.jpg)

Quick build corkscrew - with initial balance
--------------------------------------------

Ctrl+shift+6, W

### Used range: Corkscrew\_withBal

This operates in the same way as the template for the corkscrew without an initial balance. Note, if the range name is used, and there is a flag in the named, template corkscrew, this will be copied into the quick build version.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/5-1.jpg)

* * *

Add value to output sheet
-------------------------

Ctrl+alt+r

### Used range: OutputRowTemplate

This is similar to the Input row template. The macro to add a new constant or row total to the output sheet needs the structure of a standard output track sheet row. See the [reference start model](https://www.financialmodellinghandbook.org/using-a-start-model/)
 for an example of how this is set up.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/03/3.jpg)

* * *

Add output track
----------------

Ctrl+shift+5

The macro to add a new stored output set to the output sheet uses several named ranges.

### Used range: TrackStoredResults

This is used to tell the macro the numbers of the stored output sets. The macro will give the newly added output set a higher number. Note that the range must include the spacer columns - shown as M and O in the Start File.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/6-1.jpg)

### Used range: TrackActive

The macro uses the number of the active track to reset the output sheet after the track has been added.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/7-1.jpg)

### Used range: TrackLiveResults

This should cover the entire range of the live outputs from the model, and should include the space rows at the top and bottom of the range. This tells the macro which results should be copied into the new stored output track.

![](https://www.financialmodellinghandbook.org/content/images/2022/04/8.jpg)

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--63.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/range-names-needed-for-productivity-macros#/portal/signup)