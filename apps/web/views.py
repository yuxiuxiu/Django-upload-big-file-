# encoding: utf-8
import os
from libs import ajax
from django.http import HttpResponse

def index(request):
    """分片上传"""

    if request.method == 'POST':
        #print("分片上传")
        upload_file = request.FILES.get('file')
        real_file_name = upload_file._name
        chunk = request.POST.get('chunk', 0)
        print("分片上传",chunk)
        filename = './file/%s%s' % (real_file_name, chunk)
        if not os.path.exists(filename):
            try:
                with open(filename, 'wb') as f:
                    # for obj in upload_file.chunks():
                    #     f.write(obj)
                    f.write(upload_file.read())
                    f.close()
            except Exception as e:
                print (e, 111)
    return ajax.ajax_template(request, 'web_upload/web_upload.html', {})

def upload_success(request):
    """所有分片上传成功"""
    print("所有分片上传成功")
    ext = request.POST.get('ext', '')
    upload_type = request.POST.get('type')
    name = request.POST.get('name')
    if len(ext) == 0 and upload_type:
        ext = upload_type.split('/')[1]
    chunk = 0
    with open("./file/%s" % name, 'wb') as target_file:  # 创建新文件
        while True:
            try:
                filename = './file/%s%s' % (name, chunk)
                source_file = open(filename, 'rb')  # 按序打开每个分片
                target_file.write(source_file.read())  # 读取分片内容写入新文件
                source_file.close()
                os.remove(filename)  # 删除该分片，节约空间
            except Exception as e:
                print(e, 222)
                break
            chunk += 1
        target_file.close()
        return HttpResponse("上传成功")

    return ajax.ajax_data(name)

def list_exist(request):
    """判断该文件上传了多少个分片"""
    name = request.POST.get('filename')
    chunk = 0
    data = {}
    filename = "./file/%s" % name

    #判断上传的文件是否存在
    if os.path.exists(filename):
        data['flag_exist'] = True
        data['file_path'] = filename
    else:
        data['flag_exist'] = False
    list = []
    while True:
        if os.path.exists("./file/%s%s" % (name, chunk)):
            list.append(chunk)
        else:
            break
        chunk += 1
    data['list'] = list
   # print('判断该文件上传了多少个分片',data)
    return ajax.ajax_data(data)