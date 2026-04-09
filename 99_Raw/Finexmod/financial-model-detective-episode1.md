# Financial model Detective, episode 1: In search for hidden things… – Finexmod

**Source:** https://www.finexmod.com/financial-model-detective-episode1

---

[Skip to content](https://www.finexmod.com/financial-model-detective-episode1#content)

Financial model Detective  
episode 1: In search for hidden things…
===================================================================

### June 25th, 2020

Financial model Detective, episode 1: In search for hidden things…

Financial model Detective, episode 1: In search for hidden things...
--------------------------------------------------------------------

I recently posted a financial model checklist that I use when I am reviewing someone else’s financial models. it is certainly not an exhaustive list and it should be the start of a conversation about what you should be looking for when reviewing a financial model.You can download it from here.

Since this is a big topic to cover, I decided to break it down and go deeper in some of the important topics.

The first set of issues in the checklist are the “Mechanical checks” meaning things like color coding, format, integrity and basically an overall check on compatibility of the financial model with the best practice financial modelling standards.

Transparency is one of the main building blocks of a standards financial model. So one of the first checks that you need to perform is to check for hidden things in the spreadsheet.

**1\. Use the Document Inspector**

I use this as the first step to detect hidden sheets. Once you run the document inspector, you will see a summary of what it finds, and one of the items is the invisible objects, hidden rows and columns, hidden worksheet. The downside of this is that it only lets you remove and not to unhide the hidden information. But the good thing about it is that it also detects the very hidden worksheets.

To open the Document Inspector, click File > Info > Check for Issues > Inspect Document

**2\. Unhide hidden worksheets**

Once you have detected hidden sheets from the document inspector, you can unhide sheets by either

going to Home>Format > Hide & Unhide or

Right clicking on any tabs and click on Unhide.

**3\. Unhide a very hidden worksheet**

Very hidden sheets are sheets that do not appear in tabs at the bottom of your workbook, nor do they show up in the Unhide dialog box. To unhide these sheets, follow these steps:

Press Alt + F11 to open the Visual Basic Editor.

In the VBAProject window, go through the list of worksheets and identify and click on the worksheet that is very hidden.

In the Properties window (Press F4 in VBA to view properties window), set the Visible property to -1 – xlSheetVisible.

**4\. Unhide Columns and Rows**

To unhide everything in a worksheet.

Select the entire worksheet and select Unhide for each by either right mouse click anywhere in the headings or by pressing Shift + F10 and selecting Unhide.

**5\. Unhide objects**

Hidden object should also be depicted from document inspector (step 1).

To manage objects in your worksheet, you can use the Excel tool called Selection Pane and accessible :

From Home >Editing>Find & Select >Selection Pane

Or by using the shortcut keyboard Alt + F10

**6\. Hidden names**

The Document Inspector can also find hidden names in your workbook but can not delete them. To view and eventually delete hidden names, you need to run a macro.

> Sub ShowAllNames()  
> Dim n As Name  
> For Each n In ActiveWorkbook.Names  
> n.Visible = True  
> Next n  
> End Sub

**7\. Hidden Macros**

While reviewing someone else’s financial model, don’t miss the macros. Even if they are no macro buttons in the spreadsheet, there might be some macros working behind the scenes.

Check the list of available macros by :

Pressing Alt+F8 to open the macro dialogue box and you should be able to edit/view the codes.

Some macros might not appear in the macro dialogue box. To check for hidden macros press Alt +F11 to open VBA and check for these:

Private subroutine : The code simply starts with Private Sub name()

Functions: another way to hide a macro from the macro dialogue box is to declare it as a function

Also check for Private Subs and functions under worksheets in VBA. Some codes are written directly inside the sheet rather than as a separate module. In the right window pan of the VBA, you will find the list of worksheets available in the workbook. Double click on each worksheet name to detect any codes.

While inspecting the financial model for hidden information, make sure to keep track of the list of hidden things you find in the spreadsheet so that you can report to your organization and eventually include them in your Q&A sheet on the financial model. You can download my suggested Q&A sheet from [here](https://www.eloquens.com/tool/75kU0g/finance/financial-modeling-courses-tutorials/q-a-tracking-sheet-for-a-financial-model-excel?ref=FinExMod)
.

However, Many of these checks can be automated by using macros or tools that can check for these things but you can also use the excel document inspector tool and couple of clicks to spot hidden information in any spreadsheet.

Stay tuned for the next episode of Financial Model Detective…

[Hedieh Kianyfard](https://www.finexmod.com/author/hedi/ "Posts by Hedieh Kianyfard")
2020-07-26T02:07:48+00:00June 25th, 2020|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&t=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6 "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&text=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6 "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/financial-model-detective-episode1/&title=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6 "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&title=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6&summary=I%20recently%20posted%20a%20financial%20model%20checklist%20that%20I%20use%20when%20I%20am%20reviewing%20someone%20else%E2%80%99s%20financial%20models.%20it%20is%20certainly%20not%20an%20exhaustive%20list%20and%20it%20should%20be%20the%20start%20of%20a%20conversation%20about%20what%20you%20should%20be%20looking%20for%20when%20reviewing%20a%20financia "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&name=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6&description=I%20recently%20posted%20a%20financial%20model%20checklist%20that%20I%20use%20when%20I%20am%20reviewing%20someone%20else%E2%80%99s%20financial%20models.%20it%20is%20certainly%20not%20an%20exhaustive%20list%20and%20it%20should%20be%20the%20start%20of%20a%20conversation%20about%20what%20you%20should%20be%20looking%20for%20when%20reviewing%20a%20financial%20model.You%20can%20download%20it%20from%20here.%0D%0ASince%20this%20is%20a%20big "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&description=I%20recently%20posted%20a%20financial%20model%20checklist%20that%20I%20use%20when%20I%20am%20reviewing%20someone%20else%E2%80%99s%20financial%20models.%20it%20is%20certainly%20not%20an%20exhaustive%20list%20and%20it%20should%20be%20the%20start%20of%20a%20conversation%20about%20what%20you%20should%20be%20looking%20for%20when%20reviewing%20a%20financial%20model.You%20can%20download%20it%20from%20here.%0D%0ASince%20this%20is%20a%20big&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2020%2F06%2F20200724-Finexmod-Web-Illustrations-22.png "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode1%2F&title=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6&description=I%20recently%20posted%20a%20financial%20model%20checklist%20that%20I%20use%20when%20I%20am%20reviewing%20someone%20else%E2%80%99s%20financial%20models.%20it%20is%20certainly%20not%20an%20exhaustive%20list%20and%20it%20should%20be%20the%20start%20of%20a%20conversation%20about%20what%20you%20should%20be%20looking%20for%20when%20reviewing%20a%20financial%20model.You%20can%20download%20it%20from%20here.%0D%0ASince%20this%20is%20a%20big "Vk")
[Email](mailto:?body=https://www.finexmod.com/financial-model-detective-episode1/&subject=Financial%20model%20Detective%2C%20episode%201%3A%20In%20search%20for%20hidden%20things%E2%80%A6 "Email")

### Related Posts

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/financial-model-detective-episode1)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/financial-model-detective-episode1#)

[Go to Top](https://www.finexmod.com/financial-model-detective-episode1#)