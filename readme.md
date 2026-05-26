# ☢️ Mutation Testing com Cosmic Ray

Este projeto demonstra como configurar e executar **mutation testing em Python** utilizando o framework **Cosmic Ray**, com foco em avaliar a **qualidade real dos testes automatizados**.

Além disso, o projeto também utiliza **pytest-cov** para análise de:

* cobertura de linhas (line coverage)
* cobertura de branches/decisions (branch coverage)

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
pip install pytest pytest-cov cosmic-ray
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

# 📊 Coverage (Line + Branch Coverage)

## 1. Executar cobertura simples

```bash
PYTHONPATH=. pytest --cov=src
```

---

## 2. Executar cobertura com branches/decisions

```bash
PYTHONPATH=. pytest --cov=src --cov-branch --cov-report=term-missing
```

---

## 3. Gerar relatório HTML

```bash
PYTHONPATH=. pytest --cov=src --cov-branch --cov-report=html
```

Após a execução, abrir:

```bash
htmlcov/index.html
```

---

# 🔍 Interpretação do Coverage

| Métrica | Descrição                        |
| ------- | -------------------------------- |
| Stmts   | Quantidade de instruções         |
| Miss    | Linhas não executadas            |
| Branch  | Quantidade de branches/decisions |
| BrPart  | Branches parcialmente cobertos   |
| Cover   | Percentual de cobertura          |

---

# ☢️ Mutation Testing com Cosmic Ray

## 1. Inicializar sessão

```bash
cosmic-ray init cosmic-ray.conf session.sqlite
```

---

## 2. Executar mutações

```bash
cosmic-ray exec cosmic-ray.conf session.sqlite
```

ou com logs mais detalhados:

```bash
cosmic-ray --verbosity INFO exec cosmic-ray.conf session.sqlite
```

---

## 3. Gerar relatório

```bash
cr-report session.sqlite
```

---

## 4. Gerar relatório detalhado

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

# 📊 Interpretação dos Resultados (Mutation Testing)

| Métrica        | Descrição                        |
| -------------- | -------------------------------- |
| KILLED         | Mutantes detectados pelos testes |
| SURVIVED       | Mutantes não detectados          |
| Mutation Score | Qualidade real dos testes        |

---

# 🎯 Regra prática

## Coverage

* **< 60%** → Cobertura baixa
* **60–80%** → Cobertura razoável
* **> 80%** → Boa cobertura

---

## Mutation Testing

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
* Validar edge cases e boundary values
* Não confiar apenas em coverage; utilizar mutation testing em conjunto

---

# 🧪 Exemplo completo de execução

## Executar testes

```bash
PYTHONPATH=. pytest
```

---

## Executar coverage com branches

```bash
PYTHONPATH=. pytest --cov=src --cov-branch --cov-report=term-missing
```

---

## Inicializar sessão do Cosmic Ray

```bash
cosmic-ray init cosmic-ray.conf session.sqlite
```

---

## Executar mutation testing

```bash
cosmic-ray exec cosmic-ray.conf session.sqlite
```

---

## Gerar relatório

```bash
cr-report session.sqlite
```

---

# 👨‍💻 Autor

Projeto criado para estudo de qualidade de testes utilizando mutation testing com Cosmic Ray.
