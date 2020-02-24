# TSP_denso_qubo

[Quantum Annealing of Vehicle Routing Proble with Time, State and Cappacity][arxiv: denso quantum aneealing for ts-svrp] の実装デモ

## Installation

TBR

### Requirements

詳しくは [pyproject.toml](./pyproject.toml) か [requirements.txt](./requirements.txt) を参照してください
[poetry][python: poetry] を利用することをおすすめしています．

#### dependencies

- python = ^3.7
- pyqubo = ^0.4.0
- openjij = ^0.0.9
- matplotlib = ^3.1.3

#### dev-dependencies

- pytest = ^4.6
- pylint = ^2.4.4
- black = ^19.10b0
- isort[pyproject] = ^4.3.21
- pre-commit = ^2.1.0

Linter: pylint
Foramtter: black

## Usage

TBR

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Reference

- [時間を考慮した VRP の QUBO への定式化][qiita: hideto denso 論文の解説] (Qiita)
- [Quantum Annealing of Vehicle Routing Proble with Time, State and Cappacity][arxiv: denso quantum aneealing for ts-svrp] (arXiv)

<!-- reflence -->

[qiita: hideto denso 論文の解説]: https://qiita.com/snhrhdt/items/9b0d3c7c94df1e4f9ad3
[arxiv: denso quantum aneealing for ts-svrp]: https://arxiv.org/abs/1903.06322
[python: poetry]: https://python-poetry.org/
