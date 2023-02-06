from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import File
import os, datetime
import json

# Create your views here.

def index(request):
    if request.method == 'POST' and request.FILES['file']:
        upload_file = request.FILES['file']
        extension = os.path.splitext(upload_file.name)[1]
        rename = datetime.datetime.now().strftime("%Y_%m_%d %H_%M_%S") + extension
        fss = FileSystemStorage()
        filename = fss.save(rename, upload_file)
        file = File(file=rename)
        file.save()
        upload_file_path = fss.path(filename)
        #open file with path
        with open(upload_file_path, "r+b") as file:
            #read data in path
            data=file.read()
            my_str = data.decode('utf-8')
            #my_str = data.read()
            res = json.loads(my_str)
            special=[]
            for keys,values in res.items():
                if type(values)==list:
                    for values1 in values:
                        if type(values1)==dict:
                            for (key,value) in values1.items():
                                if type(value)==list:
                                    for j in value:
                                        special.append([keys,key,j])
                                else:
                                    special.append([keys,key,value])
                        else:
                            special.append([keys,values1])
                else:
                    special.append([keys,values])
            print("\n\n")
            str2=[]
            for i in special:
                str1=''
                for j in i:
                    #str1+=(j)+'.'
                    str1+='"' + str(j) + '"' + '.'
        
                str1=str1[:-1]
                str2.append(str1)
            print("\n\n")
            string=''
            for con_str in str2:
                #string+='"'+con_str+'"'+',\n'
                string+=con_str+',\n'
            string=string[:-2]

        path="output.txt"
        text_file = open(path, "w")
        n = text_file.write(string)
        text_file.close()
        basic_path=str(  os.path.dirname(__file__))
        basic_path=basic_path[:-4]+path
        
        return render(request, 'file/index.html', {
            'upload_file_path': string,
            'path':basic_path
        })
    else:
        return render(request, 'file/index.html')