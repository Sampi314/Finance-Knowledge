# Excel AutoCorrect: A Complete Guide + Time Saving Examples

**Source:** https://trumpexcel.com/autocorrect

---

[Skip to content](https://trumpexcel.com/autocorrect/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/autocorrect/#below-title)

What happens when you type the word ‘Drnik’ instead of ‘Drink’ in Excel?

You would notice that Excel will autocorrect that misspelled word to Drink (as shown below).

![Excel Autocorrect in Action](https://trumpexcel.com/wp-content/uploads/2014/05/Excel-Autocorrect-in-Action.gif)

Somehow, Excel knew that this is not the correct spelling and autocorrected it to the right one.

Now, it won’t autocorrect all the misspelled words.

Just a few!

For example, try the word ‘dirnk’.

It would not be auto-corrected.

The reason some words are autocorrected and others aren’t is because there is already a fix list of words that are prefilled in Excel to autocorrect.

Note: Autocorrect is enabled by default in Excel.

In this tutorial, I will explain what Autocorrect options are and then show you some examples where you can use it to save time. I will also cover how you can disable it (i.e., turn off autocorrect)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/autocorrect/#)

Understanding the Autocorrect Options
-------------------------------------

Autocorrect was created to help you iron out small issues you may face while typing in Excel or while doing [data entry](https://trumpexcel.com/data-entry-form/)
 (such as replacing some commonly misspelled words with correct words).

It also allows you to get some more control when using Excel (as we will see in the examples later in this tutorial).

But let’s first understand where are the autocorrect options and what is available by default.

To get the autocorrect options, click on the File tab.

![File Tab in Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20228%20161'%3E%3C/svg%3E)

In the File screen, click on ‘Options’.

![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20460'%3E%3C/svg%3E)

In the Excel Options dialog box, click on Proofing.

![Click on Proofing option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20765%20264'%3E%3C/svg%3E)

In the Proofing options, click on the Autocorrect Options.

![Click on the Autocorect Options Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20765%20264'%3E%3C/svg%3E)

This will open the Autocorrect Options dialog box.

![Autocorrect Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Let me explain the different tabs in the Autocorrect dialog box and the options in these.

### Autocorrect Options Tab

In the Autocorrect Options tab, there are some options that are enabled by default and take care of some common issues.

![Autocorrect Options tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

*   **Show Autocorrect Options buttons**: This one is not relevant for Excel but it is for other MS applications. When this option is enabled, you see the autocorrect options in MS Word or MS PowerPoint (as shown below).
*   **Correct two initial capitals**: This option when enabled will automatically correct the two capital initials in Excel. For example, if you type ‘HEllo’, it will automatically change it to ‘Hello’
*   **Capitalize first letter of sentences**: When enabled, this option ensures that a new sentence starts with a capital letter. For example, if you type, ‘Hello. how are you?’, it will be autocorrected to ‘Hello. How are you?’
*   **Capitalize names of days**: This will automatically change the first letter of the day name if you enter in lowercase. For example, _wednesday_ would be changed to _Wednesday_.
*   **Correct accidental use of Caps lock key**: In case you have the Caps lock on and you write a sentence, it will automatically correct the text and disable the Caps lock. For example, if you enter hELLO, it will automatically change it to Hello.
*   **Replace text as you type**: This is where Excel already has some commonly misspelled words (or shortcodes for some symbols). For example, if you type (c), it automatically gets converted into the [copyright symbol](https://trumpexcel.com/excel-insert-symbols/copyright/)
    . That is because it has been specified in the list in this option. You can add or remove words from the list (more on this in an example below).

#### Autocorrect Exceptions

While these autocorrect options are amazing, sometimes you may want it to not act super smart and correct these automatically.

For example, if you have the brand name ATs (where the ‘s’ is in lower case), Excel would automatically convert it into ‘Ats’.

While you like the autocorrect happening in all other cases, if you want to exclude this particular case, you can do that.

In the Autocorrect tab, click on the Exceptions tab.

![Autocorrect Exceptions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

In the Autocorrect Exceptions dialog box, you can have two types of exception:

1.  **First Letter**: By default, Excel capitalizes the alphabet after the period (dot). You can provide some exceptions here (there is already a list for common exceptions).
2.  **Initial Caps**: If you don’t want ATs to be converted to Ats, you can specify that here.

![Autocorrect Exceptions dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20283'%3E%3C/svg%3E)

### Autoformat As You Type Tab

This tab has three options (all of which are enabled). I find all these three options useful.

1.  **Replace as you type**: When you enter any hyperlinks in a cell, it would automatically be converted into a hyperlink. I sometimes disable this option as I often end up clicking the cell which then takes a few seconds and then opens the link in the browser.
2.  **Apply as you work**: This will automatically add new rows and columns in an [Excel Table](https://trumpexcel.com/excel-table/)
     when you enter anything in the cell adjacent to the one in the table.
3.  **Automatically as your work**: When you enter a formula in a column in an Excel Table, this option will enter the same formula (with [cell references](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     adjusted) into all the cells in the column.

![Autoformat as you type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

### Actions Tab

In Microsoft applications, you can create an action based on a specific word or text.

In Excel, there is only one type of action available – which is date action.

A date action means that if you have a date in a cell in Excel, you can right-click and you’ll get a few actions that you can take for that date (such as show that date in calendar or schedule a meeting in Outlook).

This could be useful if you have a list of dates and want to quickly save some in your calendar or want to schedule a meeting (using Outlook).

This option is disabled by default and you have to enable it to be able to use it in Excel.

![Autocorrect Actions option needs to be enabled](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Once enabled, you will be able to use it Excel. If you have a date in a cell, just right-click and you’ll find the actions options at the bottom.

![Date Action in Excel Autocorrect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20698'%3E%3C/svg%3E)

#### Math Autocorrect Tab

Just like you can insert symbols in an Excel cell (such as Delta, Degree, or [Checkmark](https://trumpexcel.com/check-mark/)
), you can also insert math symbols in an equation.

This tab has some text that automatically converts into the specified math symbol. For example, if you type \\sigma, it will replace it with the σ symbol.

![Autocorrect Math Symbols](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Note that this will not work in the cells in the worksheet. It only works with equations.

How to Add Your Own Words to Excel Autocorrect?
-----------------------------------------------

Wish there were some words that were a part of autocorrect?

For example, let’s say you want to add the word ‘drikn’ to autocorrect so that it corrects it to ‘drink’.

You can use the below steps to add a word to autocorrect:

1.  Click on the File tab.
2.  Click on Options.
3.  In the Options dialog box, select Proofing.
4.  Click on the ‘AutoCorrect Options’ button.
5.  In the Autocorrect dialog box, enter the following:
    *   Replace: **drikn**
    *   With: **drink![Autocorrect dialog box - replace with word](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)**
6.  Click ADD
7.  Click OK.

Now, when you type ‘drikn’ in Excel, it will autocorrect it to ‘drink’.

Before I show you some cool examples to use this, here are a few things you need to know about Autocorrect in Excel:

*   **Autocorrect list is case sensitive**. This means that you have added the word ‘drikn’ to be replaced by ‘drink’, it would only work with the lower case word. If you enter ‘Drikn’ or ‘DRIKN’, it will not be corrected.
*   This change is saved in Excel and would exist even if you close the workbook and open again. If you no longer want this, you need to go and delete it manually.
*   The change happens only when the exact word is used. For example, if you use ‘drikns’, it will not be autocorrected. For it to work, the word must not have characters just before or after it.
*   When you specify an autocorrect in Excel, it automatically gets activated in other MS applications such as MS Word or MS PowerPoint.

Autocorrect was created as a way to correct common spelling errors. But you can also use it in some awesome ways to save time.

**Related**: [Spell Check in Excel](https://trumpexcel.com/using-spell-check-in-excel/)
.

Below are some useful examples to use Autocorrect (other than correcting a misspelled word).

Example 1: Use Autocorrect to Complete Abbreviations
----------------------------------------------------

Imagine you work for a company ‘ABC Technology Corporation Limited’.

Your work involves a lot of [data entry](https://trumpexcel.com/excel-data-entry-tips/)
 in Excel and you have to manually type full company name many times in a day.

No matter how fast you type, this would feel like a waste of time.

Wouldn’t you wish there was a way where you can just enter ABC (or whatever you want), and excel replaces it with the company’s name?

This is where the awesomeness of Autocorrect can help.

You can specify an abbreviation in Autocorrect, and whenever you use that abbreviation, Excel would automatically convert that into the specified text.

For example, you can specify that whenever you type ABC, Excel should automatically replace it with ‘ABC Technology Corporation Limited’.

Something as shown below:

![Excel Complete Abbreviations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20336%20116'%3E%3C/svg%3E)

This happens when you add an autocorrect in Excel where ABC should be corrected to ” (as shown below in the autocorrect dialog box).

![Autocorrect Options to Change Abbreviations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

**What if you want to insert ABC and not the full name?**

In case you don’t want the autocorrect to change ABC to the full name, simply hit Control + Z to get back ABC.

While using Control + Z works, it’s best to choose an abbreviation which you’re unlikely to use in your work. This ensures there is no chance of you getting the full name by mistake (when all you wanted was the abbreviation text).

Below are some scenarios where this autocorrect trick can save a lot of time:

*   You can enter file names or folder names quickly (instead of copy-pasting it every time).
*   If you have a list of team members, you can use their initials to enter their names quickly.

A word of caution: Any autocorrect option you specify in Excel also get activates in other MS applications such as MS Word or MS PowerPoint. In such cases, it’s best to use abbreviations that you’re not likely to use anywhere else.

Example 2: Insert Symbols Quickly (such as Degree or Delta)
-----------------------------------------------------------

There are some symbols that are hard to insert/type in Excel as these are not already available on the keyboard (such as the [degree symbol](https://trumpexcel.com/degree-symbol-in-excel/)
 or the [delta symbol](https://trumpexcel.com/delta-symbol/)
 or [bullet points](https://trumpexcel.com/bullet-points/)
).

You either need to know the keyboard shortcut (which are often long and complicated) or need to use the Insert Symbol dialog box (which is time taking).

If there are some symbols you need to use quite often, you can use the Autocorrect feature to give these symbols a code name or abbreviation.

Now when you have to enter that symbol, you can simply use the code name and it will get autocorrected to that symbol.

Below is an example where I am using the code DEGSYM to get the degree symbol in Excel.

![Insert Degree Symbol using Autocorrect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20428%20200'%3E%3C/svg%3E)

To do this, make the following change in the Excel Autocorrect dialog box:

![Inserting Symbol using Autocorrect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Example 3: Write Formulas Faster with Autocorrect
-------------------------------------------------

This trick (which I learned from [this blog](https://chandoo.org/wp/write-faster-formulas-with-auto-correct/)
) is a little far-fetched, but if you work with a lot of long formulas, this can save you some time.

Below is a [formula](https://trumpexcel.com/excel-functions/)
 that will combine the text of the three cells that are left to the cell in which this formula is used.:

\=[INDIRECT](https://trumpexcel.com/excel-indirect-function/)
(ADDRESS(ROW(),COLUMN()-3))&INDIRECT(ADDRESS(ROW(),COLUMN()-2))&INDIRECT(ADDRESS(ROW(),COLUMN()-1))

Now if you often need to create a formula such as this, it’s better to create a simple code for it and use it in Autocorrect.

In this case, I have used the code ‘com3’ in autocorrect to get the formula.

![Autocorrect for formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Now, you can use the code ‘com3’ to get the entire formula in a few keystrokes (as shown below):

![Autocorrect to write formulas faster](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20448%20244'%3E%3C/svg%3E)

Note: As I mentioned, this is something most of you would never have to use, but it’s still a good trick to know (just in case). The above example is a real-life case where I am currently using this in one of my projects to save time.

How to Turn OFF Autocorrect Completely
--------------------------------------

While I believe autocorrect is a great feature, it may not be relevant for everyone.

And in some cases, it may actually be an irritation. For example, if you type (c) or (r) or ™, Excel autocorrect is going to change the text automatically (into © or ® or ™)

In such cases, it’s best to turn off autocorrect, or at least delete the terms that you don’t want to be autocorrected.

Below are the steps to turn off autocorrect:

1.  Click on the File tab.
2.  Click on Options.
3.  In the Options dialog box, select Proofing.
4.  Click on the ‘AutoCorrect Options’ button.
5.  In the Autocorrect dialog box, within the Autocorrect tab, uncheck the ‘Replace text as you type’ option.

![Uncheck replace text as you type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

Note: The above steps would completely turn off the autocomplete feature where it replaces some text with the specified text. This may also mean that those commonly misspelled words will no longer be corrected.

How to Disable/Replace Some Words from Getting Autocorrected
------------------------------------------------------------

If you want to keep the overall ‘Replace text as you type’ feature but want some exceptions, you can find the word in the list and delete it manually (or edit it).

Below are the steps to do this:

1.  Click on the File tab and then click on Options (in the File screen that opens).
2.  In the Options dialog box, select Proofing.
3.  Click on the ‘AutoCorrect Options’ button.
4.  In the Autocorrect dialog box, within the Autocorrect tab, select the word that you want to delete.
5.  Click the Delete button.

![Delete a word from Excel Autocorrect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

You can also replace a word in Autocorrect. For example, instead of (c) turning into the copyright symbol, you can use it to be converted into the word – copyright.

To replace the word with some other text, find and change the text and then click on Replace button.

![Replace the autocorrect word](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20413%20515'%3E%3C/svg%3E)

How to Undo Autocorrect Changes in Excel
----------------------------------------

If you write something and Excel changes it because of autocorrecting, you can get back the original text by hitting Control + Z.

For example, as soon as you type (c) in a cell in Excel and press the space key, it will instantly be converted into the copyright symbol.

But if you now use Control + Z, it will go back to being (c) and would remain that way.

While Autocorrect is a feature which most of the Excel users will never have to tweak, it’s good to know some ways you can use it to save time (as shown in the examples).

I have lately started using it for some formulas that are quite huge but I use these often (as shown in example 3).

**You May Also Like the Following Excel Tutorials:**

*   [How to Create an Excel Drop Down List](https://trumpexcel.com/excel-drop-down-list/)
    .
*   [How to Insert Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [How to track changes in Excel](https://trumpexcel.com/track-changes-in-excel/)
    .
*   [Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

9 thoughts on “Excel AutoCorrect: A Complete Guide + Time Saving Examples”
--------------------------------------------------------------------------

1.  Now a days many small enterprises need to GST billing and Primary accounting software, so please available this type of excel software.
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-11360)
    
2.  Sumit, excellent tutorial, I learned several new topics altough I use autocorrect a lot. And I really appreciate that it works in MS Word to. I have found it a bit cumbersome to add new entries. This can be easily simplified with a small vba macro. I have also made a small macro which backups or restores all autocorrect entries. because, yes I lost them all once and was not able to restore them.
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-11358)
    
3.  Your free lessons have taught and help me a lot in my line of work. Thanks so much for sharing.
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-11357)
    
4.  Nice! Thank you for the tip.
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-10688)
    
5.  autocorrect isn’t entirely case insensitive though:  
    ABotU will be corrected to ABouT
    
    lower case will correct upper case but not the other way round, which can be a useful way to avoid cases where you DON’T want it to happen
    
    you can also play amusing tricks on your friends by autocorrecting “I” to “The Dark Lord” for instance – how they’ll laugh!
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-10651)
    
6.  A very impressive trick Sumit
    
    I use “ii” for “=INDEX(ResCol,MATCH(LookupVal,LookupCol,))” – cos INDEX-MATCH just isn’t as intuitive as VLOOKUP – then I just need to double click each placeholder (eg “LookupVal” and then click its replacement in the spreadsheet  
    similarly, “iii” is “=INDEX(ResArea,MATCH(LookupVal,LookupCol,),MATCH(LookupVal,LookupRow,))” – for a two-way lookup  
    “tt” is “=IF(N(ref),TIME(ref %,MOD(ref,100),),)” – this converts the stupid time formats that SAP sometimes gives us
    
    jim
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-10650)
    
7.  Another thing to note is that this same shortcut will now exist in any of your MS programs – so typing “ABC ” in word, will also input that same company name in.
    
    You could also use characters that are not actually part of the name to be sure that you always really mean for the shortcut to work that way. For instance, I have done this at my workplace, creating a shortcut to our company name using company initials and some periods “S..K” (so that if I ever have cause to type SK, I don’t have Excel, Word or Outlook trying to auto correct).
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-1392)
    
    *   Good Suggestion.. Better to use characters that you are unlikely to use in normal course.. Thanks for sharing!!
        
        [Reply](https://trumpexcel.com/autocorrect/#comment-1393)
        
8.  Aya! so now I know how to save my time for typing something the same. Tks 4 your share.
    
    [Reply](https://trumpexcel.com/autocorrect/#comment-1380)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/autocorrect/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK