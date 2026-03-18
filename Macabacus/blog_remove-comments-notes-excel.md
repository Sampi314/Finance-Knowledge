# How to Remove Comments & Notes in Excel (Downloadable Template)

**Source:** https://macabacus.com/blog/remove-comments-notes-excel

---

How to Remove Comments and Notes in Excel
=========================================

![How to Remove Comments and Notes in Excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel.jpg)

When working in finance or investment banking, utilizing comments and notes within Excel is crucial, not just a nice-to-have feature. These resources are vital in improving financial analysis, promoting teamwork, and enhancing data transparency. They enable you to provide background information, clarifications, and valuable observations within your spreadsheets, simplifying the understanding of the reasoning and logic backing the data.

Sometimes, you might find yourself in a situation where you have to delete comments and notes from your Excel documents. This could be for reasons like wanting to make your spreadsheet look more professional for a presentation, maintaining privacy, or sharing the file with clients while keeping internal discussions private. In this blog post, we’ll discuss different ways to remove comments and notes from Excel spreadsheets that are specifically useful for finance professionals and investment bankers.

**TABLE OF CONTENTS**

1.  [Understanding Comments and Notes in Excel for Finance](https://macabacus.com/blog/remove-comments-notes-excel#understanding)
    
2.  [Dataset Overview](https://macabacus.com/blog/remove-comments-notes-excel#dataset)
    
3.  [Download Excel Template](https://macabacus.com/blog/remove-comments-notes-excel#download)
    
4.  [How to Remove Individual Comments and Notes in Financial Spreadsheets](https://macabacus.com/blog/remove-comments-notes-excel#how)
    
5.  [How to Remove Multiple Comments and Notes in Bulk](https://macabacus.com/blog/remove-comments-notes-excel#remove)
    
6.  [Best Practices for Managing Comments and Notes in Financial Spreadsheets](https://macabacus.com/blog/remove-comments-notes-excel#best)
    
7.  [Using Macabacus’ Prepare to Share Tool](https://macabacus.com/blog/remove-comments-notes-excel#macabacus)
    

**Understanding Comments and Notes in Excel for Finance**
---------------------------------------------------------

Before removing anything, let’s first understand how comments and notes work in Excel. In older versions like Excel 2019, users could add comments to cells, which are shown as red triangles in the corner. They are hovering over the comment. In newer versions like Excel for Office 365 and 2021, Microsoft introduced ‘notes’ for a more modern and user-friendly experience.

When analyzing finances, it’s important to include comments and notes to give more context to the data. These annotations can provide further insight into where numbers come from or essential factors to consider in your analysis. These explanations can help others better grasp your work and encourage teamwork among colleagues and stakeholders.

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

**Dataset Overview**
--------------------

To illustrate the process of removing comments and notes, let’s consider a typical dataset investment bankers use. This dataset might include company financial statements, valuation models, investment recommendations, and client portfolio information. Throughout the spreadsheet, you and your team have likely added comments and notes to provide context, explain assumptions, and flag important points for discussion.

For example, in a company valuation model, you might have added a comment to explain the rationale behind your choice of discount rate or a note to highlight a key sensitivity analysis. In a client portfolio spreadsheet, you may have used comments to provide additional details about specific investments or to flag assets that require further review.

**Download Excel Template**
---------------------------

![Download Template](https://macabacus.com/assets/macabacus-tables-template.svg)

Download Template
-----------------

[Remove Comments and Notes](https://macabacus.com/assets/2024/04/How-to-Remove-Comments-and-Notes-in-Excel_Dataset.xlsx)

**[Try Macabacus for free](https://macabacus.com/start-trial)
** to accelerate financial modeling in Excel.

**How to Remove Individual Comments and Notes in Financial Spreadsheets**
-------------------------------------------------------------------------

If you need to remove a single comment or note from your financial spreadsheet, the process is straightforward:

**Step 1**: Select the cell containing the comment or note you want to remove.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-1.jpg)

**Step 2**: Right-click on the cell and choose “Delete Comment” (for comments) or “Delete Note” (for notes).

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-2.jpg)

The comment or note will be instantly removed from the cell.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-13.jpg)

**How to Remove Multiple Comments and Notes in Bulk**
-----------------------------------------------------

When working with large financial spreadsheets or preparing files for sharing, it is sometimes necessary to delete comments or notes from multiple cells at once. To remove comments or notes in bulk: 

**Step 1**: Select the entire worksheet (Click the triangle between the row and column headers).

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-3.jpg)

**Step 2**: For comments: Go to Review > Delete. This will delete all comments on the sheet.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-4.jpg)

**Step 3**: For notes: Go to Home > Clear.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-5.jpg)

**Step 4**: Select ‘Clear Comments and Notes.’

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-6.jpg)

Done! All comments/notes on the current sheet have been removed.

**Using VBA to Remove Comments and Notes in Financial Models**
--------------------------------------------------------------

As an advanced Excel user, you can utilize VBA (Visual Basic for Applications) to eliminate annotations. While the VBA method is the most robust and customizable, it does necessitate some familiarity with coding. We will provide a simple VBA script as an example, which you can tailor to suit your specific requirements. 

Below is a VBA subroutine that eradicates all comments and notes from the current workbook:

_Sub DeleteAllComments()_

_‘Deletes all comments and notes in the active workbook_

_Dim ws As Worksheet_

_For Each ws In ActiveWorkbook.Worksheets_

  _ws.Cells.ClearComments_

  _ws.Cells.ClearNotes_

_Next ws_

_End Sub_

To use the above feature:

**Step 1**: Open the VBA (Alt+F11).

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-8.png)

**Step 2**: In the Project pane, right-click your workbook name and select ‘Insert > Module’.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-9.jpg)

**Step 3**: Paste the above code into the module.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-10.png)

