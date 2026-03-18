# Mutual Fund Tracker - Free Excel Template

**Source:** https://chandoo.org/wp/mutual-fund-tracker-excel

---

Track Your Mutual Fund Portfolio using Excel \[India Only\]
===========================================================

[excel apps](https://chandoo.org/wp/category/excel-apps/)
 , [personal finance](https://chandoo.org/wp/category/personal-finance/)
 - 94 comments

  

**Excel is very good for keeping track of your investments.** Due to its grid nature, you can easily create a table of all the mutual fund holdings and monitor the latest NAVs (Net Asset Values) to see how your investments are doing. A while back we have posted a file on [tracking mutual funds using excel](http://chandoo.org/wp/2008/04/18/mutual-fund-portfolio-tracker-using-ms-excel/)
. Today we are going to release an upgrade for that file.

**[Download the mutual fund portfolio tracker excel workbook](http://chandoo.org/img/d/MF%20Portfolio%20Tracker-%20India%20v3.0.zip)
 now.**

\[[Download Excel 2003 compatible version here](http://chandoo.org/img/d/MF%20Portfolio%20Tracker-%20India%20-xl2003%20v3.0.zip)\
\]

![Track Your Mutual Fund Portfolio using Excel](https://chandoo.org/img/c/mutual-fund-portfolio-tracker-excel.png "Track Your Mutual Fund Portfolio using Excel")

### How the Mutual Fund Portfolio Tracker Works?

*   **We use Excel Web Queries** (a powerful external data feature in excel) to get latest Mutual Fund NAVs for all the MFs in India. The list of funds along with their latest NAVs is published everyday at AMFI (The Association of Mutual Funds in India) at **[http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
    **
*   The data is delimited using ; as a separator, I have used some formulas (mainly [FIND](http://chandoo.org/excel-formulas/find.html "FIND Excel Formula - help and examples")
    , [MID](http://chandoo.org/excel-formulas/mid.html "MID Excel Formula - help and examples")
     and [LEFT](http://chandoo.org/excel-formulas/left.html "LEFT Excel Formula - help and examples")
     formulas) to split the text in to fund name and latest NAV.
*   I have used fuzzyText UDF (user defined formula) so that we can search against this list even when you have a spelling mistake in the fund name. For more information see [fuzzy text search using excel](http://chandoo.org/wp/2008/09/25/handling-spelling-mistakes-in-excel-fuzzy-search/)
    .
*   In the main portfolio sheet, **as soon as you type a fund name, we search against the list** to see if any fund matches the one you bought. At this point,  we use the fuzzyText UDF so that you can spell in anyway you want (as long as it closely matches with the fund name). Once a match is found, we show the latest NAV for that fund in the tracker worksheet. And of course, we [use VLOOKUP](http://chandoo.org/wp/2008/11/19/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
     to find the NAV.
*   Rest is easy, you can figure out between sips of coffee.
*   The file is protected, but there is no password. So go ahead and poke around it to learn how the whole thing works.
*   Even though the file works for Indian Mutual Funds only, you can easily build a similar model for US or UK or Any other country. All you need is a public source of fund data and a little web query.

### Changes from previous version

*   The formulas are more robust. Earlier version ([available here](http://chandoo.org/wp/2008/04/18/mutual-fund-portfolio-tracker-using-ms-excel/ "Mutual Fund Portfolio Tracker - Excel Template")
    ) has some limitations.
*   ~Selecting a fund is much more simpler. You need not scroll thru an insanely large in-cell dropdown. Instead, just type the fund name and thanks to fuzzyText UDF, the correct fund name will be found.~
*   I have updated the webquery properties, so that formulas get refreshed automatically.

**[Download the mutual fund portfolio tracker excel workbook](http://chandoo.org/img/d/MF%20Portfolio%20Tracker-%20India%20v3.0.zip)
 now.**

\[[Download Excel 2003 compatible version here](http://chandoo.org/img/d/MF%20Portfolio%20Tracker-%20India%20-xl2003%20v3.0.zip)\
\]

### What is your favorite way to track investments?

I rely my bank’s investment tracker tools to get a quick update on my mutual funds and shares. But I use excel to pull data from various sources and analyze it to optimize my portfolio. [Using excel’s financial formulas](http://chandoo.org/excel-formulas/financial-functions.html)
, I can easily find out  CAGR or IRR on my investments is and compare it with other options. I also compare my future needs against my current holdings to see if I need to invest more.

**What about you? What is your favorite way to keep track of investments?**

### Related Excel Templates and Articles on Personal Finance

*   [Find out how much you need for retirement using Excel Goal Seek](http://chandoo.org/wp/2009/07/29/excel-goal-seek-tutorial/)
    
*   [Why you should start saving early for your retirement](http://chandoo.org/wp/2007/04/04/start-early/)
    
*   [Tracking Stock Quotes and Other investments using Google Spreadsheets](http://chandoo.org/wp/2008/09/12/track-stock-mf-portfolio-google-docs/)
    
*   [Stock quotes in excel](http://chandoo.org/wp/2008/06/24/get-stock-quotes-in-excel/)
    
*   [Household Budget Templates – Free Download](http://chandoo.org/wp/2009/11/23/household-budget-spreadsheets/)
    
*   [More articles and howtos on personal finance using excel](http://chandoo.org/wp/tag/personal-finance)
    

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
| Written by Chandoo  <br>Tags: [CAGR](https://chandoo.org/wp/tag/cagr/)<br>, [concat](https://chandoo.org/wp/tag/concat/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [excel apps](https://chandoo.org/wp/tag/excel-apps/)<br>, [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)<br>, [find](https://chandoo.org/wp/tag/find/)<br>, [free](https://chandoo.org/wp/tag/free/)<br>, [fuzzy text searches](https://chandoo.org/wp/tag/fuzzy-text-searches/)<br>, [investment](https://chandoo.org/wp/tag/investment/)<br>, [IRR](https://chandoo.org/wp/tag/irr/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [left()](https://chandoo.org/wp/tag/left/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [mutual funds](https://chandoo.org/wp/tag/mutual-funds/)<br>, [NAVs](https://chandoo.org/wp/tag/navs/)<br>, [personal finance](https://chandoo.org/wp/tag/personal-finance/)<br>, [templates](https://chandoo.org/wp/tag/templates/)<br>, [udf](https://chandoo.org/wp/tag/udf/)<br>, [vlookup](https://chandoo.org/wp/tag/vlookup/)<br>, [web](https://chandoo.org/wp/tag/web/)<br>, [web queries](https://chandoo.org/wp/tag/web-queries/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 94 Responses to “Track Your Mutual Fund Portfolio using Excel \[India Only\]”

1.  ![](https://secure.gravatar.com/avatar/319efa6f24d45c8d622bb8ac435b43f7661ded6ac8b71c6a5792cba625687116?s=64&d=mm&r=g) [Vaibhav](http://technofriends.in/)
     says:
    
    [December 28, 2009 at 1:06 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89578)
    
    Hi Chandoo,
    
    Thanks for the update. I have been using your tracker and find it really cool. Could you elaborate on the update? What has changed/ what has been added?
    
    Cheers  
    Vaibhav
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89578)
    
2.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [December 28, 2009 at 2:41 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89585)
    
    @Vaibhav.. sorry for not being clear. I have added a new section to the above post mentioning some of the key changes to the template since earlier version.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89585)
    
    *   ![](https://secure.gravatar.com/avatar/ecfab4db31b8a086b568c4fd651d28c5b6e0b0918cc7f62a5d0fcd8a2d48e218?s=64&d=mm&r=g) Deb says:
        
        [November 12, 2014 at 10:01 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-846647)
        
        is this path still valid? [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
        . says page not found and the application is not able to retrieve data. What changes are to be done and how?
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-846647)
        
        *   ![](https://secure.gravatar.com/avatar/e4e88fc595be4712b0ea0049fbc8481fc5e4f691b80ae96307b3c42d709df2d1?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
             says:
            
            [January 4, 2018 at 8:48 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530720)
            
            Use this link [https://www.amfiindia.com/spages/NAVAll.txt](https://www.amfiindia.com/spages/NAVAll.txt)
            
            [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530720)
            
3.  ![](https://secure.gravatar.com/avatar/1c124f7de0561d0b5aea1a49a6930df317a1483907e1a9c2252e3cfcf372a259?s=64&d=mm&r=g) [Sachin](http://jokecricket.com/)
     says:
    
    [December 28, 2009 at 4:48 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89592)
    
    Hi Chandoo,
    
    Thanks for the updated file. I have also created a file to track my Shares with some graphs 🙂 but I was not able to pull data for Mutual funds.
    
    Thanks a lot again.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89592)
    
4.  ![](https://secure.gravatar.com/avatar/89db68f3db742cc020d1c1e35a1a85de3b3e45e9a6d9794e12cdb71a785c37fe?s=64&d=mm&r=g) srickant says:
    
    [December 29, 2009 at 1:46 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89633)
    
    Couple of things, dont know if you can pull out data but here goes:
    
    1) you need to calculate IRR s in addition to absolute gain/loss %
    
    2) you have to atleast show benchmark returns say sensex or the nifty, say annual. If you can show it for the same time period as of when you are holding the fund, thats the ideal 🙂 . And 30 year bond yield. (maybe you can just pull out 1 year returns of each of these from another source?. From current data its best to force benchmark ETF s in your file, row 3612)
    
    Cool interface. And sorry for the additional work 🙂
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-89633)
    
5.  ![](https://secure.gravatar.com/avatar/a93524fff286db949e164e67b5243ad4c2f8fd994e9c14a6a050f57077d12d88?s=64&d=mm&r=g) Mehul says:
    
    [January 12, 2010 at 7:33 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90725)
    
    Hi,
    
    Trying to use the excel sheet of Mutual fund tracker, but its not getting automaticaly refreshed and it says that automatic refresh fail also when i tried to insert my mutual fund the drop down list didnt come up, request you to please help me in using the excel sheet.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90725)
    
6.  ![](https://secure.gravatar.com/avatar/a93524fff286db949e164e67b5243ad4c2f8fd994e9c14a6a050f57077d12d88?s=64&d=mm&r=g) Mehul says:
    
    [January 12, 2010 at 7:33 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90726)
    
    Hi,
    
    Trying to use the excel sheet of Mutual fund tracker, but its not getting automaticaly refreshed and it says that automatic refresh fail also when i tried to insert my mutual fund the drop down list didnt come up, request you to please help me in using the excel sheet.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90726)
    
7.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 12, 2010 at 10:32 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90737)
    
    @Srickant... good points. I use the IRR analysis to see the fund performance all the time. I kept the sheet simple, but we can easily add the concept.
    
    @Mehul... Are you connected to internet? the file should refresh automatically. Also, there is no drop down. You have to type the name. Also, enable external connections and macros, otherwise the file wont work.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90737)
    
8.  ![](https://secure.gravatar.com/avatar/61fa6bcc5c32ea0dd6801e33ae105a675bc0eb37a646985b5741267e57e15579?s=64&d=mm&r=g) Mehul says:
    
    [January 13, 2010 at 6:52 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90807)
    
    Dear Chandoo, i am connected to Net all the time as i am using it from my office, i had tried writing the name too but it has not helped yet, request you to kindly mail me if possible the working file that you are using on my mail id [mehul.here@gmail.com](mailto:mehul.here@gmail.com)
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90807)
    
9.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 13, 2010 at 6:51 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90873)
    
    @Mehul... I am using the same version that is uploaded here and it is working fine for me. The file already has few fund names (as examples). You need to write the names of funds as listed in AMFI website (you can remove vowels or slightly mis-spell them). Also, check if you are able to visit this page from office... [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-90873)
    
10.  ![](https://secure.gravatar.com/avatar/09b0d8a1ece9d562569693028c2e0e1041178a7b116334c010e58c96aec8004c?s=64&d=mm&r=g) AK says:
    
    [February 12, 2010 at 1:14 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-93635)
    
    Hi Chandoo
    
    I liked your tracker.
    
    I have a question though. In the Portfolio Sheet, how have you restricted the navigation to go to cell M2 for example?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-93635)
    
11.  ![](https://secure.gravatar.com/avatar/446bb069b9ddbda95a05b2d132fc6be3dc593c363a94d7229108e0f2450164df?s=64&d=mm&r=g) Som says:
    
    [April 2, 2010 at 8:45 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-99510)
    
    Dear Chandoo,  
    How to track divident history, or ant redemption?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-99510)
    
12.  ![](https://secure.gravatar.com/avatar/e47fab372f2dbd14e99edb93ea52864441b43b42b240654421aef84e6c4dfc94?s=64&d=mm&r=g) kaps says:
    
    [November 17, 2010 at 5:19 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-141314)
    
    Dear Chandoo,
    
    How to keep a track of weekly dividend reinvestment funds( ICICI / UTI ) etc..weekly / fortnightly dividend reinvestment funds ?
    
    How to keep a track of returns based on varying NAV and weekly dividend reinvestment, over a large period
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-141314)
    
13.  ![](https://secure.gravatar.com/avatar/f797f65d01c40c387cd40659d084db93ebb35a98addd1fd8c0a8b3eea274035b?s=64&d=mm&r=g) mukund says:
    
    [December 2, 2010 at 7:34 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-146041)
    
    Hi Chandoo  
    I was using your MF potfolio since last 1 year version 2 now all of sudden start giving errors  
    (when i am enabling update) today i have again download new version 4 and started putting the name of fund  
    1\. its not allowing to copy paste from the nav sheet the name of funds  
    2\. when I enabled the update latast its giving the same error #value#
    
    Is there any prob ..........if not than can u please help me  
    bcoz I liked ur excel portfolio very much
    
    Thanks & Regards  
    Mukund  
    [rathimukund@rediffmail.com](mailto:rathimukund@rediffmail.com)
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-146041)
    
14.  [How To Analyse Mutual Fund Portfolio | Ranjan Varma's Blog](http://ranjanvarma.com/how-to-analyse-mutual-fund-portfolio/)
     says:
    
    [December 15, 2010 at 7:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-150000)
    
    \[...\] an excellent MS Excel workbook on tracking Mutual Funds from Chandoo’s Excel Blog: Link. You can easily create a table of all the mutual fund holdings and monitor the latest NAVs (Net \[...\]
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-150000)
    
15.  ![](https://secure.gravatar.com/avatar/8d56e35632c04c260f257e2a1689b8a8bb6f23c6c05c331a66c01002a39fe3c1?s=64&d=mm&r=g) [Ashish](http://clutterfrommymind.blogspot.com/)
     says:
    
    [December 27, 2010 at 10:04 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154615)
    
    Hi, Your Excel Tracker file gives bad/corrupted zip file. What's going on?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154615)
    
16.  ![](https://secure.gravatar.com/avatar/1c124f7de0561d0b5aea1a49a6930df317a1483907e1a9c2252e3cfcf372a259?s=64&d=mm&r=g) Sachin says:
    
    [December 27, 2010 at 1:24 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154672)
    
    When I type any name the pick list is not coming. what to do? I have already unprotected the sheet.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154672)
    
17.  ![](https://secure.gravatar.com/avatar/f797f65d01c40c387cd40659d084db93ebb35a98addd1fd8c0a8b3eea274035b?s=64&d=mm&r=g) mukund says:
    
    [December 27, 2010 at 1:28 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154674)
    
    Hi Chandoo  
    I was using your MF potfolio since last 1 year version 2 now all of sudden start giving errors  
    (when i am enabling update) today i have again download new version 4 and started putting the name of fund  
    1\. its not allowing to copy paste from the nav sheet the name of funds  
    2\. when I enabled the update latast its giving the same error #value#
    
    Is there any prob ……….if not than can u please help me  
    bcoz I liked ur excel portfolio very much
    
    Thanks & Regards  
    Mukund  
    [rathimukund@rediffmail.com](mailto:rathimukund@rediffmail.com)
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-154674)
    
18.  ![](https://secure.gravatar.com/avatar/66a68c7315026c91eb4ee555d8ac47c7c9a61b9d210f98d4914dfd5785c9c0bc?s=64&d=mm&r=g) Manish Ashok Nihal says:
    
    [December 29, 2010 at 5:38 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-155415)
    
    Chandoo you rock!
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-155415)
    
19.  ![](https://secure.gravatar.com/avatar/cf870074ea4e44325bd594f3a37c94f013858d8d2c2cbc2299db886e461bd3fc?s=64&d=mm&r=g) Nikhil says:
    
    [June 1, 2011 at 10:15 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-204064)
    
    Chandoo, this file clearly does not work. I am new to your site but get the feeling the files are not updated with details around how to resolve issues to get the file working.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-204064)
    
20.  ![](https://secure.gravatar.com/avatar/9d462ea7388c6faa916671a7900b2faaf9822d49fde71b998d0ea40284bb264e?s=64&d=mm&r=g) Mutual Fund Portfolio manager says:
    
    [July 30, 2011 at 7:12 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-207687)
    
    I have developed a Mutual Fund Portfolio Manager in Excel that maintains entire record of the investment and also gives annual rate of returns for each such investment. Any of your readers who desire to evaluate the Portfolio Manager may contact me at [sudhem65@rediffmail.com](mailto:sudhem65@rediffmail.com)
    . Thanks.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-207687)
    
21.  ![](https://secure.gravatar.com/avatar/ea58ca94a55f302679a3c13ca3d80879ad28d80fbf22194991d48235f044769e?s=64&d=mm&r=g) rajiv isaac says:
    
    [August 12, 2011 at 4:59 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-207941)
    
    Hi, am able to refresh the NAV list however while typing the fund names in the portfolio sheet the fund names do not come up. Is something amiss??
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-207941)
    
22.  ![](https://secure.gravatar.com/avatar/c5a83e3c43ce06d371285de373dd56bccb59a3f71f1a576baa5524656672f60a?s=64&d=mm&r=g) GauravS says:
    
    [October 14, 2011 at 12:03 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-209670)
    
    With Excel 2010 , it is not working. Even default funds are showing "#N/A". How to fix it?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-209670)
    
23.  ![](https://secure.gravatar.com/avatar/2aa0ec248e14963e30dff521348566893fc3912183a6998607940988e1a82f7e?s=64&d=mm&r=g) Nitesh Shivapooja says:
    
    [November 19, 2011 at 2:08 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-213154)
    
    Hi Chandoo,
    
    Very impressed with the stuff on this website.  
    i have been using the mf tracker and would like to add another table that logs the weekly nav so that i can judge its growth in a graph and compare to the index This will help me judge the performance of the fund.  
    Pls advice me on how do i add this.
    
    Thank you
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-213154)
    
24.  ![](https://secure.gravatar.com/avatar/897289840054378c757f727a54a9a1bf98c9c2be85d40fc95ed8381f06f21667?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
     says:
    
    [January 4, 2012 at 11:44 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-218980)
    
    NOT WORKING... 🙁
    
    Ex: sbi gold fund - growth plan is missing & not updating.....  
    Whenever the xls file is opened.... it gives error prompt "The following data rage failed to refresh: latestMFNavs Continue to refresh all?  
    When I click "OK".... nothing happens. 🙁
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-218980)
    
25.  ![](https://secure.gravatar.com/avatar/811450b9481756ef43aa63b7a087c5853b7a586ae7984d5138b85eb63b55f302?s=64&d=mm&r=g) Hemendra says:
    
    [January 5, 2012 at 7:18 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219020)
    
    Hey Chandoo,
    
    Came across your site and was pleasantly surprised.
    
    Awesome stuff this. Do you have a stocks portfolio tracker as well. I tried a couple of them earlier but none seem to work too well or were so cumbersome that going to Moneycontrol was easier.
    
    Would love to hear from you if you have a solution.
    
    Cheers,
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219020)
    
26.  ![](https://secure.gravatar.com/avatar/6158853e3092699a2a662604d3db9b8b32758856f8a5476be7c80ee609397348?s=64&d=mm&r=g) Radesh says:
    
    [January 11, 2012 at 4:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219258)
    
    Hi Chandoo, I have been using your MF portfolio tracker for several years without any issues. Last few days, the tracker is not working, I believe some changes in the AMFI data. Can you please check and help us on this.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219258)
    
    *   ![](https://secure.gravatar.com/avatar/897289840054378c757f727a54a9a1bf98c9c2be85d40fc95ed8381f06f21667?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
         says:
        
        [January 11, 2012 at 5:50 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219263)
        
        I've also reported the same thing on 4th jan...... haven't recieved any reply to it still..... 🙁
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219263)
        
27.  ![](https://secure.gravatar.com/avatar/b3b2b428e1b1384a120f9c3f090ad76a1396a56d4c9fab21534b0dc3a96bda36?s=64&d=mm&r=g) mohit says:
    
    [January 19, 2012 at 10:42 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219502)
    
    Even for me the same error is happening when I enable the data connection for fresh data \[as told by Radesh and gsvirdi\].
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219502)
    
28.  ![](https://secure.gravatar.com/avatar/899dd824ef80aa73fcf4709631584dbcfeb153093133cca6a490ca5d52d7b2fe?s=64&d=mm&r=g) Anand says:
    
    [January 26, 2012 at 9:06 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219706)
    
    i found the solution of it. I think recently there is some changes in AMFI's NAV file. they have added INE number with mutual fund scheme.  
    those who getting the error have to copy any paste below link into their Latest NAV's file in column E10. and drag the same upto the end of the column in entire sheet.
    
    \=IF(ISERROR(FIND(CHAR(171),SUBSTITUTE(B10,";",CHAR(171),3))),"",FIND(CHAR(171),SUBSTITUTE(B10,";",CHAR(171),3)))
    
    after doing this change your nav will be updated and it works nice.  
    If any body get any error pls write it here.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219706)
    
    *   ![](https://secure.gravatar.com/avatar/897289840054378c757f727a54a9a1bf98c9c2be85d40fc95ed8381f06f21667?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
         says:
        
        [February 6, 2012 at 8:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219991)
        
        Dear Aanad,  
        Still it's not working. Earlier the fuzzyText in Column E was finding the text value (like nf204k01471), but with this formula of ur's it is giving a neumerical output (like 22). I'm wondering how can it work???  
        With the existing Formula =IF(C10"",VALUE(MID(B10,C10+LEN(D10)+2,FIND(";",B10,C10+LEN(D10)+2)-C10-LEN(D10)-2)),"") it's giving an error #VALUE!
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219991)
        
    *   ![](https://secure.gravatar.com/avatar/897289840054378c757f727a54a9a1bf98c9c2be85d40fc95ed8381f06f21667?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
         says:
        
        [February 6, 2012 at 9:11 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219993)
        
        The above formuls should be replaced/overwritten in \[strong\]column C\[/strong\]...... As columns B & C are hidden by author so I was not able to find out the correct place for the formula.  
        Thx so much Anand for the solution, now the tracker file is working again.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219993)
        
29.  ![](https://secure.gravatar.com/avatar/7560ffe940d5d74e02d913bf70a1eb581c68363147237b70201ddf4e0e52f7bf?s=64&d=mm&r=g) Tarun says:
    
    [January 26, 2012 at 2:24 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219709)
    
    Sir,
    
    Using old version & satisfy with that , but currently in Jan-2012 its not working; Any help
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219709)
    
    *   ![](https://secure.gravatar.com/avatar/899dd824ef80aa73fcf4709631584dbcfeb153093133cca6a490ca5d52d7b2fe?s=64&d=mm&r=g) Anand says:
        
        [February 5, 2012 at 8:05 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219973)
        
        just follow my above post and your old file will work too.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-219973)
        
30.  ![](https://secure.gravatar.com/avatar/f37beba3405a4c71800110c36cc662dc24948c57b534dcb550a68db3226d23c3?s=64&d=mm&r=g) Varun says:
    
    [May 6, 2012 at 4:46 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223511)
    
    Hi, I have downloaded "MF Portfolio Tracker- India v3.0". I am not able to input the funds in the Portfolio Sheet in the file. I have to input funds like HDFC Equity/HDFC Tax Saver/Sundaram Tax Saver and other funds in which I have invested. I am not sure about the Fuzzy Text. Its not showing in the dropdown. I am using excel 2010.  
    Please help !!! 
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223511)
    
    *   ![](https://secure.gravatar.com/avatar/897289840054378c757f727a54a9a1bf98c9c2be85d40fc95ed8381f06f21667?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
         says:
        
        [May 7, 2012 at 4:15 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223536)
        
        Dear Varun,  
        It happens..... the fund name is there but still it does not appears in the cell. Manually searched from the sheet "NavPivot" and copy-paste the cell contents in the Portfolio Sheet.
        
        Plz forgive Excell, and Chandoo for this inconvenience 🙂
        
        GS Virdi.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223536)
        
31.  ![](https://secure.gravatar.com/avatar/f37beba3405a4c71800110c36cc662dc24948c57b534dcb550a68db3226d23c3?s=64&d=mm&r=g) Varun says:
    
    [May 7, 2012 at 7:58 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223539)
    
    Thanks Chandoo,
    
    I found the fund names in the dropdown..... Its little inconvenient but its working....  
    Thanks for the templete. Its really helpful.  
    Varun  
     
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-223539)
    
32.  ![](https://secure.gravatar.com/avatar/978bd88c7f51483942d325c889c8b0699d5ed32fb3bddb1f43a605b1daac27ce?s=64&d=mm&r=g) Ajay says:
    
    [August 28, 2012 at 6:21 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-229872)
    
    Thank you Chandoo,
    
    The file is a great way to track the investments. 
    
    One doubt...how to track SIP?
    
    Regards.
    
    Ajay 
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-229872)
    
33.  ![](https://secure.gravatar.com/avatar/593fea7d6adbc50e15c2e92358abedc0a03bf81f843371526fea19a9ef6ca0ab?s=64&d=mm&r=g) John says:
    
    [January 15, 2013 at 5:11 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-393377)
    
    Great Tool, since Jan 2013 started am not able to track the Fund "SBI MSFU CONTRA-DIVIDEND" in the excel. NAV is not found. Pl advice
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-393377)
    
34.  ![](https://secure.gravatar.com/avatar/b62d319b31c1cb6405c691116028e0ae7a9f04b192651a86bda0f63dea9cd0fc?s=64&d=mm&r=g) Rahul says:
    
    [May 21, 2013 at 10:03 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-431425)
    
    Very cool tool. Great work. Thanks
    
    Rahul
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-431425)
    
35.  ![](https://secure.gravatar.com/avatar/33da759bd5018796ab27830b1a1f6b3effe4439d2dd4f43bb59cfae294e8b222?s=64&d=mm&r=g) Satish Mistry says:
    
    [September 4, 2013 at 1:35 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-445047)
    
    I have developed Advance Mutual Fund Portfolio Tracker with Comprehensive report for Portfolio Valuation & Capital Gain Reports.  
    You can try it. Download link is here [http://goo.gl/fUclWU](http://goo.gl/fUclWU)
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-445047)
    
36.  ![](https://secure.gravatar.com/avatar/09ef0c2580a3ffc4382d77d67a3fe7139bf3b9062670cabe81697493e7f0c51a?s=64&d=mm&r=g) DILIP says:
    
    [October 1, 2013 at 12:44 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447663)
    
    I am using the the MF tracker India since long time and working very well, but since last 2 days it shows following error message.
    
    "Unable to open [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
    . The internet site reports that the item you requeted could not be found. http/1.0 404".
    
    Kindly update about what changes required to overcome with this problem?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447663)
    
37.  ![](https://secure.gravatar.com/avatar/77b1d1d576cb6367beddafb19f553022c871a313e1f87f780428fd13866af1b9?s=64&d=mm&r=g) Hiren says:
    
    [October 2, 2013 at 2:58 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447772)
    
    I am facing the same problem faced by Mr. Dilip. I am using MF tracker India since 2011 and working very well, but since last 2 days it shows following error message.
    
    “Unable to open [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
    ." NAV turns to "notfound" result.
    
    Please update what to do to resolve this issue?
    
    Thanks...
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447772)
    
38.  ![](https://secure.gravatar.com/avatar/33da759bd5018796ab27830b1a1f6b3effe4439d2dd4f43bb59cfae294e8b222?s=64&d=mm&r=g) Satish Mistry says:
    
    [October 2, 2013 at 7:37 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447801)
    
    Right now try on [http://www.portal.amfindia.com](http://www.portal.amfindia.com/)
    .
    
    It looks like, site is right now in modification mode. so, wait for some time. It's my personal understandings.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-447801)
    
39.  ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh says:
    
    [October 12, 2013 at 9:39 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-448908)
    
    Hi  
    For the past 10 days Mutual fund tracker is not working since web query refers [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
    . Now AMFII india had changed their web site address as [http://portal.amfiindia.com/spages/NAV0.txt](http://portal.amfiindia.com/spages/NAV0.txt)
      
    I am able to refresh Latest NAV excel sheet by changing the web link in Data Tab,how ever in Portfolio sheet drop down list i am getting values for few mutual fund details.  
    Need help on fixing this issue Can any body help in resolving this issue
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-448908)
    
    *   ![](https://secure.gravatar.com/avatar/09ef0c2580a3ffc4382d77d67a3fe7139bf3b9062670cabe81697493e7f0c51a?s=64&d=mm&r=g) DILIP says:
        
        [October 12, 2013 at 2:51 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-448926)
        
        Mr. Ramesh,
        
        Where do you find and change the web link : data tab?
        
        I am not even getting the same.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-448926)
        
40.  ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh says:
    
    [October 13, 2013 at 1:34 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-449037)
    
    Hi Dilip,  
    Follow this below steps  
    • In Excel sheet open Data Tab  
    • Click on Connections  
    • In the Pop up screen click on Properties  
    • One more pop up screen open in that select Definition Tab  
    • Currently the connection string refers to link [http://amfiindia.com/spages/NAV0.txt](http://amfiindia.com/spages/NAV0.txt)
      
    • Click on Edit Query, When you click on query in the next pop up screen you can able to see a new web page with address as [http://portal.amfiindia.com/spages/NAV0.txt](http://portal.amfiindia.com/spages/NAV0.txt)
      
    • Click on Import once it is done you can see the changes in Connection string refers to new web address.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-449037)
    
41.  ![](https://secure.gravatar.com/avatar/ae268ec97e8f47d5aa283898793c9ade088772afc507a123ecd3f379f71dad8a?s=64&d=mm&r=g) Dipanjan Dutta says:
    
    [October 18, 2013 at 6:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-449531)
    
    Dear Ramhesh  
    I have done what u have said but still it is not updating  
    Please solve this urgently
    
    Regards  
    Dipanjan
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-449531)
    
42.  ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh says:
    
    [November 13, 2013 at 8:01 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-454511)
    
    Hi,  
    After doing the necessary corrections on Web Query which i had updated on 13th Oct one more step is needed to get Data refresh automatically.  
    In NAV PIVOT sheet if you are seeing update for few mutual funds then you need to extend the formula in Latest NAV Sheet in Column R for Scheme Code for all the Mutual Funds as on date which is being updated in AMFII website. This step need to followed for all columns up to AJ  
    Currently the Mutual fund details are available till Row 14073
    
    Once i did the changes now i am able to use this excel sheet for tracking my Mutual Fund investment as before Sep 2013
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-454511)
    
43.  ![](https://secure.gravatar.com/avatar/ae268ec97e8f47d5aa283898793c9ade088772afc507a123ecd3f379f71dad8a?s=64&d=mm&r=g) Dipanjan Dutta says:
    
    [November 13, 2013 at 3:26 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-454630)
    
    Dear Ramhesh  
    Can u please send me the updated excel sheet it is still not working at my end I am not able to pick the MF scheme I want  
    Regards  
    Dipanjan
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-454630)
    
44.  ![](https://secure.gravatar.com/avatar/81685521bd9ec25c90cc4d8d4a10879e178330f205273031f71b055b8bbb27e8?s=64&d=mm&r=g) Vikas says:
    
    [November 15, 2013 at 10:58 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-455233)
    
    Hi,
    
    even i have tried all the changes as suggested by ramesh, bust still not working, dear ramesh can you upload the file, it will help a lot
    
    Thanks  
    Vikas
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-455233)
    
45.  ![](https://secure.gravatar.com/avatar/54ae0579659a8857168819ebe67c0cc140f7cb7cb8b56d1a3df9c53ecbb7d3b6?s=64&d=mm&r=g) Aejas Naik says:
    
    [January 2, 2014 at 6:30 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-463212)
    
    Hi Chandu,
    
    The tracker update doesn't work for year 2014. Can you help fix this?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-463212)
    
46.  ![](https://secure.gravatar.com/avatar/570c0c8766d0d8287c32cedbccfcfa0037fbe86cecf42d72117025e9e381d542?s=64&d=mm&r=g) kb sankaran says:
    
    [April 17, 2014 at 11:08 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-479290)
    
    Hi Chandoo,  
    I would also like to repeat the previous writer's request. Can we have the tracker fixed to work (in excel 2003)? . An extremely useful app but unfortunately not able to deploy it. Kindly do the needful.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-479290)
    
47.  ![](https://secure.gravatar.com/avatar/f395c2d9435d84c6bd4f4fb3b6bbb4fb2526265c99067cb3fd9cff1879ddf950?s=64&d=mm&r=g) Jayjit says:
    
    [June 3, 2014 at 8:15 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-548436)
    
    Hi Chandoo,  
    The mutual fund NAV sheet does not load proper. Any update sheet will be published.
    
    Thanks  
    Jayjit
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-548436)
    
48.  ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh says:
    
    [August 6, 2014 at 2:23 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-591702)
    
    Hi Chandroo  
    I am using Mutual Fund tracker for the past 3 years. I had modified the Web query and i am using the tracker efffectively. As few had requested to update the tracker i do not know how and where to upload the tracker  
    Can you please let me know wherer can this be done
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-591702)
    
49.  ![](https://secure.gravatar.com/avatar/dad88e5f287681ded59e3a1e539486ad471c5ae08918ca4cf833ce3359bba905?s=64&d=mm&r=g) Rupesh says:
    
    [September 11, 2014 at 8:34 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-719296)
    
    Hi Ramhesh,
    
    You may upload to google docs (or elsewhere) and provide the link here.
    
    Thanks
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-719296)
    
50.  ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh says:
    
    [September 21, 2014 at 6:38 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-761174)
    
    Hi  
    As requested access the MF tracker using below link
    
    [https://drive.google.com/file/d/0B8ydlEO\_ZjMyNWJUNEJtNmNHM3M/edit?usp=sharing](https://drive.google.com/file/d/0B8ydlEO_ZjMyNWJUNEJtNmNHM3M/edit?usp=sharing)
      
    Enjoy
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-761174)
    
    *   ![](https://secure.gravatar.com/avatar/7fa163da9f7ed58d474655e6b18e97a07000dd637c00b5febe540f11fad89491?s=64&d=mm&r=g) DILIP says:
        
        [December 1, 2016 at 5:36 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1356308)
        
        Thanks for uploading it on google drive.
        
        I have microsoft-2013 version.
        
        I have downloaded fresh application bu as soon as i open the file, it open the file disappears and new file open as new blanck sheet.
        
        please help to resolve the issue.
        
        Thanks already for your support.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1356308)
        
51.  ![](https://secure.gravatar.com/avatar/8dbcd8639c03ca30a9e2883303b2511679622cda30f96d8d727f8a4f08b717f5?s=64&d=mm&r=g) Venkat says:
    
    [August 2, 2015 at 7:17 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1017360)
    
    I think your wonderful programme no longer works because AMFI website says:  
    "You may not be able to locate the page you were looking for because of:
    
    An outdated bookmark/favorite  
    An outdated search engine listing  
    A miss-typed address  
    We regret the inconvenience.  
    Please click on [http://www.amfiindia.com](http://www.amfiindia.com/)
     to proceed to our home page."
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1017360)
    
52.  ![](https://secure.gravatar.com/avatar/6facc0e9ae7f4a3c26a8a79e6f3e90e328df7c96d99af39662d2d066e5f05e35?s=64&d=mm&r=g) [Sitegar](http://www.facebook.com/profile.php?id=100003469639351)
     says:
    
    [November 25, 2015 at 4:20 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1088743)
    
    I strongly agree with u. HKICPA is only a "Big-4" piatrve entertainment club. How many things they have done to us? Their fees can be covered by their Company. Therefore, they have no feeling towards any increment. And we are only a small potato. Compared with other professionals such as engineers, their annual fee is only a few hundred. Why so great difference. Why we need to pay for HK$12,500 for a sole proprietorship?Why they need to hire 200 staffs? The Society of Chinese Accountants & Auditors only hired a few staffs. SCAA has done a lot of things to us such as many reasonable price seminars, members' forum and free Annual Dinner. The contents of SCAA's seminars are better than HKICPA. Therefore, HKICPA has done a lot of "Pretty Dame Good" things to us. It is not reasonable to increase the price to us. If Big 4 is generous enough, please asks them to donate to HKICPA individually. They enjoy the facilities much more than us.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1088743)
    
53.  ![](https://secure.gravatar.com/avatar/4d33246451fc3095573540a19ae196e6377f1008f18bad148718fb40fcc4b6a5?s=64&d=mm&r=g) Jeetesh says:
    
    [April 26, 2016 at 2:26 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1175489)
    
    Dear Chandoo ,
    
    The template attached in this link is not working properly , when i download and open the file , it ask for enable editing permission. Once i give enable editing data in the Latest NAV updates sheet is getting disappeared. Kindly help me on this .
    
    Thank you in advance.
    
    Best Regards,  
    Jeetesh Jain
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1175489)
    
54.  ![](https://secure.gravatar.com/avatar/98fbd49fb20645dd63ebf7f4dbe170740c4df8a2c16ce15774c807b437088dc2?s=64&d=mm&r=g) Amol says:
    
    [December 10, 2016 at 10:57 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1363454)
    
    Dear chandoo
    
    Please reply we are facing lots of errors in this portfolio.  
    like link is not working properly
    
    we are eager to know about this.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1363454)
    
55.  ![](https://secure.gravatar.com/avatar/c00717a7f55b19dca7a192113298d28d3fa28cd49892bc28cf0fefc05935858a?s=64&d=mm&r=g) [Pranshu](https://www.simplemoney.in/)
     says:
    
    [January 4, 2017 at 5:05 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383644)
    
    Dear all - in case it is helpful, I have built a simple web-based portfolio tracker for mutual funds that takes just five clicks to setup. Here is a link to it:  
    [https://www.simplemoney.in/](https://www.simplemoney.in/)
    
    It works by finding the mutual fund investments you have made through your email. I got quite frustrated while using excel sheets and similar tools to track my portfolio, so I built this to automate the process and help others as well!
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383644)
    
    *   ![](https://secure.gravatar.com/avatar/9ae48699a8cef8b37c59e38115ba07979d7fe2a50d33deed09b84242d90945b1?s=64&d=mm&r=g) Ramhesh Babu RD says:
        
        [January 4, 2017 at 11:53 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383746)
        
        Thank you for sharing the details. I had checked this web based portfolio tracker.  
        It is really good and amazing report which you had developed.
        
        Will it be possible to enhance this tool with down load option of reports.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383746)
        
        *   ![](https://secure.gravatar.com/avatar/c00717a7f55b19dca7a192113298d28d3fa28cd49892bc28cf0fefc05935858a?s=64&d=mm&r=g) [Pranshu](https://www.simplemoney.in/)
             says:
            
            [January 4, 2017 at 4:30 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383829)
            
            Thanks for the kind words and for using the tracker!
            
            I can add a download option for the data, but could you tell me what you want to download the data for? If it is to do some calculations, maybe I can make it easier for you and just add the calculations to the tracker directly so that it is faster.
            
            [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1383829)
            
            *   ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) [Anil](http://primebankindia.com/)
                 says:
                
                [May 11, 2017 at 11:00 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1446757)
                
                Dear Guys  
                Final Solution as below  
                to open DATA tab window  
                then press Connection  
                then open new window select workbook window select connection as seen  
                open properties  
                select definition then Edit Query  
                then pest below mentioned link in address  
                [http://www.amfiindia.com/spages/NAVAll.txt](http://www.amfiindia.com/spages/NAVAll.txt)
                  
                then save
                
                [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1446757)
                
56.  ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) Anil says:
    
    [April 27, 2017 at 11:21 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440792)
    
    I am using MS office 2013 please help to run worksheet in the version
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440792)
    
57.  ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) Anil says:
    
    [April 28, 2017 at 8:26 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440996)
    
    [https://www.amfiindia.com/spages/NAVAll.txt?t=28042017015246](https://www.amfiindia.com/spages/NAVAll.txt?t=28042017015246)
     page where i modify in tour tracker
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440996)
    
58.  ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) Anil says:
    
    [April 28, 2017 at 8:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440997)
    
    [https://www.amfiindia.com/spages/NAVAll.txt?t=28042017015246](https://www.amfiindia.com/spages/NAVAll.txt?t=28042017015246)
     page where i modify inportfolio tracker v3.0
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1440997)
    
59.  ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) [Anil](http://primebankindia.com/)
     says:
    
    [May 11, 2017 at 10:59 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1446755)
    
    Dear Guys  
    Final Solution as below  
    to open DATA tab window  
    then press Connection  
    then open new window select workbook window select connection as seen  
    open properties  
    select definition then Edit Query  
    then pest below mentioned link in address  
    [http://www.amfiindia.com/spages/NAVAll.txt](http://www.amfiindia.com/spages/NAVAll.txt)
      
    then save
    
    Please Copy below mentioned link
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1446755)
    
    *   ![](https://secure.gravatar.com/avatar/d14d635ed61d04a2202d6f270e56e015209ccbf69431d9c3fa95db3f20a6f3e6?s=64&d=mm&r=g) Kalx says:
        
        [December 14, 2017 at 3:50 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1527514)
        
        Hi,
        
        Even this is not working. Its displaying the list till "Canara Robeco Mutual Fund" only
        
        Cheers,  
        Kalyan
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1527514)
        
60.  ![](https://secure.gravatar.com/avatar/5f387a3ef22cb4b483f12ecd81c7055dc5c59da7a55012371fb78c7f41b54782?s=64&d=mm&r=g) Tejaswi says:
    
    [January 4, 2018 at 7:29 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530708)
    
    This tool is not working anymore as the [http://www.amfiindia.com/spages/NAV0.txt](http://www.amfiindia.com/spages/NAV0.txt)
     is not found anymore.  
    Do you have an alternate solution?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530708)
    
    *   ![](https://secure.gravatar.com/avatar/e4e88fc595be4712b0ea0049fbc8481fc5e4f691b80ae96307b3c42d709df2d1?s=64&d=mm&r=g) [gsvirdi](http://virdigs.blogspot.com/)
         says:
        
        [January 4, 2018 at 8:51 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530721)
        
        Use this link instead..... [https://www.amfiindia.com/spages/NAVAll.txt](https://www.amfiindia.com/spages/NAVAll.txt)
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530721)
        
        *   ![](https://secure.gravatar.com/avatar/5f387a3ef22cb4b483f12ecd81c7055dc5c59da7a55012371fb78c7f41b54782?s=64&d=mm&r=g) Tejaswi says:
            
            [January 4, 2018 at 9:03 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530724)
            
            Thanks. That link works. Let me update
            
            [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530724)
            
61.  ![](https://secure.gravatar.com/avatar/07e975a8c365391c7dff515a7651600faed059b80c5755679e7ae61cdf0b7ce9?s=64&d=mm&r=g) Anil says:
    
    [January 4, 2018 at 8:31 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530716)
    
    Go to amfi website and open complete NAV download option and copy the  
    link and pest at connection
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1530716)
    
62.  ![](https://secure.gravatar.com/avatar/437b74920afcd0491be549f94c3250906e47ba3387d996fbf4274c9f5e1a54a8?s=64&d=mm&r=g) Tushar Kadam says:
    
    [August 31, 2019 at 11:37 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1682727)
    
    Hi Chandoo,  
    I have problem in Portfolio Sheet  
    Column H7 is not working - NAV not showing there only Notfound shows.
    
    in formula FUND\_NAVS AND argument of 2 but i do not find out where is the range of FUND\_NAVS.
    
    Please suggest.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1682727)
    
63.  ![](https://secure.gravatar.com/avatar/b6f4d0e8217252f0b7a276ba487d57a348ca5123cfa5ee95048e8ddd654fe42f?s=64&d=mm&r=g) Dhaval says:
    
    [November 26, 2019 at 2:47 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1716677)
    
    How to input and manage the units sold?. and its analysis and impact ?
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1716677)
    
64.  ![](https://secure.gravatar.com/avatar/8dfd4e9ff1500b43a9bd468a1bc747e60408d58abe71fa95d07a8e1062487570?s=64&d=mm&r=g) Abhinay Sharma says:
    
    [April 3, 2020 at 6:46 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1771061)
    
    First of all thanks for the Superb Tracker. I just set it up and added all my funds. It is working fine except the NAV of ICICI Prudential Mutual Fund is not getting updated since last two days.
    
    Please help.
    
    Thanks a lot in advance.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1771061)
    
65.  ![](https://secure.gravatar.com/avatar/24d0780eefa4d08d8240c866332112ddb9e3bcb26e6dbb76007110796e43c496?s=64&d=mm&r=g) Sanjeev Kumar says:
    
    [February 28, 2021 at 2:51 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1978734)
    
    Hi Chandoo,  
    It is an awesome excel sheet to track my mutual funds investment. It works quite well for me, I have just added a pivot table for the creating report and easily tracking my total investment (SIPs, Lumpsum buy) for a particular fund basis.  
    Thank you for creating such useful excel sheet.
    
    In the prsent sheet you have added a column for calculating the CAGR, this gives a return on yearly basis.
    
    I request to add the feature to see the overall CAGR (ie. XIRR) for a particular fund bought in SIP or Lumsump. This feature will make the your excel sheet more useful and versatile.  
    Thanks in advance.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1978734)
    
66.  ![](https://secure.gravatar.com/avatar/85763d9a5494bf5f119731270d7d518a904bea39610f1e63187181515ba5f423?s=64&d=mm&r=g) Hareesh Krishnan says:
    
    [April 28, 2021 at 6:26 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1996251)
    
    How to track redemption in this sheet
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-1996251)
    
    *   ![](https://secure.gravatar.com/avatar/42e113247bb41465adf0426ebd5d27d05d63370bac2f8236bae48ddfc07851ab?s=64&d=mm&r=g) Ashok Kumar says:
        
        [May 22, 2021 at 5:14 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2001860)
        
        I have been trying to figure out that. This sheet is very useful no doubts, but being able to track the partial redemption or withdrawal is its limitation.
        
        I have been a huge fan of Chandoo's works, waiting for him to help us in this.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2001860)
        
67.  ![](https://secure.gravatar.com/avatar/2a253615f627cf3a8e065f0d905193ef0bde34f015e59ec1172c8c6a553baeb4?s=64&d=mm&r=g) Saravanan says:
    
    [August 20, 2021 at 2:50 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2022437)
    
    Hi Chandoo
    
    I am using Excel 2007 (I know its outdated, but not able to get the latest version). The MF tracker is not working and it says the below
    
    "  
    Initialization of the data source failed.
    
    Check the database error or contact your database administrator. Make sure the external database is available, and then try the operation again. if you see this message again, create a new data source to connect to the database  
    "
    
    Appreciate the help !!!
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2022437)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 22, 2021 at 6:53 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2022810)
        
        Hi Saravanan... This doesn't work with Excel 2007. I suggest using an online tracker from a personal finance website.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2022810)
        
68.  ![](https://secure.gravatar.com/avatar/ef65cf0e3df395e56a66dccc54fe82d5b15254adec462eb07cce0524b3c8398c?s=64&d=mm&r=g) Nikhil says:
    
    [September 13, 2021 at 5:41 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2028253)
    
    Hello Sir,  
    I recently downloaded the excel and entered the Funds .  
    I wanted to understand how to update the SIP month on month for all the funds? should it be done manually?  
    Any option where according to the date given, the month on month deposit amount + the no of units add , automatically?
    
    am a novice here....so pardon me if i may be asking something out of context
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2028253)
    
69.  ![](https://secure.gravatar.com/avatar/ff60c1f58b7ebe128b1f730c666dccc37e3059b84891f213e1d8b9fa73c65b71?s=64&d=mm&r=g) Pinak says:
    
    [January 17, 2022 at 5:25 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2065448)
    
    Hello Chandoo,
    
    I am not able to download the file using your link?
    
    can you please help?
    
    Reference to link: Download the mutual fund portfolio tracker excel workbook now.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2065448)
    
70.  ![](https://secure.gravatar.com/avatar/890c9f6ef0b2f45cab456b5d5712861a4b0aa9d58ad79ce80cb4fd3a657d9c19?s=64&d=mm&r=g) SM says:
    
    [August 24, 2022 at 3:55 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2086899)
    
    Download link is not working.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2086899)
    
71.  ![](https://secure.gravatar.com/avatar/2f7cb6c4fd72ffd7302faaabeb388ac317b469b384fe0a4b0ecd161c3d305b62?s=64&d=mm&r=g) Rajesh Thakkar says:
    
    [January 11, 2023 at 5:55 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2118890)
    
    Download link for latest version is not working.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2118890)
    
72.  ![](https://secure.gravatar.com/avatar/104b87879798c0234cb2222fbfce320f9e5ed97ba0eff632a2af0f25d50315c6?s=64&d=mm&r=g) Raminder says:
    
    [December 11, 2024 at 2:27 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2326582)
    
    Hi Chando, thanks for doing this. I have one request, can you show us how to historical values of our individual/total portfolio to track its performance with the benchmark?
    
    Again, thanks for your help.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2326582)
    
73.  ![](https://secure.gravatar.com/avatar/8430595a4eb9ee5c59c93931ec43b81d08148961539b058dbc905879fb30b5b1?s=64&d=mm&r=g) Gopi says:
    
    [January 2, 2025 at 4:50 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2337846)
    
    Thank you very much. I wanted to create a MF tracker and ran into your excel tracker. I simply used this, and updated the NAV link and it worked beautifully.
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2337846)
    
74.  ![](https://secure.gravatar.com/avatar/2d8f8ffa76bd5a190cb6b03e175686ab313c7aa705153b5049811f17668b3b4b?s=64&d=mm&r=g) Ella says:
    
    [July 23, 2025 at 12:23 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2424887)
    
    Hi Chando, thanks for this gem.  
    I've recently noticed the AMFI links are not available for the spreadsheet to access, could you advise if there are any updates available for the file to continue tracking with another site. Or if AMFI has come up with a new link to update ?
    
    Would be a great help if you had any advise. And all the best on the fitness journey !!!
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2424887)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [July 24, 2025 at 6:12 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2425305)
        
        You are welcome. AMFI site has been down for a few months now. Looks like they are no longer operating. I will keep an eye out for another source of fund values and if I come across one, I will update the workbook.
        
        [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2425305)
        
        *   ![](https://secure.gravatar.com/avatar/bd76f12fa14909678d5ba014ec7f8378ce160f399bb1b7c826f18f30d8b9c199?s=64&d=mm&r=g) Ashwin says:
            
            [November 5, 2025 at 4:18 pm](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2496762)
            
            I am an investor , I heavily invest in MF and stocks , I have developed my own google sheet , which downloads the whole amfi file each days and updates the nav of each of my holding  
            I have used google script and triggering to ensure I donot have to do any work on day to day basis  
            It works well , my sheet gives me nav, nav table for each day , highest and lowest returns, each day change and perctage gain wef April 1 every day  
            I am a SR Cit , not professional , but have managed till this point
            
            [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2496762)
            
75.  ![](https://secure.gravatar.com/avatar/5c96e936291f2ccc3788f3076f98c6343ec627ebbef02dcbf65b48e9528aa97b?s=64&d=mm&r=g) Simon says:
    
    [December 22, 2025 at 5:33 am](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2533366)
    
    Hi Chandoo,  
    I tried the download link but it doesnt seem to be working?
    
    Cheers
    
    Simon
    
    [Reply](https://chandoo.org/wp/mutual-fund-tracker-excel/#comment-2533366)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/mutual-fund-tracker-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to Find Dates of Public Holidays using Excel](https://chandoo.org/wp/public-holidays-excel-dates/) | [Best of Pointy Haired Dilbert – 2009](https://chandoo.org/wp/best-of-pointy-haired-dilbert-2009/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)