# RetailSalesDemo: PBIP, TMDL, Tabular Editor 3, and Git Best-Practice Guide

> A practical reference for building a small Power BI project as a maintainable software project.

## 1. Project goals

This demo should teach five connected skills:

1. Import and shape CSV data with Power Query.
2. Build a clean star-schema semantic model.
3. Create and organize explicit DAX measures.
4. Manage the model with Power BI Desktop, TMDL, and Tabular Editor 3.
5. Track changes with Git using the PBIP project structure.

The goal is not only to build a working report. The goal is to make the project understandable, testable, and safe to change.

---

## 2. Recommended project structure

```text
RetailSalesDemo/
├── .git/
├── .gitattributes
├── .gitignore
├── README.md
├── RetailSalesDemo.pbip
├── Data/
│   ├── DimCustomer.csv
│   ├── DimDate.csv
│   ├── DimProduct.csv
│   ├── DimRegion.csv
│   └── FactSales.csv
├── RetailSalesDemo.Report/
│   ├── .platform
│   ├── definition.pbir
│   ├── definition/
│   └── StaticResources/
└── RetailSalesDemo.SemanticModel/
    ├── .platform
    ├── definition.pbism
    ├── .pbi/
    └── definition/
        ├── database.tmdl
        ├── model.tmdl
        ├── relationships.tmdl
        ├── cultures/
        └── tables/
            ├── _MEASURES.tmdl
            ├── DimCustomer.tmdl
            ├── DimDate.tmdl
            ├── DimProduct.tmdl
            ├── DimRegion.tmdl
            └── FactSales.tmdl
```

Power BI may omit or generate some files depending on the current project state and enabled features. Do not manually create generated model files merely to match this tree.

### Folder responsibilities

- `Data/`: small source files used by the demo.
- `RetailSalesDemo.SemanticModel/`: model metadata, tables, relationships, measures, and formatting.
- `RetailSalesDemo.Report/`: report pages and visual definitions.
- `RetailSalesDemo.pbip`: project entry point.
- `README.md`: setup instructions, design decisions, and model documentation.

---

## 3. Encoding and line endings

### CSV source files

Save CSV files as UTF-8. In Power Query, select the UTF-8 file origin if Power BI does not detect it correctly.

### PBIP and TMDL files

When externally editing PBIP files, Microsoft specifies UTF-8 **without BOM**. Power BI Desktop uses CRLF line endings. Configure Git to avoid noisy line-ending changes.

Recommended `.gitattributes`:

```gitattributes
* text=auto
*.tmdl text eol=crlf
*.json text eol=crlf
*.pbip text eol=crlf
*.pbir text eol=crlf
*.pbism text eol=crlf
*.csv text eol=crlf
*.md text eol=crlf
```

Set Git's Windows line-ending behavior:

```powershell
git config --global core.autocrlf true
```

---

## 4. Git setup

From the project root:

```powershell
cd C:\Users\frank\Desktop\dt\DAX
git init
git branch -M main
git status
git add .
git commit -m "Initial PBIP retail sales demo"
```

### Recommended `.gitignore`

```gitignore
# Power BI local cache and machine-specific settings
**/.pbi/cache.abf
**/.pbi/localSettings.json

# Optional local editor state
**/.pbi/editorSettings.json

# Temporary and backup files
*.tmp
*.bak
*.autosave
~$*

# Windows and macOS metadata
Thumbs.db
.DS_Store
```

Keep source-controlled model and report definitions such as `.tmdl`, `.pbir`, `.pbism`, `.json`, and `.pbip` files.

### Commit discipline

Make small commits that describe one logical change:

```powershell
git add .
git commit -m "Load retail sales dimension tables"

git add .
git commit -m "Create star schema relationships"

git add .
git commit -m "Add core revenue and profitability measures"

git add .
git commit -m "Build executive summary report page"
```

Before every commit:

```powershell
git status
git diff
git diff --staged
```

Do not commit until Power BI Desktop can reopen the project and the model refresh succeeds.

