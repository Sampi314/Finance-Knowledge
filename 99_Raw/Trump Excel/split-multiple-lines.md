# How to Split Multiple Lines in a Cell into a Separate Cells / Columns

**Source:** https://trumpexcel.com/split-multiple-lines

---

[Skip to content](https://trumpexcel.com/split-multiple-lines/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/split-multiple-lines/#below-title)

In Excel, you can use the [Text to Columns functionality](https://trumpexcel.com/excel-text-to-columns-examples/)
 to split the content of a cell into multiple cells.

You can specify the delimiter (such as a space, comma, or tab) and the Text to Columns would use this delimiter to split the content of the cells.

Examples of this include splitting first and last names, or username and domain name in [email ids](https://trumpexcel.com/extract-usernames-from-email-ids/)
.

However, if you have a dataset where the delimiter is a line break (in the same cell), it gets tricky to split these multiple lines in the same cell into separate cells/columns.

For example, you can have a dataset as shown below, where you need to split multiple lines in the address (separated by line breaks) into separate cells.

![Split Multiple Lines in a Cell into a Separate Cells or Columns - Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20338'%3E%3C/svg%3E)

This would allow you to have the Name, Street, City, and Country in separate cells.

So the result would look something as shown below:

![Split Multiple Lines in a Cell into a Separate Cells or Columns - Result needed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20696%20336'%3E%3C/svg%3E)

Now to separate each part of the address, we can use the Text to Columns functionality (with a twist).

Note: If you’re wondering how I managed to insert each address element into a new line in the same cell, you can do that by using the keyboard shortcut – ALT + Enter (it enters a line break). You can [read more about it here](https://trumpexcel.com/insert-line-break-in-excel/)
.

Also read: [Go To New Line In Same Cell in Excel](https://trumpexcel.com/start-a-new-line-in-excel-cell/)

Using Text to Column to Split Multiple Lines in a Cell
------------------------------------------------------

Below are the steps that will split multiple lines in a single cell into separate cells:

*   Select the entire dataset that you want to split.
*   Go to the Data tab.![Data Tab in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20129'%3E%3C/svg%3E)
*   In the Data Tools group, click on the Text to Columns option.![Text to Columns option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20632%20134'%3E%3C/svg%3E)
*   In the Text to Columns dialog box, in Step 1 of 3, select Delimited and click ‘Next’.![Step 1 - Select Delimited checkbox](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20413'%3E%3C/svg%3E)
*   In Step 2 of 3, uncheck any existing Delimiters selection, and select the ‘Other’ option. Now Use the keyboard shortcut **Control + J** (hold the ‘Control’ key and then press the ‘J’ key). You will not see anything in the box except a tiny blinking dot (if you look hard). Also, you will see the expected result in the ‘Data preview’ section (as shown below). Click on Next.![Step 2 in Text to Columns - Control + J Keyboard Shortcut](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20413'%3E%3C/svg%3E)
*   In Step 3 of 3, change the ‘Destination’ cell to the one where you want the output. In my example, I want the result in B2, so I changed the value to $B$2.![Step 3 - Specify the destination](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20507%20413'%3E%3C/svg%3E)
*   Click on Finish.

The above steps would automatically split the content of the cells based on where the line break occurs in each cell.

Note that if you don’t want to keep the original data (it’s always advisable to do so though), you don’t need to specify the destination cell. It will simply overwrite the existing data and give you the result.

Also, in case you already have data in the cells where you are about to get the result of Text to Columns, Excel will show you a prompt letting you know that you will be overwriting the existing data. You can choose to overwrite or cancel

![Excel Text to Columns Prompt - there is already data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20349%20115'%3E%3C/svg%3E)

**How does this work?**

When you use the keyboard shortcut Control J, it specifies the line break as the delimiter in the Text to Columns wizard.

Now, Text to Columns checks each cell for line breaks and use it to split the content into separate cells.

Note that Text to Columns would always split the content of the cells in separate columns. If you want to get the result in cells in different rows, you can transpose the result ([as shown here](https://trumpexcel.com/transpose-data-excel/)
).

**You May Also Like the Following Excel Tutorials:**

*   [How to Split Cells in Excel](https://trumpexcel.com/split-cells-in-excel/)
    .
*   [How to Remove Line Breaks in Excel](https://trumpexcel.com/remove-line-break-excel/)
    
*   [Split Text into Multiple Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)
    
*   [How to Number Rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
    
*   [Separate First And Last Name In Excel](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Quickly Combine Cells in Excel](https://trumpexcel.com/combine-cells-in-excel/)
    .
*   [CONCATENATE Excel Range (with and without separator)](https://trumpexcel.com/concatenate-excel-ranges/)
    .
*   [Transpose Multiple Rows into One Column](https://trumpexcel.com/transpose-multiple-rows-into-one-column/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

50 thoughts on “How to Split Multiple Lines in a Cell into a Separate Cells / Columns”
--------------------------------------------------------------------------------------

1.  Thank u so much
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14843)
    
2.  Awesome it Works
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14618)
    
3.  Thank You so much sir! Bless you!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14576)
    
4.  If I could I would kiss you right now, thank you so much <3
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14571)
    
5.  This is amazing! Saved me so much time. Thanks!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14547)
    
6.  Worked thanks
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14433)
    
7.  thanks very use full
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14308)
    
8.  This Was very Useful. Thanks.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-14190)
    
9.  Hey there, I don’t know somebody told you or not … but I must tell you that YOU ARE A GENIOUS” 🙂
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13976)
    
10.  Thank you so much!!!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13600)
    
11.  Thanks much!!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13503)
    
12.  OMG that’s awesome
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13472)
    
13.  AWESOME
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13286)
    
14.  This is awesome. Thanks so much!!!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13253)
    
15.  I am so grateful to you for this awesome trick. It saved my life and many hours. God Bless You.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12716)
    
16.  Thanks for your article. I had read about the tweak with Ctrl+J elsewhere too. I’m on Excel 2011 for Mac, though, and what happens with this is that the other lines of text seem to vanish in the air. Can’t find any trace of the text after the first line.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12509)
    
17.  I can’t explain , How much i thanks… Save my lot of time…
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11937)
    
18.  If I could reach through this computer I’d kiss you !! This is EXACTLY what I was looking for! Thank you !!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11836)
    
19.  That was awesome! I never new about the ctrl+j trick.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11726)
    
20.  Saved my sanity! thank you.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11496)
    
