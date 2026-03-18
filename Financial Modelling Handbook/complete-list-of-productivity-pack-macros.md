# Complete list of productivity pack macro functions

**Source:** https://www.financialmodellinghandbook.org/complete-list-of-productivity-pack-macros

---

Some references before you start:

*   [Download the latest version of the macros](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack/)
    
*   [Guidance on setting up the macros](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-macros/)
    
*   [Customising the macros and changing the settings](https://www.financialmodellinghandbook.org/productivity-pack-user-settings/)
    
*   [Release notes for the latest version of the macros](https://www.financialmodellinghandbook.org/financial-modelling-productivity-pack-release-notes/)
    

Hide / Unhide macros
--------------------

Ctrl+shift+7

The macros file is designed to run in the hidden state. To make changes to any of the keystrokes or settings, you'll first need to unhide the file.

When you are done making any changes, rehide with the same keystroke.  

Workflow actions
----------------

### Apply placeholder square brackets

Ctrl+shift+t

Adds placeholder square brackets to text in the selected cell.

*   [Why we use placeholders](https://www.financialmodellinghandbook.org/why-we-use-placeholders/)
    
*   [Core modelling skill 3: How to create a placeholder](https://www.financialmodellinghandbook.org/how-to-create-a-placeholder/)
    

### Create list of placeholders

Ctrl+alt+p

Creates a list of all line items in the model which have been marked as a placeholder.

*   [How to create a list of placeholders](https://www.financialmodellinghandbook.org/how-to-create-a-list-of-placeholders/)
    

### Jump to precedent/return from precedent

Ctrl+shift+j / Ctrl+shift+k

Intended to be used on links, for quick navigation/movement around the model. Replacement for the native Excel keystroke Ctrl+\[ which doesn't work on non-QWERTY keyboards.\
\
*   [How to navigate using links](https://www.financialmodellinghandbook.org/how-to-navigate-using-links/)\
    \
\
### Quick link\
\
Ctrl+shift+q\
\
Creates a link to a previously copied cell, whose address is currently on the clipboard.\
\
*   [Calculation block components](https://www.financialmodellinghandbook.org/calculation-block-components/)\
    \
*   [How to create a link](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)\
    \
\
### Quick sum\
\
Ctrl+shift+n\
\
The quick sum function has two behaviours. It adds a row total if used in the row totals column. It adds a total of the time series line above if used in the constants column.\
\
*   [How the row total macro is used when creating a new calculation](https://www.financialmodellinghandbook.org/creating-a-new-calculation/)\
    \
*   \[Addng a sum of the time series row above\]\
\
### Relocate inputs\
\
Ctrl+alt+r\
\
This moves inputs that have been added to calculation sheets to the selected input sheet, and replace them with a link.\
\
Note that your model needs the constant input sheet structure for this week, including a specific range name.\
\
*   [Skill 1: How to add an input](https://www.financialmodellinghandbook.org/how-to-add-an-input-to-an-financial-model/)\
    \
*   [Skill 10: How to relocate an input](https://www.financialmodellinghandbook.org/how-to-relocate-inputs/)\
    \
*   [Range names needed for productivity macros](https://www.financialmodellinghandbook.org/range-names-needed-for-productivity-macros/)\
    \
\
### Relocate outputs\
\
Ctrl+alt+o\
\
This adds either a constant or a row total to the output tracking / analysis sheet.\
\
*   [Skill 12: How to track outputs](https://www.financialmodellinghandbook.org/how-to-track-financial-model-outputs/)\
    \
\
### Anchoring\
\
Ctrl+alt+a\
\
This allows the batch changing of the row and column anchoring settings on a range of cells.\
\
*   \[How to change anchoring settings on a range of cells\]\
\
### Paste value\
\
Ctrl+alt+d\
\
This is a direct replacement for the native "paste special" keystroke. The purpose is to avoid having to remember and press a series of keys.\
\
*   [Making "paste value" and "paste format" easier](https://www.financialmodellinghandbook.org/making-paste-value-and-paste-format-easier/)\
    \
\
### Paste format\
\
Ctrl+alt+s\
\
This is a direct replacement for the native "paste special" keystroke. The purpose is to avoid having to member and press a series of keys.\
\
*   [Making "paste value" and "paste format" easier](https://www.financialmodellinghandbook.org/making-paste-value-and-paste-format-easier/)\
    \
\
### Add model query / feedback\
\
Ctl+alt+q\
\
This opens a dialogue box to allow structured commenting in the model. It's intended for people who are reviewing the model to leave comments or questions. These are different than placeholders which are intended to indicate temporary line items.\
\
*   [Structured commenting and feedback for financial model review](https://www.financialmodellinghandbook.org/structured-commenting-and-feedback-for-financial-model-review/)\
    \
\
### Delete worksheet\
\
Ctrl+alt+- (minus)\
\
This is a direct replacement for the native excel shortcut sequence. The purpose is to avoid having to member and press a series of keys. The same warning will be given when it's used. We use the F11 quick chart frequently which creates a need to quickly delete the charts we created.\
\
*   [Skill 11: How to create a quick chart](https://www.financialmodellinghandbook.org/how-to-quickly-add-a-chart-in-excel/)\
    \
\
### Expand / Collapse group\
\
Ctrl+e / Ctrl+shift+e\
\
These keystrokes are to allow quicker "expending" and "collapsing" of grouped rows.\
\
*   [Using grouping to see the big picture](https://www.financialmodellinghandbook.org/using-grouping-to-see-the-big-picture/)\
    \
\
### Manage exceptions list\
\
Ctrl+alt+e\
\
There are times when we do not want certain of the macros to perform their default behaviours. This keystroke opens up a dialogue to manage exceptions. These are specifically around sheets that we do not want import or export marking on, and words that will not follow the default capitalisation approach.\
\
*   [Managing import / export marking exceptions](https://www.financialmodellinghandbook.org/managing-import-export-marking-exceptions/)\
    \
*   [How to check and correct label capitalisation](https://www.financialmodellinghandbook.org/how-to-check-and-correct-label-capitalisation/)\
    \
\
### Reset end cell\
\
Ctrl+alt+c\
\
If this keystroke is activated in any of the time series columns, it will reset the end column. If it's used in any of the columns before the time series, it will reset the end row.\
\
*   [How to check and reset the used range and end cell in your model](https://www.financialmodellinghandbook.org/how-to-check-and-reset-the-used-range-in-your-model/)\
    \
\
### Add to change log / Save change log values\
\
Ctrl+shift+1 / Ctrl+shift+2\
\
These keystrokes automate the process of adding to a model change log.\
\
*   [How to track changes in your financial model](https://www.financialmodellinghandbook.org/how-to-track-changes-in-your-financial-model/)\
    \
*   [How to set up a Change Log sheet in your model](https://www.financialmodellinghandbook.org/setting-up-the-change-log-sheet-in-your-model/)\
    \
\
### Create variance tabs\
\
Ctrl+shift+3\
\
Variance tabs allow more detailed comparative analysis on targetted sections of the model.\
\
*   [Comparative analysis using variance tabs](https://www.financialmodellinghandbook.org/how-to-analyse-model-differences-using-variance-tabs/)\
    \
\
### Create output track\
\
Ctrl+shift+5\
\
This adds a new column to the output track sheet and saved the current values as a new tracked output case.\
\
*   [Output sheet structure](https://www.financialmodellinghandbook.org/output-sheet-structure/)\
    \
*   [Core modelling skill 12: How to track financial model outputs](https://www.financialmodellinghandbook.org/how-to-track-financial-model-outputs/)\
    \
\
### Add a sparkline to a calculation\
\
Ctrl+shift+s\
\
This adds a sparkline in the constants column (usually column F) for a time series calculation.\
\
*   [How to add a sparkline to a calculation](https://www.financialmodellinghandbook.org/new-keyboard-shortcut-to-add-a-sparkline/)\
    \
\
### Translate row labels\
\
Ctrl+shift+4\
\
This translates selected text via an AI translation service, either MS Azure or Google Translate.\
\
*   [AI multi-language model translation](https://www.financialmodellinghandbook.org/ai-multi-language-model-translation/)\
    \
\
* * *\
\
Model utilities\
---------------\
\
### Open utilities dialogue\
\
Ctrl+shift+6\
\
This keystroke opens the macro utility dialogue. The keystrokes to activate each utility are listed. Utilities are run on the sheets selected. Alt+a selects all sheets.\
\
![](https://www.financialmodellinghandbook.org/content/images/2022/03/4-1.jpg)\
\
### Section 1: Quick build\
\
Q - Corkscrew with no initial balance\
\
W - Corkscrew with an initial balance\
\
These provide a quick way of adding a new balance corkscrew. The macro will first ask for the name of the balance.\
\
*   [How to model balances](https://www.financialmodellinghandbook.org/p/how-to-model-balances)\
    \
*   [How to add a new balance](https://www.financialmodellinghandbook.org/adding-a-balance-corkscrew/)\
    \
\
T - Add temp sheet\
\
This shortcut builds a Template sheet carrying the default page set up.\
\
### Section 2: Prepare model for release\
\
1 - Set zoom level\
\
This shortcut will apply a zoom setting to all selected sheets. This is often used as part of a model tidy up process.\
\
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
2 - Reset focus and select cell A1\
\
This repositions each selected sheet back to the home position and selects cell A1 on each sheet. Often used as part of a model tidy up process.\
\
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
3 - Reapply level 1 and 2 grouping\
\
When copying and pasting model sections and building new parts of the model, grouping can quickly become a mess. This macro reapplies grouping according to Column A and Column B headings.\
\
*   [Using grouping to see the big picture](https://www.financialmodellinghandbook.org/using-grouping-to-see-the-big-picture/)\
    \
*   [Section completion checklist](https://www.financialmodellinghandbook.org/section-completion-checklist/)\
    \
\
4 - Remove gridlines \
\
Adding or removing worksheet gridlines has to be done on a sheet by sheet basis. This shortcut removes gridlines on all selected sheets.\
\
5 - Check and fix all label capitalisation\
\
Consistent label capitalisation is important. This shortcut checks heading and label capitalisation. Often used as part of a financial model tidy-up process. You can maintain a list of exceptions within the macro file.\
\
*   [How to check and correct label capitalisation](https://www.financialmodellinghandbook.org/how-to-check-and-correct-label-capitalisation/)\
    \
*   [What makes a poor row label](https://www.financialmodellinghandbook.org/what-makes-a-poor-row-label/)\
    \
*   [Section completion checklist](https://www.financialmodellinghandbook.org/section-completion-checklist/)\
    \
\
6 - Collapse all grouping\
\
7 - Expand all groupings\
\
Collapsing all grouping across all selected sheets can be useful when preparing a model for release. Similarly, when working on a model you may want to expand all the groupings while working.\
\
*   [Using grouping to see the big picture](https://www.financialmodellinghandbook.org/using-grouping-to-see-the-big-picture/)\
    \
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
8 - Change all print header settings\
\
This shortcut changes print heading settings across all selected sheets. It's easy to forget this and put models out with the wrong project or client name on them.\
\
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
9 - Remove links to blank cells\
\
This function removes any links to blank cells that have been created when copying a link across from Column E. These occur when creating series links due to the constants column and the blank column before the timeline being empty, and where there are now row totals, for example on balances.\
\
### Section 3: Model information\
\
The shortcuts in this section return information about your model. These can help you to review and tidy up your model.\
\
L - List all used labels\
\
The purpose of listing all the labels in your model is primarily to check for duplicates. This can be used as part of a model review / model release checklist.\
\
*   [How to check for duplicate row labels](https://www.financialmodellinghandbook.org/how-to-check-for-duplicate-row-labels-in-a-financial-model/)\
    \
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
U - List all unique units\
\
Similar to listing labels, this is a review tool to help you check for label inconsistency.\
\
*   [How to sense check the units used in your model](https://www.financialmodellinghandbook.org/how-to-sense-check-the-units-in-your-model/)\
    \
*   [Model release checklist](https://www.financialmodellinghandbook.org/model-release-checklist/)\
    \
\
C - List all conditional formats\
\
Conditional formats can cause the file size to increase. This shortcut lists all conditional formats in the business and allows you to remove any you're not using.\
\
*   [How to remove unused conditional formats](https://www.financialmodellinghandbook.org/how-to-check-the-conditional-formats-in-your-model/)\
    \
*   [How to reduce excel file size](https://www.financialmodellinghandbook.org/how-to-reduce-excel-file-size/)\
    \
\
R - List all used ranges\
\
Managing used ranges helps to keep Excel file size under control.\
\
*   [How to check and reset the used range and end cell in the model](https://www.financialmodellinghandbook.org/how-to-check-and-reset-the-used-range-in-your-model/)\
    \
*   [How to reduce excel file size](https://www.financialmodellinghandbook.org/how-to-reduce-excel-file-size/)\
    \
\
F - List all used fonts\
\
This shortcut is a simple tool to allow you to check for inconsistent font usage.\
\
O - list all unique cell formulas in workbook\
\
This will create a list of the unique formulas for model review / audit purposes.\
\
*   How to [list all unique formulas in your workbook](https://www.financialmodellinghandbook.org/how-to-list-unique-formulas-in-your-model/)\
    \
\
V - list all data validations formulas in the workbook\
\
This report is also for model review and maintenance purposes.\
\
M - Create Named Range report\
\
This will create a report of all the Named Ranges in your model to help you identify unused or hidden Names or Names with errors.\
\
*   [How to check for Range Name errors, unused Names and hidden Names](https://www.financialmodellinghandbook.org/how-to-check-for-range-name-errors-unused-names-and-hidden-names/)\
    \
\
D - Delete unwanted Range Names\
\
This macro will delete any Range Names on the Range Name report which you have indicated as not required by leaving Column A blank.\
\
*   [How to batch delete Range Names](https://www.financialmodellinghandbook.org/how-to-batch-delete-unwanted-range-names/)\
    \
\
X - list Excel application information\
\
This will create a sheet containing Excel version, file paths, adds in etc, about your excel environment. Used for general info and debugging purposes.\
\
* * *\
\
Number formatting\
-----------------\
\
### Apply "normal" style\
\
Ctrl+shift+, \
\
This is the default number style in the model. This can be customised by changing the format of Cell H48 in "Custom Shortcuts"\
\
### Increase decimal places\
\
Ctrl+.\
\
This will add one decimal place to the number in the selected cell(s)\
\
### Decrease decimal places\
\
Ctrl+,\
\
This will remove one decimal place from the number in the selected cell(s)\
\
### Factor style\
\
Ctrl+shift+.\
\
This will apply the factor style, as defined in call H39 on the Custom Shortcuts sheet. We tend to use 4 decimals places for factors (for example discount factor, escalation factors, partial period factors).\
\
### Percentage style\
\
Ctrl+shift+p\
\
This will apply the percentage style as defined in cell H40 in the Custom Shortcuts sheet.\
\
### Toggle date style\
\
Ctrl+shift+l\
\
This will toggle between the "long" and "short" date styles, as defined in Cells H42 and H43 in the Custom Shortcuts sheet.\
\
### Black font\
\
Ctrl+shift+b\
\
Used for local links and calculations.\
\
### Import marking / Export marking\
\
Ctrl+shift+m / Ctrl+shift+x\
\
Use for imported links.\
\
*   [How to create a link](https://www.financialmodellinghandbook.org/how-to-create-a-link-in-a-financial-model/)\
    \
*   [Why we mark imports and export](https://www.financialmodellinghandbook.org/why-we-mark-imports-and-exports/)\
    \
\
* * *\
\
Cell formatting\
---------------\
\
### Clear shading\
\
Ctrl+shift+c\
\
Clears all cell shading. Does not clear borders. Native excel keystroke Ctrl+shift+- will clear borders.\
\
### Placeholder shading\
\
Ctrl+shift+y\
\
Applies yellow shading for placeholders (or other colour as defined in the macro settings)\
\
*   [Why we use placeholders](https://www.financialmodellinghandbook.org/why-we-use-placeholders/)\
    \
*   [How to create a placeholder](https://www.financialmodellinghandbook.org/how-to-create-a-placeholder/)\
    \
\
### Input shading\
\
Ctrl+shift+i\
\
Applies input cell formatting as defined in the macro settings.\
\
*   [How to add an input](https://www.financialmodellinghandbook.org/how-to-add-an-input-to-an-financial-model/)\
    \
*   [Managing inputs - Part 1: Cases, scenarios and sensitivities](https://www.financialmodellinghandbook.org/p/managing-inputs-part-1-cases-scenarios)\
    \
*   [Managing inputs - Part 2: Using and comparing cases](https://www.financialmodellinghandbook.org/p/managing-inputs-part-2-using-and)\
    \
*   [Managing inputs - Part 3: Running scenarios](https://www.financialmodellinghandbook.org/p/managing-inputs-part-3-running-scenarios)\
    \
*   [Managing inputs - Part 4: Input sheet mechanics](https://www.financialmodellinghandbook.org/p/managing-inputs-part-4-input-sheet)\
    \
\
### Macro based value shading\
\
Ctrl+shift+v\
\
Sometimes macros are required to write values into the model. These are inputs, but not inputs intended to be changed by users.\
\
*   [How to add a VBA macro to a financial model](https://www.financialmodellinghandbook.org/how-to-add-a-vba-macro-to-a-financial-model/)\
    \
\
### Apply borders\
\
Ctrl+shift+d\
\
Applies top of row and bottom of row borders to the selected cells.\
\
[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--62.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)\
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
Subscribe](https://www.financialmodellinghandbook.org/complete-list-of-productivity-pack-macros#/portal/signup)