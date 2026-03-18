# Unreasonable Exams

**Source:** https://edbodmer.com/unreasonable-exams

---

This page presents some unreasonable exams and discusses different strategies if you get a ridiculos and impossible case. Hopefully it will make you not worry too much if you receive an impossible test. I believe the fundamental problem is that exams are not written by somebody senior at the company who is thinking carefully about issues that are interesting and strategic so they can hear about your deep thinking. The exams are more probably written by some young and probaly arrogant modeller who thinks he/she is really good and wants to show off by showing what he/she can do when he/or she has confronted a difficult modelling issue. These people can be aggrogant and do not think very carefully about the exam. I doubt very much that they have put on a timer and tried to complete the test by themselves — I know this because there are so many mistakes in the tests and it is the exception rather than the rule for the tests not to have errors (please do not delude yourself into thinking this is some kind of advanced thinking and that the mistakes are made on purpose). So on this page I present some unreasonable exams that are a little interesting. I have tried to think about a good strategy in completing an exam that can take a full day but has a time limit of three hours, and I am interested in your comments as to what you would do. By looking at the different exams, we are able to rate the quality of the exams and give the exam writters a very bad score if they ask for absurd deadlines and tasks.

In responding to an unreasonable exam, one idea is to think about the ultimate objective of the interview. You want to show you are profieicent in structuring a model with good formats, model structure and simple equations. A second objective is to show that you can think about debt structuring and valuation concepts. So if you recieve an impossible exam, one idea about these exams is to at least lay out the model to show that you know what you are doing (even if you do not complete every line). A second idea is to show how smart you are by pointing out errors in the exam questions. A third idea is to at least make the models look good and for this I show the generic macros file.

In describing the unreasonable exams, I will again refer to the generic macros program so that it can be your partner for modelling. If you are allowed to use your own computer, you should be able to use this model. I strongly suggest that you download the model and enable the macros (you may have to go to the explorer and allow turn off the stupid pink ribbon that comes up these days). It should only take minutes to be able to do this quickly. You can press the first button to download the file. Simple instructions as to what to do with the pink ribbon are shown by pressing the second button. You can send me an email to edwardbodmer@gmail.com and I will send a resource library that includes my collection of exams, some of which are completely unreasonable. It is of course free and this is not some kind of sales pitch.

.

**[Generic Macro File for Copying to Right (SHIFT, CNTL, R), Formatting (CNTL, ALT, C) and Other Functions (UDFs)](https://edbodmer.com/wp-content/uploads/2026/03/Generic-Macros.xlsm)
**

.

**[Instructions for Downloading Files with Macros](https://edbodmer.com/downloading-files-with-macros/)
**

.

Example 1: Re-financing Analysis for Intern
-------------------------------------------

The first example is from a bank. In the exam yoou are supposed to evaluate re-financing of a corporate loan where the corporation in question owns a few wind farms. The bank gave the person being interviewed (for an internship) a model and asked for analysis of a re-financing proposal. The bank gave a disgusting model that it most probably received from the client and then asked for an intern to put a re-financing into this horrible model. It would be an absurd task to try and modify the model except with a simple addition of debt and an adjustment to the debt service line (if you can find them). The bank also asked for scenario analysis and other comments. I have attached the model that was given in this process to the button below. In taking a glance at the model you should be able to see the amazing things not to do. These included putting references to other sheets in formulas, an inpossible to use scenario page, …. But the file also includes some interesting history on the production pattern of wind farms (it would be very nice to have a lot more history). The file that was given as part of the exam is attached to the button below.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-23.png)

.

The bank asked the following questions and gave a summary of a proposed re-financing as part of the exam. It is clear to me that the people giving out the exam were very lazy. Somebody had to make an exam and he/she was probably working on the transaction. The person then just sent out the model for the transaction and a summary of the terms and thought about what a young intern in university may come up with. The questions asked in the exam included:

*   Key points of the request from the Client (financing structure, etc)
*   Strengths and weaknesses of the requests / counterproposal / suggestions on certain terms
*   Comments on:
*   Ratios
*   Robustness of the project under a couple of sensitivity scenarios
*   Level of contingencies
*   DSRA level
*   Any other point deemed relevant

.

.

I am curious as to what you would do with this. My suggestion is to just make incremental changes to the horrible model where you remove the existing debt and add the new debt. Then you try to find lines for interest, repayment and debt service and add the new debt to the lines and subtract the existing debt.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-41.png)

