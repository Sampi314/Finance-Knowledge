# Financial Modelling Productivity Pack macros

**Source:** https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-macros

---

Keyboard shortcuts are crucial to financial modelling productivity. While the list of keyboard shortcuts in Excel is extensive and valuable, it doesn't cover everything we need as modellers.

The Financial Modelling Productivity Pack was created by our modelling team at Gridlines. These add new keystrokes to speed up operations that we frequently perform.

Like the native Excel shortcuts, these are best seen, experienced and learned in context. I'm therefore going to introduce different shortcuts at different times throughout the book, depending on what we are trying to do. For reference, I have included a complete list of the Productivity Pack macros with instructions on what each one does in Appendix 1.

In this chapter, I will explain how to "install" the macros, how to customise them, and how to update them.

[Download the latest version](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)

-----------------------------------------------------------------------------------------------------------------

We are constantly updating and improving the macros. Use the link above to get the latest version and see release notes about updates.

To be notified when we release updates to the macros, as well as all other updates to the Handbook, subscribe here:

[Subscribe for updates](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-macros#/portal/signup/free)

Productivity shortcuts increase productivity AND consistency.
-------------------------------------------------------------

We use these productivity macros in our consulting practice. They not only increase the whole team's productivity but also increase the consistency across the team. For example - we mark inputs using Ctrl+Shift+i. If everybody in the team uses the same macro, all the inputs will have the same marking.

How the Productivity Pack works
-------------------------------

The Productivity Pack is a dedicated Excel workbook containing a series of macros. These macros do specific operations and are bound to additional keyboard shortcuts.

The Productivity Pack file must be open simultaneously with the Excel file / financial model you are working on.

As the macro file opens, a series of code instructions bind certain macros to specific keystroke sequences within Excel. Our default keystrokes might conflict with existing add-ins that you have in Excel. I'll show you later how to change the keystrokes.

Hidden file
-----------

We have saved the Productivity Pack as a hidden file. That means if you open the file - Excel will look like this. In short - it seems like nothing has happened:

![](https://www.financialmodellinghandbook.org/content/images/public/images/9c73185c-e9c0-4f81-9aac-95bdaaec9c6a_3354x2046.jpeg)

To see the file, you have to unhide it.

### How to unhide the Productivity Pack

Ctrl+Shift+7

Set and forget
--------------

The Productivity Pack needs to be open for the macros to work. But we don't want to remember to keep opening it every time we work in Excel. The good news is that we can tell Excel to open it for us automatically, in the background, without thinking about it.

How to automatically open the Productivity Pack whenever you start Excel.
-------------------------------------------------------------------------

### Step 1: Set up a folder somewhere permanent. Save the Productivity Pack file in that folder.

We will tell Excel to look in this folder each time it opens, and load up the file we save there.

Make sure it's a location that a) you do not relocate and b) no other file is stored in that folder as Excel will try to open every file stored there. I save mine in a folder directly on the C drive called Macros.

### Step 2: Tell Excel where to look

Go into File / Options, and under Advanced, scroll down until you find this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/d0b744fb-ea05-49a7-9e7d-160c537f2f20_1660x1360.jpeg)

Enter the file path to the folder you set up at Stage 1.

Now, whenever Excel opens, it will automatically look in this folder and launch any files that are stored there. Because we have saved the Productivity Pack as a hidden file, it will open and operate in the background without you having to do anything.

If you want to update to a later version of the Productivity Pack in the future, delete the old one in the folder, and save the new one there.

**Note: Do not put anything else in this folder.** Excel will open it automatically. If you store hundreds of versions of your model in there by mistake, it won't be pretty.

### No undo

The Productivity Pack operates by running a macro each time one of the keystrokes is pressed. There is no undo memory when Excel runs a macro. Therefore Ctrl+z will not work for any macro keystrokes. It will work for other native Excel shortcuts as usual.

However, none of the operations performed by the macros is difficult to undo by other means. For example - if you apply input formatting using Ctrl+Shift+i by mistake, you can clear shading using Ctrl+Shift+c. If you apply Import font marking using Ctrl+shift+m, you can apply black font colour again using Ctrl+Shift+b.

### How to customise Productivity Pack keystrokes

You may find that certain keystrokes clash with add-ins or macros that you are already using in Excel.

Therefore, we have designed the Productivity Pack so that you can customise every keystroke.

Unhide the Productivity Pack workbook.

On the Custom shortcuts tab, you will see a list like this:

![](https://www.financialmodellinghandbook.org/content/images/2022/11/1-18.jpg)

You can change both the modifier keys and the shortcut letter to suit your preferences.

Once you have made the change, hit Ctrl+Shift+7 to save the changes and rehide the Productivity Pack.

Pressing this button will rebind the macros to the new keys you have selected. These will remain changes in the future.

### Manual vs automatic calculation model

In [this chapter on calculation modes](https://www.financialmodellinghandbook.org/manual-or-automatic-calculation-mode/)
, I explained that the first workbook you open in an Excel session sets the calculation mode. If you have saved your Productivity Pack to open automatically as described above, it will be the first workbook opened in an Excel session.

By default, the Productivity Pack will set the calculation mode to Manual as this is how we prefer to work. This may not be how you like to work. If you want to change this, make the change to Automatic and hit Ctrl+Shift+7 to save the changes and rehide the Productivity Pack.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/1-19.jpg)

### Updates

We will continue to update the Productivity to add new features and fix bugs. Download the latest version at [https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)

Make sure to join the mailing list at financialmodellinghandbook.org to receive notifications when we release updates to the Productivity Pack and other additional content.

### Recap of things to remember about the Productivity Pack macros

*   The macros do not exist in the file you are working on. They only exist in the macro file itself.
*   The macros will only work when the macro file is open.
*   The macro file is saved as a hidden file. That way, you don't have to see it or think about it. If you want to make changes, you first have to unhide the file.
*   Undo will not work after a macro has been run.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--91.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-macros#/portal/signup)