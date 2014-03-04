django-uuidfield
----------------

.. image:: https://travis-ci.org/julienaubert/django-uuidfield.png?branch=python3   
   :target: https://travis-ci.org/julienaubert/django-uuidfield
.. image:: https://coveralls.io/repos/julienaubert/django-uuidfield/badge.png?branch=python3 
   :target: https://coveralls.io/r/julienaubert/django-uuidfield?branch=python3 


Provides a UUIDField for your Django models.

Installation
============

Install it with pip (or easy_install)::

	pip install django-uuidfield

Usage
=====

First you'll need to attach a UUIDField to your class. This acts as a char(32) to maintain compatibility with SQL versions::

	from uuidfield import UUIDField
	
	class MyModel(models.Model):
	    uuid = UUIDField(auto=True)

Check out the source for more configuration values.

Enjoy!
