#from .carro import Carro

def importe_total_carro(request):
    total=0
    #carro = Carro(request)
    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total=total+(float(value["precio"])*value["cantidad"])
    else: return {"importe_total_carro":total}  
   