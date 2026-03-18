# Non-Recourse Debt and Minimum Gain

**Source:** https://edbodmer.com/minimum-gain

---

On this page I discuss the minimum gain and the minimum gain charge back in tax equity  structures that is a particularly painful aspect of tax equity modelling.  If I can take the fear and the mystery out of the minimum gain (for myself and for you), this would be a big success.  To take out the minimum gain fear which I find completely natural, I try to first define what is meant by the term minimum capital gain — is it a capital gain; a gain from an assumed foreclosure; where does that minimum gain come from; and why does non-recourse debt at the LLC  partnership level create a minimum gain for purposes of computing the tax equity (but not back leverage). I also attempt to explain the effects of the minimum gain and the minimum gain charge-back on the investor IRR’s and in particular, the tax investor IRR.  The manner in which the minimum gain affects the economics of tax equity project finance transactions is driven by how it affects the taxable income to the tax investor.  This is in turn driven by the inside capital account (704(b)) and whether the minimum gain and non-recourse debt can reduce the possibility of the inside capital account going down to zero and creating a tax exposure.  The outside capital account is a measure of the allocated assets in the partnership and you add the equity capital to shared liabilities.  Other than adding shared liabilities, the outside capital is not directly affected by the minimum gain.  The outside capital does not have adjustments for the minimum gain; for the change in the minimum gain; or, for the minimum gain charge-back. 

A few questions regarding the minimum gain include: what gain are we even talking about (it sounds like some sort of gain on sale or capital gain); is it income; is the minimum gain cash; how does the minimum gain and the associated minimum gain charge back affect the inside basis and the taxable income. The next question is whether how the minimum gain affects both taxable income and the calculation of inside capital.  Here are a couple of answers.  The minimum gain can be defined as a hypothetical foreclosure sale at book value — if the debt is more than the book value, there would be an implied gain from to the equity holder who does not have to pay off all of the debt. The minimum gain is the debt minus net asset cost (when positive).  The change in the minimum gain (positive) is added directly to the inside capital account.  The minimum gain charge-back is the amount of minimum gain when the change in the minimum gain is negative. The minimum gain charge-back is added to income and reduces the benefits of the minimum gain to the tax investor.

The fundamental reason for the minimum gain is to protect tax depreciation deductions that would be lost because of negative capital accounts that arise from debt. If your equity is reduced because of the existance of debt, and you depreciate the full tax basis of the asset, then the equity balance will become negative.  For example, say the asset cost is 1,000 and the debt is 500.  If you assume all of the cash income is paid in dividends, the equity balance will be -500 when the asset is depreciated (assuming the debt is not paid down).  Retained earnings are -1,000 from the depreciation and the paid in equity capital was only 500 because of the debt financing. Without accounting for the minimum gain, this -500 in equity capital causes a stop loss in because the account cannot be negative and therefor taxable income.  This is unfair because the equity investor and not the lender is supposed to get the benefit of depreciation.

So, now I begin to work through the horrible minimum gain details. I begin by reviewing some tax equity models with minimum gain spelled out. Some basic points about the minimum gain is that it arises when there is non-recourse debt at the partnership SPV. It does not occur when there is back leverage.

Definition of Minimum Gain
--------------------------

I have had trouble finding a careful definition of the minimum gain that explains the ideas and the impacts on investors.  One article stated: “Minimum gain is the amount by which the non-recourse debt exceeds the Section 704(b) basis in the property secured by the debt.” Let’s translate this.  The sentence implies that you should first compute the 704 basis in property which I is the amount of debt less the amount you spend for capital expenditures less the accumulated depreciation.  In the excerpt below, the minimum gain is defined as the gain that would be experienced on the hypothetical sale of the plant at the net tax value on the books.  This seems silly as the value of the an asset does not really go down with the accumulated tax depreciation.  But go with this crazy assumption and the tax basis goes down to zero and you sell the asset for nothing.  Then, if there is debt outstanding, with your assets that are worth zero, you have somehow realized a gain.  Maybe you have got your money back from depreciation but those stupid debt holders are still financing your company. 

If you look at the first screenshot below, you can see that minimum gain is defined as the amount of debt above the tax basis of the asset.  But the minimum gain is only computed when the debt is above the net value of the assets.  This could be written as the following formula:

**Minimum Gain = Max(Debt – Net Asset Value,0)**

