# Project Finance Cash Flow Waterfall - Priority, Structure & Modeling

**Source:** https://pivotal180.com/project-finance-cash-flow-waterfall

---

[Skip to content](https://pivotal180.com/project-finance-cash-flow-waterfall/#fl-main-content)

Project Finance Cashflow Waterfall
==================================

By Haydn Palliser | April 20, 2021

Having advised on and taught project finance around the world I have seen numerous variations on the **cashflow waterfall** and I have fielded many questions related to it.

Although not a complicated topic, there are some important variances in the order of the waterfall across industries and regions. As a common example, most Special Purpose Vehicles (SPVs) in the US, Canada, and the Netherlands are not taxable entities. The SPV does not pay income tax. Taxes do not fit in the cashflow waterfall!

Just in case your job is to worry about this apparent flagrant disregard for tax, don’t. The income from the SPV flows up to the corporations who own the project, and the corporations pay the taxes instead. Someone is still paying the tax. Well, at least they should.

Ok, enough with the preamble, let’s get to it. Why does the cashflow waterfall matter so much?

**Cashflow Matters In Project Finance**
---------------------------------------

Project finance transactions are cashflow based. Our basis of evaluation is cash-flow rather than the value of collateral.

What does this mean? Most conventional loans are collateral based, such as a home loan. The home loan is predicated on an appraisal that puts a value on the actual asset (the home). Lenders will advance funds as a percentage against the asset value based upon loan-to-value ratio. Perhaps you can borrow 80% of the appraised value of a home.

If you fail to repay the loan because you don’t have enough cashflow, your lender can repossess the home and sell it, using the proceeds to repay themselves. And by only extending loans for 80% of the value of a house, there’s a reasonable chance that they’re going to recover all of their money. The house has a solid residual value.

In project finance, it doesn’t work that way. If you were to foreclose on a wind farm, take it down and sell all of the pieces for spare parts or resemble it somewhere else, you would never ever recover the value of that wind farm. The only way that your investment is money good, both for the debt and the equity holders, is if the project operates in place and in service. The valuation of that project is based on its ability to generate cash. Hopefully you can see why we care about cash!

**Cashflow Waterfall Versus A Cashflow Statement**
--------------------------------------------------

As cash is so important in project finance, the financial statement of most interest to the lenders and investors is the cashflow waterfall, sometimes called a ‘cash cascade’. This is similar to the cashflow statement, but the cashflow waterfall shows the priority of each cash inflow and outflow from the project. And this is an important distinction!

**Cashflow Waterfall Structure**
--------------------------------

The cashflow waterfall is negotiated between the borrower (the SPV) and the lender and is stated in the loan agreement. Below is a hypothetical cashflow waterfall which you might see in the market. They vary, but here is one!

![Cash waterfall](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20283'%3E%3C/svg%3E)

### **The Lenders Appoint An Administrative Agent To Manage The Cashflow Waterfall**

For those of you who have completed a Pivotal180 [_**project finance or financial modeling course**_,](https://pivotal180.com/?page_id=774)
 you may recognize that project finance deals are often contracted and managed so tightly that the lenders don’t allow the borrowing SPV to even manage its own cash. That job is outsourced to an Administrative Agent who may work for the lead lender, or it may just be a third party who’s been contracted as a service provider.

### **The Administrative Agent Manages Each Cash Account On Behalf Of The Lenders** 

In our example above, the administrative agent makes sure that all of the project revenues are deposited into a bank account which we will call the proceeds account. And from there the administrative agent will authorize the movement of cash to satisfy different obligations in the specific order of the waterfall. And you can think of the flow of money like a cascade where cash is used to satisfy one obligation. If there’s any money left over, it will cascade downward to the next obligation and so on.

Out of that proceeds account, the administrative agent will allow the project company to pay for operating costs and any applicable taxes, but only if the costs are in the budget. Anything outside of budget requires special approval by the lenders.

After the operating expenses are paid, if there’s any money left over, the administrative agent will authorize payment of any fees that are due to the lenders like fees for lawyers or consultants or other services provided.

And if there’s money left over, the agent will then pay interest on the loan and if there’s money left over, the agent will pay principal due on the loan.

### **Seasonality Account In Project Finance**

And if there’s still money left over, the project company will have to deposit it into a seasonality account until that account reaches a certain prescribed level. What’s a seasonality account? Well imagine a hydroelectric power project where there’s a rainy season and a dry season. The lenders will require that the project accumulate cash from the rainy season into the seasonality account so it’s available if things get really bad in the dry season.

Once the seasonality account reaches a required level, money flows into a [_**Debt Service Reserve Account (DSRA)**_.](https://pivotal180.com/?p=1358)
 This is typically about six-months of principal and interest which needs to be held in cash by the project company so that they can continue to pay the lender even if the plant goes down for say an extended period of time.

Once the debt service reserve account is full, money might flow down into a major maintenance reserve account because the project needs to set aside money every year to pay for major maintenance events which occur say every 5, 10, or 15 years.

### **Sponsors (The Equity Owners) Only Have Access To The Cash Once It Is In The Distribution Account**

Equity conceived the project, and they may even operate it, but they don’t control their own cash. They have no access to the cash until that cash reaches the distribution account at the bottom of the waterfall.

### **Lenders Have Easy Access To The Cash Accounts In The Case Of A Default**

All of the bank accounts in the cashflow waterfall are pledged to the lenders as part of the collateral package. It’s relatively straightforward for lenders to get access to these accounts if the project forecloses.

**Waterfall Structure In A Project Finance Model**
--------------------------------------------------

The financial model must match the description of the cashflow waterfall in the loan agreement (and vice versa). We have shown an example below from our **_[project finance and infrastructure modeling course.](https://pivotal180.com/?course_type=renewable-energy-project-finance-modeling)
_**

![Cash waterfall](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20800%20461'%3E%3C/svg%3E)

### **The Cashflow Waterfall Is Modeled From The Perspective Of The Borrower**

The cashflow waterfall is shown from the perspective of the borrower (the SPV). Cashflows into the SPV are positive (such as revenue or funding). Cashflows out of the SPV are shown as negative values (e.g. operating costs, taxes, loan repayments, distributions).

**Subtotals Help You Understand Each Element Of The Cashflow Waterfall**
------------------------------------------------------------------------

### Cash Available for Debt Service (CADS) or Cashflow Available for Debt Service (CFADS)

Cash available for debt service (CADS) is the sum of our project cashflows from operating the project. The cash will ultimately flow to both the lender and the sponsors. However, as lenders will be paid first in the waterfall we state that this cash is ‘available for debt service’. Only cash that reaches cash available for equity is available for the sponsors.

### Cash available for the Debt Service Reserve Account (DSRA)

This is the cash available after paying the senior lenders fees, interest, and scheduled principal amortization. Check out our introductory video on **[DSRA accounts](https://pivotal180.com/?p=1358)
** here if you want to know more.

### Cash available for Equity

This is the cash that sits in the distribution account and can be distributed so long as the project is not breaching any covenants set by the lender.

Hopefully you can see how the waterfall shows who gets paid in which order.

**Additional Notes And Questions Re The Cashflow Waterfall In Project Finance Transactions**
--------------------------------------------------------------------------------------------

### **Management Fees To Sponsor**

I am often asked if the sponsor (equity owner) can include some of their own costs in the cashflow waterfall.

Let’s say you, an employee of the sponsor, are responsible for preparing and reviewing financial statements for the SPV. You are not paid by the SPV, but rather by the sponsor. Your employer also pays electricity bills related to your work and for your equipment such as your computer etc.

In this case, a portion of your costs should be considered direct project costs. If you were not doing this work then the SPV would need to pay someone else for this service. These direct costs are often called ‘management fees’.

Lenders will ensure that management fees are really true costs and are not some form of additional distribution to the sponsor.

### **A Note On The Location Of The Reserve Accounts In A Cashflow Waterfall**

You may find is odd that we are setting aside money for reserve accounts only after debt is paid, and if there is enough money in the DSRA. Surely maintenance is critical to the project’s ability to operate. Shouldn’t we set aside that money before paying lenders?

There is an advantage to having the Maintenance Reserve Account funding below debt service. If debt is paid before setting aside cash for maintenance, there’s more cash available for debt service. With more cash available to service our debt, our debt size will be higher, increasing our equity returns!

All parties need to be focused on downside risk to ensure that there is enough money to pay for maintenance costs. The same applies to other reserve accounts. Of course, cashflow waterfall structures vary, and you may just as likely see some reserve accounts above CADS / CFADS.

### **SPVs Will Maintain A Minimum Cash Balance**

Investors will also retain a minimum amount of cash in the business to pay bills. It’s called a ‘cash buffer’ or a ‘minimum cash balance’. No company wants to distribute every last cent. You need some spare cash set aside to pay for upcoming bills. You can see this in our example above (the project builds up $0.1m in cash before distributions are made)

### **Are Federal Taxes Before CADS In The Cashflow Waterfall?**

The below example (taken from the earlier example) shows taxes being paid above CADS in the waterfall. This is not always the case.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20707%2033'%3E%3C/svg%3E)

As mentioned at the beginning of this blog, in many countries, such as the US, Canada, and the Netherlands, SPVs are _not taxable entities_. What I mean by that is that tax is paid by the corporations that own by the SPV, not the SPV. In those countries we don’t see taxes paid in the cashflow waterfall.

**Want To Learn More About Project Finance And Financial Modeling?**
--------------------------------------------------------------------

The cashflow waterfall is a must-know for all project finance participants. Our courses go into further detail than what we cover here. Our financial modeling courses that teach this in more detail are:

*   [Financial Modeling and Support](https://pivotal180.com/advisory/) 
*   [Project finance financial modeling](https://pivotal180.com/?course_type=project-finance-modeling)
    
*   [Renewable energy project finance modeling](https://pivotal180.com/?course_type=renewable-energy-project-finance-modeling)
    
*   [Tax equity modeling](https://pivotal180.com/?course_type=tax-equity-course-content)
    
*   [Introduction to Battery Storage](https://pivotal180.com/?course_type=battery-storage-financial-modeling) 

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fproject-finance-cash-flow-waterfall%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fproject-finance-cash-flow-waterfall%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fproject-finance-cash-flow-waterfall%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#0f306d606b7632677b7b7f7c2a3c4e2a3d492a3d497f6679607b6e633e373f216c60622a3d497f7d60656a6c7b226966616e616c6a226c6e7c67226963607822786e7b6a7d696e63632a3d49)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/project-finance-cash-flow-waterfall/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA