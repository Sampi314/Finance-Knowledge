# Average DSCR in Financial Modelling

**Source:** https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling

---

Average DSCR in Financial Modelling
-----------------------------------

[Forvis Mazars Financial Modelling](https://financialmodelling.forvismazars.com/)
[Tutorials](https://financialmodelling.forvismazars.com/online-resources/tutorials/)

Average DSCR in Financial Modelling

Average DSCR in Financial Modelling
-----------------------------------

By John Yeldham

Wednesday 13th February 2013

[](http://twitter.com/share?text=Average+DSCR+in+Financial+Modelling&url=https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling/)
[](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling/)
[](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling/)
[](mailto:?subject=Average%20DSCR%20in%20Financial%20Modelling&body=https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling/)

[![](https://financialmodelling.forvismazars.com/wp-content/uploads/2025/03/button3.jpg)](https://info.corality.com/download-dscr?__hstc=32075169.a5ae6dcfb5b45eeb545645f32e549665.1773830948730.1773830948730.1773830948730.1&__hssc=32075169.1.1773830948730&__hsfp=a19ed06593a6dc39eb1fdade76d7cf42)

There are two different ways to calculate the average debt service coverage ratio (ADSCR) that could result in different numerical outcomes. What are the methods, what are the limitations that we should be aware of and which one should be used?

Debt service coverage ratio (DSCR) is one of the most commonly used debt metrics in project finance. Aside from the profile of the DSCR calculated on every calculation period, the ADSCR is an important output in a project finance model.

Two financial modelling solutions to ADSCR
------------------------------------------

*   Calculate the average of the period-by-period DSCRs over the life of the loan
*   Divide the total [cash flow available for debt service (CFADS)](https://www.corality.com/training/learning/blog-list/blogs/september-2008/cfads-%E2%80%93-cash-flow-available-for-debt-service?__hstc=32075169.a5ae6dcfb5b45eeb545645f32e549665.1773830948730.1773830948730.1773830948730.1&__hssc=32075169.1.1773830948730&__hsfp=a19ed06593a6dc39eb1fdade76d7cf42)
     over the life of the loan by the sum of principal (P) and interest (I)

On the face of it there is not much difference, but this tutorial will demonstrate that they can result in very different numerical outcomes. We will discuss why they are different and when to use each method, particularly when dealing with exotic cash flows or repayments.

ADSCR method 1 – Calculate ADSCR of the period-by-period
--------------------------------------------------------

This may be the most common way to calculating the ADSCR.

Let’s recap this calculation method:

*   Calculate period-by-period DSCR (CFADS/P+I)
*   Calculate the average of the period-by-period DSCRs
*   It is calculated using the ‘Average’ function in Excel
*   Remember to define as an ‘Array’ to ensure that non-zero figures are utilised
*   Activate the ARRAY function with Ctr + Shift + Enter.

ADSCR = {AVERAGE ( IF ( RANGE < > 0, RANGE ) ) }

ADSCR method 2 – total CFADS / total of P+I
-------------------------------------------

The ADSCR is calculated using the simple steps below:

*   Total the CFADS over the life of the loan
*   Total the debt service over the loan life (i.e., sum of principal and interest)
*   Divide the total CFADS over the sum of principal and interests

ADSCR = total CFADS (life of loan) / total P+I (life of loan)

Comparing the two financial modelling solutions to DSCR methods
---------------------------------------------------------------

Let’s take a look at an example where the CFADS are flat and the debt is repaid on annuity basis, which means equal  P+I. Period-by-period DSCRs are then calculated during the life of the loan and plotted, as shown below.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2020/02/Screenshot-1_Flat-repayment-profile.png)

  
SCREENSHOT 1: FLAT REPAYMENT PROFILE

Here you can see that the average DSCR using both methods give very similar results, 1.62x and 1.63x.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2020/02/2-Flat-repayment-plot-1.png)

  
SCREENSHOT 2: DSCR CHART FOR FLAT DEBT REPAYMENT

Now let’s look at what happens when the repayment profile is flat but with a final repayment which is lower than the others. This is not unusual but can seriously skew the average, the plot below shows the final DSCR is significantly higher than the others in the example

![Example of debt sculpting to achieve target DSCR Step 4](https://financialmodelling.forvismazars.com/wp-content/uploads/2019/01/Example-of-debt-sculpting-to-achieve-target-DSCR-Step-4.png)

Example of debt sculpting to achieve target DSCR Step 4

  
SCREENSHOT 3: FINAL DSCR IS HIGHER

Here you can see that the two methods give very different results. Method 1 gives1.63x and method 2 results in 4.08x.

![](https://financialmodelling.forvismazars.com/wp-content/uploads/2020/02/Screenshot-4_Lower-last-repayment.png)

  
SCREENSHOT 4: LOWER LAST REPAYMENT

Comparing the financial modelling methods for ADSCR
---------------------------------------------------

There is a conceptual difference behind the two calculation methods:

*   Method 1: calculates the average of the DSCR values over time, treating all of the elements as equally important
*   Method 2: weighs each element by the relative importance of the sum of principal and interest in each period

The difference is not obvious when the cash flow/debt service is flat, as demonstrated in the first example. However, this is best highlighted when there are extreme values, such as the final repayment being very small as shown in the later example. The DSCR in the last period is enormously high, which is given equal importance in Method 1 and distorting the overall average.

Which calculation method for ADSCR is correct?
----------------------------------------------

There is nothing wrong with either method. The important thing is to understand what they actually mean and be aware of the limitations.

In certain situations, be aware that Method 2 is probably more meaningful and would be the more accurate representation of the average.

Forvis Mazars Financial Modelling
---------------------------------

There are numerous other tutorials and webinars related to financial modelling in the [Forvis Mazars Learning Resources](https://financialmodelling.forvismazars.com/financial-modelling-resources/)
.

Some of the more popular courses that relate to this topic include:

[Introduction to Project Finance Theory](https://financialmodelling.forvismazars.com/course-schedule/introduction-to-project-finance-theory-apac/)

[Best Practice Project Finance Modelling](https://financialmodelling.forvismazars.com/course-schedule/best-practice-project-finance-modelling/)

Latest posts

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2020/03/shutterstock_1403062694-1024x684.jpg)](https://financialmodelling.forvismazars.com/welcome-to-our-digital-classrooms/)

#### Digital Classrooms

Forvis Mazars – welcome to our Digital Classrooms! We are opening our Digital Classrooms to individual registrations, making our world-leading...

[Read more](https://financialmodelling.forvismazars.com/welcome-to-our-digital-classrooms/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2026/02/WhatsApp-Image-2026-02-12-at-10.18.58-1024x681.jpeg)](https://financialmodelling.forvismazars.com/ai-in-project-finance-blog/)

#### AI in Project Finance: New Course and Webinar

To help practitioners understand and apply AI in a practical disciplined way Forvis Mazars APAC Energy has launched two complementary...

[Read more](https://financialmodelling.forvismazars.com/ai-in-project-finance-blog/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2025/11/WhatsApp-Image-2025-11-12-at-10.20.46_ff6ffcaf.jpg)](https://financialmodelling.forvismazars.com/top-5-financial-modelling-tutorials/)

#### Our Top 5 Most-Downloaded Financial Modelling Tutorials

Explore our Top 5 financial modelling tutorials — clear, practical walkthroughs of key project finance concepts like CFADS, DSCR, LLCR...

[Read more](https://financialmodelling.forvismazars.com/top-5-financial-modelling-tutorials/)

[![Phasellus platea fames vel porttitor](https://financialmodelling.forvismazars.com/wp-content/uploads/2025/08/GettyImages-1309760275-1024x683.jpg)](https://financialmodelling.forvismazars.com/excel-copilot-function-ai-formulas/)

#### How to Use the Excel Copilot Function: AI-Powered Formulas for Smarter Data Analysis

What Is the Excel Copilot Function? The Excel Copilot function is a new AI-powered formula available in Microsoft 365. It...

[Read more](https://financialmodelling.forvismazars.com/excel-copilot-function-ai-formulas/)

*   [Legal and privacy](https://www.forvismazars.com/uk/en/contact-us/legal-and-privacy)
    

Copyright 2026 - Forvis Mazars

This website uses cookies.

Some of these cookies are necessary, while others help us analyse our traffic, serve advertising and deliver customised experiences for you. For more information on the cookies we use, please refer to our [Privacy Policy](https://financialmodelling.forvismazars.com/resources/average-dscr-in-financial-modelling#)
.

Customise Settings I Accept

*    Compulsory Cookies
    
    This website cannot function properly without these cookies.
    
*    Analytical Cookies
    
    Analytical cookies help us enhance our website by collecting information on its usage.
    
*    Marketing Cookies
    
    We use marketing cookies to increase the relevancy of our advertising campaigns.
    

### Follow us

Forvis Mazars is dedicated to exceptional financial modelling. As part of our commitment to raising the bar in financial modelling, we want to ensure the financial modelling community is kept up to date with the latest events, tips, techniques and training.

By registering for email updates from Forvis Mazars you will be kept up to date about:

*   Financial modelling events
*   New tutorials
*   The latest blog posts
*   Upcoming training courses

First name\*

Last name\*

Email ([privacy policy](http://www.corality.com/suplementary-pages/Privacy-Policy?__hstc=32075169.a5ae6dcfb5b45eeb545645f32e549665.1773830948730.1773830948730.1773830948730.1&__hssc=32075169.1.1773830948730&__hsfp=a19ed06593a6dc39eb1fdade76d7cf42)
)\*

Company

Recent Form Completion