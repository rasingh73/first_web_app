# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 19:20:12 2020

@author: r_sin
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]