# Copyright 2020 Pesol
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Survey Result Date Filter",
    "summary": "Introduce a filtering section in Survey Result",
    "version": "15.0.1.0.0",
    "maintainers": ["pesol"],
    "category": "Survey",
    "website": "https://github.com/OCA/survey",
    "author": "Pesol <pedro.gonzalez@pesol.es>, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["survey", "website"],
    "data": ["views/templates.xml"],
    "assets": {
        "web.assets_frontend": [
            "survey_result_date_filter/static/src/js/survey_result.esm.js",
            "survey_result_date_filter/static/src/css/style.css",
        ],
    },
}
