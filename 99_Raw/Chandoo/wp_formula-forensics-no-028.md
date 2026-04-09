# Use VLookup to return a value from the left of the number

**Source:** https://chandoo.org/wp/formula-forensics-no-028

---

Formula Forensics No. 028 – It’s Just a Jump to the Left
========================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 , [Random](https://chandoo.org/wp/category/uncategorized/)
 - 43 comments

  

In 2010 Chandoo wrote a [post](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/ "VLookupto the Left Post")
 about options to perform a VLookup to the left of the Reference Column

Mike one of Chandoo.org’s astute readers had noticed a post by **DaddyLongLegs** over at the [Excel Forum](http://www.excelforum.com/ "Excel Forum")
 which describes a technique for using VLookup to look to the left of your reference column. Mike made a comment to the effect at [Mike’s Comment](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/#comment-140892 "Mikes Comment")

Today at Formula Forensics we have a look at this technique and see why it works as well as looking at some extensions using the same idea.

As always at Formula Forensics you can follow along with a sample file here: [Download 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/09/lookup-to-left.xls "VLookup to the left")

VLOOKUP
-------

Lets start with understanding what the Excel VLookup() function does.

VLookup uses the syntax:

[![](https://chandoo.org/wp/wp-content/uploads/2012/09/VLL01.png "VLL01")](https://chandoo.org/wp/wp-content/uploads/2012/09/VLL01.png)

So VLookup looks up a **Lookup\_Value** in the first Column of the **Table\_Array** and returns a matching value from the same position from another column in position **Col\_Index\_No** of the **Table\_Array**.

Of note here is that the Table\_Array is specified for the lookup area, not a Range.

A Table\_Array can be a Range as specified in the Syntax above eg: A2:D8 or it can be a Named Formula or it can be a formula that returns a Range as a solution.

We can use this to trick Excel into accepting an Array which has Column 1 to the right of Column 2. Effectively meaning we are returning a value from the left of Column 1.

Mike’s Solution
---------------

Lets look at Chandoo’s first Question: **_Which person made sales = 1088?_**

Mike supplied the solution:

\=VLOOKUP(1088,CHOOSE({2,1},$B$5:$B$17,$D$5:$D$17),2,0)

\=**John**

Which we can manually see is correct and the answer is in fact to the left of the Lookup value of 1088.

[![](https://chandoo.org/wp/wp-content/uploads/2012/09/VLL02.png "VLL02")](https://chandoo.org/wp/wp-content/uploads/2012/09/VLL02.png)

Mikes formula: \=VLOOKUP(1088, CHOOSE({2,1}, $B$5:$B$17, $D$5:$D$17), 2, 0)

Is a standard VLookup with:

**Lookup\_Value**: 1088

**Table\_Array**: CHOOSE({2,1}, $B$5:$B$17, $D$5:$D$17)

**Col\_Index\_No**: 2

**Range\_Lookup**: 0

So we can read this as lookup the value **1088** in Column **1** of the Table\_Array and return the equivalent value from Column 2 of the Table\_Array.

But what’s this Table\_Array of: CHOOSE({2,1}, $B$5:$B$17, $D$5:$D$17) doing?

In a Blank cell say I19 enter: **\=**CHOOSE({2,1}, $B$5:$B$17, $D$5:$D$17) press **F9** not **Enter**

Excel responds with: ={1592,”Joseph”;1088,”John”;1680,”Josh”;2133,”Jamie”;1610,”Jackie”;1540,”Johnson”;1316,”Jonathan”;1799,”Jagjit”;1624,”Jairam”;726,”Jessy”;2277,”Javed”;714,”Jimmy”;2682,”Juno”}

We can see this is an array of the elements from Column B and Column D

The 1592 is the first value in Column D, and Joseph is the first value in Column B

Then 1088 is the second value in Column D and John is the second value in Column B

Then 1680 is the third value in Column D and Josh is the third value in Column B, etc

You can see that Excel uses the “,” to separate entries in different columns in the same row and then uses “;” to separate the different rows

So the Formula \=CHOOSE({2,1}, $B$5:$B$17, $D$5:$D$17)

Has setup an array where Column 1 is Range D5:D17 and Column 2 is Range B5:B17

### Back to VLookup

VLookup looks up the Lookup\_Value from Column 1 of the Table array in this case we saw above that this is the Range: $D$5:$D$17

Vlookup finds the position of the Lookup value, 1088, in our case is position No 2. And the goes to Column 2, which is $B$5:$B$17 and returns the value from position 2 which is John.

### Why has Mike Used {2,1} ?

Why has Mike Used {2,1} ?

As it turns out it doesn’t matter what order the array elements are listed as long as the Ranges listed in the Choose function match the array order

If Mike had used {1,2} instead he would be still able to rearrange the formula to make it work

\=VLOOKUP(1088,CHOOSE({1,2},$D$5:$D$17, $B$5:$B$17),2,0)

Noting that Choose position 1 is still D5:D17 and Choose position 2 is still B5:B17

You can check that out for yourself at Cell **I21**

### Extending this Technique

You can add any number of ranges of data to the Vlookup function by simply extending the Choose Function, ensuring that the Choose Array ranges matches the Ranges order in the Choose function.

So the following function will allow us to look up a value from Column D (Column 1) and return values from either Column B or C (Columns 2 & 3 respectively) by simply changing the Column\_Index\_No 3

\=VLOOKUP(1088,CHOOSE({1,2,3},$D$5:$D$17,$B$5:$B$17,$C5:C17),3,0)

You can see here that Both Lookup Columns are to the left of the Lookup Column.

There are a number of such samples in the Extension Questions and Solutions section in the example file.

Download
--------

You can download a copy of the above file and follow along, [Download Here – Excel 97-2013](https://chandoo.org/wp/wp-content/uploads/2012/09/lookup-to-left.xls "VLookup to the left")
.

Formula Forensics “The Series”
------------------------------

This is the 28th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts: [Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "FF Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share like above, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
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
| Written by Hui...  <br>Tags: [choose()](https://chandoo.org/wp/tag/choose/)<br>, [vlookup](https://chandoo.org/wp/tag/vlookup/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 43 Responses to “Formula Forensics No. 028 – It’s Just a Jump to the Left”

1.  ![](https://secure.gravatar.com/avatar/b469d43c70727b21d83f2ed47e6c6c758e62a20e731905dbd7cd443a5151bc4e?s=64&d=mm&r=g) [Saran](http://www.lostinexcel.blogspot.com/)
     says:
    
    [September 6, 2012 at 7:26 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-233513)
    
    Thanks Hui
    
    Well explained.
    
    This is the one of the best example article for bsic array formula learners.
    
    They can able to learn simple array as well as advanced vlookp.
    
    Regards,  
    Saran  
    [http://www.lostinexcel.blogspot.com](http://www.lostinexcel.blogspot.com/)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233513)
    
2.  ![](https://secure.gravatar.com/avatar/c0fea373f8183e72154f8d8fd6e8abd84ee876f114a07756bb7b0749710d4ddc?s=64&d=mm&r=g) [Lukas](http://www.excelnova.org/)
     says:
    
    [September 6, 2012 at 7:37 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-233519)
    
    Great Stuff guys! Didn't know this technique and it is really awesome!
    
    Cheers, Lukas  
    (ExcelNova.org) 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233519)
    
3.  ![](https://secure.gravatar.com/avatar/d85e47e84ed3dd6a332dd407199befaf3210153ab3b5155d6ac8868206aca836?s=64&d=mm&r=g) George says:
    
    [September 6, 2012 at 8:43 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-233565)
    
    Whilst this is very clever, why would you ever use it rather than an Offset() Match() combination?  They seem to be much more intuitive and significantly more flexible.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233565)
    
4.  ![](https://secure.gravatar.com/avatar/e9977c0323779337d6216e89141068d273328cc36e564ca80ef0ba361b832dcf?s=64&d=mm&r=g) Kevin says:
    
    [September 6, 2012 at 11:50 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-233678)
    
    The most important argument in the use of lookup is the FALSE at then end.
    
    Your series didn't speak enough to its relevancy.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233678)
    
5.  ![](https://secure.gravatar.com/avatar/00a0910f936e0e7c9eae1c62c9b17eb3b533faf4bc700d82476205d3b938238f?s=64&d=mm&r=g) David R says:
    
    [September 6, 2012 at 2:01 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-233755)
    
    I have to agree with George. The much more elegant solution would be to simply use INDEX and MATCH. Run and INDEX on the return column data (column B in this example) and then use MATCH to determine the row to return (column D in this example).
    
    An item to note: make sure to specify that you want an exact match when using the MATCH function by using a 0 as the third parameter in the function.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233755)
    
    *   ![](https://secure.gravatar.com/avatar/84057a754cca0b26cf3f77508270959d04857f2cc11344f41feccf8caea69279?s=64&d=mm&r=g) Kdu Bonalume says:
        
        [September 6, 2012 at 3:18 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-233801)
        
        I'd say that the beauty of Excel is that: each person can decide by itself which solution uses among the available possibilities.
        
        You may choose INDEX+MATCH, Hui would prefer VLOOKUP+CHOOSE and otherwise I'd try OFFSET+MATCH. 
        
        That's the point. Excel has many different way to solve situations and them all make you learn more and then someday this knowledge will be applied in another problem, like "oh, that array formula using choose will be helpful now!".
        
        Kdu.  
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233801)
        
        *   ![](https://secure.gravatar.com/avatar/be0942581ecf6840ea793380b8ea9cc3b0c55d1890674298d87ad1ac87d70b0c?s=64&d=mm&r=g) shrivallabha says:
            
            [September 6, 2012 at 5:11 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-233872)
            
            Kdu,  
               
            While you can surely use OFFSET, it will be important to keep in mind that OFFSET is a volatile function and excessive use of it will slow down your sheet calculations. You can also try INDIRECT which belongs to the same volatile category but then you can refer any sheet from open workbooks to lookup.  
            INDEX + MATCH is tried and tested solution.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233872)
            
            *   ![](https://secure.gravatar.com/avatar/84057a754cca0b26cf3f77508270959d04857f2cc11344f41feccf8caea69279?s=64&d=mm&r=g) Kdu Bonalume says:
                
                [September 7, 2012 at 3:37 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234255)
                
                I'm not saying that i prefer OFFSET+MATCH, but I was just trying to show that all those ways are helpful and make us better prepared for new challenges at work and stuff.
                
                And obviously the main point was to present the vlookup with choose function. That's why I think we should just talk about our own ways to solve it and fill this topic with good stuff for everybody as a "Search Book".
                
                Kdu. 
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234255)
                
                *   ![](https://secure.gravatar.com/avatar/00a0910f936e0e7c9eae1c62c9b17eb3b533faf4bc700d82476205d3b938238f?s=64&d=mm&r=g) David R says:
                    
                    [September 7, 2012 at 1:46 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-234637)
                    
                    I didn't mean my response to cause any animosity. I tend to use large data sets within Excel with many functions, so whenever possible I like to use methods that help draw down the requirements on my computer's memory and processor. I've found that the INDEX/MATCH combination works best given those parameters.
                    
                    That said, in small files with minimal amounts of data, I agree that any method that works should be considered correct as it usually doesn't have a noticeable difference on overall worksheet efficiency and speed.
                    
6.  ![](https://secure.gravatar.com/avatar/7662437909e76ae603fae87ad1a84c222912b214af4a0f6f7fecde81c45ce640?s=64&d=mm&r=g) Giles says:
    
    [September 6, 2012 at 3:12 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-233798)
    
    A third vote for George's response... as soon as I started reading my thought was why do you even need this solution.  Index and Match (my preference) or Match and Offset accomplish this easily and elegantly and with much greater flexibility.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233798)
    
7.  ![](https://secure.gravatar.com/avatar/f4a301ee69305887271ead1dd1e4683bbb74955ca39ad44a5b716a986c0f39e0?s=64&d=mm&r=g) Julien says:
    
    [September 6, 2012 at 5:57 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-233901)
    
    Wow, that looks very complicated compared to what I got:
    
    Column A is all my salesmen   
    Column B is all their sales values.
    
    \=LOOKUP(_<value>_,B:B,A:A) 
    
    In the past, I also used INDEX and MATCH ... 
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-233901)
    
    *   ![](https://secure.gravatar.com/avatar/e92287ecac5c812d2f070218a99ae3458339999f96461a89469704f41fd17c16?s=64&d=mm&r=g) Amar says:
        
        [July 23, 2014 at 10:16 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-578578)
        
        Hello Julien,
        
        For Lookup function the values in lookup\_vector must be placed in ascending order, which sometimes may not be the case (or easy while handling large set of data).
        
        Regards  
        Amar
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-578578)
        
8.  ![](https://secure.gravatar.com/avatar/7c9167d17902152de4206e1887176da2c241e7aae92c86a960c9a9e837ca5127?s=64&d=mm&r=g) Kiev says:
    
    [September 7, 2012 at 12:15 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234137)
    
    Even we can do the same job with different combination, but i think the main point for this post is learn more about Vlookup by utilize Choose function.
    
    For me, i like the Choose function instruction very much as i have never be clear after reading this post.
    
    Thank you.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234137)
    
9.  ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui](http://chandoo.org/wp/about-hui/)
     says:
    
    [September 7, 2012 at 3:59 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234270)
    
    Hi All  
    Thanx for the feedback both positive and negative on the use of the Vlookup function to do searches to the left of the reference column.  
    Formula Forensics started 28 posts ago, by answering a simple question as to how something worked.
    
    Formula Forensics continues along the lines of:  
    1\. How does a formula work  
    2\. What new or alternative techniques can we discuss  
    3\. What are alternative ways of tackling problems
    
    Formula Forensics has never said:  
    1\. This is the way you must do it  
    2\. This is the only way to do something
    
    Often in previous Formula Forensics we have seen dozens of alternative solutions posed in the comments, none are more right than any other solution, provided they return the correct answer.
    
    So, Please keep an open mind when reading the techniques we discuss at Formula Forensics. Add the techniques discussed to your Excel Toolkit and Excel Knowledge Base as you never know one day soon you may be confronted with a situation that demands a Choose({1,2}, ...) solution and now at least you are prepared for it.  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234270)
    
    *   ![](https://secure.gravatar.com/avatar/84057a754cca0b26cf3f77508270959d04857f2cc11344f41feccf8caea69279?s=64&d=mm&r=g) Kdu Bonalume says:
        
        [September 7, 2012 at 12:10 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-234575)
        
        That's it Hui! Congrats (:
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234575)
        
    *   ![](https://secure.gravatar.com/avatar/a1c2faf7156aa42901ed7be3eee04f89eaa8cb6c83bcc6c9f97d9f858084c609?s=64&d=mm&r=g) Pratish Sharma says:
        
        [October 14, 2014 at 8:43 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-808723)
        
        Well said. A great thought-provoking idea in the first place. Thanks.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-808723)
        
    *   ![](https://secure.gravatar.com/avatar/77819481a65252f4f1872e2401d53a24267c72783822135bd94485023ca00808?s=64&d=mm&r=g) [Abhilash VK](http://www.exceltoxl.com/)
         says:
        
        [November 12, 2014 at 7:35 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-846538)
        
        Awesome! Hui!!!
        
        Well said, This is definitely a good post to bookmark. I am sharing it to my viewers too.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-846538)
        
10.  ![](https://secure.gravatar.com/avatar/546c2e7c6f9a6f8fcd83af05ec89e3e2bbd41515729275ef4c81f7a562af5251?s=64&d=mm&r=g) Jitendra says:
    
    [September 7, 2012 at 4:29 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234288)
    
    Good, I was waiting for clarification of this formula.  
    Excel Ninja SirJB clarify this in the comment :   
    [http://chandoo.org/forums/topic/vlookup-9](http://chandoo.org/forums/topic/vlookup-9)
      
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234288)
    
11.  ![](https://secure.gravatar.com/avatar/7dcacae7bb0dcf2c6604d26943214d2b2e3f50989c8d2bbe024e7208eda4d6b1?s=64&d=mm&r=g) SAUMYA UPADHYAY says:
    
    [September 7, 2012 at 5:46 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234341)
    
    hii Chandoo,  
    Thank for helping us,  
       
    What if the data is on different sheets????  
       
    Do we to consolidate in 1 sheet then only this formula will work??  
       
    Regards.  
    Saumya  
       
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234341)
    
12.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
    
    [September 7, 2012 at 8:39 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-234444)
    
    Interesting use of CHOOSE. While INDEX/MATCH would be my first response, this is a timely reminder of the CHOOSE function, which  - while not my first choice here - can be the best approach to other problems.  
    For instance,  you could use the 'reference' version of INDEX to dynamically sum a particular named range based on a number stored in A2, like this:  
    \=SUM(INDEX((Range1,Range2,Range3),,,A2) )  
    ...where Range1 etc are named ranges (consisting of one or more cells in each range) and in A2 is a number telling Excel which of those three range names you want the INDEX function to return  
    For instance, say we have three named ranges: Sales, Forecast, and Variance. And lay we have a picklist in cell A1 where a user can choose either 'Sales' or 'Forecast' or 'Variance'. And in A2 we have an IF or VLOOKUP or even CHOOSE function that returns 1 if the user selects Sales, 2 for Forecast, and 3 for Variance.  
    Then we have a formula like this:  
    \=SUM(INDEX((Sales, Forecast,Variance),,,A2))  
    ...which dynamically returns the sum of the range that the user selects with the picklist.  
    Choose can do the same thing with this formula:  
    \=SUM(CHOOSE(A2,Sales, Forecast,Variance)) as the CHOOSE function also accepts ranges.  
    In fact the CHOOSE function can be better at this than INDEX, because it doesn't care if your data ranges are on different sheets or even in the same workbook. Whereas try to point index to multiple ranges on different sheets and you will get an error.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-234444)
    
13.  ![](https://secure.gravatar.com/avatar/5a4c5ff0939eb76cd54c4a076521f4332f1446c60f00add71581d8f3a8736c0a?s=64&d=mm&r=g) Danièle says:
    
    [September 8, 2012 at 1:52 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-235091)
    
    Thanks for a great "forensic" and a new array usage.
    
    I took a long time to use choose, but it is a very handy tool as Hui demonstrated here ( and I like this option a lot!)as well as Jeff Weir.  
    It is lighter to use than index, and that is very appealing.  
    I totally agree with Saran that to grasp the logic of array formulas, this one is ranking top for me.  
    Thanks!
    
    Cheers,  
    Danièle  
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-235091)
    
14.  ![](https://secure.gravatar.com/avatar/92bab897cb9c041af548b2a5d118ec75d6050486ea30bf7be830f414cc42167d?s=64&d=mm&r=g) Bryn says:
    
    [September 8, 2012 at 8:15 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-235339)
    
    A most interesting post; some things that are relevant to this and similar discussions.  
    The most important equirementis an accurate answer; using data to enable decisions is better than faormula elegance.  
    Spreadsheets will outlive our interest and someone else will have to pick up the tab(s). So simple formulas will save them hassle.  
    Your time is valuable; a diect technique will use less of it. Also simple formula are reasy to debug and to prove.  
    The value of this example to illustrate array processing has been understated. Arrays are not intuiive to most and we need effective examples.  
    I find that many beginners struggle to get their heads around vlookup at all, so I now teach index/match and build form there.  
    This formula is effective though, and just shows that dogma like 'vlookup only looks to the right' is rarely the last word.  
     
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-235339)
    
15.  ![](https://secure.gravatar.com/avatar/65b9d679dc110884e4bf8be5131a461c31f798ed4028ff290f4c6f084972e57d?s=64&d=mm&r=g) Sudhir says:
    
    [September 18, 2012 at 11:51 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-243050)
    
    Hi Chandooooooo.... this post was like WOW !
    
    I have been a great fan of your site since 2007 (one of the earliest ?)...thanks for the knowledge sharing !
    
    Sudhir  
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-243050)
    
    *   ![](https://secure.gravatar.com/avatar/65b9d679dc110884e4bf8be5131a461c31f798ed4028ff290f4c6f084972e57d?s=64&d=mm&r=g) Sudhir says:
        
        [September 18, 2012 at 11:52 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-243051)
        
        ...also, I note that by using Choose, your data need not be continguous, you can actually pick up random three columns of data as you require, and build your vlookup !!
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-243051)
        
16.  ![](https://secure.gravatar.com/avatar/846098490c2482eca020aaf7f00096be16987e23c496e0f06403e70a11b1ee0f?s=64&d=mm&r=g) alejandro says:
    
    [October 4, 2012 at 10:08 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-255815)
    
    This is simply great....wonderful....I can construct a matriz in my order....thanks
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-255815)
    
17.  ![](https://secure.gravatar.com/avatar/823d95b270e663679a4867bda8cb80ec529a096d0d299a79a22db8b16a5c5372?s=64&d=mm&r=g) Mayank says:
    
    [July 26, 2013 at 6:54 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-441250)
    
    Nice post...  
    I am comfortable with macros but this formula is awesome  
    I just hav a quick question  
    If I want to introduce this as a new function in my excel sheet named let say  
    VlookDown(value to be searched , column range to be searched, column range to be returned, rangeLookup)
    
    and then I can code this to use formula  
    Vlookup(value to be searched, CHOOSE({2,1}, column range to be returned, column range to searched), 2, rangeLookup)
    
    I am not sure how to use formula in excel code..  
    Please suggest the needful
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-441250)
    
18.  ![](https://secure.gravatar.com/avatar/e20f5a1cf467d9726fa91a3b7786be1ac2b92c0cea698166b656c16936e24db0?s=64&d=mm&r=g) Dave says:
    
    [October 17, 2013 at 7:54 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-449484)
    
    I wonder why Excel doesn't just use negative column numbers for looking to the left (or up, for HLOOKUP)...???
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-449484)
    
19.  ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) [Jeff Weir](http://www.heavydutydecisions.co.nz/)
     says:
    
    [October 17, 2013 at 10:38 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-449497)
    
    Dave - probably because of recalculation reasons.
    
    VLOOKUP makes you specify a table in which to do the lookup. The reason for this is so that Excel can monitor that table range, and only recalculate that VLOOKUP when anything in that table range changes (or any formulas upstream of that table range change). So change something outside that table, and Excel won't recalculate that VLOOKUP. This makes it something called a non-Volatile function.
    
    If VLOOKUP allowed negative numbers, those numbers could result in references that fall outside the specified table range. They could fall anywhere on the entire sheet. So anytime you entered new data anywhere in the spreadsheet, Excel would have to recalculate the VLOOKUP too...because it couldn't be sure that what you just changed in the sheet was referenced by the VLOOKUP or not.
    
    This would make it what's called a Volatile function. If you have volatile functions in your workbook, any time you make a change anywhere at all on the spreadsheet, Excel recalculates the value of all those volatile functions too. Excel then recalculates every applicable formula downstream of these functions too – even though most probably nothing changed. Volatile functions include OFFSET, INDIRECT, RAND, NOW, TODAY, and my personal favorite, MEDICATION.
    
    More about this here:  
    [http://chandoo.org/wp/2013/09/29/i-said-your-spreadsheet-is-really-fat-not-real-phat](http://chandoo.org/wp/2013/09/29/i-said-your-spreadsheet-is-really-fat-not-real-phat)
    
    ...under the heading Handle sweaty Dynamite and Volatile Functions with extreme care…
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-449497)
    
    *   ![](https://secure.gravatar.com/avatar/a1c2faf7156aa42901ed7be3eee04f89eaa8cb6c83bcc6c9f97d9f858084c609?s=64&d=mm&r=g) Pratish Sharma says:
        
        [October 14, 2014 at 8:40 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-808718)
        
        @Jeff: you sir, are a proverbial genius. I have read some of your comments in other posts within forums surrounding Excel, and they are always so well written and explained (and error/typo free).
        
        You are someone who we can all learn from. Thanks for taking the time to write meaningful and considered responses.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-808718)
        
        *   ![](https://secure.gravatar.com/avatar/57f122cecb5b20fa5b3b2671fb9679fd00bbdb8a663787162eb1fe162c0d5cda?s=64&d=mm&r=g) Jeff Weir says:
            
            [October 14, 2014 at 11:39 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-808814)
            
            At last...someone who appreciates me for the genius I am. 😉  
            Thanks Pratish.
            
            [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-808814)
            
            *   ![](https://secure.gravatar.com/avatar/77819481a65252f4f1872e2401d53a24267c72783822135bd94485023ca00808?s=64&d=mm&r=g) [Abhilash VK](http://www.exceltoxl.com/)
                 says:
                
                [November 12, 2014 at 7:38 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-846541)
                
                Jeff, there are many fans for you because your thoughts are funny and your tips are outstanding!!!
                
                [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-846541)
                
20.  ![](https://secure.gravatar.com/avatar/69d199c98848d72179875d4b9bf05c4c9d656c0e213d9eb97bff59f1e946cfed?s=64&d=mm&r=g) victor ahiale says:
    
    [June 18, 2014 at 3:57 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-558083)
    
    how to make my vlookup pick both letter and numbers in a cell.  
    eg B50.9
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-558083)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [June 19, 2014 at 3:31 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-558432)
        
        @Victor  
        \=Vlookup("B50.9",Range, Column)  
        eg: =Vlookup("B50.9",A2:B20, 2)  
        or if B and 50.9 are in cells A1 and B1  
        \=Vlookup(A1&B1, A2:B20, 2)
        
        etc
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-558432)
        
21.  ![](https://secure.gravatar.com/avatar/df0c4ccaff3811418f748b466691a77ac0937aaf3fb72b7e64aa0db861098c89?s=64&d=mm&r=g) [Tuyet Nguyen](http://www.chandoo.org/)
     says:
    
    [July 25, 2014 at 5:06 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-580086)
    
    Thanks Hui,  
    I'm glad I've found this. It works like a charm! Normally I have to copy data to the right, and start normal VLookup.
    
    By inserting Choose {Table Array}, I can also select the fields I need to list in the Vlookup formula instead of having to list multiple columns and have to remember which column index number contains the data I want to return (it was a hassle in case some columns in the table were hidden)
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-580086)
    
22.  ![](https://secure.gravatar.com/avatar/c061626092b5699da0699dacf686bdc41374953decd6278dd270e1c5223190f7?s=64&d=mm&r=g) imran says:
    
    [November 22, 2014 at 6:38 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-856087)
    
    Before saying to thanks I like to share experience..
    
    Since few months back I was trying and making dash board along with staging table... With using conditional formulas which help me out to extract flat and tabular raw data form... And now little expertise on way which is going on...
    
    The October month is very tough and crucial for me forv developing new dash boards... New data form...still now struggling.... And thanks CHANDOO ORG. to make my days happy without stress full coz of the new formulated combination of vlookup and choose formula...
    
    And i have learn lot of things in that period if things newly try it... Some times will not work... But we get the ideas where we are what we have done...
    
    Once again thanks' to CHANDOO ORG. To made my days happily..  
    And now will be going on short vacation post completing my work.
    
    Heartily thanks  
    Keep teaching us! Best of luck ????
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-856087)
    
23.  ![](https://secure.gravatar.com/avatar/c061626092b5699da0699dacf686bdc41374953decd6278dd270e1c5223190f7?s=64&d=mm&r=g) imran says:
    
    [November 22, 2014 at 6:40 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-856088)
    
    Before saying to thanks I like to share experience..
    
    Since few months back I was trying and making dash board along with staging table... With using conditional formulas which help me out to extract flat and tabular raw data form... And now little expertise on way which is going on...
    
    The October month is very tough and crucial for me forv developing new dash boards... New data form...still now struggling.... And thanks CHANDOO ORG. to make my days happy without stress full coz of the new formulated combination of vlookup and choose formula...
    
    And i have learn lot of things in that period if things newly try it... Some times will not work... But we get the ideas where we are what we have done...
    
    Once again thanks' to CHANDOO ORG. To made my days happily..  
    And now will be going on short vacation post completing my work.
    
    Heartily thanks  
    Keep teaching us! Best of luck ????
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-856088)
    
24.  ![](https://secure.gravatar.com/avatar/2dea27663436335ab5b8ad75806fa5e45660a23a4fd8cd384da680b106b4807b?s=64&d=mm&r=g) p says:
    
    [January 12, 2015 at 8:51 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-892852)
    
    I have always found that it is better to keep things simple. I usually just employ a hidden helper column that pulls over the lookup range.
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-892852)
    
25.  ![](https://secure.gravatar.com/avatar/a71eb92f813ed2eab6f370e44e8ff57152b62a8f8b430a6099d7382d044fee65?s=64&d=mm&r=g) Nadeen says:
    
    [July 14, 2015 at 11:16 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-1008828)
    
    Hi I find your data useful but need help with the following please. My excel is rather rusty as i have not used it in about 4 years and for the life of me cannot remember how to do the following:  
    this is the formula i am using at the moment and it works provided there is data for both but if there is data missing in the one it either n/a or it is blank if i use an If iserror  
    \=VLOOKUP(R8,'WORKING do not DELETE'!B:F,5,FALSE)&" & "&(VLOOKUP(S8,'WORKING do not DELETE'!B:F,5,FALSE))  
    I am not adding up numbers but i need the text to look up the name in one cell and then look up the next cell and add them together if data found. but if data only found in one cell it and not the other it needs to only put in the one and not n/a on me.  
    sorry my explanation sucks. hope you can help me
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1008828)
    
26.  ![](https://secure.gravatar.com/avatar/a86b79c8d4aab972f0a4c4be4ba0707f8b5257ca72bcd4e5d3a1bdfb632d68b8?s=64&d=mm&r=g) Patrice says:
    
    [March 21, 2016 at 1:41 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-1151182)
    
    Hi There -
    
    Great article. Quick Question. How do I perform the reverse lookup when the table is in a different tab. Do I define the table before or after Choose. Thank you so much for your help!
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1151182)
    
27.  ![](https://secure.gravatar.com/avatar/9a633e19028d2e5eb3fbc8664748b92c3c2229fec4df784995d6bff5f4a34231?s=64&d=mm&r=g) Rahul Sharma says:
    
    [July 31, 2017 at 9:02 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-1489309)
    
    Hi There,
    
    I am stuck in getting the data from right to left.
    
    e h m names  
    12 15 98 a  
    74 84 32 b  
    33 45 69 c  
    21 59 77 d
    
    names h e m  
    a  
    b  
    c  
    d
    
    In there respective coloumn, can you guys please help me in this.
    
    Thanks,  
    Rahul
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1489309)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 31, 2017 at 1:39 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-1489430)
        
        @Rahul
        
        Can you please ask the question in the Chandoo.org Forums and pls attach a sample file  
        [http://forum.chandoo.org/](http://forum.chandoo.org/)
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1489430)
        
28.  ![](https://secure.gravatar.com/avatar/3172404b57b89bbbfe5df02d7d1f0de978a2cd025bd3a8b72121e1437bdcbbff?s=64&d=mm&r=g) Alex says:
    
    [November 21, 2017 at 8:17 pm](https://chandoo.org/wp/formula-forensics-no-028/#comment-1523860)
    
    No Zoolander reference...??
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1523860)
    
29.  [Mit der Excel-Funktion SVERWEIS nach links gehen – clevercalcul](https://clevercalcul.wordpress.com/2018/03/09/mit-der-excel-funktion-sverweis-nach-links-gehen/)
     says:
    
    [March 9, 2018 at 8:31 am](https://chandoo.org/wp/formula-forensics-no-028/#comment-1539489)
    
    \[…\] \]3\] [https://chandoo.org/wp/2012/09/06/formula-forensics-no-028/](https://chandoo.org/wp/2012/09/06/formula-forensics-no-028/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-028/#comment-1539489)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-no-028/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Show Decimal Points if needed \[Quick Tip\]](https://chandoo.org/wp/show-decimal-points-if-needed/) | [A Spreadsheet walks in to a bar … \[open mic\]](https://chandoo.org/wp/spreadsheet-walks-into-bar/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)