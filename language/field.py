class Field:
    field_tincture = None
    charge = None
    charge_quantity = None
    charge_tincture = None

    dof = None
    division = None

    def __init__(self, field_json, tincture, dof, division):
        self.field_tincture = tincture

        self.charge = field_json.get("charge")
        self.charge_quantity = field_json.get("quantity")
        self.charge_tincture = field_json.get("tincture")

        self.dof = dof
        self.division = division
