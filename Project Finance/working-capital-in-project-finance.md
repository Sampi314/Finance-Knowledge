# Working Capital in Project Finance

**Source:** https://edbodmer.com/working-capital-in-project-finance

---

This page reviews working capital issues in project finance models. Depending on the way you structure your model, working capital can be a very simple matter or a complex issue. Some issues in modelling working capital in project finance models include: (1) modelling initial working capital as part of the sources and uses of funds before commercial operation; (2) modelling a working capital facility and excluding the working capital facility from gearing and the capital structure for debt sizing; (3) modelling working capital needs in the initial period of operation through sculpting or a grace period; and (4) the highly complex task of modelling working capital when the period of the model is shorter than the days of working capital outstanding.

In developing this website my friend Mike Flynn helped a great deal.  He created diagrams of how the problem of working capital can be modeled if the time period of the model is monthly and the accounts receivable are not collected for 45 or 100 days.

https://studio.youtube.com/video/DTDixx-6pUw/edit

Part 1: Initial Working Capital in Project Finance
--------------------------------------------------

It is not uncommon that there can be delays in receiving revenues when a project starts. In one example I saw, a big portion of revenues was delayed for twelve months. This working capital must be financed as no cash flow will be coming into the project. There are a number of alternative possibilities for financing this initial working capital. Each of the working capital methods can lead to different equity returns. Here are a couple of alternatives:

1.  Accumulate the working capital over the first twelve months. After accumulating the working capital, create a cash reserve account and fund this account from long-term debt and equity financing. You can see this in the sources and uses of funds statement as a cash need. Then, create the reserve account and withdraw funds from the account as the working capital is reduced. With this method, the working capital results in increased debt and equity financing
2.  Create a working capital facility that is not included in the sources and uses of funds statement and in long-term financing and is not included in the debt to capital ratio. This working capital facility will reduce cash flow to the long-term debt.
3.  Compute sculpting with the cash flow after working capital changes which can result in negative amortization in the initial year. This can be like negative amortization that occurs for ramp-ups in toll road financing. If the working capital is less, you can include a grace period in the sculpting calculation.
4.  Include the working capital period in the sources and uses of funds and allow draws for the working capital period. This will increasing the long-term funding and result in a higher debt to capital ratio than method number 2.

Part 2: Working Capital Facility
--------------------------------

When I saw working capital debt in project finance I was surprised to see that working capital debt facilities were not included in the debt to capital ratio and that interest and fees on the working capital facility were not included in the DSCR. But that is the rule and maybe it makes sense because the working capital risk is very different from the overall risk of the project. Note that the VAT facility can be considered similar and does not affect the debt to capital ratio or the DSCR.

The general idea of a working capital facility is to leave debt and equity investors where they would have been had there been no working capital movement. If there was no working capital movement, then the recorded revenues and the recorded operating expenses would be real cash flow. So if you have to make an investment in working capital, you can think of a working capital loan as getting back to where you would be. I have made a small example to demonstrate this. The first screenshot illustrates the example with delay in revenues and expenses. Note that the revenues are growing and that the working capital increases until end of the period. This creates positive working capital (another example will be presented below). The delay in collection and payment means that the cash flow is delayed by one period.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-8.png)

If you make a loan to cover the working capital (no interest is assumed), then you can borrow the working capital needs as illustrated below. In this case with positive working capital needs, the amount is borrowed. At the end of the day, the cash flow to investors is what it would have been if the revenues and expenses were cash. You can use a simple MAX function in this case to compute the loan balance.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-9.png)

The situation is somewhat more complex when the revenues and expenses move up and down. In the next case revenues are below expenses in the early period and then they reverse. In this case you could put in a cash balance that is like a negative loan. Note that the working capital balance starts as a negative amount and then switches to a positive amount.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-10.png)

In this case you could ignore the first negative 35 change and then put the 10’s in a loan balance. This would create too big a loan that could not ultimately paid by the positive cash flow. In this case it would be better to set up a cash account that could then be used like a negative debt facility. This is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2021/05/image-11.png)

The file associated with the example above is attached to the button below.

**[Excel File with Example of Working Capital Facility in Project Finance to Offset Working Capital Movements](https://edbodmer.com/wp-content/uploads/2021/05/Working-Capital-Example1.xlsx)
**

Part 3: Cash Flow with Minimum Cash and Working Capital Facility
----------------------------------------------------------------

In the file below I work through some working capital issues with a series MIN and MAX statements and monthly cash flow.

**[Excel File with Illustration of Working Capital Calculation with Revolving Credit Facility and Cash Account](https://edbodmer.com/wp-content/uploads/2021/05/Working-Capital.xlsx)
**

Introduction to Working Capital Problem
---------------------------------------

In a project finance model, working capital arises from computing revenues with a meter and then sending a bill out at the end of a month.  After sending out the bill you may have to wait more than a month to get paid. Indeed, in some places, the delay in payments can become a big issue and you may have to model downside scenarios where you are not paid for a year or longer.  When modelling working capital, a few basic points should be considered:

*   The working capital calculations in a project finance model come from revenues and operating expenses and perhaps taxes. If debt repayments and interest come are semi-annual and your model is also semi-annual, you do not have to worry about these.  This is why you make you model semi-annual.
*   You can generally compute working capital after revenues and expenses (i.e. before financing and taxes if you make sensible structured model that starts with operations).
*   As long as the working capital days are less than the days in the period (e.g. the accounts receivable days are 30 and the period is semi-annual), then the days as a percent of the days in the period can be used to derive working capital.  You can then compute the total amount of receivables and payables.
*   Once you compute the total amount of receivables and payables, you can compute the change in working capital that is an item in CFADS and cash flow analysis.

Alternative Ways to Finance Initial Working Capital
---------------------------------------------------

A few of the ways to deal with the financing of working capital include:

1.  Computing initial working capital as part of the sources and uses of funds before commercial operation;
2.  Creating a working capital facility and excluding the working capital facility from gearing and the capital structure for debt sizing;
3.  Including working capital needs in the initial period of operation through sculpting or a grace period in debt;

Difficult Problem when the Days Outstanding is Longer than the Working Capital Period
-------------------------------------------------------------------------------------

UDF method

Problem when periodicity changes

Insert description

Video on

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9779&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11892&rand=0.14505660232742745)