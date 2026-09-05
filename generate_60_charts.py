import json
import os

BASE_DIR = r"C:\Users\frank\Desktop\dt\DAX\RetailSalesDemo.Report\definition\pages"
PAGES_JSON_PATH = os.path.join(BASE_DIR, "pages.json")

# Definitive 60 chart definitions with exact Power BI PBIR visualType, roles, and visual properties
CHARTS_CONFIG = [
    # 01-10 Line Fundamentals & Variations
    (1, "Discrete Line Chart", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, {"categoryAxis": [{"properties": {"axisType": {"expr": {"Literal": {"Value": "'Categorical'"}}}}}]}),
    (2, "Continuous Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"categoryAxis": [{"properties": {"axisType": {"expr": {"Literal": {"Value": "'Scalar'"}}}}}]}),
    (3, "Line Chart with Markers", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "5L"}}}}}]}),
    (4, "Line Chart with Circle Markers", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerShape": {"expr": {"Literal": {"Value": "'circle'"}}}, "markerSize": {"expr": {"Literal": {"Value": "8L"}}}}}]}),
    (5, "Dashed Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dashed'"}}}}}]}),
    (6, "Dotted Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dotted'"}}}}}]}),
    (7, "Stepped Line Chart", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"stepped": {"expr": {"Literal": {"Value": "true"}}}}}]}),
    (8, "Line Chart Multiple Dimensions", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimRegion", "RegionName", None, None),
    (9, "Line Chart Multiple Measures", "lineChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Cost", "Total Profit"], None, None, None, None),
    (10, "Line Chart Ends of Line Labels", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"labels": [{"properties": {"show": {"expr": {"Literal": {"Value": "true"}}}}}]}),
    
    # 11-18 Moving Averages & Area Variations
    (11, "Moving Average", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue 30D Moving Avg", None, None, None, None),
    (12, "Area Chart", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, None),
    (13, "Area Chart + Line Chart", "areaChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Profit"], None, None, None, None),
    (14, "Area Chart + Dashed Line", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dashed'"}}}}}]}),
    (15, "Area Chart + Dotted Line", "areaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"lineStyle": {"expr": {"Literal": {"Value": "'dotted'"}}}}}]}),
    (16, "Stacked Area Chart", "stackedAreaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (17, "% of Total Area Chart", "hundredPercentStackedAreaChart", "DimDate", "Date", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (18, "Line Chart + Moving Avg", "lineChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Revenue 30D Moving Avg"], None, None, None, None),
    
    # 19-25 Variances & Running Totals
    (19, "Difference from Previous", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Revenue MoM Variance", None, None, None, None),
    (20, "% Difference from Previous", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue MoM %", None, None, None, None),
    (21, "Difference vs. First", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Difference vs First", "DimRegion", "RegionName", None, None),
    (22, "% Difference vs. First", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue % Difference vs First", "DimRegion", "RegionName", None, None),
    (23, "Running Total", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Running Total", None, None, None, None),
    (24, "Running Total Area Chart", "areaChart", "DimDate", "Date", "_MEASURES", ["Revenue Running Total", "Cost Running Total"], None, None, None, None),
    (25, "Running Total from 1st Sale", "lineChart", "DimDate", "Date", "_MEASURES", "Revenue Running Total", "DimRegion", "RegionName", None, None),
    
    # 26-35 Bars, Columns & Dual Axis Combos
    (26, "Bar Chart", "clusteredBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, None),
    (27, "Stacked Bar Chart", "stackedBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (28, "% of Total Stacked Bars", "hundredPercentStackedBarChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (29, "Paired Column Chart", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None),
    (30, "Column Chart", "stackedColumnChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (31, "Lollipop Chart", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"dataPoint": [{"properties": {"showAllDataPoints": {"expr": {"Literal": {"Value": "true"}}}}}]}),
    (32, "Bar-in-Bar Chart", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None),
    (33, "Bar Chart w/ Reference Line", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", "Total Revenue", None, None, None, None),
    (34, "Dual Axis w/ Different Measures", "lineClusteredColumnComboChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, "Profit Margin %", None),
    (35, "Dual Axis w/ Related Measures", "lineClusteredColumnComboChart", "DimDate", "Date", "_MEASURES", "Total Cost", None, None, "Total Revenue", None),
    
    # 36-43 Averages, Cycles, Slopes & Butterflies
    (36, "Variance to Overall Average", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", "Revenue Variance to Overall Avg", None, None, None, None),
    (37, "Variance to Pane Average", "clusteredColumnChart", "DimDate", "Month", "_MEASURES", "Revenue Variance to Overall Avg", None, None, None, None),
    (38, "Cycle Plot", "lineChart", "DimDate", "Weekday", "_MEASURES", "Total Revenue", "DimDate", "Month", None, None),
    (39, "Single Month Calendar", "pivotTable", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimDate", "Weekday", None, None),
    (40, "Discrete Slope Graph", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (41, "Continuous Slope Graph", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimRegion", "RegionName", None, None),
    (42, "Butterfly Chart Single Axis", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Negative Cost"], None, None, None, None),
    (43, "Butterfly Chart Dual Axis", "clusteredBarChart", "DimDate", "Month", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None),
    
    # 44-51 Dot Plots, Barcodes & Sparklines
    (44, "Dot Plot", "scatterChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, None),
    (45, "Barcode Chart", "clusteredBarChart", "FactSales", "SalesKey", "_MEASURES", "Total Revenue", None, None, None, None),
    (46, "Sparklines", "tableEx", "DimProduct", "ProductName", "_MEASURES", ["Total Revenue", "Total Profit", "Total Units"], None, None, None, None),
    (47, "Sparkbars", "tableEx", "DimRegion", "RegionName", "_MEASURES", ["Total Revenue", "Total Cost", "Total Units"], None, None, None, None),
    (48, "Spark Area Chart", "tableEx", "DimProduct", "Category", "_MEASURES", ["Total Revenue", "Total Profit", "Profit Margin %"], None, None, None, None),
    (49, "Connected Dot Plot", "lineChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, None, {"lineStyles": [{"properties": {"showMarker": {"expr": {"Literal": {"Value": "true"}}}, "markerSize": {"expr": {"Literal": {"Value": "6L"}}}}}]}),
    (50, "Enclosed Dot Plot", "scatterChart", "_MEASURES", "Total Cost", "_MEASURES", "Total Revenue", "DimProduct", "Category", None, None),
    (51, "Circle Timeline", "scatterChart", "DimDate", "Date", "_MEASURES", "Total Revenue", None, None, "Total Units", None),
    
    # 52-60 Rankings, Trajectories, Bridges & Stock
    (52, "Bump Chart", "lineChart", "DimDate", "Month", "_MEASURES", "Product Rank", "DimProduct", "ProductName", None, None),
    (53, "Seismogram", "clusteredBarChart", "DimDate", "Date", "_MEASURES", "Revenue MoM Variance", None, None, None, None),
    (54, "Parallel Coordinates", "lineChart", "DimDate", "Month", "_MEASURES", "Total Revenue", "DimProduct", "ProductName", None, None),
    (55, "Small Multiple Donut Charts", "donutChart", "DimProduct", "Category", "_MEASURES", "Total Revenue", None, None, None, None),
    (56, "Connected Scatterplot", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None),
    (57, "Connected Scatterplot Dotted Lines", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None),
    (58, "Animated Connected Scatterplot", "scatterChart", "_MEASURES", "Total Revenue", "_MEASURES", "Total Profit", "DimDate", "Date", None, None),
    (59, "Waterfall Chart", "waterfallChart", "DimDate", "Date", "_MEASURES", "Total Profit", None, None, None, None),
    (60, "Stock Chart", "clusteredColumnChart", "DimDate", "Date", "_MEASURES", ["Total Revenue", "Total Cost"], None, None, None, None),
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
    idx, title, vtype, cat_entity, cat_prop, val_entity, val_prop, ser_entity, ser_prop, extra_arg, visual_objects = chart_tuple

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
        # Check X and Y bindings
        x_proj = make_field_measure(cat_entity, cat_prop) if cat_entity == "_MEASURES" else make_field_col(cat_entity, cat_prop)
        y_proj = make_field_measure(val_entity, val_prop) if val_entity == "_MEASURES" else make_field_col(val_entity, val_prop)
        query_state = {
            "X": {"projections": [x_proj]},
            "Y": {"projections": [y_proj]}
        }
        if ser_entity and ser_prop:
            query_state["Details"] = {"projections": [make_field_col(ser_entity, ser_prop)]}
        if extra_arg: # Size bucket
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

    visual_obj = {
        "visualType": vtype,
        "query": {"queryState": query_state}
    }
    if sort_def:
        visual_obj["query"]["sortDefinition"] = sort_def
    if visual_objects:
        visual_obj["objects"] = visual_objects
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

    for cfg in CHARTS_CONFIG:
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

        # Main Chart Visual
        main_dir = os.path.join(visuals_dir, f"main_vis_{idx:02d}")
        os.makedirs(main_dir, exist_ok=True)
        with open(os.path.join(main_dir, "visual.json"), "w", encoding="utf-8") as f:
            json.dump(make_main_visual(cfg), f, indent=2)

    pages_data["pageOrder"] = new_page_order
    with open(PAGES_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(pages_data, f, indent=2)

    print(f"Successfully generated and fixed all {len(CHARTS_CONFIG)} dedicated time-series pages!")

if __name__ == "__main__":
    main()
