#!/bin/bash
# Scrape all Tier 1 and Tier 2 financial modelling sites in parallel
cd "/Users/sampi_wu/Downloads/Project Finance Knowledge"

echo "=== Starting all 8 sites in parallel ==="
echo "Dashboard: open scrape_dashboard.html"
echo ""

# Tier 1
# Damodaran - old site, needs seed-based discovery
python3 scrape_site.py damodaran "https://pages.stern.nyu.edu/~adamodar/" "Damodaran" \
  --domain "pages.stern.nyu.edu" \
  --seed-urls "https://pages.stern.nyu.edu/~adamodar/,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/home.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/spreadsh.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valuation/val.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/lectures.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/corpfin.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/invfables.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/equity.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/littlebook.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcasteqspr.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastcfspr.htm,https://pages.stern.nyu.edu/~adamodar/New_Home_Page/webcastvalspr.htm" \
  > .firecrawl/damodaran.log 2>&1 &
echo "Started: Damodaran (PID $!)"

python3 scrape_site.py macabacus "https://macabacus.com" "Macabacus" \
  --include-paths "/learn,/blog,/excel,/category,/operating-model,/valuation,/mergers,/leveraged-buyout,/accounting" \
  > .firecrawl/macabacus.log 2>&1 &
echo "Started: Macabacus (PID $!)"

python3 scrape_site.py cfi "https://corporatefinanceinstitute.com" "CFI" \
  --include-paths "/resources" \
  > .firecrawl/cfi.log 2>&1 &
echo "Started: CFI (PID $!)"

python3 scrape_site.py wallstreetprep "https://www.wallstreetprep.com" "Wall Street Prep" \
  --include-paths "/knowledge" \
  > .firecrawl/wallstreetprep.log 2>&1 &
echo "Started: Wall Street Prep (PID $!)"

# Tier 2
python3 scrape_site.py biws "https://breakingintowallstreet.com" "BIWS" \
  --include-paths "/kb,/biws-financial-modeling" \
  > .firecrawl/biws.log 2>&1 &
echo "Started: BIWS (PID $!)"

python3 scrape_site.py forvismazars "https://financialmodelling.forvismazars.com" "Forvis Mazars" \
  > .firecrawl/forvismazars.log 2>&1 &
echo "Started: Forvis Mazars (PID $!)"

python3 scrape_site.py pivotal180 "https://pivotal180.com" "Pivotal180" \
  --seed-urls "https://pivotal180.com/,https://pivotal180.com/free-resources/,https://pivotal180.com/blog/,https://pivotal180.com/free-resources-project-finance-modeling/" \
  > .firecrawl/pivotal180.log 2>&1 &
echo "Started: Pivotal180 (PID $!)"

python3 scrape_site.py fullstackmodeller "https://www.fullstackmodeller.com" "Full Stack Modeller" \
  > .firecrawl/fullstackmodeller.log 2>&1 &
echo "Started: Full Stack Modeller (PID $!)"

echo ""
echo "All 8 sites launched. Monitoring..."
wait
echo ""
echo "=== ALL DONE ==="
