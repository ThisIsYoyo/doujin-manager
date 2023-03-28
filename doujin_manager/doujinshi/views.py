from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView, status

from doujinshi.choices import CURRENCY_CHOICES, DOUJIN_LANGUAGE_CHOICES
from doujinshi.models import Author, Circle, Doujinshi
from doujinshi.serializers import AuthorSerializer, CircleSerializer, DoujinshiSerializer


def index(request):
    return HttpResponse("This is doujinshi index")


class IDFilterAPIView(APIView):
    queryset = QuerySet()
    sz_class = serializers.ModelSerializer

    def get(self, request: Request, **kwargs):
        id = kwargs.get("id", 0)

        if not self.queryset.filter(id=id).exists():
            return Response(
                f"{self.queryset.model.__name__} with id:`{id}` not exist", status=status.HTTP_404_NOT_FOUND
            )

        model_id = self.queryset.get(id=id)
        sz = self.sz_class(model_id)
        return Response(sz.data, status=status.HTTP_200_OK)

    def post(self, request: Request, **kwargs):
        id = kwargs.get("id", 0)

        if not self.queryset.filter(id=id).exists():
            return Response(
                f"{self.queryset.model.__name__} with id:`{id}` not exist", status=status.HTTP_404_NOT_FOUND
            )

        model_id = self.queryset.get(id=id)
        model_field_name_list = [f.name for f in model_id.__class__._meta.fields]
        modified_data = request.data
        with transaction.atomic():
            for modified_f, v in modified_data.items():
                if modified_f not in model_field_name_list:
                    return Response(
                        f"{model_id.__class__.__name__} not contain `{modified_f}` field",
                        status=status.HTTP_403_FORBIDDEN,
                    )

                setattr(model_id, modified_f, v)
            model_id.save()

        return Response(self.sz_class(model_id).data, status=status.HTTP_200_OK)


class CreateAPIView(APIView):
    sz_class = serializers.ModelSerializer

    def post(self, request: Request):
        save_data = request.data.get("data", {})

        sz = self.sz_class(data=save_data)
        if sz.is_valid():
            sz.save()
            return Response({"save data": sz.data, "save status": "success"}, status=status.HTTP_201_CREATED)
        return Response(sz.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 50


class FilterListAPIView(ListAPIView):
    paginator_class = ListPagination
    queryset = QuerySet()
    serializer_class = serializers.ModelSerializer


# -------------- Circle --------------
class CircleGETView(IDFilterAPIView):
    queryset = Circle.objects.all()
    sz_class = CircleSerializer


class CircleCreateView(CreateAPIView):
    sz_class = CircleSerializer


class CircleListView(FilterListAPIView):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer


# -------------- Author --------------
class AuthorGETView(IDFilterAPIView):
    queryset = Author.objects.all()
    sz_class = AuthorSerializer


class AuthorCreateView(CreateAPIView):
    sz_class = AuthorSerializer


class AuthorListView(FilterListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# -------------- Doujinshi --------------
class DoujinshiGETView(IDFilterAPIView):
    queryset = Doujinshi.objects.all()
    sz_class = DoujinshiSerializer


class DoujinshiCreateView(CreateAPIView):
    sz_class = DoujinshiSerializer


class DoujinshiListView(FilterListAPIView):
    queryset = Doujinshi.objects.all()
    serializer_class = DoujinshiSerializer


# -------------- Choices --------------
def choices_to_list(choices: tuple) -> list[dict]:
    return [{"name": name, "value": value} for value, name in choices]


@api_view(["GET"])
def choice_view(request: Request):
    return Response(
        {
            "DOUJIN_LANGUAGE_CHOICES": choices_to_list(DOUJIN_LANGUAGE_CHOICES),
            "CURRENCY_CHOICES": choices_to_list(CURRENCY_CHOICES),
        },
        status=status.HTTP_200_OK,
    )
