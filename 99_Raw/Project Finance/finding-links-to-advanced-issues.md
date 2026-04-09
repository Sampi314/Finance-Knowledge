# Exercises for Project Finance Modelling Class

**Source:** https://edbodmer.com/finding-links-to-advanced-issues

---

On this website I have included exercises that I use in project finance courses. I think other people may even want to charge money for this sort of thing. The course and the subjects are structured in the same manner as a project finance model is structured. This is to begin with a timeline. Next you can move to the quantity and the capacity that is produced. With the quantity produced you can evaluate the key question of the project IRR and even make a preliminary valuation of the project. The course then moves to financing issues which are central to project finance. The first of these issues is how to finance the construction of a project. The second is debt sculpting and debt sizing. After establishing the model structure which is the important and essential structuring phase of project finance, the course moves to risk analysis given the structure of the the debt. This is accomplished through and exercise with a cash flow waterfall that works through the potential for default and credit protections like a cash sweep, a cash trap and a reserve account.

[Allow download of excel files when the pink ribbon appears](https://edbodmer.com/downloading-files-with-macros/)

One of the main reasons I have made this page is because of a single course I made for a company named Redcliffe that refused to make video recordings of the sessions, made a torture class for class for eight hours and did not have any staff on the call to monitor comments. If you have comments or questions about the sessions below or would like to learn this in an on-line course that is not torture, send me an email at edwardbodmer@gmail.com. Please do not ever sign up for a class at Redcliffe, they are a real ripoff.

Once the fundamental issues associated with designing a model are addressed, more complex subjects of sculpting multiple debt issues and resolving circular references and taxes are discussed in later sections. These sections also include project finance theory and issues of upside from re-financing and from selling a project in total or in part. Subjects included in this page with associated videos include:

*   Building a comprehensive renewable energy project finance model
*   Receive and understand unique tools to make efficient models
*   Include alternative debt sizing and debt sculpting
*   Modelling probabilistic resource scenarios
*   Learning about funding the project with equity and multiple debt tranches
*   Effective presentation of risks and returns

My teaching objectives in the files and videos below include:

*   Understand project finance theory for renewable energy whilst building a model
*   Learn about best practices in model structures and logic
*   Integrate project finance theory into the discussion of alternative modelling features
*   Build up, in manageable stages, an entire financial model for a renewable power project
*   Create flexible revenue, production and cost forecasts
*   Add flexible capital expenditure profiles into the model
*   Include advanced financing structures in the model including debt sculpting
*   Model dividend distributions to equity shareholders and upside from asset sale
*   Learn about bank ratios and debt covenants, and how to include them in the model
*   Include debt service reserve accounts and re-financing options in the model

Please note that it will be torture for you to work through all of the examples and videos below. This is not intended to be fun.

.

Partner Files to So You Do Not Waste Time on Formatting and Using the Paint Brush
---------------------------------------------------------------------------------

I have included two files that are used to make the excel exercises work more smoothly. The first is a file called Read PDF which allows you to grab data from PDF files and then convert the data to excel files. To run this file you copy stuff from the pdf file and then operate the macro with SHIFT, CNTL, A. When you copy data from a PDF to excel, make sure that you copy and paste special as UNICODE text. There are different formats that you can use to resolve the PDF. If you are reading from the Lazard LCOE stuff you can use the first green box. If you are reading from the PVGIS you can use the second green box.

The second file is a file that has a whole lot of macros to prevent you from wasting time on formatting and copying formulas to the right. This file is called GENERIC MACROS. I have revised the generic macro file in the link below so that you are not prevented to open it because of something called the auto open — a macro that operates when you open the file and excel considers dangerous. When working through the exercises, it would help a lot if you have this file open and enable the macros. The big things that this GENERIC MACRO allows are to press SHIFT, CNTL, R to copy to the right and also CNTL, ALT, C to open the window that has a whole lot of formatting options. There are a lot more utility macros in the GENERIC MACROS file. You can go to [https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file/](https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file/)
 and see some of the other stuff including a few user defined functions.

.

**[Read PDF to Excel File that Allows you to Format Data After Copying from PDF File (Press Shift, Cntl, A)](https://edbodmer.com/wp-content/uploads/2019/04/Read-PDF-to-Excel.xlsm)
**

.

**[Generic Macro File for Copying to Right (SHIFT, CNTL, R), Formatting (CNTL, ALT, C) and Other Functions (UDFs)](https://edbodmer.com/wp-content/uploads/2026/03/Generic-Macros.xlsm)
**

.

Some General Discussion on Project Finance Modelling History and Current Problems
---------------------------------------------------------------------------------

*   1980’s Either Pencils and Erasers or Fortran Programs with Phone Hookups
*   1990’s VisiCalc and One Sheet Lotus – Simple Models
*   2000’s Multiple Sheets – Models were a Mess; Range Names; No Structure
*   2010’s Larger Models – Big Working Page; Long Formulas; Becoming Difficult to Understand
*   2020’s Monster Bureaucratic Models – Models with Rules; Creativity Lost; Models for Auditors

### •**Nicholas Taleb:**

•In the not-too distant past, say the pre-computer days, projections remained vague and qualitative, one had to make a mental effort to keep track of them, and it was a strain to push scenarios into the future.  It took pencils, erasers, reams of paper, and huge wastebaskets to engage in the activity.  The activity of projecting, in short, was effortful, undesirable, and marred with self doubt.

•But things changed with the intrusion of the spreadsheet.  When you put an Excel spreadsheet into computer literate hands, you get projections effortlessly extending ad infinitum.  _We have become excessively bureaucratic planners thanks to these potent computer programs given to those who are incapable of handling their knowledge_.

.

### Ancient History – Very Simple Case in Indonesia and Basic Model with No Complex Timing or Debt Repayment (Case on Grasberg Mine in Indonesia)

![](https://edbodmer.com/wp-content/uploads/2023/03/image-1.png)

![](https://edbodmer.com/wp-content/uploads/2023/03/image-2.png)

#### Historic Prices – How Would you Incorporate Price Volatility in the Analysis

Include the historic prices in the InputS page.

![](https://edbodmer.com/wp-content/uploads/2023/03/image-3.png)

![](https://edbodmer.com/wp-content/uploads/2023/03/image-4.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-28.png)

.

### Monster Models and Auditors

I use the model below to illustrate what has become of modelling. Note how many lines there are on the various pages. It may be just me, but I would be intimidated by this model.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-29.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-30.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-31.png)

.

Like Writing a Book or Running a Business – Focus on the Consumer and Not Internal Bureaucratic Rules or Rules for Auditors.

### My Principal: Two Key Things:

F2 to Find Equations without Looking Far

Cntl \] and F5 to Find the source

.

This does not look so bad but it is horrible to audit and modify

.

![](https://edbodmer.com/wp-content/uploads/2023/02/image-2.png)

.

### A Little Theory

.

The class is practical, but I think a little theory is worth reviewing really fast. I have put the theory in the file attached to the button below. WACC – What Absolute Complete Crap. The risk of a project changes over time and the WACC is nothing close to constant.

.

**[Press this Button to Download Draft Version of My Book Titled Re-Thinking Finance with Addresses All Sortes of Finance Issues](https://edbodmer.com/wp-content/uploads/2026/02/Rethinking_Finance_15.02.2025.pdf)
**

.

Model Structure, FAST Modelling Standards and Completed Case – Video with Simple and Complete Case Without Difficult Timing Issues
----------------------------------------------------------------------------------------------------------------------------------

.

There are three buttons below with files attached. The first is an exercise using the pure FAST standards explained below. It is a pretty simple example and you can work trough it if you want, but I do not go through this one in the class. The second button has the file with the FAST modelling standards finished. The third button is the most important and provides a guide for where we are trying to go in the class. This third button with the completed exercise will be used to evaluate a couple of issues including circular references associated with sculpting, net operating loss calculations. The file will also be used to illustrate how to use models for either debt debt structuring or risk analysis.

.

### Fast Religion

There is a lot of good stuff about the FAST modelling standards that have been developed by my friend Kenny Whitlaw. This set of standards is very structured and has been accepted by many. I completely agree with the philosophy of FAST shown below and I sometimes try to apply it to my life.

§Flexible – What does it really mean (Really large models with too many rules are not flexible)

§Accurate – Not Appropriate. Key checks are essential. Be creative with checks.

§Structured – Separation of Cash Flows; Natural Flow of Model for Users.

§Transparent – User Focus with Simple Equations and Seeing how the Model Works

.

When you look at my files you can see that I hope to be obsessed by the transparency part of this religion. But while structuring is important, I try not to become to point of too many rules. For example, re-copying the inputs into separate lines and putting all of the time flags in one page and not using master time lines that can be integrated is irritating.

.

**[Project Finance Modelling Completed Case -- Simple FAST Model of Solar Project with Complete Equations](https://edbodmer.com/wp-content/uploads/2022/11/FAST-Simple-Case.xlsm)
**

.

**[Project Finance Modelling Exercises -- Simple FAST Model of Solar Project with Blanks to Fill In](https://edbodmer.com/wp-content/uploads/2022/11/FAST-Modelling-Exercise-1.xlsm)
**

.

**[Complete Case with Both Structuring to Size Debt and Sensitivity for Credit Analysis with Fixed Debt from Structuring](https://edbodmer.com/wp-content/uploads/2023/01/Completed-Case-with-Flexible-Structuring.xlsm)
**

.

The summary page of the file attached to the third button is shown below. The idea is that you can move from credit analysis to structuring easily by pressing the copy debt macro.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-8.png)

.

What is impressive and not impressive in modelling:

1.  Typing fast in excel and copy to the right with left, right, up, Cntl R that is not impressive
2.  Some kind of certificate on bureaucratic modelling rules is not impressive
3.  Copy and paste macros that destroy models are not impressive
4.  Monster models with fees on standby debt and LC fees on equity commitment is not impressive
5.  Creative presentations of sensitivity for different real users (not auditors) is impressive
6.  Use of mathematics to solve problems (e.g. sculpting, leases, residual) is impressive
7.  Not having one single complex formula in a whole model is impressive
8.  Effectively modelling different financing strategies and development fees is impressive

.

.

Making a Model from a Blank Sheet
---------------------------------

When I made the course for this company named Redcliffe, they received negative feedback from one of the twenty five people on the zoom call that they would have rather began from a blank sheet. Redcliffe send me some really nasty emails about this feedback. So in this section I have included a completely blank exercise with an accompanying video. Note that if you send me an email at edwardbodmer@gmail.com I will send you an outline. Unlike Redcliffe, when I have on-line sessions, I limit the number of people to 5-10.

This course is not designed to start with a completely blank excel file because if I did, I would waste a lot of time typing in titles for various things and I would not have time to properly structure inputs and other items. So, if for some reason you want to build a model from scratch, you can watch the following video. Note if there is a problem with the music in the background, I am sorry and you can resolve this with headphones. A warning, this is boring.

.

.

.

[Model for Solar Case with Debt Sizing from DSCR Associated with Video on Building Basic Project Finance Model](https://edbodmer.com/wp-content/uploads/2023/06/Solar-Project-Finance-Case.xlsx)

.

**[PDF File with Instructions for Model of Solar Case Used for the Video Discussion Below and the File Below](https://edbodmer.com/wp-content/uploads/2022/05/Test-Case-1-Solar.pdf)
**

.

**[Excel File with Exam for Solar Project with that Contains Given Inputs but Not with the Final Answer](https://edbodmer.com/wp-content/uploads/2021/05/Exam-Sheet-for-Solar-Case-Study.xlsm)
**

.

Time Line and Structuring Exercise
----------------------------------

.

The first exercise works through tricky timing issues and shows how you can either create a monthly model for operations with monthly financing or with semi-annual financing. In the semi-annual analysis, the monthly generation can be reconciled using the find\_month function. If you are just starting, some of this will be technical. You may then want to skip to the second video. The screenshot below illustrates tricky formulas for establishing a dates that are used to move monthly into semi-annual data. Point to the pre-cod flag for the prior period and use the EOMONTH function.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-32.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-41.png)

.

**[Completed Equations with Timing and Model Set-up with Monthly Financing and Semi-Annual Project Finance Page](https://edbodmer.com/wp-content/uploads/2023/01/Timing-and-Generation-Completed.xlsm)
**

.

.

**[Exercise with Timing and Model Set-up with Monthly Financing and Semi-Annual Project Finance Page](https://edbodmer.com/wp-content/uploads/2023/01/Timing-and-Generation-Exercise.xlsm)
**

.

The video below shows how to make a monthly/semi-annual page from a monthly page. The hard part is making a time line in the monthly page. This is a real pain point of modelling.

.

.

The link below shows how you can resolve generation in a semi-annual case for the difficult issue of fitting in generation to semi-annual pages. Without a user-defined function.

> [Find Month](https://edbodmer.com/find-month/)

.

Building of CFADS (EBITDA), Generation and Levelised Cost
---------------------------------------------------------

.

Building of EBITDA

In the first exercise I put a few equations for generation and for computing levelised cost of electricity. The idea is to work through a few equations in the model and see how LCOE and financial models should be the same thing. You can think of financial structuring as trying to get a low project IRR with a lot of debt. This is also in the second set of exercises below. The exercises correspond to the completed case with different structuring.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-37.png)

.

**[Completed File with Equations for Levelised Cost Analysis and Generation Analysis for Renewable Project](https://edbodmer.com/wp-content/uploads/2023/01/Generation-and-LCOE-Completed-1.xlsm)
**

.

**[Exercise with Selected Blank Equations for Levelised Cost Analysis and Generation Analysis for Renewable Project](https://edbodmer.com/wp-content/uploads/2023/01/Generation-and-LCOE-Exercise-1.xlsm)
**

.

### Extra Exercise on P90, P99 etc. and Debt Size

.

The extra model/exercise addresses computations for risk analysis. This exercise demonstrates how to compute P values using NORMSINV and use mean squared error to add up standard deviation from different (independent) sources. It also includes a financial model that demonstrates how the risk analysis affects the returns to equity investors through debt sizing. The type of exercise for you to complete is illustrated in the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2022/10/image-8.png)

.

As with the other exercises, the button attached to the first file is the file with equations for you to fill in. The second button is attached to the file with the completed exercise.

.

**[Renewable Exercise Part 2 Blank - Excel File with Blank Equations for Risk Analysis with Debt Sizing Analysis](https://edbodmer.com/wp-content/uploads/2022/11/Part-2-Course-Exercise-File-Blank-Risk-Analysis.xlsm)
**

.

**[Renewable Exercise Part 2 - Excel File with Completed Equations for Risk Analysis with Debt Sizing Analysis](https://edbodmer.com/wp-content/uploads/2022/11/Part-2-Course-Exercise-File-Filled-Risk-Analysis-1.xlsm)
**

.

.

Funding of Construction and Circular References
-----------------------------------------------

.

The exercises below addresses funding of construction with interest during construction, fees and a potential DSRA account. The exercise includes standard copy and paste macros and then illustrates the idea of making a user defined function. If you make a user defined function, you will not have to stop the model; the model will have automatic checks and you can attack the pain points in modelling. But the main subject will be using the copy and paste method. The second button below is attached to a file that has no buttons and automatically makes a goal seek calculation.

.

**[Excel File to Demonstrate Construction Financing and Circular References with Implementation of the UDF Method](https://edbodmer.com/wp-content/uploads/2023/03/UDF-Working-Multiple-Issues13.xlsm)
**

.

**[Exercise with Selected Blank Equations for Construction Financing and Circular References](https://edbodmer.com/wp-content/uploads/2023/01/Construction-Funding-and-Circular-References-Exercise.xlsm)
**

.

**[Illustration of Model that Computes Capacity Charges and Financing without Copy and Paste Method Using UDF](https://edbodmer.com/wp-content/uploads/2023/01/Example-with-No-Buttons.xlsm)
**

.

Cash Flow Waterfall With Sculpted Debt, Dividend Restriction, Cash Sweep and Default
------------------------------------------------------------------------------------

.

In the exercise attached to the button, you work through various issues with structuring credit protections. You first design scheduled debt repayment with sculpting. Then you move to credit analysis with dividend restrictions and a cash sweep. To illustrate the credit analysis a little Monte Carlo simulation is used. Do not be intimidated by the Monte Carlo Simulation or think it is useful in real models. It is a way to demonstrate what happens in alternative possible cash flow paths. The analysis with and without Monte Carlo is illustrated below.

.

No Volatility Case and Cash Sweep

![](https://edbodmer.com/wp-content/uploads/2023/01/image-33.png)

.

Volatility Case with Mean Reversion and Payback

![](https://edbodmer.com/wp-content/uploads/2023/01/image-34.png)

Volatility Case – No Mean Reversion and Default at End

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-35.png)

.

**[Exercise with Selected Blank Equations for Cash Flow Waterfall with Sweep, Default and Dividend Restriction](https://edbodmer.com/wp-content/uploads/2023/01/Cash-Flow-Waterfall-Exercise.xlsx)
**

.

**[Completed File with Equations for Cash Flow Waterfall with Sweep, Default and Dividend Restriction and Monte Carlo](https://edbodmer.com/wp-content/uploads/2023/01/Cash-Flow-Waterfall-Complete.xlsx)
**

.

.

Complexities in Sculpting – Curved DSCR; Multiple Debt Issues; Sculpting without Debt Sizing
--------------------------------------------------------------------------------------------

.

Credit policy on sizing debt for power is applying a grid of DSCRs based on different P-curves. For example, on a solar project, on each quarter we constrain P99 CFADS at a 1.00x and p50 at a 1.35x, and take the minimum resulting constrained debt.

Objective setting of debt structure with multiple sources (loan + bonds) on a pari-passu basis. Start with the following equations

|     |
| --- |
| DSCR =CFADS/(DS1 + DS2) |
| DS1 + DS2 =CFADS /DSCR |
| DS1 =CFADS/DSCR – DS2 |

*   Fixed Debt Amount with Implied DSCR
*   Fixed DSCR with Multiple Issues and Debt Capture Issue
*   Fixed Debt with Multiple Issues using LLCR
*   Curved Sculpting with Fixed Debt Amount
*   Allocation of Changing DSCR to Multiple Issues
*   Curved Sculpting with Multiple Debt Issues

Running sensitivities on a set debt amount (no longer sizing for changes made to CFADS and investors play around with model).

The file attached to the buttons below wil be used to evalulate tricky sculpting isssues. The file has simple data and no taxes, but I think the concepts are tricky.

.

**[A-Z Simple Sculpting Exercises Including Curved Sculpting, Multiple Debt Issues and Changing DSCR](https://edbodmer.com/wp-content/uploads/2023/01/A-Z-Simple-Sculpting-Examples-Exercise.xlsm)
**

.

**[A-Z Simple Sculpting Completed Including Curved Sculpting, Multiple Debt Issues and Changing DSCR](https://edbodmer.com/wp-content/uploads/2023/01/A-Z-Simple-Sculpting-Examples-1.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-10.png)

.

Building of CFADS After EBITDA (Taxes and DSRA Changes)
-------------------------------------------------------

•Ultimate tasks to be mastered include:

*   Building of CFADS
*   EBITDA
*   Income Taxes
*   Working Capital Changes
*   Working Capital Facility Interest Income
*   LC Fees on DSRA
*   Changes in Cash DSRA

*   Use Completed file to work through income tax issues with NOL and limit on carryforward

*   Use MAX for positive/negative test
*   Use MIN to limit the amount of tax carryforward that can be used 
*   Copy and paste on the CFADS to resolve interest problem

*   Use separate exercise for DSRA exercise where
*   DSRA is included in CFADS for sculpting
*   Trick of separately computing debt size from EBITDA without the DSRA

.

**[Exercise File for Learning Project Finance Modelling Concepts with Selected Blank Equations to Fill In](https://edbodmer.com/wp-content/uploads/2022/12/Exercise-for-Class-Blank.xlsm)
**

.

**[Completed Project Modelling Finance File for Learning Concepts with Completed Equations Filled In](https://edbodmer.com/wp-content/uploads/2023/01/Model-for-Class-Completed.xlsm)
**

.

**[CFADS Exercise where the DSRA change is Included in the Computation of CFADS for Sculpting](https://edbodmer.com/wp-content/uploads/2023/01/DSRA-Change.xlsx)
**

.

**[Exercise File with Applied Case for Computing CFADS Circular Reference and Tax with NOL](https://edbodmer.com/wp-content/uploads/2023/01/Exercise-for-Class-Semi-Filled.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-9.png)

.

Exercise for Both Structuring and Credit Analysis
-------------------------------------------------

.

In the exercise attached to the button below, we will work through selected areas in a model where, after you compute the debt structure using different approaches, including P50, P99, P90 and debt to capital. After computing the debt size in different scenarios, you will see how to copy the debt structure into a model and then run sensitivities with the fixed debt. The general idea is that you first copy a column with the INDEX function to a separate line in the InputC page. Copying the data is easy, but if you want to use a user form like the spinner box. The screenshots below first show the macro where you can adjust the formulas after the copy. Then you can adjust the formulas below. I have copied this screenshot so you can see the how to use the double quote and then the RC formulas. When you use the RC\[1\] the formula comes from one to the left.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-40.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-39.png)

The exercise with selected equations is attached to the button below.

.

**[Exercise File with Both Structuring to Size Debt and Sensitivity for Credit Analysis with Fixed Debt from Structuring](javascript:void(0);)
**

.

### Section 6: Tax Equity Transactions

Power sector projects area good example, given complexity added by production curves for sizing methodology and **introduction of tax equity**. The credit policy on sizing debt for power is applying a grid of  
DSCRs based on different P-curves. For example, on a solar project, on each quarter we constrain P99 CFADS at a 1.00x and p50 at a 1.35x, and take the minimum resulting constrained CFADS.

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-3.png)

.

Assumptions for the case are included in the PDF file attached to the button below. This case includes detailed operating assumptions and financing of the construction costs with an equity bridge loan and also back leverage.

.

**[Tax Equity Case Assumptions with Detailed Generation Inputs and Financing Inputs Including Equity Bridge](https://edbodmer.com/wp-content/uploads/2023/01/Tax-Equity-Financing-Case.pdf)
**

.

**[Tax Equity Excel File with Selected Equations to Fill In Related to Tax Equity Operations and Financing](https://edbodmer.com/wp-content/uploads/2023/01/Tax-Equity-Model-Exercise.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-11.png)

.

The summary output is shown on the sceenshots below. The first screenshot demonstrates the operating assumptions while the second screenshot shows the uses and sources of funds based on the assumptions provided

![](https://edbodmer.com/wp-content/uploads/2023/01/image-5.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-4.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/01/image-6.png)

The completed case study is attached to button below.

.

**[Excel File 2 with Tax Equity Including Tax Equity Bridge Loan and Back Leverage in Quarterly Model with Corporate PPA](https://edbodmer.com/wp-content/uploads/2022/08/Tax-Equity-Revised-Model-Partnership-Balance-Sheet.xlsm)
**

.

.

Nuances and Upside in Project Finance
-------------------------------------

The third exercise has more nuanced issues for project finance analysis. The general idea of this exercise is to demonstrate that the IRR in the initial analysis is just a first step. Because the risk of renewable projects declines, it is possible to realize upsides. These upsides include use of development fees, use of re-financing and use of the sale of a plant to investors who are interested in paying for safe investments. This third exercise also includes the true definition of IRR, the theory of development risk and development fee; upside option from re-finance; the upside option from selling a project; computing performance measures and equity bridge loans. As with the first exercise, the first file is completed and the second exercise has equations that you should fill in.

.

![](https://edbodmer.com/wp-content/uploads/2022/10/image-9.png)

.

**[Part 3 - Excel File with Blank Equations for Project Finance Issues including Development Fee, Re-financing, Plant Sale](https://edbodmer.com/wp-content/uploads/2022/10/Part-3-Financial-Structuring-Blank.xlsm)
**

.

**[Part 3 - Excel File with Filled Equations for Project Finance Issues including Development Fee, Re-financing, Plant Sale](https://edbodmer.com/wp-content/uploads/2022/10/Part-3-Financial-Structuring-Filled.xlsm)
**

.

.

Case with Toll road and Circular Reference from Sculpting and taxes with UDF
----------------------------------------------------------------------------

.

This section has videos and case studies from what I call the j Fitzgeral case. It is a case with semi-annual timing, sculpting, taxes, acquistion value, sensitivity cases and other items. I think it is a good case to work through for some advanced issues.

.

**[PDF File with Case Study on Toll Road Including Sculpting, Tax, Semi-Annual and Sale of Asset at Lower Target IRR](https://edbodmer.com/wp-content/uploads/2023/09/JFK-wit-notes.pdf)
**

.

**[Excel File with Case Study on Toll Road with Semi-Annual Cash Flow and Sculpting with Target Acquisition Price - Part 1](https://edbodmer.com/wp-content/uploads/2023/09/JFK-Project-Part-1.xlsm)
**

.

.

.

**[Excel File with Case Study on Toll Road with Tax and Sculpting using Copy and Paste Macro - Part 2](https://edbodmer.com/wp-content/uploads/2023/09/JFK-Project-Part-2-End.xlsm)
**

.

.

**[Excel File with Case Study on Toll Road with Implementation of Parallel Model and Debt Structuring - Part 3](https://edbodmer.com/wp-content/uploads/2023/09/JFK-Project-with-UDF-Final.xlsm)
**

.

.

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

.

.

.

.

### Section 4: Exercises for Course Including A-Z Model, Circular Exercises, Cash Flow Waterfall, Mini-Perm

As with the the other exercises, the button attached to the first file is the file with equations for you to fill in. The second button is attached to the file with the completed exercise.

.

**[Project Finance Modelling Course File with Blanks - File with Exercises for A-Z Model, Circular References, Mini Perm etc.](https://edbodmer.com/wp-content/uploads/2022/11/FAST-Simple-Case.xlsm)
**

.

I have include a file and a video below that works through some of the various different project finance issues. I use this file to go from a basic analysis to a more sophisticated analysis. The workbook attached to the button has many of the subjects discussed below.

.

**[Excel File with Comprehensive Project Finance Exercises and Model Mechanics from Basic to Advanced](https://edbodmer.com/wp-content/uploads/2021/10/Financial-Modelling-Class-Thursday-30-September-Without-Exercises.xlsm)
**

If you want the files associated with levelised cost I have the files in a folder (chapter 1, project finance and circular references) of the resources. Just drop and email to edwardbodmer@gmail.com and I will send a google drive with a whole lot of stuff (probably too much). But you can unzip the files and look for what you want and save the google drive in the cloud….

### Working through a Model from A-Z with Funding, Sculpting and Circular References

If you want to see an exercise for working through structuring issues with alternative funding you can go to the link below.

[https://edbodmer.com/financing-exercise-without-circular-reference/](https://edbodmer.com/financing-exercise-without-circular-reference/)

.

### Advanced Issue 1: Structuring a Project with Evaluation of Debt Size from Either P90, P50, or Maximum Debt to Capital

[https://edbodmer.com/solar-battery-hydrogen-course/](https://edbodmer.com/solar-battery-hydrogen-course/)

.

### Advanced Subject 2: Inclusion of DSRA changes in the DSCR for Debt Sculpting

[https://edbodmer.com/including-releases-or-deposits-to-dsra-in-dscr-and-sculpting/](https://edbodmer.com/including-releases-or-deposits-to-dsra-in-dscr-and-sculpting/)

.

### Advanced Issue 3: Resolving Circular References without Copy and Paste Macros or the Iteration Button

[https://edbodmer.com/technical-details-of-udf-parallel-model-concept/](https://edbodmer.com/technical-details-of-udf-parallel-model-concept/)

.

### Advanced Issue 4: Computing Debt Repayment where the Debt Size is Given, and Sculpting is used to Obtain a Minimum DSCR with Varying DSCR’s

[https://edbodmer.com/sculpting-with-fixed-debt-and-changing-dscr-goal-seek-and-data-table-method/](https://edbodmer.com/sculpting-with-fixed-debt-and-changing-dscr-goal-seek-and-data-table-method/)

.

### Advanced Issue 5: Debt Sculpting of Multiple Debt Issues where cash flow is Affected by Interest Expenses and Income Taxes

[https://edbodmer.com/multiple-sculpted-issues/](https://edbodmer.com/multiple-sculpted-issues/)

.

### Advanced Issue 6: Incorporating options for DSRA funding with an L/C or with Cash Funding

[https://edbodmer.com/sculpting-and-debt-fees-including-fees-for-dsra-l-c/](https://edbodmer.com/sculpting-and-debt-fees-including-fees-for-dsra-l-c/)

.

### Advanced Issue 7: Modelling Sculpting with Balloon Payment at End of Tenor

[https://edbodmer.com/separation-into-balloon-payment-and-sculpting/](https://edbodmer.com/separation-into-balloon-payment-and-sculpting/)

.

### Advanced Issue 8: Adding Re-financing to a Model where Debt Size Depends on Taxes which are Affected by Interest on the Re-financing

[https://edbodmer.com/re-financing-analysis/](https://edbodmer.com/re-financing-analysis/)

.

### Advanced Issue 9: Evaluation of NOL Time Limits on the Calculation of Income Tax

[https://edbodmer.com/expiration-of-nol-in-project-finance/](https://edbodmer.com/expiration-of-nol-in-project-finance/)

.

### Advanced Issue 10: Computation of the LLCR with Different Debt Issues using the Prospective debt IRR

[https://edbodmer.com/llcr-and-plcr-complexities-and-meaning-for-break-even/](https://edbodmer.com/llcr-and-plcr-complexities-and-meaning-for-break-even/)

.

### Advanced Issue 11: Modelling Equity Bridge Loans and the Associated Circular References along and Options for IDC

[https://edbodmer.com/equity-bridge-loans-ebl/](https://edbodmer.com/equity-bridge-loans-ebl/)

.

### Advanced Issue 12: Modelling the Effect of Financing in Different Currencies with Translation Adjustments

[https://edbodmer.com/currency-adjustments-taxes-and-debt/](https://edbodmer.com/currency-adjustments-taxes-and-debt/)

.

### Advanced Issue 13: Modelling Development Fees with Multiple Investors

[https://edbodmer.com/development-fee-timing/](https://edbodmer.com/development-fee-timing/)

.

### Advanced Issue 14: Including Actual Data in Models for the Construction Period and Operating Period

[https://edbodmer.com/project-finance/actuals-in-project-finance/](https://edbodmer.com/project-finance/actuals-in-project-finance/)

.

### Advanced Issue 15: Modelling Mini-perms and Different Re-financing Assumptions

[https://edbodmer.com/mini-perms-and-re-financing/](https://edbodmer.com/mini-perms-and-re-financing/)

.

### Advanced Issue 16: Developing Alternative ways to Model Working Capital Requirements in the Initial Operating Periods of a Project

[https://edbodmer.com/working-capital-in-project-finance/](https://edbodmer.com/working-capital-in-project-finance/)

.

### Advanced Issue 17: Evaluating Different Structures for Equity Investors including Cash Flow Flips and Incentives to Developers.

[https://edbodmer.com/performance-incentives-for-developers/](https://edbodmer.com/performance-incentives-for-developers/)

.

### Advanced Issue 18: Accumulation of Projects into a Portfolio or a Fund

[https://edbodmer.com/project-with-multiple-spvs/](https://edbodmer.com/project-with-multiple-spvs/)

.

### Advanced Issue 19: Modelling Alternative Cash Sweep Structures

[https://edbodmer.com/cash-sweep-and-risk-versus-return/](https://edbodmer.com/cash-sweep-and-risk-versus-return/)

.

### Advanced Issue 20: Valuation of Projects with Changing Buyer Target IRR’s and Computation of Holding Period Returns

[https://edbodmer.com/irr-with-changing-discount-rates-and-assumed-sale/](https://edbodmer.com/irr-with-changing-discount-rates-and-assumed-sale/)

.

### Advanced Issue 21: Evaluation of Defaults and the Risks of Senior and Subordinated Debt

[https://edbodmer.com/cash-flow-waterfall-and-financial-statements/](https://edbodmer.com/cash-flow-waterfall-and-financial-statements/)

.

### Advanced Issue 22: Creating Data Tables using VBA to Resolve Data Table Problems

[https://edbodmer.com/data-tables-with-goal-seek-using-vba/](https://edbodmer.com/data-tables-with-goal-seek-using-vba/)

.

### Advanced Issue 23: Time Lines with Different Periods and Required Sums

[https://edbodmer.com/timelines-in-project-finance-models/](https://edbodmer.com/timelines-in-project-finance-models/)

.

### Advanced Issue 24: Effective Control Pages where you can Evaluate Changes to Inputs and Properly Include the Inputs in Relevant Input Sheets

[https://edbodmer.com/scenario-analysis-with-diagrams-spinners-and-reset/](https://edbodmer.com/scenario-analysis-with-diagrams-spinners-and-reset/)

.

.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/05/image-10.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/05/image-9.png)

Step 1: Make Monthly Flag (Easy)

Step 2: Make Flag for Semi-Annual Month Ends – Be careful, this must be the month of repaymet with -1 in the edate. e.g if repayment date is 6 months after 1- Jan COD, then the first repayment is the period 1-June (5 months) and not 1-July.

Step 3: Make a COD flag. Will need this to start at COD and not 6 months after COD

Step 4: Make a flag for COD and prior Semi-annual flag from Step 2. Important to use prior flag and not same period flag.

.

![](https://edbodmer.com/wp-content/uploads/2023/05/image-11.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/05/image-13.png)

For the class, open the file named the exercise file and work through the file. In working through the file I think it is a good idea to have the generic macro file open. The hardest part of this is counting the months from the COD date to the first repayment date and then making sure that you have the time line correct. For this, I must count on my fingers and then use a counter that counts six for semi-annual periods from the COD date. Once you have the counter correct you can use the SUMIF function.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=14445&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10592&rand=0.09268159816751087)