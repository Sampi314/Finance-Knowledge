# How to Undo in Power Query?

**Source:** https://trumpexcel.com/power-query/undo

---

[Skip to content](https://trumpexcel.com/power-query/undo/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/power-query/undo/#below-title)

Power Query has an undo option that works differently than Excel.

While in Excel, you can use _Ctrl+Z_ to undo, [Power Query](https://trumpexcel.com/power-query/)
 works differently.

In Power Query, all your steps are recorded in a sequential order, and to undo any step, you need to go back to the step that you want.

Let me show you how it works.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/power-query/undo/#)

Undo in Power Query
-------------------

When working with Power Query, you will see that all your steps are recorded sequentially in the _Applied Steps_ pane, as shown below.

![Applied steps pane in Power Query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20792%20925'%3E%3C/svg%3E)

As of now, the result that I see in the Power Query editor is the result returned by the last step (named _Removed Columns_).

### Undo One Step

Now, to undo one step (which means removing the changes done by the _Removed Columns_ step and reverting back to get the result returned by the _Filtered Rows_ step), simply put your cursor on the **‘X’ icon** in the _Removed Columns_ step and click on it.

![Click on the x icon of the step in Power Query to undo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20791%20830'%3E%3C/svg%3E)

When you do this, Power Query is going to remove the _Removed Columns_ step, and you will get the result till the _Filtered Rows_ step.

This is how you can undo one step in Power Query.

**Caution**: Once you delete a step in Power Query, there is no way to get it back. The only way to get it back is to recreate it from scratch.

### Undo All Steps After a Specific Step

If you want to undo multiple steps (for example get the result only from the Source data and remove all the steps after it), follow the steps below:

1.  Place your cursor on the step till which you want to undo. In this example, since I want to get the result from the _Source_ step, I would place my cursor on the step after the _Source_ step.
2.  Right-click and then select the option _Delete Until End_.

![Click on the Delete until end option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20812'%3E%3C/svg%3E)

This will remove all the steps after the Source step.

So, instead of removing one step at a time, if you want to remove all the steps in one go, you can use the above method.

Note: If you want to remove multiple steps, and if these steps are not consecutive, then you will have to individually go to each step and click on the X icon for that step.

### Undo Without Deleting Steps

Power Query allows you to see the result of each step in the Power Query editor.

So, if I want to see the result of the _Filtered Rows_ step, I don’t need to delete the steps after it.

All I need to do is select the _Filtered Rows_ step in the _Applied Steps_ pane, and it will show me the result of this step in the Power Query data preview area.

This means that you can undo steps without actually deleting the steps.

Pro Tip: Before deleting any step, always have a look at all the steps to ensure that you do not end up deleting anything that you may need later. Remember, once you delete a step, you cannot get it back.

Important Considerations When Deleting Steps in Power Query
-----------------------------------------------------------

Here are some important considerations to know when you are undoing a step in Power Query.

### No Redo After Undo

Unlike Excel, you cannot redo after the undo step.

So, if you delete a step in Power Query, it’s gone for good, and there is no way to recover it. Be very sure when you are deleting a step in Power Query.

If you are not completely sure, it is a good idea to make a backup copy of your file.

### Deleting Step Can Break Your Query

Power Query works by using the result of the previous step in the next step.

So it’s possible that when you delete a step, it may break your query (because there are dependencies that the subsequent steps have on the one you deleted).

If that’s the case, Power Query will warn you about it while you are deleting the step. It’ll show you a message box as shown below.

![Delete step warning in Power Query when undoing step](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201380%20546'%3E%3C/svg%3E)

In this article, I showed you how to undo steps in Power Query.

While there is no traditional undo option in Power Query, it can be done by deleting the steps that you do not need.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel & Power Query articles you may also like:**

*   [How to Undo Sort in Excel (Revert to Original)](https://trumpexcel.com/undo-sort-excel/)
    
*   [Merge Tables in Excel Using Power Query](https://trumpexcel.com/merge-tables/)
    
*   [Free Power Query Course](https://trumpexcel.com/power-query-course/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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