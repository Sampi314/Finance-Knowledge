# Managing Circular References in Project Finance Models – Webinar Summary

**Source:** https://financialmodelling.forvismazars.com/managing-circular-references-blog

---

Managing Circular References in Project Finance Models – Webinar Summary
------------------------------------------------------------------------

[Forvis Mazars Financial Modelling](https://financialmodelling.forvismazars.com/)
[Blog Types](https://financialmodelling.forvismazars.com/online-resources/blog-types/)
\-[Uncategorised](https://financialmodelling.forvismazars.com/online-resources/uncategorised/)

Managing Circular References in Project Finance Models – Webinar Summary

[](http://twitter.com/share?text=Managing+Circular+References+in+Project+Finance+Models+%E2%80%93+Webinar+Summary&url=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
[](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
[](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
[](mailto:?subject=Managing%20Circular%20References%20in%20Project%20Finance%20Models%20%E2%80%93%20Webinar%20Summary&body=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)

Managing Circular References in Project Finance Models – Webinar Summary
========================================================================

By [Daniel Brooks](https://financialmodelling.forvismazars.com/author/daniel-brooks/ "Posts by Daniel Brooks")

Thursday 22nd May 2025

[![Watch full webinar here](https://no-cache.hubspot.com/cta/default/439179/interactive-190445887759.png)](https://cta-service-cms2.hubspot.com/web-interactives/public/v1/track/redirect?encryptedPayload=AVxigLIXc1pCZ%2BbvtERQ2Fd6q1ALbSRlE%2FsVE%2BWxHZTCTu6N1ZD9Gm%2BwTHKD6aksVOxA9621knUXLK3KlqR6xUBFAPKKLqDoCMcex9bGBOyADYtBko3JmiajRr20v7QvNho4r9Fmu9vpuvUdXjEsR%2FwyF%2Bf10TTmk5Iibe0xJS5kS%2F1ZMaVB01j203UUYA7aWpTKRWxDlM89IsmJTnjgNnwEE9YbvoAtDAVmIekhNIVuhA6fYhUuTRF%2BWcr4BvjLQ9g%3D&webInteractiveContentId=190445887759&portalId=439179)

**Introduction to the Webinar Series**
--------------------------------------

In a recent webinar hosted by Forvis Mazars, financial modellers were given an in-depth look at managing circular references in financial models. The session, led by [Joshua Grimm](https://www.linkedin.com/in/joshuagrimm/)
, the lead trainer for [Forvis Mazars Project Finance Modelling courses](https://financialmodelling.forvismazars.com/the-academy-financial-modelling-courses/course-portfolio/)
 in the Asia Pacific region, provided valuable insights into best practices and techniques for handling these complex issues. Circular references can often lead to errors and complexities in financial models, making it crucial for modellers to understand how to manage them effectively.

**Presenter Background**
------------------------

Joshua Grimm has extensive experience in renewable energy projects and other infrastructure assets. As an Associate Director at Forvis Mazars, he regularly encounters circular references in financial models and supports modellers in addressing these challenges—particularly through the [Advanced Project Finance Modelling course](https://financialmodelling.forvismazars.com/course-schedule/advanced-project-finance-modelling/)
. His expertise in operational modelling and project finance provided a solid foundation for the webinar.

**Key Topics Covered**
----------------------

### **Understanding the Logic of Circular References in Project Finance Models**

Circular references occur when a formula in a spreadsheet refers back to its own cell, either directly or indirectly, creating a loop. This can lead to calculation errors and make the model difficult to understand and troubleshoot. Josh highlighted common occurrences of circular references in financial models, including accidental circularities due to errors in formulae and logical circularities inherent in the model’s logic.

Josh explained, “It’s important that we understand what circular references are, where they occur, and how we can pick those up. When you see a circular reference error, don’t panic. Press OK and follow the arrows to understand how and why the circularity has occurred.”

### **Best Practices for Managing Circular References in Project Finance Models**

Josh outlined several best practices for managing circular references effectively:

*   Identify and Understand Circularities: When a circular reference error occurs, use Excel’s tracing features to follow the arrows and understand the source of the circularity.
*   Simplify Calculations: Break down complex calculations into simpler components to trace the exact point of circularity.
*   Use Algebraic Solutions: Where possible, simplify or reorder calculations to avoid circular references. This may involve back-calculating or estimating values.
*   Implement Circularity Breaks: As a last resort, use circularity breaks to separate the calculation causing the circularity from the rest of the model. This involves storing the calculated value as a hard code and using it in subsequent calculations.
*   [Use VBA Macros](https://financialmodelling.forvismazars.com/resources/copy-paste-macros-in-financial-models/)
    : For models requiring frequent updates, using VBA macros can automate the process of copying and pasting values to manage circularity breaks efficiently.

Josh emphasized, “Ultimately, if we can solve the problem algebraically, simplifying things, reordering things, back calculating, estimating, approximating, that may actually give us a better result.”

### **Managing Interest Expense Circularities – Demonstration**

Josh provided a practical demonstration of managing interest expense circularities during construction. He explained that using the closing balance to calculate interest can introduce circular references because the closing balance depends on the interest calculation itself. To avoid this, he recommended using the opening balance to calculate interest, assuming cash flows occur at the end of the period. This simplifies the calculation and avoids circular references.

He noted, “This is a commonly accepted simplifying assumption in project finance modelling. We define that cash flows occur at the very end of the period, and now we can use the opening balance to calculate our interest without introducing circularity.”

### **Summary and Implications of Circular References in Project Finance Models**

The webinar concluded with a summary of the key points discussed and a Q&A session. Josh emphasized the importance of understanding the logic behind circular calculations and using best practices to manage them effectively. He also highlighted the value of tools like VBA macros for automating the process of managing circularity breaks.

Josh concluded, “When you’re managing your circular references, definitely try to understand where the circularity is, why it’s occurring, and if it is logical. Use algebra and simplifying assumptions if appropriate, and make sure all parties involved are satisfied with the steps you are taking in the model.”

Here are five recommended tutorials that readers may also be interested in:

[Best Practice Approach to Copy-Paste Macros in Financial Models](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
: This tutorial demonstrates the best practice approach to implementing copy-paste macros and discusses potential optimizations to apply this code robustly and efficiently in different situations. It’s particularly useful for those looking to streamline their financial modelling processes using VBA macros.

[Average DSCR in Financial Modelling](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
: Learn about the two different ways to calculate the average debt service coverage ratio (ADSCR) and understand the limitations of each method. This tutorial is essential for financial modellers who need to accurately assess debt service coverage in their models.

[Cash Sweep Analysis in Project Finance](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
: This tutorial outlines the key features of a modelling cash sweep calculation and its application in analysing refinance risk and repayment ability in cash flow models for project finance. It’s a valuable resource for those involved in project finance modelling.

[Excel IRR Function and Other Ways to Calculate IRR in Excel](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
: The internal rate of return (IRR) is a common source of error in financial models. This tutorial covers how to calculate IRR in Excel, providing insights into avoiding common pitfalls and ensuring accurate calculations.

[Terminal Value in Financial Modelling](https://financialmodelling.forvismazars.com/online-resources/tutorials/)
: Terminal value accounts for a large percentage of the project value in a discounted cash flow valuation. This tutorial focuses on ways to calculate terminal value in a project finance model, making it crucial for long-term financial planning and valuation.

Related posts

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

*   [](mailto:?subject=Managing%20Circular%20References%20in%20Project%20Finance%20Models%20%E2%80%93%20Webinar%20Summary&body=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
    
*   [](https://www.linkedin.com/cws/share?url=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
    
*   [](http://twitter.com/share?text=Managing+Circular+References+in+Project+Finance+Models+%E2%80%93+Webinar+Summary&url=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
    
*   [](https://www.facebook.com/sharer/sharer.php?u=https://financialmodelling.forvismazars.com/managing-circular-references-blog/)
    

*   [Legal and privacy](https://www.forvismazars.com/uk/en/contact-us/legal-and-privacy)
    

Copyright 2026 - Forvis Mazars

This website uses cookies.

Some of these cookies are necessary, while others help us analyse our traffic, serve advertising and deliver customised experiences for you. For more information on the cookies we use, please refer to our [Privacy Policy](https://financialmodelling.forvismazars.com/managing-circular-references-blog/#)
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