# Loss Reserving Data Pulled from NAIC Schedule P with Additional Accident Years | Casualty Actuarial Society

**Source:** https://www.casact.org/publications-research/research/research-resources/loss-reserving-data-pulled-naic-schedule-p

---

Loss Reserving Data Pulled from NAIC Schedule P with Additional Accident Years
==============================================================================

This page is managed by the CAS Reserve Research Working Group: Current Chair – Chandrakant (“Chandu”) C. Patel, FCAS, MAAA; CAS Staff – Heather Davis, Research Manager; Elizabeth Smith, Director of Publications & Research

Acknowledgement: The CAS would like to thank **S&P Global Market Intelligence** for compiling this data on their behalf. The earlier data sets updated on September 1, 2011 were compiled by Glenn G. Meyers, PhD, FCAS; and Peng Shi, PhD, ASA.

1.  **Purpose**

The goal is to prepare a data set of loss triangles that could be used for claims reserving studies. The data includes major personal and commercial lines of business from U.S. property casualty insurers. The claims data comes from Schedule P – Analysis of Losses and Loss Expenses in the National Association of Insurance Commissioners (NAIC) database.

This data set extends what was compiled previously by an additional 10 accident years.

2.  **Description of Schedule P**

NAIC Schedule P contains information on claims for major personal and commercial lines for all property-casualty insurers that write business in the United States. Some parts have sections that separate occurrence from claims made coverages. The six lines included in this database are: (1) private passenger auto liability/medical; (2) commercial auto/truck liability/medical; (3) workers’ compensation; (4) medical malpractice – claims made; (5) other liability – occurrence; (6) product liability – occurrence.

For each of the above six lines, the variables included in the dataset were pulled from four different parts in Schedule P:

Part 1 - Earned premium and some summary loss data  
Part 2 - Incurred net loss triangles  
Part 3 - Paid net loss triangles  
Part 4 - Bulk and IBNR reserves on net losses and cost containment expenses

The triangles consist of losses net of reinsurance, and quite often insurer groups have mutual reinsurance arrangements between the companies within the group. Consequently, the data focuses on records for single entities in the data preparation, be they insurer groups or true single insurers. The process of data preparation took three steps:

3.  **Data Preparation**
    *   **Step I:** Pull triangle data from Schedule P of year end 2007. Each triangle includes claims of 10 accident years (1998-2007) and 10 development lags.
    *   **Step II:** Square the triangles from Schedule P of year 1998 with outcomes from Schedule P of subsequent years. Specifically, the data for accident year 1998 was pulled from Schedule P of year 2007, the data for accident year 1999 was pulled from Schedule P of year 2008, ……, the data for accident year 2007 was pulled from Schedule P of year 2016. The data in the lower triangles can be used for model validation purposes.
    *   **Step III:** Sampling. We performed preliminary analysis to ensure the quality of the dataset. An insurer  was retained in the final dataset if the following criteria were satisfied: (1) the insurer is available in both Schedule P of year 1997 and subsequent years; (2) the observations (10 accident years and 10 development lags) are complete for the insurer; (3) the claims from Schedule P of year 1997 match those from subsequent years; (4) Net premiums written are not zero for all years. 
4.  **Final Product**

The final product is a data set that contains run-off triangles of six lines of business for all U.S. property casualty insurers. The triangle data correspond to claims of accident year 1998 – 2007 with 10 years development lag. Both upper and lower triangles are included so that one could use the data to develop a model and then test its performance retrospectively. A list of variables in the data is as follows:

**\--------------VARIABLE DESCRIPTION---------------**

GRCODE NAIC company code (including insurer groups and single insurers)  
GRNAME NAIC company name (including insurer groups and single insurers)  
AccidentYear Accident year  
DevelopmentYear Development year  
DevelopmentLag Development year  
IncurLoss\_ Incurred losses and allocated expenses reported at year end  
CumPaidLoss\_ Cumulative paid losses and allocated expenses at year end  
BulkLoss\_ Bulk and IBNR reserves on net losses and defense and cost containment expenses reported at year end  
PostedReserve2007 Posted reserves in year 2007 taken from the Underwriting and Investment Exhibit – Part 2A, including net losses unpaid and unpaid loss adjustment expenses  
EarnedPremDIR\_ Premiums earned at incurral year - direct and assumed  
EarnedPremCeded\_ Premiums earned at incurral year - ceded  
EarnedPremNet\_ Premiums earned at incurral year - net  
Single 1 indicates a single entity, 0 indicates a group insurer

**"\_" REFERS TO LINES OF BUSINESS**

B Private passenger auto liability/medical  
C commercial auto/truck liability/medical  
D Workers' compensation  
F2 Medical malpractice - Claims made  
H1 Other liability - Occurrence  
R1 Products liability - Occurrence

**CURRENT DATA SETS**

[PP Auto Data Set](https://www.casact.org/sites/default/files/2026-03/ppauto_pos98-07%20%281%29.csv)
 (.csv) _(Updated: December 2025)_ 

[Workers Compensation Data Set](https://www.casact.org/sites/default/files/2026-03/wkcomp_pos_98-07.csv)
 (.csv) _(Updated: December 2025_)

[Commercial Auto Data Set](https://www.casact.org/sites/default/files/2026-03/comauto_pos_98-07.csv)
 (.csv) _(Updated: December 2025_)

[Medical Malpractice Data Set](https://www.casact.org/sites/default/files/2026-03/medmal_pos_98-07.csv)
 (.csv) _(Updated: December 2025)_

[Product Liability Data Set](https://www.casact.org/sites/default/files/2026-03/prodliab_pos_98-07.csv)
 (.csv) _(Updated: December 2025)_

[Other Liability Data Set](https://www.casact.org/sites/default/files/2026-03/othliab_pos_98-07.csv)
(.csv) _(Updated: December 2025)_

**EARLIER DATA SETS**

[PP Auto Data Set](https://www.casact.org/sites/default/files/2021-04/ppauto_pos.csv)
 (.csv) _(Updated: September 1, 2011)_

[Workers Compensation Data Set](https://www.casact.org/sites/default/files/2021-04/wkcomp_pos.csv)
 (.csv) _(Updated: September 1, 2011)_

[Commercial Auto Data Set](https://www.casact.org/sites/default/files/2021-04/comauto_pos.csv)
 (.csv) _(Updated: September 1, 2011)_

[Medical Malpractice Data Set](https://www.casact.org/sites/default/files/2021-04/medmal_pos.csv)
 (.csv) _(Updated: September 1, 2011)_

[Product Liability Data Set](https://www.casact.org/sites/default/files/2021-04/prodliab_pos.csv)
 (.csv) _(Updated: September 1, 2011)_

[Other Liability Data Set](https://www.casact.org/sites/default/files/2021-04/othliab_pos.csv)
(.csv) _(Updated: September 1, 2011)_