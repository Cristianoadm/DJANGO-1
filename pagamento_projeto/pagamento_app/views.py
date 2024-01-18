from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'pagamento_app/index.html')

def process_payment(request):
    if request.method == 'POST':
        numero_cartao = request.POST.get('numero_cartao')
        data_de_expiracao = request.POST.get('data_de_expiracao')
        cvv_do_cartao = request.POST.get('cvv_do_cartao')
        valor = request.POST.get('valor')

        #Processar os dados do pagamento aqui
        #Pode incluir a lógica de interação com um serviço de pagamento

        #Simular uma resposta de pagamento bem sucedido
        response_data = {'Status' : 'Sucesso'}

        return JsonResponse(response_data)
    return JsonResponse({'Status': 'Erro', 'Mensagem':'Método Inválido'})

