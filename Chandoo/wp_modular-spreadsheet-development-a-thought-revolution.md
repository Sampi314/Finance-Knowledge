# Modular Spreadsheet Development – A Thought Revolution » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution

---

Modular Spreadsheet Development – A Thought Revolution
======================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 24 comments

  

_This article is written by Michael Hutchens from [Best Practice Modelling](http://www.bestpracticemodelling.com/)
._

This article provides a high level overview of Modular Spreadsheet Development principles. In next part the implementation of these concepts will be discussed.

### Modular Spreadsheet Development – An awesome concept

I want to share a concept with you so awesome that once you understand it you may never use Excel the same way again.

This concept, called _Modular Spreadsheet Development_, makes it possible **to build spreadsheets exponentially faster while reducing the risk of errors and making spreadsheets much easier to understand**.

This concept is not completely new, but I’m writing this article because the spreadsheet modelling world would be a much better place if it was more commonly adopted.

### An idea born through necessity

It took me three months to build my first model after I became a professional financial modeller in 2002. It was a model of a large energy company, and it’s safe to say I didn’t get a lot of sleep during that three month period.

The second model I built was of a water company, and I realized that although it was a different business, large parts of the model required the exact same logic as my energy company model. So instead of starting from scratch, I created a copy of my energy model, deleted the parts that didn’t apply to my water company, and instantly had over half my water company model built within a day.

The third model I built was of a toll road company, and once again I realized that the majority of the model required identical logic to parts of my energy and water models. This process was more complicated, because I had to copy, cut and paste pieces out of both of my prior models, but compared to building from scratch it was relatively easily. And I got a lot of sleep.

### Never repeat yourself

Within one year of starting my financial modelling business I had already developed an obsession with efficiency. It just seemed insane to spend days and nights repeating tasks that I’d done the last time I’d built a model. Two things had become clear:

1.  Templates don’t work; and
2.  Large parts of many models are identical to parts of other models that you or someone else has built previously.

So my obsession turned to finding a way to re-use and share _parts_ of models, so that I could build more models quickly and easily instead of re-inventing the wheel each time.

### Re-using and sharing ‘modules’

The answer fell into my lap one day in 2005 thanks to a hero-worthy depreciation formula written by one of my colleagues. The formula was much shorter than any depreciation calculation I’d ever seen before, and I immediately wanted to use it in every financial model I built from that day on.

I asked my colleague to strip everything out of his model except for the depreciation parts, leaving only two sheets containing depreciation assumptions and outputs respectively. He obliged, and soon-after sent me an email with his _fixed assets module_ attached. In diagrammatic form, it looked something like this:

![fixed_assets_module - Modular Spreadsheet Development](https://chandoo.org/wp/wp-content/uploads/2014/05/fixed_assets_module.png)

This was a revolution for everyone in our firm. We never needed to model depreciation from scratch again. And we knew the calculations were correct so there was minimal risk of errors each time we re-used the module.

We immediately recognized that through compartmentalizing complexity into _modules_, we could re-use and share content when building models like Legopieces. We started building models in a fraction of our prior model development times.

### Modules, modules, modules

It’s safe to say that I’ve become obsessed with building, re-using and sharing modules. Whether it’s a _valuation module_, a _dashboard module_ or an _income statement module_, each one feels like an app I’ve developed for an App Store, and I always take great pride in sharing my most impressive modules with anyone who’s interested in using them.

My colleagues have also become obsessed with modules, and between us we’ve developed over 3,000 of them over the past 9 years, allowing for different time frames and levels of sophistication. Here’s an example of just a few of the _revenue modules_ we’ve built and use all the time:

*   Revenue (Amounts)
*   Revenue (Amount & Growth Rates)
*   Revenue (Amounts & Growth Rates)
*   Revenue (Prices × Volumes)
*   Revenue (Real & Nominal Outputs)

It’s a whole new mentality, because each time we build a module we’re aware that it will most likely be re-used indefinitely, so we obsess about making sure it is as perfect as possible.

### Infinite potential

One of the awesome things about Modular Spreadsheet Development is that it creates seemingly infinite opportunities to improve the way spreadsheets are built, used, shared and communicated.

The modules within a spreadsheet can be grouped into _module areas_, such that diagrams can be used to communicate the content of a model, as show below for a basic profitability model:

![profitability_model_modules - Modular Spreadsheet Development](https://chandoo.org/wp/wp-content/uploads/2014/05/profitability_model_modules.png)

Relationships between modules can be shown using _module links diagrams_, as shown below for a basic income statement module:

![Basic Income Statement Module - Modular Spreadsheet Development](https://chandoo.org/wp/wp-content/uploads/2014/05/income_statement_module_links.png)

Furthermore, every element of the modelling process can be systematized based on a modular approach. Our firm now scopes and builds all models on a _module-by-module_ approach, often working in teams by allocating different modules to different team members.

We also train and assess staff making sure they understand each module so that they can then use different combinations of modules on different projects without ever re-inventing the wheel.

### Basic example

The following Excel workbooks provide a basic example of the implementation of Modular Spreadsheet Development, in this case to forecast earnings over a five year period. The first workbook contains revenue, expenses, income statement and dashboard summary modules sourced from the subsequent four workbooks respectively, which each contain a single module:

*   [Modular Spreadsheet Development – Basic Example.xlsb](https://img.chandoo.org/fm/Modular%20Spreadsheet%20Development%20-%20Basic%20Example.xlsb)
    
*   [Revenue Module (Amount & Growth Rates).xlsb](https://img.chandoo.org/fm/Revenue%20Module%20%28Amount%20%26%20Growth%20Rates%29.xlsb)
    
*   [Expenses Module (Amount & Growth Rates).xlsb](https://img.chandoo.org/fm/Expenses%20Module%20%28Amount%20%26%20Growth%20Rates%29.xlsb)
    
*   [Income Statement Module.xlsb](https://img.chandoo.org/fm/Income%20Statement%20Module.xlsb)
    
*   [Dashboard Summary Module.xlsb](https://img.chandoo.org/fm/Dashboard%20Summary%20Module.xlsb)
    

Each of these modules could be exchanged with other modules to change the model functionality. For example, the _Revenue (Amount & Growth Rates)_ module might be exchanged with a _Revenue (Drivers)_ module to base the revenue forecasts on prices and volumes rather than growth rates. And this could be done without affecting the integrity of the other modules in the workbook.

This process will be discussed in more detail in the second part of this series.

### More information

I truly believe that the spreadsheet modelling world should be creating and sharing modules like free apps in an App Store. We’d all save time, build better models, reduce spreadsheet errors, and help maintain and improve Microsoft Excel’s reputation as the world’s leading analytical tool.

I have created an 83 second movie explaining Modular Spreadsheet Development, which you can access via the following link:

[http://www.bestpracticemodelling.com/chandoo/msd](http://www.bestpracticemodelling.com/chandoo/msd)

You can also download the following PDF document:

[Modular Spreadsheet Development – Fundamentals](https://chandoo.org/wp/wp-content/uploads/2014/05/Modular-Spreadsheet-Development.pdf)

### Added by Chandoo

Modular development is not a new concept. In software industry, modular development is one of the first things you learn. Even those of you who are using Excel alone, have relied on modules all the time, in the disguise of VBA functions, add-ins, classes etc.

But this is the first time, I am seeing modular development applied to spreadsheet models. I am excited to try these concepts when developing dashboards or models.

**What about you?** Have you heard about MSD? Did you come across any models developed with these concepts? **Please share your thoughts and concerns using comments.**

### More on Modeling Best Practices:

*   [Best Practice Modeling – 5 changes to implement today](http://chandoo.org/wp/2012/08/29/best-practice-modeling-5tips/)
    
*   [Project Finance Modeling using Excel – Part 1](http://chandoo.org/wp/2011/02/08/introduction-to-project-finance-modeling-in-excel/)
     & [Part 2](http://chandoo.org/wp/2011/02/16/modeling-interest-during-construction/)
    
*   [Financial Modeling using Excel – Part 1](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    , [Part 2](http://chandoo.org/wp/2010/07/28/financial-model-layout-best-practices/)
    , [Part 3](http://chandoo.org/wp/2010/08/23/assumptions-financial-modeling-excel/)
    , [Part 4, Part 5](http://chandoo.org/wp/2010/09/02/modeling-cashflow-projections-for-project-evaluation/)
     & [Part 6](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
    
*   [Spreadsheet Risk Management Part 1](http://chandoo.org/wp/2011/12/07/spreadsheet-risk-management-introduction/)
    , [Part 2](http://chandoo.org/wp/2012/01/03/how-companies-can-manage-spreadsheet-risk/)
    , [Part 3](http://chandoo.org/wp/2012/01/18/excel-auditing-functions/)
     & [Part 4](http://chandoo.org/wp/2012/02/08/spreadsheet-risk-management-software-review/)
    

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
| Written by Chandoo  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)<br>, [guest posts](https://chandoo.org/wp/tag/guest-posts/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [modeling](https://chandoo.org/wp/tag/modeling/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 24 Responses to “Modular Spreadsheet Development – A Thought Revolution”

1.  ![](https://secure.gravatar.com/avatar/dc6e6252fafab631d9523afa92dc63a01062fa7ffd7095af17e0c76a101b132d?s=64&d=mm&r=g) Robert Clark says:
    
    [May 7, 2014 at 8:18 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521458)
    
    Example links aren't working 🙁
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521458)
    
    *   ![](https://secure.gravatar.com/avatar/99d7e6f62a4460c281eeddad2e7d08fcdf1668b259b06b5d3f0580ad97866b08?s=64&d=mm&r=g) [Chris Macro](http://www.thespreadsheetguru.com/)
         says:
        
        [May 7, 2014 at 12:27 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521915)
        
        Yep, definitely getting that dreaded #VALUE! error 🙁
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521915)
        
2.  ![](https://secure.gravatar.com/avatar/5a71b84433b6ada5d601c3907f7ab431eb31c2730aa95ff83aa10fda814a8654?s=64&d=mm&r=g) shah says:
    
    [May 7, 2014 at 8:45 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521505)
    
    same issue... download link not working.
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521505)
    
3.  ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra says:
    
    [May 7, 2014 at 11:17 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521804)
    
    Yeah Chandoo, I have heard about MSD...Mahendra Singh Dhoni...
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521804)
    
4.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [May 7, 2014 at 12:52 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521954)
    
    @All.. sorry for the error in download links. They are fixed now. You can click them or use below.
    
    *   [Modular Spreadsheet Development - Basic Example.xlsb](http://img.chandoo.org/fm/Modular%20Spreadsheet%20Development%20-%20Basic%20Example.xlsb)
        
    *   [Revenue Module (Amount & Growth Rates).xlsb](http://img.chandoo.org/fm/Revenue%20Module%20%28Amount%20%26%20Growth%20Rates%29.xlsb)
        
    *   [Expenses Module (Amount & Growth Rates).xlsb](http://img.chandoo.org/fm/Expenses%20Module%20%28Amount%20%26%20Growth%20Rates%29.xlsb)
        
    *   [Income Statement Module.xlsb](http://img.chandoo.org/fm/Income%20Statement%20Module.xlsb)
        
    *   [Dashboard Summary Module.xlsb](http://img.chandoo.org/fm/Dashboard%20Summary%20Module.xlsb)
        
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-521954)
    
5.  ![](https://secure.gravatar.com/avatar/b3eb321598582d1fac12513004a952417768768488b083179287a77e1b544217?s=64&d=mm&r=g) karthiganesh says:
    
    [May 7, 2014 at 5:13 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522338)
    
    Hi Chandoo,
    
    Now I realize, I started using this modular approach in LOTUS 123, later QuatroPro. Till reading this article, I do not realize that I used very long back.
    
    In Lotus 123, I prepared a 'Production Plan' for our Yarn factory for one set of raw material combination (which took 7 days). When they changed the raw material combination, I reworked but in less time (which took 5 days). Later I designed worksheet, where entering raw material combination will generate 'Production Plan'.
    
    Was it Modular Spreadsheet Development ??
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522338)
    
6.  ![](https://secure.gravatar.com/avatar/f90842623f4accc68bec5a4810a2e9fd703d0850f841c763d9e53942f24342b8?s=64&d=mm&r=g) Rob says:
    
    [May 7, 2014 at 6:23 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522457)
    
    There is a software package in the UK called Brixx that uses this principle. The problem I tend to find with 'MSD' is that business plans start to sprawl as they become more complex. Also, calculating something in isolation then consolidating with other modules always worries me...(I'm a pessimist)
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522457)
    
    *   ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
         says:
        
        [May 8, 2014 at 2:14 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523256)
        
        Hi Rob. I just checked out Brixx. It's definitely a similar concept, although it's quite a leap from good old Microsoft Excel. I will be explaining the practical implementation of MSD in Excel in my follow-up article, so perhaps I can meter some of that pessimism!
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523256)
        
7.  ![](https://secure.gravatar.com/avatar/26958bb1d88ac804797e8a5976365de5ea8c947c46303731234a2c11f72f7d96?s=64&d=mm&r=g) Robjowens says:
    
    [May 7, 2014 at 6:24 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522460)
    
    There is a software package in the UK called Brixx that uses this principle. The problem I tend to find with 'MSD' is that business plans start to sprawl as they become more complex. Also, calculating something in isolation then consolidating with other modules always worries me...(I'm a pessimist)
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522460)
    
    *   ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
         says:
        
        [May 16, 2014 at 1:42 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-533954)
        
        Hi Rob
        
        I too was pessimistic, but the efficiency gains our organisation have achieved since adopting MSD have been quite staggering.
        
        The key to MSD is very clearly understanding how a model can best be broken up into re-usable and exchangeable pieces (modules) before diving into the build process.
        
        We found that, within a particular field (which for us is financial modelling and business planning) there is a great deal of module re-use, with obvious examples being assets depreciation, working capital analysis, financial statements and DCF valuations.
        
        In fact, we've uploaded over 1,500 of these modules to our website for free download (see [http://www.bestpracticemodelling.com/downloads/modules](http://www.bestpracticemodelling.com/downloads/modules)
        ) if you want to check them out.
        
        I will discuss more details about the implementation of MSD in my follow-up article, which Chandoo should be posting over the next few days.
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-533954)
        
8.  ![](https://secure.gravatar.com/avatar/32e805a099bbb9bb8e918f3d8939e887399ac6347e1ee1bb89bb226f10c8d7ec?s=64&d=mm&r=g) Ryan Shoemaker says:
    
    [May 7, 2014 at 7:58 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522616)
    
    If you are not familiar with BPM Toolbox, this is the Excel add-in being used to build these example models above.
    
    I have been a user for a couple years now. This product have saved countless hours in developing financial valuation, capital project and other models.
    
    Highly recommend.
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522616)
    
    *   ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
         says:
        
        [May 8, 2014 at 2:28 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523280)
        
        Thanks Ryan. The Standards and bpmToolbox played a massive role in creating the consistency that made MSD so obvious.
        
        I think one of the reasons why MSD is not yet widely used is because standardization isn't respected enough for MSD to become more prominent.
        
        My primary objectives are efficiency improvements and risk mitigation, and all of these systems fundamentally assist in achieving these objectives.
        
        It's always great when others 'get it', and I think it's only a matter of time before all of this becomes an expectation in organizations wanting to better use spreadsheets.
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523280)
        
9.  ![](https://secure.gravatar.com/avatar/3246b05c841b6205bc01eb88325e954ceb35c7912eaccb2736aec8e1b4f4debe?s=64&d=mm&r=g) Shireesha says:
    
    [May 7, 2014 at 8:49 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522698)
    
    Fantastic approach, to tidy up messy messy world of spreadsheet models. Very well documented and explained.
    
    Awesome work! Thanks.
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-522698)
    
    *   ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
         says:
        
        [May 8, 2014 at 2:16 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523259)
        
        Thanks Shiressha. Stay posted for the follow-up article. It only gets better!
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523259)
        
10.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) duncan says:
    
    [May 8, 2014 at 7:46 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523992)
    
    xlsb links still dead
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-523992)
    
11.  [Modular Spreadsheet Development - All Things Data & Excel in Chicago | DataScopic](http://datascopic.net/modular-spreadsheet-development/)
     says:
    
    [May 9, 2014 at 1:38 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-527967)
    
    \[…\] recently posted about Modular Spreadsheet Development (MDS). Like it was for him, this is a new concept for me but it made \[…\]
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-527967)
    
12.  ![](https://secure.gravatar.com/avatar/ed6626920e7ce4d67d2b1f5a487a152795e63eb3914b3dcc79456d9f7d9e433d?s=64&d=mm&r=g) Ashraf A. says:
    
    [May 10, 2014 at 11:24 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-528644)
    
    That awful moment when an undetected error somewhere in your model generates misleading output for your client?
    
    ...that awful moment when it takes hours to trace back the source of that error?
    
    ...that awful moment when you have missed the deadline and cannot still see the end in sight?
    
    These are 3 classic challenges that people in modelling face but MSD is definately a concept and mindset that can signifiantly cure the above issues.
    
    Thanks for sharing @Michael.
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-528644)
    
13.  ![](https://secure.gravatar.com/avatar/dbb84834dcdad98e0dbf48eab594be6a2ff52614f5d12b6946402a3b43bb60be?s=64&d=mm&r=g) dany says:
    
    [May 11, 2014 at 2:01 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529371)
    
    Good concept.  
    Instead of one big template...there is a split of it to modules or pillars..which are eventually templates by themselfs...and you choose which to use...  
    Might work....for something which is regural and rutine...but for new projects probablly building new template might be a better solution.  
    Another point..these days..business partners dont have time and want to see excells asap...directly and even to change some numbers..not sure if too many sheets will help with this challenge..
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529371)
    
14.  ![](https://secure.gravatar.com/avatar/7a1eda400b20ef97bc99663c26b1b936db64a6cdebc708d0516ba27ea9538a06?s=64&d=mm&r=g) Hamish says:
    
    [May 12, 2014 at 12:25 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529626)
    
    How do you make the hyperlink buttons?
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529626)
    
15.  ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
     says:
    
    [May 12, 2014 at 1:29 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529647)
    
    Hi Hamish.
    
    The 'hyperlink buttons' are actually shapes (inserted via the Insert tab, Shapes menu) with their Fill property set to 'No fill' and a hyperlink added to them by right-clicking on them and selecting the Hyperlink menu item from the displayed shortcut menu.
    
    Let me know if this doesn't make sense and I will provide more detailed instructions.
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529647)
    
    *   ![](https://secure.gravatar.com/avatar/7a1eda400b20ef97bc99663c26b1b936db64a6cdebc708d0516ba27ea9538a06?s=64&d=mm&r=g) Hamish says:
        
        [May 12, 2014 at 1:41 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529653)
        
        Thanks Michael. Much Appreciated 🙂
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529653)
        
16.  [Excel Roundup 20140512 | Contextures Blog](http://blog.contextures.com/archives/2014/05/12/excel-roundup-20140512/)
     says:
    
    [May 12, 2014 at 4:02 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529727)
    
    \[…\] Instead of starting from scratch every time you build a new workbook, you can save time with modular spreadsheet development. \[…\]
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-529727)
    
17.  ![](https://secure.gravatar.com/avatar/17823aee8678ad68c53f08f8914813c88ed71c9b6c8609dd5f803c58cb5353ce?s=64&d=mm&r=g) Fernando says:
    
    [May 16, 2014 at 12:33 pm](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-533904)
    
    Hi Michael,
    
    I understand how valuable an MSD approach can be when designing financial and risk models. Nonetheless, I believe a big part of Excel users do a lot of ad hoc reports, work with very different data basis and do adhoc reports that then become standard reports. The way I've found to become more efficient has been with macros and pivot tables.
    
    I would like to get your thoughts on MSD beyond designing financial and risk models.
    
    Thanks Michael!
    
    [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-533904)
    
    *   ![](https://secure.gravatar.com/avatar/4003999b0ee59fcce46a4b94e68b29969108bad749de209f168a6f1b94947a80?s=64&d=mm&r=g) [Michael Hutchens](http://www.bestpracticemodelling.com/)
         says:
        
        [May 19, 2014 at 12:44 am](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-536336)
        
        Hi Fernando
        
        The applicability of MSD, and the efficiency gains flowing from its implementation, are often directly related to the level of standardization present within the underlying subject matter.
        
        Financial modeling is obviously ripe for MSD because it is heavily governed by international accounting standards which create a foundation for the consistent creation of modules - e.g. financial statements, etc.
        
        For more ad hoc reports, I still see great benefits in spreadsheet standardization, but the applicability of MSD really depends on (1) whether it is likely that you or someone else has undertaken a similar analysis before and (2) whether the analysis can be divided up into smaller pieces (i.e. modules) rather than simply using templates.
        
        All things aside, MSD is certainly not appropriate for all spreadsheet modelling projects, but it certainly can be used for a lot of them. Particularly if you are a regular user of Excel undertaking similar types of analysis in different spreadsheets.
        
        I provide more practical depth on MSD in my follow-up article so please stay tuned.
        
        [Reply](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#comment-536336)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/modular-spreadsheet-development-a-thought-revolution/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Create a line chart with bands \[tutorial\]](https://chandoo.org/wp/line-chart-with-bands-excel-tutorial/) | [Building a simple timer using Excel VBA to track my Rubik’s cube solving speed \[case study\]](https://chandoo.org/wp/building-a-simple-timer-using-excel-vba-to-track-my-rubiks-cube-solving-speed-case-study/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)