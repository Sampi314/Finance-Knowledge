# What is the length of longest winning streak? [Excel homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/longest-winning-streak-problem

---

What is the length of longest winning streak? \[Excel homework\]
================================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 22 comments

  

Here is a fun problem to think about.

Let’s say you are looking at some data like this:

![What is the length of longest winning streak - Excel formula problem](https://chandoo.org/wp/wp-content/uploads/2015/01/longest-winning-streak-problem.png)

And you want to find out **_what is the longest streak of wins in the list_**.

How do you calculate it?

**bonus question:** What formula calculates when the longest streak began?

**[Download the workbook and solve this problem](https://chandoo.org/wp/wp-content/uploads/2015/01/winning-streak-problem1.xlsx)
.**

Note: this scenario is useful for many situations like finding longest attendance streak in employees, longest occupancy streak in hotel rooms, longest fault free production etc.

### Few things to keep in mind:

*   Assume the list of wins contains only Boolean values and named as _list_
*   Assume the match number column is named as _id_
*   You can use these additional names too:
    *   list.a (represents one cell above the list and all list values except the last one)
    *   list.b (all list values except the first one and extra blank cell at the end)
    *   size (the size of list, counta(list))
*   You can use single formulas, helper columns or VBA to solve this problem
*   Post your solutions in the comments.
*   If your solution uses < > symbols, write LT & GT instead. Otherwise few bits of your comment might be gobbled by byte hungry monster that handles our comment program in server.

Go ahead and figure out the solution. Happy hunting.

**Hungry for more?** Check out [Excel homework problems page](http://chandoo.org/wp/excel-problems-challenges/ "Excel Problems & Challenges")
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
| Written by Chandoo  <br>Tags: [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 22 Responses to “What is the length of longest winning streak? \[Excel homework\]”

1.  ![](https://secure.gravatar.com/avatar/0f1df416e56653d47d56eca5dee0a99c2c7f1460100d8f1c982ef734b7b6f4f9?s=64&d=mm&r=g) [Green](http://n/a)
     says:
    
    [January 30, 2015 at 9:20 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903074)
    
    Using VBA to CountIf Until and loop until the cells are blank at the bottom. That would give a list of the sizes of the groups of trues. Then a MAX formula to calculate the largest figure in the returned figures.
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903074)
    
2.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
     says:
    
    [January 30, 2015 at 11:30 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903131)
    
    \=MAX(FREQUENCY(IF(list,id),IF(list,,id)))  
    regards  
    r
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903131)
    
3.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
     says:
    
    [January 30, 2015 at 11:41 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903136)
    
    assuming that in F6 there is the formula that solves the first question ... so the formula for bonus is:  
    \=MATCH(F6,FREQUENCY(IF(list,id),IF(list,,id)),)-F6
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903136)
    
    *   ![](https://secure.gravatar.com/avatar/fa4156e329148bb9cc98ad6288794417f03d6a0f6fb214045be44bd55568f27f?s=64&d=mm&r=g) Louis Bharnabas says:
        
        [February 10, 2015 at 10:24 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-910363)
        
        Hi Roberto,
        
        Can you explain how both the formulas work?
        
        Regards,  
        Louis
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-910363)
        
    *   ![](https://secure.gravatar.com/avatar/551924fb7d4ef359c4821cbb8a59c7a02eec6d7c8c60022c6d397cce71348ac8?s=64&d=mm&r=g) Cody says:
        
        [February 26, 2015 at 5:17 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-920572)
        
        This is a cool, simpler alternative to Chandoo's solution. The only issue is that this method only works when dealing with True/False values. if the values were switched to numbers or text it would return an error.
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-920572)
        
4.  ![](https://secure.gravatar.com/avatar/08946ae8163fb8b320bf10e520933033ff0d8223317ffdb665765ed3b8eefad0?s=64&d=mm&r=g) Dick Byrne says:
    
    [January 30, 2015 at 3:11 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903247)
    
    Adding a helper column is definitely the simplest and quickest way to go here. In cell D5, put =IF(NOT(C5), 0, 1+D4) and copy that down the list. Then the longest streak is =MAX(D5:D244) and it starts at =MATCH(I6,D5:D244,0) - I6 + 1
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903247)
    
    *   ![](https://secure.gravatar.com/avatar/08946ae8163fb8b320bf10e520933033ff0d8223317ffdb665765ed3b8eefad0?s=64&d=mm&r=g) Dick Byrne says:
        
        [January 30, 2015 at 3:17 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903250)
        
        That "Starts At" formula assumes that you've put the longest streak formula in cell I6.
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903250)
        
    *   ![](https://secure.gravatar.com/avatar/4fcaed4e328b9792685dd150f182182bca7b912e0e8c2c50a52abf7f8b985801?s=64&d=mm&r=g) SantoshKumar says:
        
        [January 31, 2015 at 10:21 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903993)
        
        Thanks Byrne,  
        Simple If & Not fromula through helper column is great.  
        Also changing the value position like, =IF(NOT(C5),1+D4,0) gives longest loosing streak.
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903993)
        
5.  ![](https://secure.gravatar.com/avatar/99d7e6f62a4460c281eeddad2e7d08fcdf1668b259b06b5d3f0580ad97866b08?s=64&d=mm&r=g) [Chris Macro](http://www.thespreadsheetguru.com/)
     says:
    
    [January 30, 2015 at 3:46 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903283)
    
    If anybody needs a little help tackling this homework assignment, below is a link to an article I wrote a while back that shows how to calculate streaks
    
    [http://www.thespreadsheetguru.com/blog/2014/6/29/formulas-to-calculate-longest-current-win-streaks](http://www.thespreadsheetguru.com/blog/2014/6/29/formulas-to-calculate-longest-current-win-streaks)
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903283)
    
    *   ![](https://secure.gravatar.com/avatar/16ee71d7bb19fb0945e3c63d50fe570a95e76be0a5d33b32cfe648c3163506a8?s=64&d=mm&r=g) [Oscar](http://www.get-digital-help.com/)
         says:
        
        [January 31, 2015 at 2:52 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904114)
        
        Interesting post and comments, I also wrote a blog post about something similar a few months ago.
        
        [http://www.get-digital-help.com/2014/11/11/find-the-longestsmallest-consecutive-sequence-of-a-value/](http://www.get-digital-help.com/2014/11/11/find-the-longestsmallest-consecutive-sequence-of-a-value/)
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904114)
        
6.  ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
    
    [January 30, 2015 at 5:31 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903342)
    
    amazing 🙂  
    chandoo's solution shows the longest winner or loser-track  
    robert mensa's solution shows only the winner-track  
    Chris macro's solution is a wonderful supplement  
    THANK YOU to all
    
    will be looking for more solutions at this weekend  
    thank you chandoo for this challenge;)
    
    Regards  
    Stef@n
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903342)
    
7.  ![](https://secure.gravatar.com/avatar/15fc3f1de23e79e3d0acff9a29e63f1702992c4999a3c32d83ca3276216086ef?s=64&d=mm&r=g) KathyW says:
    
    [January 30, 2015 at 6:16 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903366)
    
    I just put a formula in column A, starting in cell A5 (which I then hid):  
    \=IF(C5=TRUE,1+A4,0)
    
    Then in cell F6 I put : =MAX(A5:A245)  
    In cell F7 I put: =VLOOKUP(F6,A5:C245,2,FALSE)-(F6-1)
    
    This only tracks winning streaks.
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903366)
    
8.  ![](https://secure.gravatar.com/avatar/0f0941e6059fa0ae1cb30df2bd8bbaed9265f7216cc76993a3ea44f6acce938f?s=64&d=mm&r=g) Mark says:
    
    [January 30, 2015 at 6:26 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903373)
    
    Using helper columns  
    in cell d5: =IF(C5=C4,1+D4,1)  
    Copy all the way down.  
    Start is: =INDEX(B5:B245,MATCH(MAX(D5:D245),D5:D245,0))-MAX(D5:D245)+1
    
    Explained:  
    Length: =MAX(D5:D245)  
    Location of that Max: =INDEX(B5:B245,MATCH(E5,D5:D245,0)) Returns 98.  
    Therefore Started when is the location (98) minus the (Max+1)
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903373)
    
9.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [January 30, 2015 at 6:35 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903382)
    
    By using the helper column J
    
    J5=IF(C5;SUM(J4;1);0)
    
    Length: F10=MAX(J:J)
    
    Started When: F11=MATCH(F10;J:J;0)-F10-3
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903382)
    
10.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason Morin says:
    
    [January 30, 2015 at 8:13 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903444)
    
    Helper column in C. So in C2:
    
    \=B2\*(B1=0)+B2\*B1\*(C1+1)
    
    Now take the max of column C:
    
    \=AGGREGATE(4,6,C:C)
    
    To make the results in column C look more legible to the user, you could also use this in C2:
    
    \=IF(AND(B2,B1=FALSE),1,IF(AND(B2,B1),C1+1,""))
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903444)
    