Note that the minimum gain calculation only applies to the debt at the LLC and not to back leverage.  To again try to explain this, suppose the asset cost is 1,000 and you finance this asset with 500 of debt and 500 of equity.  You pay out all cash as dividends and the depreciation of 800 in the third year means the cash dividends are more than the income resulting in negative retained earnings.  In the third year,  the net value of the asset is only 200.  If you have not repaid any debt, the debt exceeds the net value by 300 this is 500 of debt minus 200 of asset value.  If you have already got back 800 in cash through depreciation, and you only put in 500 to the project, you have a minimum gain of 300.  If you sold the asset for 700 and you received cash of 800, you would have a gain of 800 because the lenders took a loss of 100. 

Other key calculations of the minimum gain include how the minimum gain affects the inside capital balance and the taxable income. The outside basis is not affected by the minimum gain.

**Inside Capital (704(b)) —> Add positive changes in minimum gain**

This increase in capital does not come along with income, so it decreases income that would otherwise be paid from the negative capital constraint.  As noted above, this increase in minimum gain offsets the increase in income that would otherwise have reduced the legitimate depreciation deductions that accrue to owners of the asset.

The final part of the minimum gain calculation involves the minimum gain charge-back.  The minimum gain charge is computed when the change in the minimum gain becomes negative.  As the net cost of the asset is generally near zero after year five, the minimum gain charge back occurs when the debt decreases.

![](https://edbodmer.com/wp-content/uploads/2019/09/Minimum-Gain-Simple.jpg)

Another article states: “The Regulations create a concept called partnership minimum gain. Minimum gain is the amount by which the non-recourse debt exceeds the Section 704(b) basis (this is nets asset balance, not the  equity balance) in the property secured by the debt. The concept is that a non-recourse deduction can be allocated to a partner to cause its capital account to be negative, even without a partner obligation to restore that negative capital account.”

The idea of the minimum gain implies that if the capital account is negative because of the debt, that this negative amount should not be used to limit the tax deductions of the tax investor.  The manner in which the minimum gain is computed in a couple of models that I have studied is shown in the excepts below.  Note that the beginning of the minimum gain calculation is the comparison of debt with the net asset value of the project after depreciation.  This part of the minimum gain is clear.  The first screenshot below shows the calculation under the minimum gain section.  Note that as the minimum gain affects the capital accounts that it should be computed above the capital accounts.

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Minimum-Gain-Computation.png)

The screenshot below shows another example of computing the minimum gain.  The calculation begins with the balance of the plant and subtracts this from the debt. This is because the negative capital account will later receive an allocation of income whenever there is a decrease in the minimum gain.

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Minimum-Gain-Complex.png)

Somebody Else’s Example with My Comments to Hopefully Make it Understandable
----------------------------------------------------------------------------

The example below is from an article that I found on general partnership tax law.  This example works through the effect on the capital account and limits on the ability to take income deductions.  I have tried to translate some things in the example to hopefully illustrate how the minimum gain works.  I have put my comments on the example in the square brackets \[\].  The example demonstrates that if there was no minimum gain in the inside capital account, taxes would be increased even though all that happened is that the depreciation was taken. In this example, the asset cost of 100 and the debt is 800.  If you assume all of the cash income is paid in dividends, the equity balance will be -100 after the asset is depreciated for three years (assuming the debt is not paid down).  Without the minimum gain, this -100 causes taxable income.  This is unfair because the equity investor and not the lender is supposed to get the benefit of depreciation.

A and B each contribute $100 to a 50-50 partnership and have no obligation to restore negative capital accounts. \[_Note that the restoration of negative capital accounts could be called the deficit reduction obligation\]_. The partnership borrows $800 from an unrelated lender on a non-recourse basis using an interest-only loan _\[the balance of the loan does not go down and you can use 800 in the examples\]_ and buy the building for $1,000. The partnership depreciates the building by $100 a year.

After the third year, the partnership has depreciated the initial $1,000 of section 704(b) basis in the building down to $700 _\[$100 per year in depreciation\].  \[Remember that when you hear 704(b) that means the inside capital account which is also called the FMV account or the book basis.\]_ At the beginning of year 3, A and B have each received depreciation deductions that caused their section 704(b) capital accounts to be zero.  _\[This means that the negative balance will be considered taxable income. If you look up to the beginning of the example, the investment of both together was 200.  So, if they paid out their income as dividends, the equity balance of both partner A and partner B could easily go down to zero._\] The article states that allocating the year 3 depreciation equally to A and B would cause their capital accounts to be negative by $50 each.  You can stand  up for the tax equity investor and say the they are supposed to get the full benefit of the tax deduction. Just because there is debt, the tax advantage of the depreciation should not be reduced.

Although the general rule is that A and B are not allowed to have negative capital accounts absent a DRO \[there would be a stop loss increase in income\], the IRS makes an exception in this case because the deduction is a non-recourse deduction that creates minimum gain ($800 non-recourse debt less $700 book basis in Building).  \[_Remember from above that when the 800 of debt exceed the tax basis of 700, that there is a gain.   In this case the gain is 100 which can be allocated between the two partners._\]

