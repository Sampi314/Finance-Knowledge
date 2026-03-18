# Can you extract first name & last name from email address? [Formula Challenge] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/extract-first-name-last-name-from-email

---

Can you extract first name & last name from email address? \[Formula Challenge\]
================================================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 133 comments

  

_**Today lets rescue John Doe from John\_doe@email.com.**_

### Extract first & last name from email address

As you may know, we have an article on [how to extract names from email addresses](http://chandoo.org/wp/2010/01/19/usernames-from-email-formulas/)
. 2 days ago, Joana commented on it saying,

> Not to brag but I created a \[complex\] formula that extracts the names from emails in a much more interesting way. See the examples:
> 
> john\_doe@email.com >> my extract >> John Doe  
> john.doe@email.com >> my extract >> John Doe  
> john321doe@email.com >> my extract >> John Doe

I asked Joana how she did it. And here is the formula she shared ([#](http://chandoo.org/wp/2010/01/19/usernames-from-email-formulas/#comment-471638)
),

![Formula to extract first and last name from email address - shared by Joana](https://img.chandoo.org/hw/joanas-formula-extracting-first-last-name-from-email-address.png)

Yes, it is long. It must have taken a lot of concentration, ninja-level skills to come up with this.  
(Note: The formula is in Portuguese or Spanish version of Excel. So do not try it in English version)

### Here is your challenge.

Given an email address in the format

firstnameany\_non-alphabet.characterslastname@email.com

You need to extract first name & last name using formulas.

**Things to keep in mind:**

*   Assume only English alphabet in names. That means no letters like áèó etc.
*   The email address contains only firstname\_separator\_lastname. No middle name or other prefix or suffix etc.
*   The email address is in A1
*   Assume B1 contains just the name portion of email (ie john\_doe in B1 if A1 contains john\_doe@email.com)
*   In C1 & D1 you need to extract first name & last name.

**Example email addresses:**

*   john\_doe@email.com -> john doe
*   john.doe@email.com -> john doe
*   john123doe@email.com -> john doe
*   john-doe@email.com -> john doe
*   john1964doe@email.com -> john doe

**Sample file**

[Download the sample file](https://img.chandoo.org/hw/extract-name-from-email-challenge.xlsx)
 containing email addresses and expected results. Use it to write your formulas.

**How to post your answers?**

Simple. [Just comment on this post](http://chandoo.org/wp/2014/02/27/extract-first-name-last-name-from-email/#respond)
 with your answers. Tell us how you arrived at the formula, what it does. It will help rest of us understand and use your formulas.

**Special note:** If your formula contains < or \> symbols when posting it, use &lt; and &gt; instead. Our commenting system eats up < and > symbols.

Go ahead and liberate John Doe from john4doe@email.com. We are waiting…

**Want more Excel challenges?**

**[Try this](http://chandoo.org/wp/excel-problems-challenges/)
** – more than 25 challenges and problems in Excel.

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
| Written by Chandoo  <br>Tags: [challenge](https://chandoo.org/wp/tag/challenge/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [text processing](https://chandoo.org/wp/tag/text-processing/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 133 Responses to “Can you extract first name & last name from email address? \[Formula Challenge\]”

1.  ![](https://secure.gravatar.com/avatar/b1c5fa97090a14813a002d45570641951ee79c91b30ff1c0936b7a0e3d9cd907?s=64&d=mm&r=g) JLeno says:
    
    [February 27, 2014 at 9:07 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471838)
    
    Okay, first try:
    
    First name:  
    \=LEFT(C4,MIN(IF((CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1))91)\*(CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1))122),ROW(INDIRECT("1:"&LEN(C4)))))-1)
    
    Last name:  
    \=RIGHT(C4,LEN(C4)-MAX(IF((CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1))91)\*(CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1))122),ROW(INDIRECT("1:"&LEN(C4))))))
    
    (array entered!)
    
    Key is the CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1)) part, which does the following:
    
    MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1) splits the text to 1 character string texts  
    CODE(x) converts all text strings to ASCII codes
    
    The logical test checks all ASCII codes, if they are not between 65 and 90 or between 97 and 122 then it is a nontext character.
    
    The formula uses the first and last nontext character position in the LEFT and RIGHT statements.
    
    I'm not sure if there are any optimisations possible, or perhaps even a totally different approach?
    
    Nice challenge by the way 🙂
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471838)
    
2.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
     says:
    
    [February 27, 2014 at 9:08 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471839)
    
    on the fly ...
    
    B1=LEFT(A1,FIND("@",A1)-1)
    
    C1=LEFT(B1,MIN(IF(ISERROR(FIND(MID(B1,ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99)))-1)
    
    D1=RIGHT(B1,LEN(B1)-MAX(IF(ISERROR(FIND(MID(B1&REPT("a",100),ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99))))
    
    regards  
    r
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471839)
    
3.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
     says:
    
    [February 27, 2014 at 9:38 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471841)
    
    ops ... find is case-sensitive ... replace with SEARCH
    
    C1=LEFT(B1,MIN(IF(ISERROR(SEARCH(MID(B1,ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99)))-1)
    
    D1=RIGHT(B1,LEN(B1)-MAX(IF(ISERROR(SEARCH(MID(B1&REPT("a",100),ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99))))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471841)
    
4.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
     says:
    
    [February 27, 2014 at 9:50 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471843)
    
    shorten the formula in D1  
    \=MID(B1,MAX(IF(ISERROR(SEARCH(MID(B1&REPT("a",99),ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99)))+1,99)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471843)
    
    *   ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra says:
        
        [February 28, 2014 at 10:39 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471969)
        
        @ Roberto Mensa  
        your lastname formula gives both first name and last name.  
        With Regards  
        Rudra
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471969)
        
        *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
             says:
            
            [February 28, 2014 at 10:55 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471971)
            
            Hi Rudra,  
            I forgot to mention that the formulas must be confirmed with Ctrl + Shift + Enter  
            however, to avoid misunderstandings here a sample file with my formulas:  
            [https://sites.google.com/site/e90e50/scambio-file/mail1.xlsx](https://sites.google.com/site/e90e50/scambio-file/mail1.xlsx)
              
            regards  
            r
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471971)
            
            *   ![](https://secure.gravatar.com/avatar/1ff93dd3ee4c61141b7601f4816cd0cb2558f03841f88b0c7bc4e07905bf8ffa?s=64&d=mm&r=g) Venkat says:
                
                [February 28, 2014 at 3:28 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472011)
                
                You are awesome, the file with the formulas for extracting first name, last name and full name are tremendous!!
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472011)
                
5.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [February 27, 2014 at 9:58 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471844)
    
    First Name  
    \=MID(C4,1,MIN(IFERROR(FIND(CHAR(ROW($1:$95)),C4),FALSE))-1)  
    Last Name  
    \=MID(C4,MAX(IFERROR(FIND(CHAR(ROW($1:$95)),C4),FALSE))+1,LEN(C4))  
    C4 - having the formula  
    \=LOWER(LEFT(B4,FIND("@",B4)-1))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471844)
    
6.  ![](https://secure.gravatar.com/avatar/90d6e5a60dc393ba190b6fec95456b4f5bc058ee95919583b8fed4e65c32043c?s=64&d=mm&r=g) sam says:
    
    [February 27, 2014 at 10:09 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471846)
    
    Sorry the Last Name needs to be changed
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471846)
    
7.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 27, 2014 at 10:34 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471848)
    
    Note sure if this was open to everybody, so just trying my luck. I would have used followed suit and used  
    B1=LEFT(A1,FIND("@",A1)-1), but just for posterity, I'll use the one below
    
    B1=REPLACE(A1,FIND("@",A1),255,"")
    
    C1=LEFT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),ROW(OFFSET(A$1,,,LEN(B1))),1))90),)-1) {array}
    
    D1=RIGHT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),LEN(B1&" ")-ROW(OFFSET(A$1,,,LEN(B1))),1))90),)-1){array}
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471848)
    
8.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 27, 2014 at 10:37 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471849)
    
    Something's wrong with the posting Chandoo. Some text is being replaced / truncated. My solution is only showing half the formula!!
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471849)
    
9.  ![](https://secure.gravatar.com/avatar/9b8e5816a2081bdd7a9b450e36cf5278025ce707d4b54711bd96f4da7edddf0e?s=64&d=mm&r=g) [Stéphane](http://justdocsit.blogspot.com/)
     says:
    
    [February 27, 2014 at 10:41 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471850)
    
    Hi
    
    I made this exercise for Google Spreadsheet  
    \=split(index(split(A1;"@");1;1);REGEXEXTRACT(index(split(A1;"@");1;1);"\[0-9\_.-\]+"))
    
    For french reader : [http://justdocsit.blogspot.com/2014/02/extraire-le-prenom-et-le-nom-dun-email.html](http://justdocsit.blogspot.com/2014/02/extraire-le-prenom-et-le-nom-dun-email.html)
    
    Stéphane
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471850)
    
10.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 27, 2014 at 10:46 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471851)
    
    I'll try again. Hope this one works.
    
    '=LEFT(A1,FIND("@",A1)-1)
    
    '=LEFT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),ROW(OFFSET(A$1,,,LEN(B1))),1))<90),)-1)
    
    '=RIGHT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),LEN(B1&" ")-ROW(OFFSET(A$1,,,LEN(B1))),1))<90),)-1)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471851)
    
11.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 27, 2014 at 10:47 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471852)
    
    Nope! something wrong. text getting removed.... probably has something to do with the +, >, < characters... not sure
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471852)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 27, 2014 at 1:42 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471863)
        
        @Sam  
        Always put a space before and after a GE or LT sign
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471863)
        
12.  ![](https://secure.gravatar.com/avatar/bcf7980c24fe38795c1e9a0c2b60096de9a65aadc3a05ffd5017c3fcde1cc77a?s=64&d=mm&r=g) SHUSHU says:
    
    [February 27, 2014 at 11:53 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471858)
    
    Sam,  
    Try to take a snapshot from your worksheet where you will show the formulas as text and/or comments.  
    Upload the picture to some file hosting site and present' us' the link.  
    SHUSHU
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471858)
    
13.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [February 27, 2014 at 2:04 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471865)
    
    @Sam,  
    Take a snapshot of your sheet after presenting the formula(s) as TEXT + put the formulas into their cell comments.  
    Then, upload the picture to a file hosting site and return to present the link to that picture  
    Michael
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471865)
    
14.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
     says:
    
    [February 27, 2014 at 2:42 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471867)
    
    as Joana's formula this one return first & last name separated by a space ... however it is a bit shorter 🙂  
    mail address in A1:  
    \=REPLACE(LEFT(A1,FIND("@",A1)-1),MIN(IF(ISERROR(SEARCH(MID(A1,ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")),ROW($1:$99))),SUM(--ISERROR(SEARCH(MID(LEFT(A1,FIND("@",A1)-1),ROW($1:$99),1),"qwertyuiopasdfghjklzxcvbnm")))," ")
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471867)
    
15.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 27, 2014 at 5:07 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471880)
    
    OK, trying Hui's suggestion
    
    \=LEFT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),ROW(OFFSET(A$1,,,LEN(B1))),1)) 90),)-1)
    
    \=RIGHT(UPPER(B1),MATCH(1,(CODE(MID(UPPER(B1),LEN(B1&" ")-ROW(OFFSET(A$1,,,LEN(B1))),1)) 90),)-1)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471880)
    
