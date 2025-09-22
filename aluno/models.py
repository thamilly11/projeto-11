from django.db import models


# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    sigla_estado = models.CharField(max_length=2)

    def __str__(self):
        return self.nome + " - " + self.sigla_estado


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    SEXO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Feminino"),
        ("O", "Outro"),
    ]

    TURNO_CHOICES = [
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    ]

    STATUS_CHOICES = [
        ("A", "Ativo"),
        ("I", "Inativo"),
    ]

    nome_aluno = models.CharField(max_length=150, default="")
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=14, unique=True, default="")
    rg = models.CharField(max_length=12, unique=True, default="")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, verbose_name="Sexo", null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    emergency_phone = models.CharField(max_length=11, blank=True, null=True)
    endereco = models.CharField(max_length=250)
    numero_casa = models.CharField(max_length=10, default="")
    cep = models.CharField(max_length=9, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    numero_matricula = models.CharField(max_length=20, unique=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    obs = models.TextField(blank=True, null=True, max_length=500)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES, verbose_name="Turno", null=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, verbose_name="Status", default="A"
    )
    foto = models.ImageField(upload_to="fotos_alunos/", blank=True, null=True)
