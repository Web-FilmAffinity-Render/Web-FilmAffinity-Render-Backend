from rest_framework import generics
from project.movies import serializers, models
from rest_framework.exceptions import ValidationError


class MovieListView(generics.ListCreateAPIView):
    serializer_class = serializers.MovieListSerializer
    queryset = models.Movie.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title')
        plot = self.request.query_params.get('plot')
        min_rate = self.request.query_params.get('min_rate')
        max_rate = self.request.query_params.get('max_rate')
        genre = self.request.query_params.get('genre')

        allowed_params = {'title', 'plot', 'min_rate', 'max_rate','genre'}

        request_params = set(self.request.query_params.keys())
        invalid_params = request_params - allowed_params
        if invalid_params:
            raise ValidationError(f'Parámetros no válidos:{invalid_params}')
        try:
            if min_rate is not None:
                min_rate = float(min_rate)
            if max_rate is not None:
                max_rate = float(max_rate)

        except (ValueError, TypeError) as e:
            raise ValidationError("Los parámetros de consulta deben ser del tipo correcto.")

        if title:
            queryset = queryset.filter(title__icontains=title)
        if plot:
            queryset = queryset.filter(plot__icontains=plot)
        if min_rate and max_rate:
            queryset = queryset.filter(rate__gte=min_rate,
        rate__lte=max_rate)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        return queryset

class MovieView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()
