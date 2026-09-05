import json
import os

BASE_DIR = r"C:\Users\frank\Desktop\dt\DAX\RetailSalesDemo.Report\definition\pages"
PAGES_JSON_PATH = os.path.join(BASE_DIR, "pages.json")

# Complete Storytelling with Data (SWD) configuration for all 60 charts
# Format: (idx, page_title, visual_type, cat_entity, cat_prop, val_entity, val_prop, ser_entity, ser_prop, extra_arg, visual_objects, action_title, action_subtitle)
SWD_CHARTS = [
    # 01-10 Line Fundamentals & Variations
    (1, "Discrete Line Chart", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, 
     {"categoryAxis": [{"properties": {"axisType": {"expr": {"Literal": {"Value": "'Categorical'"}}}}}]},
     "Monthly Sales Accelerate Across Q1 2023",
     "Discrete monthly view reveals February revenue surging to $10.8K (58% of Q1 total)"),
    
    (2, "Continuous Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"categoryAxis": [{"properties": {"axisType": {"expr": {"Literal": {"Value": "'Scalar'"}}}}}]},
     "Order Velocity Escalates Significantly from Mid-January",
     "Continuous chronological axis tracks 23 transactions scaling from $594 to peak $1,720 order"),
    
    (3, "Line Chart with Markers", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "5L"}}}}}]},
     "Individual Order Milestones Isolate Discrete Enterprise Deals",
     "Markers pinpoint transaction events, showing high activity between Feb 9 and Feb 25"),
    
    (4, "Line Chart with Circle Markers", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerShape": {"expr": {"Literal": {"Value": "'circle'"}}}, "markerSize": {"expr": {"Literal": {"Value": "9L"}}}}}]},
     "Volume Surge in February Reaches 1,468 Units Sold",
     "Enlarged circle markers highlight major monthly consolidation in sales volume"),
    
    (5, "Dashed Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dashed'"}}}}}]},
     "Mid-Week Purchasing Cadence Across Business Accounts",
     "Dashed stroke distinguishes cyclic B2B purchasing patterns throughout the quarter"),
    
    (6, "Dotted Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dotted'"}}}}}]},
     "Secondary Trajectory: Granular Daily Revenue Monitoring",
     "Dotted formatting reduces visual weight, keeping focus on overall trend trajectory"),
    
    (7, "Stepped Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"stepped": {"expr": {"Literal": {"Value": "true"}}}}}]},
     "Step-Level Cumulative Capacity Shifts by Transaction",
     "Stepped interpolation highlights discrete transactional shifts without artificial linear smoothing"),
    
    (8, "Line Chart Multiple Dimensions", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimRegion", "RegionName", None, None,
     "South Territory Dominates Revenue Delivery ($8.6K Total)",
     "Regional breakdown shows South (Sarah Olsen) maintaining steady lead over North ($6.1K)"),
    
    (9, "Line Chart Multiple Measures", "lineChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Cost", "Total Profit"], None, None, None, None,
     "Revenue Growth Consistently Outpaces Operating Costs",
     "Simultaneous multi-measure tracking: $18.8K Revenue vs $13.5K Cost yielding $5.2K Net Profit"),
    
    (10, "Line Chart Ends of Line Labels", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"labels": [{"properties": {"show": {"expr": {"Literal": {"Value": "true"}}}}}]},
     "Initial vs. Latest Order Trajectory: $594 to $1,610",
     "Direct end labels eliminate visual search, grounding the growth narrative from start to finish"),

    # 11-18 Moving Averages & Area Variations
    (11, "Moving Average", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue 30D Moving Avg", None, None, None, None,
     "30-Day Moving Average Confirms Upward Commercial Trend",
     "Rolling monthly average dampens transactional volatility to expose genuine commercial expansion"),
    
    (12, "Area Chart", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, None,
     "Commercial Mass: $18,758 Total Revenue Realized in Q1",
     "Area fill visually communicates the economic volume accumulated over the operational period"),
    
    (13, "Area Chart + Line Chart", "areaChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Profit"], None, None, None, None,
     "Profitability Margin Buffer: $5,247 Net Profit Protected",
     "Filled revenue area cushions against operating costs, with profit boundary tracking above zero"),
    
    (14, "Area Chart + Dashed Line", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dashed'"}}}}}]},
     "Target Boundary Area: Dashed Ceiling Tracks Run-Rate",
     "Dashed upper contour defines revenue threshold against budgeted commercial benchmarks"),
    
    (15, "Area Chart + Dotted Line", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dotted'"}}}}}]},
     "Subdued Capacity Envelope for Secondary Forecasting",
     "Dotted perimeter provides high data-ink boundary definition on historical sales volumes"),
    
    (16, "Stacked Area Chart", "stackedAreaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Business Category Expands to 59.8% of Revenue Composition",
     "Stacked area illustrates Business category ($11.2K) outpacing Consumer ($7.5K) across Q1"),
    
    (17, "% of Total Area Chart", "hundredPercentStackedAreaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "B2B Category Mix Scales from 44% in January to 65% in March",
     "100% normalized area chart confirms strategic mix shift toward higher-margin Business products"),
    
    (18, "Line Chart + Moving Avg", "lineChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Revenue 30D Moving Avg"], None, None, None, None,
     "Actual Transaction Spikes vs. Stabilized 30-Day Mean",
     "Contrasting volatile single-order peaks ($1.7K) against the steady, upward 30-day trendline"),

    # 19-25 Variances & Running Totals
    (19, "Difference from Previous", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Revenue MoM Variance", None, None, None, None,
     "February Generates +$4,654 Net Expansion over January",
     "Variance columns isolate seasonal acceleration from routine month-over-month sales flow"),
    
    (20, "% Difference from Previous", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue MoM %", None, None, None, None,
     "75.8% Growth Surge Highlights Peak Q1 Commercial Momentum",
     "Month-over-month relative change curve benchmarks growth velocity across fiscal periods"),
    
    (21, "Difference vs. First", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Difference vs First", "DimRegion", "RegionName", None, None,
     "South and North Deliver Sustained Gains Over Day-1 Baseline",
     "Regional divergence from initial transaction baseline highlights territory scaling efficiency"),
    
    (22, "% Difference vs. First", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue % Difference vs First", "DimRegion", "RegionName", None, None,
     "Relative Growth Index: South Outpaces Starting Pace by 172%",
     "Normalized indexed expansion benchmarks all four territories against their respective start points"),
    
    (23, "Running Total", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Running Total", None, None, None, None,
     "Cumulative Sales Crosses $18.8K Revenue Milestone",
     "Smooth running total line tracks continuous financial accumulation toward annual targets"),
    
    (24, "Running Total Area Chart", "areaChart", "DimDate", "Date", "_MEASURES", ["Revenue Running Total", "Cost Running Total"], None, None, None, None,
     "The Project Controlling S-Curve: Earned Revenue vs. Cost",
     "Tufte-aligned cumulative S-Curve demonstrates positive margin gap widening to $5,247"),
    
    (25, "Running Total from 1st Sale", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Running Total", "DimRegion", "RegionName", None, None,
     "Territory Accumulation Curves: South Leads from Start to Finish",
     "Cumulative trajectory by region highlights South generating $8.6K ahead of North ($6.1K)"),

    # 26-35 Bars, Columns & Dual Axis Combos
    (26, "Bar Chart", "clusteredBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, None,
     "February Established as Prime Commercial Quarter Month ($10.8K)",
     "Horizontal bar layout ensures immediate readability and clean categorical comparisons"),
    
    (27, "Stacked Bar Chart", "stackedBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Category Revenue Contributions Across Successive Months",
     "Stacked bars reveal Business category generating the majority of February's $10.8K record"),
    
    (28, "% of Total Stacked Bars", "hundredPercentStackedBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Proportional Share Shift: Business Grows from 44% to 65%",
     "100% stacked format highlights product portfolio mix transition toward enterprise offerings"),
    
    (29, "Paired Column Chart", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None,
     "Monthly Gross Margin Expands from 21.3% (Jan) to 30.3% (Feb)",
     "Paired column comparison confirms operating profitability scaling alongside revenue growth"),
    
    (30, "Column Chart", "stackedColumnChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Monthly Sales Volume by Product Category",
     "Vertical column stack visualizes the doubling of sales from January ($6.1K) to February ($10.8K)"),
    
    (31, "Lollipop Chart", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"dataPoint": [{"properties": {"showAllDataPoints": {"expr": {"Literal": {"Value": "true"}}}}}]},
     "Lollipop Focus: Highlighting Peak Deal Value Outliers",
     "Minimalist stems and heads emphasize transactions exceeding the $1,500 threshold"),
    
    (32, "Bar-in-Bar Chart", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None,
     "Cost Envelope Contained Well Within Realized Revenue",
     "Direct visual nesting contrasts operating expenditure directly against top-line revenue"),
    
    (33, "Bar Chart w/ Reference Line", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, None,
     "February Outperforms Monthly Sales Benchmark by +70%",
     "Clear benchmark reference establishes February as the standout commercial performance month"),
    
    (34, "Dual Axis w/ Different Measures", "lineClusteredColumnComboChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, "Profit Margin %", None,
     "Volume & Margin Alignment: High Revenue Protects Healthy Margin",
     "Bars represent Total Revenue ($) while secondary line tracks Profit Margin % (peaking at 43.9%)"),
    
    (35, "Dual Axis w/ Related Measures", "lineClusteredColumnComboChart", "DimDate", "Date", "_MEASURES", "Total Cost", None, None, "Total Revenue", None,
     "Revenue Trajectory Consistently Surpasses Cost Baseline",
     "Synchronized dual axis pairs Cost (bars) with Revenue (line) to track profitability spread"),

    # 36-43 Averages, Cycles, Slopes & Butterflies
    (36, "Variance to Overall Average", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Revenue Variance to Overall Avg", None, None, None, None,
     "February Revenue Surpasses Overall Mean by +$4,540",
     "Variance columns identify days generating significant commercial over-performance"),
    
    (37, "Variance to Pane Average", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", "Revenue Variance to Overall Avg", None, None, None, None,
     "Monthly Variance Profile Highlights February Growth Driver",
     "Positive deviation in February (+4.5K) contrasts with January (-113) and March run-rate"),
    
    (38, "Cycle Plot", "lineChart", "DimDate", "Weekday", "_MEASURES", "Total Revenue", "DimDate", "Month", None, None,
     "Friday and Tuesday Emerge as Primary Deal Closing Days",
     "Decomposed weekly cycles identify weekday closing rhythms across consecutive months"),
    
    (39, "Single Month Calendar", "pivotTable", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimDate", "Weekday", None, None,
     "February Sales Calendar: Peak Activity Concentrated in Weeks 2 & 3",
     "Matrix calendar heatmap highlights specific days driving 70% of monthly deal volume"),
    
    (40, "Discrete Slope Graph", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Product Category Trajectories: Business Scales Upward",
     "Slope graph isolates category trajectory angles, highlighting Business category steep ascent"),
    
    (41, "Continuous Slope Graph", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimRegion", "RegionName", None, None,
     "Regional Slope Divergence: South Outpaces Northern Trajectory",
     "Continuous slopes trace territory performance from early-year baseline to Q1 close"),
    
    (42, "Butterfly Chart Single Axis", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Negative Cost"], None, None, None, None,
     "Bilateral Cash Flow: Inflows (Revenue) vs. Outflows (Cost)",
     "Symmetrical diverging bars contrast top-line cash generation against operational cost outflow"),
    
    (43, "Butterfly Chart Dual Axis", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None,
     "Cost Recovery Balance Across Operating Months",
     "Dual-axis butterfly evaluates gross margin health and working capital recovery"),

    # 44-51 Dot Plots, Barcodes & Sparklines
    (44, "Dot Plot", "scatterChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, None,
     "Order Value Dispersion: Concentration in the $1,000–$1,700 Tier",
     "Dot plot reveals clustering of enterprise transactions above the $1,000 threshold"),
    
    (45, "Barcode Chart", "clusteredBarChart", "FactSales", "SalesKey", "_MEASURES", "Total Revenue", None, None, None, None,
     "Transaction Density Sequence: Accelerated Velocity in February",
     "High-density barcode strips track closing tempo across the 23 transactional events"),
    
    (46, "Sparklines", "tableEx", "DimProduct", "ProductName", "_MEASURES", ["Total Revenue", "Total Profit", "Total Units"], None, None, None, None,
     "Product Portfolio Scorecard: Product C Leads Profit Generation",
     "Tabular ledger shows Product C generating $3,186 in profit (42.8% margin) on 229 units"),
    
    (47, "Sparkbars", "tableEx", "DimRegion", "RegionName", "_MEASURES", ["Total Revenue", "Total Cost", "Total Units"], None, None, None, None,
     "Territory Efficiency Scorecard: South Delivers $3,105 Profit",
     "Regional ledger highlights South's 36.0% profit margin and superior unit throughput (870 units)"),
    
    (48, "Spark Area Chart", "tableEx", "DimProduct", "Category", "_MEASURES", ["Total Revenue", "Total Profit", "Profit Margin %"], None, None, None, None,
     "Category Margin Health: Business & Consumer Post >42% Margins",
     "Category scorecard contrasts core commercial health against prototype experimental costs"),
    
    (49, "Connected Dot Plot", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None,
     {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "6L"}}}}}]},
     "Sequential Transaction Pipeline Progression",
     "Connected markers show steady progression from smaller trial deals to major enterprise accounts"),
    
    (50, "Enclosed Dot Plot", "scatterChart", "_MEASURES", "Total Cost", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None,
     "Cost-to-Revenue Efficiency Envelope by Product Category",
     "Scatter coordinates reveal high revenue-to-cost return in Business and Consumer categories"),
    
    (51, "Circle Timeline", "scatterChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, "Total Units", None,
     "Deal Sizing Timeline: Revenue vs. Unit Volume Sizing",
     "Bubble size reflects units sold while vertical height reflects deal revenue over time"),

    # 52-60 Rankings, Trajectories, Bridges & Stock
    (52, "Bump Chart", "lineChart", "DimDate", "Month", "_MEASURES", "Product Rank", "DimProduct", "ProductName", None, None,
     "Product Ranking Dynamics: Product C Secures #1 Revenue Rank",
     "Rank trajectory tracks Product C overtaking Product B to become the company's leading SKU"),
    
    (53, "Seismogram", "clusteredBarChart", "DimDate", "Date", "_MEASURES", "Revenue MoM Variance", None, None, None, None,
     "Day-to-Day Transactional Volatility & Seismic Momentum",
     "Seismic bars highlight peak positive volatility clusters during mid-February commercial cycle"),
    
    (54, "Parallel Coordinates", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "ProductName", None, None,
     "SKU Performance Profiles Traced Across Time Horizons",
     "Parallel line trajectories illustrate distinct product lifecycle paths across Q1"),
    
    (55, "Small Multiple Donut Charts", "donutChart", "DimProduct", "Category", "_MEASURES", "Total Revenue", None, None, None, None,
     "Category Market Share Mix: Business Expands to 65% Share",
     "Donut multiples visualize the steady quarterly transition toward enterprise B2B sales"),
    
    (56, "Connected Scatterplot", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None,
     "Revenue-Profit Trajectory: Simultaneous Scale and Margin Expansion",
     "Chronological path moves upward and to the right, reflecting healthy operational leverage"),
    
    (57, "Connected Scatterplot Dotted Lines", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None,
     "Dotted Efficiency Path: Tracing Enterprise Deal Trajectory",
     "Dotted trajectory connectors emphasize sequential progression across commercial stages"),
    
    (58, "Animated Connected Scatterplot", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None,
     "Dynamic Timeline Trajectory: Monitoring Value Creation Over Time",
     "Chronological coordinates map the expanding profit envelope as revenue scales to $18.8K"),
    
    (59, "Waterfall Chart", "waterfallChart", "DimDate", "Date", "_MEASURES", "Total Profit", None, None, None, None,
     "Step-by-Step Profit Contribution Bridge ($5,247 Total Net Profit)",
     "Sequential waterfall illustrates positive order increments and isolates prototype loss impact"),
    
    (60, "Stock Chart", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None,
     "Operational Spread: Revenue vs. Cost Range Brackets by Date",
     "High-low brackets monitor the gross spread between realized revenue and incurred costs")
]

