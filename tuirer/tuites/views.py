from django.shortcuts import render
from tuites.models import Tuite

# Create your views here.
def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando formulário')
        content = request.POST.get('content', None)

        if content == '' or content.isspace():      
            context['error'] = 'O campo não pode estar vazio!'
            return render(request, 'post_tuite.html', context)
        else:
            Tuite.objects.create(
                content=content,
                author=request.user,
            )
            content['success_message'] = 'Seu Tuite de conteúdo for enviado!'

    return render(request, 'post_tuite.html', context)


