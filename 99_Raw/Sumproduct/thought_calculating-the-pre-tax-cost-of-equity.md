# Calculating the Pre-Tax Cost of Equity

**Source:** https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/

---

[Home](https://sumproduct.com/)

\> Calculating the Pre-Tax Cost of Equity

*   May 14, 2025

Calculating the Pre-Tax Cost of Equity
======================================

How to calculate the pre-tax cost of equity.

Calculating the Pre-Tax Cost of Equity
======================================

If you have ever been involved in a valuation, you will appreciate a financial model is never far away. No matter what the technique used, access to valuation software is crucial. And Excel is probably the most common software of all for this purpose.

As aforementioned, there are many techniques employed to value an asset, a project, a business, a shareholding, and so on. However, one is arguably more common than the rest these days – Net Present Value (NPV) using discounted cash flows.

As many readers will know, the idea of a discounted cash flow (DCF) is a simple one. Perhaps the easiest way to think of it is as follows:

*   Let’s assume inflation is running at 10% (and we will assume this is after tax as we all earn our wages after tax and increases in spending affect this after-tax wage)
*   Something that costs $100 this year will cost 10% more next year, _i.e._ $110
*   Something that costs $110 next year will cost 10% more the year after, _i.e._ $121
*   Something that costs $121 in that year will cost 10% more the following year, _i.e._ $133.10
*   However, they are all worth the equivalent of $100 now (as we “discount” these _future values_ back to their _present values_).

![](https://sumproduct.com/wp-content/uploads/2025/05/5bfc2167e7e3ea19e850be81b98d4dd2.jpg)

Note that all of these valuations are for a _point_ of time not a _period_. This is a common mistake in modelling. We have to understand when we assume the cash flows will occur. The three most common assumptions are at the start, the middle or the end of the period in question. This assumption will obviously vary the overall valuation as a consequence.

Valuations include both cash inflows and cash outflows. Adding up all these positive and negative present values, provides a netted off total: the Net Present Value (NPV). The aim is to generate a positive return (a positive NPV) for a given rate of discounting, known as the _discount rate_.

This discount rate is a mix of both debt and equity. The cost of debt is easy to source: it’s the marginal cost of borrowing the next $1 and is quoted almost invariably pre-tax (_e.g._ banks are compelled to cite this rate).

However, cost of equity is a more complex beast. It’s the required rate of return for the shareholders and there are several methods of estimating it, most frequently used is the Capital Asset Pricing Model (CAPM). This is not an article _per se_ on valuation, so I won’t start a long monologue on betas, correlations _et al_ suffice to say that this rate is always estimated post-tax _because shareholders always receive their money after tax_.

We have to compare apples with apples, so since we live in an after-tax world we need to quote the cost of debt after tax too. Allowing for simplifying assumptions such as the tax credit is received when the interest payment is made, this allows us to use the formula

**Post-Tax Cost of Debt = Pre-Tax Cost of Debt x (1 – Tax Rate)**.

For example, if the pre-tax cost of debt is 8% and tax is charged at 30%, then the post-tax cost of debt will be 8% x (1 – 30%) = 5.6%. That’s pretty straightforward. We can then calculate the blended rate known as the _Weighted Average Cost of Capital_ (WACC):

![](<Base64-Image-Removed>)

Sometimes, such as comparing two projects in different tax regimes, it’s easier to evaluate projects / companies pre-tax. This is where mistakes get made. If I have a project with a post-tax NPV of $700m and a tax rate of 30%, many will calculate the pre-tax NPV to be $1,000m being $700m divided by (1 – 30%). This is incorrect.

Valuation theory states that if you discount pre-tax values at the pre-tax discount rate, the NPV of this calculation must equal the NPV of evaluating the post-tax cash flows at the post-tax discount rate. This is a fundamental principle that many are either unaware of or else forget. Don’t make such a mistake.

The problem is, how do you calculate the pre-tax cost of equity? It’s a theoretical construct and is not equal to

**Pre-Tax Cost of Equity = Post-Tax Cost of Equity / (1 – Tax Rate)**.

As model auditors, we see this formula all of the time, but it is wrong. Pre-tax cash flows don’t just inflate post-tax cash flows by (1 – tax rate). Some cash flows do not incur a tax charge, there may be tax losses to consider and timing issues too. And that’s just for starters. No, the pre-tax cost of equity is a balancing figure. It’s the rate that generates the correct pre-tax WACC so that the pre-tax and post-tax NPVs are equal.

If you have more than four periods in your discounted cash flow, there’s a mathematical result from a topic called Galois Theory that proves you cannot solve this formulaically (I’ll leave you to prove that!). We have to “guess” the answer and to do that we’ll need to use Excel’s Goal Seek functionality if we are using Excel as our valuation software of choice.

So how do we do this?

I will demonstrate with the [attached Excel file](https://sumproduct.com/assets/thought-files/pretax-cost-of-equity/amend/sp-calculating-the-pre-tax-cost-of-equity.xlsm)
 as follows. Let’s use the following assumptions:

![](<Base64-Image-Removed>)

The Post-Tax WACC has been calculated using the formula

**\=(PreTax\_Cost\_of\_Debt\*(1-Tax\_Rate)\*Proportion\_of\_Debt) + (PostTax\_Cost\_of\_Equity\*(1-Proportion\_of\_Debt))**

where the inputs _(above)_ have been given the range names shown in grey _(to the right)_. It’s the Excel equivalent of our formula cited above.

There’s more though:

*   The terminal value is an amount applied in the final period of a cash flow to represent the value of future cash flows after this point in time. It is typically calculated in perpetuity and uses the formula

![](<Base64-Image-Removed>)

*   Some valuers will use a different discount rate for this calculation, but this is highly debatable (I will use the same rate – the WACC – throughout)
*   The cash flow in the final period may have to be adjusted to smooth out capital expenditure and depreciation (for tax calculations) but that is a story for another day. What is important to understand is that the final period’s cash flow before creating a terminal value should have achieved a “steady state”
*   The “tolerance” is simply an indicator for an alert check: it’s dangerous to place too much value in the terminal value. I have used the rather unrealistic 90% here as the amount that the present value of the terminal value may be of the overall NPV before an alert is triggered. A more common tolerance would be 60%, but hey, I get my 6’s and 9’s mixed up all of the time (I believe “96” is very safe sex…).

The model requires further assumptions:

![](<Base64-Image-Removed>)

I have just used “100” as my relevant cash flow (_i.e._ not including any costs of financing as this is already included in the discount rate) for each period, but it’s the other assumptions that require further discussion.

The number of periods is used to determine how many periods of discounted cash flows there will be (the _explicit forecast period_) before adopting the terminal value (_the implicit forecast period_) for further periods. My [attached Excel file](https://sumproduct.com/assets/thought-files/pretax-cost-of-equity/amend/sp-calculating-the-pre-tax-cost-of-equity.xlsm)
 will calculate for up to 20 periods, even allowing for a shorter first period (as the valuation will start from the **Model\_Start\_Date**).

The tax delay assumption is used to build in a delay for the payment of tax. It’s important to realise that DCFs are calculated using cash flows and it has to be when the tax is paid, not when the liability arises.

The timing of the cash flows can be start, middle or end as discussed earlier. Consequently, three discount rates have been computed _viz._

![](<Base64-Image-Removed>)

These cells use the formula

**\=(1+PostTax\_WACC)^(#Days\_From\_Valuation\_Date/Days\_in\_Year)**.

The **Days\_From\_Valuation\_Date** is calculated as:

*   The number of days between the valuation start date (here, this is the **Model\_Start\_Date**) and the first day of the period when the timing of the cash flows is at the start of the period
*   The number of days between the valuation start date and the final day of the period when the timing of the cash flows is at the end of the period
*   The average of the above when the timing of the cash flows is in the middle of the period.

I have then used **INDEX MATCH** to select the appropriate discount rate for the valuation:

**\=IF(Counter<=Number\_of\_Periods,INDEX(Discount\_Factors\_for\_Period,  
MATCH(Timing\_of\_CashFlows,Labels,0)),””)**

We can then calculate our NPV:

![](<Base64-Image-Removed>)

Note that I have calculated this long-hand. That’s because when we use dates and periods may be of unequal lengths, the Excel function **XNPV** may not always give the right answer. And even if it did – this is clearer.

As stated earlier, the TV Tolerance just checks that the terminal value (here, 1,050), when considered in its present value form, is not an excessive amount of the total NPV.

Now, I know what the NPV is for this scenario. I also know the pre-tax cash flow, the pre-tax cost of debt and the mix of debt to equity. The only thing missing is the pre-tax cost of equity, so, given there are more than four periods, this will have to be solved for using Excel’s Goal Seek feature.

![](<Base64-Image-Removed>)

All I have to do is put together the above calculations where the discount rate is based upon the Pre-Tax WACC. I can set the only assumption cell (Pre-Tax Cost of Equity) to anything I like as this is a “dummy” value. Then, I activate ‘Goal Seek’ by going to the ‘What-If Analysis’ drop-down menu in the ‘Forecast’ grouping of the ‘Data’ tab on the Ribbon (**ALT + A + W + G**):

![](<Base64-Image-Removed>)

This activates the ‘Goal Seek’ dialog box:

![](<Base64-Image-Removed>)

Then, you should set the **PreTax\_NPV** output to the value in the **PostTax\_NPV** cell by changing the **Pre\_Tax\_Cost\_of\_Equity** input (the cell references may differ depending upon how you model this). Goal Seek should then compute the correct Pre-Tax Cost of Equity rate to make the two values equal. In our example above, this is 22.55%, which is 5.41% higher than using the incorrect gross-up of the post-tax rate (17.14%).

It’s that easy.

However, you can make it easier. The problem with this solution is that you have to manually invoke the Goal Seek feature each time you change a relevant input. This can be automated by using VBA (_i.e._ amacro) instead. In the [attached Excel file](https://sumproduct.com/assets/thought-files/pretax-cost-of-equity/amend/sp-calculating-the-pre-tax-cost-of-equity.xlsm)
 if you right-click on the sheet tab and select ‘View code’ from the shortcut menu, you can paste the following code in:

Private Sub Worksheet\_Change(ByVal Target As Excel.Range)

Dim rng As Range

For Each rng In Target

Debug.Print rng.Address

    If rng.Address = Range(“PreTax\_Cost\_of\_Debt”).Address \_

        Or rng.Address = Range(“PostTax\_Cost\_of\_Equity”).Address \_

        Or rng.Address = Range(“Tax\_Rate”).Address \_

        Or rng.Address = Range(“Proportion\_of\_Debt”).Address \_

        Or rng.Address = Range(“Terminal\_Value\_Switch”).Address \_

        Or rng.Address = Range(“Growth\_Rate\_in\_Perpetuity”).Address \_

        Or rng.Address = Range(“TV\_Tolerance”).Address \_

        Or rng.Address = Range(“Number\_of\_Periods”).Address \_

        Or rng.Address = Range(“Tax\_Delay”).Address \_

        Or rng.Address = Range(“Timing\_of\_CashFlows”).Address \_

    Then

        Range(“PreTax\_NPV”).GoalSeek Goal:=Range(“PostTax\_NPV”).Value, ChangingCell:=Range(“PreTax\_Cost\_of\_Equity”)

    End If

    For i = 1 To 100

        If rng.Address = Range(“PreTax\_Cash\_Flows”).Item(i).Address Then

            Range(“PreTax\_NPV”).GoalSeek Goal:=Range(“PostTax\_NPV”).Value, ChangingCell:=Range(“PreTax\_Cost\_of\_Equity”)

        End If

    Next i

Next rng

End Sub

This can be shown in place here:

![](<Base64-Image-Removed>)

After closing this window once pasted, the macro will work if any of the inputs (other than Pre-Tax Cost of Equity) are modified. It should be noted though, it will not update if values are changed on other sheets as the code is presently written.

**_Word to the Wise_**

This article is not intended to be a comprehensive discussion on valuations. WACC is not used for all cashflows and sometimes the cost of equity is used (_e.g._ to value shares) instead. The [attached Excel file](https://sumproduct.com/assets/thought-files/pretax-cost-of-equity/amend/sp-calculating-the-pre-tax-cost-of-equity.xlsm)
 can still calculate this – just set the proportion of debt to 0%.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/#0)
    
*   [Register](https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/#0)

[](https://sumproduct.com/thought/calculating-the-pre-tax-cost-of-equity/#0 "close")

top