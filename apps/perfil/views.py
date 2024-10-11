#O método select_related é usado para pré-carregar os objetos relacionados em um modelo ForeignKey ou OneToOne de uma única consulta ao banco de dados, em vez de executar consultas adicionais para recuperar cada objeto relacionado.

#Por exemplo, se um objeto de modelo A tem uma ForeignKey para um objeto de modelo B e você usa select_related em A, o Django carregará B junto com A em uma única consulta ao banco de dados. Isso é útil quando você precisa acessar as informações de B, mas não deseja executar consultas adicionais para recuperá-las.

#Note que o select_related só funciona com chaves estrangeiras e não funciona com campos ManyToMany.

from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from apps.contas.models import MyUser
from django.contrib.auth.decorators import login_required


@login_required()
def perfil_view(request, username):
    perfil = get_object_or_404(MyUser.objects.select_related('perfil'), username=username)
    context = {'obj': perfil}
    return render(request, 'perfil/perfil.html', context)