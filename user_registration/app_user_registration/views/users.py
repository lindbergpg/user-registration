from django.shortcuts import render
from app_user_registration.models import User


def users(request):

    # Salvar os dados da tela para o banco de dados
    new_user = User()
    new_user.user_name = request.POST.get('user_name')
    new_user.user_age = request.POST.get('user_age')
    new_user.save()

    # Exibir todos os usuarios cadastrados em uma nova pagina
    users = {
        'users': User.objects.all()
    }

    # retornar os dados para a pagina de listagem de usuarios
    return render(request, 'users/users.html', users)
