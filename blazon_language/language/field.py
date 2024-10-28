from blazon_language.language._evaluation import stringify_charge, make_charge_render_friendly


class Field:
    field_tincture = None
    charge = None
    charge_quantity = None
    charge_tincture = None

    dof = None
    division = None

    rf_charge = None

    def __init__(self, field_json, tincture, dof, division):
        self.field_tincture = tincture

        self.charge = field_json.get("charge")
        self.charge_quantity = field_json.get("quantity")
        self.charge_tincture = field_json.get("tincture")

        self.dof = dof
        self.division = division

    def get_render_friendly_charge(self):
        if not self.rf_charge:
            s_charge = stringify_charge(self.charge)
            self.rf_charge = make_charge_render_friendly(s_charge)
        return self.rf_charge

