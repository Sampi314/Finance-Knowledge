# Cash Flow Waterfall and Financial Statements

**Source:** https://edbodmer.com/cash-flow-waterfall-and-financial-statements

---

After you have finished the debt parts of the model you need to go around an compute the CFADS. The difficult issue in computing CFADS is that taxes, interest income are part of the CFADS calculation. But these items depend on the debt which in turn depends on the CFADS.  There can also be an issue with changes in the DSRA which can potentially affect the CFADS and is driven by DSRA and debt.  When setting-up the model to get ready for the circular reference, you should go all the way to the cash flow statement where CFADS is computed.  This requires computation of taxes in a profit and loss statement and setting-up a cash flow waterfall (cash flow statement number 2).

In structuring the profit and loss statement you must include some kind of amortisation or depreciation on financing elements that have been capitalised. I insist that you keep the depreciation expense is separated between amounts that are finance related and base amounts that are associated with capital expenditures, development costs and other items. The base depreciation is necessary for computing the operating taxes and if you mix up the IDC depreciation that is influenced by financing, your project IRR will be wrong.  Therefore, I suggest putting the depreciation on IDC and fees near the profit and loss statement where you will compute the taxes paid after financing.  This is illustrated in the screenshot below where depreciation rate on IDC and fees is assumed to be the same as the depreciation rate on base assets.

The rest of the profit and loss statement is standard as shown in the screenshot below.  The IDC depreciation and the fee amortisation are included as separate items. As in so many other models, the a net operating loss is computed with MIN and MAX functions. The MAX function is used to test whether the EBT is positive or negative.  The MIN function is used to test whether the balance of the NOL can be used when there are positive taxes.  The one thing that this does not have is expiration of NOL’s. This is a difficult problem addressed in the corporate finance section of the website.

![](https://edbodmer.com/wp-content/uploads/2019/01/A-Z-Profit-and-Loss.png)

### Cash Flow Waterfall and DSCR Calculation

The final statement that you can develop for the structuring section is the cash flow waterfall and the DSCR calculation.  The DSCR should be the same as the DSCR that you entered as an input. To avoid circular references I have made an error on purpose and not subtracted the taxes in computing the CFADS.  This is shown in the screenshot below.  Note that in the screenshot, the DSCR is the same as the DSCR input. The only confusing thing is where to put the changes in DSRA.  I put the change in the DSRA after the CFADS so it does not affect the DSCR and sculpting and debt sizing.  I address the issue of either putting the DSRA in the CFADS or as an adjustment to debt service in the advanced section. Now we have to deal with circular references.

![](https://edbodmer.com/wp-content/uploads/2019/01/A-Z-Debt-Cash-Flow-Waterfall.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8394&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9496&rand=0.22076413023774866)