An allocation of the $50 deduction to each of A and B creates an allowable $50 deficit in each partner’s capital account.  \[_Alternatively, you can add the gain of 50 to the subtotal of the capital account balance._\] This is because that deficit is supported by $50 each of minimum gain that the partnership agreement provides the partnership will charge back if there is a later reduction in that minimum gain. \[_Note the term charge back — the debt must be paid off so that minimum gain will go to zero._\]

Minimum Gain Effect on Inside Capital (704(b)) and the Outside Basis
--------------------------------------------------------------------

The example above illustrated that the minimum gain increases the inside capital by virtue of inserting a line from the inside capital in the capital account.  In the outside basis a different adjustment is made for the minimum gain.  Note that the change in minimum gain is not included in taxable income.  If it were included in taxable income, you would have the problem of not realizing the tax depreciation.  As with discussion of computing the minimum gain, I use selected examples from models that I have re-formatted in the discussion below.  The first example illustrates how the change in the minimum gain is included in the inside basis.

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Inside.png)

To illustrate the computation of minimum gain I have created a simple model.  The model uses a simple two partner case where each partner owns 50% of the LLC. I have created this example so that you can see what happens to the partners with and with non-recourse debt as well as with and without the minimum gain adjustments.  In the screenshot below I the check boxes at the top show un-checked boxes for the debt, the charge-back and the apply minimum gain.  Note that the total amount of the income including the stop loss is 3,000.  When setting up the example, I put no interest rate on the debt so that when debt is added, the total income to the partners should not change.

![](https://edbodmer.com/wp-content/uploads/2020/06/Minimum-Gain-No-Debt.png)

Minimum Gain Charge-Back
------------------------

The minimum gain charge-back occurs when the minimum gain change becomes negative.  To begin the discussion, I begin with continuation of the example that I began above;

\[Now the example moves to the minimum gain charge-back of the example.\]  Assume the partnership disposes of Building the next year for an amount equal to the $800 non-recourse debt. \[Recall that the net tax basis of the project was $700.\]  In this case entire minimum gain would be triggered with a minimum gain charge-back.  With paying back the debt, there is no debt left and the decline in debt is $800.  With the sale of the asset there is no longer any non-recourse debt to support the minimum gain.  In this case the equity capital for A and B would each be required to report $50 of taxable income. \[The minimum gain of 100 or 50 for each partner would be eliminated as the debt would go down and the asset balance would also go down.  This would be a negative change in the minimum gain\].

This 

The partnership has sufficient income to allocate because it has $100 of section 704(b) book income from the sale of Building. This is referred to as partnership minimum gain charge-back.

Summary of Nonrecourse Project Debt
-----------------------------------

Benefits of Non-recoruse Debt

*   Normal — reduces equity contributions and increases the equity IRR
*   Creates a higher outside basis which limits the potential suspended losses and the excess dividends that occur from using the DRO to limit for stop losses and re-allocated income
*   The interest expense as usual creates more of a tax shield

Problems

![](https://edbodmer.com/wp-content/uploads/2020/06/Minimum-Gain-Chargeback-Income.png)

Substantial economic effect. The question is whether a tax equity investor is a partner or is a “bare purchaser of tax benefits”

Winston and Strawn: Proceeds in liquidation must be distributed according to the positive capital account balances of the partners; and partners with deficit balances in their capital accounts upon liquidation are unconditionally required to restore such deficit balance to the partnership.

A contributes Building with $100 gross FMV, subject to $30 of debt. In year 1 the partnership allocates $10 of section 704(b) book income to A and distributes $4 of cash to A. A’s ending capital account is $76, which is the asset basis of 100 less the debt (note that for the more important outside basis, the debt is not reduced).

![](https://edbodmer.com/wp-content/uploads/2019/09/Gain-Allocations.jpg)

IRS Safe Harbor Requirements

Purchase rights must be at FMV when exercised and there is no purchase right during the first 5 years. Sale rights – neither the SPV nor the tax investor nor the developer/sponsor can have a contract to buy or sell their portions in the future.

Throughout the existence of the partnership SPV, the developer must have at least 1% interest in each material item of partnership income, gain, loss, deduction and credit.

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Minimum-Gain-Computation.png)

Definition of Minimum Gain

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Minimum-Gain-Chargeback.png)

Minimum Gain Charge back

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-2.png)

Stop Loss Calculations

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-3.png)

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Inside.png)

![](https://edbodmer.com/wp-content/uploads/2020/06/Minimum-Gain-No-Debt.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9151&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7912&rand=0.9583535928390138)