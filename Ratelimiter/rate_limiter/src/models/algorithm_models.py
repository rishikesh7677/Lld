from rate_limiter.src.models.base_model import BaseModel , models
from rate_limiter.src.constants.models_constants import AlgorithName

class AlgorithTable(BaseModel):
    Algorith_name  = models.CharField(max_length=50,choices=AlgorithName)
    