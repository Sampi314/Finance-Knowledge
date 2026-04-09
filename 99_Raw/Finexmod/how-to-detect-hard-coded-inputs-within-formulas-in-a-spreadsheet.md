# How to detect hard-coded inputs within formulas in a spreadsheet – Finexmod

**Source:** https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet

---

[Skip to content](https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet#content)

How to detect hard-coded inputs within formulas in a spreadsheet

One of the things that you want to avoid in a financial model is to have hard-coded inputs within formulas. But why is that?

1.  **Transparency:** A user of your financial model should be aware of all the inputs used for making the projections. By hard-coding inputs within formulas is like you are sweeping dirt under the rug! not that data is dirt, on the contrary inputs are the most valuable part of a financial model but I hope you got my point. That is why one of the rules in financial modeling is transparency and hiding information in formulas breaks that rule.
2.  **Flexibility:** We live in an unstable world and things changes. So if you hard-code inputs in formulas, then you won’t be able to easily change them when needed or apply sensitivity. It’s doable but it’s inefficient. Instead you collect all inputs and present them in a defined section in your spreadsheet and this way you can easily change the input and see the impact on the model results.

Note: I see that now people go as far as flagging constants like 365 number of days in a year in formulas as a problem. I am not that much worried about the number of hours in day and in a year to be hard-coded cause these things are constants and will not change. But some people use some softwares and anything hard-coded is detected and flagged as issues. so to avoid that you can have a section in your inputs under “constants” and you can list all constants that you are using in formulas and use ranged names to refers to those constants.

Now let’s look at **the techniques I use to detect hard-coded inputs in spreadsheets**:  

**“ Bird view” technique:** Make cells display the formulas they contain, instead of the formula result by going to **_Formulas>Show Formulas_**. You can quickly detect hard-coded figures if any within formulas. It is also a good exercise to strengthen your eye muscles.

**Combo of Bird-view and acid test:** If you have thousands columns the bird-view technique might be painful so what you can do is to check the formulas in the first entry in the row (the first column) by using the bird-view technique, then use the “Acid test” meaning copy all formulas across and see if anything changes in your spreadsheet. This way you can free 2 birds with one key. You are checking the formula consistency and hard-coding within formulas.

**User Defined Function:** I learned this from https: get-digital-help.com ([Link](https://www.get-digital-help.com/find-cells-containing-formulas-with-literal-hard-coded-values/)
) and he also got it from David Hager ([link](https://dhexcel1.wordpress.com/author/dch1dch2/)
) and Chandoo has also done something similar ([Link](https://chandoo.org/wp/check-hard-coded-excel-formulas/)
)

Step 1: Save your file under anther another name.

Step 2: If you have never dealt with the VBA editor under Excel, don’t get intimidated by it. It’s very easy. You just need to copy and paste a code that is already written by someone else. Copy and Paste the below code into your file

Copy to Clipboard

Syntax Highlighter'Name User Defined Function Function CellUsesLiteralValue(Cell As Range) As Boolean 'Reference: https://www.get-digital-help.com/find-cells-containing-formulas-with-literal-hard-coded-values/ 'Check if cell has not a formula If Not Cell.HasFormula Then 'Save boolean value FALSE to variable CellUsesLiteralValue CellUsesLiteralValue = False 'Continue here if cell has a formula Else 'Use like operator to determine if cell formula contains hardcoded values, it returns TRUE if found. 'Characters enclosed in brackets allows you to match any single character in the string. ' The hashtag matches any single digit, the asterisk matches zero or more characters CellUsesLiteralValue = Cell.Formula Like "\*\[=^/\*+-/()<>, \]#\*" End If End Function

Step 3: Conditional formatting: Now you have the function but you can run it by just creating a button. Instead, we need to play with conditional formatting:

1.  Select the whole worksheet where you want to do the search
2.  Go to Home/Conditional Formatting/New rule
3.  Select the rule type “Use a formula to determine which cells to format”
4.  Type the name of the UDF: =CellUsesLiteralValue(A1)
5.  Under format select a flashy color like red for the cell background
6.  Press Ok

Step 4: Now go through the highlighted cells and see whether it is actually a hard-coded input or not because this function even picks up zero so if you have a great than zero “<0” or less than “<0”, it will flag it.

I am sure there are softwares or add-ins that can give a report with a list of hard-coded inputs included in formulas but I don’t use any paid tools. I only use the Generic Macro which is a free tool by Professor Edward Bodmer. You can download it from [edbodmer.com](http://edbodmer.com/)
.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-02-19T10:31:33+00:00February 19th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&t=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&text=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet/&title=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&title=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet&summary=One%20of%20the%20things%20that%20you%20want%20to%20avoid%20in%20a%20financial%20model%20is%20to%20have%20hard-coded%20inputs%20within%20formulas.%20But%20why%20is%20that%3F%0D%0A%0D%0A%20%09Transparency%3A%20A%20user%20of%20your%20financial%20model%20should%20be%20aware%20of%20all%20the%20inputs%20used%20for%20making%20the%20projections.%20By%20hard-coding "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&name=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet&description=One%20of%20the%20things%20that%20you%20want%20to%20avoid%20in%20a%20financial%20model%20is%20to%20have%20hard-coded%20inputs%20within%20formulas.%20But%20why%20is%20that%3F%0D%0A%0D%0A%20%09Transparency%3A%20A%20user%20of%20your%20financial%20model%20should%20be%20aware%20of%20all%20the%20inputs%20used%20for%20making%20the%20projections.%20By%20hard-coding%20inputs%20within%20formulas%20is%20like%20you%20are%20sweeping "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&description=One%20of%20the%20things%20that%20you%20want%20to%20avoid%20in%20a%20financial%20model%20is%20to%20have%20hard-coded%20inputs%20within%20formulas.%20But%20why%20is%20that%3F%0D%0A%0D%0A%20%09Transparency%3A%20A%20user%20of%20your%20financial%20model%20should%20be%20aware%20of%20all%20the%20inputs%20used%20for%20making%20the%20projections.%20By%20hard-coding%20inputs%20within%20formulas%20is%20like%20you%20are%20sweeping&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F02%2FInsert-VBA-code-into-any-spreadsheet-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet%2F&title=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet&description=One%20of%20the%20things%20that%20you%20want%20to%20avoid%20in%20a%20financial%20model%20is%20to%20have%20hard-coded%20inputs%20within%20formulas.%20But%20why%20is%20that%3F%0D%0A%0D%0A%20%09Transparency%3A%20A%20user%20of%20your%20financial%20model%20should%20be%20aware%20of%20all%20the%20inputs%20used%20for%20making%20the%20projections.%20By%20hard-coding%20inputs%20within%20formulas%20is%20like%20you%20are%20sweeping "Vk")
[Email](mailto:?body=https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet/&subject=How%20to%20detect%20hard-coded%20inputs%20within%20formulas%20in%20a%20spreadsheet "Email")

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

[Page load link](https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet#)

[Go to Top](https://www.finexmod.com/how-to-detect-hard-coded-inputs-within-formulas-in-a-spreadsheet#)