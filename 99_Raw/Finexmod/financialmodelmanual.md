# Project Finance Manual and Databook: Is it needed? how to simplify and avoid the additional work?(Lazy Financial Modeling Techniques) – Finexmod

**Source:** https://www.finexmod.com/financialmodelmanual

---

[Skip to content](https://www.finexmod.com/financialmodelmanual#content)

Project Finance Manual and Databook: Is it needed? how to simplify and avoid the additional work?(Lazy Financial Modeling Techniques)

Sometime financial models are accompanied by two other documents:

*   Financial model Guide or manual
*   Financial model Assumption book or databook

Sometimes the guide and assumption book are combined as one.

My issue is not with the worth of these documents. I fully agree that they are quite useful.

*   the guide will show an overview of the model mechanics and functionalities and make it easier for the user to understand how to work with the model. If it is done well, a model walk-though is not even required.
*   an assumption book will present the key model assumptions and results and will make it easier to present key model information.

My issue is having this information in a separate document. I rather include it within the financial model in a dedicated sheet that I call “Guide”.

In this post, I want to take you through a typical project finance “Guide” sheet. You can download my suggested template and adopt it in your own project finance models.

**[Download Financial Model Guide Sheet for FREE](https://www.eloquens.com/tool/KybgHKNe/finance/financial-modeling-courses-tutorials/financial-model-assumption-book/?ref=FinExMod)
**

To summarize, the benefits of including a guide sheet within your financial models are:

1.  It’s going to avoid updating different documents when sending new model versions. If you or your client or colleague still insist on sending a separate documents explaining the model functionalities, then you can simply print the Guide sheet sitting within your model as PDF (lazy financial modeling techniques).
2.  it will provide comfort to users when opening the model that the model is well structured and standardized
3.  it will remind the financial modeler or anyone inheriting the model that they need to respect certain color codes and column structure when updating the model.
4.  It might help busy investment officers to quickly extract information from it and use it in their own project documents.

Just a note that you do not link and use the information in guide sheet to do any calculations. It is just for reporting purpose and if you delete the sheet Guide from the model, it should have no impact on the model.

Now let’s look at the main sections of a typical guide sheet:

1\. Model mechanics and structure
=================================

The first top section of the guide sheet should present the model functionalities and mainly the below sub sections:

1.1. Color codes used in the Model:
-----------------------------------

Explaining the color codes used in the model. Can be as simple as just mentioning the color codes used for inputs that can be changed by user of the model or can be more detailed like the below example.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-Color-codes.jpg)

1.2.Worksheet column structure:
-------------------------------

Explaining the worksheet column structure which should be harmonized across all worksheets within the model.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-column-structure.jpg)

1.3.Workbook structure:
-----------------------

listing worksheets included in the model and with a short description. Can be presented in form of a table and also a flow chart (I suggest to include both).

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-worksheet-01.jpg)

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-worksheet-02.jpg)

1.4.Operation of the model:
---------------------------

Explaining how to use and run the model. You can get some snapshot of the model and insert it as image to show which button user should press and when.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-function.jpg)

1.5.Macros:
-----------

List all macros included (Do not lock or password protect)

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-macros.jpg)

1.6.Checks:
-----------

List all check included in the model and maybe briefly explain each of them. For a complete guide on how to build error checks, check my suggested template.

[**Building Integrity Checks in Project Finance Models (Manual & Template)**](https://www.eloquens.com/tool/wmjEi0N4/finance/project-finance-models/building-integrity-checks-in-project-finance-models-manual-template?ref=FinExMod)

![](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-checks.jpg)

1.7.Abbreviations:
------------------

List all definitions and acronyms even if it seems obvious to you that CFADS stands for Cash Flow Available for Debt Service.

![](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-abbreviation.jpg)

2\. Model Key Assumptions
=========================

2.1.Timing assumptions:
-----------------------

The key base-case timing inputs summarized in a table.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-timing.jpg)

2.2.Project cost and financing plan:
------------------------------------

A summary table and pie or clustered bar chart summarizing capital expenditure during construction and basically the summary sources and uses of funds. You can combine text with links to numbers in your file to write sentence about the key financial metrics and project financial viability. You can do this by adding text inside double quotes and for numbers, I also recommend that you use the =Round() function to avoid extra digits. Here’s an example:

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-TPC.jpg)

2.3.Operating Expenses:
-----------------------

Summarizing Operating expenses mainly on annual basis. You can report the average over the life of the project or the annual Opex in the first operating year.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-Opex.jpg)

2.4.Revenues:
-------------

Report the main technical and financial assumptions behind the revenues and also report the average annual revenues.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-Revenues.jpg)

2.5.Debt assumptions:
---------------------

Summarize debt terms in a simple table.

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-Debt.jpg)

3\. Model Key Results:
======================

