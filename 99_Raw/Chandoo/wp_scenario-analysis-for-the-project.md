# Scenario Analysis for the Project Valuation [Financial Modeling] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/scenario-analysis-for-the-project

---

Scenario Analysis for the Project Valuation \[Financial Modeling\]
==================================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 10 comments

  

Few months ago, we learned how to [create a project valuation model in Excel](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
 as part of our series on [Financial Modeling in Excel](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
.

My Project Evaluation Model had a limitation!! In one of the personal comments that I received, the reader pointed out an important problem!

[![clip_image002](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image002_thumb.jpg "clip_image002")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image002.jpg)

[![clip_image004](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image004_thumb.jpg "clip_image004")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image004.jpg)

If you remember, when I had started writing on chandoo’s blog, I had written a [series of blog posts on project evaluation](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
. We had created this simple [Integrated Financial Model in Excel](http://chandoo.org/wp/2010/09/21/project-valuation-model-in-excel/)
 to the model for analysis.

In any real life project the decision makers are not satisfied with a single point analysis. In any meaningful decision making process, the decision maker wants to see the impact of change in the assumption.

*   What if – The assumption that I had made is not true?
*   What if – The starting revenues are not USD 250 Mio, but instead are just 200 Mio (Pessimistic Scenario)? What if they become 300 Mio (Optimistic Scenario)?
*   What if – To reduce risk, I make an initial investment of USD 300 Mio and the starting revenue is just USD 120 Mio? Would the project make sense?

Managers always demand a lot of data for analysis and analysts always find this a pain!! To remove (Rather reduce) the pain, **Excel provides you its own analyst – Data Tables**!

### **What are Data Tables?**

Hui and Chandoo have been speaking a lot about the data tables. They are your best friends when it comes to doing the donkey work about changing the variables and noting the scenario results. One post that [I love is here](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)
.

Just like Hui has pointed out, Data tables provide you a platform to vary two assumption variables (max) and see what your result variables are going to be!

Our reader pointed out the same question! If my revenues were not 300, what would happen to my output variable (IRR or NPV)? I told him exactly what Hui told you guys – Use Data Tables!

### **How to Use Data Tables in Your Project Evaluation Model?**

[Using Data tables](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)
 in your models is pretty simple. I am listing the steps. \[[More on data tables](http://chandoo.org/wp/2011/06/20/analyse-data-like-a-super-hero/)\
\]

0) Create a completely linked and correct model! **(A must!).** You can [download one from here](https://img.chandoo.org/d/ProjectEvaluation-Valuation-Solution-Key.xls)

1) Create the structure of the what-if analysis. If you want to vary one input variable, put it in row/ column, if you want to vary two, create a 2-D structure

a. One Variable Analysis

[![clip_image006](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image006_thumb.jpg "clip_image006")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image006.jpg)

b. Two Variable Analysis

[![clip_image008](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image008_thumb.jpg "clip_image008")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image008.jpg)

### Remember to Use constants as the changing scenarios! Never link them as formulas

2) Once we have the structure in place, link the cell on top of a 1-D array and in the intersection of the 2-D array to the variable that you want to observe (In our case NPV value)

[![clip_image010](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image010_thumb.jpg "clip_image010")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image010.jpg)

[![clip_image012](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image012_thumb.jpg "clip_image012")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image012.jpg)

3) Once you have linked to the variable, select the complete table and go to data **What if Analysis** Data Tables

[![clip_image014](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image014_thumb.jpg "clip_image014")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image014.jpg)

[![clip_image016](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image016_thumb.jpg "clip_image016")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image016.jpg)

4) Since the data is in column format, in the column input cell, link to the initial constant expectation of revenue. If it is 2-D, link to both the column and row

[![clip_image018](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image018_thumb.jpg "clip_image018")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image018.jpg)

[![clip_image020](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image020_thumb.jpg "clip_image020")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image020.jpg)

5) That’s it – All the analysis is done!

[![clip_image022](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image022_thumb.jpg "clip_image022")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image022.jpg)

