# Financial modelling productivity pack release notes

**Source:** https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-release-notes

---

  
Download the latest version from the [Productivity Pack download page](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)
.

Version 034c - Updated May 14th 2024
------------------------------------

Several bug fixes and the following updates:

### Input and Output relocation

*   Relocated inputs and outputs now match the formatting of the items being relocated.
*   An additional check has been added for the input relocation. If the name range "InputRowTemplate" is missing in the "InpC" tab, a warning message box will appear, prompting the user to provide a row number in the InpC tab to create the "InputRowTemplate".

### ChangeLog Enhancements

*   Increased flexibility to add more output stores in the "ChangeLog".
*   Ability to save outputs as hardcoded values using "Ctrl + Shift + 2". Fixes have been made to ensure hardcoded values are stored for newly added columns.
*   A dialogue box has been added, which automatically populates with the most recent changelog additions. This saves users from having to repeat previously added information.
*   Removed field restrictions for "Who requested the change" and "Any additional notes".

### Name Ranges Management

*   Added functionality to unhide and delete all name ranges. Please note that name ranges starting with "\_xlf" cannot be deleted through the "Utilities" pack and should be manually removed using Excel's Name Manager.

### End Cell References

*   Adjustments have been made to ensure stability when handling hidden columns.
*   If there are no hidden columns in the active sheet, the macro uses the “End Cell” to define the copy across the range.
*   If there are hidden columns and the end cell is beyond a hidden column, the copy across macro will copy to the last visible column. A warning will be given that the end cell is beyond the visible range.

* * *

Version 028e - Updated January 28th 2023
----------------------------------------

Several bug fixes plus the following new additions and updates:

New additions
-------------

### Avoid linking to blank cells when copying a link across

One of my training clients requested this change. When you're creating a link, and you link to the row label, then use Ctrl+Shift+a to copy across, you're left with links to blank cells.

