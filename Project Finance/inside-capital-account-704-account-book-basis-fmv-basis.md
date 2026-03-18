# Inside Capital Account (704(b))

**Source:** https://edbodmer.com/inside-capital-account-704-account-book-basis-fmv-basis

---

This page addresses calculation of the inside capital account and its implications in the modelling of tax equity investments for renewable energy.  The inside capital account (also called the 704(b) capital account or the book basis or the FMV basis) is also associated with the deficit reduction obligation (the DRO) , stop losses and income re-allocations.  The 704(b) inside capital comes from partnership tax law that is central to renewable tax equity transactions in the U.S.  The inside capital separates the partnership equity balance into amounts for the tax investor and the sponsor; it is pre-tax  and is should be computed before the outside capital which is discussed on a separate page.  The big deal about dividing up the equity balance account among investors is to test whether the balance of the account falls to below zero for the partner.  You can think of the inside capital account as the equity capital each of the two investors and you can compute the overall equity account for the partnerships. When the investment balance falls to zero without any mitigation (from the DRO), the taxable income increases and the after tax return goes down. Everything is in this page and the page about the inside basis and the minimum gain is about preventing the inside basis from being negative. The reason for limiting the inside capital is the notion of “Substantial Economic Effect.”  If the inside capital falls below zero, the tax equity investor is not considered a real partner but is a “bare purchaser of tax benefits”

