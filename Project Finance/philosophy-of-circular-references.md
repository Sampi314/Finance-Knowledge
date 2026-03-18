# Philosophy of Circular References

**Source:** https://edbodmer.com/philosophy-of-circular-references

---

This page discusses some general subjects of circular references including using alternative methods. The alternative methods include use of the interation button in excel; using algebra; creating a copy and paste macro and finaly applying the user defined function method. Once you move to more advanced issues in project finance including sculpting, re-financing, alternative debt sizing, balloon payments, equity bridge loans, debt service reserve accounts, cash sweeps and other complications, I can assure you that circular references will arise in project finance models. And these circular references will generally make a mess of your analysis and limit your ability to test different structuring strategies in an effieicnt way. If you use either a copy and paste macro or the iteration button in excel, you cannot say that your model is flexible (no goal seek), transparent (how do all the macros work) or stable (the disasters that can happen with iteration buttons).

In working through the circular reference issues in this page I discuss some philosophical issues regarding circular references. I remeber when someone insisted that there is no such thing as circular references in the real world and there should not be circular references in a financial model that is suppoosed to represent the real world. In politics, it is easier to argue that there are real circular references ad recent events have demonstrated the world does not always progress to some kind of more democratic society.  Instead, the world can regress to something a bit like politics in the 1930’s. When arguing with your significant other there are probably a whole lot of circular references that are impossible to break.

The first 90% of making a project finance model is pretty easy.  You develop time lines, detailed sheets that may count every pencil that you buy for the project and every hour of maintenance outage.  But then, at least if you are making your project finance model to evaluate alternative debt structures, you hit a wall.  The wall is created by circular references.  If you use common methods (the iteration button or the copy and paste macro) you have destroyed your model.  My position is that the only way to keep your model flexible (so you can make good scenario analyses and goal seeks) and to keep your model transparent (so users can see what is going on) and to make it accurate (test all the equations that are difficult) is to make a user defined function.

