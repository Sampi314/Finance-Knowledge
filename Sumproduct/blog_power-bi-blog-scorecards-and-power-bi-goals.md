# Power BI Blog: Scorecards and Power BI Goals

**Source:** https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Scorecards and Power BI Goals

*   December 22, 2021

Power BI Blog: Scorecards and Power BI Goals
============================================

Power BI Blog: Scorecards and Power BI Goals
============================================

23 December 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at Scorecards and Power BI Goals._

Integrating Goals and Scorecards is a key aspect of Power BI reporting. A new Scorecard visual has now been added which can be attached to Power BI reports. When included in a report, these visuals let you see the entire Scorecard and even make updates to your Goals.

Goals may also be created from within Power BI Desktop now, streamlining how they are created and managed. The underlying Scorecard added to a report must be added to the Power BI Service, but it’s straightforward to do this from Desktop. The visual supports various formatting options for Scorecards, ranging from font style and colours to backgrounds, so users may modify existing Scorecards.

![](<Base64-Image-Removed>)

**_Goal Level Permissions_**

In many organisations, people in different roles should have access to view and edit specific Goals. For example, it might be only managers should see Goals related to human resources and finances, whereas all employees may view Goals related to operations. In many cases, specific individuals or groups should be the only ones who can edit or update Goals. Using Goal level permissions, these scenarios are easily accomplished.

Goal level permissions let you set specific view and update permissions at the Goal level. Here’s how to get started setting up goal level permissions:

*   ensure you’re in Edit mode for the Scorecard
*   open the Settings pane
*   open the new Permissions tab.

![](<Base64-Image-Removed>)

On the new Permissions tab, you can create roles with different permission and assign specific user groups to those roles. For example, to give a view only experience to the leadership team, simply create a view only role, then assign the security group for my leadership team to that role. Similarly, you may give view and update permissions to individual sales representatives to ensure that they can always keep their Goals up to date.

It should be noted that there are a few different types of permissions:

*   **View permissions:**?let users view specified goals in a Scorecard
*   **Update permissions:?** let users update specific aspects of a Goal.? There are a few options available under update permissions, and you can select any combination of the following:
    *   **Note:** users May add notes in a check-in
    *   **Status:** users may update status in a check-in
    *   **Current Value:** users may update the current value in a check-in.

Additionally, selecting?the ‘Set for all’ option, turns on?inheritance?for all existing and future subgoals under that level. This means future new goals will adopt the permission set you selected.

![](<Base64-Image-Removed>)

Another aspect of Goal level permissions is enabling a “default” permission model that’s applied to anyone accessing the Scorecard.? You may create a role with any combination of permissions you choose, and make that the default permissions, ensuring that any time anyone lands on the Scorecard, they’re seeing exactly what the Scorecard author selects.

![](<Base64-Image-Removed>)

Goal level permissions also apply to the underlying scorecard dataset generated. For example, if you were to give the sales team view access to five Goals on the Scorecard, those are the five goals they will see in the underlying dataset as well. The support for automatic roles based on Goal level permissions (full Row Level Security support) is coming, but this be contained in this Goal level permissions feature.

By enabling Goal level permissions, you ensure that your Scorecard users are accessing only what they should be able to see and updating only what they should be able to update.

**_Power Automate Integration_**

Many organisations want to use Scorecards as part of processes that help them achieve results faster. However, manually monitoring Scorecards may be resource intensive and error prone.

This is where the new Power Automate integration for Power BI Goals comes in. This new capability helps you automate business processes when important changes happen within your Scorecard. It helps you and your colleagues to quickly respond to changing conditions by keeping everyone up to date and taking automated actions to improve outcomes. This new capability is very easy to use because you can launch Power Automate directly from your Scorecard and immediately construct your automated flow.

To do this, Power BI has enabled a set of triggers and actions within Power Automate:

*   Triggers:
    *   when a Goal changes (_e.g_. status, owner)
    *   when someone adds or edits a check-in
    *   when an owner is assigned to a Goal
    *   when a data refresh for a Goal fails
*   Actions:
    *   create a Goal
    *   create a check-in
    *   add a note to a check in
    *   create a Scorecard
    *   update a check-in
    *   update a Goal
    *   get Goal(s)
    *   get Goal check-in(s).

In addition to these actions and triggers, there are also some new templates that will be rolling out within the next few weeks. These templates will allow you to choose a flow that hopefully will align with your more complex business scenarios and ensure that you have the building blocks you need to automate your process. Such templates will include:

*   triggering a teams notification when a status changes to “behind” or “at risk”
*   sending reminders to team members at a specified interval with a link to a Scorecard or specific Goals to review
*   Notifying a specific team member when they are assigned to a new Goal and should perform a check-in
*   Sending a forms survey that gets added as a check-in note on a Goal at a specified interval
*   Sending a congratulations email when a team completes a Goal.

Using Power Automate with your Power BI Goals should help you respond more quickly to changing conditions and to use data to take better actions.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Coming very soon!

**_Moving Goals Around The Scorecard_**

As thing change within your business, so you may require the ability to drag and drop Goals around the Scorecard, making it easier to maintain an accurate view of your company’s priorities and Goal groupings.

To do this, simply click the Goal you want to move and drag it to the specified location. You may reorder Goals within a given family, move Goals entirely to another family, or make any Goal a standalone Goal.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Reordering Goals makes it easier to ensure the right priorities are reflected and your Scorecard order is appropriately modified.

**_Showing / Hiding And Moving Columns_**

Some organisations may use all of the fields Power BI supplies in a Goal, but there are scenarios where not all of the fields provided are applicable. With this release, you have the ability to hide / show columns in the Scorecard. This will allow Scorecard authors to dictate the columns that consumers see, making sure each Scorecard shows only columns that are appropriate to their scenario. Scorecard authors will also be able re-order the columns so that the Scorecard is best suited for their audience.

In Edit mode, simply click the arrow icon next to a column and open column settings. Here, you’ll be able to specify which columns you want to show or hide. You can also drag the column names up or down to reorder them on the Scorecard.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

This makes it easier to tailor the Scorecards to your precise needs.

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/#0)

[](https://sumproduct.com/blog/power-bi-blog-scorecards-and-power-bi-goals/#0 "close")

top