from django import forms

class FormularioRegistroEmpleados(forms.Form):

    nombre=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Nombre"
    )
    apellido=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
        label="Apellido"
    )
    cargo=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True,
        label="Cargo"
    )
    direccion=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Dirección"
    )
    telefono=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
        label="Telefono"
    )