# Suggested Chart for Visualizing the Summary Sources and Uses of Funds in a Project Finance Model – Finexmod

**Source:** https://www.finexmod.com/suchart

---

[Skip to content](https://www.finexmod.com/suchart#content)

Suggested Chart for Visualizing the Summary Sources and Uses of Funds in a Project Finance Model

One of the most important statement in a project finance model is the sources and uses of funds during construction. It is composed of two sections:

**Uses of funds statement** shows the total cost of a project with an explicit and meaningful breakdown of costs. It identifies the total financing required for a project.

**Sources of funds statement** lists the financing facilities that have been identified as available to meet the cost.

The summary sources and uses of funds table appears in most project documents and should also be included in the summary sheet or dashboard within the financial model.

It is also useful to include a chart to visualize the main items in the total project and the financing plan.

I used to include pie charts to visualize the summary S&U in my project finance models but then when you have a relatively detailed line items in the breakdown of costs, then the pie charts becomes difficult to read.

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU01.jpg)

The next best alternative is bar chart. Getting a nice looking chart with descending or ascending order require some work.

Follow the below steps to create a good looking bar chart for your Dashboard.

**Step 1:** List all the sources and uses of funds items and their values in 2 columns next to each other.

![](https://www.finexmod.com/wp-content/uploads/2021/06/SU02.jpg)

**Step 2:** Create a flag to detect the duplicate. The issue with the Rank() function is that if you have 2 cost item with the same exact value then it will rank them the same and only one will appear in the ranking. So before ranking, we want to first identify duplicates and then in the next step multiply by a very small number just to avoid having missing items in our bar chart.

I am using the below function which I am borrowing from Extend Office ([Link](https://www.extendoffice.com/documents/excel/4000-excel-find-duplicates-without-removing.html#a2)
)

\=IF(OR(F21=0;F21=””);;IF(COUNTIF($F$21:F21;F21)>1;1;0)).

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU03.jpg)

**Step 3:** Adjust the duplicate by a small value by multiplying the cost of the duplicate item by a very small value.

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU04.jpg)

**Step 4:** Now rank the adjusted values

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU05.jpg)

**Step 5:** Create a counter in either ascending or descending order

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU06.jpg)

**Step 6:** Look up for cost items to be ranked in either ascending or descending order by using Xlookup() function for both labels and amounts

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU07.jpg)

**Step 7:** Use the filter in Excel to hide the blank and items with 0 value

![Flexible and dynamic chart in Dashboard and a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/SU08.jpg)

I am sure there are multiple ways of doing the same but just wanted to share with you how I visualize the summary sources and uses of funds in my project finance models.

You can download the Excel spreadsheet from the below link:

**[Download Excel File](https://www.eloquens.com/tool/Gvxxcjzz/finexmod/summary-sources-and-uses-chart-in-a-project-finance-model?ref=FinExMod)
**

Now, I would love to hear from you. Let me know in the comment section :

*   Which chart is a great way to visualize the sources and uses of funds in your project finance models?
*   What are the other charts you include in your project finance dashboards or summary sheet?

Until next time, take care and keep modeling.

Best regards,

Hedieh

[](https://www.finexmod.com/suchart#)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-06-15T13:25:52+00:00June 15th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&t=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&text=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/suchart/&title=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&title=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model&summary=One%20of%20the%20most%20important%20statement%20in%20a%20project%20finance%20model%20is%20the%20sources%20and%20uses%20of%20funds%20during%20construction.%20It%20is%20composed%20of%20two%20sections%3A%0AUses%20of%20funds%20statement%20shows%20the%20total%20cost%20of%20a%20project%20with%20an%20explicit%20and%20meaningful%20breakdown%20of%20cost "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&name=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model&description=One%20of%20the%20most%20important%20statement%20in%20a%20project%20finance%20model%20is%20the%20sources%20and%20uses%20of%20funds%20during%20construction.%20It%20is%20composed%20of%20two%20sections%3A%0AUses%20of%20funds%20statement%20shows%20the%20total%20cost%20of%20a%20project%20with%20an%20explicit%20and%20meaningful%20breakdown%20of%20costs.%20It%20identifies%20the%20total%20financing%20required%20for%20a%20project.%0ASources%20of%20funds "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&description=One%20of%20the%20most%20important%20statement%20in%20a%20project%20finance%20model%20is%20the%20sources%20and%20uses%20of%20funds%20during%20construction.%20It%20is%20composed%20of%20two%20sections%3A%0AUses%20of%20funds%20statement%20shows%20the%20total%20cost%20of%20a%20project%20with%20an%20explicit%20and%20meaningful%20breakdown%20of%20costs.%20It%20identifies%20the%20total%20financing%20required%20for%20a%20project.%0ASources%20of%20funds&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F06%2FSU-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fsuchart%2F&title=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model&description=One%20of%20the%20most%20important%20statement%20in%20a%20project%20finance%20model%20is%20the%20sources%20and%20uses%20of%20funds%20during%20construction.%20It%20is%20composed%20of%20two%20sections%3A%0AUses%20of%20funds%20statement%20shows%20the%20total%20cost%20of%20a%20project%20with%20an%20explicit%20and%20meaningful%20breakdown%20of%20costs.%20It%20identifies%20the%20total%20financing%20required%20for%20a%20project.%0ASources%20of%20funds "Vk")
[Email](mailto:?body=https://www.finexmod.com/suchart/&subject=Suggested%20Chart%20for%20Visualizing%20the%20Summary%20Sources%20and%20Uses%20of%20Funds%20in%20a%20Project%20Finance%20Model "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/suchart)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/suchart#)

[Go to Top](https://www.finexmod.com/suchart#)