[Download some Notes on What is At Risk Investment and What is Passive Investment](https://edbodmer.com/wp-content/uploads/2020/06/At-Risk-and-Passive-Income-rules-1.pdf)
[Download](https://edbodmer.com/wp-content/uploads/2020/06/At-Risk-and-Passive-Income-rules-1.pdf)

Computing the inside basis in a model is important because of the way it affects potential income re-allocation that can increase income to the tax investor and reduce income to the developer. When income is increased to the tax investor, this is bad from the perspective of taxes and thus lowers the tax investor cash flow and IRR.  The tax investor cares about this a whole lot more than the sponsor/developer.

I again need to make my disclaimer. I am not a tax accountant; I am not a tax lawyer; I have never charged high fees for consulting on this stuff, and I have not been a financial advisor.  This means that if I have some details about the specifics of the minimum gain charge back account in the 704(b) capital account and its effect on the use of the DRO which may affect income re-allocation, please do not sue me.

Stylized and Simple Example of Substantial Economic Effect and why the Inside Capital Limit Can Decrease the Tax Investor IRR
-----------------------------------------------------------------------------------------------------------------------------

In evaluating the tax constraints and whether the tax investor is a bare purchaser of tax benefits, I try to think about why these tax constraints exist. The principal test is whether the equity investment falls below zero.  Think about why the equity balance could go to zero. Perhaps you could pay a lot of dividends.  Perhaps you have a really crappy project. (The excess dividends are generally not the case with tax equity investments as the cash distribution in dividends is not very large.)  But the equity balance can easily become negative from losses in income.  It may seem that this is a pretty good test as if you put some money into an investment and then the losses are so big that your capital goes down to zero, then you have made an investment other than to get tax losses back. But there are a couple of problems with this theory. 

The investment you make is after-tax.  But the capital calculation where you compute the balance of investment — equity contribution versus income and dividends — is pre-tax.  Think about an example if you put in 1,000 of investment and the income is -500 for three years. Then if the tax rate is 21%, you get back 500 x 21% or 315.  This amount you get back from tax deduction is less than the amount of the investment.  I am not defending tax equity investors, but this test is really not very fair because to recover your investment, you need more than the losses.  This also does not consider the cost of money as so many other accounting calculations.  An example of the equity capital calculation with horrible details is illustrated in the screenshot below.  These details will be discussed later, but for now note how the equity capital would be negative.

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-1.png)

If the capital account becomes negative, the general and simple rule is that your income deductions are limited by the amount of the negative income unless the other investor also has negative income and your project just stinks.  Before you start yelling at me, I of course realize that you can use the deficit reduction (DRO) mechanism to offset this income limit. But, putting aside the, this DRO, if the capital is negative, the income is increased for the tax investor.  This increase in income is bad.  The tax investor has less of a tax deduction.  The manner in which the income is limited is called re-allocation of income where the income for the tax investor is increased and the income for the sponsor/developer is reduced.

![](https://edbodmer.com/wp-content/uploads/2019/07/Structure-Tax-Equity-Inputs.jpg)

Basis Reduction and ITC in the Capital Accounts
-----------------------------------------------

Note that the ITC is not an explicit item in the calculation of inside capital. But the 50% of ITC that reduces the depreciation on the asset is an adjustment to the capital account. The reason for this is that the asset will never be fully depreciated and there is a loss in value because of this limit on the depreciation (of course this is much more than offset by the ITC itself). If you did not have the basis deduction the asset would never be depreciated.

Safe Harbor Provisions/ITC Recapture and Some Terms
---------------------------------------------------

The IRS issued a letter ruling that allowed assurance of “Substantial Economic Effect” and that the tax equity partner is not a “bare purchaser of tax benefits.”   This letter has been named the safe harbor that can assure that the partnership will not result the IRS considering the tax investor as a bare purchaser of tax benefits.

The IRS issued guidelines for partnership flip transactions in 2007. The guidelines provide a “safe harbor” for transactions that conform to them. Most do. The IRS said in 2015 that the guidelines were written with wind projects in mind and are not a safe harbor for solar transactions.

![](https://edbodmer.com/wp-content/uploads/2020/05/Safe-Harbour-1.png)

Some of things the partnership should do according to this IRS letter includes:

1.  **Minimum 1% interest for each Partner**
    1.  The sponsor must always have at least 1% interest of the partnership income; the partnership gain, and; the partnership loss.
2.  **Minimum of 5% economic interest in cash flow**
    1.  Each investor must have a minimum interest in each partnership gain (gain seems to be cash flow or dividends) for each year equal to 5% of its largest gain (cash flow) for any year (e.g. 99% x 5% = 4.95%).
3.  **Minimum Investment for Each Partner**
    1.  Throughout the duration of the project, the investor must have a minimum investment equal to 20% of paid in capital
    2.  The investment can be reduced by dividends
    3.  Investor must not be explicitly protected against lost
4.  **Tax Investor Purchase Rights**
    1.  The right to purchase must be at fair market value or be reasonably determined up-front
    2.  There is no purchase right during the first 5 years

Stylized and Simple Example of Why the Both the Inside Capital and Outside Capital is Computed
----------------------------------------------------------------------------------------------

The deficit restoration obligation can be used to limit the negative cash flow implications of the inside basis. It increases the capital account of the tax investor so that the income re-allocation will be be less or not even occur.  From this perspective the DRO increases the tax investor’s IRR. Indeed, what I suggest if you see a fancy model is with a DRO and calculation of the inside 704(b) capital account, is to change the parameters of the DRO and see what happens to all of the IRR’s.

*   **Capital and Basis**
    *   704(b) = inside capital = book capital basis = capital accounts
    *   Outside basis = tax basis
*   **Purposes of Accounts for IRS**
    *   Evaluate substantial economic effect and bare purchasing of tax benefits
        *   Capital account, 704(b) –> Fair market value
        *   Tax basis, outside basis –> Cost basis
        *   Capital account cannot be negative without DRO
        *   Outside basis cannot be negative
*   **Accounts and Debt at Project Level**
    *   With no debt and not negative capital –> Inside capital = outside basis
    *   Levered projects:  Inside capital + debt = outside basis (without minimum gain)
*   **What happens when inside capital or outside basis goes negative**
    *   Computed inside book equity can be negative if the DRO is applied or if there is debt
    *   The outside basis (tax basis) cannot be negative because of excess dividend calculations and/or suspended losses

*   **Loss Re-allocation**
    *   Also called stop losses
    *   Can maintain a partnership inside capital 704(b) at zero
    *   Can prevent a DRO from being used if there is not enough capital in the sponsor account
    *   But if the income is allocated to the tax investor, the tax exposure for the tax investor increases.
*   **Deficit Restoration Obligation**
    *   Allows the tax investor to have a negative capital account and not have to increase taxable income (which is very bad for the tax investor).  You do not want to re-allocate income to the sponsor
    *   With the DRO, the tax investor “borrows” equity from the sponsor to claim the negative income that would otherwise be re-allocated. Note that there must be equity to borrow.
    *   Could also borrow the tax free cash distributions
*   **DRO Effect in the case of Liquidation**
    *   Not very likely
    *   Requires the partner borrowing or taking the DRO to contribute real cash capital 
    *   This risk of the tax investor actually paying for the DRO is a credit risk for the tax investor and a benefit for the developer/sponsor
*   **Stop Losses and Limitations of Stop Losses**
    *   Loss re-allocations may not always be preventable by the DRO (there may be nothing to borrow).
    *   The stop losses (which should be named stop negative capital) can be increased by dividends.

Definition of the Capital Account or the Inside Basis – Pretend that the ITC is a Mystical Gift
-----------------------------------------------------------------------------------------------

When the tax returns are filed, both the tax basis of assets and the inside basis are submitted to the IRS — I have seen the tax forms (they are simple one page summaries). The inside basis is affected by the deficit restoration obligation, income re-allocations, the minimum gain and other factors.  In trying to make sense of the inside capital account I use a few sources — a detailed description by Winston and Strawn; some articles by Deloitte and Claborne; a detailed write-up by a tax accountant; materials from various conferences and other descriptions.  I also use interpretation of financial models.  To introduce the account, one source states: Section 704(b) income or loss tracks economic income and loss (this means the book income) while assets are held in the partnership. The partnership then allocates these amounts (of income) based on the business arrangement.

Winston and Strawn: A partner’s capital account is the Fair Market Value of partner contributions (net of any related debt assumed by the partnership, implying that the inside account at its core is the equity balance and not the asset balance like the outside basis).  This inside capital account or 704(b) account is increased or decreased by the partner’s share of income or loss (like any equity account).  It is decreased by the FMV of partner distributions (net of any debt assumed by the partner).  For this purpose, income and loss refers to the economic or book definitions under the tax rules of Section 704(b) (which uses tax depreciation and not book depreciation).  Note that 704(b) is the book basis. It may not be the same as income or loss determined for income tax if there are asset write-ups or write-downs that are not included in the tax basis.  The difference in the book and tax basis may be due to things like developer fees, (developer fees are not an actual outflow of cash) but these items are not included in many renewable financial models.

Inside Basis and Income Allocation
----------------------------------

The general idea of income allocation is demonstrated by the case where income is positive for one partner (e.g. the sponsor) and it is negative for another partner (e.g. the investor) and if the capital account is negative for the partner with the negative income. This is demonstration of the partner not having at risk capital

Excess Distributions and the Inside Capital Account (754 Step-up)
-----------------------------------------------------------------

The adjustment for 731 comes from the excess divided paid adjustment in the outside capital. When dividends are greater than capital, this is considered an implicit asset that must be depreciated. The asset does go onto the inside capital account as it is an asset write-up. This asset would not necessarily be allocated 67% to the tax investor.

Effects of excess distributions on inside capital account and on the outside tax basis  
• On the insider capital account – excess distribution gives rise to an intangible asset that increases the capital accounts (ignoring built-in gain / deemed value)

Examples of Inside Basis in Models and Income Re-allocation
-----------------------------------------------------------

The first example below shows an example of the inside basis for a tax investor.  This account includes a step up depreciation and income reallocation in the screenshot below. Note in the examples that the balance can be negative — it is not limited by the suspended loss.

As shown below on this page there is less consistency in model presentation of the inside capital account than the outside capital account across different models. Further, the manner in which adjustments and balances to this account can affect the ultimate IRR to the tax investor is less obvious.  Specifically, the question is how much does the inside basis affect taxable income given a deficit reduction obligation. I believe in part, the analysis is a pain because consultants, lawyers and tax accounts who charge very high fees want to make things confusing for you and then charge you a whole bunch of money.

In this case there is no adjustment for the basis differential. But the basis differential can be included in income or the case can be a wind case without the ITC.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-57.png)

In the next example, again for a wind farm, the inside basis does not go to zero.  There is no DRO and the only significant items other than the income, distributions and contributions are the 754 step-up and the depreciation on the step-up.  The step-up comes from the excess distribution that was calculated from excess dividends on the outside basis. In this case which I think is a wind case, there is negative capital account in 2027. In this case there is a 41,838 allocation to the partner with the negative capital balance. This allocation is larger than the income of the other partner. Note again that there is no basis difference because there is no ITC.

.

![](https://edbodmer.com/wp-content/uploads/2019/07/Structure-Part-6-Inside-Basis.jpg)

In the next case, again for a wind farm with no ITC, there is no income re-allocation as the balance does not fall below zero. There are some REC — renewable energy credit distributions — that have some different treatment from the other cash.

![](https://edbodmer.com/wp-content/uploads/2019/09/Inside-Basis-2.jpg)

##### Case with Minimum Gain

The next example demonstrates how the computation of the inside basis is not consistent for different models. Note in this case that there is charge back income and the DRO affects the balance.  In the outside basis this does not occur. The chargeback income increases the inside basis. Note that in this case there is a sub-total and the deficit restoration allocation is shown in the account. Note that some of the negative balance is accounted for with the deficit restoration and some is re-allocated.

.

![](https://edbodmer.com/wp-content/uploads/2019/09/Inside-Basis-1.jpg)

[Download Some Notes on Tax Equity from Tax AnnountantEquity-Notes](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Notes.pdf)
[Download](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-Notes.pdf)

[Download a Paper on the Summary of Tax Equity Accounts](https://edbodmer.com/wp-content/uploads/2020/06/1_Summary-of-Equity-Accounts.pdf)
[Download](https://edbodmer.com/wp-content/uploads/2020/06/1_Summary-of-Equity-Accounts.pdf)

![](https://edbodmer.com/wp-content/uploads/2020/06/Tax-Equity-1.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-58.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-59.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-60.png)

.

.

Some Notes on At-Risk Tests and Concepts
----------------------------------------

.

![](https://edbodmer.com/wp-content/uploads/2020/06/image-3.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-20.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9126&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7724&rand=0.43670981593653313)