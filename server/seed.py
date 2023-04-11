#!/usr/bin/env python3

import email
from random import choice as rc, randint

from faker import Faker

from app import app
from models import db, Customer


fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_customers():

    Customer.query.delete()
    
    customers = []

    for i in range(3):
        customer = Customer(
            email=fake.email(),
            age= randint(0, 125),
            name=fake.name()
        )
        customers.append(customer)

    db.session.add_all(customers)
    db.session.commit()        

if __name__ == '__main__':
    with app.app_context():
        make_customers()
