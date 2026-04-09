# Managing Scenario Manager

**Source:** https://sumproduct.com/thought/managing-scenario-manager/

---

[Home](https://sumproduct.com/)

\> Managing Scenario Manager

*   May 14, 2025

Managing Scenario Manager
=========================

How to generate a simple scenario analysis using Excel’s built-in Scenario Manager tool.

Managing Scenario Manager
=========================

This article looks at a very simple way to generate scenario analysis using Excel’s built-in Scenario Manager tool. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

Is there a quick way to undertake scenario analysis in Excel?

Advice
------

**Scenario analysis** is a common top-down analytical approach where numerous inputs are modified at a time, consistent with a common theme, and corresponding outputs are then analysed, e.g. “best case”, “most likely case”, “worst case”.

I have mentioned scenario analysis before; it can be readily performed in Excel using the **OFFSET** function (see [Onset of OFFSET](https://www.sumproduct.com/thought/onset-of-offset)
 for further information).

Excel can vary one or two inputs at a time using Data Tables (see [Being Sensitive With Data Tables](https://www.sumproduct.com/thought/data-tables)
 for more information). But how do you deal with changing more than two inputs at a time?

### Scenario Manager

**Scenario Manager** is a built-in Excel tool that allows users to deal with changing up to 32 variables (cells) simultaneously. It can be accessed from the ‘Data’ tab on the Ribbon and is located using the ‘What-If Analysis’ icon in the ‘Data Tools’ section:

![](https://sumproduct.com/wp-content/uploads/2025/05/image-01-accessing-scenario-manager.gif)

Locating Scenario Manager

It can also be called using the keyboard shortcut **ALT + T + E** in all versions of Excel.

Once loaded, the Scenario Manager dialog box will be displayed, and, if it is the first time of use in a particular spreadsheet, the user will be presented with the following message:

![](https://sumproduct.com/wp-content/uploads/2025/05/image-02-scenario-manager-dialog-box.gif)

Adding a Scenario

I must admit I find the Scenario Manager tool very user-friendly compared to some other, apparently more obstructive functionalities. In order to create scenarios, you simply define the scenario name and select the cells that can change, viz.

![](https://sumproduct.com/wp-content/uploads/2025/05/image-03-adding-base-case-scenario.gif)

Editing a Scenario

Comments are useful for future reference and will appear in output reports (see below). As for ‘Protection’, selecting ‘Prevent changes’ stops the user from modifying the inputs later as long as the worksheet has been protected (**ALT + T + P + P**). Regarding ‘Hide’, I am uncertain as to why you would create a scenario only to hide it!

One mistake that users may make when defining scenarios is selecting a changing cell that contains a formula (rather than a hard coded input). In this instance, when the end user presses the ‘OK’ button in the ‘Edit Scenario’ dialog box (above), the user will get the following Excel error message:

![](https://sumproduct.com/wp-content/uploads/2025/05/image-04-formula-error-message.gif)

Excel Error Message

i.e. it is possible to select a changing cell that contains a formula – it’s just if you do, Excel will warn you as a common courtesy since the formula will be replaced with hard code.

Once the scenario has been named, Excel will then prompt you to modify the scenario values of the inputs:

![](<Base64-Image-Removed>)

Modifying Inputs

Once the values have been updated, you can choose to add another scenario (the ‘Add’ button above saves the scenario and prompts the user to create another scenario) or simply return to the Scenario Manager dialog box (by clicking on ‘OK’).

Once scenarios have been defined, returning to the ‘Scenario Manager dialog box allows the user to change the values used within the underlying spreadsheet instantly by selecting the relevant scenario and clicking on the Show button:

![](<Base64-Image-Removed>)

Showing a Scenario

This allows the user to view the effects on outputs by switching scenarios. However, what do you do if you wish to view a summary of how the outputs vary for all scenarios defined?

The answer is simple: in the ‘Scenario Manager’ dialog box, regardless of the scenario selected, click on the ‘Summary…’ button:

![](<Base64-Image-Removed>)

Producing a Summary

This will take the user to the Scenario Summary dialog box, where the user can choose between either creating a static output summary or else generating a scenario PivotTable report (PivotTables have been discussed previously; please see [\>Pivotal PivotTables](https://www.sumproduct.com/thought/pivotal-pivottables)
).

![](<Base64-Image-Removed>)

Creating a Scenario Summary

At this point, the end user must specify the outputs to be reported. You may select up to a maximum of 32 output cells. Assuming we select the standard ‘Scenario summary’ at this juncture, Excel will produce the output on a new worksheet:

![](<Base64-Image-Removed>)

Example Outputs

It should be noted that these outputs are not dynamic. If you were to change any input value, the output reported will not change. However, if all you seek is a quick-fire method to generate scenario outputs, this is an invaluable tool.

The [attached Excel file](https://sumproduct.com/assets/user-upload/sp-scenario-manager-illustration.xls)
 provides an example of how the Scenario Manager may be used in practice.

### Merging Scenarios

Sometimes, you may wish to combine scenarios which have been defined in other worksheets or even other workbooks. Excel caters for this need. In the ‘Scenario Manager’ dialog box, click on the ‘Merge… button:

![](<Base64-Image-Removed>)

Merging Scenarios

This takes the user to the ‘Merge Scenarios’ dialog box where the user can choose which workbook and corresponding worksheet merged scenarios should be sourced from. Obviously, these scenarios need to have been defined first!

![](<Base64-Image-Removed>)

Locating Scenarios to Merge

### Word to the Wise

The Scenario Manager is a great tool for generating summary outputs for up to 32 inputs quickly. However, unless the Summary Output report has been produced, end users cannot view the input assumptions for multiple scenarios simultaneously. Furthermore, even if the said report has been produced, changing the inputs in any given scenario will not cause Excel to recalculate the reported outputs.

Therefore, this tool can be viewed as both inflexible and opaque. If flexibility and transparency are required, I strongly suggest using the **OFFSET** technique discussed in [Onset of OFFSET](https://www.sumproduct.com/thought/onset-of-offset)
 and the [associated Excel file](https://sumproduct.com/assets/user-upload/sp-offset-examples.xls)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/managing-scenario-manager/#0)
    
*   [Register](https://sumproduct.com/thought/managing-scenario-manager/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/managing-scenario-manager/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/managing-scenario-manager/#0)

[](https://sumproduct.com/thought/managing-scenario-manager/#0 "close")

top