21.  It worked…  
    Thank you so much..
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11228)
    
22.  helped a lot !!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11211)
    
23.  Thanks Buddy, you are a life savior
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11127)
    
24.  Thanks, dude.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-11089)
    
25.  Do you know what the equivalent line break keystroke is on a mac?
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10980)
    
    *   Shift + 2 + PC
        
        [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12055)
        
        *   My text only populates the first line and deletes the others. Maybe I don’t understand your command shift+2+PC (what is PC)
            
            [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12170)
            
            *   Same happens to me
                
                [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12510)
                
26.  AMAZING … been working on an issue for too long and this WORKED! Thanks
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10923)
    
27.  Thanks very much! You saved me about 72 hours
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10851)
    
28.  very good thank you!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10836)
    
29.  good
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10793)
    
30.  thank you
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10787)
    
31.  This is perfect, thank you so much!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10784)
    
32.  Thank You. This is really helpful.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10700)
    
33.  HI i need to split one cell in different number of row lines in excel. please help with that
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10691)
    
    *   I am in a similar situation. Did you find out how to split cell into rows?
        
        Thanks,  
        Abdul
        
        [Reply](https://trumpexcel.com/split-multiple-lines/#comment-13720)
        
34.  Awesome, thanks so much! Just want to highlight that Harry Potter’s address is actually, 4 Privet Drive 😉
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10616)
    
35.  very good trick… i like it… Thanks !! it helped me a lot.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10604)
    
36.  I’m workind on a Apple Computer… using Excel 2001…. the shortcut “control+J” isn’t working… do you the shortcut for an apple keyboard ?  
    thanks for help !
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10475)
    
    *   The shortcut Cmd+J does not work on Mac, but Ctrl+J does, in Excel 2011. However the dataset gets truncated after the first line.
        
        [Reply](https://trumpexcel.com/split-multiple-lines/#comment-12511)
        
37.  thank you! this was very helpful. People like you keep the world going round 🙂
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10403)
    
38.  Brilliant.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10290)
    
39.  See image:  
    I want to break out the ID type so that only the “26” lines are left and have the information that lines up in MPI ID be the only thing that is displayed.(basically get rid of anything other than “26” in the ID Type Is this possible? Once this is accomplished then I would like to have that remaining information populated back into their columns with line breaks so that it will correspond with the first 2 columns.  
    [https://uploads.disquscdn.com/images/f7e1f62d63579e88fab78241ba8ac1e0e9335ed08e76c41a90c8d26f5296aa03.jpg](https://uploads.disquscdn.com/images/f7e1f62d63579e88fab78241ba8ac1e0e9335ed08e76c41a90c8d26f5296aa03.jpg)
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10257)
    
40.  I want to only see “26” and it’s corresponding information in the next column. (see image)  
    How can I accomplish this? Also how do I then take only the “26” information and put it back into 1 cell? This is a merged cell with line breaks in each column and since there is other data in the 1st 2 columns that I would also need to keep as a reference.I appreciate your help  
    [https://uploads.disquscdn.com/images/f7e1f62d63579e88fab78241ba8ac1e0e9335ed08e76c41a90c8d26f5296aa03.jpg](https://uploads.disquscdn.com/images/f7e1f62d63579e88fab78241ba8ac1e0e9335ed08e76c41a90c8d26f5296aa03.jpg)
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10256)
    
41.  AWESOME!
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-10219)
    
42.  Hands down the best procedure I’ve found for converting multiple Lines in a cell into separate cells / columns
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-9975)
    
43.  always wondered how to do this
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-9843)
    
44.  HI Summit – I am using excel 2016 and the CTRl+J – did not work.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-9838)
    
45.  Appreciate this; But whether there is any way to do this by the help of formula.
    
    [Reply](https://trumpexcel.com/split-multiple-lines/#comment-9831)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/split-multiple-lines/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK