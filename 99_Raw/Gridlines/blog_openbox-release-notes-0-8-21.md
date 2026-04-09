# Openbox release notes: December update v0.8.21 - Gridlines

**Source:** https://www.gridlines.com/blog/openbox-release-notes-0-8-21

---

[Skip to content](https://www.gridlines.com/blog/openbox-release-notes-0-8-21#content)

Openbox release notes: December update v0.8.21
==============================================

*   December 14, 2020

Since the end of the Openbox beta round 3 in October, we’ve been hard at work fixing the issues our beta users have found and implementing their feature requests. Here is the complete list to date.

New features

*   Create LAMBDAs from Openbox calculations.
*   Read LAMBDAs from Excel and convert to Openbox calculations.
*   “Unfold” recursive LAMBDAs to help with understanding and testing.
*   Added “Import” to right click/ context menu.
*   If a calculation does not have a flag applied, don’t leave a blank space for the flag icon.
*   The main window now scrolls left and right if you drag items over the left/right-hand margins.
*   Single click anywhere on a calculation block selects it, double click edits.
*   If you edit a calculation name, and it is the same as an existing one, pressing “Escape” will now go back to the name it had before editing.
*   TAB in the formula bar now works like Enter/ Return.
*   After importing a component, you now see what calculations have been connected to the rest of the model, and have the option to make further connections manually.
*   You can now add actuals at any stage, and new actuals will be added if new report items are added.
*   Master checks sheet now added – any calculation in the model with the unit “check” will be included in the overall check.
*   Added a dropdown to set the number format for each calculation.
*   Added new number format manager windows. You can now change the built-in formats.
*   Number formats now read from the template.
*   When a report is in focus, underline the name.
*   F2 now puts the cursor at the end of the formula bar.
*   Sensitivities now included by default on InpC.
*   LET functions are now translated to Openbox formulas.

Bug fixes

*   Can now undo “Paste”.
*   Double-clicking a calculation name in the formula autocomplete list now inserts it in the formula.
*   The formula autocomplete window is not shown if there are no possible autocomplete choices.
*   Report lines are now shown in a lighter colour when selected. The text was not readable before.
*   Can now merge a “sum of above” calculation with another.
*   When you drag a section including placeholders to the Inputs sheet, all the placeholders are now coloured as inputs.
*   Pressing “\]” in the formula bar no longer inserts the current autocomplete suggestion.
*   Check for “OPENINGVALUE” being used in calculations that are not balances (and conversely, for balance calculations that don’t refer to their opening value).
*   Placeholders on a report sheet now have “\[” “\]” around them.
*   Arrow keys now work in Focus mode.
*   Sections in the “Input” sheet are now correctly ordered in the spreadsheet.
*   When you group items into a section, the section is left where the items are, not placed at the end of the sheet.
*   The Master check cell now works correctly even if all checks are constants.
*   The formula bar now updates when you update the name of a balance.
*   The list of flags, indices and discounts now updates automatically when something is deleted.
*   When you have a section highlighted, and add a new calculation, the calculation is put into that section, not “Unallocated”.

Share:

*   [](https://uk.linkedin.com/company/gridlines-com)
    

More Posts

[![ofwat financial software](https://www.gridlines.com/wp-content/uploads/ofwat-financial-software-300x169.jpg)](https://www.gridlines.com/blog/ofwat-builds-its-official-price-control-model-using-openbox/)

[Ofwat builds its official price control model using Openbox](https://www.gridlines.com/blog/ofwat-builds-its-official-price-control-model-using-openbox/)

Earlier today, the UK water regulator Ofwat published its draft price control model for PR24. You can view the full

[![Laptop with hands pointing at the screen, and another hand navigating the laptop](https://www.gridlines.com/wp-content/uploads/2024/05/john-schnobrich-FlPc9_VocJ4-unsplash-scaled-1-300x200.jpg)](https://www.gridlines.com/blog/financial-model-audit-a-clean-audit-report/)

[Financial Model Audit: A Clean Audit Report](https://www.gridlines.com/blog/financial-model-audit-a-clean-audit-report/)

Having spent more of my career being audited, rather than being the auditor, I always had mixed feelings when I

[![London landscape with Big Ben, buses and cars, Houses of Parliament and lots of pedestrians](https://www.gridlines.com/wp-content/uploads/East-Africas-agriculture-industry-31-1-300x169.jpg)](https://www.gridlines.com/blog/uk-spring-statement-2022-what-does-it-mean-for-tax/)

[UK Spring Statement 2022: What does it mean for tax?](https://www.gridlines.com/blog/uk-spring-statement-2022-what-does-it-mean-for-tax/)

The UK Chancellor, Rishi Sunak, delivered his Spring Statement today (23 March 2022). In terms of measures relating to companies

[![blue and green futuristic image to portray data and AI machine brain](https://www.gridlines.com/wp-content/uploads/openbox-financial-AI-300x169.jpg)](https://www.gridlines.com/blog/openbox-a-matter-of-perspective/)

[Openbox | A matter of perspective](https://www.gridlines.com/blog/openbox-a-matter-of-perspective/)

When we started building Openbox, we thought we were building a tool to create spreadsheet models. But as anyone who

[PreviousWhat does Lambda mean?](https://www.gridlines.com/blog/what-does-lambda-mean/)

[NextSpreadsheet risk. How worried should we be?](https://www.gridlines.com/blog/spreadsheet-risk-how-worried-should-we-be/)

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