class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day

    @classmethod
    def create(cls , str_date):
        # year,month,day =str_date.split('-')
        # year=int(year)
        # month=int(month)
        # day=int(day)
        year, month, day =map(int,str_date.split('-'))
        mydate = cls(year,month,day)
        return mydate

    def is_date_valid(str_date):
        year,month,day=map(int,str_date.split('-'))
        return year < 4000 and 1<=month<=12 and 1<=day<=31

if __name__ == '__main__':
    # d1 = Date(2019.3,19)
    d2 = Date.create("2019-03-19")
    print(d2.year,d2.month,d2.day)
    print(Date.is_date_valid("2019-04-01"))
    print(Date.is_date_valid("2019-15-12"))