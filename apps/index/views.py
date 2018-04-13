from django.shortcuts import render

# Create your views here.


from libs import ajax

def p_api(request):
    data = {}
    for i in range(6):
        data[i] = i * i
    return ajax.ajax_data(data)


def p_html(request):

    row = []
    for i in range(6):
        data = {}
        data['name'] = "赵铁柱" if i else '茱莉亚罗伯茨耶利奇巴鲁德蒙'
        data['sex'] = '男' if i else '女'
        data['weight'] = '80kg' if i else '60kg'
        data['height'] = 180 if i else 160
        data['marryid'] = '未婚' if i else '已婚'
        row.append(data)
        row.append(data)
    context = {}
    context['data'] = row
    print(context)
    return ajax.ajax_template(request, 'index/info.html', context)


def upload(request):
    """分片上传"""
    if request.method == 'POST':
        inp_files = request.FILES
        file_obj = inp_files.get('f1')
        f = open(file_obj.name, 'wb')
        for line in file_obj.chunks():
            f.write(line)
        f.close()
    return ajax.ajax_template(request, 'index/upload.html', {})