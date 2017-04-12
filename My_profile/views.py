# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from My_profile.models import Information,Address,Contact_Info
from django.template import RequestContext
from django.forms import ModelForm

# Create your views here.

def Name_view(request):

	'''class My_Information(ModelForm):
		class Meta:
			Model = Information
			fields =('F_name','Age','Gender')
	form = {"My_Information":My_Information}'''
	
	context = {"name":[f.name for f in Information._meta.get_fields()]}
	return render(request,'name.html', context)


def Address_view(request):

	context = {"address":[f.name for f in Address._meta.get_fields()]}
	return render(request,'name.html', context)

def contact(request):

	context = {"contact":[f.name for f in Contact_Info._meta.get_fields()]}
	return render(request,'name.html', context)