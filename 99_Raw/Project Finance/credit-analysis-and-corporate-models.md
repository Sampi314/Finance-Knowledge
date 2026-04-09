# Credit Analysis and Corporate Models

**Source:** https://edbodmer.com/credit-analysis-and-corporate-models

---

On this webpage I present some practical aspects of developing and using corporate models in credit analysis. I use a case where you have received some detailed financial projections from the company that wants to borrow your money and you want to use their detailed models as the basis for credit analysis. By starting with the company case, you can use the model to negotiate various assumptions with the borrower rather than just telling the client that you can or cannot make a loan.  With alternative assumptions and the company case, you can work through the debt size and debt structure with alternative revenue, expense, capital expenditure and other assumptions. The idea is that when developing credit analysis, you can start with the company case and then develop bank base case and bank downside cases. The problem is that it is often impossible to use a company case with thousands of lines and detail that can make you lost.  So, on this page, I demonstrate how to put together a summary model from detailed corporate models and then evaluate credit quality through negotiating with borrowers and presenting scenarios to credit committees.  This stuff is pretty boring and it is difficult to do it in one go without taking some breaks.

**[Excel File with Corporate Model for Credit Analysis Demonstrating How to Modify Company Case and Develop Scenarios](https://edbodmer.com/wp-content/uploads/2020/01/Corporate-Model-for-Credit3.xlsm)
**

Step 1: Put Together a Simplified Company Case from Detailed Company Forecast
-----------------------------------------------------------------------------

This can be the really painful part of the my suggested technique for evaluating credits of corporate credits using financial models.  Companies may give you really big models with all of their management accounts and details of every pencil that they intend to purchase.  This can be intimidating and maybe it is even intentional so that you will say to yourself — this must be a good loan because the financial model is so fancy.  They may give you models that to not tie out to the historic financial statements.  But at the end of the day you want EBITDA, capital expenditures and working capital changes first to define cash flow in the fancy model.  These few numbers along with interest expense on other loans can define the financing needs and let you evaluate whether you can repay the loan.  If you receive models from others, the first step is putting together a summary cash flow statement that can be annual if the loan is not a short-term working capital loan.  In the case below, I use a solar company that has not earned positive EBITDA in the past and the company is suggesting that through growth, it will be able to take advantage of operating leverage.  The first page shows the income statement and you can see that most of the numbers are just fixed (assumed to be taken from the company model).

Remove the depreciation from cost of goods sold.

Use the SHIFT,ALT,–> to group (temporarly hide) rows that are too detailed as illustrated below.

Step 2: Work through Assumptions and Revise Key Items in Model
--------------------------------------------------------------

After establishing a company case that summarises simple cash flow items including EBITDA, Working Capital Changes and Capital Expenditures, you can create a second sheet that works through the various accounts. I have called this the Assumptions and Working sheet. As with any corporate model, a history flag is essential.  With the historic flag, you can only change the assumptions for future items and create account balances.  There should not be way to many accounts.  Use sheet colours so you can explain exactly where things are coming from.

Work through the big assumptions.  Start with revenue as illustrated below and question whether the assumptions are reasonable.  Big growth with both price increase and volume increase is very difficult.

Capital expenditures must support the sales growth.  With capital expenditures, you can include the associated depreciation. You should really also include retirements.  The screenshot below illustrates how you may work through the items.

Other administrative expenses and overheads etc. could be a percent of revenues or they could be derived from growth independent of revenues (or both).  You can put in the revenues after developing the various assumptions.  Then, after using the INDEX function, you can put the new revenues and compute the total revenues as illustrated in the screenshot below.

Step 3: Create New Forecast with the Alternative Assumptions as Well as the Original Case
-----------------------------------------------------------------------------------------

Keep this on a separate page and make sure the original forecast still works.  I suggest using the generic macros with the colour codes so you can see where everything comes from.  You can start by copying the company case from Step 1 and making sure that there are formulas for all of the subtotals in the income statement and the cash flow like for gross income, EBITDA, net cash flow after capital expenditures etc.

Once you get to the balance sheet, just about all of the items should already be somewhere in the sheet except for the equity balance.  This is standard in corporate modelling where you can create an equity balance after working through the cash flow statement and the income statement.

As usual, the balance sheet test is the big deal. I have shown an example of the balance sheet tests in the screenshot below.

Step 4: Graphing Assumptions and Outputs
----------------------------------------

You can make flexible graphs with by going down a spread sheet

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9541&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.982074700829854)