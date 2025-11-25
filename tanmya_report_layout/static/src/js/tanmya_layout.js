/** @odoo-module */

import {patch} from "@web/core/utils/patch";
import {_t} from "@web/core/l10n/translation";
import {NewReportDialog} from "@web_studio/views/kanban_report/new_report_dialog";

patch(NewReportDialog.prototype, {
    setup() {
        super.setup();

        // Add your custom layout to the existing layouts
        this.layouts.push({
            name: "tanmya_report_layout.custom_layout",
            label: _t("Altanmya Layout"),
            description: _t("Business header/footer"),
        });
    },
});
