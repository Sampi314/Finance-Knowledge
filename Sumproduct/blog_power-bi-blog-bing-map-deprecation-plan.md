# Power BI Blog: Bing Map Deprecation Plan

**Source:** https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Bing Map Deprecation Plan

*   November 13, 2025

Power BI Blog: Bing Map Deprecation Plan
========================================

_Welcome back to this week’s edition of the Power BI blog series._  _This week, we revisit Microsoft’s plan to deprecate Bing Maps, and what that means in the world of map visualisations presently._

![](<Base64-Image-Removed>)

To stay ahead of upcoming Microsoft’s plan to retire Bing Maps for Enterprise, Power BI is proactively transitioning from Bing Maps to Azure Maps.  By making this change early, you should benefit from enhanced mapping capabilities and long-term support.  Microsoft is currently encouraging its customers to begin updating their reports to Azure Maps visuals to stay future ready.

**_Power BI Desktop and Web (Edit Mode)_**

Previously, Microsoft has shared its plans to remove the Bing Maps icon from the Visualization pane.  However, they have changed their mind (for the time being) and plan to keep the icon visible for now to ensure continuity and minimise disruption.

Having said that, it should still be noted that the Bing Maps visual is still slated for deprecation, just that the timeline has yet to be agreed.  Any existing Bing Maps already in your reports will still be available.

It is still recommended that in preparation for the upcoming change, you should upgrade to Azure Maps unless:

*   you have team members who would consume the report in China, Korea or government clouds
*   you are physically located in China or Korea (regardless of where your home tenant is located)
*   you are part of a government cloud.

Microsoft is working to support Azure Maps in these unsupported regions.  If you and all your report users are in a supported region, you’re encouraged to start using Azure Maps now.

**_Power BI Report Builder_**

The migration of paginated reports map visuals from Bing Maps to Azure Maps has begun.  This migration will occur in two \[2\] phases:

1.  migration to Azure Maps in PBIRB _then_
2.  migration to Azure Maps for paginated reports in Power BI Service.

The initial phase is now complete.  Beginning with the recent release of PBIRB, users can create map visuals powered by Azure Maps by default.  However, paginated reports published in Power BI Service will continue to use Bing Maps until the second phase is completed.  This is expected to be completed by mid-November.

Paginated reports authors may also revert to Bing Maps for authoring in PBIRB until both phases are complete.  To enable this, users must set the ‘RevertToBingMaps’ registry key located in the ‘**Computer\\HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft Power BI Report Builder**’ folder to one \[1\].  If the ‘**Microsoft Power BI Report Builder**’ folder does not exist, it should be manually created before setting the registry key.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/training)
.  If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
. 

*   [Log in](https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/#0)

[](https://sumproduct.com/blog/power-bi-blog-bing-map-deprecation-plan/#0 "close")

top