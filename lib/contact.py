from peewee import *



db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)
db.connect()
class BaseModel(Model):
    class Meta:
        database = db
class Contact(BaseModel):
    name = CharField()
    phone = IntField()





db.create_tables([Contact])
contact1= Contact(name='Lina', phone= 6758996735)
contact1.save()
print("contact created")

contact2= Contact(name='Peter', phone= 8173352789)
contact2.save()
print("contact created")

contact3= Contact(name='Antonette', phone= 262779101)
contact3.save()
print("contact created")

contact4= Contact(name='Billy', phone= 7812234782)
contact4.save()
print("contact created")

contact5= Contact(name='Teo', phone= 8956671236)
contact5.save()
print("contact created")

contact6= Contact(name='Dhruv', phone= 1879963456)
contact6.save()
print("contact created")

contact7= Contact(name='Noah', phone= 3489907253)
contact7.save()
print("contact created")

contact8= Contact(name='Brad', phone= 5649085643)
contact8.save()
print("contact created")

contact9= Contact(name='Zack', phone= 9086773512)
contact9.save()
print("contact created")

contact10= Contact(name='Alaïa', phone= 5302276359)
contact10.save()
print("contact created")
#get

get_contact = Contact.get(Contact.name == '')
print(get_contact.phone)


# list_of_people = Person.select().where(Person.birthday > datetime.date(1990, 1, 1))
# print(list_of_people)

#update 

# hello = Person.get(Person.name =='Dakk')
# hello.birthday = datetime.date(1980, 11, 30)
# hello.save()

#delete

# hello.delete_instance()