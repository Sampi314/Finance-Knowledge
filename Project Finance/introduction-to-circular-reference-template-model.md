# Solving the Pain Points in Project Finance Modelling

**Source:** https://edbodmer.com/introduction-to-circular-reference-template-model

---

Making a basic project finance model with time lines, projected cash flows and even structured debt repayments can be accomplished quickly and with relatively little pain using standard excel techniques.  But when you start to incorporate tricky funding mechanics, income taxes in different currencies, multiple debt issues that are all sculpted, changing DSCR’s to meet a minimum DSCR requirement and generate a given amount of debt, refinancing to meet a DSCR, modelling alternative debt sizing that is affected by taxes, sculpting and other issues you will hit a wall. Project finance models that are used for structuring debt and other contracts can then become rigid, difficult to understand, impossible to update for restructured financing and use formulas that seem incomprehensible because of attempts to compute sculpted repayment; incorporate different DSCR criteria; include liquidated damages; work with multiple debt issues; model VAT payments that are refunded; and, compute debt repayments from the DSCR when debt size is driven by debt to capital ratio.  Further, when you want your model to be really flexible so that you can change the debt sizing technique, any variable and then re-set your model to a base case, the process can be very awkward when you have to press a copy and paste button whenever you change something. This page discusses how the real difficulties and the pain points in project finance modelling can be solved using a system that my friend Hedieh an I have developed over the past few years. 

The system for resolving of circular references (a lot of VBA code) allows you to take a model and put it together with a really big user defined function (UDF) that avoids the need for resolving circular references with copy and paste macros. But this method is in no way just about circular references. The modelling approach allows you to solve complex debt structuring issues (for example sculpting multiple issues where the debt size is derived from debt to capital); it verifies financial and tax equations in your model; it can be dramatically faster than copy and paste macros; and it can be used to produce effective financing presentation.

.

History of UDF Development
--------------------------

The history of the UDF development demonstrates the various aspects of the process and why it is unique.

*   Worked on automatic goal seek using a UDF rather than the goal seek excel tool – involves writing equations and iterating
*   Realised that goal seek was an approach for solving circular references
*   Developed simple UDF for circular reference by modelling financial model equations in the UDF and using an iterative process
*   Developed the UDF approach with more complex problems (debt sizing and debt sculpting) but ran into problem with limits on reading variables into the UDF
*   Created approach for reading more data into UDF by putting data into a large two dimensioned array that can be separated into time series variables
*   Attempts to implement model into larger more complex models were unstructured and it was difficult to revise formulas
*   Created a modular approach with public variables and separate modules so you could much more easily find the variables
*   Created a more flexible output back to excel process so you can better mimic the process of entering formulas in excel through verifying calculations one row at a time
*   Realised that copying the UDF into a financial model and formatting the output of the model was tedious
*   Created macros to automate putting the UDF into models and formatting the output
*   Realised that the important benchmarking process was difficult and created options to temporarily fix items to make the process much easier to implement

.

