# Copyright <2020> PESOL <info@pesol.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from datetime import datetime

from odoo import _, fields, tools
from odoo.osv import expression

from odoo.addons.survey.controllers.main import Survey


class CustomeSurvey(Survey):
    def validate_and_combine_date(self, date_str, time_str):
        """
        Combine date and time and return a string with well formed date
        """
        try:
            date = datetime.strptime(
                "{} {}".format(date_str, time_str), tools.DEFAULT_SERVER_DATETIME_FORMAT
            )
        except ValueError as vale:
            raise ValueError(_("Error processing date {}").format(date_str)) from vale
        return datetime.strftime(date, tools.DEFAULT_SERVER_DATETIME_FORMAT)

    def _get_date_filters(self, post):
        date_from = False
        date_end = False
        if post.get("date_from", False) or post.get("date_end", False):
            today = fields.Date.to_string(fields.Date.today())
            date_from = post.get("date_from", today)
            date_end = post.get("date_end", today)
            date_from = self.validate_and_combine_date(date_from, "00:00:00")
            post.pop("date_from", None)
            date_end = self.validate_and_combine_date(date_end, "23:59:59")
            post.pop("date_end", None)
        return date_from, date_end

    def _get_user_input_domain(self, survey, line_filter_domain, **post):
        """Gets the date_from and date_end parameters furthermore the rest of
        filters
        :param post:
        :return: list of filters
        """
        date_from, date_end = self._get_date_filters(post)

        res = super(CustomeSurvey, self)._get_user_input_domain(
            survey, line_filter_domain, **post
        )
        if date_from and date_end:
            res = expression.AND(
                [
                    [
                        "&",
                        ("create_date", ">=", date_from),
                        ("create_date", "<=", date_end),
                    ],
                    res,
                ]
            )
        return res

    def _extract_filters_data(self, survey, post):
        user_input_lines, search_filters = super(
            CustomeSurvey, self
        )._extract_filters_data(survey, post)
        date_from, date_end = self._get_date_filters(post)
        if date_from and date_end:
            search_filters.append({"question": "Date From", "answers": date_from})
            search_filters.append({"question": "Date End", "answers": date_end})
        return user_input_lines, search_filters
