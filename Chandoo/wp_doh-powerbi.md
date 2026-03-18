# D'oh - Visualizing Homer's favorite sayings in Power BI » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/doh-powerbi

---

*   [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

D’oh – Visualizing Homer’s favorite sayings in Power BI
=======================================================

*   Last updated: May 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Before we begin:**

Today is the last day for enrolling in our Power BI Play Date. Don’t miss out on this amazing opportunity to learn, use and benefit from Power BI at your work. Check out my online class and sign up before the doors close at midnight. [**Click here**](https://chandoo.org/wp/power-bi-course/)
.

Let’s get our Simpsons on then.

### D’oh, How often Homer says his favorite things?

Here is the visualization to explore Homer’s (and other character’s) favorite sayings in 27 years worth of Simpsons episode. Have a play.  
([Click here](https://app.powerbi.com/view?r=eyJrIjoiODFiZmUyOGItODFkOS00MGIzLTg1MTItNTdkNzhiYjQ2ODU1IiwidCI6IjUzNTA4ZDUyLWQxYjAtNDliMC1iNGJhLTM1MzNjMTI0OWEwMSJ9)
 if you are unable to see the visualization.)

### Where do we get the data?

To answer this question, we need to access Homer’s brain. It is in a high security vault, otherwise known as his skull.

![](https://chandoo.org/wp/wp-content/uploads/2017/09/homers-mind.png)

_**But we can’t connect to Homer’s brain as data source in Power Query. What then?**_

I am kidding. We can simply Google for this. And we quickly land at [Kaggle’s Simpsons Script Dataset](https://www.kaggle.com/wcukierski/the-simpsons-by-the-data)
. This contains 27 years of Simpson’s script, character, location and episode data. Download and load these tables in Power BI as tables.

### Connect tables

Connect script table to characters, locations and episodes. Also,

*   set up episodes\[image\_url\] as Image URL data category thru Modeling ribbon.
*   set up episodes\[video\_url\] as web URL data category thru Modeling ribbon

### Define a phrase list

Why stop with D’oh. Let’s make a list of all phrases you want to investigate. Using “enter data” feature of query editor (Power Query) create a list of phrases you want to explore.

Add this phrase list as a slicer to your Power BI visualization. Define a harvester measure to findout which phrase is clicked. Use `SELECTEDVALUE()` for this. Let’s call this measure \[selected phrase\]

### Count how many times characters said \[selected phrase\]

We can use SUMX, SEARCH to find out how many times \[selected phrase\] is uttered in all script text, like this:

`Phrase Count =SUMX(script, IF(SEARCH([selected phrase],script[normalized_text],1,0)>0,1,0))`

### Visualize phrase count by characters, episodes and locations

Add a few vizzes (tables work great, but try others too) to see how many times each character spoke that phrase. Explore and Enjoy.

### D’oh – Homer’s favorite sayings in Power BI – Video

I made a video tutorial explaining the entire process along with many tips on data clean up thru Power Query, measure writing and visualizations. True to Homer’s style, there is a d’oh moment in the video where I realize a fatal flaw in the analysis and fix it. Check it out below.

_See this video on [our Youtube channel](https://youtu.be/wW31JVVFG1k)
._

### Want more duff? Check out Power BI Play Date

If you love to play and learn, you are going to love our Power BI online class. In this program, you will learn all about Power BI from basics to #AWESOME level. You will get 9+ hours of video content covering Power Query, Power Pivot, Power BI and elegant dashboard design techniques. **[Check it out and sign up today](https://chandoo.org/wp/resources/power-bi-play-date/)
.**

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [4 Comments](https://chandoo.org/wp/doh-powerbi/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/doh-powerbi/#respond)
    
*   Tagged under [Power BI](https://chandoo.org/wp/tag/power-bi/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [power query](https://chandoo.org/wp/tag/power-query/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Power BI](https://chandoo.org/wp/category/power-bi/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    , [Power Query](https://chandoo.org/wp/category/power-query/)
    

[PrevPreviousKeep Calm and Power BI \[Breathing Exercise Vizzes\]](https://chandoo.org/wp/keep-calm-power-bi/)

[NextFind out if a number has repetitive digits \[formula homework\]Next](https://chandoo.org/wp/number-has-repetitive-digits-formula/)

### 4 Responses to “D’oh – Visualizing Homer’s favorite sayings in Power BI”

1.  ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
    
    [September 30, 2017 at 3:39 pm](https://chandoo.org/wp/doh-powerbi/#comment-1513142)
    
    Hmm, I noticed some Dutch in "https://chandoo.org/wp/resources/power-bi-play-date/". Any Kasper involved?
    
    [Reply](https://chandoo.org/wp/doh-powerbi/#comment-1513142)
    
2.  ![](https://secure.gravatar.com/avatar/d6f70e85d96966ced05da385f0badd58c0b194677f767aa3ed8c745fa97752f8?s=64&d=mm&r=g) Andrew Rickards says:
    
    [October 1, 2017 at 7:23 am](https://chandoo.org/wp/doh-powerbi/#comment-1513244)
    
    .
    
    [Reply](https://chandoo.org/wp/doh-powerbi/#comment-1513244)
    
3.  ![](https://secure.gravatar.com/avatar/46c8fa621b680e5d1d88df2cae5f8297ea83954cdc8b0380f3f2d59f53cb4936?s=64&d=mm&r=g) dilip says:
    
    [June 15, 2024 at 9:10 am](https://chandoo.org/wp/doh-powerbi/#comment-2223427)
    
    Pls can you add this Report as I need to view Formula used in report
    
    [Reply](https://chandoo.org/wp/doh-powerbi/#comment-2223427)
    
4.  ![](https://secure.gravatar.com/avatar/f44c30fda7b6241a136aefc88497a192ed641555af799c9a2bdc1a23c916bed4?s=64&d=mm&r=g) Shre says:
    
    [August 27, 2024 at 4:59 am](https://chandoo.org/wp/doh-powerbi/#comment-2275706)
    
    can you please provide the POWER BI file of this
    
    [Reply](https://chandoo.org/wp/doh-powerbi/#comment-2275706)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/doh-powerbi/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