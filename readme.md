# ☢️ Mutation Testing com Cosmic Ray

Este projeto demonstra como configurar e executar **mutation testing em Python** utilizando o framework **Cosmic Ray**, com foco em avaliar a **qualidade real dos testes automatizados**.

---

# 📦 Requisitos

* Python 3.9 ou superior
* pip
* virtualenv (recomendado)

---

# 🔧 Instalação

## 1. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
# ou
venv\Scripts\activate     # Windows
```

---

## 2. Instalar dependências

```bash
pip install pytest cosmic-ray
```

---

# 🔍 Verificar versão

```bash
python --version
pytest --version
cosmic-ray --version
```

---

# ⚙️ Configuração

## 1. Criar arquivo de configuração

```bash
touch cosmic-ray.conf
```

---

## 2. Conteúdo do `cosmic-ray.conf`

```toml
[cosmic-ray]
module-path = "src"
test-command = "bash -c 'PYTHONPATH=. pytest -q'"
timeout = 10.0
```

---

# 🚀 Execução

## 1. Garantir que os testes estão funcionando

```bash
PYTHONPATH=. pytest
```

---

## 2. Inicializar sessão

```bash
cosmic-ray init cosmic-ray.conf session.sqlite
```

---

## 3. Executar mutações

```bash
cosmic-ray exec cosmic-ray.conf session.sqlite
ou
cosmic-ray --verbosity INFO exec cosmic-ray.conf session.sqlite
```

---

## 4. Gerar relatório

```bash
cr-report session.sqlite
```

---

## 🔍 Relatório detalhado

```bash
cr-report session.sqlite --show-diff --show-output --surviving-only
```

---

# 🛑 Parar execução

Durante a execução:

```bash
CTRL + C
```

---

# 🧹 Limpar sessão

```bash
rm session.sqlite
```

---

# 📊 Interpretação dos Resultados

| Métrica        | Descrição                        |
| -------------- | -------------------------------- |
| KILLED         | Mutantes detectados pelos testes |
| SURVIVED       | Mutantes não detectados          |
| Mutation Score | Qualidade real dos testes        |

---

## 🎯 Regra prática

* **< 60%** → Testes fracos
* **60–80%** → Testes razoáveis
* **> 80%** → Testes bons
* **100%** → Excelente (validar cenários adicionais)

---

# ⚠️ Boas práticas

* Sempre validar os testes com `pytest` antes do mutation testing
* Garantir que não há erros de import
* Evitar incluir arquivos utilitários (ex: `report.py`)
* Focar apenas no código de negócio
* Utilizar casos de teste com cenários positivos e negativos

---

# 🧪 Exemplo completo de execução

```bash
# Executar testes
PYTHONPATH=. pytest

# Inicializar sessão
cosmic-ray init cosmic-ray.conf session.sqlite

# Executar mutações
cosmic-ray exec cosmic-ray.conf session.sqlite

# Gerar relatório
cr-report session.sqlite
```

---

# 🚀 Próximos passos

* Integrar com CI/CD (GitHub Actions)
* Definir threshold mínimo de mutation score
* Gerar relatórios automatizados
* Aplicar mutation testing em APIs e pipelines de dados

---

# 👨‍💻 Autor

Projeto criado para estudo de qualidade de testes utilizando mutation testing com Cosmic Ray.