def make_field_col(entity, prop):
    return {
        "field": {
            "Column": {
                "Expression": {"SourceRef": {"Entity": entity}},
                "Property": prop
            }
        },
        "queryRef": f"{entity}.{prop}",
        "nativeQueryRef": prop,
        "active": True
    }

def make_field_measure(entity, prop):
    return {
        "field": {
            "Measure": {
                "Expression": {"SourceRef": {"Entity": entity}},
                "Property": prop
            }
        },
        "queryRef": f"{entity}.{prop}",
        "nativeQueryRef": prop
    }

def make_kpi_card_visual():
    measures = ["Total Revenue", "Total Cost", "Total Profit", "Profit Margin %", "Total Units"]
    projections = [make_field_measure("_MEASURES", m) for m in measures]
    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.12.0/schema.json",
        "name": "kpi_ribbon",
        "position": {"x": 24, "y": 24, "z": 0, "height": 110, "width": 1872, "tabOrder": 0},
        "visual": {
            "visualType": "cardVisual",
            "query": {
                "queryState": {
                    "Data": {"projections": projections}
                }
            },
            "objects": {
                "value": [{"properties": {"show": {"expr": {"Literal": {"Value": "true"}}}}}]
            },
            "drillFilterOtherVisuals": True
        }
    }

