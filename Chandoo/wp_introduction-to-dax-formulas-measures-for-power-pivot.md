# Introduction to DAX Formulas & Measures for Power Pivot » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot

---

Introduction to DAX Formulas & Measures for Power Pivot
=======================================================

[Power Pivot](https://chandoo.org/wp/category/power-pivot/)
 - 23 comments

  

Last week, you saw an [Introduction to Power Pivot for Excel](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/ "What is Power Pivot – an Introduction ")
. Today, lets talk about DAX formulas & measures for Power Pivot.  
![Definition of a measure & Introduction - Excel Power Pivot](https://img.chandoo.org/power-pivot/what-is-a-measure-power-pivot.png)

What is a Measure?
------------------

**_A measure is a formula for the values area of Power Pivot table._**

A measure can be implicit or explicit.

**Implicit measures** are created automatically when you drag and drop a field in to Power Pivot values area. For example, in last week’s introduction, we created an implicit measure for _SUM of Sales_ by dragging and dropping the sales amount field in to values area of our power pivot table.

**Explicit measures** are created by you using New measure button in Power Pivot tab (or Calculated Field button in Excel 2013 Power Pivot tab). _You can also create a measure in the Power Pivot window.  
_

### Measures vs. Calculated Fields

They both refer to the same thing in the context of Power Pivot. Up to Excel 2010 Power Pivot versions, Microsoft used Measure as the official term.

Starting Excel 2013, Measures became Calculated Fields.

![Creating a measure - Excel 2010 vs. Excel 2013](https://img.chandoo.org/power-pivot/creating-a-new-measure-excel2010-vs-excel2013.png)

So what is DAX then?
--------------------

DAX stands for **D**ata **A**nalysis E**x**pression. It is a special language we use to create measures in Power Pivot. Although it is a special language, it looks exactly like our regular Excel formulas. That means you can easily learn the DAX basics and create measures in no time.

_**Think of DAX as Excel Formula ++.** An upgraded version of Excel formulas that can handle power pivot data and give you the calculations you want._

Lets create a measure
---------------------

### Step 1: Decide what the measure should do

The first step is to figure out the need for a measure. Lets say we want a measure to sum up total sales.

### Step 2: Launch New Measure screen

In Excel 2010: Power Pivot Ribbon > New Measure

In Excel 2013: Power Pivot Ribbon > Calculation Field > New Calculation Field

This will open below screen (screenshot for Excel 2013 shown below. Excel 2010 looks almost similar).

![Creating a new measure in Excel Power Pivot - Demo](https://img.chandoo.org/power-pivot/steps-for-creating-a-new-measure-in-excel-power-pivot.png)

### Step 3: Give our measure a name

Lets call it **Total Amount**

#### Step 4: Write the DAX formula

The formula for summing sales is =SUM(sales\[sale amount\])

**_This formula looks exactly like an Excel formula!!!_**

As I mentioned before, the syntax, look & fell of DAX is just like Excel formulas. It is DAX’s power, flexibility & variety that outsmarts Excel formulas.

When you press OK, a new measure (Total Amount) will be created and attached to the Sales table in your power pivot data model. It looks like this,

![Once you create a measure, it will show up in your data model like this.](https://img.chandoo.org/power-pivot/dax-measures-or-calculated-fields-will-show-up-in-power-pivot-data-model.png)

### Step 5: Add this measure to your Power Pivot report

Just drag and drop this measure in to values area of your pivot report. Instantly total sales amount will be calculated based on your report set up.

Why bother creating a measure for such simple thing as SUM?
-----------------------------------------------------------

I know you would be asking this. It seems like a lot of trouble to create a measure, to just show the sum of sales amount. Well, SUM & COUNT are just tip of the DAX iceberg. The power of DAX formula engine is truly phenomenal. To prove it, lets play a small game.

_Imagine how much time you would take_ to write a regular Excel formula or setting up a regular Pivot report to answer each of these questions:

*   Count of distinct customers by region & Product category for month of May 2012
*   Sum of sales made in weekends only by customer gender & product size for Q1, 2012
*   Percentage of sales made in weekends (compared to total sales) by customer name
*   Number of customers during lunch hours (between 12noon & 1:30 PM) by week day

Now, how would you feel if I tell you that **using DAX, it will take less than 5 minutes to answer all these questions**. 5 minutes!!!

And the beauty is, once we have a measure that tells us sales made in weekends, we can use it in any report:

*   Sales in weekends by gender & product size – YES
*   Sales in weekends by product category & month – YES
*   Sales in weekends by year & season – YES

All without any additional work!

Oh this is so tempting, teach me how, teach me now
--------------------------------------------------

Don’t worry. I am not going to leave you high & dry. I made a video (30 mins) explaining below topics:

*   Introduction to DAX, measures & calculated fields
*   Implicit vs. Explicit measures
*   Creating a simple DAX measure
*   Example DAX measures & explanation:
    *   Sum of sales
    *   Count of distinct customers
    *   Sales made in weekend
    *   Percentage of sales made in weekend

[![Introduction to DAX measures & formulas for Excel Power Pivot](https://img.chandoo.org/power-pivot/introduction-to-measures-and-dax-formulas-for-power-pivot.png)](http://chandoo.org/wp/resources/learn-power-pivot-for-excel/ "Learn Power Pivot for Excel")
 

How can I learn more?
---------------------

If all this sounds interesting, you would enjoy our **upcoming online course on Power Pivot.** If you want to know more about our class, please enter your name & email below. I will also send you 2 videos on Power Pivot.

\[[Click here in case you are not able to see the sign-up form.](http://forms.aweber.com/form/42/1880494142.htm)\
\]  

Do you DAX? Share your tips & experiences
-----------------------------------------

It took me a while to wrap my head around the way DAX formulas work. I am still learning and struggling to come up with measures for every thing. But I find them very powerful & addictive. I am now able to create powerful analysis reports & dashboards for my clients, thanks to DAX formulas and Power Pivot.

**What about you?** Do you play with DAX often? What is your experience like? _Please share your ideas, tips & suggestions in comments._

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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [calculated fields](https://chandoo.org/wp/tag/calculated-fields/)<br>, [DAX formulas](https://chandoo.org/wp/tag/dax-formulas/)<br>, [excel 2013](https://chandoo.org/wp/tag/excel-2013/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [measures](https://chandoo.org/wp/tag/measures/)<br>, [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)<br>, [powerpivot](https://chandoo.org/wp/tag/powerpivot/)<br>, [videos](https://chandoo.org/wp/tag/videos/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 23 Responses to “Introduction to DAX Formulas & Measures for Power Pivot”

1.  ![](https://secure.gravatar.com/avatar/df4333cc363ece057952a9704b4acd511064de688497eba074f268ce597f6df9?s=64&d=mm&r=g) Rahim says:
    
    [January 28, 2013 at 9:01 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409478)
    
    Thanks for sharing your 2nd post on PowerPivot,  
    Please can you share Video link other than Youtube. Thanks  
       
    \*\*As is it still blocked in Pakistan
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409478)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [January 28, 2013 at 9:04 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409482)
        
        @Rahim... You are welcome. The video is not on youtube. You will be able to see it once you confirm your email address here: [http://chandoo.org/wp/resources/learn-power-pivot-for-excel/](http://chandoo.org/wp/resources/learn-power-pivot-for-excel/)
        
        [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409482)
        
        *   ![](https://secure.gravatar.com/avatar/df4333cc363ece057952a9704b4acd511064de688497eba074f268ce597f6df9?s=64&d=mm&r=g) Rahim says:
            
            [January 28, 2013 at 9:08 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409483)
            
            Thanks ! 🙂
            
            [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409483)
            
            *   ![](https://secure.gravatar.com/avatar/f4e46a9d94bb7991706d628f810b71d8dd408a63ef7ae0f570104630859b2837?s=64&d=mm&r=g) Syeda says:
                
                [September 6, 2021 at 10:35 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2027720)
                
                Hi Chandoo,  
                Thank you for sharing such a useful information and it really help me to upgrade my skills. I watch your measures and Dax video on your, but unable to access this video. can you please give me access to view it.  
                Apart from this I want to join the course as well.
                
                [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2027720)
                
2.  ![](https://secure.gravatar.com/avatar/df4333cc363ece057952a9704b4acd511064de688497eba074f268ce597f6df9?s=64&d=mm&r=g) Rahim Zulfiqar Ali says:
    
    [January 28, 2013 at 5:59 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409577)
    
    My Question related to video:  
    If we have to calculate "Sales in Weekend" column in rolling months. Does the DAX Formula will work for all the months correctly ? How ?  
    Do we have to always find out when the first Monday comes in a particular month ? Example our database has months from Jul to Dec 2013.  
    I hope I have written my questions well to have your answers. Thanks in Advance. Looking forward to it and your course. But would be more happy If we (Visitors) can get 1 or 2 more lessons of PowerPivot on your Blog. 🙂  
       
    Thanks again
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409577)
    
3.  ![](https://secure.gravatar.com/avatar/83378b87fd6b3d87e05c7178c073cee27609f8572cbf04c363692bcb5ccec07d?s=64&d=mm&r=g) Shar says:
    
    [January 28, 2013 at 8:51 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409604)
    
    I'm loving the PowerPivot information!  Question though, we don't use Sharepoint at my work - is there any other way to share a PowerPivot workbook?
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-409604)
    
4.  ![](https://secure.gravatar.com/avatar/d324249643b6662e2e7aa240766e1e5cae73ac85ecd48384d328e9250520e90c?s=64&d=mm&r=g) Rajeev Gautam says:
    
    [February 2, 2013 at 9:20 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-410818)
    
    Mr. Chandoo,  
       
    I Request you please add given below topic in Power Pivot course.  
       
    1\. How to Handle Many to Many Relationship  
    2\. Non Additive and Semi Additive Calculation  
    3\. How to make Asymmatire Reports using Power Pivot  
    4\. How to handle Banding Ranges Slab(0-10,11-15 etc)  
    5\. Ratio and Percentage.  
       
    Regards,  
       
    Rajeev Gautam
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-410818)
    
5.  [Blog Posts of the Week (27th Jan'13 - 02nd Feb'13) - The South Asia MVP Blog - Site Home - TechNet Blogs](http://blogs.technet.com/b/southasiamvp/archive/2013/02/04/blog-posts-of-the-week-27th-jan-13-02nd-feb-13.aspx)
     says:
    
    [February 4, 2013 at 4:33 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-411385)
    
    \[...\] Introduction to DAX Formulas & Measures for Power Pivot \[...\]
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-411385)
    
6.  [Excel Big Data Connectivity and other Microsoft BI and Analysis Offerings | Moonlight Knowledge Exchange](http://moonlightkx.com/microsoft-excel-b/)
     says:
    
    [March 30, 2013 at 1:31 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-421625)
    
    \[...\] Chandoo.org on DAX Formulas and PowerPivot \[...\]
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-421625)
    
7.  ![](https://secure.gravatar.com/avatar/0ab4d949d416389c1fbec36020481c8750c2a64a333a466af0acf659f6ec2ec7?s=64&d=mm&r=g) Kim Cook says:
    
    [May 24, 2013 at 12:06 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-432371)
    
    Hi,
    
    I am trying to view the DAX formula video and I have already signed up for the course. Everytime I try to view the video I get the sign up screen.
    
    TIA
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-432371)
    
8.  ![](https://secure.gravatar.com/avatar/022c5eda5fcc966f10035963138f78574584f60b607f15e6d44a68ef05e15353?s=64&d=mm&r=g) Heather says:
    
    [March 31, 2014 at 1:19 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-476686)
    
    I need help. I have Tasks listed in the column labels quadrant in excel 2010, a date in the row label and values in the values quadrant. I created a new measure to average some time values for each of the 2 tasks. Now I want to create a mesaure to average the 2 averages. Both columns are labled the same thing "Avg Time (Minutes)". How do I get an average of those two columns when they are titled the same thing because of how it was done? Can I do a new measure and put in column names like a basic excel function (i.e. =Average(I8,J8)? Thanks!
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-476686)
    
9.  ![](https://secure.gravatar.com/avatar/a4cdcd7c550898d00b44bc664800c71cad3508058a03073d0fd8cd33a010d8df?s=64&d=mm&r=g) Jacob Metzger says:
    
    [April 17, 2015 at 8:07 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-954421)
    
    I am trying to view "Introduction to Measures & DAX" video, after I signup with my email, all I get is the course sign-up screen!
    
    Please help!
    
    Jacob
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-954421)
    
10.  ![](https://secure.gravatar.com/avatar/9ea9294e48f924c016584f64c78b0fa223ee02006bf4eb9ef25350348559904d?s=64&d=mm&r=g) Vinicius Martim says:
    
    [November 24, 2015 at 4:50 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1088450)
    
    I've been trying to find the "Calculated Item" functionality of the conventional Pivot Table on the PowerPivot options and measures. But I haven't found any so far.  
    Does someone here has a hint about it?
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1088450)
    
    *   ![](https://secure.gravatar.com/avatar/635224a2b130b222c49a6da67874be274b2c704cbb47249494387589884512f2?s=64&d=mm&r=g) jeremy says:
        
        [December 20, 2021 at 6:38 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2054624)
        
        Hi have you found a way to solve it? im also suffered from that PowerPivot with it you cant use the calculated item function which is quite powerful in excel pivot. pls help.
        
        [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2054624)
        
11.  ![](https://secure.gravatar.com/avatar/ce1aee913eb8a0304381f58a37e75122dcf1849fde8d8400444f6720c7800393?s=64&d=mm&r=g) Arturo says:
    
    [April 13, 2016 at 3:42 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1168101)
    
    Estoy incursionando en el Power Pivot y quisiera saber cómo agrupo las fechas por ejemplo?. Gracias de antemano.  
    \[Google translate\] I'm dabbling in Power Pivot and let me know how I group the dates for example ?. Thanks in advance.
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1168101)
    
12.  ![](https://secure.gravatar.com/avatar/2f003815955b38cf901c44ca72554f3e5baf949c79e741c9760d5794b4e8ee91?s=64&d=mm&r=g) harga rumah kunci motor honda says:
    
    [July 28, 2018 at 4:35 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566537)
    
    Hi there everyone, it's my first pay a quick visit at this web page, and  
    piece of writing is genuinely fruitful in support of me, keep up  
    posting these types of content.
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566537)
    
13.  ![](https://secure.gravatar.com/avatar/789bee9fa6080ce84b0fe04c0b9ca2e8e639bcd3bbba4a0d034085852620729b?s=64&d=mm&r=g) Satish Shah says:
    
    [August 1, 2018 at 6:35 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566948)
    
    Hi Chandoo,
    
    I am trying to find return on investment when money have been invested at irregular time.
    
    So let's say that my initial investment was £100 for a fund and that grew to £x by a certain date, I then add more money at a later date to the same fund and at a later date I add more money to the same fund.
    
    The unit price of the fund is say £Y at new dd/mm/yy so I know total value of my fund at any point but how do I work out return on my investment.
    
    Hope my question make sense.  
    Many thanks  
    Satish
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566948)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 1, 2018 at 10:42 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566960)
        
        @Satish... you can use XIRR() to get rate of return from irregular cash flows. Set up your data like this and you are good to go:  
        ![XIRR example - calculating rate of return from irregular cash flows](https://chandoo.org/wp/wp-content/uploads/2018/08/SNAG-0451.png)
        
        [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1566960)
        
14.  ![](https://secure.gravatar.com/avatar/0fc63cdf414912665cd69b486a12a99fe979f66175ba87c2f90c8975579a8490?s=64&d=mm&r=g) iptv server uhd says:
    
    [October 26, 2018 at 8:05 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1583866)
    
    Hey there I am so glad I found your website, I really found you by error, while I was researching on Aol for something else,  
    Anyhow I am here now and would just like to say thanks  
    for a marvelous post and a all round interesting blog (I  
    also love the theme/design), I don’t have time to browse it all at the moment but I have bookmarked it and also included your RSS feeds, so when I have time I will be back to read more, Please do keep up the fantastic work.
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1583866)
    
15.  ![](https://secure.gravatar.com/avatar/aaf2a2e7a48f90877c28041e3002a9a6a68f96aca70308d1aaf895ab43fbb155?s=64&d=mm&r=g) Dahlia says:
    
    [October 3, 2019 at 6:01 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1692436)
    
    I cannot sign up. I have been trying to request to see the video so i entered my name and email but it says i am not in the mailing list.
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1692436)
    
16.  ![](https://secure.gravatar.com/avatar/b47d8465eb28d548c98753c18c5e16230390a07cbe1c5aec27513cf280bb5893?s=64&d=mm&r=g) Mila says:
    
    [June 14, 2020 at 2:41 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1811201)
    
    Hi Chandoo,  
    I enjoy your blog. I tried watching the video, but was not able to. It says the mailing list is not active.
    
    Thank you!!  
    Mila
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1811201)
    
17.  ![](https://secure.gravatar.com/avatar/6a64ed3c96507eae0a37528d808293a752dbd0380e5a54cf9e02f7ebd2da26b6?s=64&d=mm&r=g) mehdi bakhshi says:
    
    [December 6, 2020 at 1:04 pm](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1941622)
    
    hi, when i fallow the link to "Learn Power Pivot for Excel" this error is appeared "Mailing List Not Active"  
    what I have to do?
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-1941622)
    
18.  ![](https://secure.gravatar.com/avatar/d02cb3e9d9a178115c1a4bc543ce0da5c599bef8ea8b750ec9e065ef96b6128e?s=64&d=mm&r=g) jeremy says:
    
    [December 6, 2021 at 4:33 am](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2050378)
    
    The problem is " how to build a hundred measures" i was told to install Dax studio, but unluckily I find it cant not updates my changes in the edit zone back to Powerpivot. as i search further it shows more of powerBI, i dont really need that. is there a efficient way to solve this problem, which supposed to be very commenly encountered by users.
    
    [Reply](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#comment-2050378)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/introduction-to-dax-formulas-measures-for-power-pivot/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Can you calculate vacation days in a period? \[Homework\]](https://chandoo.org/wp/calculate-vacation-days/) | [Details about our Power Pivot Course \[and a video for those of you not interested\]](https://chandoo.org/wp/power-pivot-course-details/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)