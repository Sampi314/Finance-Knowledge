# AI Blog: Excel Agent Mode vs Claude Excel Add-in – Which AI Builds the Better Financial Model?

**Source:** https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/

---

[Home](https://sumproduct.com/)

\> AI Blog: Excel Agent Mode vs Claude Excel Add-in – Which AI Builds the Better Financial Model?

*   January 2, 2026

AI Blog: Excel Agent Mode vs Claude Excel Add-in – Which AI Builds the Better Financial Model?
==============================================================================================

_Welcome back to our AI blog series!  Today we explore a question many financial modellers have been quietly asking for some time: can AI now build a full financial model directly inside Excel?  Both Excel’s new Agent Mode and the Claude Excel Add-in now claim they can create complete three-statement models with valuation from a single natural-language prompt._

![](<Base64-Image-Removed>)

**_The Modelling Brief_**

To test how far this capability has really come, we gave both tools the exact same prompt:

“Build a fully integrated 3-statement model with a complete DCF valuation, clean assumptions, proper working-capital logic and a 10-year forecast.”

You can download the full version of the prompt [here](https://sumproduct.com/wp-content/uploads/2025/12/Prompt.docx)
.

Both tools produced multi-tab Excel workbooks within seconds. Below, we walk through what each tool produced, what worked, what failed and whether either model is ready for real-world financial modelling.

**THE MODEL PRODUCED BY EXCEL AGENT MODE**

Agent Mode generated a simple but functional workbook with three main tabs:

1.  ASSUMPTIONS
2.  CALCULATIONS
3.  DCF VALUATION.

**_1.  Assumptions_**

Agent Mode used inputs that were realistic, coherent and internally consistent:

*   revenue growth tapering from 3% to 15%
*   a logical cost structure with appropriate margins
*   standard working-capital ratios
*   capital expenditure at 5% of revenue
*   straight-line depreciation at 20%
*   a standard 25% corporate tax rate.

Nothing felt extreme or arbitrary.  For a single-prompt model, this was already encouraging.

![](<Base64-Image-Removed>)

**_2.  Core Calculations_**

Agent Mode handled revenue, gross margin, operating expenditure (OPEX) and earnings before interest and tax (EBIT) correctly.  Working capital logic was formulaically sound**.**  So far so good.

However, the property, plant and equipment (PP&E) revealed inconsistencies.  Depreciation and net book value (NBV)were sometimes calculated from revenue and sometimes from existing PP&E balances.  The movement schedule did not consistently follow the standard structure:

**Opening + Capex – Depreciation**

![](<Base64-Image-Removed>)

The sheet worked, but it was not something we would accept in a production-quality model.

**_3.  FCFF and DCF_**

Despite upstream weaknesses, the discounted cash flow (DCF) tab was the strongest part of the workbook. 

The weighted average cost of capital (WACC) was derived using a standard approach and applied consistently throughout the valuation.  Net debt and equity value reconciled cleanly, with no unexplained balancing items.  The WACC–growth sensitivity analysis also worked as expected, with assumption changes flowing through correctly.

![](<Base64-Image-Removed>)

**THE MODEL PRODUCED BY CLAUDE EXCEL ADD-IN**

In Claude’s model, the formatting was neat and inputs were grouped logically.  However, the underlying finance theory told a different story.

![](<Base64-Image-Removed>)

**_1.  Assumptions_**

Although Claude’s inputs were visually well organised, several major issues were noticeable:

*   equity risk premium was set to 120%, not the typical 5% to 6%
*   beta was generated via a formula that did not follow market-standard logic
*   cost of debt was 30%, unrealistic for most corporates
*   WACC was not calculated using the standard approach.

The layout looked professional.  The assumptions did not.

**_2.  Calculations_**

Claude’s income statement, depreciation and working-capital sections were tidy and easy to read. 

The problems were:

*   cash was used as a balancing plug, acceptable in templates but not in valuation
*   changes in working capital and cash from operations referenced incorrect ranges

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

*   capital expenditure was linked to the wrong cells.

![](<Base64-Image-Removed>)

These issues made the resulting cash flow mathematically unreliable.

**_3.  DCF_**

Claude’s DCF tab looked excellent at first glance.  The discounting table was clearly laid out, present-value columns were tidy and easy to follow, and the sensitivity analysis was well styled. 

However, once we traced the numbers back to their source, the problems became clear.  Free cash flow to the firm (FCFF) was already incorrect due to upstream errors in capital expenditure and changes in working capital.  These issues flowed directly into the valuation, meaning that every discounted cash flow was built on flawed inputs.

More importantly, the discounting logic itself was wrong.  Cash flows were discounted using a debt-to-equity ratio rather than the weighted average cost of capital, while the terminal value was discounted using WACC.  This inconsistency breaks the internal logic of the valuation and generates an incorrect equity value.

In short, Claude delivered strong presentation, but the financial logic failed at critical stages where accuracy matters most.

**_Word to the Wise_**

After reviewing both workbooks in detail, the contrast between the two tools became very clear.  AI tools have different personalities when working on financial modelling.

From a structure and readability perspective, Claude performs better.  Its layout is cleaner, inputs are grouped logically and the model is generally more pleasant to audit.  Excel Agent Mode is simple and focuses on functionality.

When it comes to financial-modelling logic, however, Excel Agent Mode is stronger where it truly matters.  WACC is calculated correctly, discounting is applied consistently, free cash flow follows the standard definition and terminal value logic is sound.  Claude’s model, despite its attractive structure, miscalculates several fundamental measures, including WACC and free cash flow, which undermines the entire valuation.

Assumption realism is another clear differentiator.  Agent Mode uses inputs that resemble real-world corporate finance assumptions and stay within reasonable ranges. 

These differences also influence how each tool feels to work with.  Agent Mode behaves like a reliable calculator, but the presentation skills are limited.  Claude behaves more like a junior analyst who is excellent formatting and structure.

For real-world modellers, the implication is clear.  Both tools can accelerate the early stages of model building, but neither can operate autonomously.  Assumptions still need to be reviewed, PP&E and depreciation schedules must be validated, WACC logic requires careful checking and working capital movements often need to be rebuilt.  Free cash flow and discounting should never be accepted without verification.

AI can now build your **first draft**.  We still need to build the **final model**.

_Join us next time for more exciting news of AI tools!_

*   [Log in](https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/#0)
    
*   [Register](https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/#0)

[](https://sumproduct.com/blog/ai-blog-excel-agent-mode-vs-claude-excel-add-in-which-ai-builds-the-better-financial-model/#0 "close")

top