**[Template UDF Parrallel Model that You Can Put Directly in Your Model By Pressing Button and then Following Instructions](https://edbodmer.com/wp-content/uploads/2024/01/Updated-Template.xlsm)
**

.

**[Excel File with UDF from March 2013 including Multiple Debt Issues and Structuring versus Risk Analysis](https://edbodmer.com/wp-content/uploads/2023/04/File-for-Kenny-Session.xlsm)
**

.

.

.

.

.

.

.

.

.

.

.

Good and Bad Things about Excel
-------------------------------

Excel has taken over and it is certainly the tool for financial models. You can modify things easily and present outputs well. The calculations are efficient and any real thought of using tools other than excel are not very serious.

But excel does not do some things very well. These include:

*   A lot of repetitive calculations were you want to present selective outputs
*   Circular references
*   Structured models with error checks
*   Selected functions like interpolate
*   Compiling data sets

To solve these and other pain points in structuring a model we have developed a tool called the parallel model. I have worked with Hedieh on this. She is always looking for better way to structure and present her financial models.  She has helped me enormously over the years with new ideas; with explanations of how real world project financed investments are structured; with finding contacts in the project finance community; and with very creative suggestions on how to make some of my methods applicable in the real world.  Hedieh is the world leader in applying parallel model concepts in real world project finance models.  She is responsible for our system of putting making the parallel model flexible, transparent and structured for real world applications.  You can see some of her work at www.finmod.com and you can order her book by clicking on the picture below.

The system that Hedieh and I have developed is founded on re-writing formulas in a separate program can solve debt sizing, repayment sculpting, complex funding, auditing, tax, re-financing and model presentation challenges in project finance models. This method may occasionally involve a little programming, but a template program covers the vast majority of pain points that you may experience. I explain how the method that I have developed with Hedieh over the past few years that translates formulas which create circular references can address the pain points and at the same time make project finance models more transparent, more efficient, more flexible and accurate.  Importantly, recent work with Hedieh has made the process of adding the technique to your existing models much easier to implement and to adjust to particular circumstances. Rather than working through the technical details of our method, this page explains each part of project finance models that can cause you to bang your head against the wall and why our method can ameliorate your pain.

.

#### Playlist of Videos for Solving Circular References

.

.

Pain Points in Project Finance Models
-------------------------------------

If you are explaining how a pill can make you feel better, you could describe each of the chemicals in the pill and details of the scientific theory of why the pill should work. This may be interesting to some scientists.  But most people would be much more interested in seeing how the pills really do make you feel better (and hopefully do not result in cancer).  This latter approach of describing how something can reduce the pain rather than the technical details of our approach is the subject of this page.  Other pages work through how to accomplish relatively standard things in financial modelling such as scenario analysis, efficient and transparent structures for setting up modelling calculations for different companies and application of finance theory to models.  This page does not deal with issues that can be easily resolved in excel (or resolved with a bit of work).  It deals with things that do not really work in excel without going outside of the program.  It is advanced and it is for people (hopefully you) who want to take the excel models to the next level. It is primary publicity and if you want to know more about our services for implementing the method, please fill in the contact form below.

### Pain Point 1: Big Models Take Too Long to Calculate Making it Difficult to Efficiently Present Scenarios, Risks and Opportunities to Management

![](https://edbodmer.com/wp-content/uploads/2020/06/Pain-Point-1.png)

These days, models are often very big and include very detailed and precise calculations.  It is not uncommon to see models that are more than 10 megabytes. If you are working with one of these big models that may be computed on a monthly basis or may have a whole bunch of detail for operating costs, capital expenditures, debt issues and revenues, circular references that are resolved by with copy and paste macros can slow your model down and take 10-30 seconds to run.  This may sound like it is not a big deal, but it is really painful when you are making presentations with your models in important meetings. For example,  you may want to try a whole lot of different delay scenarios along with potential increases in the EPC cost to compensate for the risk.  You may think that pressing the copy and paste button and sitting silent for 20 seconds each time is not a big deal.  But it can ruin your meeting. Our method using the parallel model is far more efficient than going to a range, copying it, and doing this over and over again (the copy and paste method).

If you click on the picture you can see how much difference in time it takes it to resolve circular references associated with the construction period of models (interest and fees during construction, development fees, the DSRA, interest on VAT) compared to with resolution of the circular references using our method.  In the example the time declined by a factor of something like 10 times by using our system.  This means that when you present scenario analysis to senior executives and investors, they will immediately see the risks and benefits of the project rather than having the irritating dead time.  Click on the link attached to this sentence to find out more.

### Pain Point 2: Non-transparent Buttons or Circular Reference Warnings When you Open the Model

If you are creating or reviewing a project finance model or a real estate model that does not have our system implemented, two things generally happen when you open the model.  The first possibility is that you  receive a circular reference warning because you do not have the iteration button clicked in excel.  You can try to fix this by finding the iteration button and enabling it, but if you do and you try to restructure your model, you will often destroy the model and you will receive a lot of #REF’s.  You also cannot use the goal seek tool which is one of the most important features for structuring revenue, expense and loan contracts. Alternatively you may see some kind of really artistic button the resolves the circular references in the model with copy and paste macros. Even if you are very proud of your copy and paste button, most people are afraid to move things around and then press the buttons (it is often fine, but if the copy and paste is not well written it can be dangerous). Worse, the little bit of code in the model can be difficult to understand and be non-transparent.  If you are good at writing code you can make the code work with goal seeks or data tables, but this is not very easy. (Click on the pain point picture for video illustration of pain point resolution.)  An example of a model that contrasts our method with a copy and paste method is illustrated in the file that is attached to the button below.

**[Excel File that Demonstrates Pain Points for Pressing a Copy and Paste Button with Flexible UDF and VBA Code](https://edbodmer.com/wp-content/uploads/2020/07/Off-Shore-Wind-Model-Updated-v04.xlsm)
**

### Pain Point 3: You Run Into a Brick Wall When You Try to Optimise DSCR’s that Drive Debt Repayments to Project Finance Models

![](https://edbodmer.com/wp-content/uploads/2020/06/Pain-Point-5.png)

When you build a model you are really evaluating how your project works in the context of a complex web of contracts and an array of risks. One of the important items in the loan agreement contract that can affect the returns to shareholders and the risks to bankers is the repayment profile of different loans known as sculpting. This manner in which a loan is repaid can take more time and be subject to more negotiation than just about any other provision.

Loan agreements can define at the same time the amount of the loan as a percent of total project cost and the minimum DSCR that is acceptable.  Defining these two terms seems straightforward but it in fact means that the DSCR may not be constant over the term of the debt.  Computing a DSCR that is not constant and meets the requirements of the debt term sheet is a complex process. Project finance models may use all kinds of excel techniques (solver, goal seek with trial and error) which are difficult to resolve in computing the optimal sculpting for the case when the debt size is given by a fraction of the project cost and the cash flow coverage must be above a given minimum.  The method we have developed allows you to resolve issues such as computing a non-constant DSCR to meet the terms of the loan agreement without manual and crude procedures.   This page introduces my preferred approach to resolving circular references using a concept that I call the parallel model.  (Click on the pain point picture for video illustration of pain point resolution.)

.

### Pain Point 4: Modelling the Allocation of Debt to Different Debt Facilities with Sculpted Repayment

![](https://edbodmer.com/wp-content/uploads/2020/06/Pain-Point-3.png)

One of the most difficult things in creating a project finance model structuring the repayment with sculpting for many different debt issues that have different terms (interest rates, tenures and so forth).  If you have a solar or a wind project, sculpting debt is a practical necessity. Different financial institutions that may lend to the project with different terms include export credit agencies, development institutions like the African Development Bank and a multitude of private banks.  The programming problem is that all of the debt issues may have sculpted debt repayment and they may have different tenures.  This makes the sculpting exercise very difficult.  Our method resolves this quickly. (Click on the pain point picture for video illustration of pain point resolution.)

.

### Pain Point 5: Adding Alternative Funding to Models

![](https://edbodmer.com/wp-content/uploads/2020/06/Pain-Point4.png)

Funding issues in project models can become complex when you consider that some items may be paid by the project, but not be permitted by the financial institution to be included in their financing calculation.  For example, say that you spend 1,000 for the EPC contract and another 100 for owners costs that include your CEO’s salary.  The bank may include only the 1,000 of EPC cost in the calculation for computing both the debt to capital ratio and draws.  I call this the debt financing base.  In the financing base that is used for calculation of such as Interest During Construction on Mezzanine, development costs that are included , EPC fees, Shareholder IDC and other items may be included in the project cost for purposes of computing debt, but they may be included in the total project cost for purposes of computing equity investment and for purposes of depreciation and assets on the balance sheet.  Other difficulties include the treatment of liquidated damages (e.g. does all of the liquidated damage proceeds reduce the amount of debt) and the manner in which VAT taxes are included in the sources and uses of funds.  All of these items as well as the DSRA cause circular references and can slow down operation of the model. There may be capitalisation of interest, some items may not qualify for financing, there may be mezzanine debt issues or there may be shareholder debt or thene may by equity bridge loans. All of these factors change the way the circular references work and you may want to change the methods.  Our approach is flexible so you can change things and then demonstrate the effect on the investment without re-writing different copy and paste macros.

.

### Pain Point 6: EBITDA and Cash Flow are Different in Structuring Debt Size and Debt Repayment than the EBITDA and Cash Flow for Risk Analysis as with Scenarios (P50, P99) with Debt to Capital Constraint

For good reason lenders can impose a number of different tests in setting the size of debt.  The debt cannot be more than a given amount of the project spending.  But the debt cannot result in a DSCR below a given level in a negotiated base case financial model and it also must meet another DSCR criteria in a negotiated downside case.  This means that your model must include different cash flow scenarios and it must be able to optimise the amount of debt issued from the different scenarios. Funding issues in project models can become complex.  Finally, you link variables from the parallel model page to items like interest during construction, CFADS and funding needs that are often fixed from copy and paste macros.

### Pain Point 7: Adding Re-Financing Into Your Models

After you have finished making your model, the last thing you feel like doing is adding some potential refinancing to the model.  When you add re-financing to the model it can occur at different times and it can have different sizing assumptions.  Worse, the sizing of the refinanced debt depends CFADS which in turn depends on the taxes that are paid.  But the taxes drive the CFADS and thus the size of the re-financed debt. After working out all of the other circular references with copy and paste macros, do you really want to deal with another one.  With the method Hedieh and I have developed, you can enter a new re-financed debt issue into the model and evaluate the IRR without further copy and paste macros.

.

### Pain Point 8: Carefully Auditing Calculations in Your Model that Result in Circular References

You can make obvious checks to a model like the balance sheet balancing, the sources matching the uses, and the debt being fully repaid. But checking the interest during construction on each debt issue; assuring that the development fee is computed on the basis of project cost; evaluating the sculpting calculations and many others are very difficult to verify. The method that Heideh and I have developed forces you to test your model carefully and can be considered and enhanced auditing tool.

### Pain Point 9: Incorporating Complex Tax Regulations into Your Model

The screenshot below illustrates the kind of issues that you may run into these days. First, there are taxes and the taxes can become quite complex. Second, the debt sizing can come different revenue elements or it can come from the the debt to capital ratio. This can lead to really painful points.

[Excel File that Addresses Advanced Issues Including Alternative Currencies and Translation Adjustments in Models](https://edbodmer.com/wp-content/uploads/2021/05/Advanced-Course.xlsm)

.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-74.png)

.

Tax calculations can be simple or complex in models.  A common problem is that depreciation expense can be in local currency while the model results are in a different currency such as Euro or USD. 

### Pain Point 10: Development Cost and Fee Analysis

https://edbodmer.com/wp-content/uploads/2020/07/Off-Shore-Wind-Model-Updated-v04.xlsm

How You Can Incorporate the Parallel Model Concept into Your Models
-------------------------------------------------------------------

This section explains how you can work with us to implement the parallel model without much pain. The fundamental point is that many things are really good in excel like structuring input sheets; like designing time lines and flags; like computing EBITDA with different economic assumptions. But there are a few things that suck with excel. The biggest of which is dealing with circular references and having to copy and paste from a structuring mode to a risk analysis mode using sculpting.

### Step 1: Potential Re-structuring of Your Model

Use of generic macros; master time line

### Step 2: Addition of Parallel Model Template

### Step 3: Instruction on Modification to Parallel Model Template

History of the Parallel Model Concept
-------------------------------------

I hope that by browsing through the history that made me arrive at this parallel modelling concept you can understand why I think it is such an important idea for the project finance modelling community. The time line below illustrates some of key events that have led to the UDF method. The timeline demonstrates that many different factors had to be put together to enable this method to be used in an efficient and realistic manner in your models. I did not put in the timeline dates because I of course don’t remember them.  But this is not a project that has taken a few months or even a year. I think I must have started this model around the financial crisis in 2008.

![](https://edbodmer.com/wp-content/uploads/2019/03/Timeline.png)

### Concerns about Circular References

![](https://edbodmer.com/wp-content/uploads/2019/03/Survey.png)

I have been teaching classes in project finance modelling since 1997 (my classes back then were not too good).  In preparing for classes, I used to give out a pre-course questionnaire where I asked what students wanted me to focus on.  For example, I would ask if participants wanted to create models from A-Z models or whether they wanted to deal with more advanced issues like circular references (illustrated below). A few people asked how to avoid impossible to understand macros for circular references and how to avoid using the iteration button in excel.

I was arrogant and I thought that I could find a better method than the copy and paste method or the very dangerous (geferlish) iteration button. I had a disastrous class using the iteration button with #VALUE!’s and #REF’s that I could not get rid of and decided never to use the iteration button again.  I remember whenever we tried to add a scenario analysis or anything a little different the whole model crashed and then we had to start over.  I had a lot of nightmares about this and I still get very nervous with the dreaded blue lines.

.

### Initial Efforts to Solve Circular References with Mathematical Formulas and Backwardation

.

I began to try to solve the problem after reading the comments from my students and my disastrous.  First I tried to find mathematical equations that could solve the problem that can be used in corporate modelling and simple things like contingency fees.  For things like a contingency payment that is a percent of the cost of the project including the fee is a very simple example of this. But when solving things like IDC, these equations became very long as shown in the excerpt that I still have in the resource library.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Mathematical-Equation.png)

.

I remember trying to solve the commitment fee problem while riding on my brother’s boat on the Amazon (his website) and it was impossible for me. I gave up on the mathematical equations and decided that I had wasted a lot of time.  Then I tried a method where you can find equations for the closing balance and then back into the opening balance that some people call backwardation.  This method seemed promising at first and then quickly became impossible. Maybe it was best to just use the copy and paste method.

### Big Moment of UDF Discovery for Solving Circular References

![](https://edbodmer.com/wp-content/uploads/2019/03/John-Lennon.png)

You have heard stories about remembering exactly you were when big events happen. I remember that I was going to take an accounting exam in a little farm town when I heard about the killing of John Lennon. I remember the hotel were I was when I saw the Fukushima tsunami and I also remember in what hotel I was staying at when I heard the depressing news about Brexit and Donald Trump’s election.

When I was working on a dynamic goal seek where you make a UDF function that automatically computes the goal seek without pressing any menu items, I tried a similar technique for a simple circular reference.  And it worked.  This was a really big moment in my old age. I remember exactly what couch I was sitting on when the UDF technique with a little iteration button worked.  Then I took a shower while I was shaking with excitement.  I then tried it with more and more complex applications that included for next loops.  And, the UDF method still worked. I dropped the other methods involving mathematical equations and started working on real applications.

### Implementing UDF in Project Finance Models

![](https://edbodmer.com/wp-content/uploads/2019/03/Function-Inputs-1.png)

To implement the UDF technique, you have to work backwards across all of the dreaded blue lines in the circular reference.  You start by making an equation for the item that causes the circular reference and then add more and more equations. With this you can solve circular references that for example come from IDC that also affect depreciation and therefore taxes and therefore CFADS and therefore sculpting which then affects debt and IDC itself.  There can be a lot if inputs and equations for solving the circular reference and you must input them all. 

I demonstrated with quite a few models that it is totally possible to do this.  But the required inputs and the equations can be difficult as shown in the adjacent screenshot. You can see the inputs that you have to put into your user defined function.  These are a lot more inputs than you would have to put in any function in excel.  I moan a lot about long formulas being non-transparent.  I was a hypocrite to suggest that you would every realistically do this (except Hedieh who did make models like this). If you have to re-write these equations each time you make a model, it is frankly not very realistic.

### UDF’s and Advanced Project Finance Issues

![](https://edbodmer.com/wp-content/uploads/2019/03/Advanced-Modelling.png)

These days some of my clients are not very interested in boring old blah blah blah about quickly making a model and computing the IRR’s, DSCR’s, LLCR’s etc. Instead they are interested in things like what is the effect on the investor and the lender from balloon payments, inclusion of changes in the DSRA on sculpting, how to evaluate strategies when there is both a debt to capital constraint and a DSCR construction, how to sculpt multiple debt issues, what is the effect of re-financing and these kind of more advanced issues.

I have included a screenshot of the place where you can find [some of the advanced issues](https://edbodmer.com/http-edbodmer-wikispaces-com-project-finance-structuring/)
 on this website. When creating exercises for these models such as for [balloon payments](https://edbodmer.com/sculpting-with-multiple-debt-issues-or-balloon-payment/)
 or analysis of putting [changes in the DSRA](https://edbodmer.com/including-releases-or-deposits-to-dsra-in-dscr-and-sculpting/)
 in CFADS or debt service, there are a lot of circular references. The UDF technique worked well as a way to make the models flexible (with spinner boxes etc.) and with goal seeks and with simple data tables.  So, even if the UDF function was not too realistic in big models, the UDF discovery for me was not a complete waste of time.

### Meeting with Hedieh and Template Concept

I tried to be realistic realistic about the prospects for this UDF stuff. I touted the method in videos and I demonstrated the approach in my classes.  But nobody seemed very interested.  I was a bit depressed but I just think about Churchill’s saying that success is going from one failure to another without lack of enthusiasm. There was one person who was still interested in the concept — Hedieh Kanfard.

![](https://edbodmer.com/wp-content/uploads/2019/03/Istanbul.png)

She suggested a meeting in Istanbul and worked on the models. We were able to implement part of the concept for the funding circular references in a real model that she was working on. She was even able to copy the code into other models she created and it still worked. She suggested making a template UDF that could be applied in alternative situations. At first I thought about how I do not like template models (I tried them in the past).  Then I reluctantly told Hedieh that I would try to make a template UDF.

Hedieh later introduced me to Danny and Kenny who I could tell did not believe the concept.  They told me they were trying to develop innovative new project finance modelling methods.

### Reading Data from Tables and Making the UDF Concept Manageable

When I started working on the template model suggested by Hedieh I ran into a problem. To make a flexible template you would need to read in a whole lot of different variables and to make it usable, the method would have to deal with many different options including multiple debt issues and therefore be able to read in many variables. But there is a limitation for UDF functions involving the number of variables that can be read in — only 128 characters.

This limitation made it virtually impossible to make a usable template. Then, when sitting at a cafe, I googled the limitation and found someone who suggested using a table for reading in data.  This changed everything.  Reading a table into a UDF was painful to develop but I think it can make the parallel model realistic to use. I wish I could thank the man who made the suggestion on google.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Read-In-Variables.png)

.

### Structuring a Flexible and Comprehensive Parallel Model

Once the process to easily read information into the UDF was solved, I worked for a long time creating a comprehensive template model that . The UDF can output anything you calculate and this output can be structured consistent with they way project finance models should work.  The outputs can work all the way through a model to the equity IRR after EBL, shareholder loans and re-financing. This allows you to verify your model. But more importantly, you can try a whole bunch of advanced things like balloon repayments, multiple re-financing, DSRA moves in CFADS, using a letter of credit in lieu of a funded DSRA, multiple sculpting, mezzanine debt, EBL’s alternative debt sizing and other things without re-doing your model. In terms of verifying your model, at first when I checked the differences between the UDF model and my excel models, many of the mistakes were in the UDF model.  But after working very hard and making my mistakes, the parallel model can find mistakes in your model now. That’s why I am arrogantly claiming that this concept represents the future of modelling.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Future-Picture.jpg)

.

Video Demonstration of Parallel Model (with Beetoven’s 9th)
-----------------------------------------------------------

The video below illustrates how you can implement the parallel model concept in your model in a couple of minutes.  I have not made you listen my voice while you see how it works.  Instead, you can listen to Beetoven’s Ode to Joy.  In subsequent pages you can see how this concept works in a whole bunch of different models and advanced project finance concepts.

Explanation of Parallel Model Features in Associated Web Pages
--------------------------------------------------------------

When I first developed some UDF’s I made the UDF’s with really long lists of inputs that were painful to implement.  But the process worked.  Then I met with my friend Hedieh and she told me to make a template model.  My first reaction was that template models really suck.  But then I realised that she was absolutely right. I have tried to convince you that the parallel model/UDF concept is realistic to implement and can be applied to many different circumstances in the web pages associated with this section. My goal is to make you interested enough in the concept to become motivated to be a really advanced and efficient modeller.  So here is a demonstration of how easy the process is to make.

First, with your financial model open, open the first file below that you can download by clicking on the box.  This file contains the UDF code for making a parallel model.  Once you have opened the file, copy the code to your model (in English you can use the ALT, E, M short-cut) and click the button for creating a copy.

.

**[Add-in File that Includes UDF for Making a Parallel Model and Resolving Circular References in a Project Finance Model](https://edbodmer.com/wp-content/uploads/2018/11/Circular-Template.xlsm)
**

.

To illustrate how this process works, I have included a second file that is a very simple project finance model.  As usual, the simplest model is a solar model (although I seen amazingly long and absurd models for simple projects – an impeachable crime). The file that I will use in the example is available for download by clicking on the button below.

.

**[Basic Project Finance Model that is Solution to the Case Study and Used for Illustrating Parallel Model](https://edbodmer.com/wp-content/uploads/2018/11/Basic-Solar-Model.xlsm)
**

.

*   The first exercise with the parallel model involves working with simple annual model with a one period construction duration.  This case is used to demonstrate that the parallel model can be applied for case with no circular reference or a case with circular references only for DSRA and fees.  In this case, the model is annual model.
*   The second exercise with the parallel model involves working with multiple debt issues in the context of a simple model. In this exercise, the parallel model is attached with multiple debt issues in alternative sculpting scenarios.  In the first case there is no sculpting.  In the second case there is one sculpted issue and multiple non-sculpted issues.
*   The third exercise using the parallel model addresses re-financing.  Re-financing can be tricky if taxes are combined with sculpting to determine the amount of debt that can be supported at alternative assumed repayment dates.
*   The fourth exercise using the parallel model addresses various more complex issues including periodic construction on a monthly basis, semi-annual operations, an EBL, withholding taxes, tax timing, alternative depreciation for financing costs, multiple debt issues with sculpting and other factors.

Overview of Step by Step Process for Applying the Circular Reference Template
-----------------------------------------------------------------------------

To make the process work, you just follow the few steps below:

Step 1: Copy the template sheet into a new sheet of your model. The template has the required inputs that go into the UDF (most of which can be left blank or unchanged) and outputs generated from the UDF. After you have opened both of the models, the first step of copying the parallel model to your project finance model and using the copy check box is illustrated in the first screenshot.

Step 2: Copy the UDF functions related to the parallel model into your model. First go to the copy macro button in the parallel mode (not your model) and the press the copy macro button. After pressing the button, the VBA code will appear in a box. Go to the box an press CNTL A first and then CNTL C. This is illustrated in the first screenshot below. After pressing CNTL A and CNTL C, you should exit the screen so you can paste the code.  To do this press the x or the close button on the screen.

Step 3: Once you have copied the code, go back to your model. Find the VBA page with the functions and then copy the functions to a VBA page in your file. Then type any name for a macro in the box shown below.  This could be something like TEST or COPYPASTESUCKS.  Then, delete anything that excel puts there and make sure you paste the VBA code to the top of the page. More specifically, the OPTION BASE 1 should be at the top of the page. The two screenshots below illustrate the process of copying the UDF from the parallel model to your model.

Step 4: Make a timeline in the new page of your model that contains the UDF. The timeline should include switches for the development, construction and operation period. The periods in the time line (e.g. months during construction) should be consistent with interest calculations in the base model.

Step 4: Go to the input section of the UDF and find the required inputs such as periodic interest rates, EBITDA and DSRA requirements. These inputs should be lined from the financial model. (It is possible that you may have to make a couple of calculations in your model to compute things like effective interest rates on different debt tranches).

Step 5: Enter the function and use the SHIFT, CNTL, ENTER sequence

Step 6: Link various circular references from your model such as funding needs, CFADS, and DSRA to the parallel model

To illustrate how the circular reference model works in general, I have presented a short discussion of the inputs and outputs below along with a discussion of how to

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=4604&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12004&rand=0.6932866732030298)