[![clip_image024](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image024_thumb.jpg "clip_image024")](https://chandoo.org/wp/wp-content/uploads/2011/07/clip_image024.jpg)

6) So if my initial revenue was 200, I would be making a huge loss in the project. Similarly if the initial revenue is 250 but the growth remains curtailed to 5%, the project would still make a –ve NPV.

### **Beware!!**

The basic assumption before starting the scenario analysis was complete linking and correctness of model. In one of the consulting assignments that we worked on, we got a model that was not correctly linked and the client wanted scenario analysis. That is not going to happen!

In the different scenarios make sure that you use constants as your changing inputs. For example, if the revenue is varying from 200 – 220 – 240 – 260, then you should put them as constants and NOT as 200, and then an increment of 20 on the initial value!

### **Limitations**

Since MS Excel has a 2-D structure, so Excel Data Tables can vary 2 inputs at a time. If you want to see effect of more than 2 variables, then Data Tables would not work. You need to use scenario manager or Macros to overcome the limitation.

Each time you update your sheet, all the data tables get updated (Each cell). If your model is a large one, it can considerably slow down your sheet.

### **How do you generate scenarios in your models?**

Do you generate scenarios for your models? I am sure you would be. If you are not, then you should!

If you are already doing it, then how do you do it? Do you use data tables/ macros/ scenario manager? Share your experience!