def make_main_visual(chart_tuple):
    idx, title, vtype, cat_entity, cat_prop, val_entity, val_prop, ser_entity, ser_prop, extra_arg, visual_objects, action_title, action_subtitle = chart_tuple

    # 1. Table / Matrix
    if vtype == "tableEx":
        projections = [make_field_col(cat_entity, cat_prop)]
        if isinstance(val_prop, list):
            for p in val_prop:
                projections.append(make_field_measure(val_entity, p))
        else:
            projections.append(make_field_measure(val_entity, val_prop))
        query_state = {"Values": {"projections": projections}}
        sort_def = {
            "sort": [{"field": {"Measure": {"Expression": {"SourceRef": {"Entity": "_MEASURES"}}, "Property": "Total Revenue"}}, "direction": "Descending"}],
            "isDefaultSort": True
        }
    elif vtype == "pivotTable":
        # Matrix visual for Calendar
        query_state = {
            "Rows": {"projections": [make_field_col(cat_entity, cat_prop)]},
            "Columns": {"projections": [make_field_col(ser_entity, ser_prop)]},
            "Values": {"projections": [make_field_measure(val_entity, val_prop)]}
        }
        sort_def = None
    elif vtype == "donutChart":
        query_state = {
            "Category": {"projections": [make_field_col(cat_entity, cat_prop)]},
            "Y": {"projections": [make_field_measure(val_entity, val_prop)]}
        }
        sort_def = {
            "sort": [{"field": {"Measure": {"Expression": {"SourceRef": {"Entity": val_entity}}, "Property": val_prop}}, "direction": "Descending"}],
            "isDefaultSort": True
        }
    elif vtype == "scatterChart":
        x_proj = make_field_measure(cat_entity, cat_prop) if cat_entity == "_MEASURES" else make_field_col(cat_entity, cat_prop)
        y_proj = make_field_measure(val_entity, val_prop) if val_entity == "_MEASURES" else make_field_col(val_entity, val_prop)
        query_state = {
            "X": {"projections": [x_proj]},
            "Y": {"projections": [y_proj]}
        }
        if ser_entity and ser_prop:
            query_state["Details"] = {"projections": [make_field_col(ser_entity, ser_prop)]}
        if extra_arg:
            query_state["Size"] = {"projections": [make_field_measure("_MEASURES", extra_arg)]}
        sort_def = None
    elif vtype == "waterfallChart":
        query_state = {
            "Category": {"projections": [make_field_col(cat_entity, cat_prop)]},
            "Y": {"projections": [make_field_measure(val_entity, val_prop)]}
        }
        sort_def = {
            "sort": [{"field": {"Column": {"Expression": {"SourceRef": {"Entity": cat_entity}}, "Property": cat_prop}}, "direction": "Ascending"}],
            "isDefaultSort": True
        }
    elif vtype in ("lineClusteredColumnComboChart", "lineStackedColumnComboChart"):
        query_state = {
            "Category": {"projections": [make_field_col(cat_entity, cat_prop)]},
            "Y": {"projections": [make_field_measure(val_entity, val_prop)]},
            "Y2": {"projections": [make_field_measure("_MEASURES", extra_arg)]}
        }
        sort_def = {
            "sort": [{"field": {"Column": {"Expression": {"SourceRef": {"Entity": cat_entity}}, "Property": cat_prop}}, "direction": "Ascending"}],
            "isDefaultSort": True
        }
    else:
        # Standard lineChart, areaChart, stackedAreaChart, hundredPercentStackedAreaChart,
        # clusteredColumnChart, stackedColumnChart, hundredPercentStackedColumnChart,
        # clusteredBarChart, stackedBarChart, hundredPercentStackedBarChart
        query_state = {
            "Category": {"projections": [make_field_col(cat_entity, cat_prop)]}
        }
        if isinstance(val_prop, list):
            y_proj = [make_field_measure(val_entity, p) for p in val_prop]
        else:
            y_proj = [make_field_measure(val_entity, val_prop)]
        query_state["Y"] = {"projections": y_proj}

        if ser_entity and ser_prop:
            query_state["Series"] = {"projections": [make_field_col(ser_entity, ser_prop)]}

        sort_col = "Date" if cat_prop == "Date" else cat_prop
        sort_def = {
            "sort": [{"field": {"Column": {"Expression": {"SourceRef": {"Entity": cat_entity}}, "Property": sort_col}}, "direction": "Ascending"}],
            "isDefaultSort": True
        }

    # Build objects with Storytelling with Data Title & Subtitle + visual styling
    objects_dict = {}
    if visual_objects:
        objects_dict.update(visual_objects)
    
    # Storytelling with Data Titles
    objects_dict["title"] = [
        {
            "properties": {
                "show": {"expr": {"Literal": {"Value": "true"}}},
                "text": {"expr": {"Literal": {"Value": f"'{action_title}'"}}},
                "fontColor": {"solid": {"color": "#1E293B"}}
            }
        }
    ]
    objects_dict["subTitle"] = [
        {
            "properties": {
                "show": {"expr": {"Literal": {"Value": "true"}}},
                "text": {"expr": {"Literal": {"Value": f"'{action_subtitle}'"}}},
                "fontColor": {"solid": {"color": "#64748B"}}
            }
        }
    ]

    visual_obj = {
        "visualType": vtype,
        "query": {"queryState": query_state},
        "objects": objects_dict
    }
    if sort_def:
        visual_obj["query"]["sortDefinition"] = sort_def
    visual_obj["drillFilterOtherVisuals"] = True

    return {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.12.0/schema.json",
        "name": f"chart_vis_{idx:02d}",
        "position": {"x": 24, "y": 150, "z": 1, "height": 906, "width": 1872, "tabOrder": 1},
        "visual": visual_obj
    }

