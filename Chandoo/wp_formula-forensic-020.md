# Setup a Working days calendar using this neat formula

**Source:** https://chandoo.org/wp/formula-forensic-020

---

Formula Forensic 020. Bhavik’s Monthly Workingdays Formula
==========================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 7 comments

  

I recently received an email from **Bhavik** who was excited to share a neat little formula for determining the number of days worked during a month.

This formula has a wide range of uses in accounting, payroll, staff scheduling, accommodation planning & reporting and general scheduling activities.

Bhavik’s formula,

 \=MAX(0,NETWORKDAYS(MAX($A2,C$1),MIN($B2,EOMONTH(C$1,0))))

cleverly uses the Networkdays( ) function in conjunction with Min( ), Max( ) and Eomonth( ) functions to calculate the number of working days available during the month.

So today at Formula Forensics we will look at Bhavik’s Formula and see what makes it tick.

Bhavik’s Formula
----------------

To follow along you can Download a Sample File of Bhavik’s Formula here: [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2012/04/WorkDays-Cal.xls "Sample File")

Bhavik’s Formula is based around the Excel Networkdays( ) function, which is wrapped inside a Max ( ) function and uses a couple of other Min( ), Max( ) and Eomonth( ) functions as part of the Networkdays( ) parameters.

\=MAX(0,NETWORKDAYS(MAX($A2,C$1),MIN($B2,EOMONTH(C$1,0))))

Lets jump in and see what makes Bhavik’s Formula tick.

\=MAX(0,NETWORKDAYS(MAX($A2,C$1),MIN($B2,EOMONTH(C$1,0))))
 

### Caution

Instead of using the cell Ranges in describing the functionality of the file, I am going to use the following words

**Join Date**:            The Date that the employee Joined the company, Column A

**Finish Date**:        The Date that the employee’s position ended with the company, Column B

**Month**:                    The current Month’s Date. The month’s are described as dates using the first of the month as a Reference date. Eg: April 2012 = 1/4/2012

So to rewrite Bhavik’s Formula we using the above names (These aren’t Named Formulas)

\=MAX(0, NETWORKDAYS(MAX(Join Date, Month), MIN(Finish Date , EOMONTH(Month, 0))))

Bhavik’s Formula is based around the Excel Networkdays( ) function.

The syntax for the Networkdays( ) function is shown below:

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_1.png "FF20_1")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_1.png)

We can see that the Networkdays( ) function has 2 requirements , being the Start Date and End Date

In Bhavik’s Formula:

NETWORKDAYS(MAX(Join Date, Month), MIN(Finish Date , EOMONTH(Month, 0)))

**Start\_Date**:         MAX(Join Date, Month)

**End\_Date**:           MIN(Finish Date , EOMONTH(Month, 0))

We can see that Bhavik’s Formula hasn’t included the optional Holidays functionality of the Networkdays( ) function. This will be discussed later.

Networkdays returns the number of work days between the Start Date and the End Date.

### Start Date

In Bhavik’s Formula, the Start Date is defined as MAX(Join Date, Month)

This will select the later date or highest of the Join Date and the Current Month. Hence if the Join Date is before the current month, the Current Month will be used as the start date.

If the Join Date is during the Current Month, the Join Date will be used as it will be higher than the Current month.

If the Join Date is after the Current Month, Networkdays will return a negative. This is dealt with by the leading Max(0, ) function which will take a 0 value if Networkdays  returns a negative number as any negative number is less than zero.

\=MAX(0, NETWORKDAYS(MAX(Join Date,Month), MIN(Fisnish Date , EOMONTH(Month, 0)))) 

### End Date

\=MAX(0, NETWORKDAYS(MAX(Join Date,Month), MIN(Finish Date , EOMONTH(Month, 0))))

In Bhavik’s Formula, the End Date is defined as MIN(Finish Date , EOMONTH(Month, 0))

This will select the minimum date of the Finish Date or End of the Current Month, which is determined by the function, EOMONTH(Month, 0).

If the Finish Date is before the current month, the Finish Date will be used as the End Date. This may cause Networkdays to return a –‘ve which is corrected by the Max(0 as descried above:

\=MAX(0, NETWORKDAYS(MAX(Join Date, Month), MIN(Finish Date , EOMONTH(Month, 0))))

If the Finish Date is during the current month, the Finish Date will be used as the End Date.

If the Finish Date is after the current month, the End of Month of the Current Month will be used as the End Date.

Application
-----------

Now we understand how the formula works we can have a look at it in use :

In cell C2 put:

\=MAX(0,NETWORKDAYS(MAX($A2,C$1),MIN($B2,EOMONTH(C$1,0))))

Copy across and down

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_4.png "FF20_4")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_4.png)

There is an example of every date combination described above and listed in the **Options** Column.