.

Example 2: Project and Holding Company Debt for Two Projects with Three Alternative Financing Cases
---------------------------------------------------------------------------------------------------

.

On of the craziest exam I have looked at is a case of two conventional power plants that operate in merchant and PPA markets. When I looked at the test with somebody who had tried I at first throught it was interesting. The case included merchant cash flow, different target DSCRs for merchant and contract cash flows and project debt that was different from holding company debt. In addition, the case included some interesting sculpting where you used a combination of cash flows with DSCRs and an additional payment at the debt tenor. Finally, the case used payment in kind interest with a different interest rate than cash interest which involved some cash flow waterfall issues to see if cash interest could be paid. This case would have been fine if you had a couple of days to work on it. If you only had three hours, the case in my opinion was utterly absurd. On top of this, the exam contained obvious errors in the inputs which compounds the analysis. You can look at this case to think about how you would have addressed the test.

The three screenshots below show the tasks asked for in the exam. I have attached the instructions to the button below that also includes my attempt at completing the disgusting exercise. After showing the screenshots that were given as instructions, I include a button with how I have tried to complete the exam.

.

**[Excel file with Unreasonable Exam Incluing Multiple Plants, Holding and Project Debt and Alternative Debt Structuring](https://edbodmer.com/wp-content/uploads/2024/04/CCGT-Senior-and-Holding-CompanyModeling-Exercise-v4.xlsm)
**

.

Inputs for two power plants were first given. The plants had merchant and contract cash flows and inputs for fuel price and carbon price were given among other inputs.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-15.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-16.png)

.

Three different debt sizing methodologies were given; each with a method for sizing and repayment of project debt and also holding company debt.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-17.png)

.

The final inputs given were for valuation

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-18.png)

.

My solution to this test that includes fixing a number of items in the test. For example, the gas price is expressed in USD/MWH instead of USD/MMBTU, the fixed O&M expense is expressed in USD/kW-month when it is obviously USD/kW-year; the implied market heat rate for the plants is far to high compared to any but very extreme markets; the time period is completely ambigious; the case 2 holding company debt has no repayment and no maturity — it could not be a perputal bond for a project; the definition of summer and witner are not given; the CO2 tons per MWH are not given; the labeling of PIK and cash interest are ambigious … For me, this is all evidence of an extremely arrogant person who made the exam who did not think he/she had to check the details of what he/she wrote. I can imagine the exam writer thinking, “I am so cool, I will make and exam with DSCR’s for contract and merchant; I will make an exam with even more complex calculations for holding company debt; I will make an exam with sizing debt that has a bullet repayment; I will be really cool and make an exam with with PIK debt that has a different interest rate that forces analysis of a cash flow waterfall.” I suppose this is not too surprising as the excel file was written by Taylor Swift.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-19.png)

.

.

Working Throught the Crazy Case (A lot Longer than 3 Hours)
-----------------------------------------------------------

.

The first thing I did was to fix the inputs. In the example below you can see the Fixed O&M and the Capital Expenditures are changed to $-kW-mo. If the Fixed O&M and the Cap Exp were $/kW-year as in the instructions, the cash flow would be negative and the level of O&M for gas unit would be more than for a nuclear plant. I completely understand if you are saying, how could I know this.

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-20.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-21.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-22.png)

.

![](https://edbodmer.com/wp-content/uploads/2024/04/image-24.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=17305&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9404&rand=0.27163577624547774)