![](https://www.financialmodellinghandbook.org/content/images/2023/01/1-7.jpg)

While they liked the calculation block structure and the use of links, they didn't like having these links to empty cells.

We have added a user setting that prevents the links to blank cells from being created. In the User Settings sheet, change the setting shown below to FALSE to have links operate in this way.

![](https://www.financialmodellinghandbook.org/content/images/2023/01/2-3.jpg)

This macro uses the Column Use definitions to determine which columns not to link to. Links to blank cells will be prevented in the Constants, Units and Totals columns and the blank column before the start of the timeline.

### Remove existing links to blank cells from

A new function has been added to the Ctrl+Shift+6 utilities that will remove links to blank cells from selected sheets. This allows users who do not want these links to remove them from an existing model.

Select Option 9 from the Prepare Model for Release list.

Updates
-------

### Change to sheet list in Ctrl+Shift+6 utilities

There was an issue with the Ctrl+Shift+6 utilities where there were hidden sheets in the model. The macros would unhide the sheets to perform an operation and then leave them unhidden.

We have updated the sheet list in the Ctrl+Shift+6 utilities to show which sheets are hidden and which sheets are protected. The use of square brackets around the section headings is pretty ugly, but unfortunately, the formatting choices in VBA dialogues are limited.

As well as giving more control over the functions that can be run across sheets, it's a useful way of seeing any hidden or protected sheets in your model.

![](https://www.financialmodellinghandbook.org/content/images/2023/01/3-2.jpg)

We've added buttons to make it easier to toggle between selecting all sheets and selecting and de-selecting hidden sheets that you may not want to perform a function on.

Protected sheets are always excluded from any of the processes.

Now, if hidden sheets are selected for an operation to be applied, they will be unhidden for the macro to run and returned to their hidden state at the end of the process.

* * *

Version 025d - Updated November 28th 2022
-----------------------------------------

In addition to numerous bug fixes, there have been several new additions to the Productivity Pack and updates to existing functionality.

New additions
-------------

### AI translation tool

Addition of a new keystroke allocation (Ctrl+Shift+4) to translate row labels. This is to allow easy translation of the labels in the model into another language.

See: [AI multi-language model translation](https://www.financialmodellinghandbook.org/ai-multi-language-model-translation/)

### Named Ranges report

A new report, accessed from the Model build utilities dialogue (Ctrl+Shift+6, M) will list all the Range Names in your model. This helps to identify Names containing errors, unused Names and hidden names.

See: [How to list all the Named Ranges in your model.](https://www.financialmodellinghandbook.org/how-to-check-for-range-name-errors-unused-names-and-hidden-names/)

The Named Ranges report can be used to select particular Names that you'd like to delete. This could be because they have errors, are not used or are hidden Names that you'd like to get rid of. Access from the Model build utilities dialogue (Ctrl+Shift+6, D)

See: [How to delete unwanted range names](https://www.financialmodellinghandbook.org/how-to-batch-delete-unwanted-range-names/)

### Unique formulas report

This shows a list of all unique formulas in the model. This can be useful when sending a model for audit. It's also a good checking tool for generally reviewing formula length etc. Access from the Model build utilities dialogue (Ctrl+Shift+6, O)

See: [How to list unique formulas in your model](https://www.financialmodellinghandbook.org/how-to-list-unique-formulas-in-your-model/)

Updates
-------

**Model columns defined in user settings.** Since not all models follow the column definition in base training models, column usage can be configured in user settings.

*   See [Productivity Pack user settings](https://www.financialmodellinghandbook.org/productivity-pack-user-settings/)
    

**Ctrl+shift+c** (clear shading) also clears sparklines.

**Update to keyboard shortcut configuration.** All macros listed with a drop-down for keystroke modifiers and the ability to selectively activate or deactivate specific macros.

*   See [Productivity Pack user settings](https://www.financialmodellinghandbook.org/productivity-pack-user-settings/)
    

**Improvements to conditional formats list.** The layout of the conditional formats report has been improved.

**Capitalisation check** doesn't require placeholders to follow capitalisation rules.  
  
**Used range list.** Updated to include sheet visibility, protection, count of formulas, error values, validations, format conditions. (add to model release checklist). The used ranges report is now added as a sheet in the active model - not as a separate workbook.

**Used row labels.** The report is now sorted in reverse order by number of occurrences of a label. This is used to check for duplicate row labels - potentially indicating that something is being calculated twice in the model, or that links have not been properly created. The report is now created as a sheet in the active workbook rather than in a new workbook.

* * *

Version 020a - Updated April 1st 2022
-------------------------------------

This update was "under the hood" code review & tidy up, and changes to ensure all shortcuts work on Excel for Mac.

### New keystrokes for Mac users.

All Ctrl+alt keystrokes on Windows are now Shift+Ctrl+Option on Mac.

### Windows keystroke change

Adding variance tabs was previously activated using Ctrl+Shift+3. This keystroke is not usable on Mac. We have therefore moved to Ctrl+Shift+9 on both Windows and Mac. Guidance on using this macro to follow as it's not yet been added to the handbook.

There is a known bug on the changelog macro Ctrl+shift+1. This will be addressed in the next version.

* * *

Version 18o - Updated March 16th 2022
-------------------------------------

### New: Add a Sparkline

Ctrl+shift+s

See [this guide on adding a sparkline to a calculation](https://www.financialmodellinghandbook.org/new-keyboard-shortcut-to-add-a-sparkline/)
.

Version 18n - Updated March 15th 2022
-------------------------------------

### Bug fixes & minor updates:

*   Reset end cell macro didn't clear out formatting.
*   Used Range report didn't correctly report last column in extreme cases
*   Adding to the capitalisation exceptions list now checks for duplicates and reports
*   Changing the sheet exceptions for import / export marking now autosave

* * *

Version 18m - Updated March 12th 2022
-------------------------------------

### Managing exceptions for import/export marking and capitalisation macro

Improvement to the interface to make it clearer which sheets were excepted for import marking and export marking.

*   [Managing import and export marking exceptions](https://www.financialmodellinghandbook.org/managing-import-export-marking-exceptions/)
    
*   \[Capitalisation checking\]

### Bug fix: Macros don't work on protected worksheets

Certain macros were not working where some sheets in the model are protected with a password.

* * *

Version 18j - Updated March 2nd 2022
------------------------------------

### Updated: Reset end cell

Ctrl+alt+c

This was not working consistently on all files. Works consistently now but further testing and user feedback across more file types will be useful.

### Updated: Sum of the row above

Shift+control+n

When the new is used in the constants column to give sum of the series values in the row above, it now also copies down the units from the row above.

### Update: Input relocation macro

Ctrl+alt+r

Now contains a dropdown for the sheet that you want to send the inputs to. Only asks once for constants, and once for series, in each session then defaults to those options for future relocation

Input relocation macro adds constants to the active case. Range name CASE\_ACTIVE is required to tell the macro which case is active.

### Update: Add to exceptions list

Ctrl+alt+e

Previously to add a sheet to the exceptions list, you had type the sheet name. There is now a dropdown to select the sheet name.

### Update: Label capitalisation check - "spell checker" type behaviour added

Previously the macro to check label capitalisation would make corrections all over the sheet without any user control. The macro will now make suggestions and allow the user to decide on a case by case basis, like a spell checker dialogue would.

* * *

Version 18d - Updated 22nd February 2022
----------------------------------------

### New: Unhide and hide the macros

Ctrl+shift+7

Previously when we wanted to hide and unhide the macros, we had to do it through the menus. We can now do this with Ctrl+Shift+7. This keystroke toggles the macro workbook between hidden and unhidden.

### New: Delete a worksheet

Ctrl+alt+-

Using F11 regularly to chart parts of your model leaves you with the need to delete sheets regularly. We have therefore added a shortcut for this. You will get the same "are you sure you want to do this" warning as would get using the menu commands.

### New: Reset the end cell

Ctrl+alt+c

The behaviour of this shortcut depends on where you are in the sheet:

*   If you are in column J or later, the shortcut will set the end column
*   If you are in column A through I, the shortcut will set the end row

![](https://www.financialmodellinghandbook.org/content/images/2022/02/1-14.jpg)

With a cell in column EA selected (at the end of the timeline) the macro will confirm that you want to clear all data from column EB onwards, setting column EA as the end column

![](https://www.financialmodellinghandbook.org/content/images/2022/02/2-10.jpg)

Running the same macro while in Call A56, the macro will confirm that you want to clear all date from row 57 onwards. 

### New: Add to output sheet

Ctrl+alt+o

You can only run this shortcut on constants or row totals. The macro will create a link to the selected item on the [Output sheet](https://www.financialmodellinghandbook.org/output-sheet-structure/)
.

You need to maintain a template row on your Output sheet, named "OutputRowTemplate". The [Handbook start file](https://www.financialmodellinghandbook.org/using-a-start-model/)
 has the correct range names for reference.

See also [this summary of the range names needed in your model for the macros to work.](https://www.financialmodellinghandbook.org/range-names-needed-for-productivity-macros/)

![](https://www.financialmodellinghandbook.org/content/images/2022/02/3-11.jpg)

Maintain a template row on your output sheet, named "OutputRowTemplate"

### Updated: Row total

Ctrl+shift+n

This keystroke has a new behaviour. When run in the Row Total column, it will add a row total as usual. If we run it in the Constants column, it will add a total of the line above as a constant and add "Sum of " & \[above row label" as the row label. It will copy the units from the row above.\
\
![](https://www.financialmodellinghandbook.org/content/images/2022/02/5-8.jpg)\
\
Ctrl+shift+n in the constants column adds the sum of the series line above\
\
We have added this because we regularly need to bring the total of a series row into the constants column to be able to perform further calculations using that total.  \
\
### Updated: Utilities dialogue\
\
Ctrl+shift+6\
\
This dialogue has been renamed from "Prepare for release" to "Utilities".\
\
**Changes to the dialogue**\
\
*   Select all button added for when we want to run a utility on all sheets.\
*   Shift+down arrow works to select ranges of sheets to apply the utilities.\
\
![](https://www.financialmodellinghandbook.org/content/images/2022/03/2022-03-02_05-31-56-1.jpg)\
\
The utilities have been grouped into three types:\
\
*   **Quick build.** These utilities help you get small build tasks done quickly, such as adding a new corkscrew or a new template sheet.\
*   **Prepare model for release.** These are a series of "tidy up" operations that can be run on selected sheets.\
*   **Model information.** These run on all sheets and return information about the model.\
\
New utilities have been added:\
\
*   **Collapse/expand all grouping.** This will toggle the grouping state on all selected sheets.\
*   **Change header.** This will change the print header across all selected sheets. Helpful in updating, for example, a Project Name across all sheets\
\
### Other changes\
\
*   The utility macro to reapply grouping no longer hides the rows after the "END" marker at the bottom of the sheet.\
*   Changelog. The spacing settings have changed on the control log (Ctrl+Shift+1). Spacer rows are only inserted between change log sections.\
*   We've made changing the keystrokes for macros easier by adding modifier keys to a dropdown menu. They previously had to be typed, which was error-prone.\
\
  \
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
Subscribe](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-release-notes#/portal/signup)