16.  ![](https://secure.gravatar.com/avatar/4dd750916a9ada60351e061eb94759569e284a134136746007641b1d84bb5e6c?s=64&d=mm&r=g) [XLarium](https://plus.google.com/b/111273925303719415801/)
     says:
    
    [February 27, 2014 at 7:12 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471888)
    
    Hi
    
    My humble contribution.
    
    In C1:  
    {=LEFT(B1,MATCH(0,COUNTIF($Z$1:$Z$26,MID(B1,COLUMN(1:1),1)),0)-1)}
    
    In D1:  
    {=MID(B1,LEN(C1)+MATCH(1,COUNTIF($Z$1:$Z$26,MID(SUBSTITUTE(B1,C1,""),COLUMN(1:1),1)),0),999)}
    
    Z1:Z26 house the valid characters A..Z.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471888)
    
17.  ![](https://secure.gravatar.com/avatar/5fe66d1b524b2fa578600cdebd109c355494f7e4052dd281f2e27adeb9f479c4?s=64&d=mm&r=g) [Dan](http://www.ofoinc.org/)
     says:
    
    [February 27, 2014 at 7:34 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471890)
    
    \=LEFT(B1,SEARCH("\_",B1)-1)  
    \=RIGHT(B1,LEN(B1)-SEARCH("\_",B1,1))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471890)
    
18.  ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
    
    [February 27, 2014 at 8:02 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471896)
    
    Looks like others may have come up with similar:  
    \=LEFT(C4,MIN(IF(((CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))&lt97)+(CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))&gt122)),ROW(INDIRECT("1:"&LEN(C4)))))-1)
    
    \=MID(C4,MAX(IF(((CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))&lt97)+(CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))&gt122)),ROW(INDIRECT("1:"&LEN(C4)))))+1,999)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471896)
    
    *   ![](https://secure.gravatar.com/avatar/bed2121b2fafbf45b2c69182e2891360f3b806bf22d5f3e67313d4d671bea0d7?s=64&d=mm&r=g) Luke M says:
        
        [February 27, 2014 at 8:03 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471898)
        
        Bah, missed the semicolon. And to clarify, these are array formulas:  
        \=LEFT(C4,MIN(IF(((CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))<97)+(CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))>122)),ROW(INDIRECT("1:"&LEN(C4)))))-1)
        
        \=MID(C4,MAX(IF(((CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))<97)+(CODE(MID(LOWER(C4),ROW(INDIRECT("1:"&LEN(C4))),1))>122)),ROW(INDIRECT("1:"&LEN(C4)))))+1,999)
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471898)
        
        *   ![](https://secure.gravatar.com/avatar/92f6db045719630ef748b06e7407ae1e40df13f0f57d447085d4cd3dbce5ba63?s=64&d=mm&r=g) Nitin Verma says:
            
            [January 25, 2016 at 5:46 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1126464)
            
            Nice One..:)  
            Really healpfull
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1126464)
            
19.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
     says:
    
    [February 27, 2014 at 8:10 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471900)
    
    First Name:
    
    {=LEFT(C4,MATCH(1,--(CODE(MID(C4,ROW($1:$99),1)) lt; 96),)-1)}
    
    Last Name:
    
    \=MID(C5,LOOKUP(1,1/(CODE(MID(C5,ROW($1:$99),1)) lt; 96),ROW($1:$99))+1,99)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471900)
    
20.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
     says:
    
    [February 27, 2014 at 8:14 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471902)
    
    First Name:
    
    {=LEFT(C4,MATCH(1,–(CODE(MID(C4,ROW($1:$99),1)) <96),)-1)}
    
    Last Name:
    
    \=MID(C5,LOOKUP(1,1/(CODE(MID(C4,ROW($1:$99),1)) <96),ROW($1:$99))+1,99)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471902)
    
21.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
     says:
    
    [February 27, 2014 at 8:16 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471903)
    
    OK. Last attempt to get past the comment parser...
    
    First Name:
    
    {=LEFT(C4,MATCH(1,- -(CODE(MID(C4,ROW($1:$99),1)) <96),)-1)}
    
    Last Name:
    
    \=MID(C4,LOOKUP(1,1/(CODE(MID(C4,ROW($1:$99),1)) <96),ROW($1:$99))+1,99)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471903)
    
    *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
         says:
        
        [February 28, 2014 at 4:11 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472015)
        
        Ciao Daniel,  
        good to see you!  
        your formula is brilliant, as always ... I think we can still remove some characters  
        {=LEFT(B2,MATCH(1=1,MID(B2,ROW($1:$99),1) < "a",)-1)}  
        what do you think?
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472015)
        
    *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
         says:
        
        [February 28, 2014 at 4:35 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472019)
        
        and for lastname:  
        \=RIGHT(B2,MATCH(1=1,MID(B2,LEN(B2)-ROW($1:$99),1)<"a",))  
        🙂
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472019)
        
        *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50fx/)
             says:
            
            [February 28, 2014 at 4:53 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472020)
            
            ops ...  
            I forgot it is array formula too:  
            {=RIGHT(B2,MATCH(1=1,MID(B2,LEN(B2)-ROW($1:$99),1)<"a",))}
            
            here the new file:  
            [https://sites.google.com/site/e90e50/scambio-file/mail2.xlsx](https://sites.google.com/site/e90e50/scambio-file/mail2.xlsx)
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472020)
            
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
         says:
        
        [February 28, 2014 at 5:00 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472021)
        
        Hi Roberto.
        
        Both very good. I should have thought of eliminating the CODE() function by comparing to the literals!
        
        As for the Last Name, I was seduced by the LOOKUP() function's ability to find the last match in an unsorted list without array-formula confirmation while at the same time ignoring error values. But no doubt, your approach is more succinct.
        
        Great job.
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472021)
        
        *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
             says:
            
            [March 1, 2014 at 10:31 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472189)
            
            @Daniel thanks!  
            what I like is that the formulas are very similar ... just working in a specular way 🙂
            
            This last formula:  
            [http://goo.gl/LpFoog](http://goo.gl/LpFoog)
              
            returns name and last name separated by a space. It work directly from the email address (without support) ... it is assumed that the email address is a real address and then uses only the allowed characters
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472189)
            
22.  ![](https://secure.gravatar.com/avatar/abaf422cb25118c380a4710155a3800b31b49313961f2978cb138c861ce0e93a?s=64&d=mm&r=g) Mike Daniels says:
    
    [February 28, 2014 at 12:09 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471921)
    
    I did them separately:  
    [john\_doe@eamile.com](mailto:john_doe@eamile.com)
    : =CONCATENATE(LEFT(B2,4)," ",(MID(B2,6,3)))  
    [john.doe@email.com](mailto:john.doe@email.com)
    : =CONCATENATE(LEFT(B3,4)," ",(MID(B3,6,3)))  
    Hope you get the picture.  
    Fun to do - thanks.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471921)
    
    *   ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra says:
        
        [February 28, 2014 at 10:43 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471970)
        
        your formula is hardcoded, it will not work in the longer/shorter names...
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471970)
        
        *   ![](https://secure.gravatar.com/avatar/abaf422cb25118c380a4710155a3800b31b49313961f2978cb138c861ce0e93a?s=64&d=mm&r=g) Mike Daniels says:
            
            [February 28, 2014 at 4:17 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472017)
            
            Correct, but that was not the assignment. 🙂
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472017)
            
            *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
                 says:
                
                [March 1, 2014 at 3:26 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472092)
                
                nope.. that _was_ the assignment.
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472092)
                
23.  ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.wordpress.com/)
     says:
    
    [February 28, 2014 at 3:08 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471933)
    
    D4:  
    \=LEFT(C4,MATCH(TRUE,LOOKUP(CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1)),{0;65;91;97;123},{"nontext";"text";"nontext";"text";"nontext"})="nontext",0)-1)  
    CTRL SHIFT ENTER
    
    E4:  
    \=RIGHT(C4,LEN(C4)-MAX(IF(LOOKUP(CODE(MID(C4,ROW(INDIRECT("1:"&LEN(C4))),1)),{0;65;91;97;123},{"nontext";"text";"nontext";"text";"nontext"})="nontext",ROW(INDIRECT("1:"&LEN(C4))))))  
    CTRL SHIFT ENTER
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471933)
    
