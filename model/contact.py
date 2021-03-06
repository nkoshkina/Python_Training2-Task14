from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 title=None, company=None, address=None,
                 hphone=None, mphone=None, wphone=None, fax=None,
                 email=None, email2=None, email3=None,
                 homepage=None,
                 dbirthday=None, mbirthday=None, ybirthday=None,
                 danniversary=None, manniversary=None, yanniversary=None,
                 saddress=None, sphone=None, snotes=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None
                 ):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.hphone = hphone
        self.mphone = mphone
        self.wphone = wphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.dbirthday = dbirthday
        self.mbirthday = mbirthday
        self.ybirthday = ybirthday
        self.danniversary = danniversary
        self.manniversary = manniversary
        self.yanniversary = yanniversary
        self.saddress = saddress
        self.sphone = sphone
        self.snotes = snotes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
        (self.lastname == other.lastname or self.lastname is None  or
         other.lastname is None) and \
        (self.firstname == other.firstname or self.firstname is None or
        other.firstname is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize