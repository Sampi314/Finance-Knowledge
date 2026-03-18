# The Excel = Function

**Source:** https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip

---

Check Cells for Equality – Follow Up \[Quick Tip\]
==================================================

[Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 , [Quick Tip](https://chandoo.org/wp/category/quick-tip-2/)
 - 19 comments

  

Last week in [Write a formula to check few cells have same value \[Homework\]](http://chandoo.org/wp/2012/10/12/check-cells-for-equality/ "Check Cells for Equality")
,

Chandoo posed the question: _**Can you write a formula to check if a few cells are equal?**_

A lot of people answered with answers like:

\=IF(COUNTIF(A1:A4,A1)=COUNT(A1:A4),TRUE,FALSE)

or

~\=IF(SUM(A1:A4)/COUNT(A1:A4)=A1,TRUE,FALSE)~

or

\=IF(PRODUCT($A:$A)=A1^(COUNTIF($A:$A,A1)),”Yes”,”No”)

etc.

Although these are all correct, the formulas can be simplified by using a built in function of Excel

The function is **\=** 

\=
--

In Excel the = sign does two things

1\. When the = sign is the first character of a Cell, Named Formula or Reference it tells the Cell, Named Formula or Reference that it contains a formula

2\. It acts as an equality function when it has a value or formula on either side of it

What does the = function do?
----------------------------

What does the = function do?

The = function returns a Boolean or TRUE / FALSE value depending on the equality of the values/formula on either side of it

**Example:**

In a blank cell enter =2=1

Excel will display **FALSE** to tell us that the values aren’t equal

Now change the formula to =2=2

Excel will display **TRUE** to tell us that the values are equal

Either side of the = sign can contain a Formula, Cell Reference etc

\=(200/100)=2 will return **TRUE**

\=SIN(PI()/2)=1 will return **TRUE**

\=SIN(PI()/2)=15 will return **FALSE**

\=-1=COS(PI()) will Return **TRUE**

\=SIN(PI()/2)=A1 will return **TRUE** if cell A1 contains either a 1 or a formula that returns the value 1**.**

It will return False for all other values.

So the above, Homework, formulas can be simplified as :

**Original**: \=IF(COUNTIF(A1:A4,A1)=COUNT(A1:A4),TRUE,FALSE)

**Simplified**:  \=COUNTIF(A1:A4,A1)=COUNT(A1:A4)

or

**Original**: \=IF(SUM(A1:A4)/COUNT(A1:A4)=A1,TRUE,FALSE)

**Simplified**: \=SUM(A1:A4)/COUNT(A1:A4)=A1

or

**Original**: \=IF(PRODUCT($A:$A)=A1^(COUNTIF($A:$A,A1)),”Yes”,”No”)

**Simplified**: \=PRODUCT($A:$A)=A1^(COUNTIF($A:$A,A1))

and all will still, correctly, answer the question

Challenge:
----------

If your formula started with an If(), see if you can rewrite it based on the above.

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
| Written by Hui...  <br>Tags: [\=](https://chandoo.org/wp/tag/1419/)<br>, [Excel 101](https://chandoo.org/wp/tag/excel-101/)<br>, [excel basics](https://chandoo.org/wp/tag/excel-basics/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [quick tip](https://chandoo.org/wp/tag/quick-tip/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 19 Responses to “Check Cells for Equality – Follow Up \[Quick Tip\]”

1.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [Mawdo81](http://www.mypetbubble.com/)
     says:
    
    [October 16, 2012 at 10:25 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269156)
    
    Sorry but =SUM(A1:A4)/COUNT(A1:A4)=A1 will fail in the case of: {2,1,3,2}  
    Sum = 8, Count = 4 Sum/Count = 2 = A1 = True but 2<>1<>3<>2 although 2 =2!
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269156)
    
2.  ![](https://secure.gravatar.com/avatar/e0cf079609834ed36b8c9eb00e4f8600e6a7d92c823f5399cf4c7fd22c05e8d7?s=64&d=mm&r=g) Renjith M Das says:
    
    [October 16, 2012 at 11:45 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269211)
    
    Why not something even more simple?  
    \=AND(G2:G5=H2:H5)  
    Ctrl+Shift+Enter
    
    If you insist on the "If..", then
    
    \=If (And(G2:G5=H2:H5),"True",False")  
    Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269211)
    
3.  ![](https://secure.gravatar.com/avatar/e0cf079609834ed36b8c9eb00e4f8600e6a7d92c823f5399cf4c7fd22c05e8d7?s=64&d=mm&r=g) Renjith M Das says:
    
    [October 16, 2012 at 11:48 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269216)
    
    Please ignore above...I misread the question
    
    Please use the below
    
    \={If (And(G2:G5=G2),"True",False")}  
    Ctrl+Shift+ Enter
    
    Or
    
    \={AND(G2:G5=G2)}  
    Ctrl+Shift+Enter
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269216)
    
4.  ![](https://secure.gravatar.com/avatar/e0cf079609834ed36b8c9eb00e4f8600e6a7d92c823f5399cf4c7fd22c05e8d7?s=64&d=mm&r=g) Renjith M Das says:
    
    [October 16, 2012 at 12:05 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269226)
    
    Went back and saw that the formula I suggested is very similar to the obvious answer...so here is another
    
    \=IF(COUNTA(I4:I7)>SUMPRODUCT(--(I4:I7=I4)),"False","True")
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269226)
    
5.  ![](https://secure.gravatar.com/avatar/d218c6f0da6af730667ab9baa7b529132461dc13b1c1d81ff4dd1cfbcd43f102?s=64&d=mm&r=g) Jorrie says:
    
    [October 16, 2012 at 2:42 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269330)
    
    Dan u good ! Learned a new thing today.
    
    Here's my new formula
    
    Old Formula: {=IF(SUM(IF(A1=$A:$A,1,0))=COUNTA($A:$A),TRUE,FALSE)}
    
    New Formula: {=SUM(IF(A1=$A:$A,1,0))=COUNTA($A:$A)}
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269330)
    
6.  ![](https://secure.gravatar.com/avatar/24336abf0b11f2a73e2d076bc70ddc09a1fd0e65c35ca985efa97b58d5e8d12b?s=64&d=mm&r=g) Valentin says:
    
    [October 16, 2012 at 4:16 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269398)
    
    your formula with the equal sign to check ceels for equality works correctly with numbers but not with letters.
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269398)
    
    *   ![](https://secure.gravatar.com/avatar/45e6ef71cca2b3044e9df69874b8c8f923dc6bfb6b0718784c17061738192727?s=64&d=mm&r=g) Mike Coffey says:
        
        [October 10, 2013 at 5:34 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-448692)
        
        Should you want to compare cellular equality with letters or text, use the =EXACT(D4,D) The result will be either TRUE or FALSE.
        
        MC
        
        [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-448692)
        
7.  ![](https://secure.gravatar.com/avatar/83378b87fd6b3d87e05c7178c073cee27609f8572cbf04c363692bcb5ccec07d?s=64&d=mm&r=g) shairal says:
    
    [October 16, 2012 at 5:19 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269446)
    
    Quick question, what does the ^ in  
    \=PRODUCT($A:$A)=A1^(COUNTIF($A:$A,A1)) do?
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269446)
    
    *   ![](https://secure.gravatar.com/avatar/f33949dd1ee9bddd9cc98439bbaf453d0e2a575ff4fe35795f06171488148aa1?s=64&d=mm&r=g) Stephen says:
        
        [October 16, 2012 at 7:34 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269545)
        
        ^ is "to the power of  
        e.g. 2\*2 could be written as 2^2  
        2\*2\*2 could be written as 2^3 
        
        [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269545)
        
8.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [James Travers](http://www.mypetbubble.com/)
     says:
    
    [October 16, 2012 at 5:23 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269451)
    
    ^ raises to the power of.  
    But that formula fails for {2,2,1,1} Product is 4, countif is 2, 2^2 is 4 but whilst 2=2 & 1=1, 1<>2.
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269451)
    
9.  ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid K. says:
    
    [October 16, 2012 at 8:15 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269573)
    
    My solution is: **COUNTDIFF(A1:A4,1,)=1**  
    Excel function **COUNTDIFF** counts the number of unique values in a range or an array.  
    **SYNTAX :**  
    **\=COUNTDIFF(Array**,Blanks,Exclude**)**  
    \- **Array** (range or array) : can contain any type of data (numbers, text, empty cells...).  
    \- **Blanks** (boolean, optional) : specifies if empty cells must be taken into account (default : FALSE).  
    \- **Exclude** (value, range or array, optional) : value(s) which must be excluded from the count.  
    Unlike many posted solutions, this function allows handling blank cells.  
     
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269573)
    
    *   ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid K. says:
        
        [October 16, 2012 at 11:30 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269715)
        
        My bad.
        
        **COUNTDIFF** is not Excel build in function, but part of free MoreFunc add-in.  
        [http://download.cnet.com/Morefunc/3000-2077\_4-10423159.html](http://download.cnet.com/Morefunc/3000-2077_4-10423159.html)
          
        A free library of 66 new worksheet functions for Excel 95 or above.
        
        [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269715)
        
10.  ![](https://secure.gravatar.com/avatar/024dde822e78b6bff17a52658a9029aaec6af087294dd5801f9af24d228b97dc?s=64&d=mm&r=g) Andrew says:
    
    [October 16, 2012 at 9:42 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269639)
    
    @leonid
    
    Thank you! this is a great function. Did not know about it. 
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269639)
    
    *   ![](https://secure.gravatar.com/avatar/024dde822e78b6bff17a52658a9029aaec6af087294dd5801f9af24d228b97dc?s=64&d=mm&r=g) Andrew says:
        
        [October 16, 2012 at 9:45 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269644)
        
        Ah must be in 2007+. It no worky in 2003
        
        [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269644)
        
        *   ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid K. says:
            
            [October 16, 2012 at 11:05 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269696)
            
            @Andrew
            
            Did you install Analysis ToolPak?
            
            [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269696)
            
11.  ![](https://secure.gravatar.com/avatar/8be321aa960420aa9f33ad113a37bb9657bb18d6812685cd7a13fdcdd117540b?s=64&d=mm&r=g) jeje says:
    
    [October 17, 2012 at 1:32 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269798)
    
    \=COUNTIF($A$1:$A$4,A1)>1
    
    is this correct? not sure if I understood the question correctly. 
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-269798)
    
12.  ![](https://secure.gravatar.com/avatar/1f39af04164236ece3ed823f30f330f69a2de3c016b10204af752941a386b15b?s=64&d=mm&r=g) Quotenjunkie says:
    
    [October 21, 2012 at 10:06 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-273375)
    
    At the moment I am trying to learn array formulas,
    
    is this also correct ?
    
     {=A1:A4=A1}
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-273375)
    
    *   ![](https://secure.gravatar.com/avatar/1f39af04164236ece3ed823f30f330f69a2de3c016b10204af752941a386b15b?s=64&d=mm&r=g) Quotenjunkie says:
        
        [October 23, 2012 at 7:08 am](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-274943)
        
        sry this was wrong, but the following should work  
        {=MIN((E15:E19=E15)\*1)}
        
        [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-274943)
        
13.  ![](https://secure.gravatar.com/avatar/40b911e650391fe172a3ac297e2a345d2e31c9e0e8bc6b3afb08dde1df648941?s=64&d=mm&r=g) [Ankit](http://www.techsapling.com/)
     says:
    
    [October 22, 2012 at 8:23 pm](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-274591)
    
    Thanks man. You are a live saver 😀
    
    [Reply](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#comment-274591)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/check-cells-for-equality-follow-up-quick-tip/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Last day to join Excel School + Excel Hero Academy](https://chandoo.org/wp/eha-es-last-call/) | [Please help me design our new product: Vitamin XL](https://chandoo.org/wp/vitamin-xl-survey/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)