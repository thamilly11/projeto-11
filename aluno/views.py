from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno, Curso, Cidade
from .forms import AlunoForm, CidadeForm, CursoForm
from datetime import date


def aluno_editar(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES, instance=aluno)

        if form.is_valid():
            form.save()
            return redirect("aluno_listar")
    else:
        form = AlunoForm(instance=aluno)

    return render(request, "aluno/form.html", {"form": form})


def aluno_remover(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    aluno.delete()
    return redirect("aluno_listar")  # procure um url com o nome 'lista_aluno'


def aluno_criar(request):
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AlunoForm()
            return redirect("aluno_listar")
    else:
        form = AlunoForm()

    return render(request, "aluno/form.html", {"form": form})


def aluno_listar(request):
    alunos = Aluno.objects.all()
    context = {"alunos": alunos}
    return render(request, "aluno/alunos.html", context)


def index(request):
    total_alunos = Aluno.objects.count()
    total_cidades = Cidade.objects.count()
    total_curso = Curso.objects.count()
    context = {
        "total_alunos": total_alunos,
        "total_cidades": total_cidades,
        "total_cursos": total_curso,
    }
    return render(request, "aluno/index.html", context)


def aluno_detail(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    context = {
        "aluno": aluno,
    }

    return render(request, "aluno/detalhes.html", context)


def curso_listar(request):
    cursos = Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, "curso/curso_listar.html", context)


def curso_criar(request):
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            form = CursoForm()
            return redirect("curso_listar")
    else:
        form = CursoForm()
    return render(request, "curso/form.html", {"form": form})


def cidade_criar(request):
    if request.method == "POST":
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CidadeForm()
            return redirect("cidade_listar")
    else:
        form = CidadeForm()
    return render(request, "cidade/form.html", {"form": form})


def cidade_editar(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    if request.method == "POST":
        form = CidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            return redirect("cidade_listar")
    else:
        form = CidadeForm(instance=cidade)
    return render(request, "cidade/form.html", {"form": form})


def cidade_listar(request):
    cidades = Cidade.objects.all()
    context = {"cidades": cidades}
    return render(request, "cidade/cidade_listar.html", context)


def cidade_remover(request, id):
    cidade = get_object_or_404(Cidade, id=id)
    cidade.delete()
    return redirect("cidade_listar")
