# Agenda Template for meetings, events, conferences etc. - Download Excel Agenda Template

**Source:** https://chandoo.org/wp/agenda-template-excel

---

Creating an Agenda template in Excel
====================================

[Templates](https://chandoo.org/wp/category/templates-2/)
 - 13 comments

  

When planning a meeting, an event or activity, we deal with many individual steps (each taking certain amount of time). **Today let us understand how to create an agenda template** in Excel using simple formulas.

![Agenda Template in Excel - Download free](https://img.chandoo.org/templates/agenda-template-in-excel.png)

Setting up Agenda Template
--------------------------

In a blank workbook, set up a structure like this:

![Setting up Agenda Template - Excel template download](https://img.chandoo.org/templates/setting-up-agenda-template.png)

Then,

1.  Enter the start time of the first activity.
2.  In fill up durations for all activities in minutes.
3.  End time = start time + minutes
4.  So the formula for end time cell is \=start-time + duration-minutes / 24 / 60.
    
    **Note:** We need to divide by 24 & 60 because in Excel each day 1 number, each hour is 1/24th and each minute is 1/24/60th. \[[learn more about Excel dates](http://chandoo.org/wp/2008/08/26/date-time-tips-ms-excel/)\
    \]
    
5.  The start time for subsequent activities is equal to end time of previous activity.
6.  Fill down the formulas and your agenda template is ready!

Download Excel Agenda Template
------------------------------

[**Click here to download Agenda template**](https://img.chandoo.org/templates/agenda-template.xlsx)
 and use it for planning next big, awesome event 🙂

It contains a ready to use agenda template with built in formulas. The template also highlights any activities marked as break in different color _using conditional formatting_.

More templates for you
----------------------

If you like this agenda template, you are going to love these other templates too.

*   [To do list template](http://chandoo.org/wp/2008/10/01/simple-todo-list-using-excel/ "Simple Todo List application using Excel – Download and become productive")
    
*   [Issue tracker template](http://chandoo.org/wp/2009/09/08/issue-trackers/ "Issue Trackers & Risk Management using Excel [Project Management using Excel - Part 5 of 6]")
    
*   [New year resolutions template](http://chandoo.org/wp/2010/01/07/new-year-resolutions-template/ "A New Year Resolutions Template that Kicks Ass")
    
*   [2013 Calendar and event planner template](http://chandoo.org/wp/2012/12/26/download-free-2013-calendar/ "2013 Calendar – Excel Template [Downloads]")
    

_This template is inspired from a question emailed by Renuka, one of our readers._

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
| Written by Chandoo  <br>Tags: [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [templates](https://chandoo.org/wp/tag/templates/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 13 Responses to “Creating an Agenda template in Excel”

1.  ![](https://secure.gravatar.com/avatar/049b5849a1c9afa1b0b0c05aa34e3a8f506d0c8423dc1c69d5a83ce504960872?s=64&d=mm&r=g) Yard says:
    
    [January 4, 2013 at 8:52 am](https://chandoo.org/wp/agenda-template-excel/#comment-377599)
    
    \*\*KLAXON SOUND\*\*  
       
    The template contains merged cells!!  
       
    \*\*KLAXON SOUND\*\*
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-377599)
    
    *   ![](https://secure.gravatar.com/avatar/e9b125c95205a0ad380d8e59daa8c30a260d7c7aaa109c2847b0e0c6b86677d2?s=64&d=mm&r=g) Adam says:
        
        [January 7, 2013 at 2:56 pm](https://chandoo.org/wp/agenda-template-excel/#comment-382529)
        
        In this day and age, there is no need for merged cells. Ever.
        
        [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-382529)
        
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [January 7, 2013 at 3:29 pm](https://chandoo.org/wp/agenda-template-excel/#comment-382574)
        
        I disagree. There is no harm in having a merged cell in a simple workbook like this. Even in complex workbooks, I rarely notice any performance or macro coding issues with merged cells. Although they may cause certain problems, you should not worry about them unless you are doing some heavy duty programming or constantly referring to merged cells thru your code.
        
        I used it in this template for cosmetic reasons alone and I feel going thru format cells > alignment > center across selection is un-necessary steps for something simple like agenda template.
        
        [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-382574)
        
        *   ![](https://secure.gravatar.com/avatar/e9b125c95205a0ad380d8e59daa8c30a260d7c7aaa109c2847b0e0c6b86677d2?s=64&d=mm&r=g) Adam says:
            
            [January 7, 2013 at 4:04 pm](https://chandoo.org/wp/agenda-template-excel/#comment-382605)
            
            I understand why people merge cells, it looks better.  
            But when you go to select one column some 150 rows lower it is maddening that four are selected because of a merge & centre elsewhere!  
            Given that 'centre across selection' (from the ctrl + F1 menu, alignments tab) does exactly the same job, merge & centre should be avoided at all costs.  
            I think that was what Yard was hinting at!!  
            🙂  
             
            
            [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-382605)
            
2.  ![](https://secure.gravatar.com/avatar/55443793b0a927a95862967d50699956e1974ab164a1289610920f84e9f34cca?s=64&d=mm&r=g) Johnny says:
    
    [January 4, 2013 at 6:48 pm](https://chandoo.org/wp/agenda-template-excel/#comment-378239)
    
    Hi Chandoo  
    When cell E7 is selected, a comment box pops up.  
    Can you explain to me how that was done?  
    Thank you.
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-378239)
    
    *   ![](https://secure.gravatar.com/avatar/df4333cc363ece057952a9704b4acd511064de688497eba074f268ce597f6df9?s=64&d=mm&r=g) Rahim Zulfiqar Ali says:
        
        [January 5, 2013 at 7:52 am](https://chandoo.org/wp/agenda-template-excel/#comment-379103)
        
        This can be applied via Go to Data Ribbon, Than Data Tools Tab, Click on Data Validation. A window will appear Select Input Message Tab and Write your Message in "Input Message Box". Click OK to be applied. 
        
        Thanks,
        
        Regards, RIMZ 
        
        [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-379103)
        
3.  ![](https://secure.gravatar.com/avatar/dc6a9317448fdb66504e1cd9aa2b758eae48ddfe3e36f8bb8777ab79517a9acf?s=64&d=mm&r=g) Ananthram says:
    
    [January 5, 2013 at 6:17 am](https://chandoo.org/wp/agenda-template-excel/#comment-379009)
    
    Hi Chandoo sir,  
       
    When i click on E7 Cell a box pop up can i know how its been done.
    
    Thanks in Advance
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-379009)
    
4.  [Blog Posts of the Week (23rd Dec'12 - 05th Jan'13) - The South Asia MVP Blog - Site Home - TechNet Blogs](http://blogs.technet.com/b/southasiamvp/archive/2013/01/07/blog-posts-of-the-week-23rd-dec-12-05th-jan-13.aspx)
     says:
    
    [January 7, 2013 at 12:09 pm](https://chandoo.org/wp/agenda-template-excel/#comment-382360)
    
    \[...\] Creating an Agenda template in Excel \[...\]
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-382360)
    
5.  ![](https://secure.gravatar.com/avatar/3fa9570c3f14447eb131a5cf5dfd0a96506ce2d1e1322cb5192d84add1d23da2?s=64&d=mm&r=g) Warren says:
    
    [January 19, 2013 at 4:02 pm](https://chandoo.org/wp/agenda-template-excel/#comment-399634)
    
    Suggestion: use +TIME(0,duration-minutes,0) instead.  
    It makes it easier to see that there's a time calculation being made, and just what is being done.  
     
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-399634)
    
6.  ![](https://secure.gravatar.com/avatar/465ef9f955fc04b0a0d328e6a89acd505032fe361b66f8656be49e2f9af3dfb3?s=64&d=mm&r=g) Shane says:
    
    [February 19, 2013 at 4:14 pm](https://chandoo.org/wp/agenda-template-excel/#comment-414903)
    
    Hello! I work in a role that's constantly used for planning big and multiple meetings any given day. I actually created this exact agenda on my own, but I've always had trouble with sorting. I have researched various blogs and excel sites to figure out how to retain formula/data integrity when sorting on the agenda item #. Things are bound to change at the last moment, so I'm trying to come up with a solution when I have to reorder agenda items but ensure meeting times still reflect accurately based on duration and end times. Any suggestions?
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-414903)
    
7.  ![](https://secure.gravatar.com/avatar/dde176cf0764e511e51f434abe887bf060095772daad7ab26160cde52e16fccd?s=64&d=mm&r=g) Nada says:
    
    [January 2, 2014 at 8:05 am](https://chandoo.org/wp/agenda-template-excel/#comment-463233)
    
    I couldnt open any of the templates. I have Office 2010 and when I saved the link then tried top open there was not .xls or .xlsx files. all was XML which yet couldnt be opened in Excel 2010. Kindly advise...
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-463233)
    
8.  ![](https://secure.gravatar.com/avatar/ca37c4da5cc8bc859b9d51d8b16bb2d4e09db6d14d8176f0537f29ad75b85465?s=64&d=mm&r=g) [generatefifa15coins.com](http://generatefifa15coins.com/)
     says:
    
    [June 11, 2015 at 12:09 am](https://chandoo.org/wp/agenda-template-excel/#comment-990714)
    
    It's always interesting to actually receive a sales call,  
    especially when you work in the sales profession and  
    have your own goals for sales. These banks are often smaller than their competitors  
    and focused on a specific geographic niche. Little did she know that three years  
    later, when she was just 15, she would be called up  
    for the United States national women.
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-990714)
    
9.  ![](https://secure.gravatar.com/avatar/f262e6d7198763ad3a124368d7acbae306da53332632bee593c0c0fc5e9f4675?s=64&d=mm&r=g) Carol says:
    
    [December 18, 2024 at 6:01 pm](https://chandoo.org/wp/agenda-template-excel/#comment-2329334)
    
    I want to add a line but not have the time or numbering change. how do i do that.. example  
    1\. Welcome start duration end  
    a.approve minutes  
    b.discuss in person meetings  
    2\. topic start duration end  
    a. bla bla
    
    is there a way i can do this with the template?
    
    [Reply](https://chandoo.org/wp/agenda-template-excel/#comment-2329334)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/agenda-template-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Please take our readership survey and help me make you awesome in 2013 \[Surveys\]](https://chandoo.org/wp/readership-survey-2013/) | [To-do List with Priorities using Excel](https://chandoo.org/wp/todo-list-with-priorities/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)