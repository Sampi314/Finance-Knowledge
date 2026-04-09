# Send Email From Excel + FREE Email Generator Tool

**Source:** https://trumpexcel.com/send-email-from-excel-hyperlink

---

[Skip to content](https://trumpexcel.com/send-email-from-excel-hyperlink/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/send-email-from-excel-hyperlink/#below-title)

Yes, it’s true! You can send emails from Excel by using the [HYPERLINK function](https://trumpexcel.com/hyperlinks/)
.

In this blog post, I will show you various ways to use the HYPERLINK function to send emails from Excel. There is also a bonus Email Generator [Excel Template](https://trumpexcel.com/free-excel-templates/)
 available for download at the end of this post.

Let me first explain the Hyperlink function:

Hyperlink Function Syntax:
--------------------------

\=HYPERLINK(link\_location, \[friendly\_name\]

*   **link\_location:** This is a mandatory argument where you give the link of a cell, worksheet, workbook, or an external URL.
*   **friendly\_name:** This is optional, and displays the text which is hyperlinked to the specified location.

Send Email from Excel
---------------------

Coming back to how to send email from excel, you can use the fact that hyperlink can handle “mailto” URL property and can be used to make a hyperlink that would automatically construct the email. Here is how you can construct a formula to create various components of the email.

### Single Recipient Email Id

\=HYPERLINK("**mailto:abc@trumpexcel.com**","Generate Email")

This would open the email client with the email id abc@trumpexcel.com in the ‘To’ field.

### Multiple Recipients Email Id

\=HYPERLINK("mailto:abc@trumpexcel.com**,def@trumpexcel.com**","Generate Email")

For sending the email to multiple recipients, use comma to separate email ids. This would open the email client with all the email ids in the ‘To’ field.

### Add Recipients in CC and BCC List

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com**?cc=123@trumpexcel.com&bcc=456@trumpexcel.com**","Generate Email")

To add recipients to CC and BCC list, use question mark ‘?’ when ‘mailto’ argument ends, and join CC and BCC with ‘&’. Now when you click on the link in excel, it would have the first 2 ids in ‘To’ field, 123@trumpexcel.com in ‘CC’ field and 456@trumpexcel.com in the ‘BCC’ field.

### Add Subject Line

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&**subject=Excel is Awesome**","Generate Email")

You can add a subject line by using the &Subject code. In this case, this would add ‘Excel is Awesome’ in the ‘Subject’ field.

### Add Single Line Message in Body

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&subject=Excel is Awesome&**body=I love Excel**","Email Trump Excel")

This would add a single line ‘I love Excel’ to the email message body.

### Add Multiple Lines Message in Body

\=HYPERLINK("mailto:abc@trumpexcel.com,def@trumpexcel.com?cc=123@trumpexcel.com&bcc=456@trumpexcel.com&subject=Excel is Awesome&**body=I love Excel.%0AExcel is Awesome**","Generate Email")

To add multiple lines in the body you need to separate each line with **%0A**. If you wish to introduce 2 [line breaks](https://trumpexcel.com/start-a-new-line-in-excel-cell/)
, add **%0A** twice, and so on.

BONUS – Email Generator Tool in Excel
-------------------------------------

Now that you know how to send emails from Excel, it is not rocket science to create a simple tool that can generate an email with a single click.

I have created a [template](https://trumpexcel.com/free-excel-templates/)
 where you need not worry about memorizing the syntax. Just type the email ids, subject line, and message, and this will automatically do it for you.

![Send Email from Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20788%20328'%3E%3C/svg%3E)

_**Download Email Generator Excel Tool  
[![Download File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2016/11/Excel-Email-Generator.xls)
  
**_

_Note: This works only when you have a default email client set in your system (such as Outlook, Lotus Notes, Gmail). If the email client is not set, this may not work._

**You May Also Like the Following Excel Tutorials:**

*   [How to Quickly Remove Hyperlinks from a Worksheet in Excel](https://trumpexcel.com/remove-hyperlinks/)
    
*   [How to Quickly Find Hyperlinks in Excel (using Find and Replace)](https://trumpexcel.com/find-hyperlinks-in-excel/)
    
*   [Create Dynamic Hyperlinks in Excel](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/)
    
*   [Quickly Create Summary Worksheet with Hyperlinks in Excel](https://trumpexcel.com/create-summary-worksheet-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

35 thoughts on “Send Email From Excel Using Hyperlink Function + BONUS Email Generator Tool”
--------------------------------------------------------------------------------------------

1.  How do you get the users default outlook signature to appear?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-14677)
    
2.  Hey, great article. helps a bucket load.  
    Is it possible to add the cell value to the email, ie when the email is sent, it will add he value that is in for example A4?  
    The value of the cell does not influence if or when the email is sent, the value is just added as part of the email,
    
    cheers
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-13294)
    
3.  This is amazing, thank you. Is it possible for the mailto address to be dynamic, i.e. to build the email address based on the inputs into other cells in the row? Our email addresses follow a set format, so if someone writes “Joe” in cell A1 and “Bloggs” in cell A2, I’d like them to be able to click the link and outlook generate an email to “joe.bloggs@domain.com”.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-13030)
    
4.  Can we add table in the body?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-12857)
    
5.  When i putting more words then its showing error message. Would you please help me how could i add long mail body
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-12818)
    
6.  Fantastic! but is it possible attached file?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-11533)
    
7.  Love it soooooo much
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-10920)
    
8.  Hi friend, How can I add more than 4 email in your template? please help
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-10266)
    
9.  Can we select From Address using this formula?? I am handling 3 email accounts, so I require to select From Address manually. Please revert.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3927)
    
10.  The page you are trying to access doesn’t exist. Try searching for it below or click here to return to the homepage. =(
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3816)
    
11.  how to add an attachment if path is already copy in any cell?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3317)
    
    *   Is it possible to edit the cells which are currently hidden? If Cc & Bcc are left empty they currently generate an error in the Cc field of the message and I would like to try and fix this for my application.
        
        I regularly send out a “club” newsletter and include Yes & No RSVP links that generate a easy way for the recipient to reply. At the moment I write the whole mailto links manually in a text editor and then copy and paste them as hyperlinks into the email with the newsletter. If I can customise the spreadsheet to suit my needs it would save me a lot of time each month. Thanks
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3487)
        
