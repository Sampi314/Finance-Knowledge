# Sheet Structure in a Financial Model

**Source:** https://edbodmer.com/sheet-structure-in-a-financial-model

---

Setting-up Model Sheets and Structure (The S in FAST)
-----------------------------------------------------

In discussing modelling philosophy, I have chosen to be flexible rather than perfectly structured (if you think about your life, sometimes it is good to be structured, sometimes it is better to be flexible and many times these objectives conflict).  The people taking care of my 90 year old father tend to be very structured and only take him out bed at very distinct and distinct times.  But I think they should be more flexible and if he is moaning that he is tired, just let him relax and sleep.  It will not make much of a difference in the world. This is the conflict.  For modelling, you may want to begin with the Structuring part of a model.  Structuring issues essentially involve where should you start (with a time line) and how the model should progress.  These issues in turn drive the order of the assumptions in your model.

### Sheet Order – Depends on Debt Sizing Method and Your Opinion

Option 1 – Development, Construction, Sources and Uses, EBITDA, Debt: Time Order of Constructing and Financing Projects. Use the following order of items and put in different sheets.  This works when the financing is set from the capital expenditures and not from the CFADS. Start with development; move to EPC and construction; sources and uses of funds with financing; operations with revenues and expenses; depreciation, debt schedules and finally financial statements with a cash flow waterfall. In this case, the sheet order may be:

*   Input Scalars
*   Input Time Series
*   Sheet with Time Line Analysis (Simple Formulas)
*   Development and Capital Expenditure Analysis
*   Construction Financing with IDC, Fees and Other Thing that Cause Circular References
*   Operations Analysis starting with capacity and volumes including EBITDA
*   Debt Schedules with Repayment and Interest
*   Waterfall and Financial Statements

At the beginning of the model there should be standard summary sheets the present the IRR’s, DSCR’s and other data.  In addition there should be a scenario sheet and an annual summary sheet.  An example of the sheet order is shown in the screenshot below.  This table of contents was created from the generic macros file after you press CNTL, ALT, C.  You can go to the webpage for generic macros and see how this

![](https://edbodmer.com/wp-content/uploads/2019/07/Contents.jpg)

Option 2 – Merton Miller and Splitting up Operations from Financing: Begin with Operations and No cash; move to free cash flow without finance; then evaluate debt size from CFADS; then work on the sources and uses and finally taxes and cash flow waterfall. This works better when the debt size may occur from CFADS.  If the debt can come from cash flow, you need the cash flow as well as the capital expenditures before you can derive the debt. In this case I strongly suggest a debt sizing section that is different from the basic debt schedule in the model. The sheet order may be:

*   Input Scalars
*   Input Time Series
*   Sheet with Time Line Analysis (Simple Formulas)
*   Operations Analysis starting with capacity and volumes including EBITDA
*   Debt Sizing from CFADS (this will include a circular reference)
*   Construction Expenditures and Financing (with more circular references)
*   Debt Schedule and Waterfall
*   Summary of Financial Statements

As with the other structure above where debt is derived from the uses of funds, there should be standard summary sheets the present the IRR’s, DSCR’s and other data at the beginning of the sheet.  In addition there should be a scenario sheet and an annual summary sheet.

When you set-up sheets, you should put the order of the inputs in the same order as the way the assumptions are used in the model.  You should start with dates and then move to macro-economic data and operations.  You could also start with development costs and capital expenditures.  In my opinion the financing should be after all of the operations, capital expenditures and revenues. Some people separate time series inputs from scalar inputs and put the time series inputs in InputS while the scalar in InputC. An example of what not to do is shown in the screenshot below.  Here the inputs do not start with dates and the fancy colouring is in my opinion very irritating. The silly macros that go to the audit checks drive me crazy.  I hope you are not impressed by this type of idiocy.  I also object to the different fonts (where the name General has a larger size than the inputs, and the different colours that do not show you when you are moving to a different section of the model.

![](https://edbodmer.com/wp-content/uploads/2019/07/Input-problems.jpg)

A better example of an input structure is shown in the screenshot below. You should start with the timing inputs; separate inputs in that are constants in one sheet from inputs that are time series that should be in another sheet.  You should also use the generic macros file to colour the section headings and the inputs.  After this section, you could move to the development cost section or the operating inputs section depending on how the sheets of your model are structured.

![](https://edbodmer.com/wp-content/uploads/2019/07/Inputs-Better.jpg)

### Spreadsheet Structure in Model

In the model below, the sheet structure made my head spin and looking at it still makes me a little crazy.  The debt was sized from the CFADS, but you had to go to the control sheet to find the debt size, which in turn came from yet another sheet in the model and created a horrible to trace circular reference that was solved with the iteration button. To fix this I suggested beginning with a cash flow analysis and a section for evaluating debt size.  This debt goes into a summary sources and uses statement can construction financing after the cash flow statement.

![](https://edbodmer.com/wp-content/uploads/2019/07/No-Nice-Flow.jpg)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9700&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11532&rand=0.27872713822705775)