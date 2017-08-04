# -*- encoding: utf-8 -*-
# begin

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, BigInteger,String, ForeignKey, Unicode, Binary, LargeBinary, Time, DateTime, Date, Text, Boolean, Float
from sqlalchemy.orm import relationship, backref, deferred
from sqlalchemy.orm import sessionmaker


engine = create_engine("DB_FILE/URL")
Base = declarative_base()
session = sessionmaker(bind=engine)()


# Basic user info
class User (Base):
    __tablename__ = "user"

    roll_no = Column('roll_no', Unicode, primary_key = True)
    name = Column('name', Unicode)
    dob = Column('DOB', Date)
    gender = Column('gender', Unicode)
    photograph = deferred(Column('photograph', Text))
    resident_country = Column('resident_country', Unicode)
    nationality = Column('nationality', Unicode)
    blood_group = Column('blood_group', Unicode)
    marital_status = Column('marital_status', Boolean)
    email_0 = Column('email_0', Unicode)
    email_1 = Column('email_1', Unicode)
    phone_0 = Column('phone_0', Unicode)
    phone_1 = Column('phone_1', Unicode)
    link_facebook = Column('link_facebook', Unicode)
    link_twitter = Column('link_twitter', Unicode)
    link_github = Column('link_github', Unicode)
    link_blog = Column('link_blog', Unicode)
    link_website = Column('link_website', Unicode)
    link_skype = Column('link_skype', Unicode)
    correspondence_address_id = Column('correspondence_address_id', Unicode, ForeignKey('address.id'))
    permanent_address_id = Column('permanent_address_id', Unicode, ForeignKey('address.id'))

    correspondance_address = relationship('Address', foreign_keys=correspondence_address_id)
    permanent_address = relationship('Address', foreign_keys=permanent_address_id)


# The collection of all addresses
class Address (Base):
    __tablename__ = "address"

    id = Column('id', Unicode, primary_key = True)
    address_line_1 = Column('address_line_1', Unicode)
    address_line_2 = Column('address_line_2', Unicode)
    city = Column('city', Unicode)
    state = Column('state', Unicode)
    country = Column('country', Unicode)
    zipcode = Column('zipcode', Unicode)
    user_roll_no = Column('user_roll_no', Unicode)


# Collection of qualifications of all users
class Qualification (Base):
    __tablename__ = "qualification"

    id = Column('id', String, primary_key = True)
    roll_no = Column('roll_no', Unicode, ForeignKey('user.roll_no'))
    category = Column('category', Integer)
    institute = Column('institute', Unicode)
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date)
    grade = Column('grade', BigInteger)

    user = relationship('User', foreign_keys=roll_no)

# Collection of all work experiences
class WorkExperience (Base):
    __tablename__ = "work_experience"

    id = Column('id', String, primary_key = True)
    roll_no = Column('roll_no', Unicode, ForeignKey('user.roll_no'))
    employer = Column('employer', Unicode)
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date)
    sector = Column('sector', Unicode)
    designation = Column('designation', Unicode)
    founder = Column('founder', Boolean)
    city = Column('city', Unicode)
    country = Column('country', Unicode)
    address_id = Column('address_id', Unicode, ForeignKey('address.id'))

    user = relationship('User', foreign_keys=roll_no)
    address = relationship('Address', foreign_keys=address_id)

# end
