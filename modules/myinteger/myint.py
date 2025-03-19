class IntegerWrapper:
    def __init__(self, base_value: int):
        self.input_value = base_value

    def get_modified_value(self, value_modifier : int) -> int:
        return value_modifier + self.input_value

if __name__ == '__main__':
    print("###############################################################################")
    print("This is MAIN of %s" % __file__)
    print("###############################################################################")