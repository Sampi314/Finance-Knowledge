# Building a Layout for Project Evaluation Model & Best Practices to follow while building financial models - Download sample model layouts

**Source:** https://chandoo.org/wp/financial-model-layout-best-practices

---

Building a Layout for Project Evaluation Model & Best Practices \[Part 2 of 6\]
===============================================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 17 comments

  

_This is a guest post written by Paramdeep from [Pristine](http://edupristine.com/)
. Chandoo.org is partnering with Pristine to bring an excel financial modeling online training program for you._

### _![Building a Layout for Project Evaluation Model & Best Practices - Part 2 of 6](https://chandoo.org/img/fm/financial-model-layout-best-practices.png)This is Part 2 of 6 on Financial Modeling using Excel_

**In this tutorial we are going to learn how to build a financial model to do project evaluation using Excel.** The 6 parts of this tutorial are,

1.  [Introduction to Financial Modeling](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    
2.  **Building a layout for Project Evaluation Model – Best practices**
3.  [Building Inputs and Assumptions Sheet](http://chandoo.org/wp/2010/08/23/assumptions-financial-modeling-excel/)
    
4.  [Building Projections for Project Evaluation](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
    
5.  [Modeling the Cash Flow Statement and Projections](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
    
6.  [Putting it all together – Final Project Evaluation Model](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
    
7.  **[Join our Financial Modeling Classes](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
    **

Building a Layout for a Project Evaluation Model
------------------------------------------------

If you know basic referencing and formula framework in excel, you can write a model that calculates numbers. Good vs Bad financial model would be decided by the layout of the model.

Before we start discussing on how to build a good layout, lets see the layout that I have in mind. The layout is based on my experience of working as an investment banker and as a consultant and I find it neat.

![Building a layout for Project Evaluation Model & Best Practices](https://chandoo.org/img/fm/building-a-model-template-1.png)

![Building a layout for Project Evaluation Model - 2](https://chandoo.org/img/fm/building-a-model-template-2.png)

### What is so awesome about this model layout?

*   Structured in logical modules (Separate sections/ sheets for separate units like Assumptions, P&L, Cash, Balance Sheet, calculations and conclusion. It makes navigation and understanding very clear
*   Formatting of the sheet
    *   Inputs different from calculations (Typically you would find inputs in blue font and calculations in black)
    *   No grid lines
    *   Numbers with similar decimal points, etc.
*   Proper indenting of model with comments
*   Ease of navigation in the model

### Start building the model template

Follow these steps to create a simple layout to perform project evaluations.

1.  [Disable Grid lines for the sheets](http://chandoo.org/wp/2009/08/13/hide-grid-lines-quick-tip/)
    .
2.  Decrease the size of the first 2 columns and increase the size of the third column.
3.  Use the columns after that to set the required years.

![Building a layout for Project Evaluation Model - 3](https://chandoo.org/img/fm/building-a-model-template-3.png)

### Benefits of such a template

Since the size of columns A and B is small, if we use column A for a main heading, then we can use column B for a sub-heading. This would act as an indenting for the document (Similar to what you see in table of content in any book). This also acts as a bookmark.

Lets say, if I have 3 main headings – Assumptions, calculations and valuation, then we put them in column A and all the subheadings like, Investment assumptions, P&L Assumptions, Working Capital, Cash etc. in subheadings.

If you remember the **_Ctrl + arrow_** shortcut to navigate fast, you can use it to navigate from one section to the other in a fast manner. **_The columns act as a bookmark!_**

**_![Building a layout for Project Evaluation Model - 4](https://chandoo.org/img/fm/building-a-model-template-4.png)  
_**

The other thing to note is the **_Column mapping to the year is sacrosanct_**. For example, in my model FY 10 is aligned to column E. Now whenever anybody wants to do any calculation for FY 10, she would remember to do it in column E. If there is any mention of FY 10 in columns different from E, it raises an alarm!!

**One more trick that I generally use in the model is to freeze panes**, so that I can always see for a particular year, what is the item that I am using. (tip # 12 on [15 excel tips](http://chandoo.org/wp/2008/08/01/15-fun-things-with-excel/)
)

### Single sheet or multiple sheet model

If you are developing a mini model (Like the one we are doing here), you can use a single sheet and use the bookmarking methodology to separate the logical sections. If the information is large then one sheet might become too large. If you are using multiple sheets, then REMEMBER – always use the same template and you should maintain the matrix integrity (In our case column E corresponding to FY 10). Just copy the sheet to create other logical units. When you are using multiple sheet models, remember **Ctrl + PgUp/ PgDn is your best friend to navigate across sheets.**

**![Building a layout for Project Evaluation Model - 6](https://chandoo.org/img/fm/building-a-model-template-6.png)  
**

Best Practices While Designing Models:
--------------------------------------

_\[added by Chandoo\]_

I hate to interrupt Paramdeep’s flow. But I want to list down few best practices I have seen across various models.

*   **Keep your formats consistent**: As observed above, use one color for input cells, one color labels, one for outputs etc. Also, follow same formats  for charts and all other visual elements of your model. Consistency is very important to keep your model simple and easy to maintain. (tip: [use cell styles](http://chandoo.org/wp/2009/10/01/use-cell-styles-in-spreadsheet-models/)
    )
*   **Separate calculations from outputs:** While simple models can have all the calculations done on output sheet, ideally you should have a separate worksheet for doing all the calculations (formulas). This will make your model elegant and simple.
*   **Do not hard code values, instead use “assumptions” sheet:** If you need to use inflation rate of say 6%, never hard code that in to formulas like =A1\*(106%)^A3, instead keep all the assumptions in a separate worksheet (call it as assumptions like above) and fetch the values from that. This will help you revise your financial model easily when your assumptions change.
*   **Use named ranges:** Financial models can be quite complicated beings. A formula like =Assumptions!C23\*(1+Calculations!A21)/Inputs!B13 can be quite confusing and useless. When you need to debug or modify your model you are totally clueless as to what these references mean. Instead define names for all important values and use them in formulas.
*   **Use helper columns without shame:** While most of us would get a nice ego boost to write one big formula to solve all the problems, it may not be a nice thing to do in modeling. Instead split your problem in to small, meaningful chunks and use helper columns to solve it. This will make your model easy to maintain.
*   **Use conditional formatting to highlight relevant stuff:** If you are going to demonstrate scenarios in your model, you can use conditional formatting to highlight scenarios. You can also use CF to bring key values / areas to user’s focus. (tip: [become a conditional formatting rockstar](http://chandoo.org/wp/2008/03/13/want-to-be-an-excel-conditional-formatting-rock-star-read-this/)
    )
*   **Use data validation:** Getting invalid data in to your model can be quite frustrating. Instead of addressing invalid data thru formulas, you should try to avoid them by using data validation for input / assumption worksheets. (tip: [allow only a list of values in a cell](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/)
    )
*   **Know Excel Better:** Learn a few keyboard shortcuts, understand how features like tables, formulas & formatting work. This will save precious amount of time when you are busy modeling. (100s of tips on [keyboard shortcuts](http://chandoo.org/wp/2010/02/22/complete-list-of-excel-shortcuts/)
    , [excel tables](http://chandoo.org/wp/2009/09/10/data-tables/)
    , [formulas](http://chandoo.org/wp/tag/formulas/)
    , [charting](http://chandoo.org/wp/category/visualization/)
     & [formatting](http://chandoo.org/wp/tag/formatting/)
    )

**Most importantly,**

*   **Know your industry better:** Nothing beats industry knowledge. Even if you know nothing about excel and modeling, you can learn them easily thru sites like chandoo.org and pristine. But industry knowledge is something that is hard to pick up. Thorough understanding of your company, your market, your customers, your products and your processes is very important to define and prepare a good model.

**All the best.**

### Download Project Evaluation Model Layouts

I have created part templates and you can download the single sheet model and the multiple sheet model to take a look at it. I would suggest that you look at it and try to create a template of your own (Even if that means just trying to create an exactly same template).

[Download zip file containing the model layouts](https://img.chandoo.org/fm/ProjectEvaluation-Building-layout.zip)
 | [Download the case-study](https://img.chandoo.org/fm/financial-modeling-case.pdf)
 \[pdf\]  
[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "inancial Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### What Next?

In the next installment, we would see, how we can fill in the assumptions part of the model. It would mean reading through the case and filling in the assumptions part of the model. For maximum benefit from the series, please try to fill it on your own and fill in the other parts of the model as well.

**Read first part of this series – [Introduction to Financial Modeling](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
**

### What Best Practices & Layout ideas you follow in Modeling?

We are very eager to learn from you about ideas and best practices you follow when building financial models. **Please share using comments.**

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**

### Added by Chandoo:

**Thank you Paramdeep & Pristine:**

Many thanks to Paramdeep and Pristine for making this happen. I am really enjoying this series and learning a lot of valuable tricks about financial modeling.

**If you like this series, say thanks to Paramdeep. I am sure he can take any amount of appreciation without choking.**

### Join our Newsletter

_**If you are new here, consider [joining my newsletter](http://feedburner.google.com/fb/a/mailverify?uri=PointyHairedDilbert&loc=en_US)
**, because I can send you updates when new articles are posted (plus you get a cool e-book with 95 excel tips, FREE)_

This article is written by [Pristine](http://edupristine.com/)
. The author can be contacted on [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)
.  
_Pristine is an awesome training institute for CFA, PRIMA, GARP etc. They have trained folks at HSBC, BoA etc. Chandoo.org is partnering with Pristine to bring an excel financial modeling online training program for you._

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [cell styles](https://chandoo.org/wp/tag/cell-styles/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)<br>, [guest posts](https://chandoo.org/wp/tag/guest-posts/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [pristine](https://chandoo.org/wp/tag/pristine/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 17 Responses to “Building a Layout for Project Evaluation Model & Best Practices \[Part 2 of 6\]”

1.  ![](https://secure.gravatar.com/avatar/34c992512f60e1cad679670edaff5bc946024602f0ade25188df50d3d02b92d7?s=64&d=mm&r=g) Brian Clendinen says:
    
    [July 28, 2010 at 2:22 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-118737)
    
    I do like the bookmark tip, there are some cases where I will have more than two levels but that is a great standard to go by and it is easy to add additional cells for more levels.
    
    Separate calculations from outputs, this advice is not necessarily a good idea all the time. I admit I due get myself into trouble having input and calculation cells on the same sheet. However, this is mostly due to forgetting to lock or re-lock (when making changes) to formula cells. I somehow get a sticky finger and delete or somehow change a calculation cell and I rarely know how I did it. I just know that one month is right, the next is wrong and it was due to me changing a calculation field somehow.
    
    The reason one cannot go by this guideline often is for presentation purposes or data input reasons. It is a pain for usability to separate some data which naturally should go together. Example calculating EAC's when updating and validating if my update projections for ETC's are valid. I need calculation fields based on Actuals to date, EAC, monthly EAC variances, budget variances, and monthly variance to help sanitize ETC's people give me or I update. Seconly, from a presentation standpoint this data should be on the same sheet. The time maintaining ETC's on the separate tab which would have the exact same number of cells on the presentation sheet would just not make practical sense.
    
    So my recommendation is once you are done creating your formulas lock the cells if you are going to have input and outputs on the same tab.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-118737)
    
2.  ![](https://secure.gravatar.com/avatar/b45cfaac7191262611069d450eb0e26b44bca6ca588213c9a4a775b4b13f0b0e?s=64&d=mm&r=g) [Josh L](http://projectdashboards.com/Dashboards.html)
     says:
    
    [July 28, 2010 at 6:43 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-118767)
    
    Great stuff you guys! I love the column mapping concept; a simple but very effective approach. I also really like how you have made this series interactive: letting us work with the model and case data so we can try each step on our own before showing us how you did it.
    
    For complex models I like to build 'alarms' into the file along the way. These are simple IF formulas that return bright red "ALERT" text if selected data values or ranges don't balance. You can keep them off to the side or out of sight on the bottom. I find that reviewing your data from a different direction than what you used in your model is a good practice (e.g if your model is set up so that A + B = C then test that C - B = A, etc).
    
    You can also set up a separate worksheet that does nothing but test all of your calculations to make sure they balance and if you test each section (and subsection) of your model separately you can better isolate problems.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-118767)
    
3.  ![](https://secure.gravatar.com/avatar/ba37a8a436d481c5a1a4c0c662d56e36a217484bc76fde9d4a6b127a604dfb1b?s=64&d=mm&r=g) Henk says:
    
    [July 30, 2010 at 4:25 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-119073)
    
    Good stuff!  
    However, I agree w Brian saying that separating assumptions from calcs is not necessarily a good idea always. I try to do it as much as possible, but when you quickly need to be able to do some basic variance analysis, it might be helpful to have model and assumptions on same page. I've gotten into the habit of color coding my inputs. i.e. all inputs are blue font, calcs are just black, green are references to different sheets, and pink is special manual adjustment. I also like to use if-statements in conditional formatting to set wrong cells/formulas to red font. I just have a couple of basic fontcolor macros in my personal workbook, so I can switch font colors with shortcuts. I found this makes it really easy to audit formulas.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-119073)
    
4.  ![](https://secure.gravatar.com/avatar/34c992512f60e1cad679670edaff5bc946024602f0ade25188df50d3d02b92d7?s=64&d=mm&r=g) Brian Clendinen says:
    
    [August 2, 2010 at 5:24 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-119588)
    
    Henk,
    
    I have done some If statments with conditional formatting for audit purposes. However, the problem I ran into is I would have to recreate information because conditional formatting could not be based on others tabs. However, I just read the named ranges take care of this problem, so I will try to see if this works.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-119588)
    
5.  [12 Rules for Making Better Spreadsheets | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/08/05/better-spreadsheets-12-rules/)
     says:
    
    [August 5, 2010 at 9:19 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-120129)
    
    \[...\] Spreadsheet tips for People making Financial Models \[...\]
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-120129)
    
6.  [Building Inputs & Assumptions Sheets – Excel Financial Modeling \[Part 3 of 6\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/08/23/assumptions-financial-modeling-excel/)
     says:
    
    [September 2, 2010 at 2:49 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-125357)
    
    \[...\] Building a layout for Project Evaluation Model – Best practices \[...\]
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-125357)
    
7.  [Modeling & Building Cash-flow Projections for Project Valuation \[Part 4,5 of 6\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
     says:
    
    [September 21, 2010 at 4:54 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-128827)
    
    \[...\] Building a layout for Project Evaluation Model – Best practices \[...\]
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-128827)
    
8.  ![](https://secure.gravatar.com/avatar/12fce69e0c6fbc7df62cf00731bfef0fbcf140f6d5e71146bfdc32138e036e49?s=64&d=mm&r=g) [Paramdeep Singh](http://www.edupristine.com/)
     says:
    
    [September 22, 2010 at 1:59 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-129081)
    
    Again my apologies for the late reply on the comments!  
    @Brian, Henk: I agree, sometimes if your input data is heavy, navigating within sheets can become difficult. What I do for that is - I keep the assumptions in 1 sheet (called assumptions). If there is a need for particularly large amount of data in some other sheet (For example, if I need the revenue in P&L and it is going to take my growth assumptions for various years from assumptions sheet) I just link the assumptions in the top of revenue sheet (Just an = assumptions.revenue). This does not take too long and presentation wise its better as well.  
    @Josh: A very good practice to put your tests in the sheet. I use that very often for the basic sheets.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-129081)
    
9.  ![](https://secure.gravatar.com/avatar/ebeda0e64443deb79d351b00964423a13689ce295f918de61d720a2363e62cd1?s=64&d=mm&r=g) DARSHAN KN says:
    
    [June 26, 2011 at 7:08 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-206192)
    
    This is fantastic...
    
    Thank you so much
    
    DKN
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-206192)
    
10.  [Final Valuation of the Project - Financial Modeling using Excel - Part 6 | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
     says:
    
    [July 28, 2011 at 5:17 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-207622)
    
    \[...\] Building a layout for Project Evaluation Model – Best practices \[...\]
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-207622)
    
11.  [FREE Excel Financial Model for Analyzing an IPO – Download Today | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/10/22/download-free-excel-financial-model/)
     says:
    
    [July 28, 2011 at 5:33 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-207628)
    
    \[...\] Building a layout for Project Evaluation Model – Best practices \[...\]
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-207628)
    
12.  ![](https://secure.gravatar.com/avatar/505fde894e34c337b576ab941cce2fd179e87d05c39f6a9c1a9593e4c1527222?s=64&d=mm&r=g) ARUN says:
    
    [September 21, 2011 at 6:28 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-208951)
    
    Hi,
    
    Just want to know the online classes can be download and saved in my sytem.
    
    Pls advice.
    
    Regards,  
    Arun
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-208951)
    
    *   ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) [paramdeep@gmail.com](http://www.edupristine.com/)
         says:
        
        [September 14, 2012 at 4:09 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239769)
        
        Hi Arun,
        
        Yes the online classes (video tutorials) and the excel models can be downloaded and saved in your system.
        
        [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239769)
        
13.  ![](https://secure.gravatar.com/avatar/03355977f324328c21cd248d7d231df27379a11e7acb266f88253a836885bff7?s=64&d=mm&r=g) vimal says:
    
    [July 30, 2012 at 7:22 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-227984)
    
    i will accounting make to party bill name, address, in excel in formating
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-227984)
    
14.  ![](https://secure.gravatar.com/avatar/b389f5e73fd7b6503f0cca13bd5efceafadd3d8c813867c856d5650f68e4ed8b?s=64&d=mm&r=g) dikshita says:
    
    [September 13, 2012 at 10:09 pm](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239590)
    
    hie ppl…I jst wantd a small favour cn smone help me out in calculating **EBITDA**, along with its working,  **from wipros annual report** 2011-2012, link –   [http://www.wipro.com/investors/annual-reports.aspx](http://www.wipro.com/investors/annual-reports.aspx)
      
    …PLZ plz… i am having a submission tommorow.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239590)
    
    *   ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) [paramdeep@gmail.com](http://www.edupristine.com/)
         says:
        
        [September 14, 2012 at 4:12 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239771)
        
        If you send the excel sheet in the same format with historical statements put in the same, I can help you with calculating the EBITDA.
        
        [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-239771)
        
15.  ![](https://secure.gravatar.com/avatar/9d29c4e5b412c52f65bfbc811cab70168dbcd89647e841bb36d66b2265df8956?s=64&d=mm&r=g) Vuyani says:
    
    [September 23, 2015 at 7:04 am](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-1049954)
    
    Hi all,
    
    Has anyone done any financial modelling of cross-border real estate acquisitions? I am just battling with incorporating currency movements into my model.
    
    [Reply](https://chandoo.org/wp/financial-model-layout-best-practices/#comment-1049954)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/financial-model-layout-best-practices/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to show Indian Currency Format in Excel?](https://chandoo.org/wp/indian-currency-format-excel/) | [Introducing Excel Wedding Planner](https://chandoo.org/wp/introducing-excel-wedding-planner/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)