# Sculpted and Non-Sculpted with Fixed Repayment

**Source:** https://edbodmer.com/sculpted-and-non-sculpted-fixed-repayment-issues

---

This page addresses situations were there are multiple debt issues in project finance. This page works through the case where one of the multiple debt issues (defined as Last or the sculpting capture issue) is used for sculpting and repayment of the other issues is given by some kind of fixed, non-sculpted formula. In this case with fixed, pre-defined debt service, the basic formula can be adjusted and the process if straightforward. You can start with the DSCR formula and derived the debt service for the last formula. Note that if you are sculpting two debt facilities at the same time and these facilities have different interest rates and different tenures, then the process is difficult because for the NPV formula you need a common interest rate.

Formulas and mechanical techniques for a basic case of sculpting with two debt issues are included in the file that has various different exercises.  You can file this file on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  The file is also available for download by pressing the button below. This file does not address balloon payments which are a little more difficult because the size of the balloon payment affects the DSCR on the non-balloon portion which in turn affects the size of the balloon payment and you have a good old fashioned circular reference.

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

Formulas for Multiple Debt Issues where There is One Sculpted Debt Issue and the Other Issues have Fixed Repayment
------------------------------------------------------------------------------------------------------------------

You can use the following couple of equations to resolve the case where there are multiple debt facilities and repayment for one of the debt issues is determined from sculpting.  For the equations, the term Other DS is the debt issue on the non-sculpted issue (which could be balloon portion of the sculpted issue).  The term Sculpted Issue DS represents the debt service for the debt issue where repayments are determined from sculpting.

**DSCR = CFADS/(Other DS + Sculpted Issue DS)**

**Other DS + Sculpted Issue DS = CFADS/DSCR**

**Sculpted Issue DS = CFADS/DSCR – Other DS**

The modelling of multiple debt issues using the sculpting exercise file that you can download above is illustrated in the screenshot below. In this example there are three debt issues, the last one of which has sculpted repayments driven by sculpting from CFADS. If the debt is separated in this manner, developing sculpting is pretty easy.  The problem comes when the first issue is a function of the sculpting itself.  This is the issue with balloon payment.

![](https://edbodmer.com/wp-content/uploads/2023/06/image-15.png)

![](https://edbodmer.com/wp-content/uploads/2023/06/image-16.png)

![](https://edbodmer.com/wp-content/uploads/2023/06/image-17.png)

![](https://edbodmer.com/wp-content/uploads/2023/06/image-18.png)

![](https://edbodmer.com/wp-content/uploads/2023/06/image-19.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=9604&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11296&rand=0.1003090463205405)