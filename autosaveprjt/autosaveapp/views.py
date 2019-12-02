from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from autosaveapp.models import automodel

# Create your views here.
def autoview(request):

    return render(request,'auto.html',)


@csrf_exempt
def autosaveview(request):
    x=request.POST.get('x')
    y=request.POST.get('y')
    z=request.POST.get('z')
    a=request.POST.get('a')
    b=request.POST.get('b')
    c=request.POST.get('c')
    d=request.POST.get('d')
    print(x)
    print(y)
    print(z)
    print(c)
    print(d)
    auto=automodel()
    auto.fname=x
    auto.lname=y
    auto.text=d
    auto.bike=c
    auto.symptoms=z
    auto.save()
    # print(type(form))
    # print(QueryDict(form))
    # print(form)
    print(56467777777777777777777777777777)

    data={
    'hello':'hello'
    }
    return JsonResponse(data)





# $().ready(function(){
#   var timer;
#   var timeout=5;
#   $('#formauto').keyup(function(){
#     if(timer){
#       clearTimeout(timer);
#     }
#     timer = setTimeout(saveData,timeout);
#
#   })
# });
# function saveData(){
#   var patient_id = $('#formauto').val();
#     $.ajax({
#       url:'/autosave/',
#       type: 'GET',
#       'csrfmiddlewaretoken': '{{ csrf_token }}',
#       image:{hello:'patient_id', hi:'hii'},
#       success: function(response){
#         $('#postid').val(response);
#       }
#     });
# }





  # $(document).ready(function(){
  #     function autosave(){
  #       var formdata = $('#formauto').val();
  #       var postid = $('#postid').val();
  #       var formdata = $('formdata').serialize();
  #       if (formdata != '')
  #       {
  #         $.ajax({
  #           url:'autosave/',
  #           method:'GET',
  #           data:{formdata:formdata},
  #           datatype:text,
  #           success:function(data)
  #           {
  #             if (data != '')
  #             {
  #               $('#postid').val(data);
  #             }
  #             $('#autosave').text("post save as data");
  #             setInterval(function(){
  #               $('#autosave').text('');
  #             },20);
  #           }
  #         });
  #       }
  #     }
  #     setInterval(function(){
  #       autosave();
  #     },10);
  # });
