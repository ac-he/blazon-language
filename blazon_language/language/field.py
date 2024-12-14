from blazon_language.language.evaluation import stringify_charge, make_charge_render_friendly, is_metal


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

        self.enforce_rule_of_tincture(self.charge_tincture)

    def enforce_rule_of_tincture(self, charge_tincture):
        if not charge_tincture or not self.field_tincture:
            return
        if ((is_metal(charge_tincture) and is_metal(self.field_tincture)) or
                (not is_metal(self.field_tincture) and not is_metal(charge_tincture))):
            raise Exception(f"Cannot have a {charge_tincture} charge on a {self.field_tincture} field.")

    def get_render_friendly_charge(self):
        if not self.rf_charge:
            s_charge = stringify_charge(self.charge)
            self.rf_charge = make_charge_render_friendly(s_charge)
        return self.rf_charge

