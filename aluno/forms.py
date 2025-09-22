import re
from django.forms import ModelForm
from django import forms
from .models import Aluno, Cidade, Curso


class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = "__all__"
        widgets = {
            "nome_aluno": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome completo do aluno"}
            ),
            "data_nascimento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "cpf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "000.000.000-00",
                    "oninput": "formatCPF(this)",
                }
            ),
            "rg": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "00.000.000-0"}
            ),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "exemplo@email.com"}
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(00) 00000-0000",
                    "oninput": "formatPhone(this)",
                }
            ),
            "emergency_phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "(00) 00000-0000",
                    "oninput": "formatPhone(this)",
                }
            ),
            "endereco": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Rua, Avenida, etc."}
            ),
            "numero_casa": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Número da residência"}
            ),
            "cep": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "00000-000",
                    "oninput": "formatCEP(this)",
                }
            ),
            "cidade": forms.Select(attrs={"class": "form-control"}),
            "numero_matricula": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Número da matrícula"}
            ),
            "curso": forms.Select(attrs={"class": "form-control"}),
            "obs": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Observações sobre o aluno (máximo 500 caracteres)",
                }
            ),
            "turno": forms.Select(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.FileInput(
                attrs={"class": "form-control", "accept": "image/*"}
            ),
        }

        labels = {
            "nome_aluno": "Nome do Aluno",
            "data_nascimento": "Data de Nascimento",
            "cpf": "CPF",
            "rg": "RG",
            "sexo": "Sexo",
            "email": "E-mail",
            "phone": "Telefone",
            "emergency_phone": "Telefone de Emergência",
            "endereco": "Endereço",
            "numero_casa": "Número da Casa",
            "cep": "CEP",
            "cidade": "Cidade",
            "numero_matricula": "Número da Matrícula",
            "curso": "Curso",
            "obs": "Observações",
            "turno": "Turno",
            "status": "Status",
            "foto": "Foto do Aluno",
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if cpf:
            cpf_numbers = re.sub(r"[^\d]", "", cpf)

            if len(cpf_numbers) != 11:
                raise forms.ValidationError("CPF deve ter 11 dígitos.")

            if cpf_numbers == cpf_numbers[0] * 11:
                raise forms.ValidationError("CPF inválido.")

            def validar_cpf(cpf_str):
                soma = sum(int(cpf_str[i]) * (10 - i) for i in range(9))
                primeiro_digito = ((soma * 10) % 11) % 10

                soma = sum(int(cpf_str[i]) * (11 - i) for i in range(10))
                segundo_digito = ((soma * 10) % 11) % 10

                return cpf_str[9:11] == f"{primeiro_digito}{segundo_digito}"

            if not validar_cpf(cpf_numbers):
                raise forms.ValidationError("CPF inválido.")

            return f"{cpf_numbers[:3]}.{cpf_numbers[3:6]}.{cpf_numbers[6:9]}-{cpf_numbers[9:]}"
        return cpf


class CursoForm(ModelForm):

    class Meta:
        model = Curso
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
        }


class CidadeForm(ModelForm):

    class Meta:
        model = Cidade
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "sigla_estado": forms.TextInput(attrs={"class": "form-control"}),
        }
