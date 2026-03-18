# When Modelling Dozen Work

**Source:** https://sumproduct.com/thought/when-modelling-dozen-work/

---

[Home](https://sumproduct.com/)

\> When Modelling Dozen Work

*   May 14, 2025

When Modelling Dozen Work
=========================

The quick and dirty dozen tips for checking over spreadsheets.

When Modelling Dozen Work
=========================

_Liam Bastick highlights some of the common mistakes prevalent in financial modelling / Excel spreadsheeting. This article considers how to help yourself check over a spreadsheet you’ve built with 12 top tips._

### Self-Review Checks: The Quick and Dirty Dozen

Every year, around the world, many millions are spent on having key spreadsheets and financial models audited by third parties. I know there is a time and a place for this (I know this because our firm audits models for a living!), but companies and analysts can help themselves by building models to key established principles (such as ICAEW’s 20 Principles for Good Spreadsheet Practice or our own company’s CRaFT: Consistency, Robustness, Flexibility and Transparency).

Companies and their staff can also create a checklist of tasks that can be performed by those involved in the construction of the model. Whilst it is nigh on impossible to identify holes in one’s own logic, there are other things that can be performed to reduce the risk of error in the spreadsheets created.

The following is a list of 12 such tasks that may be performed as part of a self-review. Although not as robust, independent or objective as a third party model audit, it is better than nothing.

1\. **Use Excel’s Background Error Checking** – Strictly speaking, this should be instigated during the model development phase as it can assist the modeller throughout construction.

To enable this functionality, go to Excel’s Options (**ALT + T + O**) and in the ‘Formulas’ section, ensure that the ‘Enable background error checking’ tick box is checked. Once activated, the user can select which error checking rules should be catered for by inspecting the ‘Error checking rules’ section directly beneath this check box.

![](https://sumproduct.com/wp-content/uploads/2025/05/5638c6c11f5b83eb4efca10c93fe5139.jpg)

This functionality does not prevent errors from occurring, but potentially erroneous cells are highlighted by Excel in a fashion similar to cells that include comments, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/8376024e7f4015a6f9ecc67b59ef31bb.jpg)

The problem with this approach is it is easy to miss this annotation, but it is better than not using it.

2\. Use Excel’s Formula Auditing tools – In the ‘Formulas’ tab of the Ribbon, use the tools in the ‘Formula Auditing’ section of the toolbar. In particular, ‘Error Checking’ is useful (although it may only be applied to one worksheet at a time) as it highlights a lot of issues Excel is programmed to consider as “dubious” (e.g. inconsistent formulae, #DIV/0! errors).

![](https://sumproduct.com/wp-content/uploads/2025/05/b5549fc08caf4cae6f8c65617cdd6a68.jpg)

3\. **Find Prima Facie Errors** – There are glitches in Excel and occasionally, a prima facie error may slip through. These obvious errors are particularly embarrassing to miss, as these are usually identified by end users picoseconds after a model has been handed over.

There is a simple sure-fire check: **CTRL + F** (Excel’s ‘Find’ functionality).

![](https://sumproduct.com/wp-content/uploads/2025/05/de42cbc10d9dee49559849b9924828cf.jpg)

Simply type ‘#’ in ‘Find what’ (the obvious errors all begin with ‘#’), but then click on the ‘Options’ button to display the options and change the ‘Within’ setting to ‘Workbook” and then look at ‘Formulas’, ‘Values’ and ‘Comments’ in turn using the ‘Find All’ button to correct any issues identified.

4\. **Review inconsistencies in formulae** – I have discussed this issue before (please see [Common Modelling Errors: Spotting Inconsistencies and Plugs](https://www.sumproduct.com/thought/spotting-inconsistencies-and-plugs)
) using **CTRL +** and **CTRL + SHIFT +** to find inconsistent formulae in rows and columns respectively.

![](https://sumproduct.com/wp-content/uploads/2025/05/6e43630346a7403c3517ab1dda39592c.jpg)

5\. **Look for errors in unintentional links in range names** – Open the Name Manager in Excel (**CTRL + F3**) to both identify links and range names containing errors (the latter may be done by a simple filter).

![](https://sumproduct.com/wp-content/uploads/2025/05/ab43e2772c332da8d900d8abc4003c61.jpg)

6\. **Locate unintentional links** – As long as there are models there will be unintentional links. **CTRL + F** and searching for ‘\[‘ will uncover many in a model, but I have already discussed these previously in Common Modelling Errors: Phantom Links.\
\
7\. **Perform high level analysis** – Depending upon the purpose and scope of the model built, you can create a check list of items to review for each model (e.g. does your Balance Sheet balance? Does the cash in the Cash Flow Statement reconcile to the amount in the Balance Sheet? What is my forecast days receivable?). Using accounting ratios focusing on profitability, liquidity and gearing can be beneficial too.\
\
8\. **Create “quick” charts** – For key outputs, you can graph the data momentarily. Simply highlight the data and press the **F11** function key for the chart on a new worksheet or **ALT + F1** for the chart on the same worksheet, _viz._\
\
![](<Base64-Image-Removed>)\
\
Do the charts make sense? Are there unseemly ‘blips’ or inconsistent trends? Can dramatic changes be readily explained? These rough and ready charts can highlight calculation mistakes in an instant upon occasion.\
\
9\. **Close and re-open** – Do you get unexpected error messages upon opening? This is a frequent oversight made by modellers. Are calculations set to ‘Automatic’? Are there any unexpected links, circular arguments or other error messages (_e.g._ “Not enough memory to display”)? It is better that you discover these issues before your recipients do.\
\
10\. **Spell check** – Nothing looks less professional than opening a Dashboard Summary to look at the “Selas Turnover” or items labelled incorrectly. There is really no excuse for not spell checking a model (‘Review’ tab of the Ribbon has a spelling check). Why is it so important? I have trained modellers for over 25 years and end users expect that a modeller has paid meticulous attention to detali _(Ed – that’s a joke)_: spotting obvious errors and typos reduces a model’s – and a modeller’s – credibility. Not career enhancing at all.\
\
11\. **Printing and viewing** – Not strictly speaking an error, how many times have you decided to print out a model sent to you only to find it print over several reams of paper that even Tolstoy would have been proud of? It is worth taking time to set up print margins and included headers and footers. Also, each page should be reset (**CTRL + HOME**) and saved on the front page so that models are not opened with the end user finding themselves in cell **GG494** of a sheet called “ID\_Rev\_MR”. Been there, done that, bought the consequences.\
\
12\. **Protection** – If as a modeller you have invested sleepless nights in getting a model to work, you do not really want an end user typing “17” over a sophisticated formula that has taken hours to get precisely right. These unowned hard codes often come back to haunt the modeller – unfairly – and cast doubt over the credibility of an otherwise robust model. Take the time to protect cells, worksheets and the workbook as required to avoid these issues.\
\
At the end of the day, getting an independent, objective review of the model trumps all of my suggestions above. This may seem like blatant self-promotion, but I can provide many war stories concerning the value of a model audit. Many baulk at this option due to cost, but what is the cost for a business that makes decision based on flawed forecasts?\
\
[More Thoughts](https://www.sumproduct.com/thought)\
\
*   [Log in](https://sumproduct.com/thought/when-modelling-dozen-work/#0)\
    \
*   [Register](https://sumproduct.com/thought/when-modelling-dozen-work/#0)\
    \
\
Remember me \
\
Sign in\
\
      \
\
[Forgot your password?](https://sumproduct.com/thought/when-modelling-dozen-work/#0)\
\
Create account\
\
      \
\
Lost your password? Please enter your email address. You will receive mail with link to set new password.\
\
  \
\
Reset password\
\
[Back to login](https://sumproduct.com/thought/when-modelling-dozen-work/#0)\
\
[](https://sumproduct.com/thought/when-modelling-dozen-work/#0 "close")\
\
top