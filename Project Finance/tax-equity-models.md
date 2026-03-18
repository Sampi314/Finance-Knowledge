# Modelling Tax Equity Structures (U.S. Renewable Energy)

**Source:** https://edbodmer.com/tax-equity-models

---

I have tried to work through tax equity issues associated with U.S. partnerships for a number of years. The more detailed pages of this section of the website work through general modelling issues in creating partnership and lease structures and in modelling the transactions. More detailed pages work through the capital accounts that can limit the tax benefits to the tax investor. The detailed webpages work through general flip structures with IRR flips and fixed term flips. Then, I discuss the details of capital accounts, suspended losses, DRO’s and other complexities in detail.  In describing the details of the various tax terms and constraints. Unlike some of the other subjects, I include a lot of reference materials with details on the definitions of different terms. I have worked through the

![](https://edbodmer.com/wp-content/uploads/2020/10/image-53.png)

Here is what a friend of mine told me in an e-mail about tax equity: “the tax equity structures drive everyone crazy, except the blowhard Tax Equity legal counsel, who love to  charge $750 hr redlining precedent deals.  The structures are getting a bit more complex lately (norm now is PAYGO structure and sometimes bring in Back Leverage, also stupid Safe Harbor requirements to qualify for PTCs). Off takes are also much more complex, most now not traditional utility PPAs, but corporate PPAs (essentially a SWAP aka contract for differences) and also a new product called Proxy Revenue Swaps, and/or traditional Hedges (or combination of all the above).”

I have put some of the issues associated with tax equity into the slides that you can download below.

**[Power Point Slides that Work Through Modelling and Accounting Issues Associated with Tax Equity Financing](https://edbodmer.com/wp-content/uploads/2018/04/Tax-Equity.pptx)
**

Tax Equity Analysis for U.S. Renewable Energy Projects
------------------------------------------------------

The files below are examples of models with tax equity flip structures using alternative methods of determining the investment of tax equity investors. A tax equity structure works as a partnership where cash flows are split between alternative parties. Much of the analysis involves efficiently a cash flow waterfall where the cash flow is split in a different manner before and after the flip. To compute the timing of the flip you can set up an account that maintains the present value of the first senior facility and accumulates the cost of funds at the flip rate. This can be accomplished by using sub-totals in the cash flow statement and then using the MIN function with the balance of the account that maintains the value of the senior securities. The files include some some discussion of how the flip structures work and it demonstrates how to evaluate the flows and risks to alternative investors. The file demonstrates that you can use accounts similar to cash sweeps with subordinated debt to establish flip timing and cash flow waterfalls. The key is to use a MIN function and test the tax equity flip in two steps.

Tax equity structures can be affected by limitations on the tax deductions if an equity capital falls to a value below zero. There are different ways to define capital and the capital must be above zero from both tests in order for deductions to be allowed for the senior tax investor. If have seen a lot of absurd models that over-complicate the tests and have macros or circular references. If the cash flow waterfall is structured correctly and the timing is consistent the constraints can be modelled in a structured manner. I have not put up videos for this issue yet.

Tax Equity Analysis.xlsm

Solar Annual Model.xlsm

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=812&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8496&rand=0.15999643022971577)