---

## 5. Data-layer design

Use one row per business transaction in `FactSales`.

### FactSales

Recommended fields:

```text
Date
ProductKey
RegionKey
CustomerKey
Revenue
Cost
UnitsSold
```

Prefer numeric foreign keys in the fact table. Remove duplicate descriptive columns such as product name or region name after the corresponding keys and relationships work.

### DimProduct

```text
ProductKey
ProductName
Category
SubCategory
LaunchYear
Status
```

`ProductKey` must be unique and nonblank.

### DimRegion

```text
RegionKey
RegionName
Country
SalesManager
```

`RegionKey` must be unique and nonblank.

### DimCustomer

```text
CustomerKey
CustomerID
Segment
City
```

`CustomerKey` must be unique and nonblank. Keep `CustomerID` as a readable business identifier.

### DimDate

Recommended fields:

```text
Date
Year
Quarter
YearQuarter
MonthNumber
MonthName
MonthShort
YearMonth
WeekdayNumber
WeekdayName
```

Use columns such as `YearMonth` for labels and a numeric/date-backed column for correct sorting.

---

## 6. Power Query practices

Name queries exactly like their destination model tables:

```text
FactSales
DimProduct
DimRegion
DimCustomer
DimDate
```

For each query:

1. Keep a clearly identifiable `Source` step.
2. Promote headers once.
3. Assign explicit data types.
4. Remove unused columns early.
5. Rename columns consistently.
6. Check for errors, null keys, and duplicates.
7. Keep step names readable.

Example naming:

```text
Source
Promoted Headers
Changed Type
Removed Unused Columns
Added Customer Key
Reordered Columns
```

### Suggested data types

- Keys: whole number
- Dates: date
- Revenue and cost: fixed decimal number or decimal number, chosen consistently
- Units sold: whole number
- Names and categories: text

### Source path caution

A hard-coded path such as `C:\Users\frank\Desktop\dt\DAX\Data` is acceptable for a local learning demo but is machine-specific. Document it in `README.md`. A later improvement is to use a Power Query parameter for the data folder.

---

## 7. Star-schema relationships

Create these relationships:

```text
DimDate[Date]        1 --> * FactSales[Date]
DimProduct[ProductKey] 1 --> * FactSales[ProductKey]
DimRegion[RegionKey]   1 --> * FactSales[RegionKey]
DimCustomer[CustomerKey] 1 --> * FactSales[CustomerKey]
```

Recommended settings:

- Cardinality: one-to-many
- Filter direction: single, from dimension to fact
- Active: yes
- Referential integrity: every fact key should match exactly one dimension row

Avoid bidirectional filtering unless a specific, tested requirement justifies it.

### Model layout

Arrange the Model view as a star:

```text
                DimDate
                   |
DimProduct --- FactSales --- DimRegion
                   |
              DimCustomer
```

---

## 8. Date-table setup

Use one explicit date dimension and mark it as the model's date table using `DimDate[Date]`.

Recommended actions:

- Disable Auto date/time for the project when using a proper date table.
- Ensure `DimDate[Date]` contains unique, contiguous dates.
- Sort `MonthName` by `MonthNumber`.
- Sort `WeekdayName` by `WeekdayNumber`.
- Add a `YearMonth` sort column when required.

Do not use Power BI's generated local date tables as the intended production date dimension.

---

## 9. Naming conventions

Use consistent, readable names.

### Tables

```text
FactSales
DimDate
DimProduct
DimRegion
DimCustomer
_MEASURES
```

### Columns

Use business-friendly names in the model if desired:

```text
Product Key
Product Name
Units Sold
Customer ID
```

Keep `sourceColumn` intact when the model display name differs from the Power Query/source name.

### Measures

Name measures as business concepts, not implementation details:

```text
Total Revenue
Total Cost
Gross Profit
Gross Margin %
Total Units
Customer Count
Revenue per Customer
```

Avoid ambiguous measure names such as `Value`, `Calc1`, or `Sum Revenue`.