11.  ![](https://secure.gravatar.com/avatar/5671034704d280c4a557ef7ac78e92a0ae9df0246d7eb707283548ec2c7af157?s=64&d=mm&r=g) Ghazanfar J says:
    
    [January 31, 2015 at 4:19 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903733)
    
    @roberto mensa
    
    What sorcery is this ?!?!
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903733)
    
12.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 31, 2015 at 5:56 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903805)
    
    Excellent solutions everyone. Special thanks to @Roberto for sharing a very elegant and simple solution. Thanks to Chris for linking to a valuable resource.
    
    Here is what I came up with. Both array formulas.
    
    Streak length (in cell F6)
    
    \=MAX(IFERROR(SMALL(IF(list.b LT GT list,id),id)- SMALL(IF(list.aLT GT list,id),id), 0))+1
    
    Streak position:
    
    \=SMALL(IF(list.a LT GT list,id),MATCH(F6-1,IFERROR(SMALL(IF(list.b LT GT list,id),id)- SMALL(IF(list.a LT GT list,id),id), 0),0))
    
    Notes:
    
    1\. list.a (represents one cell above the list and all list values except the last one)  
    2\. list.b (all list values except the first one and extra blank cell at the end)
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-903805)
    
    *   ![](https://secure.gravatar.com/avatar/dc8aafb2fb7eceb973a282d2e6871f90468b4378bd915ca0c772258e92898e43?s=64&d=mm&r=g) Ashfaqur Rahman says:
        
        [May 18, 2015 at 3:41 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-975970)
        
        would you please tell me how you set list, id, list.a, list.b,  
        Thanks in advance
        
        [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-975970)
        
13.  [Find the longest/smallest consecutive sequence of a value | Get Digital Help - Microsoft Excel resource](http://www.get-digital-help.com/2014/11/11/find-the-longestsmallest-consecutive-sequence-of-a-value/)
     says:
    
    [January 31, 2015 at 2:59 pm](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904119)
    
    \[…\] What is the length of longest winning streak?  \[…\]
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904119)
    
14.  ![](https://secure.gravatar.com/avatar/8dd91d046b7b96b4c6fae58335d9a30de3d532ff0f93c0586a4f1a15ef9f40d7?s=64&d=mm&r=g) Navin says:
    
    [February 1, 2015 at 8:25 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904616)
    
    Created a column to start counting the streak (from cell D5) :  
    \=IF(C5=TRUE,D4+1,0)  
    To get the length of longest winning streak :  
    \=MAX(D5:D244)  
    To get the ID where it started :  
    \=INDEX($B$5:$D$244,MATCH(G6,$D$5:$D$244,0)-G6+1,1)
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-904616)
    
15.  ![](https://secure.gravatar.com/avatar/ce59b0d8e22bf577f01d4211907632b05b396bfcf8c32699db707da405274298?s=64&d=mm&r=g) Steve S. says:
    
    [February 2, 2015 at 12:03 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-905039)
    
    I used VBA to come up with this solution:
    
    Sub Winningtreak()
    
    Dim CurrentStreak As Long  
    Dim LongestStreak As Long  
    Dim FinalRow, x, y As Long
    
    FinalRow = Cells(Rows.Count, 3).End(xlUp).Row + 1  
    CurrentStreak = 0  
    LongestStreak = 0
    
    For x = 5 To FinalRow
    
    If Cells(x, 3) = "True" Then
    
    CurrentStreak = CurrentStreak + 1
    
    ElseIf CurrentStreak GT= LongestStreak Then  
    LongestStreak = CurrentStreak  
    CurrentStreak = 0  
    y = x - LongestStreak - 4  
    ElseIf CurrentStreak LT LongestStreak Then  
    CurrentStreak = 0
    
    End If
    
    Next x
    
    Cells(4, 6) = LongestStreak  
    Cells(4, 7) = "Starting at match " & y
    
    End Sub
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-905039)
    
16.  ![](https://secure.gravatar.com/avatar/66b4e0fd75431f8cf0f12eb7bee860e484daeeaf51fd581fbbaf58fbf7f6ffe0?s=64&d=mm&r=g) Chris says:
    
    [March 13, 2015 at 5:49 am](https://chandoo.org/wp/longest-winning-streak-problem/#comment-929575)
    
    Hi all,  
    This my first time on this site. Wow! I specialize in dynamic charts which I use to teach math and I came here to look for "hover" possibilities but I was captivated by this homework. What a great site!!!  
    I don't know how this column works but replaced all items in the won column with letter grades: A,B, C, D, F. It is easy to count the most winners but what do I do to count the number of each grade letter? Any tutors to help me please?
    
    [Reply](https://chandoo.org/wp/longest-winning-streak-problem/#comment-929575)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/longest-winning-streak-problem/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Doing Cost Benefit Analysis in Excel – a case study](https://chandoo.org/wp/cost-benefit-analysis-in-excel/) | [2 Must watch Excel webinars for you](https://chandoo.org/wp/2-must-watch-excel-webinars-for-you/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)