Now that you understand the logic, You can work through these cells, one by one, and examine why each month’s formula works.

Holidays
--------

In the syntax of the Networkdays( ) function, you will see there is an optional Holidays parameter.

This can be as simple as a range of cells or an array of dates defining the holidays

In the worked example the range B13:B15 contains 3 dates reflecting 3 Public Holidays in Australia.

When the dates are added to the formula

\=MAX(0,NETWORKDAYS(MAX($A9,C$1),MIN($B9,EOMONTH(C$1,0)),$B$13:$B$15))

We can see that the workdays in January and March are reduced by 1 day each, noting that New Years Day is on a Sunday and hence not included as a Holiday.

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_3.png "FF20_3")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_3.png)

I should note that in Australia the New Years Day holiday is actually taken on the following Monday (2 Jan 2012), but this was excluded for this example as a demonstration only to show that because it is on a Sunday it is not included.

New Functions !
---------------

In **Excel 2010**, Microsoft introduced the **Networkdays.intl( )** function.

This is a new version of the Networkdays Functionality but has the added benefit of being able to define the Weekends.

The Excel Networkdays.intl( ) function uses the following syntax:

[![](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_2.png "FF20_2")](https://chandoo.org/wp/wp-content/uploads/2012/04/FF20_2.png)

The main benefit of using  the Excel Networkdays.intl( ) function is that you can define your own weekends, rather than rely on the standard Saturday/Sunday option that Networkdays( ) provides.

For example:

\=MAX(0,NETWORKDAYS.INTL(MAX($A9,C$1),MIN($B9,EOMONTH(C$1,0)), 6, $B$13:$B$15))

The weekend parameter is set to 6 and so excel will use Thursday and Friday as the weekend

\=MAX(0,NETWORKDAYS.INTL(MAX($A9,C$1),MIN($B9,EOMONTH(C$1,0)), "1010100", $B$13:$B$15))

The weekend parameter is set to a text string of “1010100” and so excel will use Monday, Wednesday and Friday as the weekend days

\=MAX(0,NETWORKDAYS.INTL(MAX($A9,C$1),MIN($B9,EOMONTH(C$1,0)), Z1, $B$13:$B$15))

The weekend parameter is set to Z1 and so Excel will retrieve the value from cell Z1 to define the weekend. Cell Z1 must contain a valid number from 1 to 17 as described above or a 7 character Text string like ‘1010100.

I strongly recommend that users who have switched to Excel 2010 start using the new formulas, as they add a raft of new features to your Excel arsenal.

### What else is new in Excel 2010?

What else is new in Excel 2010? [Have a look here](http://office.microsoft.com/en-us/excel-help/what-s-new-in-excel-2010-HA010369709.aspx "What's new in Excel 2010")
.

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/04/WorkDays-Cal.xls "Sample file")
.

Formula Forensics “The Series”
------------------------------

This is the 20th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics - The Series")

Formula Forensics Needs Your Help !
-----------------------------------

I need more ideas for future Formula Forensics posts and so I continue to need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained but don’t want to write a post as Bhavik’s has done here, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "About Chandoo")
.

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
| Written by Hui...  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [eomonth](https://chandoo.org/wp/tag/eomonth/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [max()](https://chandoo.org/wp/tag/max/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [MIN()](https://chandoo.org/wp/tag/min/)<br>, [networkdays()](https://chandoo.org/wp/tag/networkdays/)<br>, [Networkdays.intl()](https://chandoo.org/wp/tag/networkdays-intl/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 7 Responses to “Formula Forensic 020. Bhavik’s Monthly Workingdays Formula”

1.  ![](https://secure.gravatar.com/avatar/8c7a45c1b40aba6138103d76acd3ecda6ff16bbf27e06bb9c407103327e1bf2f?s=64&d=mm&r=g) ahmed says:
    
    [May 4, 2012 at 10:16 am](https://chandoo.org/wp/formula-forensic-020/#comment-223464)
    
    This is a great formula, but it considered weekdays to be Saturday and Sunday, by default.
    
    How can it be changed for weekdays to be Friday and Saturday as in my country?  
     
    
    [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-223464)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) Hui... says:
        
        [May 4, 2012 at 11:57 am](https://chandoo.org/wp/formula-forensic-020/#comment-223468)
        
        Ahmed  
        Did you read the section on Networkdays.Intl ?  
        It does exactly what you want.
        
        [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-223468)
        
2.  ![](https://secure.gravatar.com/avatar/b5df25b5205023eb56a66fb7c8079a8253d31319c8d72249c525cc42d03a66bf?s=64&d=mm&r=g) [Planilhas Excel](http://blog.planilhasexcel.com/)
     says:
    
    [May 6, 2012 at 8:00 pm](https://chandoo.org/wp/formula-forensic-020/#comment-223530)
    
    I'm glad they added this function to Excel 2010, as it is very easy to make mistakes when making such a calculation
    
    [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-223530)
    
3.  ![](https://secure.gravatar.com/avatar/20f171816a827e9ce8a9f484ed251a2cbbd2f903220948a4370eb26f9a0176ef?s=64&d=mm&r=g) Cameron says:
    
    [May 16, 2012 at 3:13 pm](https://chandoo.org/wp/formula-forensic-020/#comment-223972)
    
    I had someone recently ask for number of working days between two dates by weekday.  
       
    Here's what I came up with; I would be interested to see if anyone has a different solution:  
       
    \[Uses two system tables, **Semesters** and **Holidays**\]  
       
    \[**Semesters** has 10 columns:\
    \
    **Semester** - The name of the date range (obviously a school semester in my example, but not necessarily so.)  \
    **start** - the first date in the date range  \
    **end** - the last date in the date range  \
    **Sunday** - shows the number of Sundays in the date range, excluding Sunday holidays  \
    **Monday** - you get the idea.  \
    **Tuesday**  \
    **Wednesday**  \
    **Thursday**  \
    **Friday**  \
    **Saturday**\]
    
    \[**Holidays** has 1 column:\
    \
    **List** - just a list of dates representing holidays\]
    
    \[**Semesters** formulas as follows:\
    \
    **Sunday**: =SUMPRODUCT(--(TEXT(\[@start\]-1+ROW(OFFSET($B$1,0,0,\[@end\]-\[@start\],1)),"dddd")="Sunday"))-SUMPRODUCT((Holidays\[List\]>=\[@start\])\*(Holidays\[List\]<=\[@end\])\*(TEXT(Holidays\[List\],"dddd")="Sunday"))  \
    **Monday**: =SUMPRODUCT(--(TEXT(\[@start\]-1+ROW(OFFSET($B$1,0,0,\[@end\]-\[@start\],1)),"dddd")="Monday"))-SUMPRODUCT((Holidays\[List\]>=\[@start\])\*(Holidays\[List\]<=\[@end\])\*(TEXT(Holidays\[List\],"dddd")="Monday"))   \
    **Tuesday**: Ok you get the idea again.  \
    ...\]
    
    I get the feeling that there's a cleaner, yet more abstract method to get these results?  
       
    Here's the file: [http://www.vertexvortex.com/r/excel/Workdays-Weekdays.xlsx](http://www.vertexvortex.com/r/excel/Workdays-Weekdays.xlsx)
    
    [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-223972)
    
4.  ![](https://secure.gravatar.com/avatar/aa687df58e3eef4947e1d25590c7637f19edf271bf711f93a2ce843289e52dcb?s=64&d=mm&r=g) Bob says:
    
    [July 12, 2012 at 4:46 pm](https://chandoo.org/wp/formula-forensic-020/#comment-226882)
    
    I am trying to use the following (copied it from this post). =MAX(0,NETWORKDAYS.INTL(MAX($B21,D$20),MIN($C21,EOMONTH(D$20,0)),1,$C$32:$C$34))  
    What need to do is has the data calculate to a status date vs. going on if there is no Finish date.  
    I have been working on it fro 2 days now and need some help.  Can anyone help me please.  
    Thank you in advance for any and all help...  
    
    [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-226882)
    
5.  ![](https://secure.gravatar.com/avatar/a4ddf6ee208e6b9210fc1a65c7e925d0a4fe40053ee8e8c92d9fc1a82d6f9ba2?s=64&d=mm&r=g) MamaG says:
    
    [September 14, 2014 at 3:50 am](https://chandoo.org/wp/formula-forensic-020/#comment-729115)
    
    I am attempting to make a calendar that will allow me to enter a date and then it will calculate for me the date that is 60 days before that date, 45 days before the date entered, 60 days after the date entered, and 120 days after the date entered. And it needs to exclude weekends and federal holidays for some of these time periods. Any ideas?
    
    [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-729115)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [September 14, 2014 at 4:14 am](https://chandoo.org/wp/formula-forensic-020/#comment-729211)
        
        @MamaG  
        Try using the Workdays.Intl() function  
        \=WORKDAY.INTL(A1,-60,1,Holidays)  
        Where A1 is the Date  
        \-60 is 60 days before  
        1 is Sat/Sun weekends  
        Holidays is a Named Range with a list of Valid Holidays
        
        [Reply](https://chandoo.org/wp/formula-forensic-020/#comment-729211)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensic-020/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Excel Links – Live from Sydney Edition](https://chandoo.org/wp/excel-links-live-from-sydney-edition/) | [Displaying Text Values in Pivot Tables without VBA](https://chandoo.org/wp/displaying-text-values-in-pivot-tables-without-vba/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)