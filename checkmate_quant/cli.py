"""CLI: python -m checkmate_quant.cli summary FILE | compare FILE FILE."""
import argparse
import json
from .ledger import load_ledger
from .metrics import summarize
from .compare import compare_ledgers


def main(argv=None):
    parser = argparse.ArgumentParser(description='Local TradingView export research only; no order execution')
    commands = parser.add_subparsers(dest='command', required=True)
    s = commands.add_parser('summary',help='Descriptive metrics for one CSV')
    s.add_argument('csv')
    s.add_argument('--json',action='store_true')
    c = commands.add_parser('compare',help='Compare normal and stressed TradingView exports')
    c.add_argument('normal')
    c.add_argument('harsh')
    c.add_argument('--json',action='store_true')
    args = parser.parse_args(argv)
    if args.command == 'summary':
        data = summarize(load_ledger(args.csv))
    else:
        data = compare_ledgers(load_ledger(args.normal),load_ledger(args.harsh))
    if args.json:
        print(json.dumps(data,indent=2,sort_keys=True))
    else:
        print('CHECKMATE — LOCAL EXPORT ANALYSIS (NOT VERIFIED LIVE PERFORMANCE)')
        for key, value in data.items():
            print(f'{key}: {value}')


if __name__ == '__main__':
    main()
