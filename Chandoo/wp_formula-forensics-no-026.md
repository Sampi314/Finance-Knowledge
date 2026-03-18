# Highlight Only the Duplicate Entries in an Excel range

**Source:** https://chandoo.org/wp/formula-forensics-no-026

---

Formula Forensics No. 026 – Highlight Only Duplicate Entries
============================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 20 comments

  

Last week I received an email from Chandoo.org reader, **Debra**.

“I have a formula that I think would be a good idea for a future formula forensics post, and also I’ve always wondered how it works. 

I know how to use it and use it often, but I’m not really sure how it actually works.  (I found it years ago on a Microsoft Office website.)”

Debras formula is:

\=COUNTIF($B$3:$B3, B3)>1

So today at Formula Forensics we will look at this formula and see what makes it tick as well as looking at a small extensions Debra might be interested in using.

As always at Formula Forensics you can follow along using a Worked Example which you can [Download here: Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/08/Debs-Duplicates.xls "Deb's Duplicates")
.

Debras Formula
--------------

Debras formula \=COUNTIF($B$3:$B3, B3)>1 uses the Excel Countif() function to count the occurrence of a value in a range.

The Countif() function has the following syntax:

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/DD01.png "DD01")](https://chandoo.org/wp/wp-content/uploads/2012/08/DD01.png)

So the Countif() function counts the number of occurrences of the Criteria in the Range

In Debra’s example: \=COUNTIF($B$3:$B3, B3)>1

**Range**: $B$3:$B3

**Criteria**: B3

Looking at Debras formula it looks like the formula is looking to see how many times the value in Cell B3 occurs in the Range $B$3:$B3, which of course is one as the range only includes B3

The formula then compares the number of times the value occurs with the number 1 using the **\>1** logic at the end of Debras formula and returns True if the count is greater than 1 and False if it isn’t

\=COUNTIF($B$3:$B3, B3)>1 is equivalent of using =If(COUNTIF($B$3:$B3, B3)>1, True, False)

You can see that Excel does the If and conversion to a Boolean automatically.

The clever part of the formula is the use of the Relative/Absolute Range Modifiers, the **$** signs.

The $ signs in the formula =COUNTIF($B$3:$B3,B3)>1, serve to lock the start position of the range so that when it is copied down the range increases in size as it is copied down

The original Formula =COUNTIF($B$3:$B3, B3)>1

references cell B3

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex1.png "Ex1")](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex1.png)

When we copy the cell C3 down to C4, the formula now becomes:

\=COUNTIF($B$3:$B4, B4)>1

We can see that the Countif() function is now counting how many times the value in **B4** occurs in the extended range **B3:B4** and if it is greater than 1 it will return TRUE

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex2.png "Ex2")](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex2.png)
  
When we copy the cell C4 down to C10, the formula now becomes:

\=COUNTIF($B$3:$B10, B10)>1

We can see that the Countif() function is now counting how many times the value in B10 occurs in the extended range B3:B10 and if it is greater than 1 it will return TRUE

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex3.png "Ex3")](https://chandoo.org/wp/wp-content/uploads/2012/08/Ex3.png)

Finally resulting in a table of True/False highlighting the Duplicate Status of each entry:

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/EX4_2.png "EX4_2")](https://chandoo.org/wp/wp-content/uploads/2012/08/EX4_2.png)

Debras Formula Extended
-----------------------

A good aspect of having a Table of TRUE/FALSE is that you can use it with a number of excel functions to trigger them. One of the more useful features of Excel is Conditional Formatting.

Conditional Formatting can rely on a cell formula returning True/False to trigger whether it displays the cell using the Conditional Formatting or not.

Lets see how:

Select the Duplicate area C3:C12

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex5.png "ex5")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex5.png)

On the Home Ribbon got **Conditional Formatting**, **New Rule**

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex6.png "ex6")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex6.png)

The following Dialog box appears, we are going to add Two New Rules

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex7.png "ex7")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex7.png)

Press **New Rul**e

In the **New Formatting Rule** dialog select **Use a Formula to determine which cells to format**

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex8.png "ex8")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex8.png)

