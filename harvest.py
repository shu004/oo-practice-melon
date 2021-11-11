############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, name, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType("musk", "Muskmelon", 1998, "green", True, True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    casaba = MelonType("cas", "Casaba", 2003, "orange", False, False)
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType("cren", "Crenshaw", 1996, "green", False, False)
    crenshaw.add_pairing("proscuitto")
    all_melon_types.append(crenshaw)

    yw  = MelonType("yw", "Yellow Watermelon", 2013, "yellow", False, True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types




def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for item in melon.pairings:
            print(f"- {item}")

    # Fill in the rest

# print_pairing_info(make_melon_types())

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}
    for melon_obj in melon_types:
        if melon_obj.code not in melon_dict:
            melon_dict[melon_obj.code] = melon_obj

    return melon_dict




############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvestor):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvestor = harvestor

    def is_sellable(self):
        if self.shape_rating > 5 and self.color_rating > 5 and self.field != 3:
            return True



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    our_melon_type = []
    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 5, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 5, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Micheal")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")
    our_melon_type.extend([melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9])

    return our_melon_type



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon_obj in melons:
        if melon_obj.is_sellable():
            print(f"Harvested by {melon_obj.harvestor} from Field {melon_obj.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon_obj.harvestor} from Field {melon_obj.field} (NOT SELLABLE)")

get_sellability_report(make_melons(make_melon_types()))

