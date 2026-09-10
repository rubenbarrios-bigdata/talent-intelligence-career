import json

def generate_gtm_json(gtm_id="GTM-P2Z4TZ4Z", ga4_id="G-NQC5PHY67R"):
    container = {
        "exportFormatVersion": 2,
        "exportTime": "2026-09-09 21:55:00",
        "containerVersion": {
            "path": f"accounts/1000/containers/{gtm_id}/versions/0",
            "accountId": "1000",
            "containerId": gtm_id,
            "containerVersionId": "0",
            "name": "Talent Intelligence Career (TIC)®",
            "publicId": gtm_id,
            "container": {
                "path": f"accounts/1000/containers/{gtm_id}",
                "accountId": "1000",
                "containerId": gtm_id,
                "name": "Talent Intelligence Career",
                "publicId": gtm_id,
                "usageContext": ["WEB"]
            },
            "tag": [
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "1",
                    "name": "Google Tag - GA4 Configuration (TIC)",
                    "type": "googtag",
                    "parameter": [
                        {"type": "BOOLEAN", "key": "tagIdSettings", "value": "false"},
                        {"type": "TEMPLATE", "key": "tagId", "value": ga4_id}
                    ],
                    "firingTriggerId": ["2147479553"]  # All Pages
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "2",
                    "name": "GA4 Event - cv_kpi_interaction",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_kpi_interaction"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_id}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_number"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_number}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_label"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_label}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "target_anchor"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - target_anchor}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - candidate_id}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["101"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "3",
                    "name": "GA4 Event - cv_cert_filter",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_cert_filter"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "filter_category"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - filter_category}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - candidate_id}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["102"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "4",
                    "name": "GA4 Event - cv_document_download",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_document_download"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "document_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - document_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "document_name"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - document_name}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["103"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "5",
                    "name": "GA4 Event - cv_scroll_depth",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_scroll_depth"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "depth_percentage"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - depth_percentage}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["104"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "6",
                    "name": "GA4 Event - cv_theme_toggle",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_theme_toggle"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "theme_applied"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - theme_applied}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["105"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "7",
                    "name": "GA4 Event - cv_language_switch",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_language_switch"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "selected_language"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - selected_language}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["106"]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "tagId": "8",
                    "name": "GA4 Event - cv_external_click",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementId", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_external_click"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "link_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - link_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "target_url"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - target_url}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["107"]
                }
            ],
            "trigger": [
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "101",
                    "name": "Custom Event - cv_kpi_interaction",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_kpi_interaction"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "102",
                    "name": "Custom Event - cv_cert_filter",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_cert_filter"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "103",
                    "name": "Custom Event - cv_document_download",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_document_download"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "104",
                    "name": "Custom Event - cv_scroll_depth",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_scroll_depth"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "105",
                    "name": "Custom Event - cv_theme_toggle",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_theme_toggle"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "106",
                    "name": "Custom Event - cv_language_switch",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_language_switch"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "triggerId": "107",
                    "name": "Custom Event - cv_external_click",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_external_click"}
                            ]
                        }
                    ]
                }
            ],
            "variable": [
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "201",
                    "name": "dlv - kpi_id",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_id"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "202",
                    "name": "dlv - kpi_number",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_number"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "203",
                    "name": "dlv - kpi_label",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_label"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "204",
                    "name": "dlv - target_anchor",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "target_anchor"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "205",
                    "name": "dlv - filter_category",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "filter_category"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "206",
                    "name": "dlv - document_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "document_type"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "207",
                    "name": "dlv - document_name",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "document_name"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "208",
                    "name": "dlv - depth_percentage",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "depth_percentage"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "209",
                    "name": "dlv - theme_applied",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "theme_applied"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "210",
                    "name": "dlv - selected_language",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "selected_language"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "211",
                    "name": "dlv - link_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "link_type"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "212",
                    "name": "dlv - target_url",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "target_url"}
                    ]
                },
                {
                    "accountId": "1000",
                    "containerId": gtm_id,
                    "variableId": "213",
                    "name": "dlv - candidate_id",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"}
                    ]
                }
            ]
        }
    }

    filename = "gtm_tic_container.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(container, f, indent=2, ensure_ascii=False)
    print(f"GTM Container JSON exported to: {filename}")

if __name__ == "__main__":
    generate_gtm_json()
