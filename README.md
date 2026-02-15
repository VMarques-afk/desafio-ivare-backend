# API de Vacinação Pet

Backend em **Django + Django REST Framework** para gerenciamento de:

- usuários,
- pets,
- vacinas,
- registros de vacinação,
- veterinários.

1. Visão rápida

- Framework: Django 5.x
- API REST: DRF (ModelViewSet + routers)
- Documentação: drf-spectacular (OpenAPI/Swagger)
- Banco atual: SQLite
- Autenticação: Session + Basic
- Permissão padrão: usuário autenticado

---

2. Como o código está organizado

```text
.
├── app/
│   ├── settings.py      # Configuração global (apps, DRF, DB, auth)
│   └── urls.py          # Rotas principais + docs + inclusão dos apps
├── vacinacao/
│   ├── models.py        # Usuario, Raca, Pet, Vacina, RegistroVacinacao
│   ├── serializers.py   # Transformação model <-> JSON
│   ├── views.py         # Regras da API (queryset, permissões, filtros)
│   └── urls.py          # Rotas REST via DefaultRouter
├── veterinarios/
│   ├── models.py        # Modelo Veterinario
│   ├── serializers.py   # Serializer do veterinário
│   └── views.py         # ViewSet de veterinários
├── manage.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

3. Como o fluxo da API funciona (passo a passo)

Quando uma requisição chega, o fluxo principal é:

1. **`app/urls.py`** recebe a URL e encaminha para o app correto (`vacinacao` ou `veterinarios`).
2. O **router** do DRF resolve a ação (`list`, `create`, `retrieve`, etc.).
3. O **ViewSet** executa regras de negócio:
   - filtra queryset por usuário,
   - define serializer,
   - aplica permissões.
4. O **Serializer** valida dados e converte JSON em objeto Django (ou objeto em JSON).
5. O **Model** persiste no banco.
6. O DRF devolve a resposta HTTP com payload JSON.

Em resumo:
**URL -> Router -> ViewSet -> Serializer -> Model -> Response**.

4. Domínio e regras de negócio

4.1 `vacinacao.models`

- **Usuario**
  - Modelo customizado de autenticação (`AUTH_USER_MODEL = vacinacao.Usuario`).

- **Raca**
  - Cadastro de raças por espécie (`cachorro`, `gato`, `outro`).

- **Pet**
  - Pertence a um dono (`Usuario`).
  - Pode ter raça opcional.

- **Vacina**
  - Catálogo de vacinas com dados de fabricante/lote/estoque.

- **RegistroVacinacao**
  - Liga um `Pet` a uma `Vacina`.
  - `data_aplicacao` é automática (`auto_now_add=True`).

  4.2 `veterinarios.models`

- **Veterinario**
  - Perfil com CRMV (único), telefone e vínculo opcional com usuário.

5. Regras por endpoint (o que realmente acontece no código)

Global (settings DRF)

- Permissão padrão: `IsAuthenticated`
- Autenticação: `SessionAuthentication` e `BasicAuthentication`
- Paginação: `PageNumberPagination`, `PAGE_SIZE = 10`

`UsuarioViewSet`

- CRUD padrão de usuários.

`PetViewSet`
Regras importantes:

- Usuário comum vê **somente os próprios pets**.
- Superusuário vê **todos os pets**.
- Na criação:
  - usuário comum: `dono` é forçado para o usuário autenticado;
  - superusuário: pode informar `dono` livremente.
- Serializer varia por perfil:
  - superusuário: `PetAdminSerializer` (`fields='__all__'`)
  - demais usuários: `PetSerializer` (com campos calculados como `especie_extenso`, `dono_nome`).

`VacinaViewSet`

- CRUD padrão de vacinas.

`RegistroVacinacaoViewSet`

- Usuário comum vê apenas registros de vacinação de pets que são dele.
- Superusuário vê todos os registros.

`VeterinarioViewSet`

- CRUD padrão do modelo de veterinários.

6. Endpoints

Base local: `http://localhost:8000`

API principal

- `GET/POST /api/usuarios/`
- `GET/POST /api/pets/`
- `GET/POST /api/vacinas/`
- `GET/POST /api/registros/`
- `GET/POST /api/veterinarios/`

Auxiliares

- `/admin/` — Django Admin
- `/api-auth/` — login/logout do DRF
- `/api/schema/` — OpenAPI
- `/api/docs/` — Swagger UI

7. Filtros, busca e ordenação

Aplicado em **pets**:

- Filtro: `?especie=` e `?raca=`
- Busca textual: `?search=` (campo `nome`)
- Ordenação: `?ordering=nome` ou `?ordering=id`

Exemplos:

```http
GET /api/pets/?especie=gato
GET /api/pets/?search=mel
GET /api/pets/?ordering=nome
```

8. Exemplos práticos de payload (simples e diretos)

Criar usuário

**POST** `/api/usuarios/`

```json
{
  "username": "alice",
  "email": "alice@email.com",
  "password": "SenhaForte123"
}
```

Criar pet (usuário comum)

**POST** `/api/pets/`

```json
{
  "nome": "Mel",
  "especie": "gato",
  "raca": 1,
  "data_nascimento": "2023-03-10"
}
```

Criar vacina

**POST** `/api/vacinas/`

```json
{
  "nome": "V4",
  "fabricante": "Lab Pet",
  "lote": "L-2026-001",
  "estoque": 120
}
```

Criar registro de vacinação

**POST** `/api/registros/`

````json
{
  "pet": 10,
  "vacina": 5,
  "proxima_dose": "2026-08-15",
  "veterinario_responsavel": "Dra. Mariana Rocha"
}

9) Como executar

Local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````

Acesse: `http://127.0.0.1:8000`

Docker

```bash
docker compose up --build
```

Acesse: `http://localhost:8000`

10. Dicas para entender e evoluir o projeto

1) Comece lendo `app/settings.py` (regras globais da API).
2) Depois `app/urls.py` para entender o mapa de rotas.
3) Em seguida leia `vacinacao/views.py` (principal lógica de negócio por perfil).
4) Valide os contratos em `vacinacao/serializers.py`.
5) Consulte `/api/docs/` para testar os endpoints.

11) Observações importantes

- O projeto está em modo desenvolvimento (`DEBUG=True`, `ALLOWED_HOSTS=['*']`).
- Há dependências de PostgreSQL no `requirements.txt`, mas a configuração ativa atual é SQLite.
- Os arquivos de teste existem, mas ainda sem cenários implementados.
