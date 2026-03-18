# Different Debt Size – Cash Flow (P90/P50), Debt/Cap

**Source:** https://edbodmer.com/debt-sizing-with-alternative-cash-flow-p90-p50-and-debt-to-capital

---

This webpage describes how to compute debt size when different constraints such as P50/P90 and debt to capital are used. Implicitly or explicitly, banks use downside cases (e.g. P99), debt to capital constraints or other methods to evaluate debt size. This can be a relatively simple problem if no construction period with IDC and Fees, DSRA, income taxes, DSRA fees, multiple debt issues or other factors are considered. In these cases you can use different cases of the cash flow divided by the DSCR and the NPV of cash flow to compute debt size. You can also compute the amount of debt from the debt to capital ratio. But if you have to compute the interest during construction, DSRA, fees, taxes and other items in each case with a circular reference, this problem can be difficult. The number of lines and the pain of re-doing all of the detailed calculations with circular references suggests that using the UDF technique may be a very good idea. A couple of files that illustrate the issue are attached to the buttons below. The first file includes a simple example without construction timing and taxes. The second example, I use construction periods, DSRA and income taxes and demonstrate how the process works with the UDF/Parallel model.

.

**[Excel File with Demonstration of How to Compute Sculpting for Multiple Debt Issues with Different Tenures and Interest](https://edbodmer.com/wp-content/uploads/2019/01/Sculpting-with-Multiple-Issues.xlsm)
**

.

**[Excel File with Advanced Project Finance Issues Including Sculpting for Multiple Debt Issues and P50/P99 etc.](https://edbodmer.com/wp-content/uploads/2021/05/Advanced-Course.xlsm)
**

.

.

Mechanics of Computing Debt Size with Alternative Cash Flow
-----------------------------------------------------------

![](https://edbodmer.com/wp-content/uploads/2021/09/image-11.png)

.

**[Excel File with Analysis of Debt Funding for Different Solar Projects in a Portfolio with Macro and Indirect Function](https://edbodmer.com/wp-content/uploads/2021/09/Solar-Fund-Example.xlsm)
**

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14524&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8224&rand=0.22174612830076845)