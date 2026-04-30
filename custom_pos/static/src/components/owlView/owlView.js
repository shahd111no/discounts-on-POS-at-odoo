/** @odoo-module */

import { Order } from "@point_of_sale/app/store/models";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    set_partner(partner) {

        super.set_partner(partner);
        if (partner && partner.discount>0) {
            const lines = this.get_orderlines();
            lines.forEach(line => {

                line.set_discount(partner.discount);

            });
        }

        else {
            const lines = this.get_orderlines();
            lines.forEach(line => {
                line.set_discount(0);
            });

        }



    },

    async add_product(product, options) {
        super.add_product(...arguments);
        const partner= this.get_partner();
        if (partner && partner.discount>0) {
            const line = this.get_last_orderline();
            if(line){
                line.set_discount(partner.discount)
            }
        }
    },
});




