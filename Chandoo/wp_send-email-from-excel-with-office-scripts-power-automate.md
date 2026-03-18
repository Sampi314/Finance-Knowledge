# Send Email from Excel with Office Scripts & Power Automate » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/send-email-from-excel-with-office-scripts-power-automate

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Office Scripts](https://chandoo.org/wp/category/office-scripts/)
    , [Power Automate](https://chandoo.org/wp/category/power-automate/)
    

Send Email from Excel with Office Scripts & Power Automate
==========================================================

*   Last updated on March 21, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**_Do you have an Excel report or graphs that need to be emailed to various people every month?_** We can use Excel automation features to do this task quite easily.

![send email from Excel](https://chandoo.org/wp/wp-content/uploads/2023/03/send-email-from-Excel.jpg)

The inspiration – A client request for Excel Email Solution
-----------------------------------------------------------

The idea for this came from a recent project I did for a client. They wanted me to build an Excel workbook which shows latest sales summary and then allows them to email the _snapshot_ to the relevant people in **one click**.

Here is a snapshot of the solution I created for them (with dummy data):

![](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2544.png)

1.  You select a product and see the dynamic report
2.  Pick the person who will receive the report (from drop-down list)
3.  Click on the “Send email” button to send the email

The ingredients – What we need
------------------------------

Here, I am using 3 main ingredients.

*   A report created in Excel 365
*   Office Scripts to generate the email contents and trigger the mail process
*   Power Automate flow to send the email

Below is a schematic of the whole process.

![](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2545.png)

The Recipe – How to send emails from Excel
------------------------------------------

The actual recipe is a bit detailed and harder to explain in text only format. So I made a video with the whole thing. Watch it here or [on my YouTube channel](https://youtu.be/eeCqaokSSoQ)
. I have included the key steps as text below too.

### Scripts & Instructions:

We can send either _text_ or images as the email. In our case, I have both text content and images. The images come from a grouped object named **_Group 5._**

**GenerateReport Script:**

Go to your “Automate” ribbon in Excel and click on “New Script” button.

![](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2546.png)

In the script window, paste below script and customize the names as needed (refer to the video for explanation on the script).

				
					`function main(workbook: ExcelScript.Workbook):myOutput {     // Your code here     let ws = workbook.getWorksheet("Report");      let repGroup = ws.getShape("Group 5");      const repImage = repGroup.getImageAsBase64(ExcelScript.PictureFormat.png);     const emailSubject = ws.getRange("c2").getText();     const sendTo = ws.getRange("I22").getText();      console.log(emailSubject);     console.log(sendTo);      return {repImage,emailSubject,sendTo};  }  interface myOutput {   repImage: string;   emailSubject: string;   sendTo: string; }`
				
			

Set up the Power Automate Flow
------------------------------

1.  Go to Power Automate website and login with your credentials
2.  Create a new **instant cloud flow**
3.  Set the trigger as “When HTTP request is received”
4.  Add “Run Script” step in Excel
5.  Add Send an email (v2) step
6.  Set up the flow as depicted below.

![Power Automate Flow for Email Sender](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2548.png)

Obtain the Trigger URL
----------------------

1.  Save your flow
2.  Now go back the “trigger” step (step 1 of your flow)
3.  Make sure you set the method to GET
4.  Expand and copy the URL.

![URL for triggering the flow](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2549.png)

Back to Excel to make one more Script
-------------------------------------

We are nearly done. We just need to add one more script & a button in our sales report so that we can initiate the flow from Excel.

Add one more script in Excel and use the below code.

				
					`function main(workbook: ExcelScript.Workbook) {     // Your code here     const triggerURL = "___YOUR TRIGGER URL___";       let request = new XMLHttpRequest();          request.open("GET", triggerURL, false);     request.send(null); }`
				
			

*   Save your script. 
*   From “Code Editor” click on the options menu for your script and use the “Add Button” to add a button on Excel worksheet.
*   Whenever you click on this button, your flow will start.

![Adding a button - Office Script](https://chandoo.org/wp/wp-content/uploads/2023/03/SNAG-2550.png)

Other ways to Automate this:
----------------------------

We can also use VBA to create & send emails automatically. I have previously written about that approach too. [Read this article for VBA Excel Email Sender](https://chandoo.org/wp/send-mails-using-excel-vba-and-outlook/)
.

VBA vs. Office Script approach – which is better?
-------------------------------------------------

Both technologies offer automation. I have summarized the pros & cons of each technology below. 

As of 2023 March, my preference is to use VBA for things like Email automation as it is easy to control and deploy. 

### VBA

**VBA Pros:**

*   Works in any version of Excel
*   Easy to learn, easy to code
*   Lots of help & resources
*   Very old and stable language base
*   Works with Excel, Office & Windows Objects & API

**VBA Cons:**

*   Can't use with Web / Mobile version of Excel
*   Not easy to integrate with Cloud platforms (Power Automate, Sharepoint etc.)
*   Security problems

### Office Script

**Office Script Pros:**

*   Works on Web / Mobile versions too
*   Integrates with cloud platforms (Power Automate etc.)
*   Future ready technology

**Office Script Cons:**

*   No easy help or resources
*   Hard language to learn and master
*   Doesn't work in older versions of Excel
*   Can't use all objects of Excel. Will not work with Windows API etc. too
*   Needs costly subscription plans to use
*   Runs on server, thus no control and susceptible to downtimes etc.

Thanks to Mark Proctor
----------------------

I got the idea for URL trigger [from Mark Proctor](https://exceloffthegrid.com/power-automate-from-excel/)
. Thanks Mark for the fantastic work 🙂

### Got questions?

Do you have any questions reg. this implementation. Post a comment so that our community can help you.

### More automation with Excel

*   [Send Emails from Excel with VBA](https://chandoo.org/wp/send-mails-using-excel-vba-and-outlook/)
    
*   [Create Power Point presentations from Excel](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/)
    
*   [Create Word reports from Excel data](https://chandoo.org/wp/hui%e2%80%99s-excel-report-printer/)
    
*   [More VBA articles & tutorials](https://chandoo.org/wp/category/vba-macros/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [2 Comments](https://chandoo.org/wp/send-email-from-excel-with-office-scripts-power-automate/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/send-email-from-excel-with-office-scripts-power-automate/#respond)
    
*   Tagged under [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [office scripts](https://chandoo.org/wp/tag/office-scripts/)
    , [outlook](https://chandoo.org/wp/tag/outlook/)
    , [power automate](https://chandoo.org/wp/tag/power-automate/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Office Scripts](https://chandoo.org/wp/category/office-scripts/)
    , [Power Automate](https://chandoo.org/wp/category/power-automate/)
    

[PrevPreviousTop AI features in Excel – a round up](https://chandoo.org/wp/top-ai-features-in-excel/)

[NextCreate a beautiful, elegant & interactive to-do list with Excel (FREE Template + Tutorial)Next](https://chandoo.org/wp/beautiful-to-do-list-excel-template/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