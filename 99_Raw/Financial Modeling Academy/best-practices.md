# Financial Modeling Best Practices

**Source:** https://www.financialmodelingacademy.com/best-practices

---

top of page

Best Practices
--------------

**1\. Keep it simple**

As Einstein said, "everything should be made as simple as possible, but not simpler", the project or the company you need to model may be complex, but it is always possible to break complex formulas into several, smaller, easier to understand formulas.

As a rule of thumb no formula should be longer than your longest finger, if it is the case then you should consider breaking it into several cells.

If a formula is too complicated it will be very difficult for other people to work with your model or even for you if you forget why a formula was designed in a particular way.

**2\. Be consistent**

*   Separate the spreadsheets with the inputs from the ones with the calculations and the ones with the outputs
    

**4\. Prefer sums over a sequence of additions and substractions**

Rather than writing complicated, long formulas where you have to add and substract several cells, directly add the sign in the cell to allow the use of SUM to calculate the end result, this way you can visually check that there is no sign problem.

The example below compares the two methodologies, the recommended methodology is the Option 2.

![](https://www.financialmodelingacademy.com/quality_auto/be24a7_d48bef8f153b4c83b0108a4b4cbc917c.png)

**5\. Use 0/1 flags**

When the same condition applies to several rows in the model, create a forumla in a dedicated row that will return 1  if the condition is True and 0 else. This way you can simplify the model and create shorter formulas.

In the example below the user created a flag that indicates whether the operations period has started or not, this way the user can start operating costs and maintenance costs only after the commissioning date.

![](https://static.wixstatic.com/media/be24a7_d27c7fc2ba744c219a43b4a62b44f1b9.gif)

**6\. Never ever allow circular references**

It can be tempting sometimes to allow circular references in a model, especially to model interest during constructions (to learn how to avoid it, click [here](https://www.financialmodelingacademy.com/funding-requirement)
), this should never be done. Once iterative calculation is activated, there is no way to check whether the model is behaving properly or not. One other side effect is that if at some point you get a lot of #REF ! in the model, undoing what you just did may not be enough to recover the model and it may remain plagued with #REF ! everywhere.

There is always a way to avoid circular reference, either through VBA coding or through approximations.

**7\. Add as many checks as possible**

Every time you have the opportunity to calculate the same result with two methods, do it and add a check formula to make sure the two results are identical.

**8\. Save as many versions of the model as possible**

Disk space is no longer a problem so take advantage of the all the space that is now available and save as many versions of the model you are working on as possible. It will be particularly useful if you wish to go back to an earlier version of the model if something went wrong with the current version.

![](https://static.wixstatic.com/media/be24a7_0c8ed8db4a6f41df828f1d5afa211e2e.gif)

![](https://www.financialmodelingacademy.com/quality_auto/be24a7_d15fd2becc2c41bab748cfe01b7b02cc.png)

*   Color code the inputs, for example asign the color blue to all the constants so that the user can immediately identify where the inputs are in the model. Excel can help you isolate the constants in any spreadsheet very quickly, click [here](https://www.financialmodelingacademy.com/isolate-constants) to know more
    

*   Make sure that the same column always corresponds to the same time period in every spreadsheet (for example if column J is 2016 in spreadsheet #1, make sure column J also corresponds to 2016 in all the other spreadsheets), this will make your life much easier when you will need to check formulas that refer to cells in other spreadsheets
    

*   Try as much as possible to keep the formulas consistent in a given row, if you need to change the formula at some point in the row, highlight the cell where the change is happening with a very flashy color to inform the user that he should be careful there and not copy and paste the first cell of the row to the whole row
    

**3\. Do not hide anything**

Always keep in mind that your model will be used by someone else at some point or that you may have to use it again in a long time. Hiding rows, columns or cells (by using a white font for example) is very dangerous as the user may not see that rows and columns are hidden and thus erase by mistake entire areas of the spreadsheet.

Rather than hiding rows or columns you can group them such that the user knows that some rows or columns are not visible.

Excel modeling

1\. Select the row(s) or column(s) that you want to group

2\. Go to Data / Group / Group

3\. A "+" appears on the left for rows and on top for columns, by clicking on it you can show or hide the rows/columns

bottom of page