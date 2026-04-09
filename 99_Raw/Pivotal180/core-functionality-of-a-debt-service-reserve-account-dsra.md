# Debt Service Reserve Account (DSRA)

**Source:** https://pivotal180.com/core-functionality-of-a-debt-service-reserve-account-dsra

---

[Skip to content](https://pivotal180.com/core-functionality-of-a-debt-service-reserve-account-dsra/#fl-main-content)

Core Functionality of a Debt Service Reserve Account (DSRA)
===========================================================

By Haydn Palliser | November 3, 2021

The **Debt Service Reserve Account** (DSRA) is an important element in most project finance transactions. Let’s explore the core functionality of a DSRA and why it is needed in project finance transactions.

Before we dive into the need for a Debt Service Reserve Account (DSRA), it is important to consider the three core concepts of project finance that we cover in our courses.

1.  Project finance is all about long term promises of cash flow. The project is worth something as long as it is operating and generating a cash flow.
2.  Risk sharing is allocated in contracts to capable parties best able to deal with that risk.
3.  The debt is **non-recourse** to the project sponsors. If a project does not go to plan and there is not enough money to repay the lenders, the lenders can only seek repayment from the project company. The lenders cannot go back to the ultimate owners of the project (the ‘Sponsors’) to repay the debt. The debt is non-recourse to the Sponsors.

What does this all mean? The project company must stand on it’s own two feet without the support of the owners of the project company (the “Sponsors”). The repayment of the loan is not guaranteed by the Sponsors. The lenders therefore require protection for themselves for situations when the project has insufficient cashflow to repay the debt.

One of the most common ways the lenders protect themselves is to have the borrower fund a special account with spare cash. This spare cash can be used to cover short-term shortfalls in debt service. This account is called a **Debt Service Reserve Accounts (DSRA).**

**So, what is a DSRA?**

It is a cash reserve account that retains money for when cash available for debt service (CADS) is too low to service debt. This account is cash security for the lenders.

Project finance debt is often repaid on a quarterly or semi-annual periodicity. Lenders often require the DSRA to be funded with enough cash to cover the next 2 periods of debt service. With quarterly debt repayments the DSRA must be funded with an amount of cash equal to the next 6 months of debt service. This extends to 12 months of debt service if the repayments are semi-annual. This amount of cash required to be in the account is called the **target balance.**

If the borrower cannot pay some of the debt service due cash flow being lower than expected, the DSRA cash can be used to pay the lender their principal and interest (debt service) payments. The DSRA is a useful tool to protect the lenders and the borrower from short-term issues that may arise.

**The DSRA is a safety net for the borrower and lender. It provides breathing room such that the**  **borrower** **has time to** **resolve short-term issues. The lender can get paid during the underperforming** **periods** **and the borrower** **can avoid default.**

**DSRA target balance**

Let’s start with a simple project (shown below) when CADS (cash available for debt service) and scheduled debt service, over a 5-quarter period. Assume that the loan has been sized and the debt repayments are now fixed. The CADS shown represent the _actual CADS that occurred_ in each period, rather than a forecast of CADS at t = 0.

![DSRA modeling ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%20116'%3E%3C/svg%3E)

The DSRA target balance is now added below, equal to the _next two periods of debt service_.

![DSRA modeling ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201200%2040'%3E%3C/svg%3E)

The blue cell is the initial required balance in the DSRA. This is equal to the sum of both quarter 1 and quarter 2’s forecast debt service of $18. The target balance is recalculated at the end of every quarter, based on the next two quarter’s forecast debt service. The target balance remains constant until the end of quarter 3.

Let’s assume that debt service ends in quarter 5. The target balance at the end of quarter 4 is equal to the sum of the debt service in quarter 5 and quarter 6. There is no debt service in quarter 6, so the target balance is only $9 (one period of debt service).

In quarter 5 the target balance is zero, as there are no further debt repayment periods.

**DSRA modeling layout and funding of the DSRA during construction**

The layout of a common DSRA account is shown below. We will explain each line as we get to it.

![DSRA modeling target balance ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201211%20436'%3E%3C/svg%3E)

The first line in the account is the initial funding of the account (‘DSRA cons funding, BoP). The DSRA is most commonly funded prior to the end of the construction period. We are showing the DSRA funded with $16 at the beginning of quarter 1 (indicated by BoP in the label). We are showing it this way simply to make the example easier to read. A project finance model would show initial funding occurring at the end of construction.

What you may notice is that the amount funded of $16 (in the blue cell) is less than the target balance of $18. Most commonly, the DSRA must be fully funded during construction, but in certain circumstances the DSRA is funded either partly or entirely during the first few periods of operations. In our case, the construction period funding of $16 is $2 short of the $18 target required. The DSRA must be funded in the first few periods of operations from cashflow.

**DSRA in the waterfall**

The DSRA is normally located below scheduled debt service in the cashflow waterfall, but above equity distributions. Lenders want their scheduled payments paid first. The below shows the basic layout based on the cashflows and debt service above. The decrease / (increase) in the DSRA balance are covered in the following sections.

![DSRA and waterfall](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201194%20203'%3E%3C/svg%3E)

**DSRA funding during operations**

We have extended the DSRA below to include funding to the target balance from cashflow in the first few periods of operations.

![DSRA operations](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201211%20436'%3E%3C/svg%3E)

Recall we are $2 short of the target balance in quarter 1. We have a required balance of $18, but only have $16 in the account at the beginning of quarter 1. This shortfall must be funded from cashflow. In quarter 1, CADS is $10 and existing debt service is $9. After paying debt service there is only $1 of spare cashflow. We use this $1 to bring the balance of the DSRA at the end of the quarter up to $17. We did not have enough spare cash to fully fund the DSRA up to $18.

In quarter 2, the DSRA target balance is $18. The opening balance is $17, so we are $1 short of the target balance. The project generates $16 of CADS. With $9 of debt service, the remaining cashflow available is $7 ($16-$9). We have enough cash to fund the DSRA with the extra $1 required. $1 of the $7 of spare cash is used to fund the DSRA. The remaining $6 can flow to equity.

**DSRA releases to pay debt service**

This is the point of the DSRA!

![DSRA releases for debt service ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201211%20440'%3E%3C/svg%3E)

Quarter 3 has $8 of CADS, which is not enough to cover the $9 of debt service! We have an issue! The DSRA has $18 of cash available, which is more than enough to cover the $1 shortfall. $1 is released from the DSRA to repay the lenders. The closing balance is $17 on the DSRA.

Without the DSRA, the borrower would have not been able to pay the lenders and would have been in default. The DSRA helped the borrowed avoid default and ensured the lenders could be paid during this one underperforming quarter.

**DSRA due to overfunding**

Cash can be released from the DSRA if the balance exceeds the target balance.

In quarter 4, the target balance has reduced to $9. The initial balance of the DSRA is $17, so the DSRA is overfunded by $17-$9 = $8. This $8 of cash is released back into the waterfall and is available for equity.

**![DSRA overfunding ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201206%20438'%3E%3C/svg%3E)**

**DSRA final releases**

Quarter 5 has a few things going on!

![DSRA and final releases ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201214%20441'%3E%3C/svg%3E)

The target balance in quarter 5 is $0. We can release all the remaining cash in the DSRA. But we cannot release it all to equity. We again have had a worse year than expected, with CADS of $8, being $1 short of the required $9 of debt service. This period has $8 being released to equity and $1 to the lenders to repay the final balance on the loan.

**Cashflow waterfall with DSRA**

The cash waterfall is shown below matching the calculations above. We are not showing the initial funding below as it will occur before operations starts. Just notice that the sign of the cashflows from the perspective of the waterfall are the _opposite_ of the account. Additions to the DSRA account are a reduction from the waterfall as money is being taken from the waterfall to put into the account. Releases from the DSRA are additions back into the waterfall to pay debt service or to flow to equity.

![DSRA and cashflow waterfall ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201213%20283'%3E%3C/svg%3E)

**Lock-up when the DSRA is not fully funded**

The DSRA helps the borrower avoid default. The cash in the DSRA is used to pay debt service if CADS is too low to service debt.

When the DSRA is used to pay debt service due to a shortfall in cash, the project goes into lock-up. Lock-up means that Equity cannot distribute cash from the project. The usual requirement from the lenders is that the project will be in lock-up whenever the DSRA is not fully funded (i.e., meeting the target balance).

The DSRA cash account is managed by the lenders. It is therefore easy for lenders to use the cash in the DSRA when required.

DSRAs simply provide breathing room. There are bound to be surprises over the life of the project, and allowing lenders to draw the DSRA, by going into lock-up, is certainly better than defaulting.

**Final thoughts**

This is just a high-level of the moving parts within a DSRA account. The calculations can be surprisingly difficult.

If you would like to learn more about the DSRA please check out Pivotal180’s free video  [**DSRA requirements**](https://pivotal180.com/?p=1358)
  or If you would like to learn more about financial modeling including learning how to model a DSRA check out [**Pivotal180’s  Financial Modeling Courses.**](https://pivotal180.com/?course_type=renewable-energy-project-finance-modeling)

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fcore-functionality-of-a-debt-service-reserve-account-dsra%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fcore-functionality-of-a-debt-service-reserve-account-dsra%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fcore-functionality-of-a-debt-service-reserve-account-dsra%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#a29dc0cdc6db9fcad6d6d2d18791e38790e48790e4d2cbd4cdd6c3ce939a928cc1cdcf8790e4c1cdd0c78fc4d7ccc1d6cbcdccc3cecbd6db8fcdc48fc38fc6c7c0d68fd1c7d0d4cbc1c78fd0c7d1c7d0d4c78fc3c1c1cdd7ccd68fc6d1d0c38790e4)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/core-functionality-of-a-debt-service-reserve-account-dsra/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA