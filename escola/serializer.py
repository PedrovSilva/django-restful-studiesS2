from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import cpf_invalido, nome_invalido, celular_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = "__all__"

    def validate(self, attrs):
        if cpf_invalido(attrs["cpf"]):
            raise serializers.ValidationError({"cpf":"O cpf deve ter 11 digitos"})
        if nome_invalido(attrs["nome"]):
            raise serializers.ValidationError({"nome":"Nome error"})
        if celular_invalido(attrs["celular"]):
            raise serializers.ValidationError( { "celular":"O celular deve ter 13 digitos"})
        return attrs
    

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"

class ListaMatricularEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()    
    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome =serializers.ReadOnlyField(source = "estudante.nome")
    class Meta:
        model = Matricula
        fields = ["estudante_nome"]

