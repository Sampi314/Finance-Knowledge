# Equity Bridge Loans (EBL)

**Source:** https://edbodmer.com/equity-bridge-loans-ebl

---

This page discusses theory and practice associated with an equity bridge loan in project finance. The modelling of a bridge loan is not difficult.  With and equity bridge loan, a lender allows the sponsor of the project to borrow the amount of equity invested in the project. The loan can be paid at commercial operation or even later.  The loan has capitalized interest that accumulates until the loan is paid. A key issue about the EBL is whether the effects of the EBL should be added to the returns.  If many EBL’s are issued, the debt capacity of the parent will be used up and it has a real cost. If the EBL matures after the COD, another issue that arises is the potential difficulty in computing the IRR because there is no discount rate that results in a zero NPV.

This page describes the mechanics of equity bridge loans and how they can be incorporated into a financial model.  I also discuss the theory of an equity bridge loan the should come along with a parent guarantee.  The question is whether the benefit in terms of a higher equity IRR for the project should be attributed to the project.  One could argue that the EBL is outside of the project and any increase in IRR that comes from the EBL only arises from a parent guarantee.  Further, at least in theory, this use of a guarantee comes along with a cost.

EBL Mechanics
-------------

Let’s begin with some mechanics.  All you need to know about the mechanics is how to use some switches (flags) and how to model capitalised interest.  You can create a switch both for the repayment where you multiply the opening balance plus the capitalised interest by the switch to compute the repayment.

![](https://edbodmer.com/wp-content/uploads/2019/05/Equity-Bridge-Loan.jpg)

The video below describes modelling of an equity bridge loan in the context of a Brazilian wind farm financed by BNDES.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1872&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13772&rand=0.022718210988731058)