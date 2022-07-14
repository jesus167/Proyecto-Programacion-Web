def total_carrito(request):
    total2 = 0
    #if request.user.is_authenticated:
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total2 += int(value["acumulado"])

    return {"total_carrito": total2}

def totalDescuento(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"] * 0.9)

    return {"totalDescuento": total}