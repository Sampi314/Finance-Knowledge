# Financial model detective, Episode 2: Looking for misplaced inputs – Finexmod

**Source:** https://www.finexmod.com/financial-model-detective-episode2

---

[Skip to content](https://www.finexmod.com/financial-model-detective-episode2#content)

Financial model detective  
Episode 2: Looking for misplaced inputs
===================================================================

### June 25th, 2020

Financial model detective, Episode 2: Looking for misplaced inputs

Looking for misplaced inputs
----------------------------

We’ve seen couple of techniques on how to detect hidden things in a spreadsheet earlier in the previous post, so now would be a good time to focus solely on how you can detect misplaced inputs in a spreadsheet.

Mission 1: Detect hard-coded inputs within calculation sheets

Background: For transparency and ease of access to model assumptions, the modeller should dedicate separate worksheet or a separate place on a single model worksheet for assumptions. Also, the modeller should categories assumptions by type.

Detecting techniques: Use “Go To” function to identify hard-coded values in a spreadsheet. The F5 key gives you quick access to the “Go To” function.

Step 1: Save your file under another name

Step 2: Go to the first calculation sheet in the financial model and Press F5>click Special> select constants>check only the numbers box.

![](https://www.finexmod.com/wp-content/uploads/2020/06/Figure-3.jpg)

Step 3: Click **OK** and all constants (hard-coded inputs) will be selected.

Step 4: Once all constant all selected, open the **Format Cells** dialog by pressing **Ctrl + 1** or go to _Home tab_ > _Font_\> _Fill Color…_ and change the background color to red.

Step 4: you will have to repeat the above steps for each worksheet individually.

**Mission 2:** Detect hard coded figures within formulas
--------------------------------------------------------

![](https://www.finexmod.com/wp-content/uploads/2020/06/0.jpg)

**Background:** Best practice is to avoid hard-coding figures within formulas and to have all inputs documented in a separate section of the financial model.

**Detecting techniques:**

1.  “ Bird view” technique: Make cells display the formulas they contain, instead of the formula result by going to **_Formulas>Show Formulas_**. You can quickly detect hard-coded figures if any within formulas.

![](https://www.finexmod.com/wp-content/uploads/2020/06/Figure-7-2.png)

2\. “INQUIRE”: This is an add in developed by Microsoft itself. You can use the spreadsheet inquire to analyse your spreadsheet and get a report showing detailed information about the workbook as well as details of all formula within the workbook that contain a hard coded value.

**To enable INQUIRE in Excel**

*   Go to File > Options > Add-Ins.
*   Manage box, select COM add-Ins and click Go.
*   Tick the box next to INQUIRE and click OK.

**Start the workbook analysis**
-------------------------------

*   Click I**nquire > Workbook Analysis.**
*   Under items, scroll down to **Formula** and then select “**with numeric constants**”.
*   In the results pane you will now see details of all formula within the workbook that constant a numeric constant or a hard coded value within a formula.

![](https://www.finexmod.com/wp-content/uploads/2020/06/Figure-8.jpg)

Note that if a sheet within a workbook has more than 100 million cells, you will get an error message and you will not see results directly in the results pane. You can however export the data to a report by clicking the Excel Export button.

![](https://www.finexmod.com/wp-content/uploads/2020/06/Figure-9.jpg)

Last step is to list your findings in the Q&A sheet.

![](https://www.finexmod.com/wp-content/uploads/2020/06/Figure-10.jpg)

[Hedieh Kianyfard](https://www.finexmod.com/author/hedi/ "Posts by Hedieh Kianyfard")
2020-07-26T02:23:51+00:00June 25th, 2020|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&t=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&text=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/financial-model-detective-episode2/&title=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&title=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs&summary=We%E2%80%99ve%20seen%20couple%20of%20techniques%20on%20how%20to%20detect%20hidden%20things%20in%20a%20spreadsheet%20earlier%20in%20the%20previous%20post%2C%20so%20now%20would%20be%20a%20good%20time%20to%20focus%20solely%20on%20how%20you%20can%20detect%20misplaced%20inputs%20in%20a%20spreadsheet.%0D%0A%0D%0AMission%201%3A%20Detect%20hard-coded%20inputs%20within "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&name=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs&description=We%E2%80%99ve%20seen%20couple%20of%20techniques%20on%20how%20to%20detect%20hidden%20things%20in%20a%20spreadsheet%20earlier%20in%20the%20previous%20post%2C%20so%20now%20would%20be%20a%20good%20time%20to%20focus%20solely%20on%20how%20you%20can%20detect%20misplaced%20inputs%20in%20a%20spreadsheet.%0D%0A%0D%0AMission%201%3A%20Detect%20hard-coded%20inputs%20within%20calculation%20sheets%0D%0A%0D%0ABackground%3A%20For%20transparency%20and%20ease "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&description=We%E2%80%99ve%20seen%20couple%20of%20techniques%20on%20how%20to%20detect%20hidden%20things%20in%20a%20spreadsheet%20earlier%20in%20the%20previous%20post%2C%20so%20now%20would%20be%20a%20good%20time%20to%20focus%20solely%20on%20how%20you%20can%20detect%20misplaced%20inputs%20in%20a%20spreadsheet.%0D%0A%0D%0AMission%201%3A%20Detect%20hard-coded%20inputs%20within%20calculation%20sheets%0D%0A%0D%0ABackground%3A%20For%20transparency%20and%20ease&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2020%2F07%2F20200724-Finexmod-Web-Illustrations-23.png "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-model-detective-episode2%2F&title=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs&description=We%E2%80%99ve%20seen%20couple%20of%20techniques%20on%20how%20to%20detect%20hidden%20things%20in%20a%20spreadsheet%20earlier%20in%20the%20previous%20post%2C%20so%20now%20would%20be%20a%20good%20time%20to%20focus%20solely%20on%20how%20you%20can%20detect%20misplaced%20inputs%20in%20a%20spreadsheet.%0D%0A%0D%0AMission%201%3A%20Detect%20hard-coded%20inputs%20within%20calculation%20sheets%0D%0A%0D%0ABackground%3A%20For%20transparency%20and%20ease "Vk")
[Email](mailto:?body=https://www.finexmod.com/financial-model-detective-episode2/&subject=Financial%20model%20detective%2C%20Episode%202%3A%20Looking%20for%20misplaced%20inputs "Email")

### Related Posts

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

[Page load link](https://www.finexmod.com/financial-model-detective-episode2#)

[Go to Top](https://www.finexmod.com/financial-model-detective-episode2#)