# MLOps-HW

Учебный проект по дисциплине **MLOps**. Репозиторий содержит  задания по работе с инструментами разработки.

Студент: Маслов Денис

## Домашние задания

| № | Тема | Описание | Статус |
|---|---|---|---|
| 1 | Python Project Setup | Настройка uv, Ruff и ty | ✅ |
| 2 | Git Branching | Работа с ветками и Pull Requests | ✅ |
| 3 | Data Version Control (DVC) | Версионирование данных и воспроизводимый пайплайн | ✅ |
|  4|  |  | ☐  |


## Установка

Python 3.12+ и [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/denismaslovv/mlops.git
cd mlops
uv sync
```

## Домашнее задание 3 — DVC

Реализован учебный пайплайн для расчёта количества вещества по массе и молярной массе.

### Пайплайн

```text
generate_data → calculate → summarize
```

| Стадия | Действие | Результат |
|---|---|---|
| `generate_data` | Генерация исходных данных | `data/substances.csv` |
| `calculate` | Расчёт n = m / M | `data/results.csv` |
| `summarize` | Агрегация результатов | `reports/summary.json` |

### Запуск и проверка

```bash
uv run dvc repro
uv run dvc dag
uv run dvc status
uv run dvc metrics show
```

### Хранение данных

Код и метаданные (`dvc.yaml`, `dvc.lock`) хранятся в Git. Артефакты отслеживаются DVC.

Настроен локальный remote `localstorage` вне репозитория.

```bash
uv run dvc push      # Отправка артефактов в remote
uv run dvc pull      # Получение данных из remote
uv run dvc checkout  # Восстановление из локального кэша
```

Проверены создание стадий, отслеживание зависимостей, автоматический пропуск неизменившихся этапов и восстановление данных из кэша и remote.