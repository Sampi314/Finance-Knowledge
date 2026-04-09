# Multiple Debt Issues and SUMIF

**Source:** https://edbodmer.com/structuring-multiple-issues-and-sumif

---

This page illustrates some formatting issues that can allow you to more efficiently and accurately structure debt draws and debt repayments with multiple debt issues in project finance models.  The webpage demonstrates how you can set-up a project finance model with multiple debt issues in the input page and in the financial model by separating an general debt section and individual issues on an issue by issue basis. I suggest using the SUMIF formula with codes for the different items such as interest expense, commitment fees, repayments and so forth. The set-up of debt funding and debt repayment is often confusing and takes hundreds or even thousands of lines in a model.  When finished, I hope that you can do some things to make the case with multiple debt issues easier to read, understand and present.

.

Input Page with Multiple Debt Issues
------------------------------------

In setting-up inputs for multiple debt issues, I suggest that you begin with a general section and then put the debt sizing, the debt repayments, the interest rates and the fees.  The layout includes a separate debt issue with characteristics of export credit agency debt as well as VAT debt and equity bridge loan debt.  The screenshot below illustrates the set-up of input pages for debt issues that are used in the exercise.  For the ECA debt, the premium is on itself as well as the base debt amount of qualifying expenditures.  The premium is therefore computed as Qualifying Expenditure/(1-Premium %) – Qualifying Expenditure.  A video is included below the screenshots that works through details of setting-up the inputs.

.

![](https://edbodmer.com/wp-content/uploads/2020/01/Debt-Input.jpg)

.

.

![](https://edbodmer.com/wp-content/uploads/2020/01/Debt-Input-1.jpg)

.

.

Formatting and Structuring a Project Finance Model with Multiple Debt Issues
----------------------------------------------------------------------------

The first point about structuring a model with multiple debt issues in the model sheet is to

Use columns on the left or drivers, sum, tests and other factors as illustrated below.  Note that the EBL debt IDC and Fees increases the project cost and can therefore increase the amount of other debt and equity.

.

![](https://edbodmer.com/wp-content/uploads/2019/07/Using-Columns-on-the-Left.jpg)

.

I have many examples of what not to do.  Put the drivers in the left columns instead of taking the numbers from the INPUT sheet as shown below.  Then people can see how the formula is working.

.

![](https://edbodmer.com/wp-content/uploads/2019/07/Use-Left.jpg)

.

Using SUMIF
-----------

My suggestion is to not engage in the torture and dangerous simple sum functions. Instead of this, you can use the SUMIF with code names.

.

![](https://edbodmer.com/wp-content/uploads/2019/07/SUMIF-on-Multiple-Issues-1.jpg)

.

![](https://edbodmer.com/wp-content/uploads/2019/07/Using-SUMIF-for-totals.jpg)

.

![](https://edbodmer.com/wp-content/uploads/2019/07/SUMIF-on-Multiple-Issues-2.jpg)

### Using SUMIF to Aggregate Interest Expense, IDC, Repayment and Balance

.

![](https://edbodmer.com/wp-content/uploads/2019/05/Aggregate-Debt.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9606&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11916&rand=0.931146425669823)