**Step 4**: Save the workbook as a macro-enabled .xlsm file.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-11-1.jpg)

**Step 5**: Close the VBA editor.

**Step 6**: Go to View > Macros > View Macros.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-12-1.jpg)

**Step 7**: Select the ‘DeleteAllComments’ macro and click ‘Run’.

![remove comments notes excel](https://macabacus.com/assets/2024/04/remove-comments-notes-excel-13-1.jpg)

The code loops through each worksheet in the workbook and uses the \`ClearComments\` and \`ClearNotes\` methods to remove annotations. You can modify it to only affect certain sheets by changing the \`For Each\` loop.

Here are a few things to keep in mind when using VBA to remove comments:

*   Always keep backups of your files before running macros.
*   Be sure you want to delete EVERY comment and note. It’s not undoable!
*   If you share the workbook, the recipient will need to enable macros to use the script.

**Best Practices for Managing Comments and Notes in Financial Spreadsheets**
----------------------------------------------------------------------------

While comments and notes can be extremely helpful in financial analysis, it’s important to use them judiciously and manage them effectively. Here are some best practices to keep in mind:

*   Develop a standard system for categorizing your comments (e.g., Assumptions, To-Dos, Questions). This will make it easier to remove certain types in bulk later.
*   Another crucial practice we discussed is the regular review and cleanup of comments as you work. This is important to prevent the accumulation of unnecessary data and maintain your Spreadsheet’s clarity. Don’t let them pile up into an overwhelming mess.
*   Before removing all comments, carefully review them to ensure you’re not deleting critical information. Move any vital notes to a dedicated documentation sheet or README tab.
*   Establishing a comment protocol with your team is essential for shared workbooks. This promotes collaboration and ensures everyone is on the same page about what to include in annotations and how to handle cleanup. It’s a simple step that can significantly enhance your team’s productivity.
*   Consider using an external tool like Spreadsheet Compare to locate and remove annotations across multiple versions of a model

The key is staying organized and communicating with your colleagues. A little proactive comment management will save you massive headaches down the line!

**Using Macabacus’ Prepare to Share Tool**
------------------------------------------

Macabacus offers a number of “sanitation” tools designed to refine files before you distribute them to your co-workers or external clients. The Prepare to Share feature from Macabacus enables users to verify the integrity of a workbook, safeguard sensitive or proprietary data, and enhance the overall look and formatting of spreadsheets, among its many capabilities.

For example, cell comments provide clarity to assumptions and methodologies used in a model. However, they may contain sensitive information or internal communication that is not suitable for external distribution. Using Macabacus’ Prepare to Share tool, you can remove the comments to keep them away from prying eyes. See the video below to learn more about the tool:

**Conclusion**
--------------

Maintaining clean, efficient, and professional Excel spreadsheets is crucial in the fast-paced finance and investment banking world. While comments and notes can be valuable tools for enhancing financial analysis and collaboration, there are times when you need to remove them.

By understanding the different methods for removing individual comments and notes, deleting them in bulk, and even using VBA for more advanced removal tasks, you can keep your financial spreadsheets polished and ready for presentation or sharing. Remember to use comments and notes strategically, review them before removal, and always back up your data to ensure the integrity of your financial models and analyses.

With these tips and techniques, you’ll be well-equipped to manage comments and notes efficiently in your Excel spreadsheets. This lets you focus on what matters most: providing accurate, insightful, and impactful financial analysis to drive informed decision-making. If you’re looking to enhance your productivity and streamline your workflows further, [**Macabacus**](https://macabacus.com/start-trial)
 is your go-to solution!

Build Financial Models in Minutes
---------------------------------

**Enterprise-Grade Financial Modeling** used by 80,000+ professionals across Investment Banking, Private Equity, and Corporate Finance. Ensure consistency, accuracy, and efficiency across your entire organization.

[Get Started](https://macabacus.com/start-trial)
[Book a Demo](https://macabacus.com/demo-request)

Discover more topics
--------------------

[Webinar: The AI Edge in Investment Banking](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

Join experts from Macabacus & LSEG to learn practical insights about AI’s influence on the future of banking.

[Read more](https://macabacus.com/lp/webinar-ai-edge-investment-banking)

[DCF Excel Template](https://macabacus.com/excel/templates/discounted-cash-flow)

Elevate your investment analysis with our free DCF model template. Understand discounted cash flow principles and perform accurate valuations in Excel.

[Read more](https://macabacus.com/excel/templates/discounted-cash-flow)

[Operating Model Excel Template](https://macabacus.com/excel/templates/operating-model)

Download our free operating model Excel template. Forecast revenue, expenses, and key financial metrics for better decision-making.

[Read more](https://macabacus.com/excel/templates/operating-model)

[LBO Excel Model](https://macabacus.com/excel/templates/lbo-model-short)

Try LBO modeling with our comprehensive Excel template. Understand key concepts, calculate returns, and gain actionable insights.

[Read more](https://macabacus.com/excel/templates/lbo-model-short)