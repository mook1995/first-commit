from django.shortcuts import render, get_object_or_404
from noticeboard.models import Notice
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
# Create your views here.

def index(request):
    article_list = Notice.objects.all().order_by('-writeDate')
    #이렇게 하면 notice오브젝트안에 있는 모든것을 다 가져온다. orderby 하는데 '-'desc로 writeDate라는 컬럼을 기준으로 정렬
    context = {'article_list':article_list}
    return render(request, 'noticeboard/index.html', context)
##request를 받으면 noticeboard/index.html과 context를 뿌려준다.(context는 딕셔너리 형태로 넘겨준다.)


def write_article(request):
    return render(request, 'noticeboard/writeArticle.html')


def add_article(request):
    notice = Notice()
    notice.title = request.POST['title']
    notice.content = request.POST['content']
    notice.writeID = 'root' #아직 안만들었기 때문에 임의로 넣음
    notice.save()  #장고에서 제공하는 저장 기능
    return HttpResponseRedirect(reverse('noticeboard:index'))
#redirect는 클라이언트에게 정보를 보내는게 아니라 클라이언트가 스스로 이미 받은 정보를 호출하도록 지시하는것으로 볼수 있고
#이때 지시를 하면서 주소를 같이 보내줘야 한다. 이러한 지시를 내리기 위해 필요한것이 reverse이다. 계속
# 쓰고있는 장고의 url language와 같은 기능을
#하는것으로 볼수 있다.(소스를 안바꾸면서도 다른 기능을 하도록한다.)

def view_article(request, article_id):
    notice = get_object_or_404(Notice, pk=article_id) #Notice 에서 article_id가 pk이인 놈들을 불러오는데
    #없으면 get object or 404를 이용해서 NOT FOUND를 출력해주는 것이다.
    return render(request, 'noticeboard/detail.html', {'article':notice})  #넘겨줄떄는 딕셔너리 형태로 넘겨줘야 한다.
#딕셔너리 부분이 사용자로부터 받은 부분임



def update_article(request, article_id):
    notice = Notice.objects.get(id=article_id)
    #get_object_or_404을 쓰지 않은것은 당연히 있는놈을 받아온것이기떄문에 없을리가 없기 떄문이다.
    if request.method == 'POST':
        #주소창에 수동타이핑으로 입력해서 들어온경우를 방지하기 위함
        notice.writeID = request.POST['writer']
        notice.title = request.POST['title']
        #'title'은 name attribite의 값을 말함
        notice.content = request.POST['content']
        notice.writeDate = timezone.datetime.now()
        notice.save()
        return HttpResponseRedirect(reverse('noticeboard:view', args=(article_id,)))
        #파이썬 튜플에서 원소가 하나인경우에는 반드시 콤마를 붙여줘야 튜플로 인식이된다.
    else:
        return render(request, 'noticeboard/detail.html', {'article':notice})



def delete_article(request, article_id):
    notice = Notice.objects.get(id=article_id)
    notice.delete()
    return HttpResponseRedirect(reverse('noticeboard:index'))