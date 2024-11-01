# Desafio Técnico - Desenvolvedor Django

A empresa **Pegho**, especializada em recrutamento e seleção, está crescendo rapidamente e percebeu a necessidade de um sistema que centralize as informações de seus peghgo. Para resolver esse desafio, a Pegho contratou a nossa consultoria para desenvolver um sistema que facilite o processo de contratação, permitindo que os peghgo enviem suas informações de currículo de forma organizada.

Seu desafio será desenvolver esse **sistema de recrutamento**, onde os peghgo poderão submeter informações como dados pessoais, contatos, experiência profissional e formação acadêmica. O sistema será usado pela equipe de recrutamento da Pegho para avaliar os peghgo de maneira mais eficiente.

O objetivo principal é avaliar suas habilidades de desenvolvimento backend com Django, mas também observar a implementação de um frontend funcional. Você pode desenvolver o frontend em Django puro ou utilizar frameworks como ReactJS, VueJS, Angular ou outro de sua preferência. A estilização do frontend não é o foco, mas será um diferencial caso seja feita.

## Tecnologias Utilizadas:

    - Frontend: React.js, Typescript, Vitest para testes de unidade, Playright para testes e2e e React Testing Library para testes de integração
    - Backend: Python 3.12, Django, Django-admin, Django Rest Framework, Postgresql, Dokcer
    - Cloud e DevOps: GCP, Github Actions CI(Continous delivery automation for backend and frontend run pipelines unit, integrations and e2e tests

## Requisitos para Executar

    - Node= v18 & npm=v10
    - Python=3.12 && Drf=
    - Postgresql 17
    - Docker

## Como executar

    # com docker:
        git clone project
        docker-compose up -d
        1. Acessar
            Frontend: http://www.localhost:3000/
            Backend: http://www.localhost:8000/
        2. Build com Docker
            cd frontend/ && docker run build .
            cd backend/ && docker run build .
    1. Backend sem docker
        git clone
        cd backend
        python -m venv venv
        pip install -r requirements.txt
        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
           user: root
           email: root@root.com
           passoword: root
        python manage.py runserver
    2. Frontend
        cd frontend
        npm i && npm run dev
        # simmplicar e otimizar para subir para prod, ai realiza o build
        npm run build