### Templates to download

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers! You can [download the same from here](https://chandoo.org/wp/wp-content/uploads/2011/07/ProjectEvaluation-Scenario-DataTables-Par.xlsx)
**.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, [matches mine or not](https://chandoo.org/wp/wp-content/uploads/2011/07/ProjectEvaluation-Scenario-DataTables-Ins.xlsx)
!

I am just doing that for the single sheet model and recommend that you do the same for multi-sheet model as a homework problem. If you face any issue, post your excel with the exact problem and we can discuss the way to move forward.  
[![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine")

### **Next Steps**

Here we made the assumption that variables are known. What if the input variables were themselves flowing from some distribution, instead of deterministically known inputs! Then the scenarios could be large in number and you might be required to do an advanced technique like Monte Carlo Simulation! I do hope that you found the posts interesting and look forward to your comments and suggestions!

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration.

**[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
**

For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

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
| Written by paramdeep@gmail.com  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [data tables](https://chandoo.org/wp/tag/data-tables/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Evaluate](https://chandoo.org/wp/tag/evaluate/)<br>, [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)<br>, [hui](https://chandoo.org/wp/tag/hui/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [monte carlo simulations](https://chandoo.org/wp/tag/monte-carlo-simulations/)<br>, [project finance](https://chandoo.org/wp/tag/project-finance/)<br>, [project management](https://chandoo.org/wp/tag/project-management/)<br>, [scenarios](https://chandoo.org/wp/tag/scenarios/)<br>, [simulation](https://chandoo.org/wp/tag/simulation/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 10 Responses to “Scenario Analysis for the Project Valuation \[Financial Modeling\]”

1.  ![](https://secure.gravatar.com/avatar/c4c35ede91d84d5bc19462e78f1415eaabaf6a168f074a73a249d7a7bb68b76f?s=64&d=mm&r=g) Ashish says:
    
    [July 26, 2011 at 9:07 am](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207580)
    
    You could also use Spin Buttons from the Developer ribbon to create scenarios efficiently. Spin Buttons, when linked to cells, allow the target cell to be changed by a pre-decided amount (increased or decreased). Like you said, if the model is formula based and linked properly, this works as well.
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207580)
    
2.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) paramdeep@gmail.com says:
    
    [July 26, 2011 at 10:52 am](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207582)
    
    @Ashish: That is right. But if you want to see all the scenarios at the same point of time, then the spin buttons might not be helpful.
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207582)
    
3.  ![](https://secure.gravatar.com/avatar/3e1943bb07f6b979e2dc599612814f06a4c4c3a07c6090f888a914e4fa0ba645?s=64&d=mm&r=g) Pankaj says:
    
    [July 26, 2011 at 6:41 pm](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207595)
    
    I have used database functions to do scenario management. For my purpose I wanted average, count and standard deviation. Here is the link to the file that can dynamically change the scenario considering upto 7 dimensions. No macros.
    
    [http://pankaj.dishapankaj.com/share](http://pankaj.dishapankaj.com/share)
    
    Explore the file. Since I work in obesity space, the file is built to display weight loss for individuals/groups. the data in this file is simulated data based on averages and standard deviations for the groups. I am hoping to write a post regarding it soon. I am sure this can be applied to financial models as well or for that matter many other situations.
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207595)
    
4.  ![](https://secure.gravatar.com/avatar/3e1943bb07f6b979e2dc599612814f06a4c4c3a07c6090f888a914e4fa0ba645?s=64&d=mm&r=g) Pankaj says:
    
    [July 26, 2011 at 6:44 pm](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207596)
    
    Its obvious but I forgot to mention the filename is 'USE\_of\_Excel\_as\_database20110622.xls'
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207596)
    
5.  ![](https://secure.gravatar.com/avatar/fcf20e8474729e01fbf14e7156860d78dc15dde01e5fbd59ac2ad3a46d6fa5e2?s=64&d=mm&r=g) Peter Thomsen says:
    
    [August 8, 2011 at 8:19 am](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207813)
    
    Long time ago I was teaching a course on financial modelling in Excel.
    
    As far as I remember the students had an assignment what-if with more than two variables. I think it was handled by using a list with the scenarioes and reference the scenarioes with the lookup function.  
    That way you only need one value in order to change multiple values in your analysis.
    
    Peter Thomsen
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207813)
    
6.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) paramdeep@gmail.com says:
    
    [August 8, 2011 at 10:30 am](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207823)
    
    @Peter: Yes, you can do that. But it would also show the impact of only 2 input variables on the output variable at one point of time. If I want to change more than 2 variables (simultaneously) and see the impact, the excel data tables cannot be used.
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-207823)
    
7.  [Learn Any Area of Excel using these 80 Links | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2011/12/12/learn-excel-by-topic/)
     says:
    
    [December 12, 2011 at 9:01 am](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-216200)
    
    \[...\] Scenario Analysis for a Project \[...\]
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-216200)
    
8.  ![](https://secure.gravatar.com/avatar/84514bc4a819a3aa154f742ff0eab0d723f1abc4310c60f461776706b6748a51?s=64&d=mm&r=g) Emma Tameside says:
    
    [August 3, 2012 at 12:59 pm](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-228276)
    
    Multi-point modelling analysis is the bane of my life! I've never really got my head around the advanced functions of Excel to model these scenarios for me, so I always end up with multiple worksheets that all need updating when the fundamentals change! This article should help me immensely if I can find the time to really learn it all.  
       
    This is what we are taught during our [CFA](http://financial.kaplan.co.uk/trainingandquals/internationalstudents/professional-qualifications/cfa-chartered-financial-analyst/pages/default.aspx)
     training, but that kind of ends at using pivot tables 🙂  
       
    Just one question, are there are readable formats for 3 or more data variables? I can only envision 2 variables vs. 1 constant at the momemtn in my mind.
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-228276)
    
9.  ![](https://secure.gravatar.com/avatar/e644aadb8cbeec3382af0f89bc48f0a929b4477366b824b0dd94704c0d42a5f1?s=64&d=mm&r=g) Alex says:
    
    [December 17, 2013 at 11:20 pm](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-460176)
    
    Could not get the values you got by using Data Table. Could you please specify how you got all the different scenario values?
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-460176)
    
10.  ![](https://secure.gravatar.com/avatar/e644aadb8cbeec3382af0f89bc48f0a929b4477366b824b0dd94704c0d42a5f1?s=64&d=mm&r=g) Alex says:
    
    [December 17, 2013 at 11:23 pm](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-460178)
    
    I got it. But why we use the value cell with formula?
    
    [Reply](https://chandoo.org/wp/scenario-analysis-for-the-project/#comment-460178)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/scenario-analysis-for-the-project/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Video Tutorial on Interactive Dashboard using Hyperlinks](https://chandoo.org/wp/video-on-interactive-dashboard-using-hyperlinks/) | [Financial Modeling School is Open, Please Join Today!](https://chandoo.org/wp/financial-modeling-online-classes/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)