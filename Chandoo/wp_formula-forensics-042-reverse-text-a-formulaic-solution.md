# Formula Forensics 042: Reverse Text - A Formulaic Solution » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution

---

Formula Forensics 042: Reverse Text – A Formulaic Solution
==========================================================

[Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
 , [Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 - 32 comments

  

Over the xmas break I finally found the time to install Office 365.

One of the new functions that Office 365/Excel 2016 allows is the **Textjoin()** function.

Textjoin takes an array or range of text and joins them together with an optional separator character

eg: =Textjoin(“,”,True,”C”,”h”,”a”,”n”,”d”,”o”,”o”,””,”.”,”o”,”r”,”g”) will return **Chandoo.org**

The use of Textjoin allows for a single celled formulaic solution to the previously impossible Reverse Text problem, as yet unsolved in previous versions of Excel without using VBA.

That is there was no way to reverse a string of text in Excel without using either helper cells or vba

This post looks at the construction of such a function.

### Textjoin()

The Textjoin() function has 3 components as shown in the Excel Help

[![tj001](https://chandoo.org/wp/wp-content/uploads/2017/01/TJ001.png)](https://chandoo.org/wp/wp-content/uploads/2017/01/TJ001.png)

-------------------------------------------------------------------------------------------------------------------------------------

How to Reverse Text
-------------------

Previously in Formula Forensics we have used a simple formula to extract each character of a text string into an array using:

\=MID(B2,ROW(INDIRECT(“1:”&LEN($B$2))),1)

Assuming you have the text **Chandoo.org** in cell B2, Excel will return

\={“C”;”h”;”a”;”n”;”d”;”o”;”o”;”.”;”o”;”r”;”g”}

so each character takes up a single location within the array

We can reverse the order of the array by changing the location of the character during extraction so that instead of taking characters from left to right we take them right to left, by using a small modification to the above formula:

\=MID(B2,LEN(B2)-ROW(INDIRECT(“1:”&LEN($B$2)))+1,1)

Excel returns

\={“g”;”r”;”o”;”.”;”o”;”o”;”d”;”n”;”a”;”h”;”C”}

Now we simply send the array into the Textjoin() function

\=TEXTJOIN(“”,TRUE,MID(B2,LEN(B2)-ROW(INDIRECT(“1:”&LEN($B$2)))+1,1))

Excel returns

gro.oodnahC

Limitations
-----------

Unfortunately the Textjoin() function is only available in the Office 365/Excel 2016 version of Excel and so this will not work in previous versions of Excel.

It would be wonderful of the nice folk at Microsoft to add this and other new functions into future Excel 2013 and Excel 2016 updates!

Download
--------

You can download a copy of the above file and follow along, [Download Here](https://chandoo.org/wp/wp-content/uploads/2017/01/Reverse-Text.xlsx "FF 23 Sample File")
.

Formula Forensics “The Series”
------------------------------

This is the 45th post in the Formula Forensics series.

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic Series](http://chandoo.org/wp/category/formula-forensics/ "The Formula Forensics Series")

Formula Forensics Needs Your Help
---------------------------------

I need more ideas for future Formula Forensics posts and so I need your help.

If you have a neat formula that you would like to share and explain, try putting pen to paper and draft up a Post like above or;

If you have a formula that you would like explained, but don’t want to write a post, send it to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
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
| Written by Hui...  <br>Tags: [INDIRECT()](https://chandoo.org/wp/tag/indirect/)<br>, [len()](https://chandoo.org/wp/tag/len/)<br>, [mid()](https://chandoo.org/wp/tag/mid/)<br>, [row()](https://chandoo.org/wp/tag/row/)<br>, [Textjoin()](https://chandoo.org/wp/tag/textjoin/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 32 Responses to “Formula Forensics 042: Reverse Text – A Formulaic Solution”

1.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [January 4, 2017 at 10:05 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383721)
    
    Just to correct a small misunderstanding.  
    "Exce 365" has these (and a few more) new functions but they are not a part of "Excel 2016".  
    Using the term: "Office 365/Excel 2016" is a little misleading.  
    It seems as if the new functions can be found in BOTH mentioned versions which is not true.  
    "Office 365" is a stand alone application and has nothing to do with the "Excel 2016".  
    To my opinion the best way is to use only the term "Excel 365" as it is going to keep its name for many years and it gets a monthly update incl. new features/functions, from time to time.  
    Thanks.
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383721)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 4, 2017 at 11:16 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383736)
        
        Micky
        
        [https://support.office.com/en-us/article/What-s-the-difference-between-Office-365-and-Office-2016-ed447ebf-6060-46f9-9e90-a239bd27eb96](https://support.office.com/en-us/article/What-s-the-difference-between-Office-365-and-Office-2016-ed447ebf-6060-46f9-9e90-a239bd27eb96)
        
        "Office 365 is a subscription service that includes the most recent version of Office, which currently is Office 2016.  
        It comes with the applications you’re familiar with, like Word, PowerPoint, and Excel, plus extra online storage, ongoing tech support at no extra cost, and more."
        
        So yes, it is Excel 2016 that I use, but it is the Office 365 version of Excel 2016. The new functions are not available in stand alone Excel 2016 versions.
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383736)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [January 4, 2017 at 11:29 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383740)
            
            Hui,  
            With all due respect there is nothing new in your comment.  
            When you mention OFFICE 365/Excel 2016 in "a single breath" this might mislead some of the readers.  
            To my opinion (you may or may not agree) if you want to mention some of Excel 365 New/additional features - it will be good practice NOT TO MENTION THE YEAR 2016.  
            All the above was written from the eyes of the average end user (not you nor me).  
            I rest my case and have nothing more to add (at this point).
            
            [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383740)
            
            *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) [David Hager](https://dhexcel1.wordpress.com/)
                 says:
                
                [January 4, 2017 at 1:17 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383780)
                
                You make a good point, but in a poor tone, IMO. The main problem is that Microsoft marketing is about as clear as mud on this subject. BTW, I have amended several TEXTJOIN articles I wrote this week to include your viewpoint, so thanks!
                
                [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383780)
                
                *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                     says:
                    
                    [January 4, 2017 at 2:31 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383794)
                    
                    Thanx David
                    
                    I have been using Excel 2016 for a couple of years and it was one of your posts i the Forums that reminded me of Textjoin which unfortunately 2016 doesn't include natively.
                    
                    As an MVP we get free access to a 365 Subscription which I implemented last week.
                    
                    So now I use Excel 2016 with a few new functions and facilities with the side effects of having a 365 a/c
                    
                *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [January 4, 2017 at 2:34 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383796)
                    
                    @David,  
                    It is not a secret that English is not my mother's tongue.  
                    Therefore the so called "TONE" should be examined & interpreted as long as the above statement being considered.  
                    Thank you.
                    
                *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) [David Hager](https://dhexcel1.wordpress.com/)
                     says:
                    
                    [January 9, 2017 at 10:20 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1387347)
                    
                    Thanks, Hui! I have written quite a few articles about TEXTJOIN recently. If anyone is interested, visit [https://dhexcel1.wordpress.com/](https://dhexcel1.wordpress.com/)
                    
                *   ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) David Hager says:
                    
                    [January 12, 2017 at 12:02 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1389177)
                    
                    Micky,
                    
                    Did your mother teach you to communicate in ALL CAPS?
                    
2.  ![](https://secure.gravatar.com/avatar/efdd88b16970c70dc36076b434b7288b4d8dfbb1c255a9a2b8314b0d4327e365?s=64&d=mm&r=g) Gino says:
    
    [January 4, 2017 at 11:44 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383744)
    
    Thanks for the post, Hui! I'm just struggling to understand why anyone would ever need to use this formula. The example you used makes sense from a formula approach but do you know of any um, more "real life" reasons why you would use it?
    
    Just seems like an odd function!
    
    Cheers,  
    Gino
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383744)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [January 4, 2017 at 1:51 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383786)
        
        @Gino,  
        Does the linked picture make any sense ?  
        [https://s28.postimg.org/p5uslp1l9/NONAME.png](https://s28.postimg.org/p5uslp1l9/NONAME.png)
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383786)
        
        *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
             says:
            
            [January 4, 2017 at 2:32 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383795)
            
            Thanx Michael
            
            That explains Textjoin but probably doesn't explain why you would need to reverse text in the first place
            
            [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383795)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [January 4, 2017 at 2:35 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383797)
                
                Well, I left something for you "to explain"...
                
                [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383797)
                
        *   ![](https://secure.gravatar.com/avatar/efdd88b16970c70dc36076b434b7288b4d8dfbb1c255a9a2b8314b0d4327e365?s=64&d=mm&r=g) Gino says:
            
            [January 4, 2017 at 7:35 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383872)
            
            Yes, Micky - that really helps me understand it better. So a CONCATENATE on steroids! 🙂
            
            Awesome! And to all this MS stuff about differences between 365 and standalone - maybe MS way of forcing us all eventually to move to a software subscription model?
            
            Probably.
            
            Anyway - thanks, Michael (Micky)! Much appreciated!
            
            [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383872)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [January 5, 2017 at 4:39 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384170)
                
                @Gino,  
                "Great minds think alike".  
                Eventually, this is what MS has in mind.
                
                [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384170)
                
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 5, 2017 at 4:11 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384001)
        
        @Gino
        
        Assume that a company has a production line making widgets  
        its widgets are named A through Z
        
        So next weeks requirements may be listed as DCHGSDCXZX  
        That is we need to make widget D then C then H then G etc widgets
        
        I could imagine that there is a requirement at some stage to know what is last, then second last etc, ie the list in reverse order
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384001)
        
3.  ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
    
    [January 4, 2017 at 2:52 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383801)
    
    Hi  
    or VBA 😉
    
    Option Explicit  
    Function Mirror(z)  
    Dim i As Long, l As Long, temp As String  
    l = Len(z)  
    For i = l To 1 Step -1  
    temp = temp & Mid(z, i, 1)  
    Next i  
    Mirror = temp  
    End Function
    
    Kind regards  
    Stef@n
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383801)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) Hui says:
        
        [January 4, 2017 at 3:07 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383802)
        
        @Stefan
        
        If using VBA simply use
        
        Function Reverse(str As String) As String  
        Reverse = StrReverse(Trim(str))  
        End Function
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383802)
        
        *   ![](https://secure.gravatar.com/avatar/591cb617c7a2fec3fd8ca25733cda79a46fce16174b4325175f1961ba0b8201c?s=64&d=mm&r=g) Stef@n says:
            
            [January 5, 2017 at 3:11 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384144)
            
            😉 is so much easier 😉  
            Thx Hui  
            Regards  
            Stef@n
            
            [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384144)
            
4.  ![](https://secure.gravatar.com/avatar/c72d023366260ebef49fa7df98159f503f920992df6e18250421b1ab86019c06?s=64&d=mm&r=g) John Jairo V says:
    
    [January 4, 2017 at 3:54 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383815)
    
    "The use of Textjoin allows for a formulaic solution to the previously impossible Reverse Text problem, as yet unsolved in previous versions of Excel without using VBA.
    
    That is there was no way to reverse a string of text in Excel without using vba"
    
    I think you should be careful in the way you say it can not be done in Excel. In itself the problem is to do it with a single function, but that can be done, can be with helper cells. Blessings!
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383815)
    
5.  ![](https://secure.gravatar.com/avatar/0446f53a29ce21f4620e930e762bc2f5891b705a22e205ad098b5eb1688ed1d0?s=64&d=mm&r=g) Jon M. says:
    
    [January 4, 2017 at 7:08 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383863)
    
    Wouldn't this formula work? I went out 20 characters, but you could go more if needed. And I admit, it's not as elegant.
    
    A1=Chandoo.org
    
    A2=MID(A1,20,1)&MID(A1,19,1)&MID(A1,18,1)&MID(A1,17,1)&MID(A1,16,1)&MID(A1,15,1)&MID(A1,14,1)&MID(A1,13,1)&MID(A1,12,1)&MID(A1,11,1)&MID(A1,10,1)&MID(A1,9,1)&MID(A1,8,1)&MID(A1,7,1)&MID(A1,6,1)&MID(A1,5,1)&MID(A1,4,1)&MID(A1,3,1)&MID(A1,2,1)&MID(A1,6,1)&MID(A1,1,1)
    
    \-Jon
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383863)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 5, 2017 at 4:08 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383999)
        
        @Jon  
        That formula works if the string is 20 characters long  
        If it is 19 it will have an error  
        If it is 21 it will give the wrong answer
        
        My solution is generic and works regardless of the string length
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1383999)
        
        *   ![](https://secure.gravatar.com/avatar/0446f53a29ce21f4620e930e762bc2f5891b705a22e205ad098b5eb1688ed1d0?s=64&d=mm&r=g) Jon M. says:
            
            [January 5, 2017 at 1:28 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384132)
            
            Self righteous much Hui?
            
            I acknowledged in my post that it max's out at 20, but it is expandable depending on the user's needs; and that it was not as elegant as yours.
            
            Also, my solution does NOT error if it is less than 20, try it (or just look at the formula).
            
            PS. Does your solution does really work regardless of string length? Is it truly free of the maximum number of characters?
            
            [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384132)
            
            *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
                 says:
                
                [January 5, 2017 at 3:39 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384151)
                
                @Jon
                
                Thanx for your comments
                
                [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384151)
                
6.  ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid says:
    
    [January 5, 2017 at 8:19 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384238)
    
    Another option to put together reversed characters is to use the CONCAT function that was also introduced in Excel 2016:  
    \=CONCAT(INDEX(MID($B$2,LEN($B$2)-ROW(INDIRECT("1:"&LEN($B$2)))+1,1),))  
    or array entered  
    \=CONCAT(MID($B$2,LEN($B$2)-ROW(INDIRECT("1:"&LEN($B$2)))+1,1))
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1384238)
    
    *   ![](https://secure.gravatar.com/avatar/0ceda4ad2f79f67afb17ede30f4332b1f4d69e7c4136dd0f0d35036f221e2be4?s=64&d=mm&r=g) Giancarlo says:
        
        [January 7, 2017 at 11:41 pm](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1385856)
        
        Hallo
        
        Unfortunately I do not have Office 365.  
        You can definitely reverse an integer using formula.  
        Tested with Office 2016  
        \=MATR.SOMMA.PRODOTTO(STRINGA.ESTRAI(0&A2;GRANDE(INDICE(VAL.NUMERO(--STRINGA.ESTRAI(A2;RIF.RIGA($1:$15);1))\*  
        RIF.RIGA($1:$15);0);RIF.RIGA($1:$15))+1;1)\*(10^(LUNGHEZZA(A2)+1-RIF.RIGA($1:$15))/10))
        
        \[English translation\]  
        B4: =SUMPRODUCT(MID(0&A4,LARGE(INDEX(ISNUMBER(--MID(A4,ROW($1:$15),1))\*ROW($1:$15),0),ROW($1:$15))+1,1)\*(10^(LEN(A4)+1-ROW($1:$15))/10))
        
        following example  
        [https://onedrive.live.com/view.aspx?resid=E54E0D0F38AE0A9E!1086&ithint=file%2cxlsx&app=Excel&authkey=!AMML3tvo1EmOnOo](https://onedrive.live.com/view.aspx?resid=E54E0D0F38AE0A9E!1086&ithint=file%2cxlsx&app=Excel&authkey=!AMML3tvo1EmOnOo)
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1385856)
        
7.  ![](https://secure.gravatar.com/avatar/4b3206db7dae5bb01d148b28cdb3f96e77c02bd2c9b9723c464be0cc02bfa22b?s=64&d=mm&r=g) Volkan Güven says:
    
    [January 9, 2017 at 10:56 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1387044)
    
    Hi,
    
    If it is okay for you to use third party excel add-ins; ASAP utilities and Kutools has "reverse text" options.
    
    Best Regards
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1387044)
    
8.  ![](https://secure.gravatar.com/avatar/2156393d07c4ddb3d2fe5e7a47a5fa5b034d2857872886ed4c4ee0cdf524d6e1?s=64&d=mm&r=g) [Stephen Lee](https://www.webpixeltechnologies.com/seo-packages/)
     says:
    
    [February 2, 2017 at 9:56 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1401809)
    
    Thanks for sharing! Perkful content got! Keep it up!! I am eager to wait for next writings!
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1401809)
    
9.  ![](https://secure.gravatar.com/avatar/082174b1f8da6ff820622f5e5efd3c298752d503cc853bd963cee1bfb1051001?s=64&d=mm&r=g) Brad Yundt says:
    
    [April 12, 2017 at 3:48 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1436032)
    
    If you want to reverse the order of words in a phrase or sentence, it can be done with TEXTJOIN as well. The following formula may be used, and does not need to be array-entered.  
    \=TEXTJOIN(" ",,INDEX(TRIM(MID(SUBSTITUTE(" " & A1 & " "," ",REPT(" ",LEN(A1))),LEN(A1)\*(LEN(A1)-LEN(SUBSTITUTE(A1," ",""))+2-ROW(INDIRECT("1:" & (LEN(A1)-LEN(SUBSTITUTE(A1," ",""))+1)))),LEN(A1))),))
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1436032)
    
10.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [April 12, 2017 at 6:29 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1436064)
    
    @Brad,  
    As far as I recall - the TEXTJOIN function is only available if you have an "Office 365" subscription.  
    Micky
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1436064)
    