In the Format values where this formula is true: type **\=C3**

This will apply the Conditional Formatting shown in the Preview: window when the value in cell C3 is True, in our case when it is a Duplicate

**Hint:** Don’t worry about the other cells in our Range C3:C12, Excel will adjust the Conditional Formatting accordingly for those cells

Select the Format Button and set a Red & Bold Font (or whatever else you want)

Ok When Done

Excel shows us the first Conditional Formatting rule

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex9.png "ex9")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex9.png)

We now add a second Conditional Formatting rule using the New Rule button

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/EX10.png "EX10")](https://chandoo.org/wp/wp-content/uploads/2012/08/EX10.png)

In the Format values where this formula is true: type **\=Not(C3)**

This will apply the Conditional Formatting shown in the Preview: window when the value in cell C3 is not True ie: is False, in our case when it is not a Duplicate

Select the Format Button and set a White Font (or whatever else you want)

**Hint**: Because we have used a White Font on a White Cell background color it will appear that the cell is blank, Don’t worry It isn’t

Ok When Done

Excel shows us the two Conditional Formatting rules

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex11.png "ex11")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex11.png)

Once we press Apply or Ok, Excel will apply the Conditional Formatting rules to our selected cells

[![](https://chandoo.org/wp/wp-content/uploads/2012/08/ex12.png "ex12")](https://chandoo.org/wp/wp-content/uploads/2012/08/ex12.png)

You can see that the False cells above have a White Font on top of a White Background?

You don’t believe me, select some of the blank cells and change the background color!

Try changing a few cells in Column B to your own values to check that the Conditional Formatting rules are being applied correctly

Download
--------

You can download a copy of the above file and follow along, [Download Here – Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/08/Debs-Duplicates.xls "Deb's Duplicates")
.

Formula Forensics “The Series”
------------------------------

This is the 26th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "The Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share with us all, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained as Debra did above, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "Hui")
 or [Chandoo](http://chandoo.org/wp/contact/ "Contact Chandoo")
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
| Written by Hui...  <br>Tags: [Coutif()](https://chandoo.org/wp/tag/coutif/)<br>, [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 20 Responses to “Formula Forensics No. 026 – Highlight Only Duplicate Entries”

1.  ![](https://secure.gravatar.com/avatar/39bc48a47d605978740d76b63cc0f856b06c56e9271608bf126ff7b1640e9acf?s=64&d=mm&r=g) Ram Kapoor says:
    
    [August 9, 2012 at 9:24 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228577)
    
    Hi Debra,
    
    Thanks for your post!
    
    We can get the same results without applying Conditional Formatting also. Here is the formula.
    
    \=IF(COUNTIF($B$3:$B3,B3)>1,COUNTIF($B$3:$B3,B3)>1,"")
    
    Regards,  
    Ram
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228577)
    
2.  ![](https://secure.gravatar.com/avatar/39bc48a47d605978740d76b63cc0f856b06c56e9271608bf126ff7b1640e9acf?s=64&d=mm&r=g) Ram Kapoor says:
    
    [August 9, 2012 at 9:28 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228578)
    
    Hi Debra,
    
    Thanks for your post!
    
    I observed, this can be done without applying Conditional Formatting also, here is the formula.
    
    \=IF(COUNTIF($B$3:$B3,B3)>1,COUNTIF($B$3:$B3,B3)>1,"")
    
    Regards,  
    Ram
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228578)
    
    *   ![](https://secure.gravatar.com/avatar/24094a8a2795807c57a9c353fdbc27ae49b03fbefaf055ecd608bbde73784b81?s=64&d=mm&r=g) Shadow Jam says:
        
        [August 9, 2012 at 10:13 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228583)
        
        Would it not be easier to use?
        
        \=IF(COUNTIF($B$3:$B3,B3)>1,True,”")  
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228583)
        
3.  ![](https://secure.gravatar.com/avatar/d112b983bfb331500bf2b717bc8e886fbf616e360ae4d4bbddba8ac5a6c0b863?s=64&d=mm&r=g) Manna Das says:
    
    [August 9, 2012 at 11:44 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228592)
    
    Dear Ram,
    
    your answer was helpful, but if we use that we won't be able to identify first occurance of duplicates   
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228592)
    
    *   ![](https://secure.gravatar.com/avatar/7181e339ba2d6299d074872612097feea78d2d1e056f585eb81f7497ea468260?s=64&d=mm&r=g) tadovn says:
        
        [August 9, 2012 at 1:43 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-228600)
        
        @Manna, it could be done.  
        Named the range of value DIR is RANGE1, ex.  
        So the formula will be:  
        \= IF(Countif(RANGE1,B3)>1,"TRUE","").  
           
        It will show all duplicates and more.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228600)
        
4.  ![](https://secure.gravatar.com/avatar/18bebb259a5e0b8dfbdfe8e49715e6846819865c3d39b4f2229e0eddfec87fc7?s=64&d=mm&r=g) Nick aka Trader273 says:
    
    [August 9, 2012 at 3:39 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-228607)
    
    Always something new to learn.  I personally like going the conditional formatting route, less "helper columns", but I suppose both ways work well.  Also, kind of off topic, but when I enter a formula in the conditional formatting and hit "OK", it seems xl automatically puts quotes around it, resulting in nothing happening. I can go in and delete them out and then the formula works.  Not sure why it's doing that, though not a huge deal.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228607)
    
5.  ![](https://secure.gravatar.com/avatar/4e03d6bc27a49f4dd68a52a9aef882ac746eb50cc32927fea0d83d11008c04bf?s=64&d=mm&r=g) Felicia says:
    
    [August 9, 2012 at 4:29 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-228609)
    
    this is helpful but what if you want all the duplicates and the original to be highlighted or selected. if i am trying to remove 'MATCHES" i currently have to sort by account number and remove both rows, how can i do that with a formula?
    
    IE,, row  3, 6 and 9 all match and i need to delet all 3,, right now i sort by account number and then delete all 3 rows, with this formula, i can delete the TRUE but it leaves the original false....  
    thanks
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228609)
    
    *   ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
        
        [August 10, 2012 at 1:48 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-228661)
        
        Change the formula to just:  
         **\=countif(C1:C10,C1)>0** And now you can delete the original and the duplicates.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228661)
        
6.  ![](https://secure.gravatar.com/avatar/ea471fc5bfd7d966039793b41640d3138a9bb6a85f44172ec2a1191ebc58dfc6?s=64&d=mm&r=g) Jonathan Micael says:
    
    [August 9, 2012 at 5:10 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-228611)
    
    Hoo dude... Long time ago I search this form... Thanks a lot! I really apreciatte your website!
    
    See ya. 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228611)
    
7.  ![](https://secure.gravatar.com/avatar/a57ecfffc12098ebbdfc5993d2208b918ddc8d447ce23331e9b8443b6f7eb144?s=64&d=mm&r=g) Ramki says:
    
    [August 10, 2012 at 1:52 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228621)
    
    Hi!!,  
    Add to this , if you want to identify and remove duplicate values in a range i.e. C1:C10, use **\=countif(C1:C10,C1)>1**. Go for absolute reference if you want to delete existing values also. This formula gives True/False, select True, press delete.  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228621)
    
8.  ![](https://secure.gravatar.com/avatar/37910ac7132149b6e4fb971c776418c9e0cf32a67198422c7397ba0b2a6bbdef?s=64&d=mm&r=g) md says:
    
    [August 10, 2012 at 6:20 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228625)
    
    Hi Chandoo,
    
    Conditional formatting is always a first option when we think of finding duplicate with clear reporting the data in issue.  
    Thanks to Debra for putting this solution on Chandoo.
    
    Well, I would like to request extension to the extension what you have did.  
    Now since we got to know that Duplicate record is found;  
    1\. I want to see how many times this record appeared  
    2\. If any colour formatting to source data to identify duplicates as a group? 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228625)
    
9.  ![](https://secure.gravatar.com/avatar/7e4bbe28731d39a97ec7b0d1213a910e1d60d324b4a8c08001438da330c4378a?s=64&d=mm&r=g) Mark says:
    
    [August 10, 2012 at 7:59 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228634)
    
    Hi Chandoo,
    
    I think I am missing something here?
    
    Why not use the Conditional Formatting to show the duplicate values (in the screenshots its the rule above the one you use in this example). I think it works really well, as it shows you the origoinal and all the values that are duplicated (in this example, the TRUE is only assigned to the any duplicates but not the original).
    
    Why are you creating the helper column?
    
    Ramki - there is also a function on the Data Ribbon to remove duplicates.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228634)
    
10.  ![](https://secure.gravatar.com/avatar/a57ecfffc12098ebbdfc5993d2208b918ddc8d447ce23331e9b8443b6f7eb144?s=64&d=mm&r=g) Ramki says:
    
    [August 10, 2012 at 8:26 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-228635)
    
    Hi! Mark!!  
    Yeah.. I am aware of the tip in excel 2007. But the above tip is handy in excel 2003.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-228635)
    
11.  ![](https://secure.gravatar.com/avatar/2a5af47c92104c0454dc7c9cb60d57abe5cf0f19cb12ec46c4222801aedffec7?s=64&d=mm&r=g) julien says:
    
    [August 22, 2012 at 9:54 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-229139)
    
    To go a little bit further, is it possible with formula only, when a duplicate is found, to find at which line the other duplicates is ?  
       
    Thanks,
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-229139)
    
12.  ![](https://secure.gravatar.com/avatar/64bbf7b8ede34180dd757ffd3a9d51c44f8e676080c764bb25cdca1a06bb6025?s=64&d=mm&r=g) SMA Quadri (Pakistan) says:
    
    [October 21, 2013 at 1:12 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-449895)
    
    I apreciatte your website
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-449895)
    
13.  ![](https://secure.gravatar.com/avatar/dbbd983a7e1d6d6aac2729a95fe6e21aff7c97d9f0e2a79eb7a4ace8ac52c125?s=64&d=mm&r=g) David says:
    
    [November 16, 2013 at 5:49 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-455630)
    
    Can finding duplicates with conditional formatting only be done if all the items are listed in a single column? In other words, how would I find duplicates if I have four lists - four columns in excel 97 and I want to find duplicates within all four lists - where a duplicate of an item in column-1 could be located in any of the other three columns?  
    Thanks, Dave
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-455630)
    
14.  ![](https://secure.gravatar.com/avatar/b1a48cd68d542c02de65a848cea521e84f21fdd96be092eda59a19cd89660d41?s=64&d=mm&r=g) Saju says:
    
    [January 29, 2015 at 12:26 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-902421)
    
    Dear Chandu,  
    through countifs function i found out count of duplicate values in a database.  
    how to findout cell reference of those duplicates?
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-902421)
    
15.  [Best of Excel on the Web – Hidden Treasures (2016)](http://candidsourcing.com/blog/index.php/2016/01/05/best-of-excel-on-the-web-hidden-treasures-2016/)
     says:
    
    [January 5, 2016 at 12:50 pm](https://chandoo.org/wp/formula-forensics-no-026/#comment-1116412)
    
    \[…\] How to highlight duplicate entries in a list \[Chandoo\] \[…\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-1116412)
    
16.  [Best of Excel on the Web | Candid Sourcing](http://blog.candidsourcing.com/best-of-excel-on-the-web/)
     says:
    
    [February 23, 2016 at 5:32 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-1135423)
    
    \[…\] How to highlight duplicate entries in a list \[Chandoo\] \[…\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-1135423)
    
17.  [Hidden Treasures – Best of Excel on the Web (Sep 2012) – Launch Excel](https://www.launchexcel.com/web-round-up-1/)
     says:
    
    [February 17, 2018 at 6:07 am](https://chandoo.org/wp/formula-forensics-no-026/#comment-1536636)
    
    \[…\] How to highlight duplicate entries in a list \[Chandoo\] \[…\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-026/#comment-1536636)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-026/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Excel Salary Survey Dashboards – Choose the winner \[poll\]](https://chandoo.org/wp/excel-salary-dashboards-voting/) | [How fast can you finish this Excel Hurdles Challenge \[Spreadsheet Olympics\]](https://chandoo.org/wp/excel-hurdles/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)