You should already have all the information you need in this section in your summary sheet but it’s ok, you can replicate the same here and add a sentence or two especially in the commercial viability section. This will help the user to just simply copy and paste the whole section in a document.

3.1.Commercial Feasibility:
---------------------------

You can combine text with links to numbers in your file to write sentence about the key financial metrics and project financial viability. You can do this by adding text inside double quotes and for numbers, I also recommend that you use the =Round() function to avoid extra digits. Here’s an example:

![Project Finance Spreadsheet Design and Guide sheet ](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-financial-viability.jpg)

You just need to make sure that when you are printing or sending, you are reporting the base case figures.

3.2.Sensitivity results:
------------------------

In most project documents, under the project financials, they also have a section for sensitivities. All the above sections should reflect the base case assumptions and results but then in this section, you report the key metrics under some stress cases. If you don’t have sensitivity in your financial model, then have a look at my sensitivity template. You can easily integrate it within your model and simply link the sensitivity output table here.

![Project Finance Spreadsheet Design and Guide sheet](https://www.finexmod.com/wp-content/uploads/2021/05/Guide-sensitivity.jpg)

As you can see in order to have all the above sections in your guide sheet, you need to have a structured model containing color codes, unique column structure within all worksheets, well designed Input sheets and all important financial modeling best practices. If you want to learn more about how to build a well designed and structured project finance model, check out my online course.

[![Financial Model Spreadsheet Design Course](https://www.finexmod.com/wp-content/uploads/2021/05/Course.jpg)](https://courses.finexmod.com/spreadsheet-design-course)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-05-31T09:06:24+00:00May 31st, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&t=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29 "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&text=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29 "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/financialmodelmanual/&title=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29 "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&title=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29&summary=Sometime%20financial%20models%20are%20accompanied%20by%20two%20other%20documents%3A%0D%0A%0D%0A%20%09Financial%20model%20Guide%20or%20manual%0D%0A%20%09Financial%20model%20Assumption%20book%20or%20databook%0D%0A%0D%0ASometimes%20the%20guide%20and%20assumption%20book%20are%20combined%20as%20one.%0D%0A%0D%0AMy%20issue%20is%20not%20with%20the%20worth%20of%20these "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&name=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29&description=Sometime%20financial%20models%20are%20accompanied%20by%20two%20other%20documents%3A%0D%0A%0D%0A%20%09Financial%20model%20Guide%20or%20manual%0D%0A%20%09Financial%20model%20Assumption%20book%20or%20databook%0D%0A%0D%0ASometimes%20the%20guide%20and%20assumption%20book%20are%20combined%20as%20one.%0D%0A%0D%0AMy%20issue%20is%20not%20with%20the%20worth%20of%20these%20documents.%20I%20fully%20agree%20that%20they%20are%20quite%20useful.%0D%0A%0D%0A%20%09the%20guide%20will%20show%20an%20overview%20of%20the%20model "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&description=Sometime%20financial%20models%20are%20accompanied%20by%20two%20other%20documents%3A%0D%0A%0D%0A%20%09Financial%20model%20Guide%20or%20manual%0D%0A%20%09Financial%20model%20Assumption%20book%20or%20databook%0D%0A%0D%0ASometimes%20the%20guide%20and%20assumption%20book%20are%20combined%20as%20one.%0D%0A%0D%0AMy%20issue%20is%20not%20with%20the%20worth%20of%20these%20documents.%20I%20fully%20agree%20that%20they%20are%20quite%20useful.%0D%0A%0D%0A%20%09the%20guide%20will%20show%20an%20overview%20of%20the%20model&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F05%2FGuide-Cover2.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancialmodelmanual%2F&title=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29&description=Sometime%20financial%20models%20are%20accompanied%20by%20two%20other%20documents%3A%0D%0A%0D%0A%20%09Financial%20model%20Guide%20or%20manual%0D%0A%20%09Financial%20model%20Assumption%20book%20or%20databook%0D%0A%0D%0ASometimes%20the%20guide%20and%20assumption%20book%20are%20combined%20as%20one.%0D%0A%0D%0AMy%20issue%20is%20not%20with%20the%20worth%20of%20these%20documents.%20I%20fully%20agree%20that%20they%20are%20quite%20useful.%0D%0A%0D%0A%20%09the%20guide%20will%20show%20an%20overview%20of%20the%20model "Vk")
[Email](mailto:?body=https://www.finexmod.com/financialmodelmanual/&subject=Project%20Finance%20Manual%20and%20Databook%3A%20Is%20it%20needed%3F%20how%20to%20simplify%20and%20avoid%20the%20additional%20work%3F%28Lazy%20Financial%20Modeling%20Techniques%29 "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/financialmodelmanual)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/financialmodelmanual#)

[Go to Top](https://www.finexmod.com/financialmodelmanual#)