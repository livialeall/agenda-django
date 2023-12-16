#usado para ser a primeira coisa a ser executado
#Vou criar modulos e colocar para ser iniciado aqui
#simular que essa pasta views é o arquivo views.py do django

from .contact_views import * #importa da view( funcionalidade ) que eu crirei - importa todas as funções
from .contact_forms import *
from .user_forms import *