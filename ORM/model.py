# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = {'schema': 'northwind'}

    categoryid = Column(Integer, primary_key=True)
    categoryname = Column(String(50))
    description = Column(String(100))
    qtd_products = Column(Integer, nullable=False, server_default=text("0"))


class Customer(Base):
    __tablename__ = 'customers'
    __table_args__ = {'schema': 'northwind'}

    customerid = Column(String(5), primary_key=True)
    companyname = Column(String(50))
    contactname = Column(String(30))
    contacttitle = Column(String(30))
    address = Column(String(50))
    city = Column(String(20))
    region = Column(String(15))
    postalcode = Column(String(9))
    country = Column(String(15))
    phone = Column(String(17))
    fax = Column(String(17))


class Employee(Base):
    __tablename__ = 'employees'
    __table_args__ = {'schema': 'northwind'}

    employeeid = Column(Integer, primary_key=True)
    lastname = Column(String(10))
    firstname = Column(String(10))
    title = Column(String(25))
    titleofcourtesy = Column(String(5))
    birthdate = Column(DateTime)
    hiredate = Column(DateTime)
    address = Column(String(50))
    city = Column(String(20))
    region = Column(String(2))
    postalcode = Column(String(9))
    country = Column(String(15))
    homephone = Column(String(14))
    extension = Column(String(4))
    reportsto = Column(Integer)
    notes = Column(Text)


t_qtd_produtos_categorias = Table(
    'qtd_produtos_categorias', metadata,
    Column('categoryid', Integer),
    Column('categoryname', String(50)),
    Column('count', BigInteger),
    schema='northwind'
)


t_relatorio = Table(
    'relatorio', metadata,
    Column('orderid', Integer),
    Column('customerid', String(5)),
    Column('employeeid', Integer),
    Column('total_products', BigInteger),
    Column('total_price', Numeric),
    schema='northwind'
)


class Shipper(Base):
    __tablename__ = 'shippers'
    __table_args__ = {'schema': 'northwind'}

    shipperid = Column(Integer, primary_key=True)
    companyname = Column(String(20))
    phone = Column(String(14))


class Supplier(Base):
    __tablename__ = 'suppliers'
    __table_args__ = {'schema': 'northwind'}

    supplierid = Column(Integer, primary_key=True)
    companyname = Column(String(50))
    contactname = Column(String(30))
    contacttitle = Column(String(30))
    address = Column(String(50))
    city = Column(String(20))
    region = Column(String(15))
    postalcode = Column(String(8))
    country = Column(String(15))
    phone = Column(String(15))
    fax = Column(String(15))
    homepage = Column(String(100))


class Order(Base):
    __tablename__ = 'orders'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(Integer, primary_key=True)
    customerid = Column(ForeignKey('northwind.customers.customerid', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    employeeid = Column(ForeignKey('northwind.employees.employeeid', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    orderdate = Column(DateTime)
    requireddate = Column(DateTime)
    shippeddate = Column(DateTime)
    freight = Column(Numeric(15, 4))
    shipname = Column(String(35))
    shipaddress = Column(String(50))
    shipcity = Column(String(15))
    shipregion = Column(String(15))
    shippostalcode = Column(String(9))
    shipcountry = Column(String(15))
    shipperid = Column(Integer)
    qtdprodutos = Column(Integer, server_default=text("0"))
    maisdesconto = Column(Integer, server_default=text("0"))

    customer = relationship('Customer')
    employee = relationship('Employee')


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'northwind'}

    productid = Column(Integer, primary_key=True)
    productname = Column(String(35))
    supplierid = Column(Integer, nullable=False)
    categoryid = Column(ForeignKey('northwind.categories.categoryid', ondelete='RESTRICT', onupdate='CASCADE'), nullable=False)
    quantityperunit = Column(String(20))
    unitprice = Column(Numeric(13, 4))
    unitsinstock = Column(SmallInteger)
    unitsonorder = Column(SmallInteger)
    reorderlevel = Column(SmallInteger)
    discontinued = Column(String(1))

    category = relationship('Category')


class OrderDetail(Base):
    __tablename__ = 'order_details'
    __table_args__ = {'schema': 'northwind'}

    orderid = Column(ForeignKey('northwind.orders.orderid', ondelete='RESTRICT', onupdate='CASCADE'), ForeignKey('northwind.orders.orderid', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    productid = Column(ForeignKey('northwind.products.productid', ondelete='RESTRICT', onupdate='CASCADE'), ForeignKey('northwind.products.productid', ondelete='RESTRICT', onupdate='CASCADE'), primary_key=True, nullable=False)
    unitprice = Column(Numeric(13, 4))
    quantity = Column(SmallInteger)
    discount = Column(Numeric(10, 4))

    order = relationship('Order', primaryjoin='OrderDetail.orderid == Order.orderid')
    order1 = relationship('Order', primaryjoin='OrderDetail.orderid == Order.orderid')
    product = relationship('Product', primaryjoin='OrderDetail.productid == Product.productid')
    product1 = relationship('Product', primaryjoin='OrderDetail.productid == Product.productid')
    
class EmployeeRanking:
    def __init__(self, firstname, lastname, orders, total_value):
        self.firstname = firstname
        self.lastname = lastname
        self.orders = orders
        self.total_value = total_value

    def __repr__(self):
        return f"EmployeeRanking(firstname={self.firstname}, lastname={self.lastname}, orders={self.orders}, total_value={self.total_value})"
