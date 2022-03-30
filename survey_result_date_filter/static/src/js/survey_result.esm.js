/** @odoo-module **/

import "survey.result";
import publicWidget from "web.public.widget";

publicWidget.registry.SurveyResultWidget.include({
    events: _.extend({}, publicWidget.registry.SurveyResultWidget.prototype.events, {
        "click #filter_date": "_onFilterDateClick",
    }),
    /**
     * @private
     * @param {Event} ev
     */
    _onFilterDateClick: function () {
        var params = new URLSearchParams(window.location.search);
        var date_from = $("input#datetimepicker_from").val();
        var date_end = $("input#datetimepicker_end").val();
        // Add new parameters or update existing ones;
        params.set("date_from", date_from);
        params.set("date_end", date_end);
        console.log(params.toString());
        window.location.href = window.location.pathname + "?" + params.toString();
    },
    /**
     * @private
     * @param {Event} ev
     */
    _onClearFilterClick: function () {
        this._super(...arguments);
        var params = new URLSearchParams(window.location.search);
        params.delete("date_from");
        params.delete("date_end");
        window.location.href = window.location.pathname + "?" + params.toString();
    },
});
