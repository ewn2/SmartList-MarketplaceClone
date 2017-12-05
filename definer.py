
class definer:

    def __init__(self, ListingName, AskingPrice, Description, Picture, Email, Phone):

        self.ListingName = ListingName
        self.AskingPrice = AskingPrice
        self.Description = Description
        self.Picture = Picture
        self.Email = Email
        self.Phone = Phone

    def get_ListingName(self):
        return self.ListingName

    def get_AskingPrice(self):
        return self.AskingPrice

    def get_Description(self):
        return self.Description

    def get_Picture(self):
        return self.Picture

    def get_Email(self):
        return self.Email

    def get_Phone(self):
        return self.Phone