---

## 10. Dedicated `_MEASURES` table

For this demo, storing explicit measures in `_MEASURES` is a clean organizational choice.

A calculated measure table can contain a dummy column:

```tmdl
table _MEASURES

    column Value
        summarizeBy: sum
        sourceColumn: [Value]

    partition _MEASURES = calculated
        mode: import
        source = { BLANK() }
```

Hide the dummy `Value` column from report view. Do not delete the table's partition or only column unless you intentionally redesign how the table is materialized.

### Display folders

Suggested folders:

```text
Base Measures
Profitability
Customers
Time Intelligence
Comparisons
Quality Checks
```

A measure's home table can be `_MEASURES`, while display folders organize the field list.

---

## 11. Core DAX measures

Create base measures first:

```DAX
Total Revenue =
SUM ( FactSales[Revenue] )
```

```DAX
Total Cost =
SUM ( FactSales[Cost] )
```

```DAX
Total Units =
SUM ( FactSales[UnitsSold] )
```

```DAX
Gross Profit =
[Total Revenue] - [Total Cost]
```

```DAX
Gross Margin % =
DIVIDE ( [Gross Profit], [Total Revenue] )
```

```DAX
Customer Count =
DISTINCTCOUNT ( FactSales[CustomerKey] )
```

```DAX
Revenue per Customer =
DIVIDE ( [Total Revenue], [Customer Count] )
```

### Time-intelligence measures

After the date table is working:

```DAX
Revenue YTD =
TOTALYTD ( [Total Revenue], DimDate[Date] )
```

```DAX
Revenue Previous Year =
CALCULATE (
    [Total Revenue],
    DATEADD ( DimDate[Date], -1, YEAR )
)
```

```DAX
Revenue YoY Change =
[Total Revenue] - [Revenue Previous Year]
```

```DAX
Revenue YoY % =
DIVIDE ( [Revenue YoY Change], [Revenue Previous Year] )
```

If the mock dataset contains only one year, prior-year measures will be blank. This is expected. Add a second year of data before testing year-over-year behavior.

### Quality-check measures

The deliberately unprofitable rows can support validation measures:

```DAX
Loss-Making Revenue =
CALCULATE (
    [Total Revenue],
    FILTER (
        FactSales,
        FactSales[Revenue] - FactSales[Cost] < 0
    )
)
```

```DAX
Loss-Making Rows =
COUNTROWS (
    FILTER (
        FactSales,
        FactSales[Revenue] - FactSales[Cost] < 0
    )
)
```

Prefer reusable base measures over repeating `SUM(...)` expressions inside many derived measures.

---

## 12. Measure metadata

Every visible production measure should have:

- A clear name
- A meaningful description
- A format string
- A display folder
- An appropriate home table

Suggested formats:

```text
Total Revenue         #,0
Total Cost            #,0
Gross Profit          #,0;(#,0)
Gross Margin %        0.0%
Total Units           #,0
Customer Count        #,0
Revenue per Customer  #,0.00
```

For Norwegian presentation, choose currency/locale formatting intentionally rather than relying on accidental machine defaults.

---

## 13. Column visibility and summarization

Hide technical fields from report consumers:

- Surrogate keys
- Fact foreign keys
- Sort-by columns
- Dummy `_MEASURES[Value]`
- Columns used only internally

Recommended summarization:

- Keys: do not summarize
- Names/categories: do not summarize
- Numeric fact columns: preferably hidden when report authors must use explicit measures
- Measures: use explicit formatting and descriptions

This encourages report visuals to use governed measures instead of implicit aggregations.

---

## 14. Hierarchies

Use only helpful hierarchies.

Examples:

```text
Date Hierarchy
- Year
- Quarter
- MonthName
- Date
```

```text
Product Hierarchy
- Category
- SubCategory
- ProductName
```

Do not create hierarchies merely because columns can be grouped.

---

## 15. Tabular Editor 3 workflow

Recommended workflow:

1. Keep Power BI Desktop open with `RetailSalesDemo.pbip`.
2. Open Tabular Editor 3 from **External Tools**.
3. Create or modify measures in `_MEASURES`.
4. Add descriptions, format strings, display folders, and visibility settings.
5. Save changes in Tabular Editor 3.
6. Return to Power BI Desktop and confirm the changes.
7. Save the PBIP project in Power BI Desktop.
8. Review changed `.tmdl` files with `git diff`.
9. Reopen or refresh the model when necessary and test before committing.

### TMDL editing rule

For early learning, prefer Power BI Desktop or Tabular Editor for structural changes. Read the resulting TMDL diff to learn the format.

When editing PBIP TMDL files externally, save them as UTF-8 without BOM. Microsoft notes that direct external file changes may require Power BI Desktop to reload or restart, whereas TMDL view applies scripts to the currently open semantic model.

### Lineage tags

Do not casually delete or regenerate `lineageTag` values. Treat them as generated object identity metadata unless you have a specific reason and understand the consequences.

---

## 16. Best Practice Analyzer

Run Tabular Editor's Best Practice Analyzer before major commits or releases.

Typical checks should cover:

- Visible technical columns
- Missing descriptions
- Missing measure format strings
- Implicit measures
- Bidirectional relationships
- Invalid DAX expressions
- Unused or duplicate objects

Treat analyzer output as review guidance. Understand each rule before applying bulk fixes.

---

## 17. Report design

Start with one focused page named `Executive Summary`.

### Suggested layout

Top row:

- Total Revenue
- Gross Profit
- Gross Margin %
- Customer Count

Main visuals:

- Line chart: Total Revenue by month
- Bar chart: Total Revenue and Gross Profit by product
- Bar chart: Total Revenue by region
- Table or matrix: Category, product, revenue, cost, profit, margin

Slicers:

- Year
- Region
- Category
- Customer Segment

### Visual practices

- Use explicit measures in values.
- Use dimension columns for axes, legends, rows, columns, and slicers.
- Keep titles business-oriented.
- Apply consistent number formatting.
- Avoid unnecessary colors and visual types.
- Test cross-filtering deliberately.
- Add tooltip content only when it helps interpretation.
- Keep the first demo page simple enough to explain in a few minutes.

---

## 18. Validation checklist

### Data checks

- [ ] Every fact row has a valid date.
- [ ] Every fact key matches one dimension row.
- [ ] Dimension keys are unique and nonblank.
- [ ] Revenue, cost, and units use intended data types.
- [ ] CSV encoding displays all characters correctly.

### Model checks

- [ ] Relationships are one-to-many.
- [ ] Filtering flows from dimensions to the fact table.
- [ ] `DimDate` is marked as the date table.
- [ ] Month and weekday names have correct sort columns.
- [ ] Technical columns are hidden.
- [ ] Auto date/time is disabled when appropriate.

### DAX checks

- [ ] Grand totals match source totals.
- [ ] Product totals reconcile to the grand total.
- [ ] Region totals reconcile to the grand total.
- [ ] Profit equals revenue minus cost.
- [ ] Margin safely handles zero revenue.
- [ ] Empty filter contexts produce sensible blanks or zeros.
- [ ] Time-intelligence measures are tested against suitable dates.

### PBIP and Git checks

- [ ] Power BI Desktop can reopen the PBIP.
- [ ] Refresh completes successfully.
- [ ] `git status` contains no unintended cache files.
- [ ] TMDL diffs correspond to intended model changes.
- [ ] Report JSON changes correspond to intended visual changes.
- [ ] Commit messages describe logical changes.

---

## 19. Recommended build sequence

### Milestone 1: Repository

- Create PBIP project.
- Add `.gitignore` and `.gitattributes`.
- Initialize Git.
- Make the initial commit.

### Milestone 2: Data import

- Load five CSV files.
- Apply data types.
- Validate keys and row counts.
- Commit.

### Milestone 3: Star schema

- Create relationships.
- Mark the date table.
- Hide technical columns.
- Commit.

