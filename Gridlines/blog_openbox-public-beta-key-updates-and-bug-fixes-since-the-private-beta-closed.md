# Key Updates & Bug Fixes For Openbox Public Beta - Gridlines

**Source:** https://www.gridlines.com/blog/openbox-public-beta-key-updates-and-bug-fixes-since-the-private-beta-closed

---

[Skip to content](https://www.gridlines.com/blog/openbox-public-beta-key-updates-and-bug-fixes-since-the-private-beta-closed#content)

Openbox Public Beta – Key updates and bug fixes since the private beta closed
=============================================================================

*   July 9, 2021

The Openbox private beta closed late last year, and since then we’ve been concentrating on delivering the improvements that beta users asked for. We’re grateful to the dedicated users who have continued to send us additional suggestions, and we’ve been working to include those as well.

So, as we launch the public beta, here is what has changed since version 0.8 at the end of the private beta.

First, we’ve given the **user interface** an update, moving to a consistent, more modern look. There’s an extended context/ right-click menu, and simplified access to components.

We’ve also worked on **reports** – which after all are the purpose of any model. Formatting has improved. You can now create headers, sub-headers, and change calculations to and from report lines as well as “normal” calculations. Sub-totals now say more clearly how they are calculated, and you can have them calculate automatically from the items above or specify the calculation manually.

**Components are more flexible** now too. When you are loading them, you get an editable preview that lets you see and change the component before connecting it to your model – and the connection process has been improved.

One thing people seem to do a lot with Openbox is **repeated calculations**. Suppose you are modelling a business that sells five products. It makes sense to use the same calculations for revenue and costs for each one. Openbox now makes it easier to do this, by adding two new buttons. The first repeats a calculation for (say) products, scenarios or whatever you choose. The second calculates the total over all the products/ the maximum over all scenarios or any aggregation you want.

Another big change is the ability to produce models that **aren’t built to the FAST standard**. You can now produce a model either following FAST or to a standard that is still best practice but does not have the colours and block structure of FAST. We always had a vision for Openbox to be standards-agnostic, and this is a step towards that. We will be actively adding on specific other modelling approaches and standards in the coming months.

And we’ve added **LAMBDA** – Excel’s latest feature. Openbox can read them, create them, and even unfold the recursive ones to see what is going on. We think it’s the best available interface for LAMBDAs, but have a look for yourself.

Finally, we’re looking internationally. Formulas now display with commas or semicolons, depending on your Excel regional settings. We’re looking at the possibility of having functions in your own language, just like Excel.

For those of you who like detail, a more complete list of new features, and bug fixes, is below.

New Features

User Interface

*   New Ribbon UI (similar to Office)
*   Remove library menus, using Import Component window only
*   Calculations and sections move out of the way when dragging something over them
*   User can now say “Always” or “Never” for some dialog boxes, rather than being told about them every time
*   Move dialog boxes to WPF, more modern interface, consistent with main window
*   Single click now selects an item, double click to edit
*   Don’t allow any space for flag icon if none needed
*   Updated flags, indices and discounts menus
*   Tidy up popup for adding external links to a calculation
*   Add “Focus on” to shortcut menu
*   Clicking an item in focus mode now shows it in the preview
*   Improve pop-up chart window (F11)
*   Improved shortcut menu

Actuals

*   Allow users to add actuals for any calculation, not just report lines
*   Improve actuals handling including asking for actuals date when actuals first added
*   Offer to add actuals when creating a new model

Reports

*   Report headers now formatted more clearly
*   Report headers no longer create calculation nodes, so it is no longer possible to accidentally include a header in your formulas
*   Allow brackets in report lines, without assuming they are negated e.g. (Dis)investment is now a legitimate name
*   Show “change to report line” buttons
*   Allow basic dashboard to be created
*   Warn about constants on reports
*   Hovering over a ‘sum of above’ item now shows how it is calculated and what lines it depends on
*   Correctly compress sum of above items on yearly reports
*   Deal correctly with inputs on compressed reports
*   Show explicit “sum of above” formulas if desired
*   Deal with sign switch in non-FAST models
*   Improve report line deletion
*   Allow user to move reports left and right
*   Add “Add report header” and “Add report subheader” commands, including to shortcut menu for report
*   Report lines can now be sub-totals, which have a user-defined calculation but are treated as a sub-total when calculating “sum of above” formulas

Units and number formatting

*   Improve units window
*   Better number formatting management
*   Users can now use custom number formats, or standard named ones (e.g. “General”, “Percent”)
*   Can now change the default format for each unit e.g. set all items which are in “US$” to be formatted as “0.00”

Components

*   Preview window when importing component now allows you to see the formulas in the component and edit items before importing
*   More feedback and flexibility on how an imported component is linked to the rest of the model
*   Allow use of placeholders in components, which will be replaced by text chosen by the user when the component is imported. E.g. if the component contains a calculation called “%%debt type%% debt”, Openbox will ask what to replace ‘debt type’ with. Placeholders can be in names or in units

Formulas

*   Improve autocompletion in formula bar
*   Where a balance and an inflow/ outflow vary over different arrays, offer to fix this
*   Use the “BEG” function for the opening value of a balance, not OPENINGVALUE. Now consistent across all balances
*   Where a formula includes “BEG()” ask if it should be a balance. Conversely, warn about balances where the closing formula doesn’t refer to the opening balance
*   When you are editing a formula, clicking on another calculation now inserts the name into the formula (like clicking on a cell in Excel)
*   Simple autocorrection for formulas including adding missing brackets to PREVIOUSVALUE and NA
*   Separator in formulas now respects user’s country/ language settings e.g. “;” in Germany, “,” in USA
*   Formulas now have a “Local” version – which is what the user sees – and a “Standard” version which is always in US English, like Excel

Arrays

*   Allow user to specify that any calculation varies over an array (e.g. sales should vary over all products) and works out which inputs need to vary to allow this. New “Break down by” button on main menu
*   Allow user to “add total” for any item, which adds it up over an array
*   Arrays can now be dates, as well as text or numbers

Lambda

*   Create, read and unfold LAMBDAs

Circular references

*   Allow user to break a circular reference at any calculation, even if Openbox hasn’t identified it as part of a circular reference
*   When there’s a circular reference, show it as a circle which the user can spin round to select where to break it
*   Create optimisation group if needed when breaking circular reference

Updating

*   When you select rows and tell OpenBox to mark them as new/modified or for deletion, it marks all selected rows not just the top one
*   Allow user to read updated inputs on InpS, including items that vary by some array

Other

*   Allow sub-sections, sub-sub-sections and so on
*   Add navigation/ contents page
*   Add master check to all sheets
*   Additional components
*   Better telemetry and error reporting.
*   Improve template, e.g. include sensitivity columns on InpC
*   Add issues log
*   Allow user to add named ranges to the generated Excel file
*   Standard time nodes (e.g. Period number, or model period end) now have an internal tag, so Openbox recognises them as such even if their name is changed
*   Openbox now runs in separate process to Excel, so you can do things in Excel while OpenBox window is open
*   Additional validation and checks e.g. for financial year end month
*   When warning about deleting items with dependents, say what the dependents are
*   When deleting a group of items, don’t warn about dependencies within the group, only about dependents outside the group
*   Add WEEKNUM function
*   Add DAYS360 function
*   Add LEFT and RIGHT functions
*   LOOKUP function can now correctly lookup a value in any array, even if a calculation varies by more than one array
*   Don’t try to show in-place placeholders unless using FAST

Bug Fixes

*   Fix crashes on second new/ open command
*   Fix bad ref to ICSharpCode
*   Placeholder colouring now applied as soon as an input is moved out of the inputs sheet
*   Better report line selection
*   Fix issue with licensing which was triggering several anti-virus programs
*   Remove duplicate/ corrupt reports on loading file
*   Show correct headings on secondary timeline sheets
*   Timeline now set correctly from new model form
*   Drag/drop occasionally copied rather than moving items. Now fixed
*   Fix missing reference to Visual C++ 2014 runtimes
*   Tidy buttons on forms
*   Use correct version of Excel template
*   Don’t show blank and missing sections in contents
*   “Expected units” button now works
*   Dragging sheets into empty sheets now works
*   New balances now appear in the selected sheet, not in unallocated
*   PREVIOUSVALUE function now works for precedents which vary over an array
*   Fix import mapping window
*   Shortcut keys now work whichever part of the main window is active – not just Kanban
*   Correct links to OBZ and OBC files in installer
*   Model period end bug fixed
*   “Actuals” bug fixes
*   “SELECT” function now works with a constant index, rather than a reference to an input
*   Updating “Sum of Above” correctly changes formatting
*   Don’t leave blank columns on the right hand side of a sheet
*   Don’t allow sheets and reports to have the same name
*   Strip illegal characters from sheet names
*   Don’t insert the autocomplete suggestion when the user presses enter in the formula bar, only when they press tab
*   Fixed bug which meant that you occasionally had to press return twice in the formula bar to exit
*   Only show the “Do you want to put all reports on the same time basis” message once per change
*   Correct the labels on sign switched report lines which vary over an array
*   Check for missing time inputs, and existing actuals, on load
*   “Replace”/ “Replace all” now warn the user if the replacement would create a duplicate name, rather than crashing
*   Right clicking on item with no dependents in focus mode no longer crashes
*   Allow loading old .obx file format even if it has a bad number format
*   When ingesting, don’t crash if Excel fails to respond
*   When user presses delte when editing the name of a report line, don’t delete the line
*   Fix spacing between rows in Excel for non-FAST models
*   Correct explicit formula (tooltip) for sum of above items that have only one item above
*   Ingestor no longer crashes if no section headings found
*   Clicking on number format dropdown no longer moves to main window
*   Don’t crash if the component library is being synced e.g by Dropbox or OneDrive
*   If there’s a problem with the template, hide the progress form
*   Correctly trim \[ \] from placeholder names when ingesting
*   Loading invalid model now gives a warning, rather than crashing
*   Don’t allow duplicate calculation names when merging
*   Focus on comment box when it appears
*   Fix bug evaluating units for formulas that contain PREVIOUSVALUE
*   “Sum of above” formulas now deal correctly with sub-totals above them
*   When ingesting, only ask once for each Excel file which column has which purpose
*   Custom number formats now used for all input cells on InpC
*   Caret goes to end of formula when you press F2
*   “Delete” option on shortcut menu now works for report lines
*   Don’t apply the FAST % style to a currency unit
*   Merge placeholders on reports properly
*   Don’t try to add a new dashboard if one is already there
*   Don’t report an error if the user clicks an item which is not in the preview
*   Don’t add pre-defined sheets to the model twice
*   Make all calculations visible before going to focus mode
*   Don’t crash if no initial opening value available for a balance
*   Fix “bouncing” in drag and drop
*   Don’t crash if Excel is busy when marking rows as new/ modified/ for deletion

If you haven’t already enrolled onto our free “Introduction to Openbox” course, you can do so [here](https://academy.gridlines.com/p/introduction-to-openbox)
. Or if you’d like to speak directly to the Openbox development team then reach out to us by filling out the email form [here](https://www.gridlines.com/contact-us/)
. We are always looking to meet people interested in the programme!

Share:

*   [](https://uk.linkedin.com/company/gridlines-com)
    

More Posts

[![financial audit modelling](https://www.gridlines.com/wp-content/uploads/financial-audit-modelling-300x169.jpg)](https://www.gridlines.com/blog/openbox-dev-diary-week-1/)

[Openbox dev diary – Private Beta week 1](https://www.gridlines.com/blog/openbox-dev-diary-week-1/)

Openbox diaries – Beta week 1 Our beta users received Openbox last week and have spent their first week using

[![Autumn Statement 2023](https://www.gridlines.com/wp-content/uploads/Autumn-Statement-300x169.jpg)](https://www.gridlines.com/blog/autumn-statement-2023-boosting-business-growth-in-the-uk/)

[Autumn Statement 2023: Boosting Business Growth in the UK](https://www.gridlines.com/blog/autumn-statement-2023-boosting-business-growth-in-the-uk/)

Minimum tax has been discussed in the international tax arena for some time now, and certain jurisdictions already apply some

[![picture of a vehicle bridge over the water](https://www.gridlines.com/wp-content/uploads/Bridge-300x167.png)](https://www.gridlines.com/blog/what-is-a-model-audit/)

[What is a model audit?](https://www.gridlines.com/blog/what-is-a-model-audit/)

What is a Model Audit? In simple terms, a model audit is a review of a financial model, generally completed

[![](https://www.gridlines.com/wp-content/uploads/pexels-mhtoori-1646164-300x225.jpg)](https://www.gridlines.com/blog/what-project-sponsors-get-wrong-about-financial-advisory/)

[What project sponsors get wrong about financial advisory](https://www.gridlines.com/blog/what-project-sponsors-get-wrong-about-financial-advisory/)

By Gaurav Singh, Head of Infrastructure Advisory In project development, sponsors obsess over technology choices, EPC contracts, permitting, and commercial

[PreviousHow to avoid repeating history: 3 of the highest profile Excel errors of all time](https://www.gridlines.com/blog/how-to-avoid-repeating-history-3-of-the-highest-profile-excel-errors-of-all-time/)

[NextAn Openbox Easter Egg Has Been Found](https://www.gridlines.com/blog/an-openbox-easter-egg-has-been-found/)

Tell us about your project
--------------------------

[![Akram Mostafa](<Base64-Image-Removed>)](mailto:akram.mostafa@gridlines.com)

Akram Mostafa
-------------

Associate Director

akram.mostafa@gridlines.com

[![](<Base64-Image-Removed>)](mailto:morag.loader@gridlines.com)

Morag Loader
------------

Director of Accounting & Tax

morag.loader@gridlines.com