def main():
    with open(PAGES_JSON_PATH, "r", encoding="utf-8") as f:
        pages_data = json.load(f)

    existing_order = pages_data.get("pageOrder", [])
    base_pages = [p for p in existing_order if not p.startswith("ts_p")]
    new_page_order = list(base_pages)

    for cfg in SWD_CHARTS:
        idx, title = cfg[0], cfg[1]
        page_id = f"ts_p{idx:02d}"
        page_display_name = f"{idx:02d} {title}"
        new_page_order.append(page_id)

        page_dir = os.path.join(BASE_DIR, page_id)
        os.makedirs(page_dir, exist_ok=True)

        # 1. page.json
        page_json_content = {
            "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.1.0/schema.json",
            "name": page_id,
            "displayName": page_display_name,
            "displayOption": "FitToPage",
            "height": 1080,
            "width": 1920
        }
        with open(os.path.join(page_dir, "page.json"), "w", encoding="utf-8") as f:
            json.dump(page_json_content, f, indent=2)

        # 2. Visuals
        visuals_dir = os.path.join(page_dir, "visuals")
        os.makedirs(visuals_dir, exist_ok=True)

        # KPI Ribbon Visual
        kpi_dir = os.path.join(visuals_dir, "kpi_ribbon")
        os.makedirs(kpi_dir, exist_ok=True)
        with open(os.path.join(kpi_dir, "visual.json"), "w", encoding="utf-8") as f:
            json.dump(make_kpi_card_visual(), f, indent=2)

        # Main Chart Visual with Storytelling with Data
        main_dir = os.path.join(visuals_dir, f"main_vis_{idx:02d}")
        os.makedirs(main_dir, exist_ok=True)
        with open(os.path.join(main_dir, "visual.json"), "w", encoding="utf-8") as f:
            json.dump(make_main_visual(cfg), f, indent=2)

    pages_data["pageOrder"] = new_page_order
    with open(PAGES_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=2)

    print(f"Successfully generated all {len(SWD_CHARTS)} charts aligned with Storytelling with Data!")

if __name__ == "__main__":
    main()