### Milestone 4: Core measures

- Create `_MEASURES`.
- Add base and derived measures.
- Apply descriptions, formats, and folders.
- Commit.

### Milestone 5: Report page

- Build cards, trends, breakdowns, and slicers.
- Validate interactions.
- Commit.

### Milestone 6: Quality review

- Run Best Practice Analyzer.
- Reconcile totals.
- Reopen the PBIP from disk.
- Review Git diffs.
- Tag a demo release.

```powershell
git tag -a v0.1.0 -m "First working retail sales demo"
git log --oneline --decorate --graph
```

---

## 20. Daily development loop

Use this repeatable loop:

```text
Pull or inspect repository
        ↓
Open RetailSalesDemo.pbip
        ↓
Refresh and confirm baseline
        ↓
Make one logical change
        ↓
Save in Tabular Editor and Power BI Desktop
        ↓
Refresh and test
        ↓
Inspect git status and git diff
        ↓
Commit with a focused message
```

Useful commands:

```powershell
git status
git diff
git diff --stat
git add .
git diff --staged
git commit -m "Describe the logical change"
```

---

## 21. Common mistakes to avoid

- Editing the `.pbix` and PBIP versions independently.
- Committing `cache.abf` or machine-specific local settings.
- Using many-to-many or bidirectional relationships by default.
- Keeping product, region, and customer descriptions in the fact table after proper dimensions exist.
- Using raw numeric columns directly in report visuals instead of explicit measures.
- Creating time-intelligence measures before confirming the date table and relationships.
- Deleting lineage tags without understanding object identity.
- Manually editing TMDL while Power BI Desktop has stale model state.
- Making model, data, and report redesigns in one giant commit.
- Assuming a successful file save proves the model refreshes and calculations are correct.
- Using long object and folder names that risk exceeding Windows path limits.
- Saving the active PBIP directly into locations where file synchronization can interfere with Power BI Desktop saves.

---

## 22. Definition of done for the demo

The demo is complete when:

1. `RetailSalesDemo.pbip` opens successfully.
2. All CSV queries refresh successfully.
3. The semantic model is a clean star schema.
4. `DimDate` is configured correctly.
5. Measures are organized and formatted in `_MEASURES`.
6. Technical fields are hidden.
7. One report page answers basic revenue, profit, customer, product, regional, and time questions.
8. Totals reconcile with the source data.
9. Best Practice Analyzer has been reviewed.
10. Git tracks only intentional project artifacts.
11. The repository has small, understandable commits.
12. A fresh reopen and refresh succeeds before the release tag.

---

## 23. Further learning path

After the base demo works, add features one at a time:

1. A second year of fact data for year-over-year analysis.
2. Calculation groups for time intelligence.
3. Dynamic format strings.
4. Field parameters.
5. Row-level security.
6. DAX query-based regression checks.
7. Automated model and report quality checks.
8. A CI/CD deployment pipeline.

Do not add these until the base star schema, explicit measures, and Git workflow are reliable.

---

## 24. Official references

- [Power BI Desktop projects (PBIP)](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-overview)
- [Power BI Desktop semantic model project folder and TMDL format](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset)
- [Use TMDL view in Power BI Desktop](https://learn.microsoft.com/en-us/power-bi/transform-model/desktop-tmdl-view)
- [Power BI implementation planning: Develop content and manage changes](https://learn.microsoft.com/en-us/power-bi/guidance/powerbi-implementation-planning-content-lifecycle-management-develop-manage)

---

## Quick reference

```text
Source layer:      CSV files in Data/
Transform layer:   Power Query
Model structure:   Star schema
Fact table:        FactSales
Dimensions:        DimDate, DimProduct, DimRegion, DimCustomer
Measures:          _MEASURES
Model source:      TMDL
Report source:     PBIR/JSON
Model editor:      Power BI Desktop + Tabular Editor 3
Version control:   Git
Validation:        Refresh + reconciliation + BPA + reopen test
```
