# Cloud Janitor CLI

A Python-based cloud auditing utility that identifies idle and orphaned infrastructure resources.

## Features

* Environment-based configuration
* Structured logging
* Resource auditing
* Automated report generation
* Unit testing with pytest
* GitHub Actions CI pipeline

## Installation

```bash
git clone <repository-url>
cd cloud-janitor-cli
pip install -r requirements.txt
```

## Configuration

Create a `.env` file:

```env
ENVIRONMENT=development
```

## Run

```bash
python src/main.py
```

## Test

```bash
pytest
```

## Architecture

```text
main.py
    ↓
CloudResource
    ↓
Logger
    ↓
Audit Report
```

## Future Improvements

* AWS boto3 integration
* Azure SDK integration
* Slack notifications
* Email reporting
* Docker support
* Kubernetes deployment