12.  how to add an attachment if path is already copy in any cell?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3316)
    
13.  how to add an attachment if path is already copy in any cell?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3315)
    
14.  I am trying to create a hyperlink or formula that will generate an email but also include the file I am in as an attachment. Please help me.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2592)
    
15.  SL  
    NAME  
    FATHERS NAME  
    CASTE  
    QUALIFICATION  
    MOBILE NO.
    
    1  
    NISHA PATHAK  
    MUKESH PATHAK  
    OBC  
    12th  
    8435137818
    
    2  
    MADHU CHANDRAKAR  
    DASHRATH LAL CHANDRAKAR  
    OBC  
    12th  
    9977020227
    
    3  
    SUSHMA CHANDRAKAR  
    BABU LAL CHANDRAKAR  
    OBC  
    12th  
    7089407553
    
    4  
    SONMAT DHRUW  
    DHASUN RAM DHRUW  
    ST  
    12th  
    7354356854
    
    5  
    BHUNESHWARI DEWANGAN  
    GOVIND DEWANGAN  
    OBC  
    8th  
    8871047773
    
    6  
    SHOBHA RAJPUT  
    MUNIR RAJPUT  
    OBC  
    5th  
    7879006008
    
    7  
    SONIYA BARIK  
    AASHRIT BARIK  
    OBC  
    12th  
    9926753989
    
    8  
    MANJULATA PATEL  
    AMLESH PATEL  
    OBC  
    10th  
    8602373206
    
    9  
    SUKVANTIN BAI  
    LALIT DHRUW  
    ST  
    8th  
    7354818561
    
    10  
    PILESHWARI DHRUW  
    ASHOK KUMAR DHRUW  
    ST  
    12th  
    9329361963
    
    11  
    SUSHILA DHRUW  
    LOCHAN DHRUW  
    ST  
    12th  
    7354105757
    
    12  
    RITU VAISHNAV  
    NAGENDRA VAISHNAV  
    OBC  
    10th  
    8959745123
    
    13  
    NANDANI VISHVKARMA  
    HEMANT VISHVKARMA  
    OBC  
    10th  
    9575528821
    
    14  
    LATA YADAW  
    CHANDU YADAW  
    OBC  
    10th  
    7415884170
    
    15  
    UMA SAHU  
    SANJAY SAHU  
    OBC  
    12th  
    8889637598
    
    16  
    NAVNIT KAUR  
    KALYAN SING KAUR  
    OBC  
    12th  
    9009151220
    
    17  
    CHANDRAKALA TANDI  
    CHINTA RAM TANDI  
    SC  
    10th  
    9926709810
    
    18  
    TORAN MAHANAND  
    PAWAN SING MAHANAND  
    SC  
    10th  
    9753318605
    
    19  
    TARUNA KUMAR  
    SURESH KUMAR  
    SC  
    10th  
    9575765262
    
    20  
    MANJU MAHANAND  
    SARJU MAHANAND  
    SC  
    12th  
    7697069210
    
    21  
    BHARTI NAGESH  
    GOPAL NAGESH  
    SC  
    10th  
    8889052477
    
    22  
    RAJNI SONWANI  
    GOPAL SONWANI  
    SC  
    12th
    
    23  
    KIRAN CHAUHAN  
    KISHAN LAL CHAUHAN  
    SC  
    12th  
    8889623421
    
    24  
    KANCHAN CHAUHAN  
    VINOD CHAUHAN  
    SC  
    10th  
    8602255781
    
    25  
    SUNITA SIKA  
    GULAB SIKA  
    SC  
    10th
    
    26  
    SIMRAN TANDI  
    KUNURAM TANDI  
    SC  
    12th  
    7566676234
    
    27  
    RUKHMANI TANDI  
    BRIZLAL TANDI  
    SC  
    12th  
    8463039313
    
    28  
    DIPIKA CHAUHAN  
    KISHOR CHAUHAN  
    SC  
    12th  
    9755175440
    
    29  
    SARITA TANDI  
    DINESH TANDI  
    SC  
    12th  
    7089102231
    
    30  
    NIKITA TANDI  
    RAJKUMAR TANDI  
    SC  
    12th  
    8962519302
    
    31  
    RUCHIKA NEHA QLAIV  
    SANJAY QLAIV  
    ISAI  
    12th  
    8223982695
    
    32  
    KIRAN DHRUW  
    LOCHAN DHRUW  
    ST  
    10th  
    7354105757
    
    33  
    ISHWARI BHATT  
    RAMKUMAR BHATT  
    OBC  
    12th  
    8120285106
    
    34  
    AARTI CHANDRAKAR  
    NARESH CHANDRAKAR  
    OBC  
    10th  
    8435800606
    
    35  
    BHARTI JAIN  
    HARISH JAIN  
    OBC  
    12th  
    9575156411
    
    36  
    JIGYASA SHRIVASTAV  
    JITENDRA SHRIVASTAV  
    OBC  
    10th  
    9753860463
    
    37  
    DIPTI SAHU  
    RAVI SHANKAR SAHU  
    OBC  
    12th  
    9753217676
    
    38  
    LAXMI SAHU  
    MANOHAR LAL SAHU  
    OBC  
    12th  
    9926164827
    
    39  
    NITU YADAW  
    SHANKARLAL YADAW  
    OBC  
    12th  
    8085881425
    
    40  
    RUCHI DEWANGAN  
    RAJESH DEWANGAN  
    OBC  
    12th  
    7772056017
    
    41  
    GARIMA BHATT  
    HEMANT BHATT  
    OBC  
    10th  
    8109890430
    
    42  
    JYOTI SHARMA  
    PARAS SHARMA  
    OBC  
    10th  
    7049023235
    
    43  
    RINU SAMANTRAY  
    SUSHIL SAMANTRAY  
    OBC  
    10th  
    7697982949
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2582)
    
