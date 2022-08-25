def normalize_path_params(cidade=None,estrelas_min=0,estrelas_max=5,diaria_min=0,diaria_max=10000,limit=50,offset=0, **dados):
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': 50,
            'offset': 0
            }
  
    return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'limit': 50,
            'offset': 0,
            }


