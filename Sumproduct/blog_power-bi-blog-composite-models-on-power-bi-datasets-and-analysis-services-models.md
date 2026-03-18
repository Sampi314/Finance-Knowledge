# Power BI Blog: Composite Models on Power BI Datasets and Analysis Services Models

**Source:** https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Composite Models on Power BI Datasets and Analysis Services Models

*   June 21, 2023

Power BI Blog: Composite Models on Power BI Datasets and Analysis Services Models
=================================================================================

Power BI Blog: Composite Models on Power BI Datasets and Analysis Services Models
=================================================================================

22 June 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we discuss composite models._

In December 2020, Power BI launched the Preview of DirectQuery for Power BI Datasets and Analysis Services. Since then, Microsoft has been working on improving this feature to get it ready for General Availability. There were various improvements made, such as:

*   support for SQL Server Analysis Services Tabular models (version 2022 required)
*   ensured display folders, sort by column properties and format strings persist
*   introduced sub setting and the ability to connect to perspectives
*   users may now view a report built using this feature with Read permissions / Viewer role instead of Build permission / Contributor role.

Models built using this feature are referred to as **composite models**. Originally known as “DirectQuery for Power BI Datasets and Analysis Services”, this name is now superseded as it has served its purpose during the Preview period to be able to clearly identify that this was a Preview feature.

This update acknowledges the end of the Preview period: composite models based upon Power BI datasets and Analysis Services Tabular models are now Generally Available and fully supported on Premium, PPU and new Pro workspaces.

Microsoft will announce General Availability for existing Pro workspaces later as the Power BI team finish the backend changes required. It should be noted that as these back-end changes are happening, users might no longer need Build permissions to view a report built using this feature, but instead they can rely on just Read permissions. When this happens, you can safely take away the Build permissions for your consumers.

If you are currently using Pro workspaces and want to switch over to the Read permission model right away, you can. However, it requires you to create new workspaces and host the datasets and reports there. As a reminder, going forward you will need to enable the ‘Allow XMLA endpoints and Analyze in Excel with on-premises datasets’ setting enabled in your tenant to use this feature.

Furthermore, when the Preview began, any consumer of a report that leveraged a composite model based upon a Power BI dataset was required to have Build permissions or the Contributor role. Since then, Power BI has changed this for Premium and PPU workspaces: readers of reports based upon datasets in Premium or PPU workspaces just require Read permissions (or the Viewer role).

However, for most Pro workspaces Build permissions are still required in the scenario above. As mentioned above, Microsoft is still making backend changes to align the Pro workspaces with the Premium and PPU workspaces so everyone consuming these reports will just require Read permission or the Viewer role, regardless of the workspace type the data is stored in. Apparently, these changes are still underway and are taking longer than expected!

This does have an impact for us end users:

*   if you only use Premium / PPU workspaces, Read permission is required to view a report
*   if you use a mixture of Premium / PPU and Pro workspaces or use Pro workspace exclusively, some of your reports might currently only require Read permissions while others will still require Build. The ratio of these will shift over time to the vast majority just requiring Read as Microsoft completes the backend changes
*   if you currently use Pro workspaces, some datasets will not benefit from the backend changes and will still require Build permissions, even after the back-end changes are completed. This includes datasets that:

*   *   use one or more unsupported sources _and / or_
    *   consume a large amount of memory, which is true for about 0.03% of all datasets.

Microsoft has stated it has seen numerous users making DirectQuery connections to unsupported sources, such as usage metrics and real-time data sets. Whilst during the Preview you might not have received an error when using these sources, you will start seeing an error going forward as “loose ends are tightened”. Even if you do not see an error, you should still use this feature with supported sources. The unsupported sources are documented, so please make sure you use supported sources for your reports that rely on this feature now or trouble may be finding you out in the very near future…

![](<Base64-Image-Removed>)

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
 . If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/#0)

[](https://sumproduct.com/blog/power-bi-blog-composite-models-on-power-bi-datasets-and-analysis-services-models/#0 "close")

top