16.  Hi,  
    That was a good info..  
    Thanks..  
    Can we insert a picture .jpg in the body instead “&body=text” or any cell reference &G3″.
    
    insert a picture from a location in the pc.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2534)
    
17.  Hi sumit, great work. Is there a way to attach the files in this.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2144)
    
    *   Hello Fredrick.. Thanks for commenting. You can not attach a file using this template. If you are sending a file that resides on a network and the recipient also has access to the same network, then you can send the link to the file and it will work. But it won’t work otherwise
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2145)
        
        *   Thanks for the prompt reply sumit.
            
            [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-2146)
            
18.  Hi mate, great site. Just quick one. When I input body text into the hyperlink, it removes my signature from the email. Any ideas on how i can fix this?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1991)
    
19.  Hi Summit,  
    I wonder if I can send same text otherthan then attention (Name & Designation of the recipient) to multiple email IDs through gmail/yahoo/hotmail with a single click?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1648)
    
    *   Hi Asif.. This works with your default email client, which could be only one of these.
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1650)
        
20.  I’m trying to actually DO the send email via a hyperlink, not just to “generate” the email. Is that possible?
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1637)
    
    *   Hi Roger.. It can create the email, but it can not send it automatically. The send button needs to be pressed manually.
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1638)
        
21.  Hi Sumit
    
    Greetings of the day  
    Its a good informative without VBA, I am looking such solution
    
    I have Query
    
    can we insert a range of cells in the body of the Email
    
    example i am looking
    
    Hi Team
    
    Need your …….
    
    template:  
    1  
    2  
    3  
    4  
    5  
    6
    
    attached  
    1  
    2  
    3
    
    Regards  
    Dutt
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1616)
    
    *   Hi Goparaju.. This can be done. All you need to do is create this construct in the body section in the template. For example, if you have the list in A1 and A2, you can use the formula:
        
        \=”1. “&A1&CHAR(10)&”2. “&A2
        
        Char(10) here would work as Alt + Enter. In the similar fashion, you can create for multiple items.
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1639)
        
        *   Hi Sumit,  
            Can you please help me as I want to add multiple email address then what else need to be done because it is showing error as I do not add more then 2 or 4 email address.  
            Please advise.
            
            [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3122)
            
            *   Hello Amit.. The problem is due to the fact that Hyperlink function can’t handle more than 256 characters at a time. You can add more email address, but then you’ll have to remove the ones from CC/BCC or cut short on the body text. I just noticed this, and will see if there could be a workaround
                
                [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-3138)
                
                *   Sumit,
                    
                    Did you find a work around?
                    
                *   Buy the way, I love these templates!
                    
                *   Hi Sumit,  
                    finding this really helpful, but I am suffering the same problem with multiple emails via hyperlink.
                    
                    Have you managed to find a workaround for this?  
                    Many thanks,
                    
22.  this is really useful.
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1574)
    
23.  This is great!
    
    [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1530)
    
    *   Thanks.. Glad you liked it!
        
        [Reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#comment-1531)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/send-email-from-excel-hyperlink/#respond)

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