import tempfile
import unittest
from pathlib import Path
from decimal import Decimal
from checkmate_quant.ledger import load_ledger, decimal_of
from checkmate_quant.metrics import summarize
from checkmate_quant.compare import compare_ledgers

ROOT=Path(__file__).resolve().parents[1]

class ExportResearchTests(unittest.TestCase):
    def setUp(self):
        self.normal=load_ledger(ROOT/'examples/synthetic_normal.csv')
        self.harsh=load_ledger(ROOT/'examples/synthetic_harsh.csv')

    def test_exit_first_does_not_double_count(self):
        self.assertEqual(self.normal.row_count,6)
        self.assertEqual(self.normal.entry_count,3)
        self.assertEqual(len(self.normal.exits),3)

    def test_descriptive_metrics(self):
        r=summarize(self.normal)
        self.assertEqual(r['net_pnl_usd'],'25')
        self.assertEqual(r['gross_profitable_legs_usd'],'35')
        self.assertEqual(r['absolute_gross_losing_legs_usd'],'10')
        self.assertEqual(r['profit_factor'],'3.5')
        self.assertEqual(r['max_closed_leg_drawdown_usd'],'10')
        self.assertEqual(r['losing_days_in_export_clock'],1)
        self.assertEqual(r['worst_day_usd'],'-10')

    def test_harsh_comparison(self):
        r=compare_ledgers(self.normal,self.harsh)
        self.assertEqual(r['closed_leg_count_difference'],0)
        self.assertEqual(r['ordinal_identity_mismatches'],0)
        self.assertEqual(r['stress_minus_normal_net_usd'],'-9')

    def test_duplicate_export_identifies_hash(self):
        self.assertTrue(compare_ledgers(self.normal,self.normal)['identical_file_bytes'])

    def test_invalid_numeric_data_rejected(self):
        with self.assertRaises(ValueError):
            decimal_of('not-a-number',field='n')

    def test_differing_leg_records_flagged(self):
        changed=(ROOT/'examples/synthetic_harsh.csv').read_text().replace('2,Exit short,2026-01-02 09:00', '2,Exit short,2026-01-02 09:01')
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'changed.csv'
            p.write_text(changed)
            r=compare_ledgers(self.normal,load_ledger(p))
            self.assertEqual(r['ordinal_identity_mismatches'],1)
            self.assertEqual(r['first_ordinal_identity_mismatch']['ordinal'],2)

if __name__=='__main__':
    unittest.main()