24.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 28, 2014 at 5:54 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471944)
    
    One more attempt to escape from the parser
    
    \`C1=LEFT(B6,MATCH(1,--(ISNA(MATCH(CODE(MID(UPPER(B6),ROW($1:$99),1)),ROW($65:$90),))),)-1)
    
    \`D1=RIGHT(B6,MATCH(1,--(ISNA(MATCH(CODE(MID(UPPER(B6),LEN(B6&0)-ROW(OFFSET(A$1,,,LEN(B6))),1)),ROW($65:$90),))),)-1)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471944)
    
25.  ![](https://secure.gravatar.com/avatar/264475311ad5a4e3fd8d67bd93e44458e316c365b07c19d322f266f10f300663?s=64&d=mm&r=g) Istiyak Shaikh says:
    
    [February 28, 2014 at 6:26 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471948)
    
    Is there any solution for below
    
    [Johndoe@gmail.com](mailto:Johndoe@gmail.com)
    
    Regards,  
    Istiyak
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471948)
    
    *   ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.wordpress.com/)
         says:
        
        [February 28, 2014 at 1:38 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471990)
        
        C1: John  
        D1: Doe
        
        ;p
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471990)
        
        *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
             says:
            
            [February 28, 2014 at 2:01 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471999)
            
            @MF  
            First name: =MID(A1,FIND(": ",A1)+2,FIND(" ",A1,FIND(": ",A1)+2)-FIND(": ",A1)-2)  
            Second Name: =MID(A1,FIND(": ",A1,FIND(" ",A1,FIND(": ",A1)+2)-FIND(": ",A1))+2,FIND(";",A1)-(FIND(": ",A1,FIND(" ",A1,FIND(": ",A1)+2)-FIND(": ",A1))+3))
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-471999)
            
            *   ![](https://secure.gravatar.com/avatar/264475311ad5a4e3fd8d67bd93e44458e316c365b07c19d322f266f10f300663?s=64&d=mm&r=g) Istiyak Shaikh says:
                
                [March 1, 2014 at 3:25 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472153)
                
                Getting Error;
                
                Incorrect Formula.
                
                Regards  
                Istiyak
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472153)
                
            *   ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.wordpress.com/)
                 says:
                
                [March 3, 2014 at 2:26 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472312)
                
                @Hui,  
                Have I lost something? I couldn't FIND anything... 🙂
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472312)
                
26.  ![](https://secure.gravatar.com/avatar/abaf422cb25118c380a4710155a3800b31b49313961f2978cb138c861ce0e93a?s=64&d=mm&r=g) Mike Daniels says:
    
    [February 28, 2014 at 4:15 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472016)
    
    Hello Everyone,  
    While I'm impressd with some of the answers given, it is always my preference to keep things simple and "elegant". It is unlikely that I would have to work with a data set containing so many different iterations of an email address; more likely one or two. I humbly submit my answers below. They are constructed from my Chandoo Excel Lessons, which are helping me become AWSOME in Excel. Thank you.
    
    [john\_doe@email.com](mailto:john_doe@email.com)
     =CONCATENATE(LEFT(B2,4)," ",MID(B2,6,3))  
    [john.doe@email.com](mailto:john.doe@email.com)
     =CONCATENATE(LEFT(B3,4)," ",MID(B3,6,3))  
    [john123doe@email.com](mailto:john123doe@email.com)
     =CONCATENATE(LEFT(B4,4)," ",MID(B4,8,3))  
    [john-doe@email.com](mailto:john-doe@email.com)
     =CONCATENATE(LEFT(B5,4)," ",MID(B5,6,3))  
    [john1964doe@email.com](mailto:john1964doe@email.com)
     CONCATENATE(LEFT(B6,4)," ",MID(B6,9,3))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472016)
    
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
         says:
        
        [February 28, 2014 at 11:14 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472068)
        
        Hi Mike.
        
        It is with respect that I mention this. Please try to accept challenges such as this one as an opportunity to learn by pushing your understanding.
        
        Elegant solutions are concise but at the same time work over a generalized problem domain. Perhaps you will never have such a dataset to work on, but the solutions shown here work in an infinite number of scenarios that have nothing to do with email addresses.
        
        Hardcoding splice points to a string is anything but generalized as your small sampling of formulas demonstrate. It is extremely unlikely that all of your addresses have John for the first name, or even a four-letter first name.
        
        The challenge here is to create ONE formula that will work with first and last names of any length and that ONE formula can simply be copied down a column adjacent to the addresses. This is actually pretty simple, but this particular challenge is a little more interesting as the type of non-alpha characters and the number of them used within any give address is unknown, so the formula must manage that as well.
        
        Again, the tactics used to solve this can be used in an infinite number of Excel scenarios that have nothing to do with email addresses.
        
        You will become exponentially more productive when you learn how to wield advanced Excel techniques.
        
        .
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472068)
        
27.  ![](https://secure.gravatar.com/avatar/9b8723ca6877f342070e9890dd6f016689977ff14ceca7016d9fdf3d50ffa1c5?s=64&d=mm&r=g) steven portman says:
    
    [February 28, 2014 at 4:29 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472018)
    
    I looked around and found a solution for this somewhere.
    
    I tried this;
    
    First name: =MID(A1,FIND("john",A1),LEN(A1)-FIND("l.com",A1))  
    Last name: =MID(A1,FIND("doe",A1),LEN(A1)-FIND(".com",A1))
    
    Seems to work. Don't know why though (I'm a newbie).  
    Just need to remember the "FIND" is case sensitive.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472018)
    
28.  ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
    
    [February 28, 2014 at 5:10 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472022)
    
    Can someone tell me why nobody is considering the characters {, |, }
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472022)
    
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
         says:
        
        [February 28, 2014 at 5:15 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472023)
        
        MF did.
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472023)
        
        *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
             says:
            
            [February 28, 2014 at 5:57 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472029)
            
            But building on Roberto's solutions should handle the pipe character and anything else you might wish to throw at it:
            
            First Name:  
            {=LEFT(C4,MATCH(1,(MID(C4,ROW($1:$99),1) < "a")+(MID(C4,ROW($1:$99),1) > "z"),)-1)}
            
            Last Name:  
            {=RIGHT(C4,MATCH(1,(MID(C4,LEN(C4)-ROW($1:$99),1) < "a")+(MID(C4,LEN(C4)-ROW($1:$99),1) > "z"),))}
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472029)
            
            *   ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
                
                [February 28, 2014 at 8:16 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472048)
                
                nice
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472048)
                
            *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
                 says:
                
                [February 28, 2014 at 10:22 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472059)
                
                However, if I'm not mistaken, the characters you can use in an e-mail address are:  
                \[a-z\]  
                \[A-Z\]  
                \[0-9\]  
                \-  
                \_  
                .  
                so that the formulas with 122\]1,\[122\]1,\[122\]1,\[<97\]1," for non-English versions ...  
                here the file:  
                [https://sites.google.com/site/e90e50/scambio-file/mail3.xlsx](https://sites.google.com/site/e90e50/scambio-file/mail3.xlsx)
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472059)
                
                *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
                     says:
                    
                    [February 28, 2014 at 10:32 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472061)
                    
                    ummm bad Editor for the formulas ... these are what I posted above  
                    [https://sites.google.com/site/e90e50/scambio-file/formule.png](https://sites.google.com/site/e90e50/scambio-file/formule.png)
                    
                *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
                     says:
                    
                    [March 1, 2014 at 3:36 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472155)
                    
                    Very cool, Roberto.
                    
                    Number formatting uses semicolons in the English language version of Excel as well, so the Italian version of the formula is the correct one for us as well.
                    
                *   ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
                     says:
                    
                    [March 1, 2014 at 9:58 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472184)
                    
                    @Daniel  
                    oh, really? this is a good news for me. Thanks
                    
                *   ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
                    
                    [March 2, 2014 at 12:19 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472251)
                    
                    Innovative Roberto. I was trying something similar with MID(B2,ROW($1:$99),1)={" < a>z"}, but you've beat me to it.
                    
                    Also, was wondering if I can modify your formula slightly to cover capital letters also
                    
                    \`=MATCH(1,--TEXT(CODE(MID(UPPER(B2),ROW($1:$99),1)),"\[>90\]1;\[<65\]1"),)
                    
                *   ![](https://secure.gravatar.com/avatar/2b93f38c84c784c95940ee204174d1e0278600001d8de2a382d71ffdcf6d12c3?s=64&d=mm&r=g) Sam Mathai Chacko says:
                    
                    [March 2, 2014 at 12:22 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472253)
                    
                    '=MID(B2,ROW($1:$99),1)={"< a>z"} (what I was trying to post above)
                    
                *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
                     says:
                    
                    [March 3, 2014 at 3:26 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472316)
                    
                    Awesome formula Roberto...
                    
29.  ![](https://secure.gravatar.com/avatar/d2954e5601f6f56fa999994db2d404869feba5181b6b78ddfe0ab2a03b249bb8?s=64&d=mm&r=g) [Joana Pereira](http://dentistaemlisboa.com/)
     says:
    
    [March 1, 2014 at 1:24 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472078)
    
    Well I never though my formula would cause such an impact...lol
    
    I have to say I'm not an Excel expert, very far from it and I see that there are already much better ways to do what I needed to do, which was to locale and extract names from emails.
    
    Let me just say that this came up when a company I work for needed to email their 20k email list and I suggested they would personalize each email. Guess who got to extract the names. I said to my boss, well this will take me all week, but, 2 hours latter it was done 🙂 (not getting a raise though...lol)
    
    Glad to see so much people involved in this, keep it up 🙂
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472078)
    
30.  ![](https://secure.gravatar.com/avatar/d05a179a7746f889b341da9222366f671482924bbe21fd1bd7f3a7acc8c6b0c5?s=64&d=mm&r=g) Aaron says:
    
    [March 1, 2014 at 10:32 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472190)
    
    The code below is a bit long, but it creates a full index array of all available text characters to compare vs. the non text characters. Then it uses the smallest indexed to extract the first name, and the 2nd and 3rd kth largest to extract the last name. Works well for all variants of the email addresses given.
    
    LEFT(B10;MIN(IF((N(ISERROR(MATCH(CODE(MID(B10;ROW(OFFSET($A$1;;;LEN(B10)));1));IF(ROW(OFFSET($A$1;64;;52))>90;0;ROW(OFFSET($A$1;64;;52)))+IF(ROW(OFFSET($A$1;70;;52))0;N(ISERROR(MATCH(CODE(MID(B10;ROW(OFFSET($A$1;;;LEN(B10)));1));IF(ROW(OFFSET($A$1;64;;52))>90;0;ROW(OFFSET($A$1;64;;52)))+IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+IF(ROW(OFFSET($A$1;70;;52))<97;0;ROW(OFFSET($A$1;70;;52)));0)))\*ROW(OFFSET($A$1;;;LEN(B10)));3)+1))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472190)
    
    *   ![](https://secure.gravatar.com/avatar/d05a179a7746f889b341da9222366f671482924bbe21fd1bd7f3a7acc8c6b0c5?s=64&d=mm&r=g) Aaron says:
        
        [March 1, 2014 at 10:55 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472192)
        
        I tried to break the monster formula below due to the missing parts above. Learning how to post here :). When you see it broken down below, you can see the main context of the formula repeats. I just use SMALL and LARGE to find the indexes for the LEFT and MID formulas.
        
        EXTRACT THE FIRST NAME USING THE LEFT FORMULA
        
        \=LEFT(B4;
        
        FIND THE MINIMUM INDEXED NON CHARACTER
        
        MIN(IF((N(ISERROR(MATCH(CODE(MID(B4;ROW(OFFSET($A$1;;;LEN(B4)));1));
        
        IF(ROW(OFFSET($A$1;64;;52))>90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))0;
        
        N(ISERROR(MATCH(CODE(MID(B4;ROW(OFFSET($A$1;;;LEN(B4)));1));
        
        IF(ROW(OFFSET($A$1;64;;52))>90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))<97;0;ROW(OFFSET($A$1;70;;52)));0)))  
        \*ROW(OFFSET($A$1;;;LEN(B4)));3)+1))
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472192)
        
31.  ![](https://secure.gravatar.com/avatar/d05a179a7746f889b341da9222366f671482924bbe21fd1bd7f3a7acc8c6b0c5?s=64&d=mm&r=g) Aaron says:
    
    [March 1, 2014 at 10:59 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472193)
    
    Ok, i can not post my glorious monster formula, so I will just add a link to the workbook in dropbox
    
    [https://dl.dropboxusercontent.com/u/2950543/extract-name-from-email-challenge-Aaron.xlsx](https://dl.dropboxusercontent.com/u/2950543/extract-name-from-email-challenge-Aaron.xlsx)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472193)
    
    *   ![](https://secure.gravatar.com/avatar/d05a179a7746f889b341da9222366f671482924bbe21fd1bd7f3a7acc8c6b0c5?s=64&d=mm&r=g) Aaron says:
        
        [March 2, 2014 at 8:40 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472232)
        
        1) Extract all string characters to array (range X)  
        MID(B4;ROW(OFFSET($A$1;;;LEN(B4)));1)
        
        2) convert all array characters to unicode  
        CODE(X)
        
        3) Create array of unicode text for comparison  
        ROW(OFFSET($A$1;64;;52))  
        ROW(OFFSET($A$1;70;;52))
        
        4) Use IF to remove unicode out of range and combine arrays with addition (range Y)  
        IF(ROW(OFFSET($A$1;64;;52))>90;0;ROW(OFFSET($A$1;64;;52)))+  
        IF(ROW(OFFSET($A$1;70;;52))0; Z))-1)
        
        7) For the last name, use the same procedure but remove the right text from the string after "@".  
        LEFT(B4;SEARCH("@";B4)-1);
        
        8) Find the number of characters in the right side of the string by subtracting the MAX non-text indexed position from the length of the string. Replace all string length references with the adjustment in step 7.  
        RIGHT("Step 7"; LEN("Step 7") - MAX(IF(Z>0;Z)))
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472232)
        
32.  ![](https://secure.gravatar.com/avatar/cf7f2e589330fe8c4f4e5ea738e426d9acecdba49514ba340aa46c1cdb1eff74?s=64&d=mm&r=g) XOR LX says:
    
    [March 2, 2014 at 7:49 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472229)
    
    \=LEFT(A1,MATCH(TRUE,INDEX(ABS(110-CODE(MID(A1,ROW($1:$99),1)))>13.5,,),0)-1)
    
    Regards
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472229)
    
33.  ![](https://secure.gravatar.com/avatar/cf7f2e589330fe8c4f4e5ea738e426d9acecdba49514ba340aa46c1cdb1eff74?s=64&d=mm&r=g) XOR LX says:
    
    [March 2, 2014 at 7:55 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472230)
    
    Correction, for symmetry:
    
    \=LEFT(A1,MATCH(TRUE,INDEX(ABS(109.5-CODE(MID(A1,ROW($1:$99),1)))>12.5,,),0)-1)
    
    Regards
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472230)
    
34.  ![](https://secure.gravatar.com/avatar/782dcb7bcfbc54c350deb8694677851a6492f7a9ee3c5b9b94c2f3bcaa5359d3?s=64&d=mm&r=g) ilana says:
    
    [March 2, 2014 at 8:30 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472231)
    
    Sorry. but I think that you are working too hard. Save it to text file, replace separator between first name and last name with @, open the file from Excel with Delimited option and @ as separator.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472231)
    
35.  ![](https://secure.gravatar.com/avatar/f6fb631cb5af8ef896c056c59eee762e3c8aebb9b7f99c46044a735449aaa449?s=64&d=mm&r=g) Jeanbar says:
    
    [March 2, 2014 at 9:43 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472235)
    
    To follow Stéphane's example on regular expressions (but using Excel):
    
    First name : ExtractSentence(RC3;"^(\[a-z\]\*).\*$")
    
    Last name : =ExtractSentence(RC3;"^\[a-z\]\*\[^a-z\]\*(\[a-z)\]\*).\*$")
    
    The ExtractSentence function just activates the Microsoft VBScript Regular Expressions Reference 5.5.
    
    The first argument is the reference of the data  
    The second argument is the "pattern" identifying the substring (in parentheses) within a string of characters.
    
    It can be read like :
    
    "First Name: from the beginning, fetch any consecutive alphabetical character \[a-z\] and forget the remaining characters starting with a non-alphabetical character";
    
    "Last Name : from the beginning, skip any consecutive alphabetical character followed by any consecutive non-alphabetical character, then fetch any consecutive alphabetical character (the name) and skip the remaining characters (starting with the non-alphabetical character @)".
    
    Link: [https://drive.google.com/file/d/0ByQ7-BavxWcNYVNaSmNKdWNISmc/edit?usp=sharing](https://drive.google.com/file/d/0ByQ7-BavxWcNYVNaSmNKdWNISmc/edit?usp=sharing)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472235)
    
36.  ![](https://secure.gravatar.com/avatar/892a728e01c28466e5c67cd51f882f5031799ef20b8874be859f595a8cd5735c?s=64&d=mm&r=g) Tom Cairns says:
    
    [March 3, 2014 at 4:29 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472385)
    
    A bit longwinded, but if column C is  
    \=LOWER(LEFT(B2, FIND("@", B2)-1)  
    and column b is the email addresses  
    then I made an 80 character equivalent of the "name" part in column d by using  
    \=REPT("\_", 80-len(c2))&c2
    
    in column e I calculate the number of non-alpha characters  
    {=SUM(--(CODE(MID(D24,ROW($A$1:$A$80),1)) <97))}
    
    And in column F I find the last non-alpha character
    
    {=MAX(--(CODE(MID(d23,ROW($A$1:$A$80),1)) <97)\*ROW($A$1:$A$80))}
    
    Then the last name in column H is just  
    \=right(d2, 80-f2)
    
    And the first name in column G is just  
    \=left(c2, f2-e2)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472385)
    
37.  ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark Duchesne says:
    
    [March 4, 2014 at 2:04 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472433)
    
    This was a tricky one and had me stumped for days.
    
    This will extract the first name. Havnt even tried to work out the second name yet....
    
    B6 = cell with the email  
    Formula is entered as an array
    
    Originally i was missing the parenthesis for the individual expressions causing excel to evaluate an unintended result. After adding the brackets it worked!
    
    \=LEFT(B6,MIN(IF((CODE(MID(B6,ROW(INDIRECT("1:"&LEN(B6))),1))122),ROW(INDIRECT("1:"&LEN(B6))),""))-1)
    
    I love it how everyone thinks so differently, great to see so many different ways of arriving at the same result.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472433)
    
38.  ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark Duchesne says:
    
    [March 4, 2014 at 10:01 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472471)
    
    Here was my working to extract the second name, not pretty but it works 🙂
    
    \=RIGHT(LEFT(B10,SEARCH("@",B10)-1),(SEARCH("@",B10)-1)-MAX(IF((CODE(MID(B10,ROW(INDIRECT("1:"&(SEARCH("@",B10)-1))),1))122),ROW(INDIRECT("1:"&(SEARCH("@",B10)-1))),"")))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472471)
    
39.  ![](https://secure.gravatar.com/avatar/b69adf3e745981f473ae08cc1c128b308e4083241c96f3b2d0ebfe54da4cfad9?s=64&d=mm&r=g) [Aliasgar Fakhri](http://none./)
     says:
    
    [March 5, 2014 at 8:59 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472605)
    
    Would prefer using "Text-to-column" approach.
    
    Ex : [John.doe@email.com](mailto:John.doe@email.com)
      
    1st Step in delimiters , use "@" :  
    Hence, you would get John.Doe and email.com as separate
    
    2nd Step for first name / last name , use "." as a delimiter  
    Hence, You would get John and Doe as separate.
    
    Instant results.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472605)
    
40.  [Resposta ao desafio do Chandoo | fcvidoto :: DATA Analyst ::](http://fcvidoto.com.br/?p=27)
     says:
    
    [March 6, 2014 at 3:26 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472766)
    
    \[…\] site do chandoo foi postado um desafio de tratamento de dados bem complicado de se \[…\]
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472766)
    
41.  ![](https://secure.gravatar.com/avatar/c52360bca673d0ece477dab688937f82fd859d0307945ab161c0469c830a6ec1?s=64&d=mm&r=g) Athar Siddiqui says:
    
    [March 6, 2014 at 5:51 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472793)
    
    So we start with [fred.bloggs@stink.com](mailto:fred.bloggs@stink.com)
    
    if the cell is F5 then fred is:
    
    \=LEFT(F5,FIND(".",F5)-1) and
    
    bloggs is:
    
    \=MID(F5,FIND(".",F5)+1,FIND("@",F5)-FIND(".",F5)-1)
    
    a colleague showed me this and it beats everything above
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472793)
    
    *   ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [March 6, 2014 at 9:17 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472815)
        
        @Athar,  
        This was not the task.  
        The task was to return the first & Last name from VARIOUS E-Mail combinations (with one formula that fits all) - such as:  
        [john\_doe@email.com](mailto:john_doe@email.com)
          
        [john.doe@email.com](mailto:john.doe@email.com)
          
        [john123doe@email.com](mailto:john123doe@email.com)
          
        [john-doe@email.com](mailto:john-doe@email.com)
          
        [john1964doe@email.com](mailto:john1964doe@email.com)
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472815)
        
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://excelhero.com/)
         says:
        
        [March 7, 2014 at 12:59 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472840)
        
        @Athar
        
        Nope. Your colleague's formulas do not even come close to solving this challenge.
        
        I'm interested in what you meant by "beats everything above?" Were you referring to how short the formulas are?
        
        Here is a shorter one that is precisely as useful:
        
        \=LEFT(F5,4)
        
        .
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472840)
        
42.  ![](https://secure.gravatar.com/avatar/c52360bca673d0ece477dab688937f82fd859d0307945ab161c0469c830a6ec1?s=64&d=mm&r=g) Athar Siddiqui says:
    
    [March 6, 2014 at 5:52 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472794)
    
    (I cant claim credit)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472794)
    
    *   ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark duchesne says:
        
        [March 6, 2014 at 11:22 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472826)
        
        Hi Atar,
        
        Your formula only works where there is a single "." In the email address. What if the email have 2 dots or 3 dots or any other combination of non text characters? Try you formula on the test examples given and you will see that it doesn't work.
        
        Keep trying;)
        
        Mark
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-472826)
        
43.  ![](https://secure.gravatar.com/avatar/0ca3f6325da54a72a2743f0ae41761d4f49dcb89400b0a6a54da50d22350385e?s=64&d=mm&r=g) Chris says:
    
    [March 9, 2014 at 11:43 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473209)
    
    you could just use extractmails.com to process complex scenarios, it's faster.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473209)
    
44.  ![](https://secure.gravatar.com/avatar/5459c97700e2aae9567eb6aaf2bc9665485c11c98e8d6e623ade895932c3dbb9?s=64&d=mm&r=g) AlexK says:
    
    [March 10, 2014 at 5:13 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473276)
    
    This should work with iterative calculations turned on and will work with capitalisation and any character you can throw at it I believe.
    
    Assumes email is in cell A1.
    
    First name in cell C1:  
    \=IFERROR(IF(C1<100,IF(OR(AND(CODE(MID($A1,C1,1))>=97,CODE(MID($A1,C1,1))<=122),AND(CODE(MID($A1,C1,1))>=65,CODE(MID($A1,C1,1))<=90)),C1+1,LEFT($A1,C1-1)),C1+1),1)
    
    Last name in cell D1:  
    \=IFERROR(IF(D1<100,IF(OR(AND(CODE(MID($A1,FIND("@",$A1)-D1,1))>=97,CODE(MID($A1,FIND("@",$A1)-D1,1))<=122),AND(CODE(MID($A1,FIND("@",$A1)-D1,1))>=65,CODE(MID($A1,FIND("@",$A1)-D1,1))<=90)),D1+1,MID($A1,FIND("@",$A1)-D1+1,D1-1)),D1+1),1)
    
    Apologies if this has already been posted, I wanted to work it out before checking the other submissions.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473276)
    
    *   ![](https://secure.gravatar.com/avatar/9c8add29f4aa9c7adf28f9e766cb0109f2bc4411de38a4b8c85626dab9a791ca?s=64&d=mm&r=g) Rudra Sharma says:
        
        [March 11, 2014 at 2:29 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473410)
        
        If I place your formulas in cells you specified it shows error (Circular Reference error).  
        If I place them to someother cell then they just give result as 1.
        
        With Regards  
        Rudra
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473410)
        
        *   ![](https://secure.gravatar.com/avatar/5459c97700e2aae9567eb6aaf2bc9665485c11c98e8d6e623ade895932c3dbb9?s=64&d=mm&r=g) AlexK says:
            
            [March 11, 2014 at 3:34 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473417)
            
            Hi Rudra,
            
            If you go into Options then formulas and then tick 'Enable iterative calculation'. Once you have done this, paste the formula back in and it should work. I have also noticed that you have to change the quotation marks from “ & ” to " to make it work.
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-473417)
            
45.  ![](https://secure.gravatar.com/avatar/e9af07077c4aeb371bef6f629e4cd0729f2e4697a3641881e0e08408502ef183?s=64&d=mm&r=g) Socrates G says:
    
    [March 21, 2014 at 5:31 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475066)
    
    the formula I used was:
    
    \=left(cell,find("@",cell)-1) - seems to work, but I have a bit of a block retrieving the domain name
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475066)
    
46.  ![](https://secure.gravatar.com/avatar/08ba2b5f28b4cace6440554f39b4eddf238968d4528167b1220abd5c06c06536?s=64&d=mm&r=g) MOHA says:
    
    [March 21, 2014 at 11:26 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475144)
    
    \=LEFT(B4;FIND("\_";B4)-1)=Jhon  
    \=RIGHT(LEFT(B4;FIND("@";B4)-1);3)=doe
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475144)
    
47.  ![](https://secure.gravatar.com/avatar/2316df589f6aae48ebb74b0787222a1c9d5baee2db3b2f536fe0861f1c5c60cd?s=64&d=mm&r=g) DavidRaj says:
    
    [March 22, 2014 at 4:38 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475167)
    
    \=MID(B7,1,4) = John  
    \=RIGHT(LEFT(B7,(FIND("@",B7)-1)),3) = doe
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475167)
    
48.  ![](https://secure.gravatar.com/avatar/613715ad3bf6f4fdfa71974b6f3c865209391f063a7564e0e642e0e40af5b07c?s=64&d=mm&r=g) SAMBIT KUMAR MOHAPATRA says:
    
    [March 22, 2014 at 9:14 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475230)
    
    \=LEFT(D4,4) = John  
    \=RIGHT(LEFT(D4,FIND("@",D4)-1),3) = doe
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475230)
    
49.  ![](https://secure.gravatar.com/avatar/5465fa2bd3d98c3553e039128cbf86b6cf6d88bb61843044d48ac3a66e6c5861?s=64&d=mm&r=g) ARVIND says:
    
    [March 22, 2014 at 9:59 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475235)
    
    \=LEFT(cell,FIND("@",cell)-1)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475235)
    
50.  ![](https://secure.gravatar.com/avatar/513fbc0b4817abd85275836dfa2068aeafd09ecbcd2d366c984025837cf67996?s=64&d=mm&r=g) Naveen BP says:
    
    [March 22, 2014 at 3:51 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475289)
    
    \=LEFT(D23,4) for first name  
    \=RIGHT(LEFT(D23,(FIND("@",D23))-1),3) to find last name
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475289)
    
51.  ![](https://secure.gravatar.com/avatar/b474635bede0a7762c762ac11c9f1feb23856ac452225cdefc465a04165ad051?s=64&d=mm&r=g) [Abbott Katz](http://www.spreadsheetjournalism.com/)
     says:
    
    [March 22, 2014 at 10:47 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475332)
    
    The LEFT formulation works only if you assume that the first name in question is always John, as per the actual examples. But if you want to prepare an expression that could glean ANY first name the problem gets considerably trickier.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475332)
    
52.  ![](https://secure.gravatar.com/avatar/2defc83c5fcc6616efc74e2f0b1fc08249db1ac14a60297ecfe0ae8e5de47167?s=64&d=mm&r=g) [Shaikh Sajid](http://yahoo/)
     says:
    
    [March 23, 2014 at 5:35 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475372)
    
    1)=LEFT(A1,FIND("@",A1,1)-1)  
    2)=LEFT(D1,FIND("\_",D1,1)-1)  
    3)=RIGHT(D1,LEN(D1)-FIND("\_",D1,1))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475372)
    
53.  ![](https://secure.gravatar.com/avatar/3cc6c1eb9c9e780fecccc5c3bb00071cfca35dcb02951a080af7f13109ab4b10?s=64&d=mm&r=g) Peter says:
    
    [March 24, 2014 at 12:09 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475542)
    
    Some great formulas, especially liking Roberto's version, which I amended to be able to find the last name from the whole email (instead of having to split out first/last names initially)
    
    \=MID(A3,FIND(RIGHT(B3,MATCH(1=1,MID(B3,LEN(B3)-ROW($1:$99),1)<"a",)),B3),(FIND("@",A3)-FIND(RIGHT(B3,MATCH(1=1,MID(B3,LEN(B3)-ROW($1:$99),1)<"a",)),B3)))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475542)
    
54.  ![](https://secure.gravatar.com/avatar/78b9377e0e9042941d3e0e0a3fe8dcd15a4e20ae64fb3f78125c14fe43252af5?s=64&d=mm&r=g) Amiq Khan says:
    
    [March 27, 2014 at 6:32 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475937)
    
    I used the 'Text to Columns' functionality. First separate text on the basis of @ and then \_ and we will have just the first name and last name in two columns.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-475937)
    
55.  ![](https://secure.gravatar.com/avatar/1bd8065e9e7b590929689c52d7281010cd50544f726ec6368c745dd418c5ab85?s=64&d=mm&r=g) [Rekha Chaudhary](http://chandoo.org/)
     says:
    
    [March 28, 2014 at 10:18 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-476104)
    
    i used this for the question.
    
    For Name portion  
    \=LEFT(D31,SEARCH("@",D31)-1)
    
    For First Name  
    \=LEFT(LEFT(D31,SEARCH("@",D31)-1),4)
    
    For Last Name  
    \=RIGHT(LEFT(D31,SEARCH("@",D31)-1),3)
    
    this formula works only when the names are same, but it will not work in case of different-different names. For that we have to use different formula
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-476104)
    
56.  ![](https://secure.gravatar.com/avatar/57de2e9f66e24dbdb2483c4ed75d844e8708f689032ce059ea85739ae6d6f3bf?s=64&d=mm&r=g) HunterHisoka says:
    
    [April 1, 2014 at 1:08 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-476884)
    
    C1 = an email text ( [John\_2342\_4353doe@gmail.com](mailto:John_2342_4353doe@gmail.com)
     )
    
    Character (to identify middle)  
    A1:A13 fill with ( \_ - , . 0 1 2 3 4 5 6 7 8 9 )
    
    Character (to identify last name)  
    B1:B26 fill with ( a b c d e f g h i j k l m n o p q r s t u v w x y z )
    
    Name of Portion  
    D1 : =LEFT(C1;SEARCH("@";C1;1)-1)
    
    First Name  
    E1 : =LEFT(D1;MIN(IFERROR(SEARCH(A1:A13;D1;1);"x"))-1) Then Ctrl + Enter
    
    Last Name  
    F1 : =MID(D1;LEN(E1)+MIN(IFERROR(SEARCH(B1:B26;RIGHT(D1;LEN(D1)-LEN(E1));1);"x"));LEN(D1)-LEN(E1)-1) Then Ctrl + Enter
    
    Best Regard,  
    Naruto
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-476884)
    
57.  ![](https://secure.gravatar.com/avatar/a7dac39a691fce4c367686737569328c87ace55328ad33e3f97c3c62343b4d90?s=64&d=mm&r=g) Ashok Sindkar says:
    
    [April 5, 2014 at 4:30 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-477315)
    
    It is very simple with Excel 2013 version. It is having new function Flash fill. Just start typing required output in top cell. Press enter for next cell and start typing ... Excel will show all required output in faint letters Just press enter and Done. Try this.  
    Thanks.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-477315)
    
    *   ![](https://secure.gravatar.com/avatar/5c22d0583e8751c356e535bdec57a4d20c6307a44cea7e930595c009241ee6ad?s=64&d=mm&r=g) Alexie Nepeh says:
        
        [April 16, 2014 at 5:38 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-479102)
        
        \=LEFT(A2,FIND("@email.com",A2,1)-1) to extract the name from the email addresses
        
        \=LEFT(C2,4) to extract the first name
        
        \=RIGHT(C2,3) to extract the last name
        
        why write complex formular when it can be done easily?
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-479102)
        
        *   ![](https://secure.gravatar.com/avatar/e1e47761ba69674d3800e64b1596695e611fc999292036b614be3ec72df2c445?s=64&d=mm&r=g) Hannah Li says:
            
            [June 28, 2017 at 6:26 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1471063)
            
            Dear Alexie,
            
            Do your formula applicable to [Alexie\_123\_Nepeh@mail.com](mailto:Alexie_123_Nepeh@mail.com)
            ?
            
            This is the question talking about.
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1471063)
            
            *   ![](https://secure.gravatar.com/avatar/e1e47761ba69674d3800e64b1596695e611fc999292036b614be3ec72df2c445?s=64&d=mm&r=g) Hannah Li says:
                
                [June 28, 2017 at 6:28 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1471064)
                
                How to deal with hundred customers?
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1471064)
                
58.  ![](https://secure.gravatar.com/avatar/9a549fca4e5e262f141e615c69fe15de125cf44636de0a41543548fc2cf5157a?s=64&d=mm&r=g) Tom Smith says:
    
    [May 8, 2014 at 4:18 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-525396)
    
    I went back to the simpler process of breaking things down into steps, after making sure that for valid email addresses the only special characters that are permissable are hyphen (-), underscore (\_) , period (.), plus (+) and I added comma (,) and hash (#) just for fun. The steps:  
    1\. retrive the name portion  
    2\. replace the characters we don't want with spaces  
    3\. trim the results of step 2 and use a Proper function to make them look right (they are names after all)  
    4\. capture the first and last names from the result of step 3
    
    Then I put the first 3 steps into a single formula and used a simple parse to capture the names.
    
    So for the combined steps 1-3, I ended up with:
    
    \=PROPER(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LEFT(A1,FIND("@",A1)-1),"."," "),"("," "),"-"," "),"\_"," "),"#"," "),"+"," "),"1"," "),"2"," "),"3"," "),"4"," "),"5"," "),"6"," "),"7"," "),"8"," "),"9"," "),"0"," ")))
    
    Then, with those results in column B, looked for the first name for col C:  
    \=LEFT(B1,FIND(" ",B1)-1))
    
    and the last name in col D:  
    \=MID(B1,FIND(" ",B1)+1,LEN(B1))
    
    Seems to work for all the combinations mentiond in the requirements.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-525396)
    
59.  ![](https://secure.gravatar.com/avatar/9f3ce1538ef7c7f78ee45dae669c3f48b2d7bd5e678d3073658d8383350094db?s=64&d=mm&r=g) Sanjeet Singh says:
    
    [June 27, 2014 at 3:37 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-563716)
    
    LEFT(LEFT(B4,FIND("@",$B4,1)-1),4)  
    RIGHT(LEFT(B4,FIND("@",$B4,1)-1),3)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-563716)
    
60.  ![](https://secure.gravatar.com/avatar/df63a6774a3f8c43847f10dd5fe62e05ef9108f1e2e321966f3353a46ba314e2?s=64&d=mm&r=g) Lynn C says:
    
    [August 14, 2014 at 4:00 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614300)
    
    Could you just:  
    Search the list for the rarest # in the emails addys (say it's #8)  
    Cut & paste those few addys to a new column  
    Original data, replace @ with 8  
    Use 8 as separating value
    
    Manually separate the few in the new column
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614300)
    
61.  ![](https://secure.gravatar.com/avatar/6d1774c5847a615b7cebe5256ffc773029f3ba85b5a8a68f0c1a0d38a19f8a3f?s=64&d=mm&r=g) suyash says:
    
    [August 14, 2014 at 4:03 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614312)
    
    We can use Left and right formula  
    for ex.
    
    john999doe to extract John "=left(john999doe,4) as from left only 4 characters we need"  
    and for  
    "=right(john999doe,3) as from right only 3 characters we need"
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614312)
    
62.  ![](https://secure.gravatar.com/avatar/76a100d67f6724f83ccba735558d08847a7c942d29b889f46c378526e75ea0cc?s=64&d=mm&r=g) karl says:
    
    [August 14, 2014 at 7:33 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614984)
    
    b1:=LEFT(A1,FIND("@",A1)-1)  
    c1:=LEFT(B1,FIND("\_",B1)-1)  
    d1:=RIGHT(B1,FIND("\_",B1)-1)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-614984)
    
63.  ![](https://secure.gravatar.com/avatar/6c5bb325cc2b84f6a962398018fff7353f295a92202b51d2de8ba9026126acb0?s=64&d=mm&r=g) Peter Thompson says:
    
    [August 14, 2014 at 7:52 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-615043)
    
    I decided to make a function to do this:
    
    The code is below this works by entering =NameFromEmail in a cell with the cell and then either 1 or 2 as parameter. So in the example worksheet the email address is in column b so if you enter in cell d4
    
    \=NameFromEmail(b4,1) then it will return the first name and if in cell e4 you enter =NameFromEmail(b4,2) it will return the 2nd name.
    
    Function NameFromEmail(ByVal rngEmail As Range, ByVal lngFirstOrLastName)
    
    Dim strEmail As String  
    strEmail = rngEmail.Value
    
    Dim lngStringLength As Long  
    lngStringLength = Len(strEmail)
    
    'Loop through string  
    For I = 1 To lngStringLength
    
    Dim lngAscNumber As Long, lngCountNonChar As Long, lngEndOfFirstName As Long, lngEndOfName As Long
    
    'Get the Ascii number of the email string  
    lngAscNumber = Asc(Mid(strEmail, I, 1))
    
    'Check for non text symbol  
    If lngAscNumber < 97 Then '''Note there should be at LT symbol in case it doesn't show on the websit  
    'look for @ symbol  
    If lngAscNumber = 64 Then  
    lngEndOfName = I  
    'If the @ symbol has been encountered increment I s we quit the loop  
    I = lngStringLength  
    Else
    
    If lngCountNonChar = o Then  
    lngEndOfFirstName = I  
    Else  
    End If
    
    'Count non consequitive letters for use later on in the string formulas  
    lngCountNonChar = lngCountNonChar + 1  
    End If  
    Else  
    End If
    
    Next I
    
    Dim strName As String
    
    'identify what name is required and get appropriatte string  
    If lngFirstOrLastName = 1 Then  
    strName = Left(strEmail, lngEndOfFirstName - 1)  
    Else  
    strName = Mid(strEmail, lngEndOfFirstName + lngCountNonChar, lngEndOfName - (lngEndOfFirstName + lngCountNonChar))  
    End If
    
    NameFromEmail = strName
    
    End Function
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-615043)
    
64.  ![](https://secure.gravatar.com/avatar/a7dac39a691fce4c367686737569328c87ace55328ad33e3f97c3c62343b4d90?s=64&d=mm&r=g) Ashok says:
    
    [August 15, 2014 at 12:14 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-617942)
    
    I tried following and got output, but I am not satisfied. I have taken output of first formula in a C column then used second formula to get final output in column D.  
    Friends, I am sure you will guide me, how to get output of first formula in to second without using C column.  
    Thanks in advance.
    
    \=CONCATENATE(LEFT(B3,4)," ",RIGHT(B3,13))  
    \=LEFT(C3,8)  
    Write these formulas and drag.
    
    [john\_doe@email.com](mailto:john_doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john.doe@email.com](mailto:john.doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john321doe@email.com](mailto:john321doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john\_\_\_doe@email.com](mailto:john___doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john-doe@email.com](mailto:john-doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john999doe@email.com](mailto:john999doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe  
    [john0doe@email.com](mailto:john0doe@email.com)
     john [doe@email.com](mailto:doe@email.com)
     john doe
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-617942)
    
65.  ![](https://secure.gravatar.com/avatar/55a44e8c79dd3a76f211cb40ac5f01ec0736906f5efff3bd9bcb47066f87099c?s=64&d=mm&r=g) [Danail](http://danailgardev.blogspot.com/)
     says:
    
    [August 15, 2014 at 12:43 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618022)
    
    Hi there,
    
    I will break my answer in its parts for easier explanation. The assume the emails are positioned on the sheet as in the sample file I downloaded here where the name portion are in col C4:C10.
    
    First, I get the position of the first non-alphabetic character in the name before the @email.com by (in cell D4):  
    {=MATCH(96,CODE((MID(C4,ROW(INDIRECT("A1:C"&LEN(C4))),1))),-1)}  
    The number 96 is the the ASCII code of "a" minus 1.
    
    I convert the string in an array of ASCII symbols and use simple MATCH on it.  
    Then it is extremely easy to extract the first name (in cell E4):  
    \=LEFT(C4,D4)
    
    The I find the last occurrence of a non-alpha character in the string that results from the original name portion stripped with the first name (in cell F4):  
    {=MATCH(96,CODE((MID(MID(C4,D4+1,100),ROW(INDIRECT("A1:C"&LEN(C4))),1))),1)}  
    The second MID function strips the full name part from the the fist name. The other part is same as with extraction of first name with only difference of the last parameter for MATCH to be -1 as I am looking for the first occurrence of alpa-character.
    
    The last name then is again easy (cell G4):  
    \=MID(C4,D4+F4+1,100)
    
    I could then put everything together in two scary formulas:  
    First Name (in H4):  
    {=LEFT(C4,MATCH(96,CODE((MID(C4,ROW(INDIRECT("A1:C"&LEN(C4))),1))),-1))}  
    Last Name (I4) (extremely scary):  
    {=MID(C4,MATCH(96,CODE((MID(C4,ROW(INDIRECT("A1:C"&LEN(C4))),1))),-1)+MATCH(96,CODE((MID(MID(C4,MATCH(96,CODE((MID(C4,ROW(INDIRECT("A1:C"&LEN(C4))),1))),-1)+1,100),ROW(INDIRECT("A1:C"&LEN(C4))),1))),1)+1,100)}
    
    How do you find my approach?
    
    Danail
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618022)
    
66.  ![](https://secure.gravatar.com/avatar/c555959f7ce940adf186a5d17869d3867ff3d69d4c360d4a769798210bd700f2?s=64&d=mm&r=g) LEE THANG YEN says:
    
    [August 15, 2014 at 2:07 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618265)
    
    \=LEFT(A5,4)&" "&MID(A5,SEARCH("@",A5)-3,3)  
    I think mine is super formula, can apply use for all the emails.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618265)
    
67.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://www.excelhero.com/)
     says:
    
    [August 15, 2014 at 2:50 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618374)
    
    @Lee Thang Yen,
    
    What happens with your formula when the first name is not exactly four characters long, or when the last name is not exactly three characters long?
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618374)
    
68.  ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://www.excelhero.com/)
     says:
    
    [August 15, 2014 at 4:10 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618579)
    
    @Peter Thompson
    
    Working with byte arrays in more efficient than working with strings.
    
    The following UDF should be array-entered over two adjacent cells, the first cell will display the First Name and the second will display the Last Name:
    
    `   Function EmailNames(r As Range) As Variant  Dim b() As Byte   Dim vOut(0, 1) As Variant   Dim i As Long, p1 As Long, p2 As Long, p3 As Long  b = LCase$(r)   For i = 0 To UBound(b) Step 2   If b(i) > 96 And b(i) < 123 Then   If p1 And p2 = 0 Then p2 = i + 1   Else   If p1 = 0 Then p1 = i - 1   If p2 Then p3 = i - 1: Exit For   End If   Next   vOut(0, 0) = LeftB(b, p1): vOut(0, 1) = MidB(b, p2, p3 - p2 + 1)  EmailNames = vOut  End Function   `
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-618579)
    
    *   ![](https://secure.gravatar.com/avatar/6c5bb325cc2b84f6a962398018fff7353f295a92202b51d2de8ba9026126acb0?s=64&d=mm&r=g) Peter Thompson says:
        
        [August 17, 2014 at 6:57 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-626545)
        
        Daniel,
        
        Thanks for the feedback.
        
        When I try and run this code it gives errors around the second group of if statements. Also the vOut statement at the end errors.
        
        Can I also ask why the step 2 is used I understand what it does, but I would like to understand why it is used in this context.
        
        Peter
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-626545)
        
        *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://www.excelhero.com/)
             says:
            
            [August 17, 2014 at 11:47 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-627210)
            
            @Peter
            
            Hmm. Are you in a locale other than US English?
            
            The line that assigns the range text (r) to the byte array (b) converts VBA's BSTR representation of the string to the byte array. This creates a byte array with two bytes per character in the text string.
            
            This is why we step by two. The array is base ZERO so the character code values that we are interested in are at the byte array indexes of 0, 2, 6, 8, 10, etc.
            
            However, if you are in a locale that uses both bytes to represent your characters, then this WILL NOT WORK.
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-627210)
            
            *   ![](https://secure.gravatar.com/avatar/6c5bb325cc2b84f6a962398018fff7353f295a92202b51d2de8ba9026126acb0?s=64&d=mm&r=g) Peter Thompson says:
                
                [August 20, 2014 at 6:53 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-636127)
                
                Daniel,
                
                My PC is on English (United Kingdom) would this stop it from working?
                
                Thanks,
                
                Peter
                
                [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-636127)
                
                *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://www.excelhero.com/)
                     says:
                    
                    [August 21, 2014 at 2:51 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-638706)
                    
                    @Peter.
                    
                    No, it would not.
                    
                    But I found the problem. I just noticed that when a reader copies my UDF from this blog post the minus signs get translated into another character that looks like a minus sign, but is not.
                    
                    Specifically, the minus signs in my code should be ASCII character number 45, but this blog post is displaying them as ASCII character 150.
                    
                    So, when you paste my UDF into the VBE in Excel, simply delete the three minus signs and replace them by typing them from your keyboard.
                    
                    That should do it.
                    
                    Please remember that the UDF returns an array of one cell high and two cells wide. This means it should be array-entered over two adjacent cells and confirmed simultaneously for those two cells.
                    
                    Daniel
                    
69.  ![](https://secure.gravatar.com/avatar/e550bf755519b1901393190a0c9dcb083b1b8b7f82101172abe0fb35a8ddaf4b?s=64&d=mm&r=g) [Giancarlo](http://none/)
     says:
    
    [August 15, 2014 at 9:13 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619289)
    
    Using the formulas GetFirst & GetLast
    
    Option Explicit
    
    Function GetFirst(r As String) As String  
    Dim arr As Variant  
    With CreateObject("vbscript.regexp")  
    .Pattern = "\[\_\]{1,8}"  
    If .Test(r) Then GetFirst = .Execute(r)(0)  
    .Pattern = "\[.\]"  
    If .Test(r) Then GetFirst = GetFirst & .Execute(r)(0)  
    .Pattern = "\[0-9\]{1,8}"  
    If .Test(r) Then GetFirst = GetFirst & .Execute(r)(0)  
    .Pattern = "\[-\]"  
    If .Test(r) Then GetFirst = GetFirst & .Execute(r)(0)  
    End With  
    arr = Split(r, GetFirst)  
    GetFirst = arr(0)  
    End Function
    
    Function GetLast(r As String) As String  
    Dim arr As Variant  
    With CreateObject("vbscript.regexp")  
    .Pattern = "\[\_\]{1,8}"  
    If .Test(r) Then GetLast = .Execute(r)(0)  
    .Pattern = "\[.\]"  
    If .Test(r) Then GetLast = GetLast & .Execute(r)(0)  
    .Pattern = "\[0-9\]{1,8}"  
    If .Test(r) Then GetLast = GetLast & .Execute(r)(0)  
    .Pattern = "\[-\]"  
    If .Test(r) Then GetLast = GetLast & .Execute(r)(0)  
    End With  
    arr = Split(r, GetLast)  
    GetLast = arr(1)  
    End Function
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619289)
    
70.  ![](https://secure.gravatar.com/avatar/ccbc75f224d9414823919a549b8e4a427cef6e440f9390219e86db6c3ec2c33d?s=64&d=mm&r=g) Anwar Alrubeidy says:
    
    [August 15, 2014 at 11:07 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619539)
    
    Somewhat time consuming formulas, where i have done a separate  
    formulas in each row,sent file by email.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619539)
    
71.  ![](https://secure.gravatar.com/avatar/ccbc75f224d9414823919a549b8e4a427cef6e440f9390219e86db6c3ec2c33d?s=64&d=mm&r=g) Anwar Alrubeidy says:
    
    [August 15, 2014 at 11:16 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619558)
    
    Email name Portion  
    [john\_doe@email.com](mailto:john_doe@email.com)
     =LEFT(A2,FIND("@",A2)-1)  
    [john.doe@email.com](mailto:john.doe@email.com)
     =LEFT(A3,FIND("@",A3)-1)  
    [john321doe@email.com](mailto:john321doe@email.com)
     =LEFT(A4,FIND("@",A4)-1)  
    [john\_\_\_doe@email.com](mailto:john___doe@email.com)
     =LEFT(A5,FIND("@",A5)-1)  
    [john-doe@email.com](mailto:john-doe@email.com)
     =LEFT(A6,FIND("@",A6)-1)  
    [john999doe@email.com](mailto:john999doe@email.com)
     =LEFT(A27,FIND("@",A7)-1)  
    [john0doe@email.com](mailto:john0doe@email.com)
     =LEFT(A8,FIND("@",A8)-1)  
    First Name  
    \=SUBSTITUTE(LEFT(B2,SEARCH("\_",B2)),"\_","",1)  
    \=SUBSTITUTE(LEFT(B3,SEARCH(".",B3)),".","",1)  
    \=SUBSTITUTE(LEFT(B4,SEARCH("321",B4)-1),321,"",1) etc etc  
    Last Name  
    \=SUBSTITUTE(RIGHT(B2,SEARCH("\_",B2)-1),"\_","",1)  
    \=SUBSTITUTE(RIGHT(B3,SEARCH(".",B3)-1),".","",1)  
    \=SUBSTITUTE(RIGHT(B4,SEARCH("321",B4)-2),"321","",1) etc etc  
    hope i answered the question
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-619558)
    
72.  ![](https://secure.gravatar.com/avatar/5d9306ecaca6c99592123d0bf52d27fb09032e91f8c61f0ebeb7ff635fcb9389?s=64&d=mm&r=g) Candy says:
    
    [August 16, 2014 at 9:18 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621109)
    
    Formula: =Left(B4,4)&" "&Left(Right(B4,13),3)
    
    This formula will apply to all rows giving you same answer = john doe
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621109)
    
73.  ![](https://secure.gravatar.com/avatar/4aa7177c8f04818ede9206e6866a088c27c9afd70147746d1d229bd8375068c1?s=64&d=mm&r=g) Maloo says:
    
    [August 16, 2014 at 1:19 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621692)
    
    What does match(1=1,....) signifies.
    
    I mean 1=1, means?
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621692)
    
    *   ![](https://secure.gravatar.com/avatar/1598c78c3a3c055e277b9b072ffbf6783713a7ea48a92490a1085987194058b3?s=64&d=mm&r=g) [Daniel Ferry](http://www.excelhero.com/)
         says:
        
        [August 16, 2014 at 5:35 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-622295)
        
        @Maloo
        
        1=1 means TRUE.  
        1=0 means FALSE.
        
        This convention is often employed by formula crafters that try to make formulas as concise as possible, when suggesting a solution to a formula challenge.
        
        The convention saves a couple of characters in formula length.
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-622295)
        
74.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [August 16, 2014 at 2:40 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621876)
    
    I think there happened a problem while I was sending my respond so it is not published.
    
    In my solution only the columns D & E are used. Column D is the output for First Names where the first letter starts with capital while the Column E is output for Last Names. Last name is completely written in uppercase. Column B contains the e-mail address.
    
    The formula in the cell in Column D is as follows:
    
    \=PROPER(LEFT(SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LOWER(LEFT(B4,FIND("@",B4)-1)),"\_","."),"-","."),"9","."),"8","."),"7","."),"6","."),"5","."),"4","."),"3","."),"2","."),"1","."),"0","."),"/","."),"..",". ")," ."," ")),". ","."),FIND(".",SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LOWER(LEFT(B4,FIND("@",B4)-1)),"\_","."),"-","."),"9","."),"8","."),"7","."),"6","."),"5","."),"4","."),"3","."),"2","."),"1","."),"0","."),"/","."),"..",". ")," ."," ")),". ","."))-1))
    
    The formula in the cell in Column E is as follows:
    
    \=UPPER(RIGHT(SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LOWER(LEFT(B4,FIND("@",B4)-1)),"\_","."),"-","."),"9","."),"8","."),"7","."),"6","."),"5","."),"4","."),"3","."),"2","."),"1","."),"0","."),"/","."),"..",". ")," ."," ")),". ","."),LEN(SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LOWER(LEFT(B4,FIND("@",B4)-1)),"\_","."),"-","."),"9","."),"8","."),"7","."),"6","."),"5","."),"4","."),"3","."),"2","."),"1","."),"0","."),"/","."),"..",". ")," ."," ")),". ","."))-FIND(".",SUBSTITUTE(TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(LOWER(LEFT(B4,FIND("@",B4)-1)),"\_","."),"-","."),"9","."),"8","."),"7","."),"6","."),"5","."),"4","."),"3","."),"2","."),"1","."),"0","."),"/","."),"..",". ")," ."," ")),". ","."))))
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-621876)
    
75.  ![](https://secure.gravatar.com/avatar/2ea15975af84d2929550e6fd5276d5e84cebe336b11b03912e2909be7b46c27c?s=64&d=mm&r=g) Kishan says:
    
    [August 17, 2014 at 7:12 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-624801)
    
    Answers:  
    1 '=REPLACE(LEFT(B4,FIND("@",B4)-1),FIND("\_",B4),1," ")  
    2 '=REPLACE(LEFT(B5,FIND("@",B5)-1),FIND(".",B5),1," ")  
    3 '=SUBSTITUTE(LEFT(B6,FIND("@",B6)-1),"321"," ")  
    4 '=SUBSTITUTE(LEFT(B7,FIND("@",B7)-1),"\_\_\_"," ")  
    5 '=REPLACE(LEFT(B8,FIND("@",B8)-1),FIND("-",B8),1," ")  
    6 '=SUBSTITUTE(LEFT(B9,FIND("@",B9)-1),"999"," ")  
    7 '=REPLACE(LEFT(B10,FIND("@",B10)-1),FIND("0",B10),1," ")
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-624801)
    
76.  ![](https://secure.gravatar.com/avatar/ccbc75f224d9414823919a549b8e4a427cef6e440f9390219e86db6c3ec2c33d?s=64&d=mm&r=g) Anwar Alrubeidy says:
    
    [August 17, 2014 at 9:11 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-626851)
    
    A1= Email Address B1= First Name  
    A2= [John\_doe@email.com](mailto:John_doe@email.com)
      
    B2 =LEFT(A2,SEARCH(CHAR(H2),A2)-1) =John  
    A3 = [John.doe@email.com](mailto:John.doe@email.com)
      
    B3 = LEFT(A3,SEARCH(CHAR(H3),A3)-1) =John  
    A4 = [John321doe@email.com](mailto:John321doe@email.com)
      
    B4 =LEFT(A4,SEARCH(CHAR(H4),A4)-1) =John  
    D1 = FirstName+email  
    D2 =REPLACE(A2,1,SEARCH("doe",A2)-1,"")=doe@email.com  
    D3 =REPLACE(A3,1,SEARCH("doe",A3)-1,"")=doe@email.com  
    D4=REPLACE(A4,1,SEARCH("doe",A4)-1,"")=doe@email.com  
    H2 = 95, H3 = 46, H4 = 51, H5 = 64  
    C1 = Last Name  
    C2 =LEFT(D2,SEARCH(CHAR($H$5),D2)-1) = doe  
    C3 ==LEFT(D3,SEARCH(CHAR($H$5),D3)-1)= doe  
    C4 ==LEFT(D4,SEARCH(CHAR($H$5),D4)-1)= doe
    
    Hope this helps.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-626851)
    
77.  ![](https://secure.gravatar.com/avatar/4842c879bf4a6574348bf50c85e5ee446a4e770b2e522b601a9707c1a7694765?s=64&d=mm&r=g) Sam says:
    
    [August 19, 2014 at 6:43 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-633415)
    
    B1: =left(A1,find("@",A1)-1)  
    C1: =left(A1,4)  
    D1: =mid(A1,find("@",A1)-3,3)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-633415)
    
78.  ![](https://secure.gravatar.com/avatar/07c1a26021334ba4edd07817d0cc4912eb17346c14c9eccf86ed8ffd40590bed?s=64&d=mm&r=g) Siva says:
    
    [August 21, 2014 at 5:08 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-637469)
    
    Given below are the macro codes to extract the name portion, first name and last name based on the given emails :-
    
    Sub NameExtractionFromEmail()
    
    Dim cell As Range  
    Dim tempVal As String, NamePortion() As String  
    Dim Num As Integer  
    Dim Firstname As String, LastName As String  
    Dim LastRow As Long  
    Dim tempName As Long
    
    Sheets(1).Select  
    LastRow = Cells(Rows.Count, 2).End(xlUp).Row
    
    For Each cell In Range(Cells(4, 2), Cells(LastRow, 2))  
    tempVal = cell.Value  
    NamePortion() = Split(tempVal, "@")  
    cell.Offset(0, 1).Value = NamePortion(LBound(NamePortion))
    
    For Num = 1 To 96  
    tempName = InStr(cell.Offset(0, 1).Value, Chr(Num))  
    If tempName > 0 Then  
    Firstname = Left(cell.Offset(0, 1).Value, tempName - 1)  
    cell.Offset(0, 2).Value = Firstname  
    LastName = Right(cell.Offset(0, 1).Value, tempName - 2)  
    cell.Offset(0, 3).Value = LastName  
    End If  
    Next  
    Next  
    End Sub
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-637469)
    
79.  ![](https://secure.gravatar.com/avatar/dcc5de23a61a3b6926141cb9059bbf0e8662f6aa444c43ffed7838d039d5c82b?s=64&d=mm&r=g) Mari A. says:
    
    [August 21, 2014 at 3:43 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-638832)
    
    For the given example name sample:
    
    First Name: =REPLACE(B2, 5, 9, " ")
    
    Last Name: =RIGHT(B2, 3)
    
    I kept it simple, however, I am still working on how to get ONE formula for any name length.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-638832)
    
80.  ![](https://secure.gravatar.com/avatar/ccbc75f224d9414823919a549b8e4a427cef6e440f9390219e86db6c3ec2c33d?s=64&d=mm&r=g) Anwar says:
    
    [August 22, 2014 at 9:44 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-643508)
    
    A B C  
    1-Email Name Portion CODE  
    [2-john\_doe@email.com](mailto:2-john_doe@email.com)
     john\_doe 95  
    [3-john.doe@email.com](mailto:3-john.doe@email.com)
     john.doe 46  
    [4-john321doe@email.com](mailto:4-john321doe@email.com)
     john321doe 51  
    [5-john\_\_\_doe@email.com](mailto:5-john___doe@email.com)
     John\_\_\_doe 95  
    [6-john-doe@email.com](mailto:6-john-doe@email.com)
     john-doe 45  
    [7-john999doe@email.com](mailto:7-john999doe@email.com)
     john999doe 57  
    [8-john0doe@email.com](mailto:8-john0doe@email.com)
     john0doe 48
    
    First Name  
    \=LEFT(SUBSTITUTE(B2,CHAR(C2)," "),SEARCH(CHAR(C2),B2))  
    Last Name  
    \=RIGHT(SUBSTITUTE(B2,CHAR($C2)," "),SEARCH(CHAR(C2),B2)-2)  
    Change B2 and C2 to B3,B4,etc,and C3,C4,etc.  
    Anwar
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-643508)
    
81.  ![](https://secure.gravatar.com/avatar/e45953c9ec00832eb45336bc82c312d9cea6a41ac6e6bb6a3445c183b9e38d74?s=64&d=mm&r=g) Dhiti says:
    
    [September 26, 2015 at 8:05 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052155)
    
    C4  
    \=LEFT(B4,FIND("@",B4)-1)  
    Enter
    
    D4  
    \=LEFT(C4,MATCH(1,1/((CODE(MID(C4,ROW(INDIRECT("A1:A"&LEN(C4))),1))122)),0)-1)  
    {array}
    
    E4  
    \=MID(C4,MATCH(2,1/((CODE(MID(C4,ROW(INDIRECT("A1:A"&LEN(C4))),1))122)))+1,255)  
    {array}
    
    It's too long. Sorry, I'm just starter. Thank you for your useful website and for your quiz.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052155)
    
    *   ![](https://secure.gravatar.com/avatar/e45953c9ec00832eb45336bc82c312d9cea6a41ac6e6bb6a3445c183b9e38d74?s=64&d=mm&r=g) Dhiti says:
        
        [September 26, 2015 at 8:12 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052160)
        
        Why my answers are changed? I want to type  
        D4  
        \=LEFT(C4,MATCH(1,1/((CODE(MID(C4,ROW(INDIRECT("A1:A"&LEN(C4))),1))122)),0)-1)
        
        and
        
        E4  
        \=MID(C4,MATCH(2,1/((CODE(MID(C4,ROW(INDIRECT("A1:A"&LEN(C4))),1))122)))+1,255)
        
        Best regards,  
        Dhiti T.
        
        [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052160)
        
        *   ![](https://secure.gravatar.com/avatar/e45953c9ec00832eb45336bc82c312d9cea6a41ac6e6bb6a3445c183b9e38d74?s=64&d=mm&r=g) Dhiti says:
            
            [September 26, 2015 at 8:18 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052162)
            
            It has changed again.  
            This is my file.  
            [https://drive.google.com/file/d/0Bz3ZrPpxvdlXU1BVZ3V6dGRJXzQ/view?usp=sharing](https://drive.google.com/file/d/0Bz3ZrPpxvdlXU1BVZ3V6dGRJXzQ/view?usp=sharing)
            
            Best Regards,  
            Dhiti T.
            
            [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052162)
            
82.  ![](https://secure.gravatar.com/avatar/6d1774c5847a615b7cebe5256ffc773029f3ba85b5a8a68f0c1a0d38a19f8a3f?s=64&d=mm&r=g) suyash says:
    
    [September 26, 2015 at 8:11 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052533)
    
    why ppl making it too complicated  
    for ex. [john\_doe@email.com](mailto:john_doe@email.com)
    
    1st step extract "john\_doe"=LEFT(B4,(FIND("@",B4)-1))  
    2nd step extract john= =LEFT(F4,FIND("n",F4))  
    3rd step extract doe= =RIGHT(F4,3)
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1052533)
    
83.  ![](https://secure.gravatar.com/avatar/dbef6227297fde7dd0b4adcbb35b2f6313bc4461c1efc175a2fe5a8ee2e77d2e?s=64&d=mm&r=g) Mukesh says:
    
    [November 4, 2015 at 10:47 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1075895)
    
    You may refer this also.  
    \=++LEFT(B3,4)&" "&LEFT(RIGHT(B3,13),3)  
    \=++LEFT(B4,4)&" "&LEFT(RIGHT(B4,13),3)  
    \=++LEFT(B5,4)&" "&LEFT(RIGHT(B5,13),3)
    
    \*B3=john\_doe@email.com  
    \*B4=john.doe@email.com  
    \*B5=john321doe@email.com
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1075895)
    
84.  ![](https://secure.gravatar.com/avatar/42c63173b45cccd941f9d99714c7081d0346e4554129223c6b7f6dc614a7efa6?s=64&d=mm&r=g) Ata says:
    
    [November 6, 2015 at 7:34 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1076619)
    
    First Name: =LEFT(LOWER(LEFT(B4,FIND("@",B4)-1)),MIN(IFERROR(FIND(CHAR(ROW($A$1:$A$95)),LOWER(LEFT(B4,FIND("@",B4)-1))),FALSE))-1)  
    \[control+shift+enter\]
    
    Last Name: =RIGHT(LOWER(LEFT(B4,FIND("@",B4)-1)),LEN(LOWER(LEFT(B4,FIND("@",B4)-1)))-MIN(IFERROR(FIND(CHAR(ROW($A$97:$A$122)),LOWER(LEFT(B4,FIND("@",B4)-1)),MIN(IFERROR(FIND(CHAR(ROW($A$1:$A$95)),LOWER(LEFT(B4,FIND("@",B4)-1))),FALSE))),FALSE))+1)  
    \[control+shift+enter\]
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1076619)
    
85.  ![](https://secure.gravatar.com/avatar/e3115aafe00f957ac135d7cde50823adf369de725cb75ebe0b58239c9cd2a17c?s=64&d=mm&r=g) sandeep kelakr says:
    
    [May 6, 2019 at 5:06 am](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1644662)
    
    Date Particulars Voucher No. Voucher Ref. & Date Narration Quantity Rate Value Gross Total SALES RETURN Carrige Outward Sales Return Gst 5% Output Cgst 2.5% Output Sgst 2.5%  
    01-May-2019 Haribhau Ramkisan Gadgule 825 spcod-0363 / 1-5-2019 4 Unit Fodder Grass Gopi Krishna 50 gm Rs. 385-Santosh Bhosale CLUSTER2 4.00 pkt 1540.00 1540.00 1540.00  
    Fodder Grass - Gopikrishna - 50 Gm - Amar Seed 4.00 pkt 385.00/pkt 1540.00  
    01-May-2019 Vitthal Raisingh Daberao 826 spcod-0411 / 1-5-2019 4 Unit Fodder Grass Gopi Krishna 50 gm Rs. 385-Anjali Barge CLUSTER2 4.00 pkt 1540.00 1540.00 1540.00  
    Fodder Grass - Gopikrishna - 50 Gm - Amar Seed 4.00 pkt 385.00/pkt 1540.00  
    01-May-2019 Chandrakant Tukaram Borate 827 spcod-0330 / 1-5-2019 2 Unit Fodder Grass Gopi Krishna 50 gm Rs. 385-Shridhar Dhembare CLUSTER2 2.00 pkt 770.00 770.00 770.00  
    Fodder Grass - Gopikrishna - 50 Gm - Amar Seed 2.00 pkt 385.00/pkt 770.00  
    01-May-2019 Vaibhav Ram Kadam 828 SPCOD-0681 / 1-5-2019 1 Unit Fodder Grass Bajra No 1 1 kg Rs. 495+30-Nayana Hule CLUSTER2 1.00 pkt 495.00 525.00 495.00 30.00  
    FODDER BAJRA No.1-Maxim Seed-1kg 1.00 pkt 495.00/pkt 495.00  
    01-May-2019 Ujjawal Dhanpal Ladhe 829 SPCOD-0587 / 1-5-2019 1 Unit PGR Induce G 500 ml Rs. 525+30-Urmila Sawant CLUSTER2 1.00 NOS 500.00 555.00 30.00 500.00 12.50 12.50
    
    above is sample i want to row no 2 in front of row no1  
    then narration contents name also should be in separate colu
    
    pls suggest
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1644662)
    
86.  ![](https://secure.gravatar.com/avatar/f7bb0e0604540e1c5ca270605207b9e2ae4f81922854fc1a07d646246e8ce0dc?s=64&d=mm&r=g) Talveer says:
    
    [February 16, 2021 at 3:49 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1974996)
    
    Thank you so much!
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-1974996)
    
87.  ![](https://secure.gravatar.com/avatar/ca132fda5de254fa4bb743e49dc7a7fb50a2bd5d71bcf982f84d0cbb655dcd46?s=64&d=mm&r=g) [Tom Hill](https://parser.name/)
     says:
    
    [August 13, 2021 at 2:36 pm](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-2021372)
    
    Copy a list of names from Excel into the Name Parser Web App and it will split the full name into the first and last name. Additionally it will validate the names, tell you the gender and predict the nationality of the name.
    
    [Reply](https://chandoo.org/wp/extract-first-name-last-name-from-email/#comment-2021372)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/extract-first-name-last-name-from-email/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Robust Dynamic (Cascading) Dropdowns Without VBA](https://chandoo.org/wp/robust-dynamic-cascading-dropdowns-without-vba/) | [Handle Volatile Functions like they are dynamite](https://chandoo.org/wp/handle-volatile-functions-like-they-are-dynamite/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)