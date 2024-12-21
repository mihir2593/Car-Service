from django.shortcuts import get_object_or_404
from rest_framework import status
from  rest_framework.response import Response
from rest_framework.decorators import api_view
from storeapi import serializer
from storesapp.models import categorymodel
from storesapp.models import usecategorymodel
from storesapp.models import productmodel
from storesapp.models import storemodel


@api_view(['POST'])
def addcategory(request):
        s = serializer.categoryserializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response("Category data Added Suceesully")
        else:
            print(s.errors)
            return Response("error")



@api_view(['GET'])
def managecategory(request):
        data = categorymodel.objects.all()
        serialize = serializer.categoryserializer   (data, many=True)
        return Response(serialize.data)





@api_view(['POST'])
def updatecategory(request, id):
    item = categorymodel.objects.get(id=id)
    data = serializer.categoryserializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(['POST'])
# def deleteitem(request,id):
#     data = categorymodel.objects.get(id=id)
#     data.delete()
#     return Response("data deleted successfully")


@api_view(['DELETE'])
def deletecategory(request, id):
	item = get_object_or_404(categorymodel, id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)





@api_view(['POST'])
def addusecategory(request):
        s = serializer.usecategoryserializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response("UseCategory data Added Suceesully")
        else:
            print(s.errors)
            return Response("error")

@api_view(['GET'])
def manageusecategory(request):
        data = usecategorymodel.objects.all()
        serialize = serializer.usecategoryserializer(data, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def updateusecategory(request, id):
    item = usecategorymodel.objects.get(id=id)
    data = serializer.usecategoryserializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteusecategory(request, id):
	item = get_object_or_404(usecategorymodel, id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)




@api_view(['POST'])
def addproduct(request):
        s = serializer.productserializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response("Product data Added Suceesully")
        else:
            print(s.errors)
            return Response("error")

@api_view(['GET'])
def manageproduct(request):
        data = productmodel.objects.all()
        serialize = serializer.productserializer(data, many=True)
        return Response(serialize.data)


@api_view(['POST'])
def updateproduct(request, id):
    item = productmodel.objects.get(id=id)
    data = serializer.productserializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteproduct(request, id):
	item = get_object_or_404(productmodel, id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)




@api_view(['POST'])
def addstore(request):
    s = serializer.storeserializer(data=request.data)
    if s.is_valid():
        s.save()
        return Response("store data Added Suceesully")
    else:
        print(s.errors)
        return Response("error")


@api_view(['GET'])
def managestore(request):
    data = storemodel.objects.all()
    serialize = serializer.storeserializer(data, many=True)
    return Response(serialize.data)


@api_view(['POST'])
def updatestore(request, id):
    item = storemodel.objects.get(id=id)
    data = serializer.storeserializer(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deletestore(request, id):
	item = get_object_or_404(storemodel, id=id)
	item.delete()
	return Response(status=status.HTTP_202_ACCEPTED)








