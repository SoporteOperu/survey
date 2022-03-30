# Copyright <2020> PESOL <info@pesol.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models


class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    # ------------------------------------------------------------
    # STATISTICS / REPORTING
    # ------------------------------------------------------------

    def _get_percent_stat(self, count, answer_lines):
        skipped_lines = answer_lines.filtered(lambda line: line.skipped)
        done_lines = answer_lines - skipped_lines
        done_lines = done_lines.mapped("user_input_id")
        return round(count * 100.0 / (len(done_lines) or 1), 2)

    def _get_stats_data(self, user_input_lines):
        res1, res2 = super(SurveyQuestion, self)._get_stats_data(user_input_lines)
        if self.question_type in ["simple_choice", "multiple_choice"]:
            res1 = sorted(
                res1,
                key=lambda r: self._get_percent_stat(r["count"], user_input_lines),
                reverse=True,
            )
        return res1, res2