![](https://edbodmer.com/wp-content/uploads/2018/05/images.jpg)

Loan Example – Your Grandmother Wants to Buy a Ferrari with a Loan
------------------------------------------------------------------

To explain circular references in a project finance model, consider a case where the woman below is asking to make a loan from you, the banker, for a really expensive Massaratti.  She wants a loan for a million euro to buy a few cars.  You say ok, but she has to pay you fees of 50%.  The lady says fine, but now she needs a loan of 1.5 million euros.  You say ok, but she needs to pay you fees of 750 thousand and the going around and around starts.  She says fine, but she needs a loan of 1.750 million.  You again say ok but your fee goes up.  This silly example demonstrates the problem of circular references. Note that in this example, the fees are decreasing with each go around. Evenutually, the fees change when you go around — the iteration — will become very small and your Grandmother can get her cars. As you can maybe imagine, excel does not deal with these circular references well because the calculations must go around and around and excel does not know exactly what areas of the sheet are causing the problem.

In the case of project finance the situation is almost the same with interest during construction (IDC) and fees. With higher IDC and fees, the cost of the project increases. With the increase in project cost, the debt if measured on the basis of debt to capital increases. When the debt goes up, the IDC and fees go up and you go around and around again. You can keep changing the debt amount and then re-computing the fees and IDC. Eventually as with the loan example above the difference becomes smaller and smaller and the calculations resolve.

![](https://edbodmer.com/wp-content/uploads/2018/08/Bank-2.jpg)

In project finance, unless you fix just about everything including the amount of debt, the amount of equity, the DSRA and other debt related items, a circular reference will invariably arise.  To really solve the circular references, you need to understand a lot more than a few excel tricks.  In particular, you need to fully understand the sculpting formulas and you need to not force things when mathematical formulas can be used.

Four Solutions to Circular References
-------------------------------------

This and the next few pages demonstrate how to resolve circular references through using user-defined functions rather than non-transparent and circular resolution clumsy copy and past macros, goal seeks or solver methods. For a series of circular reference problems, the benefits and problems of various different circular reference resolution methods are illustrated beginning with the iteration button, moving to the goal seek method and finally to two different circular reference methods that use functions.

*   **ITERATON BUTTON:** The _**first**_ circular reference resolution method that involves pressing the iteration button is demonstrated with files that demonstrate how things can go wrong from the un-stability of your model. The file shows when the iteration button can be reasonable and how you can fix things when things go wrong.

*   **ALGEBRA:** The _**second**_ circular reference resolution attempts to solve circular references using algebra. This circular method can result in long and tedious formulas but can also be elegant. In some situations like for IDC with an annual model or for simple fees, this can be the best approach.

*   **COPY AND PASTE MACRO:** The _**third**_ circular reference resolution method in which you create a copy and paste macro that copies from COMPUTED to FIXED, COMPUTED to FIXED and sets the calculation formula to the fixed item is pretty simple. The important thing is to understand where the circularity comes from and minimise the copy and paste macros.

*   **USER DEFINED FUNCTION:** The **_fourth_** circular reference method applies user defined functions with a structured approach that can solve any circular reference problem. This is the method that is most documented and it involves re-programming equations in excel that result in the dreaded blue arrows.

Say that somebody was really lazy and used the iteration button. Your task is to fix the circular references. Here are some suggestions:

### First, fix easy things with algebra

If the circular reference is coming from a simple fee calculation or from a contingency calculation, just change the calculation to a formula using some simple algebra as shown below.

Total = Total x Contingency + All Else  
Total – Total x Contingency = All Else  
Total x (1- Contingency) = All Else

**Total = All Else / (1 – Contingency)**

If you have an annual model, you can use the following formulas to resolve the IDC problem with average balance.  In the equations below, ob stands for opening balance of the debt.  The last equation is the equation you can use for IDC in an annual model.

*   draws = cost x debt pct / (1-int rate/2 x debt pct – fee pct x debt pct)
*   new debt = total funding – equity
*   new debt = construction + idc – equity
*   idc = ob \* rate + new debt \* rate/2
*   idc = ob \* rate + (construction + idc – equity ) \* rate/2
*   idc – idc \* rate/2 = ob \* rate + (construction + equity ) \* rate/2
*   idc \* (1 – rate/2) = ob \* rate + (construction + equity ) \* rate/2
*   idc  = (ob \* rate + (construction + equity ) \* rate/2)/(1-rate/2)

You can download a file that uses this method to solve the interest during construction problem in an annual model by clicking on the button below.

**[Annual Project Finance Model with Interest Computed on Average Debt Balance and Circularity in IDC from Algebra](https://edbodmer.com/wp-content/uploads/2018/09/IDC-and-Fees-in-Annual-Model-with-Equations.xlsx)
**

### Second, make sure the closing balance is NOT part of the interest expense calculation

Look around for the model for the interest expense or interest income calculations. If the calculation uses the closing balance, change the calculation. Make the interest on the opening balance which implicitly assumes that the repayment etc. occurs at the END of the period. If you are worried about this assumption change the timing of the model. For example, change an annual model to a quarterly model, at least for the debt schedule.

### Third, in PF Model make sure there is a summary sources and uses statement with IDC, Fees and DSRA funding during construction

The IDC, fees and DSRA cannot be fixed with a simple copy and paste macro. To fix the IDC first use the clumsy copy and paste method. This involves the following steps:

First make a copy and paste near the sources and uses statement. Name ranges and copy the COMPUTED TO FIXED with paste special. Do this with recording a macro. In this section I explain how you can resolve a couple of circular references that arise in corporate models. The most classic circular reference comes from interest expense and interest income that is affected by financing over the course of the year.

![](https://edbodmer.com/wp-content/uploads/2018/09/Web_circular.jpg)

Note: please do not make your macro password protected as if it is something fancy. In fact it ruins your model and destroys the ability to efficiently make scenario analysis.

### Fourth, Change the Copy and Past Macros to User Defined Functions

Making a user-defined function is the second-best alternative after the algebraic option. For some resolving some circular reference problems like the classic circular reference from interest expense and interest income, the process is relatively simple. In these cases the blue lines and the circular reference are all a single column and the item in question does not depend on the prior year. For the IDC, fees and DSRA funding, the problem is that IDC defines project cost and you need to work through the entire construction period to find the IDC. This implies that a loop is necessary.

To make the mechanics of user-defined functions easier, a file named “Circular Template” is included here. This file has a lot of the generic programming that you will need to solve the circular reference problem where loops are necessary. So, if you want to build a user-defined function with a loop, first download the file. Next, change the name of Read Array per the instructions and start defining period by period variables as well as accumulated variables. In the example below, the equity is funded before debt during the construction period and a minimum function is necessary to understand when the equity funding will be complete and the debt funding will begin.

![](https://edbodmer.com/wp-content/uploads/2018/05/breaking-wall.jpg)

Sad Situation that People Still Want Copy and Paste Macros
----------------------------------------------------------

It is very sad for me, but a lot of people are not interested in making a UDF to solve the circular reference problem. While I am strongly opposed to making copy and paste macros, I have included a video below where I go through how to solve the problem with this method. If you want to get straight to the point you can go skip to minute number 7 in the video below.

.

In this video if you go to about minute number 9, you can see how the make a copy and paste macro in the context of taxes and sculpting.  I am reluctant to do this. These copy and paste macros are total B.S. and mess-up your model.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=13123&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=13708&rand=0.059629596251008055)