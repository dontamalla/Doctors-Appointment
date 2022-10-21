from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.dbmodel import Doctors
from app.dbmodel import Appointments

import time
import random
from datetime import datetime

@api_view(['GET','POST','DELETE'])
def doctors_info(request,dept):
    if request.method == 'GET':
        doc_obj = Doctors.objects.filter(department=dept)
        doc_list = []
        avail_dic = {}
        if len(doc_obj) == 0:
            return Response(status=400)
        else:
            for i in doc_obj:
                dic = {}
                dic["doctor_id"]=i.doctor_id
                dic["doctor_name"]=i.doctor_name
                dic["department"]=i.department
                doc_list.append(dic)
            avail_dic["doctors_available"]=doc_list
            return Response(status=200,data=avail_dic)
    elif request.method == 'POST':
        pat_name = request.data.get("name")
        pat_gen = request.data.get("gender")
        pat_age = request.data.get("age")
        pat_disease = request.data.get("disease")
        pat_dept = request.data.get("department")
        doc_name = request.data.get("doctor")
        pat_mobile = request.data.get("mobile")

        doc_id = request.data.get("doctor_id")

        # apt = Doctors.objects.filter(doctor_id=doc_id)
        ts = int(time.time()) + (2*86400)
        dt = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        Appointments(
            Patient_name = pat_name,
            gender = pat_gen,
            patient_age = pat_age,
            disease = pat_disease,
            contact = pat_mobile,
            doctor_name = doc_name,
            department = pat_dept,
            doctor_id = doc_id,
            date_time = dt
        ).save()
        return Response(status=200)


@api_view(['POST'])
def doctors_data(request,did):
    if request.method == 'POST':
        # doc_id = request.data.get("user_id")
        doc_name = request.data.get("name")
        dep = request.data.get("department")
        dic = Doctors.objects.filter(doctor_id=doc_id)
        if len(dic) >= 1:
            return Response(status=400)
        else:
            Doctors(
                doctor_id = doc_id,
                doctor_name = doc_name,
                department = dep
            ).save()
            return Response(status=200)

@api_view(['GET'])
def patients_list(request,did):
    if request.method == "GET":
        # quary_data = request.query_params.get("date")
        ls = Appointments.objects.filter(doctor_id=did)
        if len(ls) == 0:
            return Response(status=400)
        else:
            em_list = []
            em_dict = {}
            for i in ls:
                dic = {}
                dic["Patient_name"]=i.Patient_name
                dic["gender"]=i.gender
                dic["patient_age"]=i.patient_age
                dic["disease"]=i.disease
                dic["contact"]=i.contact
                dic["doctor_name"]=i.doctor_name
                dic["department"]=i.department
                dic["doctor_id"]=i.doctor_id
                dic["date_time"]=i.date_time
                em_list.append(dic)
            em_dict["patients"]=em_list
            return Response(status=200,data=em_dict)
