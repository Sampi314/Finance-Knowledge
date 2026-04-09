# How to add a VBA code that you’ve find on the internet into your Excel spreadsheet? – Finexmod

**Source:** https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet

---

[Skip to content](https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet#content)

How to add a VBA code that you’ve find on the internet into your Excel spreadsheet?

I see users of Excel shy away from using the VBA by saying that they don’t know VBA. I am a user of VBA and not a developer. I get most of the codes I use from online sources and make minor tweaks and adopt them into my own financial models. if like my friend who didn’t want to use the UDF because he thinks he doesn’t know how to write a code under VBA, then I want to tell you not to be intimidated by any of these things or don’t be a perfectionist and say I don’t know how to write the code so I will not use it! 95% of things we are using on daily basis, we are ignorent on how they function including electricity. So, just get into it and learn by doing instead of studying.

If you are new to VBA, I want you to follow these steps and insert your first VBA code in your model.

Task: Let’s say you want to add a table of content in your financial model and because you are lazy and smart at the same time, you want to automate this task.

Step 1: If you have the developer tab in your Excel ribbon then go to step 2. If however, you don’t have it, then follow the below stapes:

1.  On the **File** tab, go to **Options** \> **Customize Ribbon**.
    
2.  Under **Customize the Ribbon** and under **Main Tabs**, select the **Developer** check box.

![](https://www.finexmod.com/wp-content/uploads/2021/12/show-developer-tab.jpg)

Step 2: Let’s find the code: So, go to google and search for “VBA code add table of content”. I am using the one from Microsoft community.

Copy to Clipboard

Syntax HighlighterOption Explicit Sub Create\_TOC() Dim wbBook As Workbook Dim wsActive As Worksheet Dim wsSheet As Worksheet Dim lnRow As Long Dim lnPages As Long Dim lnCount As Long Set wbBook = ActiveWorkbook With Application .DisplayAlerts = False .ScreenUpdating = False End With 'If the TOC sheet already exist delete it and add a new 'worksheet. On Error Resume Next With wbBook .Worksheets("TOC").Delete .Worksheets.Add Before:=.Worksheets(1) End With On Error GoTo 0 Set wsActive = wbBook.ActiveSheet With wsActive .Name = "TOC" With .Range("A1:B1") .Value = VBA.Array("Table of Contents", "Sheet # - # of Pages") .Font.Bold = True End With End With lnRow = 2 lnCount = 1 'Iterate through the worksheets in the workbook and create 'sheetnames, add hyperlink and count & write the running number 'of pages to be printed for each sheet on the TOC sheet. For Each wsSheet In wbBook.Worksheets If wsSheet.Name <> wsActive.Name Then wsSheet.Activate With wsActive .Hyperlinks.Add .Cells(lnRow, 1), "", \_ SubAddress:="'" & wsSheet.Name & "'!A1", \_ TextToDisplay:=wsSheet.Name lnPages = wsSheet.PageSetup.Pages().Count .Cells(lnRow, 2).Value = "'" & lnCount & "-" & lnPages End With lnRow = lnRow + 1 lnCount = lnCount + 1 End If Next wsSheet wsActive.Activate wsActive.Columns("A:B").EntireColumn.AutoFit With Application .DisplayAlerts = True .ScreenUpdating = True End With End Sub

Step 3: Go to your Excel file and open the VBA editor.

1.  On the **Developer** tab, go to **Visual Basic.** 
    
2.  If you don’t see the _Project Explorer_ window (something like the below), then you can activate it from the view tab.

Step 4: Now, on the project explorer, you see all the Excel file open. You want to insert the code in your workbook and not in the other workbooks.

1.  under your workbook you should see 2 folders. One  called **Microsoft Excel Objects** and another one called **Modules**. We want to add another module and insert the code.
2.  right click on the module and **Insert/Module** 

![](https://www.finexmod.com/wp-content/uploads/2021/12/Add-module.jpg)

1.  You should have a blank window, just copy and paste the code from the website in the blank window and you are done.

![](https://www.finexmod.com/wp-content/uploads/2021/12/paste-code-into-blank-window.jpg)

1.  Close the VBA editor and run the macro

Step 4: don’t forget to mention the source where you’ve got the code from inside your VBA macro code.

![](https://www.finexmod.com/wp-content/uploads/2021/12/ref.jpg)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-12-28T11:05:53+00:00December 23rd, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&t=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&text=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet/&title=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&title=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F&summary=I%20see%20users%20of%20Excel%20shy%20away%20from%20using%20the%20VBA%20by%20saying%20that%20they%20don%27t%20know%20VBA.%20I%20am%20a%20user%20of%20VBA%20and%20not%20a%20developer.%20I%20get%20most%20of%20the%20codes%20I%20use%20from%20online%20sources%20and%20make%20minor%20tweaks%20and%20adopt%20them%20into%20my%20own%20financial%20models.%20if%20like%20my%20fri "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&name=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F&description=I%20see%20users%20of%20Excel%20shy%20away%20from%20using%20the%20VBA%20by%20saying%20that%20they%20don%26%2339%3Bt%20know%20VBA.%20I%20am%20a%20user%20of%20VBA%20and%20not%20a%20developer.%20I%20get%20most%20of%20the%20codes%20I%20use%20from%20online%20sources%20and%20make%20minor%20tweaks%20and%20adopt%20them%20into%20my%20own%20financial%20models.%20if%20like%20my%20friend "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&description=I%20see%20users%20of%20Excel%20shy%20away%20from%20using%20the%20VBA%20by%20saying%20that%20they%20don%26%2339%3Bt%20know%20VBA.%20I%20am%20a%20user%20of%20VBA%20and%20not%20a%20developer.%20I%20get%20most%20of%20the%20codes%20I%20use%20from%20online%20sources%20and%20make%20minor%20tweaks%20and%20adopt%20them%20into%20my%20own%20financial%20models.%20if%20like%20my%20friend&media= "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet%2F&title=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F&description=I%20see%20users%20of%20Excel%20shy%20away%20from%20using%20the%20VBA%20by%20saying%20that%20they%20don%26%2339%3Bt%20know%20VBA.%20I%20am%20a%20user%20of%20VBA%20and%20not%20a%20developer.%20I%20get%20most%20of%20the%20codes%20I%20use%20from%20online%20sources%20and%20make%20minor%20tweaks%20and%20adopt%20them%20into%20my%20own%20financial%20models.%20if%20like%20my%20friend "Vk")
[Email](mailto:?body=https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet/&subject=How%20to%20add%20a%20VBA%20code%20that%20you%E2%80%99ve%20find%20on%20the%20internet%20into%20your%20Excel%20spreadsheet%3F "Email")

Related Posts
-------------

![Accuracy in Financial Modeling](https://www.finexmod.com/wp-content/uploads/2025/06/2-500x383@2x.png)

[](https://www.finexmod.com/draft-post-2/)

#### [Accuracy in Financial Modeling](https://www.finexmod.com/draft-post-2/ "Accuracy in Financial Modeling")

June 12th, 2025

![My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/wp-content/uploads/2024/09/Copy-of-White-Minimalist-Blog-Post-Linkedin-Article-Cover-500x383@2x.png)

[](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/)

#### [My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/ "My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn")

September 27th, 2024

![Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/wp-content/uploads/2024/09/contingency-Cover-500x383@2x.png)

[](https://www.finexmod.com/project-finance-contingency/)

#### [Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/project-finance-contingency/ "Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision")

September 13th, 2024 | [0 Comments](https://www.finexmod.com/project-finance-contingency/#respond)

[Page load link](https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet#)

[Go to Top](https://www.finexmod.com/how-to-add-a-vba-code-that-you-find-on-the-internet-into-your-excel-spreadsheet#)