11.  [#Excel Super Links #11 – shared by David Hager | Excel For You](https://dhexcel1.wordpress.com/2017/04/22/excel-super-links-11-shared-by-david-hager/)
     says:
    
    [April 22, 2017 at 11:45 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1439284)
    
    \[…\] [http://chandoo.org/wp/2017/01/04/formula-forensics-042-reverse-text-a-formulaic-solution/](http://chandoo.org/wp/2017/01/04/formula-forensics-042-reverse-text-a-formulaic-solution/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1439284)
    
12.  ![](https://secure.gravatar.com/avatar/3e4e3e90ef10e6c4a83d63f80d2938c3b6926c472865cdcc285709195d9f58b4?s=64&d=mm&r=g) Dan Mayoh says:
    
    [December 6, 2017 at 2:11 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1526342)
    
    Hui, I just came across this post, nice work. The reversal can also be done with the new CONCAT function too.  
    \=CONCAT(MID(B$2,1+LEN($B$2)-ROW(OFFSET($A$1,,,LEN($B$2))),1))
    
    Still the same conclusion though that it makes use of a function that wasn't previously available!  
    Cheers, Dan
    
    [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1526342)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [December 6, 2017 at 2:34 am](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1526346)
        
        @Dan  
        Nice solution also
        
        I wish MS would spread these new'ish functions to all Excel versions rather than leaving them stuck in 365.
        
        [Reply](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#comment-1526346)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/formula-forensics-042-reverse-text-a-formulaic-solution/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Merry Christmas & Happy New Year 2017 \[Holiday Greeting\]](https://chandoo.org/wp/2017-holiday-greeting/) | [Untrimmable Spaces – Excel Formula](https://chandoo.org/wp/untrimmable-spaces-excel-formula/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)